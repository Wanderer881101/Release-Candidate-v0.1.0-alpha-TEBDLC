#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
"""TEBDLC controlled-distribution record validator v0.1.

Stdlib-only validator for the v0.1 licence-acceptance, distribution-event,
and release-manifest contracts. It intentionally fails closed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
SHA1_RE = re.compile(r"^[a-f0-9]{40}$")
STATES = {"PRIVILEGED", "NEUTRAL", "RESTRICTED"}
ACTIONS = {"READ_SOURCE", "BUILD", "EXECUTE", "TEST", "BENCHMARK", "PRIVATE_MODIFY", "FALSIFY", "DELIVER_PACKAGE"}
REASONS = {
    "ALLOW_PRIVILEGED", "ALLOW_NEUTRAL", "DENY_RESTRICTED_TERRITORY",
    "DENY_UNRESOLVED_TERRITORY", "DENY_NO_LICENCE_ACCEPTANCE",
    "DENY_LICENCE_VERSION_MISMATCH", "DENY_PACKAGE_HASH_MISMATCH",
    "DENY_RIGHT_NOT_GRANTED", "DENY_AUTHENTICATION_FAILURE",
    "DENY_POLICY_INTEGRITY_FAILURE",
}

class ValidationError(ValueError):
    pass

def req(obj: dict, *names: str) -> None:
    missing = [n for n in names if n not in obj]
    if missing:
        raise ValidationError("missing required field(s): " + ", ".join(missing))

def exact_keys(obj: dict, allowed: set[str]) -> None:
    extra = sorted(set(obj) - allowed)
    if extra:
        raise ValidationError("unexpected field(s): " + ", ".join(extra))

def nonempty(value, name: str, min_len: int = 1, max_len: int = 256) -> None:
    if not isinstance(value, str) or not (min_len <= len(value) <= max_len):
        raise ValidationError(f"{name}: invalid non-empty string")

def sha256(value, name: str) -> None:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValidationError(f"{name}: expected lowercase SHA-256")

def iso_time(value, name: str) -> None:
    if not isinstance(value, str):
        raise ValidationError(f"{name}: expected RFC3339/ISO-8601 timestamp")
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"{name}: invalid timestamp") from exc

def validate_acceptance(o: dict) -> None:
    allowed = {
        "acceptance_id","authorization_identity","declared_territory","territorial_state",
        "licence_version","licence_sha256","territorial_policy_version","territorial_policy_sha256",
        "tebdlc_release","package_sha256","accepted_at","acceptance_mechanism_version",
    }
    exact_keys(o, allowed)
    req(o, *allowed)
    nonempty(o["acceptance_id"], "acceptance_id", 8, 128)
    nonempty(o["authorization_identity"], "authorization_identity")
    nonempty(o["declared_territory"], "declared_territory")
    if o["territorial_state"] not in STATES:
        raise ValidationError("territorial_state: invalid state")
    if o["territorial_state"] == "RESTRICTED":
        raise ValidationError("a RESTRICTED recipient cannot hold a controlled-source acceptance record")
    if o["licence_version"] != "0.1" or o["territorial_policy_version"] != "0.1":
        raise ValidationError("unsupported licence/policy version")
    sha256(o["licence_sha256"], "licence_sha256")
    sha256(o["territorial_policy_sha256"], "territorial_policy_sha256")
    sha256(o["package_sha256"], "package_sha256")
    nonempty(o["tebdlc_release"], "tebdlc_release", 1, 128)
    iso_time(o["accepted_at"], "accepted_at")
    nonempty(o["acceptance_mechanism_version"], "acceptance_mechanism_version", 1, 64)

def validate_event(o: dict) -> None:
    required = {
        "event_id","authorization_identity","declared_territory","territorial_state","policy_version",
        "policy_sha256","licence_version","licence_sha256","tebdlc_release","package_sha256",
        "requested_action","decision","reason_code","timestamp","authorization_engine_version",
    }
    allowed = required | {"acceptance_id"}
    exact_keys(o, allowed)
    req(o, *required)
    nonempty(o["event_id"], "event_id", 8, 128)
    nonempty(o["authorization_identity"], "authorization_identity")
    nonempty(o["declared_territory"], "declared_territory")
    if o["territorial_state"] not in STATES:
        raise ValidationError("territorial_state: invalid state")
    if o["policy_version"] != "0.1" or o["licence_version"] != "0.1":
        raise ValidationError("unsupported licence/policy version")
    sha256(o["policy_sha256"], "policy_sha256")
    sha256(o["licence_sha256"], "licence_sha256")
    sha256(o["package_sha256"], "package_sha256")
    if o["requested_action"] not in ACTIONS:
        raise ValidationError("requested_action: invalid action")
    if o["decision"] not in {"ALLOW", "DENY"}:
        raise ValidationError("decision: invalid decision")
    if o["reason_code"] not in REASONS:
        raise ValidationError("reason_code: invalid reason")
    if o["decision"] == "ALLOW" and not o.get("acceptance_id"):
        raise ValidationError("ALLOW requires acceptance_id")
    if o["territorial_state"] == "RESTRICTED" and o["decision"] != "DENY":
        raise ValidationError("RESTRICTED must DENY")
    if o["territorial_state"] == "NEUTRAL" and o["requested_action"] == "FALSIFY":
        if o["decision"] != "DENY" or o["reason_code"] != "DENY_RIGHT_NOT_GRANTED":
            raise ValidationError("NEUTRAL falsification must be denied with DENY_RIGHT_NOT_GRANTED")
    if o["decision"] == "ALLOW":
        expected = "ALLOW_PRIVILEGED" if o["territorial_state"] == "PRIVILEGED" else "ALLOW_NEUTRAL"
        if o["reason_code"] != expected:
            raise ValidationError(f"ALLOW reason must be {expected}")
    nonempty(o["tebdlc_release"], "tebdlc_release", 1, 128)
    iso_time(o["timestamp"], "timestamp")
    nonempty(o["authorization_engine_version"], "authorization_engine_version", 1, 64)

def validate_manifest(o: dict) -> None:
    allowed = {
        "manifest_version","release_id","source_commits","package_sha256","assembly_procedure_version",
        "licence_version","licence_sha256","territorial_policy_version","territorial_policy_sha256",
        "verification_record_sha256","created_at",
    }
    exact_keys(o, allowed)
    req(o, *allowed)
    if o["manifest_version"] != "0.1" or o["licence_version"] != "0.1" or o["territorial_policy_version"] != "0.1":
        raise ValidationError("unsupported manifest/licence/policy version")
    nonempty(o["release_id"], "release_id", 1, 128)
    commits = o["source_commits"]
    if not isinstance(commits, list) or not commits or len(set(commits)) != len(commits):
        raise ValidationError("source_commits must be a non-empty unique array")
    if any(not isinstance(c, str) or not SHA1_RE.fullmatch(c) for c in commits):
        raise ValidationError("source_commits contains invalid Git commit SHA")
    for k in ("package_sha256","licence_sha256","territorial_policy_sha256","verification_record_sha256"):
        sha256(o[k], k)
    nonempty(o["assembly_procedure_version"], "assembly_procedure_version", 1, 64)
    iso_time(o["created_at"], "created_at")

VALIDATORS = {"acceptance": validate_acceptance, "event": validate_event, "manifest": validate_manifest}

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("kind", choices=VALIDATORS)
    p.add_argument("file", type=Path)
    args = p.parse_args()
    try:
        obj = json.loads(args.file.read_text(encoding="utf-8"))
        if not isinstance(obj, dict):
            raise ValidationError("top-level JSON value must be an object")
        VALIDATORS[args.kind](obj)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"DENY: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: {args.kind} record valid")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
