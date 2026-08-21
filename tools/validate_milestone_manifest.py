# Jonathan Therrien, Marieville, Québec.
"""Validate TEBDLC material-continuity milestone manifests.

A solid milestone is not materially continuous unless all seven required
artifact families are explicitly represented by non-empty references.
This validator checks structure only; it does not prove that referenced
artifacts are correct, immutable, or scientifically valid.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_FAMILIES = (
    "source_code",
    "tests",
    "vectors",
    "logs",
    "fingerprints",
    "results",
    "documentation",
)

ALLOWED_STATUSES = {"DRAFT", "EXECUTED", "PERSISTED", "VERIFIED", "SUPERSEDED"}


def fail(message: str) -> None:
    raise ValueError(message)


def validate_manifest(data: dict) -> None:
    if not isinstance(data, dict):
        fail("manifest root must be an object")

    milestone_id = data.get("milestone_id")
    if not isinstance(milestone_id, str) or not milestone_id.strip():
        fail("milestone_id must be a non-empty string")

    status = data.get("status")
    if status not in ALLOWED_STATUSES:
        fail(f"status must be one of {sorted(ALLOWED_STATUSES)}")

    evidence = data.get("evidence")
    if not isinstance(evidence, dict):
        fail("evidence must be an object")

    missing = [name for name in REQUIRED_FAMILIES if name not in evidence]
    if missing:
        fail(f"missing required evidence families: {', '.join(missing)}")

    empty = []
    for family in REQUIRED_FAMILIES:
        refs = evidence[family]
        if not isinstance(refs, list) or not refs:
            empty.append(family)
            continue
        for index, item in enumerate(refs):
            if not isinstance(item, dict):
                fail(f"{family}[{index}] must be an object")
            ref = item.get("ref")
            if not isinstance(ref, str) or not ref.strip():
                fail(f"{family}[{index}].ref must be a non-empty string")
    if empty:
        fail(f"empty required evidence families: {', '.join(empty)}")

    if status in {"PERSISTED", "VERIFIED", "SUPERSEDED"}:
        continuity = data.get("material_continuity")
        if continuity is not True:
            fail(f"status {status} requires material_continuity=true")

    limitations = data.get("limitations")
    if not isinstance(limitations, list):
        fail("limitations must be a list (it may be empty only when justified by the evidence)")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {Path(argv[0]).name} <manifest.json>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        validate_manifest(data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1

    print(f"VALID: {data['milestone_id']} status={data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
