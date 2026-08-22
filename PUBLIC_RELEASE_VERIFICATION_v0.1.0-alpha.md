# TEBDLC v0.1.0-alpha — Public Release Verification

**Jonathan Therrien, Marieville, Québec.**

Status: **STRUCTURAL PASS / EXECUTABLE CERTIFICATION PENDING**

## Scope

This record verifies the assembled public Release Candidate while distinguishing exact Git-object identity, static/public-overlay review, historical execution evidence and execution that still remains to be performed on the corrected public candidate.

The historical controlled-distribution GitHub Actions workflows are not re-run as part of this public-product certification.

## Canonical private source identity

- source repository: `Wanderer881101/TEBDLC`
- source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`
- source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`

## Exact shared product identities

The following shared product subtrees in the corrected public assembly retain the exact same Git tree SHA as the frozen canonical source:

- `c_core/` — `e8509e078587c76fca8a31eb9899b4d9f58b4440`
- `docs/` — `962b86d888bcce3bbd7a0c62afd15cb9abae39be`
- `evidence/` — `6bbd71ce6740b6b4ca557a7a215d346f80edd691`
- `src/` — `cfa4c0c953dc067a12f3859d541953038e1410b4`
- `tests/` — `3d46e47d690b35ef2673f81fd3061323567afb7f`
- `tools/` — `54020165e7f359916f9ff4380c3ff0e727233258`

The following root product files also preserve their canonical blob identity:

- `CHANGELOG.md` — `2763b92712b8fdca221ff9b721fb1d1a2a043c5a`
- `Makefile` — `b7e438c805d8e0bc528dd1b33ee57e5cb43fce86`
- `pyproject.toml` — `7b431c58aed419ec2e536b9076455d17580212c2`

`README.md` and `NOTICE.md` intentionally differ from the private snapshot because they are public-release overlays. Public governance/licence/release files are also intentional overlays.

## Historical execution evidence and its limit

Historical TEBDLC verification records establish successful execution of earlier canonical product states, including Python 3.11, 3.12 and 3.13 CI for the initial materialization and later product/build verification work.

That historical execution evidence remains applicable to unchanged Git objects within the scope actually tested. It is not represented as an execution of the current corrected public overlay.

The controlled-distribution 81/90-control workflows remain historical/R&D evidence and are not relabelled as proof of the active public-release boundary.

## Certification defect discovered after the first freeze attempt

The first public candidate frozen at `b05e4e415fa53996a1d06b045f1c5c4cba11f4cf` was subsequently found not to satisfy the repository-wide authorship-attribution invariant enforced by `tests/test_authorship_attribution.py`.

That test requires every tracked `.md`, `.py`, `.toml`, `.yml` and `.yaml` text file it scans to contain the exact attribution:

`Jonathan Therrien, Marieville, Québec.`

The defect was caused by public-release overlays and historical controlled-distribution files that did not yet carry the required attribution. Therefore the earlier `PASS / PRE-FREEZE` wording of this record was too strong and is superseded by this corrected record.

## Corrective branch

Correction is isolated on:

`cert-fix/v0.1.0-alpha`

The rejected freeze branch and commit are preserved for traceability; they are not silently rewritten.

Corrections applied on the certification branch are limited to public-overlay consistency, required authorship attribution, public build/CI clarification and historical/R&D files outside the six canonical product subtrees.

The six canonical product subtree SHA values listed above remain unchanged.

## Build and package contract review

Static review confirms:

- `pyproject.toml` declares package `tebdlc`, version `0.1.0`, Python `>=3.11`, and console entry point `tebdlc = tebdlc.cli:main`;
- the public README build/test/verify/sanitize commands correspond to actual `Makefile` targets;
- `make test` invokes `python -m pytest` and therefore includes `tests/test_authorship_attribution.py`;
- `make release-check` calls `tools/release_readiness.py`;
- required public product families are present in the assembled tree;
- `PUBLIC_BUILD_AND_VERIFY_v0.1.0-alpha.md` clarifies the public CI state without modifying the canonical `docs/` subtree.

## Workflow-cost boundary

The inherited controlled-distribution workflows `rc-validation.yml` and `cross-runtime-proof.yml` are manual `workflow_dispatch` only on the corrected assembly branch. They do not automatically run merely because commits are pushed to the branch or later integrated into public `main`.

## Sensitive-material review

The release assembly was reviewed for obvious operational credential/private-material patterns and no exposed operational credential was identified in the checks performed.

This is a repository release review, not a claim of formal forensic secret-scanner certification.

Intentionally published provenance — including historical branch names, experiment/sandbox references, author/location attribution, archive names and hashes — is retained by explicit release-scope decision and is not treated as accidental leakage.

## Active-document consistency

The active publication architecture is defined by:

- `ACTIVE_RELEASE_MODEL_v0.1.0-alpha.md`;
- `ACTIVE_POLICY_INDEX.md`;
- `LICENSE-SOURCE-AVAILABLE-v0.1.1.md`;
- `TERRITORIAL_RIGHTS_POLICY_v0.2.md`;
- `PUBLIC_RELEASE_GATE_v0.1.0-alpha.md`;
- `PUBLIC_RELEASE_NOTES_v0.1.0-alpha.md`;
- `PUBLIC_BUILD_AND_VERIFY_v0.1.0-alpha.md`;
- `README.md` and `NOTICE.md`.

Earlier controlled-distribution documents remain preserved as historical records and do not govern the publication boundary of this first public Release Candidate.

## Current verification verdict

**STRUCTURAL PASS / EXECUTABLE CERTIFICATION PENDING.**

Confirmed now:

- canonical product subtree identity is preserved;
- the known attribution defects have been corrected on the isolated certification branch;
- active licence/NOTICE/build-document references have been reconciled;
- no automatic historical workflow execution is required for this correction.

Not yet claimed:

- a fresh successful `pytest` / `make test` execution against the exact current `cert-fix/v0.1.0-alpha` candidate;
- a fresh full `make verify` execution against that exact candidate;
- final freeze/tree/package hashes for the corrected candidate;
- final GitHub Release publication.

The candidate must not be declared final until the exact corrected commit passes the executable product checks or an equivalently strong execution proof is recorded.
