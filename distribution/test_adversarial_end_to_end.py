#!/usr/bin/env python3
"""Adversarial end-to-end tests for TEBDLC controlled distribution v0.1."""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from authentication import derive_verifier
from controlled_delivery import controlled_deliver
from audit_log import append_event, verify_chain

NOW = datetime(2026, 8, 20, 15, 0, tzinfo=timezone.utc)
SECRET = "adversarial-secret"
SALT = base64.urlsafe_b64encode(b"0123456789abcdef").decode("ascii")
VERIFIER = derive_verifier(SECRET, SALT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def registry(country="CA", subdivision="QC", city="Montréal"):
    return {
        "schema": "tebdlc-auth-registry/0.1",
        "registry_version": "adversarial-test",
        "accounts": [{
            "subject_id": "subject_adv",
            "status": "ACTIVE",
            "declared_territory": {
                "country_code": country,
                "subdivision_code": subdivision,
                "city": city,
            },
            "credentials": [{
                "credential_id": "cred_adv",
                "status": "ACTIVE",
                "not_before": None,
                "expires_at": None,
                "revoked_at": None,
                "auth": {
                    "algorithm": "PBKDF2-HMAC-SHA256",
                    "iterations": 310000,
                    "salt": SALT,
                    "verifier": VERIFIER,
                },
            }],
        }],
    }


def records(package_hash: str, state="PRIVILEGED"):
    manifest = {
        "manifest_version": "0.1",
        "release_id": "v0.1.0-alpha",
        "source_commits": ["a" * 40],
        "package_sha256": package_hash,
        "assembly_procedure_version": "0.1",
        "licence_version": "0.1",
        "licence_sha256": "b" * 64,
        "territorial_policy_version": "0.1",
        "territorial_policy_sha256": "c" * 64,
        "verification_record_sha256": "d" * 64,
        "created_at": NOW.isoformat(),
    }
    acceptance = {
        "acceptance_id": "accept-0001",
        "authorization_identity": "subject_adv",
        "declared_territory": "declared-test-territory",
        "territorial_state": state,
        "licence_version": "0.1",
        "licence_sha256": "b" * 64,
        "territorial_policy_version": "0.1",
        "territorial_policy_sha256": "c" * 64,
        "tebdlc_release": "v0.1.0-alpha",
        "package_sha256": package_hash,
        "accepted_at": NOW.isoformat(),
        "acceptance_mechanism_version": "0.1",
    }
    return manifest, acceptance


def run_delivery(tmp: Path, reg, manifest, acceptance, secret=SECRET):
    package = tmp / "package.bin"
    if not package.exists():
        package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
    output = tmp / "out"
    return controlled_deliver(
        registry=reg,
        credential_id="cred_adv",
        presented_secret=secret,
        package_path=package,
        release_manifest=manifest,
        licence_acceptance=acceptance,
        output_directory=output,
        now=NOW,
    )


def test_valid_privileged_delivery():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        package = tmp / "package.bin"
        package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes()))
        result = run_delivery(tmp, registry(), m, a)
        assert result["decision"] == "ALLOW"
        assert (tmp / "out" / "package.bin").read_bytes() == package.read_bytes()


def test_wrong_secret_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes()))
        assert run_delivery(tmp, registry(), m, a, "wrong")["decision"] == "DENY"


def test_restricted_territory_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes()), "RESTRICTED")
        assert run_delivery(tmp, registry("IL", None, None), m, a)["decision"] == "DENY"


def test_neutral_state_mismatch_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes()), "PRIVILEGED")
        r = run_delivery(tmp, registry("JM", None, None), m, a)
        assert r["decision"] == "DENY" and r["reason_code"] == "DENY_ACCEPTANCE_TERRITORY_MISMATCH"


def test_acceptance_identity_substitution_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes())); a["authorization_identity"] = "other-subject"
        assert run_delivery(tmp, registry(), m, a)["reason_code"] == "DENY_ACCEPTANCE_IDENTITY_MISMATCH"


def test_release_substitution_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes())); a["tebdlc_release"] = "v9.9.9"
        assert run_delivery(tmp, registry(), m, a)["reason_code"] == "DENY_RELEASE_MISMATCH"


def test_package_tamper_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"ORIGINAL")
        m, a = records(sha(package.read_bytes()))
        package.write_bytes(b"TAMPERED")
        assert run_delivery(tmp, registry(), m, a)["reason_code"] == "DENY_PACKAGE_HASH_MISMATCH"


def test_policy_hash_substitution_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes())); a["territorial_policy_sha256"] = "e" * 64
        assert run_delivery(tmp, registry(), m, a)["reason_code"] == "DENY_POLICY_INTEGRITY_FAILURE"


def test_licence_hash_substitution_denied():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); package = tmp / "package.bin"; package.write_bytes(b"TEBDLC-CONTROLLED-PACKAGE")
        m, a = records(sha(package.read_bytes())); a["licence_sha256"] = "f" * 64
        assert run_delivery(tmp, registry(), m, a)["reason_code"] == "DENY_LICENCE_INTEGRITY_FAILURE"


def test_audit_tampering_detected_and_blocks_append():
    with tempfile.TemporaryDirectory() as d:
        log = Path(d) / "audit.jsonl"
        append_event(log, {"decision": "ALLOW", "event_id": "one"}, now=NOW)
        append_event(log, {"decision": "DENY", "event_id": "two"}, now=NOW)
        lines = log.read_text(encoding="utf-8").splitlines()
        first = json.loads(lines[0]); first["event"]["decision"] = "DENY"
        lines[0] = json.dumps(first, sort_keys=True, separators=(",", ":"))
        log.write_text("\n".join(lines) + "\n", encoding="utf-8")
        assert verify_chain(log)["valid"] is False
        try:
            append_event(log, {"decision": "ALLOW", "event_id": "three"}, now=NOW)
        except ValueError:
            pass
        else:
            raise AssertionError("tampered chain accepted append")


def test_audit_secret_field_rejected():
    with tempfile.TemporaryDirectory() as d:
        try:
            append_event(Path(d) / "audit.jsonl", {"secret": "must-not-persist"}, now=NOW)
        except ValueError:
            pass
        else:
            raise AssertionError("secret-bearing event accepted")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
    print(f"adversarial end-to-end tests: PASS ({len(tests)})")
