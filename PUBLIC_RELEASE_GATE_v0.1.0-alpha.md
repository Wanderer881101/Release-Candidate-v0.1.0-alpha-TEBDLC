# TEBDLC v0.1.0-alpha — Public Release Gate

Status: **ACTIVE / PRE-PUBLICATION CHECKLIST**

This gate applies to the first public, usable and independently verifiable TEBDLC `v0.1.0-alpha` Release Candidate.

## Product identity

- [x] Canonical source commit identified: `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Canonical source root tree identified: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [x] Public assembly branch exists and is isolated from `main`.
- [x] Canonical shared product subtrees are present in the public assembly.

## Required public product content

- [x] `src/` present.
- [x] `c_core/` present.
- [x] `tests/` present.
- [x] `tools/` present.
- [x] `docs/` present.
- [x] `evidence/` present.
- [x] `Makefile` present.
- [x] `pyproject.toml` present.
- [x] Product README present.
- [x] Ownership notice present.

## Public-overlay governance

- [x] Active public-release architecture recorded in `ACTIVE_RELEASE_MODEL_v0.1.0-alpha.md`.
- [x] Active policy index separates current documents from historical controlled-distribution material.
- [x] Active public-release licence created as `LICENSE-SOURCE-AVAILABLE-v0.1.1.md`.
- [x] Territorial project-right policy separated from technical public availability in `TERRITORIAL_RIGHTS_POLICY_v0.2.md`.
- [x] Historical controlled-distribution material preserved rather than deleted.

## Historical continuity

- [x] Earlier controlled-distribution gate, notes, policy and publication record remain traceable.
- [x] `distribution/` remains preserved as historical/R&D gain.
- [x] Historical proofs/hashes are not silently re-labelled as proof of the new publication boundary.

## Remaining gates before public `main`/GitHub Release

- [x] Confirm no credential, private key, access token or unrelated private material is present in the assembled public tree. See `PUBLIC_RELEASE_VERIFICATION_v0.1.0-alpha.md` for scope and limitations.
- [x] Confirm active documentation contains no unresolved contradiction about the first public Release architecture.
- [x] Confirm build/test/verify instructions reference files actually present in the public assembly.
- [x] Confirm release workflows cannot automatically consume paid GitHub Actions minutes merely because the assembly is merged to `main`, unless explicitly approved.
- [x] Re-run or reuse a suitable final verification of the **public product assembly**, distinguishing product verification from historical controlled-distribution tests. Verification is recorded in `PUBLIC_RELEASE_VERIFICATION_v0.1.0-alpha.md` using exact canonical Git-object identity for unchanged product material.
- [ ] Freeze the exact public Release Candidate commit.
- [ ] Record final public tree/package hashes for the public assembly itself.
- [ ] Create the actual public GitHub Release `v0.1.0-alpha` only after the above gates pass.

## Publication invariant

The public Release Candidate must not be reduced to metadata-only documentation. It must remain the intentionally approved usable/verifiable product snapshot.

The private TEBDLC development repository remains private and is not made public by this release.
