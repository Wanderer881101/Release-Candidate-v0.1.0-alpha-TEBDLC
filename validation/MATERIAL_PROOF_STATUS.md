# TEBDLC v0.1.0-alpha — Material Proof Status

**Jonathan Therrien, Marieville, Québec.**

Status date: 2026-08-20

## 1. Executed public reference proof

The public RC validation was executed materially on GitHub-hosted Python 3.11.16.

Persisted record: `validation/LAST_EXECUTION.json`

Confirmed executable results:

- compileall: PASS;
- record validator: PASS (8 tests);
- territorial resolver: PASS (11 tests);
- authentication: PASS (8 tests);
- integrated authorization: PASS (8 tests);
- controlled delivery: PASS (10 tests);
- audit log: PASS (5 tests);
- adversarial distribution: PASS (18 tests);
- adversarial end-to-end: PASS (11 tests).

The first executed pass exposed two repository-coherence defects rather than semantic failures:

1. direct execution import mismatch in `test_resolve_territory.py`;
2. `audit_chain`/`audit_log` naming mismatch in the extended adversarial suite.

The clean-room harness also referenced the obsolete `test_audit_chain.py` name. These issues were corrected while preserving the canonical `audit_log.py` implementation and adding a compatibility import surface for the older module name.

After correction, the complete public suite returned `overall_pass: true`.

## 2. Executed clean-room harness proof

Persisted record: `validation/CLEAN_ROOM_HARNESS_EXECUTION.json`

The clean-room harness was exercised end-to-end against a synthetic material package generated during CI and bound to the active project licence and territorial-policy files by their real SHA-256 hashes.

Confirmed result:

- clean-room process return code: `0`;
- clean-room status: `CLEAN_ROOM_PASS`;
- all eight reference/adversarial suites re-executed through the clean-room harness: PASS;
- package, manifest, licence and territorial-policy SHA-256 values persisted in the verification record.

This proves the clean-room verification mechanism itself is executable and fail-gated. The synthetic package is test material only and is **not** the controlled TEBDLC source release.

## 3. Canonical private product source anchor

Canonical private repository: `Wanderer881101/TEBDLC`

Canonical development/release-candidate lineage branch: `proof/r6-executable-invariants`

A private material packaging attempt was made by temporarily enabling PR execution and adding a deterministic source-archive job. The resulting private workflow run started at the GitHub workflow level, but all runner jobs failed before exposing any executable steps; the dependent package job was therefore `skipped`.

No TEBDLC product test failure is inferred from that run because no product step executed.

The private workflow was restored immediately afterward to its quota-safe policy so the repository is not left intentionally red or consuming private runner quota.

## 4. Real controlled package status

The real `TEBDLC-v0.1.0-alpha` controlled source archive has **not yet been materially assembled in the current tooling environment**.

Reason: the available connector can read the private repository file-by-file but does not expose a repository-archive download operation, while the attempted private GitHub-hosted runners terminated before execution and therefore could not create the deterministic archive artifact.

Accordingly:

- no fake package SHA is recorded;
- no synthetic package is represented as the TEBDLC product;
- no final release manifest is marked immutable;
- the final clean-room gate remains open specifically for the exact private source archive.

## 5. Remaining material sequence

The next valid material sequence is:

1. obtain an exact checkout/archive of the canonical private source commit through an execution environment able to read that private repository;
2. assemble `TEBDLC-v0.1.0-alpha-source.tar.gz` deterministically;
3. calculate and persist the package SHA-256;
4. bind the package to the active licence and territorial-policy SHA-256 values in the release manifest;
5. execute `distribution/clean_room_verify.py` against that exact archive;
6. require `CLEAN_ROOM_PASS`;
7. persist the verification record and final audit checkpoint;
8. only then mark the controlled package as materially release-ready.

The absence of step 1 capability in the current environment is an infrastructure boundary, not permission to replace the real package with a surrogate.
