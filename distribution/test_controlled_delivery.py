#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
from __future__ import annotations

import base64
import hashlib
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from authentication import derive_verifier
from controlled_delivery import controlled_deliver

NOW = datetime(2026, 8, 20, 15, 0, tzinfo=timezone.utc)
SECRET = "delivery-secret"
SALT = base64.urlsafe_b64encode(b"abcdefghijklmnop").decode("ascii")
VERIFIER = derive_verifier(SECRET, SALT)
HEX_A = "a" * 64
HEX_B = "b" * 64


def make_registry(country="CA", subdivision="QC", city="Montréal"):
    return {
        "schema": "tebdlc-auth-registry/0.1",
        "registry_version": "delivery-test",
        "accounts": [{
            "subject_id": "subject_delivery",
            "status": "ACTIVE",
            "declared_territory": {
                "country_code": country,
                "subdivision_code": subdivision,
                "city": city,
            },
            "credentials": [{
                "credential_id": "cred_delivery",
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
        "source_commits": ["1" * 40],
        "package_sha256": package_hash,
        "assembly_procedure_version": "0.1",
        "licence_version": "0.1",
        "licence_sha256": HEX_A,
        "territorial_policy_version": "0.1",
        "territorial_policy_sha256": HEX_B,
        "verification_record_sha256": "c" * 64,
        "created_at": NOW.isoformat(),
    }
    acceptance = {
        "acceptance_id": "acceptance-delivery-001",
        "authorization_identity": "subject_delivery",
        "declared_territory": "test fixture",
        "territorial_state": state,
        "licence_version": "0.1",
        "licence_sha256": HEX_A,
        "territorial_policy_version": "0.1",
        "territorial_policy_sha256": HEX_B,
        "tebdlc_release": "v0.1.0-alpha",
        "package_sha256": package_hash,
        "accepted_at": NOW.isoformat(),
        "acceptance_mechanism_version": "0.1",
    }
    return manifest, acceptance


def package(tmp: Path, data=b"controlled TEBDLC candidate package\n"):
    p = tmp / "tebdlc-v0.1.0-alpha.tar.gz"
    p.write_bytes(data)
    return p, hashlib.sha256(data).hexdigest()


def deliver(registry, pkg, manifest, acceptance, out):
    return controlled_deliver(
        registry=registry,
        credential_id="cred_delivery",
        presented_secret=SECRET,
        package_path=pkg,
        release_manifest=manifest,
        licence_acceptance=acceptance,
        output_directory=out,
        now=NOW,
    )


def test_privileged_exact_package_delivery():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        out = root / "out"
        result = deliver(make_registry(), pkg, manifest, acceptance, out)
        assert result["decision"] == "ALLOW"
        delivered = out / pkg.name
        assert delivered.read_bytes() == pkg.read_bytes()
        assert hashlib.sha256(delivered.read_bytes()).hexdigest() == digest


def test_neutral_package_delivery_allowed():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest, "NEUTRAL")
        result = deliver(make_registry("JM", None, None), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "ALLOW" and result["territorial_state"] == "NEUTRAL"


def test_restricted_delivery_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest, "RESTRICTED")
        result = deliver(make_registry("IL", None, None), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "DENY"
        assert not (root / "out" / pkg.name).exists()


def test_wrong_secret_denied_without_output():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        result = controlled_deliver(
            registry=make_registry(), credential_id="cred_delivery", presented_secret="wrong",
            package_path=pkg, release_manifest=manifest, licence_acceptance=acceptance,
            output_directory=root / "out", now=NOW,
        )
        assert result["decision"] == "DENY"
        assert not (root / "out" / pkg.name).exists()


def test_tampered_package_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        pkg.write_bytes(b"tampered")
        result = deliver(make_registry(), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_PACKAGE_HASH_MISMATCH"


def test_acceptance_identity_mismatch_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        acceptance["authorization_identity"] = "another-subject"
        result = deliver(make_registry(), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_ACCEPTANCE_IDENTITY_MISMATCH"


def test_acceptance_state_mismatch_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest, "NEUTRAL")
        result = deliver(make_registry(), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "DENY"
        assert result["reason_code"] == "DENY_ACCEPTANCE_TERRITORY_MISMATCH"


def test_release_mismatch_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        acceptance["tebdlc_release"] = "v9.9.9"
        result = deliver(make_registry(), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "DENY" and result["reason_code"] == "DENY_RELEASE_MISMATCH"


def test_policy_hash_mismatch_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        acceptance["territorial_policy_sha256"] = "d" * 64
        result = deliver(make_registry(), pkg, manifest, acceptance, root / "out")
        assert result["decision"] == "DENY" and result["reason_code"] == "DENY_POLICY_INTEGRITY_FAILURE"


def test_same_source_and_output_path_denied():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        pkg, digest = package(root)
        manifest, acceptance = records(digest)
        result = deliver(make_registry(), pkg, manifest, acceptance, root)
        assert result["decision"] == "DENY" and result["reason_code"] == "DENY_PATH_INTEGRITY_FAILURE"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
    print(f"controlled delivery tests: PASS ({len(tests)})")
