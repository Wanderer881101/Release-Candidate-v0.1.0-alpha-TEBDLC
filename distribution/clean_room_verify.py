#!/usr/bin/env python3
"""TEBDLC clean-room release verification harness v0.1.

This tool validates an assembled controlled package against explicit expected hashes
and runs the public reference distribution test suites. It is intentionally fail-closed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "distribution"

TEST_FILES = [
    "test_validate_records.py",
    "test_resolve_territory.py",
    "test_authentication.py",
    "test_authorize_request.py",
    "test_controlled_delivery.py",
    "test_audit_chain.py",
    "test_adversarial_distribution.py",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(message: str) -> int:
    print(f"CLEAN_ROOM_FAIL: {message}")
    return 1


def run_tests() -> tuple[bool, list[dict[str, object]]]:
    results = []
    for name in TEST_FILES:
        path = DIST / name
        if not path.is_file():
            results.append({"test": name, "returncode": None, "ok": False, "reason": "missing"})
            return False, results
        proc = subprocess.run([sys.executable, str(path)], cwd=str(DIST), capture_output=True, text=True)
        results.append({
            "test": name,
            "returncode": proc.returncode,
            "ok": proc.returncode == 0,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
        })
        if proc.returncode != 0:
            return False, results
    return True, results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--licence", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--expected-package-sha256")
    parser.add_argument("--output-record", required=True)
    args = parser.parse_args()

    package = Path(args.package)
    manifest_path = Path(args.manifest)
    licence = Path(args.licence)
    policy = Path(args.policy)
    output = Path(args.output_record)

    for p in (package, manifest_path, licence, policy):
        if not p.is_file() or p.is_symlink():
            return fail(f"missing/unsafe input: {p}")

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail(f"manifest parse failure: {exc}")
    if not isinstance(manifest, dict):
        return fail("manifest must be object")

    package_sha = sha256_file(package)
    licence_sha = sha256_file(licence)
    policy_sha = sha256_file(policy)

    if args.expected_package_sha256 and package_sha != args.expected_package_sha256.lower():
        return fail("package SHA differs from command-line expected SHA")
    if manifest.get("package_sha256") != package_sha:
        return fail("package SHA differs from manifest")
    if manifest.get("licence_sha256") != licence_sha:
        return fail("licence SHA differs from manifest")
    if manifest.get("territorial_policy_sha256") != policy_sha:
        return fail("territorial-policy SHA differs from manifest")

    ok, tests = run_tests()
    record = {
        "clean_room_version": "0.1",
        "package_sha256": package_sha,
        "manifest_sha256": sha256_file(manifest_path),
        "licence_sha256": licence_sha,
        "territorial_policy_sha256": policy_sha,
        "tests_ok": ok,
        "tests": tests,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not ok:
        return fail("one or more reference/adversarial suites failed")
    print(json.dumps({"status": "CLEAN_ROOM_PASS", "package_sha256": package_sha}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
