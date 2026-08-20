#!/usr/bin/env python3
"""Adversarial tests for TEBDLC controlled distribution v0.1.

Tests are confined to the TEBDLC reference authorization/delivery implementation.
They exercise fail-closed behavior and integrity bindings; they do not target third-party systems.
"""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from authentication import derive_verifier
from authorize_request import authorize
from controlled_delivery import controlled_deliver
from audit_chain import append_event, verify_chain

NOW = datetime(2026, 8, 20, 15, 0, tzinfo=timezone.utc)
SECRET = "adversarial-secret"
SALT = base64.urlsafe_b64encode(b"abcdefghijklmnop").decode("ascii")
VERIFIER = derive_verifier(SECRET, SALT)
HEX_A = "a" * 64
HEX_B = "b" * 64
COMMIT = "1" * 40


def registry(country="CA", subdivision="QC", city="Montréal", status="ACTIVE"):
    return {
        "schema": "tebdlc-auth-registry/0.1",
        "registry_version": "adversarial-test",
        "accounts": [{
            "subject_id": "subject_adv",
            "status": status,
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


def manifest(package_sha: str):
    return {
        "manifest_version": "0.1",
        "release_id": "v0.1.0-alpha",
        "source_commits": [COMMIT],
        "package_sha256": package_sha,
        "assembly_procedure_version": "assembly/0.1",
        "licence_version": "0.1",
        "licence_sha256": HEX_A,
        "territorial_policy_version": "0.1",
        "territorial_policy_sha256": HEX_B,
        "verification_record_sha256": "c" * 64,
        "created_at": NOW.isoformat(),
    }


def acceptance(package_sha: str, state="PRIVILEGED", subject="subject_adv"):
    return {
        "acceptance_id": "accept-adv-0001",
        "authorization_identity": subject,
        "declared_territory": "CA-QC Montréal",
        "territorial_state": state,
        "licence_version": "0.1",
        "licence_sha256": HEX_A,
        "territorial_policy_version": "0.1",
        "territorial_policy_sha256": HEX_B,
        "tebdlc_release": "v0.1.0-alpha",
        "package_sha256": package_sha,
        "accepted_at": NOW.isoformat(),
        "acceptance_mechanism_version": "acceptance/0.1",
    }


def make_package(root: Path, payload: bytes = b"controlled-package\n") -> tuple[Path, str]:
    p = root / "tebdlc-v0.1.0-alpha.pkg"
    p.write_bytes(payload)
    return p, hashlib.sha256(payload).hexdigest()


def deliver_with(tmp: Path, reg=None, man=None, acc=None, secret=SECRET):
    package, actual_hash = make_package(tmp)
    man = man or manifest(actual_hash)
    acc = acc or acceptance(actual_hash)
    out = tmp / "out"
    result = controlled_deliver(
        registry=reg or registry(),
        credential_id="cred_adv",
        presented_secret=secret,
        package_path=package,
        release_manifest=man,
        licence_acceptance=acc,
        output_directory=out,
        now=NOW,
    )
    return result, package, out, actual_hash


def test_baseline_privileged_delivery_allows():
    with tempfile.TemporaryDirectory() as td:
        result, package, out, _ = deliver_with(Path(td))
        assert result["decision"] == "ALLOW"
        assert (out / package.name).is_file()


def test_wrong_secret_cannot_reach_delivery():
    with tempfile.TemporaryDirectory() as td:
        result, _, _, _ = deliver_with(Path(td), secret="wrong")
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_AUTHENTICATION_FAILURE"


def test_restricted_territory_cannot_download():
    with tempfile.TemporaryDirectory() as td:
        result, _, _, _ = deliver_with(Path(td), reg=registry("IL", None, None))
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_RESTRICTED_TERRITORY"


def test_ottawa_explicit_restriction_cannot_download():
    with tempfile.TemporaryDirectory() as td:
        result, _, _, _ = deliver_with(Path(td), reg=registry("CA", "ON", "Ottawa"))
        assert result["decision"] == "DENY"


def test_neutral_can_download_but_cannot_falsify():
    reg = registry("JM", None, None)
    authz_download = authorize(reg, "cred_adv", SECRET, "DOWNLOAD_PACKAGE", NOW)
    authz_falsify = authorize(reg, "cred_adv", SECRET, "FALSIFY", NOW)
    assert authz_download["decision"] == "ALLOW" and authz_download["territorial_state"] == "NEUTRAL"
    assert authz_falsify["decision"] == "DENY" and authz_falsify["reason_code"] == "DENY_RIGHT_NOT_GRANTED"


def test_acceptance_identity_swap_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        acc = acceptance(h, subject="different-subject")
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=manifest(h), licence_acceptance=acc,
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_ACCEPTANCE_IDENTITY_MISMATCH"


def test_acceptance_territory_promotion_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        acc = acceptance(h, state="PRIVILEGED")
        result = controlled_deliver(registry=registry("JM", None, None), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=manifest(h), licence_acceptance=acc,
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_ACCEPTANCE_TERRITORY_MISMATCH"


def test_release_replay_against_different_release_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        man = manifest(h)
        man["release_id"] = "v0.1.1"
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=man, licence_acceptance=acceptance(h),
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_RELEASE_MISMATCH"


def test_package_hash_swap_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        man = manifest("d" * 64)
        acc = acceptance("d" * 64)
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=man, licence_acceptance=acc,
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_PACKAGE_HASH_MISMATCH"


def test_policy_hash_swap_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        acc = acceptance(h)
        acc["territorial_policy_sha256"] = "e" * 64
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=manifest(h), licence_acceptance=acc,
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_POLICY_INTEGRITY_FAILURE"


def test_licence_hash_swap_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        acc = acceptance(h)
        acc["licence_sha256"] = "f" * 64
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=manifest(h), licence_acceptance=acc,
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_LICENCE_INTEGRITY_FAILURE"


def test_source_symlink_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        real, h = make_package(root)
        link = root / "link.pkg"
        try:
            link.symlink_to(real)
        except (OSError, NotImplementedError):
            return
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=link, release_manifest=manifest(h), licence_acceptance=acceptance(h),
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_PACKAGE_UNAVAILABLE"


def test_source_destination_collapse_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=manifest(h), licence_acceptance=acceptance(h),
                                    output_directory=root, now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_PATH_INTEGRITY_FAILURE"


def test_missing_acceptance_field_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        acc = acceptance(h)
        del acc["package_sha256"]
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=manifest(h), licence_acceptance=acc,
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_NO_LICENCE_ACCEPTANCE"


def test_missing_manifest_field_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        package, h = make_package(root)
        man = manifest(h)
        del man["verification_record_sha256"]
        result = controlled_deliver(registry=registry(), credential_id="cred_adv", presented_secret=SECRET,
                                    package_path=package, release_manifest=man, licence_acceptance=acceptance(h),
                                    output_directory=root / "out", now=NOW)
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_MANIFEST_INTEGRITY_FAILURE"


def test_audit_chain_detects_tampering():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "audit.jsonl"
        append_event(p, {"decision": "DENY", "reason_code": "X", "timestamp": NOW.isoformat()})
        append_event(p, {"decision": "ALLOW", "reason_code": "Y", "timestamp": NOW.isoformat()})
        assert verify_chain(p)["valid"] is True
        lines = p.read_text(encoding="utf-8").splitlines()
        obj = json.loads(lines[0])
        obj["event"]["reason_code"] = "TAMPERED"
        lines[0] = json.dumps(obj, sort_keys=True, separators=(",", ":"))
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        assert verify_chain(p)["valid"] is False


def test_audit_chain_detects_deletion():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "audit.jsonl"
        append_event(p, {"decision": "DENY", "reason_code": "A", "timestamp": NOW.isoformat()})
        append_event(p, {"decision": "DENY", "reason_code": "B", "timestamp": NOW.isoformat()})
        append_event(p, {"decision": "ALLOW", "reason_code": "C", "timestamp": NOW.isoformat()})
        lines = p.read_text(encoding="utf-8").splitlines()
        p.write_text("\n".join([lines[0], lines[2]]) + "\n", encoding="utf-8")
        assert verify_chain(p)["valid"] is False


def test_registry_subject_duplication_fails_closed():
    reg = registry()
    reg["accounts"].append(copy.deepcopy(reg["accounts"][0]))
    result = authorize(reg, "cred_adv", SECRET, "DOWNLOAD_PACKAGE", NOW)
    assert result["decision"] == "DENY"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
    print(f"adversarial distribution tests: PASS ({len(tests)})")
