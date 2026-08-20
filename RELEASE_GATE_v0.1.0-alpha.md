# TEBDLC v0.1.0-alpha — Controlled Release Gate

This gate prevents accidental publication of the complete territorially controlled source through a globally public GitHub branch.

## Completed governance and reference-implementation prerequisites

- [x] Public Release Candidate repository exists.
- [x] Evidence-safe `.gitignore` policy established.
- [x] Isolated `falsification-registry` branch established.
- [x] Falsification attribution/provenance policy established.
- [x] Territorial policy v0.1 established.
- [x] Caribbean classification corrected to NEUTRAL.
- [x] Explicit restricted territorial entries recorded from the approved policy inputs.
- [x] Sovereign source-available licence activated as project licence v0.1.
- [x] Rights matrix for PRIVILEGED / NEUTRAL / RESTRICTED established.
- [x] PRIVILEGED and NEUTRAL rights made identical except for the formal TEBDLC falsification right.
- [x] NEUTRAL ordinary testing, benchmarking, debugging and private evaluation preserved without granting participation in the formal falsification regime.
- [x] Recipient authorization/decision contract v0.1 specified.
- [x] Licence acceptance, distribution-event and release-manifest schemas added.
- [x] Stdlib-only fail-closed record validator added.
- [x] Deterministic Caribbean and restricted-region annexes added.
- [x] Deterministic territorial resolver added with narrow-rule precedence and fail-closed default.
- [x] Explicit non-regression coverage added for Switzerland (`CH -> PRIVILEGED`) and Belgium (`BE -> PRIVILEGED`).
- [x] Recipient authentication reference implementation and credential lifecycle added.
- [x] Integrated authentication + territorial resolution + rights authorization engine added.
- [x] Controlled-delivery reference primitive added with pre-copy/copy/post-copy SHA verification and atomic promotion.
- [x] Hash-chained append-only audit log reference added; existing chain is verified before append.
- [x] Audited delivery wrapper persists ALLOW and DENY outcomes without storing the raw presented secret.
- [x] Controlled-distribution threat model and private deployment specification added.
- [x] Clean-room verification harness added.
- [x] Public executable validation persisted with `overall_pass: true`.
- [x] Base distribution/reference suite totals: validator 8, resolver 13, authentication 8, authorization 8, controlled delivery 10, audit 5, adversarial distribution 18, adversarial end-to-end 11 — **81 controls**.
- [x] Git-tree/archive binding suite added with 4 controls.
- [x] Authenticated private-Git assembler added with 5 executable controls covering known Git object vectors, one-byte mutation, deterministic rebuild, archive/tree round-trip and symlink round-trip.
- [x] Active executable baseline raised to **90 controls**.
- [x] GitHub-hosted compatibility proof materially completed on Python 3.11.16, 3.12.14 and 3.13.15: **90/90 PASS on all three runtimes**.
- [x] Cross-runtime semantic concordance v0.4 confirmed: all three runtimes produce normalized output SHA-256 `4dc648dfe39adfbd35b2d76783e9525ad52b82c9e82a1e0cad2cd1e141e90954`.
- [x] Clean-room v0.2 binds a candidate archive to its expected Git root tree in addition to package/licence/policy SHA-256 values.
- [x] Exact private source candidate bound to PR #4 branch `proof/r6-executable-invariants`, commit `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Exact private Git root-tree Merkle identity persisted: `63658d334ae8c3d280e9ef2c29845fffce2747e6`; recursive authenticated Git-tree query returned `truncated:false`.
- [x] Public non-disclosing source-tree proof persisted in `validation/PRIVATE_SOURCE_TREE_PROOF.json`.
- [x] Operational acceptance gate persisted in `distribution/OPERATIONAL_ACCEPTANCE_v0.1.md`.
- [x] Material-proof boundary and private-package attempts recorded without substituting synthetic/package-placeholder hashes for the real package.

## Verification note

The active public reference/release-tooling battery now contains **90 controls**. GitHub-hosted Python 3.11.16, 3.12.14 and 3.13.15 each execute all 90 successfully. Concordance matrix schema `tebdlc-runtime-concordance/0.4` reports the same normalized output SHA-256 across all three runtimes: `4dc648dfe39adfbd35b2d76783e9525ad52b82c9e82a1e0cad2cd1e141e90954`.

The private product candidate is materially bound at the Git-object level. Its exact source commit is `677a28d87164379cb2a268e55cfc30302ebc44ab`; the commit object points to root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`. A recursive authenticated Git-tree query for that candidate is complete (`truncated:false`).

`distribution/assemble_private_git_tree.py` is the current material assembly path. It authenticates to GitHub, verifies every fetched blob against its Git SHA-1, rebuilds the complete source tree locally, requires exact root-tree equality, creates a canonical deterministic tar.gz, rebuilds it byte-for-byte, and emits `PACKAGE_PROOF.json` plus `SHA256SUMS`.

The current ChatGPT lab does not expose a `GITHUB_TOKEN` or `GH_TOKEN`; therefore the private blobs cannot yet be fetched into that container. No real package SHA-256 is claimed until a token-bearing/private-source-readable execution actually produces the archive.

## Blocking before controlled source distribution

- [x] Materially confirm the active 90-control compatibility battery on Python 3.11 / 3.12 / 3.13.
- [x] Confirm cross-runtime semantic concordance for all 90 controls.
- [x] Resolve and persist the exact canonical private source commit and complete Git-tree Merkle identity.
- [x] Bind clean-room verification to the expected private Git root tree.
- [x] Implement and test the authenticated Git-object → canonical archive assembly path.
- [ ] Execute that assembly path in an environment able to authenticate to/read the bound private source and materially produce the real `v0.1.0-alpha` archive.
- [ ] Calculate and persist the immutable package SHA-256 and final release manifest bound to source commit `677a28d87164379cb2a268e55cfc30302ebc44ab` and root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [ ] Run `distribution/clean_room_verify.py` against that exact real package, active licence and territorial policy and persist `CLEAN_ROOM_PASS`.
- [ ] Place the verified package in a private controlled package store and exercise the real controlled-delivery path.
- [ ] Verify authorized and denied deliveries, pre/post-delivery SHA equality, territorial resolution, authentication/authorization decisions and append-only audit-chain continuity against the real package.
- [ ] Execute reference/adversarial suites against the deployed/private-package environment and persist results/hashes.
- [ ] Complete production operational controls from `distribution/OPERATIONAL_ACCEPTANCE_v0.1.md` (TLS, secrets/KMS, isolation, ACLs, rate limiting, monitoring, backup/recovery, incident/revocation procedures as applicable).
- [ ] Verify recipient/provenance records bind recipient identity, resolved territory, authorization decision, licence/policy versions, delivered package hash and audit checkpoint without storing raw secrets.
- [ ] Preserve formal falsification attribution and contributor intellectual-property provenance in the isolated falsification registry.
- [ ] Complete applicable mandatory-law/export/sanctions review and record any required operational adjustment.
- [ ] Persist immutable final release manifest, real-package verification record, policy/licence hashes, distribution proof and final audit checkpoint.
- [ ] Freeze/tag the release identity only after all preceding blockers are closed.

## External legal status

The project licence is active as TEBDLC project policy. No claim is made that it has received governmental, judicial, or specialist legal certification. Mandatory applicable law prevails where required, without silently rewriting historical distribution provenance.

## Hard publication invariant

**DO NOT COPY THE COMPLETE CONTROLLED TEBDLC SOURCE PACKAGE TO PUBLIC `main` WHILE ANY CONTROLLED-DISTRIBUTION BLOCKER ABOVE REMAINS OPEN.**

The public repository may continue to host intentionally global governance, policy, provenance formats, release metadata, hashes and documentation that do not disclose controlled source material.

## Release identity

Candidate: `v0.1.0-alpha`
Private source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`
Private source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`
Active runtime baseline: `90 controls`
Cross-runtime normalized proof SHA-256: `4dc648dfe39adfbd35b2d76783e9525ad52b82c9e82a1e0cad2cd1e141e90954`

The final controlled package must receive its own immutable SHA-256, manifest SHA-256, licence version/hash, territorial-policy version/hash, build/verification record, delivery proof and audit checkpoint before release identity is frozen.
