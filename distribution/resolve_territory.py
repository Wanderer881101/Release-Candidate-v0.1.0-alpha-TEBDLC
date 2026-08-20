#!/usr/bin/env python3
"""Deterministic TEBDLC territorial resolver v0.1.

Fail-closed semantics: unresolved/unknown territories are RESTRICTED by policy default.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "territories" / "territorial-policy-v0.1.json"
CARIBBEAN = ROOT / "territories" / "caribbean-neutral-v0.1.json"
MIDDLE_EAST = ROOT / "territories" / "middle-east-restricted-v0.1.json"


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _codes(entries: list[dict[str, Any]]) -> set[str]:
    return {str(e.get("code", "")).upper() for e in entries if e.get("code")}


def resolve(country_code: str, subdivision_code: str | None = None, city: str | None = None) -> dict[str, str]:
    country = (country_code or "").upper().strip()
    subdivision = (subdivision_code or "").upper().strip()
    city_norm = (city or "").strip().casefold()

    if not country:
        return {"state": "RESTRICTED", "reason": "DENY_UNRESOLVED_TERRITORY"}

    # Narrow explicit restriction wins first.
    if country == "CA" and city_norm == "ottawa":
        return {"state": "RESTRICTED", "reason": "EXPLICIT_CITY_RESTRICTION"}

    # Explicit privileged subdivision.
    if country == "US" and subdivision == "FL":
        return {"state": "PRIVILEGED", "reason": "EXPLICIT_PRIVILEGED_SUBDIVISION"}

    policy = _load(POLICY)
    restricted_codes = _codes([e for e in policy["explicitly_restricted"] if e.get("type") == "country"])
    if country in restricted_codes:
        return {"state": "RESTRICTED", "reason": "EXPLICIT_RESTRICTED_COUNTRY"}

    middle_east = _load(MIDDLE_EAST)
    if country in _codes(middle_east["members"]):
        return {"state": "RESTRICTED", "reason": "RESTRICTED_ANNEX"}

    # Explicit privileged states/countries from policy.
    if country == "CA" and subdivision in {"QC", "QUEBEC", "QUÉBEC"}:
        return {"state": "PRIVILEGED", "reason": "EXPLICIT_PRIVILEGED_SUBDIVISION"}
    privileged_country_codes = _codes([e for e in policy["privileged"] if e.get("type") == "country"])
    if country in privileged_country_codes:
        return {"state": "PRIVILEGED", "reason": "EXPLICIT_PRIVILEGED_COUNTRY"}

    caribbean = _load(CARIBBEAN)
    if country in _codes(caribbean["members"]):
        return {"state": "NEUTRAL", "reason": "NEUTRAL_CARIBBEAN_ANNEX"}

    # Rest of the USA is restricted by explicit policy.
    if country == "US":
        return {"state": "RESTRICTED", "reason": "US_DEFAULT_RESTRICTED_EXCEPT_FL"}

    return {"state": "RESTRICTED", "reason": "DEFAULT_RESTRICTED"}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("country")
    parser.add_argument("--subdivision")
    parser.add_argument("--city")
    args = parser.parse_args()
    print(json.dumps(resolve(args.country, args.subdivision, args.city), sort_keys=True))
