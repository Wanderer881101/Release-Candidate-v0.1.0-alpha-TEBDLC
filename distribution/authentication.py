#!/usr/bin/env python3
"""TEBDLC controlled-distribution authentication primitives v0.1.

Stdlib-only reference implementation. Stores/verifies password-equivalent secrets only
through salted PBKDF2-HMAC-SHA256 verifiers; raw credentials must never be committed.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import base64
import hashlib
import hmac
import json
import secrets
from typing import Any

PBKDF2_ITERATIONS = 310_000
SALT_BYTES = 16
TOKEN_BYTES = 32


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _parse_ts(value: str | None) -> datetime | None:
    if value is None:
        return None
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp must be timezone-aware")
    return dt.astimezone(timezone.utc)


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii")


def _unb64(value: str) -> bytes:
    return base64.urlsafe_b64decode(value.encode("ascii"))


def derive_verifier(secret: str, salt_b64: str, iterations: int = PBKDF2_ITERATIONS) -> str:
    if not secret:
        raise ValueError("empty secret")
    if iterations < 100_000:
        raise ValueError("PBKDF2 iteration count below minimum")
    digest = hashlib.pbkdf2_hmac("sha256", secret.encode("utf-8"), _unb64(salt_b64), iterations)
    return _b64(digest)


def generate_credential_material() -> tuple[str, dict[str, Any]]:
    """Return (raw_secret_once, persisted_verifier_record)."""
    raw = secrets.token_urlsafe(TOKEN_BYTES)
    salt = _b64(secrets.token_bytes(SALT_BYTES))
    return raw, {
        "algorithm": "PBKDF2-HMAC-SHA256",
        "iterations": PBKDF2_ITERATIONS,
        "salt": salt,
        "verifier": derive_verifier(raw, salt),
    }


@dataclass(frozen=True)
class AuthDecision:
    authenticated: bool
    reason_code: str
    subject_id: str | None
    credential_id: str | None
    account_status: str | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def authenticate(registry: dict[str, Any], credential_id: str, presented_secret: str,
                 now: datetime | None = None) -> AuthDecision:
    """Fail-closed credential check against an in-memory registry document."""
    now = (now or _utcnow()).astimezone(timezone.utc)
    if not credential_id or not presented_secret:
        return AuthDecision(False, "DENY_AUTHENTICATION_FAILURE", None, credential_id or None, None)

    accounts = registry.get("accounts")
    if not isinstance(accounts, list):
        return AuthDecision(False, "DENY_REGISTRY_INTEGRITY_FAILURE", None, credential_id, None)

    matches: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for account in accounts:
        if not isinstance(account, dict):
            return AuthDecision(False, "DENY_REGISTRY_INTEGRITY_FAILURE", None, credential_id, None)
        credentials = account.get("credentials", [])
        if not isinstance(credentials, list):
            return AuthDecision(False, "DENY_REGISTRY_INTEGRITY_FAILURE", None, credential_id, None)
        for cred in credentials:
            if isinstance(cred, dict) and cred.get("credential_id") == credential_id:
                matches.append((account, cred))

    if len(matches) != 1:
        reason = "DENY_DUPLICATE_CREDENTIAL_ID" if len(matches) > 1 else "DENY_AUTHENTICATION_FAILURE"
        return AuthDecision(False, reason, None, credential_id, None)

    account, cred = matches[0]
    subject_id = account.get("subject_id")
    status = account.get("status")
    if not isinstance(subject_id, str) or not subject_id:
        return AuthDecision(False, "DENY_REGISTRY_INTEGRITY_FAILURE", None, credential_id, status if isinstance(status, str) else None)
    if status != "ACTIVE":
        return AuthDecision(False, "DENY_ACCOUNT_NOT_ACTIVE", subject_id, credential_id, str(status))

    if cred.get("status") != "ACTIVE":
        return AuthDecision(False, "DENY_CREDENTIAL_NOT_ACTIVE", subject_id, credential_id, status)

    try:
        not_before = _parse_ts(cred.get("not_before"))
        expires_at = _parse_ts(cred.get("expires_at"))
        revoked_at = _parse_ts(cred.get("revoked_at"))
    except Exception:
        return AuthDecision(False, "DENY_REGISTRY_INTEGRITY_FAILURE", subject_id, credential_id, status)

    if revoked_at is not None and revoked_at <= now:
        return AuthDecision(False, "DENY_CREDENTIAL_REVOKED", subject_id, credential_id, status)
    if not_before is not None and now < not_before:
        return AuthDecision(False, "DENY_CREDENTIAL_NOT_YET_VALID", subject_id, credential_id, status)
    if expires_at is not None and now >= expires_at:
        return AuthDecision(False, "DENY_CREDENTIAL_EXPIRED", subject_id, credential_id, status)

    auth = cred.get("auth")
    if not isinstance(auth, dict) or auth.get("algorithm") != "PBKDF2-HMAC-SHA256":
        return AuthDecision(False, "DENY_UNSUPPORTED_CREDENTIAL_SCHEME", subject_id, credential_id, status)
    try:
        expected = str(auth["verifier"])
        actual = derive_verifier(presented_secret, str(auth["salt"]), int(auth["iterations"]))
    except Exception:
        return AuthDecision(False, "DENY_REGISTRY_INTEGRITY_FAILURE", subject_id, credential_id, status)

    if not hmac.compare_digest(expected, actual):
        return AuthDecision(False, "DENY_AUTHENTICATION_FAILURE", subject_id, credential_id, status)

    return AuthDecision(True, "ALLOW_AUTHENTICATED", subject_id, credential_id, status)


def rotate_credential(account: dict[str, Any], old_credential_id: str, now: datetime | None = None) -> tuple[str, dict[str, Any]]:
    """Create a new credential and revoke the selected old credential in-memory."""
    now = (now or _utcnow()).astimezone(timezone.utc)
    credentials = account.get("credentials")
    if not isinstance(credentials, list):
        raise ValueError("invalid account credential list")
    old = [c for c in credentials if isinstance(c, dict) and c.get("credential_id") == old_credential_id]
    if len(old) != 1:
        raise ValueError("old credential id must exist exactly once")
    old[0]["status"] = "REVOKED"
    old[0]["revoked_at"] = now.isoformat()

    raw, auth = generate_credential_material()
    new_record = {
        "credential_id": "cred_" + secrets.token_hex(12),
        "status": "ACTIVE",
        "not_before": now.isoformat(),
        "expires_at": None,
        "revoked_at": None,
        "auth": auth,
    }
    credentials.append(new_record)
    return raw, new_record


def load_registry(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError("registry must be a JSON object")
    return data
