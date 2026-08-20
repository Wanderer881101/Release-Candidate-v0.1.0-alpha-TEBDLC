#!/usr/bin/env python3
from datetime import datetime, timezone
import base64

from authentication import derive_verifier
from authorize_request import authorize

NOW = datetime(2026, 8, 20, 14, 30, tzinfo=timezone.utc)
SECRET = "integration-secret"
SALT = base64.urlsafe_b64encode(b"abcdefghijklmnop").decode("ascii")
VERIFIER = derive_verifier(SECRET, SALT)


def make_registry(country="CA", subdivision="QC", city="Montréal", account_status="ACTIVE"):
    return {
        "schema": "tebdlc-auth-registry/0.1",
        "registry_version": "integration-test",
        "accounts": [{
            "subject_id": "subject_integration",
            "status": account_status,
            "declared_territory": {
                "country_code": country,
                "subdivision_code": subdivision,
                "city": city,
            },
            "credentials": [{
                "credential_id": "cred_integration",
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


def test_privileged_download_allowed():
    d = authorize(make_registry(), "cred_integration", SECRET, "DOWNLOAD_PACKAGE", NOW)
    assert d["decision"] == "ALLOW" and d["territorial_state"] == "PRIVILEGED"


def test_neutral_download_allowed():
    d = authorize(make_registry("JM", None, None), "cred_integration", SECRET, "DOWNLOAD_PACKAGE", NOW)
    assert d["decision"] == "ALLOW" and d["territorial_state"] == "NEUTRAL"


def test_neutral_falsification_denied():
    d = authorize(make_registry("JM", None, None), "cred_integration", SECRET, "FALSIFY", NOW)
    assert d["decision"] == "DENY" and d["reason_code"] == "DENY_RIGHT_NOT_GRANTED"


def test_restricted_country_denied():
    d = authorize(make_registry("IL", None, None), "cred_integration", SECRET, "DOWNLOAD_PACKAGE", NOW)
    assert d["decision"] == "DENY" and d["reason_code"] == "DENY_RESTRICTED_TERRITORY"


def test_ottawa_denied_over_country_context():
    d = authorize(make_registry("CA", "ON", "Ottawa"), "cred_integration", SECRET, "DOWNLOAD_PACKAGE", NOW)
    assert d["decision"] == "DENY" and d["territorial_state"] == "RESTRICTED"


def test_wrong_secret_denied_before_territory():
    d = authorize(make_registry(), "cred_integration", "bad-secret", "DOWNLOAD_PACKAGE", NOW)
    assert d["decision"] == "DENY" and d["reason_code"] == "DENY_AUTHENTICATION_FAILURE"


def test_unknown_action_denied():
    d = authorize(make_registry(), "cred_integration", SECRET, "MAGIC_ADMIN", NOW)
    assert d["decision"] == "DENY" and d["reason_code"] == "DENY_RIGHT_NOT_GRANTED"


def test_unknown_territory_fail_closed():
    d = authorize(make_registry("ZZ", None, None), "cred_integration", SECRET, "DOWNLOAD_PACKAGE", NOW)
    assert d["decision"] == "DENY"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
    print(f"integrated authorization tests: PASS ({len(tests)})")
