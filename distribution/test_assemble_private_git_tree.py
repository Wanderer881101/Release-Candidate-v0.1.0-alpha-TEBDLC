#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path, PurePosixPath

from assemble_private_git_tree import deterministic_tar_gz, git_object_sha1, git_tree_sha1
from clean_room_verify import git_tree_sha1_from_tar


class PrivateTreeAssemblerTests(unittest.TestCase):
    def test_known_git_blob_and_tree_vector(self) -> None:
        data = b"hello\n"
        self.assertEqual(git_object_sha1("blob", data), "ce013625030ba8dba906f756967f9e9ca394464a")
        tree = git_tree_sha1({PurePosixPath("a.txt"): ("100644", data)})
        self.assertEqual(tree, "2e81171448eb9f2ee3821e3d447aa6b2fe3ddba1")

    def test_one_byte_mutation_changes_tree(self) -> None:
        a = {PurePosixPath("a.txt"): ("100644", b"hello\n")}
        b = {PurePosixPath("a.txt"): ("100644", b"jello\n")}
        self.assertNotEqual(git_tree_sha1(a), git_tree_sha1(b))

    def test_archive_rebuild_is_byte_identical(self) -> None:
        entries = {
            PurePosixPath("a.txt"): ("100644", b"alpha\n"),
            PurePosixPath("bin/run.sh"): ("100755", b"#!/bin/sh\necho ok\n"),
        }
        self.assertEqual(
            deterministic_tar_gz(entries, "v-test"),
            deterministic_tar_gz(entries, "v-test"),
        )

    def test_archive_round_trip_preserves_git_tree(self) -> None:
        entries = {
            PurePosixPath("a.txt"): ("100644", b"alpha\n"),
            PurePosixPath("dir/b.txt"): ("100644", b"beta\n"),
            PurePosixPath("bin/run.sh"): ("100755", b"#!/bin/sh\necho ok\n"),
        }
        expected = git_tree_sha1(entries)
        archive = deterministic_tar_gz(entries, "v-test")
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "package.tar.gz"
            p.write_bytes(archive)
            observed, count = git_tree_sha1_from_tar(p)
        self.assertEqual(observed, expected)
        self.assertEqual(count, len(entries))

    def test_symbolic_link_round_trip_preserves_git_tree(self) -> None:
        entries = {
            PurePosixPath("target.txt"): ("100644", b"target\n"),
            PurePosixPath("alias.txt"): ("120000", b"target.txt"),
        }
        expected = git_tree_sha1(entries)
        archive = deterministic_tar_gz(entries, "v-test")
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "package.tar.gz"
            p.write_bytes(archive)
            observed, count = git_tree_sha1_from_tar(p)
        self.assertEqual(observed, expected)
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
