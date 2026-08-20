#!/usr/bin/env python3
"""TEBDLC clean-room release verification harness v0.2.

This tool validates an assembled controlled package against explicit expected hashes,
binds the archive contents to an expected Git root-tree SHA-1, and runs the public
reference distribution test suites. It is intentionally fail-closed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import stat
import subprocess
import sys
import tarfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "distribution"

TEST_FILES = [
    "test_validate_records.py",
    "test_resolve_territory.py",
    "test_authentication.py",
    "test_authorize_request.py",
    "test_controlled_delivery.py",
    "test_audit_log.py",
    "test_adversarial_distribution.py",
    "test_adversarial_end_to_end.py",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_object_sha1(kind: str, data: bytes) -> str:
    header = f"{kind} {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _tree_sort_key(name: str, is_tree: bool) -> bytes:
    # Git compares tree entry names bytewise, treating a directory as if its
    # name ended in '/'. This matters for exact tree-object identity.
    return name.encode("utf-8", "surrogateescape") + (b"/" if is_tree else b"")


def git_tree_sha1_from_tar(package: Path) -> tuple[str, int]:
    """Reconstruct the Git root-tree SHA-1 represented by a git-archive tar.gz.

    The archive must contain exactly one top-level prefix directory. Regular files,
    executable files, and symbolic links are represented using Git-compatible modes.
    Unsafe paths, hard links, devices, FIFOs and duplicate paths are rejected.
    """
    files: dict[PurePosixPath, tuple[str, str]] = {}
    prefixes: set[str] = set()

    with tarfile.open(package, mode="r:gz") as tf:
        for member in tf.getmembers():
            raw = PurePosixPath(member.name)
            parts = raw.parts
            if not parts:
                continue
            if raw.is_absolute() or ".." in parts:
                raise ValueError(f"unsafe archive path: {member.name}")

            prefixes.add(parts[0])
            if len(parts) == 1:
                if member.isdir():
                    continue
                raise ValueError("archive root must be a directory prefix")

            rel = PurePosixPath(*parts[1:])
            if member.isdir():
                continue
            if rel in files:
                raise ValueError(f"duplicate archive path: {rel}")

            if member.isreg():
                fh = tf.extractfile(member)
                if fh is None:
                    raise ValueError(f"unable to read archive member: {rel}")
                data = fh.read()
                mode = "100755" if (member.mode & stat.S_IXUSR) else "100644"
                files[rel] = (mode, git_object_sha1("blob", data))
            elif member.issym():
                data = member.linkname.encode("utf-8", "surrogateescape")
                files[rel] = ("120000", git_object_sha1("blob", data))
            else:
                raise ValueError(f"unsupported archive member type: {rel}")

    if len(prefixes) != 1:
        raise ValueError("archive must contain exactly one top-level prefix")
    if not files:
        raise ValueError("archive contains no tracked files")

    # Nested dictionary representation of the tree hierarchy.
    root: dict[str, object] = {}
    for path, leaf in files.items():
        node = root
        parts = path.parts
        for part in parts[:-1]:
            existing = node.get(part)
            if existing is None:
                child: dict[str, object] = {}
                node[part] = child
                node = child
            elif isinstance(existing, dict):
                node = existing
            else:
                raise ValueError(f"path collision at {path}")
        if parts[-1] in node:
            raise ValueError(f"path collision at {path}")
        node[parts[-1]] = leaf

    def digest_tree(node: dict[str, object]) -> str:
        entries: list[tuple[str, str, str, bool]] = []
        for name, value in node.items():
            if isinstance(value, dict):
                sha = digest_tree(value)
                entries.append((name, "40000", sha, True))
            else:
                mode, sha = value  # type: ignore[misc]
                entries.append((name, mode, sha, False))
        entries.sort(key=lambda x: _tree_sort_key(x[0], x[3]))
        body = bytearray()
        for name, mode, sha, _ in entries:
            body.extend(mode.encode("ascii"))
            body.extend(b" ")
            body.extend(name.encode("utf-8", "surrogateescape"))
            body.extend(b"\0")
            body.extend(bytes.fromhex(sha))
        return git_object_sha1("tree", bytes(body))

    return digest_tree(root), len(files)


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
    parser.add_argument("--expected-source-tree-sha1")
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

    expected_tree = (args.expected_source_tree_sha1 or manifest.get("source_tree_sha1") or "").lower()
    if not expected_tree:
        return fail("source tree SHA-1 is required")
    if len(expected_tree) != 40 or any(c not in "0123456789abcdef" for c in expected_tree):
        return fail("invalid expected source tree SHA-1")
    if manifest.get("source_tree_sha1") != expected_tree:
        return fail("source tree SHA differs from manifest")

    try:
        observed_tree, tracked_file_count = git_tree_sha1_from_tar(package)
    except Exception as exc:
        return fail(f"source-tree reconstruction failure: {exc}")
    if observed_tree != expected_tree:
        return fail("archive contents do not match expected Git source tree")

    manifest_count = manifest.get("tracked_file_count")
    if manifest_count is not None and manifest_count != tracked_file_count:
        return fail("tracked file count differs from manifest")

    ok, tests = run_tests()
    record = {
        "clean_room_version": "0.2",
        "package_sha256": package_sha,
        "manifest_sha256": sha256_file(manifest_path),
        "licence_sha256": licence_sha,
        "territorial_policy_sha256": policy_sha,
        "expected_source_tree_sha1": expected_tree,
        "observed_source_tree_sha1": observed_tree,
        "source_tree_match": observed_tree == expected_tree,
        "tracked_file_count": tracked_file_count,
        "tests_ok": ok,
        "tests": tests,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not ok:
        return fail("one or more reference/adversarial suites failed")
    print(json.dumps({
        "status": "CLEAN_ROOM_PASS",
        "package_sha256": package_sha,
        "source_tree_sha1": observed_tree,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
