#!/usr/bin/env python3
"""Assemble a controlled TEBDLC source archive from authenticated GitHub Git objects.

The tool never writes credentials to disk and never publishes source. It fetches the
exact commit/tree/blobs through GitHub's Git database API, verifies every Git object,
reconstructs the root-tree SHA-1 locally, then emits a deterministic tar.gz plus a
non-secret PACKAGE_PROOF.json.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import io
import json
import os
import stat
import tarfile
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath

API = "https://api.github.com"
USER_AGENT = "TEBDLC-controlled-release-assembler/0.1"


def git_object_sha1(kind: str, data: bytes) -> str:
    return hashlib.sha1(f"{kind} {len(data)}\0".encode("ascii") + data).hexdigest()


def _tree_sort_key(name: str, is_tree: bool) -> bytes:
    return name.encode("utf-8", "surrogateescape") + (b"/" if is_tree else b"")


def git_tree_sha1(entries: dict[PurePosixPath, tuple[str, bytes]]) -> str:
    root: dict[str, object] = {}
    for path, leaf in entries.items():
        if path.is_absolute() or ".." in path.parts or not path.parts:
            raise ValueError(f"unsafe path: {path}")
        node = root
        for part in path.parts[:-1]:
            existing = node.get(part)
            if existing is None:
                child: dict[str, object] = {}
                node[part] = child
                node = child
            elif isinstance(existing, dict):
                node = existing
            else:
                raise ValueError(f"path collision: {path}")
        if path.parts[-1] in node:
            raise ValueError(f"duplicate/path collision: {path}")
        node[path.parts[-1]] = leaf

    def digest(node: dict[str, object]) -> str:
        rows: list[tuple[str, str, str, bool]] = []
        for name, value in node.items():
            if isinstance(value, dict):
                rows.append((name, "40000", digest(value), True))
            else:
                mode, data = value  # type: ignore[misc]
                rows.append((name, mode, git_object_sha1("blob", data), False))
        rows.sort(key=lambda row: _tree_sort_key(row[0], row[3]))
        body = bytearray()
        for name, mode, sha, _ in rows:
            body.extend(mode.encode("ascii") + b" ")
            body.extend(name.encode("utf-8", "surrogateescape") + b"\0")
            body.extend(bytes.fromhex(sha))
        return git_object_sha1("tree", bytes(body))

    return digest(root)


def github_json(url: str, token: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"GitHub API HTTP {exc.code} for {url}") from exc
    obj = json.loads(payload.decode("utf-8"))
    if not isinstance(obj, dict):
        raise RuntimeError("unexpected GitHub API response")
    return obj


def fetch_source(repo: str, commit: str, expected_tree: str, token: str) -> dict[PurePosixPath, tuple[str, bytes]]:
    commit_obj = github_json(f"{API}/repos/{repo}/git/commits/{commit}", token)
    observed_commit = str(commit_obj.get("sha", "")).lower()
    tree_obj = commit_obj.get("tree") or {}
    observed_tree = str(tree_obj.get("sha", "")).lower()
    if observed_commit != commit.lower():
        raise RuntimeError("commit identity mismatch")
    if observed_tree != expected_tree.lower():
        raise RuntimeError("commit root-tree mismatch")

    listing = github_json(f"{API}/repos/{repo}/git/trees/{observed_tree}?recursive=1", token)
    if listing.get("truncated") is not False:
        raise RuntimeError("recursive Git tree is truncated or unconfirmed")
    rows = listing.get("tree")
    if not isinstance(rows, list):
        raise RuntimeError("tree response has no entry list")

    out: dict[PurePosixPath, tuple[str, bytes]] = {}
    for row in rows:
        if not isinstance(row, dict) or row.get("type") != "blob":
            continue
        path = PurePosixPath(str(row.get("path", "")))
        mode = str(row.get("mode", ""))
        sha = str(row.get("sha", "")).lower()
        if mode not in {"100644", "100755", "120000"}:
            raise RuntimeError(f"unsupported Git mode {mode} at {path}")
        if path.is_absolute() or ".." in path.parts or not path.parts or path in out:
            raise RuntimeError(f"unsafe/duplicate Git path: {path}")
        blob = github_json(f"{API}/repos/{repo}/git/blobs/{sha}", token)
        if blob.get("encoding") != "base64":
            raise RuntimeError(f"unsupported blob encoding at {path}")
        data = base64.b64decode(str(blob.get("content", "")), validate=False)
        if git_object_sha1("blob", data) != sha:
            raise RuntimeError(f"blob SHA mismatch at {path}")
        declared_size = row.get("size")
        if declared_size is not None and int(declared_size) != len(data):
            raise RuntimeError(f"blob size mismatch at {path}")
        out[path] = (mode, data)

    if not out:
        raise RuntimeError("no tracked blobs fetched")
    rebuilt = git_tree_sha1(out)
    if rebuilt != expected_tree.lower():
        raise RuntimeError(f"rebuilt root tree mismatch: {rebuilt}")
    return out


def deterministic_tar_gz(entries: dict[PurePosixPath, tuple[str, bytes]], release_id: str) -> bytes:
    raw_tar = io.BytesIO()
    prefix = f"TEBDLC-{release_id}/"
    with tarfile.open(fileobj=raw_tar, mode="w", format=tarfile.PAX_FORMAT) as tf:
        root = tarfile.TarInfo(prefix)
        root.type = tarfile.DIRTYPE
        root.mode = 0o755
        root.uid = root.gid = 0
        root.uname = root.gname = ""
        root.mtime = 0
        tf.addfile(root)

        for path in sorted(entries, key=lambda p: p.as_posix().encode("utf-8", "surrogateescape")):
            mode, data = entries[path]
            name = prefix + path.as_posix()
            ti = tarfile.TarInfo(name)
            ti.uid = ti.gid = 0
            ti.uname = ti.gname = ""
            ti.mtime = 0
            if mode == "120000":
                ti.type = tarfile.SYMTYPE
                ti.mode = 0o777
                ti.linkname = data.decode("utf-8", "surrogateescape")
                ti.size = 0
                tf.addfile(ti)
            else:
                ti.type = tarfile.REGTYPE
                ti.mode = 0o755 if mode == "100755" else 0o644
                ti.size = len(data)
                tf.addfile(ti, io.BytesIO(data))

    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="wb", compresslevel=9, mtime=0, filename="") as gz:
        gz.write(raw_tar.getvalue())
    return out.getvalue()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/repository")
    parser.add_argument("--commit", required=True)
    parser.add_argument("--expected-tree-sha1", required=True)
    parser.add_argument("--release-id", default="v0.1.0-alpha")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    args = parser.parse_args()

    token = os.environ.get(args.token_env, "")
    if not token:
        raise SystemExit(f"missing token in environment variable {args.token_env}")
    if len(args.commit) != 40 or len(args.expected_tree_sha1) != 40:
        raise SystemExit("commit and expected tree must be 40-hex Git SHA-1 values")

    entries = fetch_source(args.repo, args.commit.lower(), args.expected_tree_sha1.lower(), token)
    archive = deterministic_tar_gz(entries, args.release_id)
    # Rebuild once more from the same verified entries: deterministic packaging must be byte-identical.
    rebuilt = deterministic_tar_gz(entries, args.release_id)
    if archive != rebuilt:
        raise SystemExit("deterministic archive rebuild mismatch")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"TEBDLC-{args.release_id}-{args.commit.lower()}.tar.gz"
    package_path = output_dir / filename
    package_path.write_bytes(archive)
    package_sha = sha256_bytes(archive)

    proof = {
        "schema": "tebdlc-private-package-proof/0.2",
        "release_id": args.release_id,
        "repository": args.repo,
        "source_commit": args.commit.lower(),
        "source_tree_sha1": args.expected_tree_sha1.lower(),
        "tracked_file_count": len(entries),
        "archive_filename": filename,
        "package_sha256": package_sha,
        "package_size_bytes": len(archive),
        "assembly": "authenticated-git-objects + canonical-pax-tar + gzip-mtime0-level9 / v0.2",
        "deterministic_rebuild_match": True,
    }
    (output_dir / "PACKAGE_PROOF.json").write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "SHA256SUMS").write_text(f"{package_sha}  {filename}\n", encoding="utf-8")
    print(json.dumps(proof, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
