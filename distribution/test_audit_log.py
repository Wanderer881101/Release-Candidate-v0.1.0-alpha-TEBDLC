#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
from __future__ import annotations

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from audit_log import append_event, verify_chain, GENESIS

NOW = datetime(2026, 8, 20, 15, 30, tzinfo=timezone.utc)


def test_empty_log_is_valid_genesis():
    with tempfile.TemporaryDirectory() as td:
        result = verify_chain(Path(td) / "audit.jsonl")
        assert result == {"valid": True, "entries": 0, "head_hash": GENESIS}


def test_append_and_verify_two_entries():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "audit.jsonl"
        one = append_event(p, {"decision": "ALLOW", "event_id": "evt-1"}, now=NOW)
        two = append_event(p, {"decision": "DENY", "event_id": "evt-2"}, now=NOW)
        assert one["sequence"] == 1
        assert two["sequence"] == 2
        assert two["previous_hash"] == one["entry_hash"]
        result = verify_chain(p)
        assert result["valid"] is True and result["entries"] == 2
        assert result["head_hash"] == two["entry_hash"]


def test_tampered_event_is_detected():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "audit.jsonl"
        append_event(p, {"decision": "ALLOW", "event_id": "evt-1"}, now=NOW)
        rows = p.read_text(encoding="utf-8").splitlines()
        obj = json.loads(rows[0])
        obj["event"]["decision"] = "DENY"
        p.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
        result = verify_chain(p)
        assert result["valid"] is False and result["reason"] == "ENTRY_HASH_MISMATCH"


def test_deleted_middle_entry_breaks_sequence_or_link():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "audit.jsonl"
        append_event(p, {"event_id": "1"}, now=NOW)
        append_event(p, {"event_id": "2"}, now=NOW)
        append_event(p, {"event_id": "3"}, now=NOW)
        rows = p.read_text(encoding="utf-8").splitlines()
        p.write_text(rows[0] + "\n" + rows[2] + "\n", encoding="utf-8")
        result = verify_chain(p)
        assert result["valid"] is False
        assert result["reason"] in {"SEQUENCE_MISMATCH", "PREVIOUS_HASH_MISMATCH"}


def test_forbidden_secret_field_rejected():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "audit.jsonl"
        try:
            append_event(p, {"event_id": "1", "presented_secret": "nope"}, now=NOW)
            raise AssertionError("secret-bearing event should be rejected")
        except ValueError:
            pass


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
    print(f"audit log tests: PASS ({len(tests)})")
