# TEBDLC v0.1.0-alpha — Public Release Gate

**Jonathan Therrien, Marieville, Québec.**

Status: **ACTIVE / PRE-PUBLICATION CHECKLIST**

This gate applies to the first public, usable and independently verifiable TEBDLC `v0.1.0-alpha` Release Candidate.

## Product identity

- [x] Canonical source commit identified: `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Canonical source root tree identified: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [x] Corrective public certification branch exists and is isolated from `main`: `cert-fix/v0.1.0-alpha`.
- [x] Canonical shared product subtrees are present and retain their expected Git tree identities.

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
- [x] Public build/CI interpretation clarified without modifying the canonical `docs/` subtree.

## Historical continuity

- [x] Earlier controlled-distribution gate, notes, policy and publication record remain traceable.
- [x] `distribution/` remains preserved as historical/R&D gain.
- [x] Historical proofs/hashes are not silently re-labelled as proof of the new publication boundary.
- [x] Rejected public freeze candidate `b05e4e415fa53996a1d06b045f1c5c4cba11f4cf` remains traceable rather than being silently rewritten.

## Public-tree review

- [x] Confirm no unrelated sensitive or operationally private material was identified by the repository-level review performed. See `PUBLIC_RELEASE_VERIFICATION_v0.1.0-alpha.md` for scope and limitations.
- [x] Confirm active documentation contains no unresolved contradiction currently identified about the first public Release architecture.
- [x] Confirm build/test/verify instructions reference files actually present in the public assembly.
- [x] Confirm historical release workflows are manual-only and do not automatically consume GitHub Actions minutes merely because commits are pushed or later integrated into `main`.
- [x] Correct known repository-wide authorship-attribution violations in public overlays and historical/R&D files while retaining the canonical product subtrees unchanged.

## Executable certification still required

- [ ] Execute `make test` (or an equivalent command set proving the same Python + C test contract) against the **exact corrected certification commit** and persist the result.
- [ ] Execute `make verify` against the exact corrected certification commit and persist the result.
- [ ] Confirm `tests/test_authorship_attribution.py` passes on the exact corrected certification tree.
- [ ] Record the exact corrected public candidate commit and root tree after executable certification passes.
- [ ] Record final public tree/package hashes for that corrected public assembly.
- [ ] Create a new final freeze identity for the corrected candidate; do not reuse the rejected `b05e...` candidate as the final release target.
- [ ] Create the actual public GitHub Release `v0.1.0-alpha` only after all above gates pass.

## Publication invariant

The public Release Candidate must not be reduced to metadata-only documentation. It must remain the intentionally approved usable/verifiable product snapshot.

The private TEBDLC development repository remains private and is not made public by this release.
