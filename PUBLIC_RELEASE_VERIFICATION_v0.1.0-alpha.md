# TEBDLC v0.1.0-alpha — Public Release Verification

Status: **PASS / PRE-FREEZE**

## Scope

This record verifies the assembled public Release Candidate without re-running the historical controlled-distribution GitHub Actions workflows.

The product verification is based on exact Git-object identity for the shared product material copied from the frozen private TEBDLC snapshot, combined with direct review of the public overlay files and repository hygiene.

## Canonical private source identity

- source repository: `Wanderer881101/TEBDLC`
- source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`
- source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`

## Exact shared product identities

The following shared product subtrees in the public assembly have the exact same Git tree SHA as the frozen canonical source:

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

## Reuse of prior product verification

Because the shared product code, tests, tools, documentation and evidence retain exact Git-object identity with the frozen source snapshot, prior validation evidence attached to that canonical source remains applicable to those unchanged product objects.

This record does not relabel the historical controlled-distribution 81/90-control workflows as proof of the new public-release boundary. Those workflows and their evidence remain historical/R&D records.

## Build and package contract review

Direct review confirms:

- `pyproject.toml` declares package `tebdlc`, version `0.1.0`, Python `>=3.11`, and console entry point `tebdlc = tebdlc.cli:main`;
- the public README build/test/verify/sanitize commands correspond to actual `Makefile` targets;
- `make release-check` calls `tools/release_readiness.py`;
- required public product families are present in the assembled tree.

## Workflow-cost boundary

The inherited controlled-distribution workflows `rc-validation.yml` and `cross-runtime-proof.yml` have been changed to manual `workflow_dispatch` only on the assembly branch. They therefore do not automatically run merely because the branch is later fast-forwarded into public `main`.

## Secret / unrelated-private-material review

The release assembly was reviewed for obvious credential/private-key/token patterns and no exposed operational credential was identified. Earlier targeted checks against the selected source material likewise found no GitHub PAT/private-key markers. The repository hygiene policy excludes local environment secrets and private-key material by default.

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
- `README.md` and `NOTICE.md`.

Earlier controlled-distribution documents remain preserved as historical records and do not govern the publication boundary of this first public Release Candidate.

## Verification verdict

**PASS.**

The assembled public product is materially bound to the frozen TEBDLC product snapshot for all shared product objects, while the public overlays are explicitly separated and documented. No product subtree was simplified or replaced by metadata-only material.
