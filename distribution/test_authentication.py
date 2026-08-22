#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
from datetime import datetime, timezone, timedelta
from authentication import authenticate, derive_verifier, rotate_credential
import base64

NOW = datetime(2026, 8, 20, 14, 0, tzinfo=timezone.utc)
SECRET = "correct-horse-battery-staple"
SALT = base64.urlsafe_b64encode(b"0123456789abcdef").decode("ascii")
VERIFIER = derive_verifier(SECRET, SALT)


def registry(status="ACTIVE", cred_status="ACTIVE", not_before=None, expires_at=None, revoked_at=None):
    return {
        "schema": "tebdlc-auth-registry/0.1",
        "registry_version": "test-1",
        "accounts": [{
            "subject_id": "subject_test",
            "status": status,
            "declared_territory": {"country_code": "CA", "subdivision_code": "QC", "city": "Montréal"},
            "credentials": [{
                "credential_id": "cred_test",
                "status": cred_status,
                "not_before": not_before,
                "expires_at": expires_at,
                "revoked_at": revoked_at,
                "auth": {
                    "algorithm": "PBKDF2-HMAC-SHA256",
                    "iterations": 310000,
                    "salt": SALT,
                    "verifier": VERIFIER
                }
            }]
        }]
    }


def test_valid_authentication():
    r = authenticate(registry(), "cred_test", SECRET, NOW)
    assert r.authenticated and r.reason_code == "ALLOW_AUTHENTICATED"


def test_wrong_secret_denied():
    r = authenticate(registry(), "cred_test", "wrong", NOW)
    assert not r.authenticated and r.reason_code == "DENY_AUTHENTICATION_FAILURE"


def test_suspended_account_denied():
    r = authenticate(registry(status="SUSPENDED"), "cred_test", SECRET, NOW)
    assert not r.authenticated and r.reason_code == "DENY_ACCOUNT_NOT_ACTIVE"


def test_revoked_credential_denied():
    r = authenticate(registry(cred_status="REVOKED"), "cred_test", SECRET, NOW)
    assert not r.authenticated and r.reason_code == "DENY_CREDENTIAL_NOT_ACTIVE"


def test_expired_credential_denied():
    expiry = (NOW - timedelta(seconds=1)).isoformat()
    r = authenticate(registry(expires_at=expiry), "cred_test", SECRET, NOW)
    assert not r.authenticated and r.reason_code == "DENY_CREDENTIAL_EXPIRED"


def test_not_yet_valid_denied():
    nbf = (NOW + timedelta(seconds=1)).isoformat()
    r = authenticate(registry(not_before=nbf), "cred_test", SECRET, NOW)
    assert not r.authenticated and r.reason_code == "DENY_CREDENTIAL_NOT_YET_VALID"


def test_duplicate_credential_id_denied():
    reg = registry()
    reg["accounts"].append({
        "subject_id": "subject_other",
        "status": "ACTIVE",
        "declared_territory": {"country_code": "FR", "subdivision_code": None, "city": None},
        "credentials": [dict(reg["accounts"][0]["credentials"][0])]
    })
    r = authenticate(reg, "cred_test", SECRET, NOW)
    assert not r.authenticated and r.reason_code == "DENY_DUPLICATE_CREDENTIAL_ID"


def test_rotation_revokes_old_and_creates_new():
    reg = registry()
    account = reg["accounts"][0]
    raw, new_record = rotate_credential(account, "cred_test", NOW)
    assert raw
    assert new_record["status"] == "ACTIVE"
    assert account["credentials"][0]["status"] == "REVOKED"
    assert account["credentials"][0]["revoked_at"] is not None
    r_old = authenticate(reg, "cred_test", SECRET, NOW)
    r_new = authenticate(reg, new_record["credential_id"], raw, NOW)
    assert not r_old.authenticated
    assert r_new.authenticated


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
    print(f"authentication tests: PASS ({len(tests)})")
