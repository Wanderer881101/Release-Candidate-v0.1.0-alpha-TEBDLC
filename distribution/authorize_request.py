#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
"""Integrated TEBDLC controlled-distribution authorization decision v0.1."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from authentication import authenticate
from resolve_territory import resolve

ALLOWED_ACTIONS = {
    "READ_SOURCE",
    "BUILD",
    "EXECUTE",
    "TEST",
    "BENCHMARK",
    "PRIVATE_MODIFY",
    "FALSIFY",
    "DOWNLOAD_PACKAGE",
}


def _deny(reason: str, subject_id: str | None = None, territorial_state: str | None = None) -> dict[str, Any]:
    return {
        "decision": "DENY",
        "reason_code": reason,
        "subject_id": subject_id,
        "territorial_state": territorial_state,
    }


def authorize(registry: dict[str, Any], credential_id: str, presented_secret: str,
              requested_action: str, now: datetime | None = None) -> dict[str, Any]:
    """Authenticate, resolve declared territory, and enforce v0.1 rights matrix.

    Fail closed on malformed account data, unknown actions, authentication failure,
    territory mismatch/absence, RESTRICTED status, or rights not granted.
    """
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    action = (requested_action or "").strip().upper()
    if action not in ALLOWED_ACTIONS:
        return _deny("DENY_RIGHT_NOT_GRANTED")

    auth = authenticate(registry, credential_id, presented_secret, now)
    if not auth.authenticated:
        return _deny(auth.reason_code, auth.subject_id)

    accounts = registry.get("accounts", [])
    matches = [a for a in accounts if isinstance(a, dict) and a.get("subject_id") == auth.subject_id]
    if len(matches) != 1:
        return _deny("DENY_REGISTRY_INTEGRITY_FAILURE", auth.subject_id)

    territory = matches[0].get("declared_territory")
    if not isinstance(territory, dict):
        return _deny("DENY_UNRESOLVED_TERRITORY", auth.subject_id)

    country = territory.get("country_code")
    subdivision = territory.get("subdivision_code")
    city = territory.get("city")
    if not isinstance(country, str) or not country:
        return _deny("DENY_UNRESOLVED_TERRITORY", auth.subject_id)

    result = resolve(country, subdivision if isinstance(subdivision, str) else None,
                     city if isinstance(city, str) else None)
    state = result.get("state")
    if state not in {"PRIVILEGED", "NEUTRAL", "RESTRICTED"}:
        return _deny("DENY_UNRESOLVED_TERRITORY", auth.subject_id)
    if state == "RESTRICTED":
        return _deny("DENY_RESTRICTED_TERRITORY", auth.subject_id, state)

    if action == "FALSIFY" and state != "PRIVILEGED":
        return _deny("DENY_RIGHT_NOT_GRANTED", auth.subject_id, state)

    return {
        "decision": "ALLOW",
        "reason_code": "ALLOW_PRIVILEGED" if state == "PRIVILEGED" else "ALLOW_NEUTRAL",
        "subject_id": auth.subject_id,
        "credential_id": auth.credential_id,
        "territorial_state": state,
        "territorial_reason": result.get("reason"),
        "requested_action": action,
        "decision_timestamp": now.isoformat(),
    }
