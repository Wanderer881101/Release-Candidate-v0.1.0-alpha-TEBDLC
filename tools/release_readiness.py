# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "NOTICE.md",
    "Makefile",
    "pyproject.toml",
    "src/tebdlc/__init__.py",
    "src/tebdlc/cli.py",
    "tests",
    "c_core",
    "docs",
    "evidence",
)

SUSPICIOUS_TRACKED_SUFFIXES = (
    ".pyc", ".pyo", ".o", ".obj", ".so", ".dylib", ".dll", ".exe",
    ".pem", ".key", ".p12", ".pfx",
)
SUSPICIOUS_TRACKED_NAMES = {
    ".env", ".env.local", ".DS_Store", "Thumbs.db",
}
SUSPICIOUS_TRACKED_PARTS = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "venv", "build", "dist",
}


def tracked_files() -> list[str]:
    try:
        proc = subprocess.run(
            ["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=True
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def suspicious_tracked(paths: list[str]) -> list[str]:
    hits: list[str] = []
    for raw in paths:
        p = Path(raw)
        if p.name in SUSPICIOUS_TRACKED_NAMES:
            hits.append(raw)
            continue
        if p.suffix.lower() in SUSPICIOUS_TRACKED_SUFFIXES:
            hits.append(raw)
            continue
        if any(part in SUSPICIOUS_TRACKED_PARTS for part in p.parts):
            hits.append(raw)
    return sorted(set(hits))


def run() -> dict[str, object]:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    tracked = tracked_files()
    suspicious = suspicious_tracked(tracked)
    return {
        "product": "TEBDLC",
        "required_missing": missing,
        "tracked_file_count": len(tracked),
        "suspicious_tracked_generated_or_secret_like": suspicious,
        "gitignore_present": (ROOT / ".gitignore").exists(),
        "status": "PASS" if not missing and not suspicious else "REVIEW",
        "note": "Pattern audit only; this is not a complete secret scanner.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline TEBDLC release-readiness structure audit.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    payload = run()
    if args.json:
        print(json.dumps(payload, sort_keys=True, ensure_ascii=False))
    else:
        for key, value in payload.items():
            print(f"{key}: {value}")
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
