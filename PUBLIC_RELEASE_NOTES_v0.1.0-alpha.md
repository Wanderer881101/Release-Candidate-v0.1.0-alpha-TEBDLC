# TEBDLC v0.1.0-alpha — Public Release Notes

**Jonathan Therrien, Marieville, Québec.**

Status: **ASSEMBLED PUBLIC RELEASE CANDIDATE / NOT YET FINAL GITHUB RELEASE**

## Purpose

This is the first TEBDLC Release Candidate intended for public use by programmers/technologists as a materially usable and independently verifiable snapshot.

It is not a metadata-only publication and it is not the earlier controlled-delivery prerelease model.

## Source lineage

- Private development repository: `Wanderer881101/TEBDLC`.
- Frozen source identity: `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- Frozen source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- Public distribution repository: `Wanderer881101/Release-Candidate-v0.1.0-alpha-TEBDLC`.

The private development repository remains private. The public repository contains the intentionally selected Release Candidate product, not the complete private development history.

## Public product content

The assembled Release Candidate includes the product source and verification material selected for publication, including:

- Python implementation under `src/`;
- experimental/reference C implementation under `c_core/`;
- Python tests under `tests/`;
- validation/continuity tools under `tools/`;
- experimental and build documentation under `docs/`;
- reconstructible evidence and milestone material under `evidence/`;
- build/package contracts including `Makefile` and `pyproject.toml`.

## Build and verification

The product README and `docs/BUILD_AND_VERIFY.md` describe local build, test, verification and sanitizer paths.

The Release Candidate intentionally preserves code, tests, vectors, logs, fingerprints, results and documentation rather than stripping evidence merely to simplify publication.

## Licence and ownership

Public availability does not place TEBDLC in the public domain and does not make the project OSI open source.

Active terms for this public Release Candidate are recorded in:

- `NOTICE.md`;
- `LICENSE-SOURCE-AVAILABLE-v0.1.1.md`;
- `TERRITORIAL_RIGHTS_POLICY_v0.2.md`;
- `ACTIVE_RELEASE_MODEL_v0.1.0-alpha.md`.

## Historical controlled-distribution work

The repository preserves the earlier controlled-distribution architecture, including private-vault, authorization, territorial-resolution, audit and delivery work. That work remains valuable R&D/provenance but no longer defines the publication boundary of this first public Release Candidate.

See `ACTIVE_POLICY_INDEX.md` and `distribution/README.md` for the active/historical distinction.

## Current publication state

The product has been assembled on an isolated public branch. It has **not yet been declared the final public GitHub Release**.

Before final publication, `PUBLIC_RELEASE_GATE_v0.1.0-alpha.md` must pass, including secret scanning, active-document consistency, workflow-cost control, public-assembly verification and final public hash/freeze recording.
