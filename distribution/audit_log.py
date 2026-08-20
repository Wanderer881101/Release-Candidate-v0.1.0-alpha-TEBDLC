#!/usr/bin/env python3
"""Append-only hash-chained audit log for TEBDLC controlled distribution v0.1."""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

AUDIT_VERSION = "tebdlc-audit-chain/0.1"
GENESIS = "0" * 64


def _canonical(obj: dict[str, Any]) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _entry_hash(entry_without_hash: dict[str, Any]) -> str:
    return hashlib.sha256(_canonical(entry_without_hash)).hexdigest()


def append_event(path: str | os.PathLike[str], event: dict[str, Any], *, now: datetime | None = None) -> dict[str, Any]:
    """Append one audit event and return the stored chained entry.

    The caller-provided event is embedded as data. Raw secrets/tokens must never be passed.
    """
    if not isinstance(event, dict):
        raise ValueError("event must be an object")
    forbidden = {"presented_secret", "password", "secret", "token", "raw_token", "private_key"}
    if forbidden.intersection(event.keys()):
        raise ValueError("event contains forbidden secret-bearing field")

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    prev_hash = GENESIS
    sequence = 1

    if p.exists():
        lines = [line for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
        if lines:
            last = json.loads(lines[-1])
            if not isinstance(last, dict) or not isinstance(last.get("entry_hash"), str):
                raise ValueError("existing audit log tail is malformed")
            prev_hash = last["entry_hash"]
            sequence = int(last.get("sequence", 0)) + 1

    timestamp = (now or datetime.now(timezone.utc)).astimezone(timezone.utc).isoformat()
    body = {
        "audit_version": AUDIT_VERSION,
        "sequence": sequence,
        "timestamp": timestamp,
        "previous_hash": prev_hash,
        "event": event,
    }
    stored = dict(body)
    stored["entry_hash"] = _entry_hash(body)

    # Append exactly one canonical JSON line and fsync for best-effort persistence.
    with p.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(stored, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n")
        fh.flush()
        os.fsync(fh.fileno())
    return stored


def verify_chain(path: str | os.PathLike[str]) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {"valid": True, "entries": 0, "head_hash": GENESIS}

    previous = GENESIS
    expected_sequence = 1
    count = 0
    for raw in p.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        try:
            entry = json.loads(raw)
        except json.JSONDecodeError:
            return {"valid": False, "reason": "MALFORMED_JSON", "entries": count}
        if not isinstance(entry, dict):
            return {"valid": False, "reason": "MALFORMED_ENTRY", "entries": count}
        if entry.get("audit_version") != AUDIT_VERSION:
            return {"valid": False, "reason": "AUDIT_VERSION_MISMATCH", "entries": count}
        if entry.get("sequence") != expected_sequence:
            return {"valid": False, "reason": "SEQUENCE_MISMATCH", "entries": count}
        if entry.get("previous_hash") != previous:
            return {"valid": False, "reason": "PREVIOUS_HASH_MISMATCH", "entries": count}
        stored_hash = entry.get("entry_hash")
        if not isinstance(stored_hash, str) or len(stored_hash) != 64:
            return {"valid": False, "reason": "ENTRY_HASH_INVALID", "entries": count}
        body = {k: entry[k] for k in ("audit_version", "sequence", "timestamp", "previous_hash", "event") if k in entry}
        calculated = _entry_hash(body)
        if calculated != stored_hash:
            return {"valid": False, "reason": "ENTRY_HASH_MISMATCH", "entries": count}
        previous = stored_hash
        expected_sequence += 1
        count += 1

    return {"valid": True, "entries": count, "head_hash": previous}
