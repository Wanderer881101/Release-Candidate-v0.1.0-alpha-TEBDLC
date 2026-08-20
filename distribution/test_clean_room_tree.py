#!/usr/bin/env python3
from __future__ import annotations

import io
import tarfile
import tempfile
import unittest
from pathlib import Path

from clean_room_verify import git_tree_sha1_from_tar

EXPECTED_TREE = "6374c14b7aee595df913f11cd926dfb4821fd3d0"


def build_archive(path: Path, *, mutate: bool = False) -> None:
    with tarfile.open(path, "w:gz") as tf:
        root = tarfile.TarInfo("TEBDLC-v0.1.0-alpha/")
        root.type = tarfile.DIRTYPE
        root.mode = 0o755
        tf.addfile(root)

        entries = [
            ("a.txt", b"hello\n" if not mutate else b"hEllo\n", 0o644),
            ("bin.sh", b"#!/bin/sh\nexit 0\n", 0o755),
            ("sub/b.txt", b"world\n", 0o644),
        ]
        for rel, data, mode in entries:
            info = tarfile.TarInfo(f"TEBDLC-v0.1.0-alpha/{rel}")
            info.size = len(data)
            info.mode = mode
            tf.addfile(info, io.BytesIO(data))


class CleanRoomTreeTests(unittest.TestCase):
    def test_known_git_tree_vector(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            archive = Path(td) / "candidate.tar.gz"
            build_archive(archive)
            observed, count = git_tree_sha1_from_tar(archive)
            self.assertEqual(observed, EXPECTED_TREE)
            self.assertEqual(count, 3)

    def test_single_byte_mutation_changes_tree(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            archive = Path(td) / "candidate-mutated.tar.gz"
            build_archive(archive, mutate=True)
            observed, count = git_tree_sha1_from_tar(archive)
            self.assertNotEqual(observed, EXPECTED_TREE)
            self.assertEqual(count, 3)

    def test_duplicate_path_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            archive = Path(td) / "duplicate.tar.gz"
            with tarfile.open(archive, "w:gz") as tf:
                for data in (b"one", b"two"):
                    info = tarfile.TarInfo("TEBDLC-v0.1.0-alpha/a.txt")
                    info.size = len(data)
                    info.mode = 0o644
                    tf.addfile(info, io.BytesIO(data))
            with self.assertRaisesRegex(ValueError, "duplicate archive path"):
                git_tree_sha1_from_tar(archive)

    def test_unsafe_parent_path_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            archive = Path(td) / "unsafe.tar.gz"
            with tarfile.open(archive, "w:gz") as tf:
                data = b"x"
                info = tarfile.TarInfo("TEBDLC-v0.1.0-alpha/../escape.txt")
                info.size = len(data)
                info.mode = 0o644
                tf.addfile(info, io.BytesIO(data))
            with self.assertRaisesRegex(ValueError, "unsafe archive path"):
                git_tree_sha1_from_tar(archive)


if __name__ == "__main__":
    unittest.main(verbosity=2)
