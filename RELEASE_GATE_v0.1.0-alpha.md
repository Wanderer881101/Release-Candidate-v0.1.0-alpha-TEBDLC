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
- [x] Git-tree/archive binding suite added with 4 controls: known Git-tree vector, one-byte mutation, duplicate-path rejection, and traversal rejection.
- [x] Active executable baseline raised to **85 controls**.
- [x] GitHub-hosted compatibility proof materially completed on Python 3.11.16, 3.12.14 and 3.13.15: **85/85 PASS on all three runtimes**.
- [x] Cross-runtime semantic concordance v0.3 confirmed: all three runtimes produce normalized output SHA-256 `66b8e73171d66b753b5c0d5e1ed288999ea597f7026bba7c68ba4ac176e7b96e`.
- [x] Clean-room v0.2 binds a candidate archive to its expected Git root tree in addition to package/licence/policy SHA-256 values.
- [x] Exact private source candidate bound to PR #4 branch `proof/r6-executable-invariants`, commit `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Exact private Git root-tree Merkle identity persisted: `63658d334ae8c3d280e9ef2c29845fffce2747e6`; recursive authenticated Git-tree query returned `truncated:false`.
- [x] Public non-disclosing source-tree proof persisted in `validation/PRIVATE_SOURCE_TREE_PROOF.json`.
- [x] Material-proof boundary and private-package attempts recorded without substituting synthetic/package-placeholder hashes for the real package.

## Verification note

The public reference/distribution system is materially exercised, not merely reviewable. GitHub-hosted Python 3.11.16, 3.12.14 and 3.13.15 each execute the full **85-control** active battery successfully. Concordance matrix schema `tebdlc-runtime-concordance/0.3` reports identical normalized output hashes across all three runtimes.

The private product candidate is materially bound at the Git-object level. Its exact source commit is `677a28d87164379cb2a268e55cfc30302ebc44ab`; the commit object points to root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`. A recursive authenticated Git-tree query for that candidate is complete (`truncated:false`). This establishes exact Merkle identity of the tracked private source content without publishing that source.

The Git root-tree identity is **not** the final distribution archive SHA-256. The archive must still be materially assembled, hashed, checked back against the expected Git tree, and then passed through clean-room verification.

The private hosted-runner packaging attempt failed before exposing executable steps and produced no artifact/log blob. No product or packaging-script failure is inferred from that non-execution. Authenticated Git-object API access is therefore the preferred source-reading path for the next material assembly attempt.

## Blocking before controlled source distribution

- [x] Materially confirm the active 85-control compatibility battery on Python 3.11 / 3.12 / 3.13.
- [x] Confirm cross-runtime semantic concordance for all 85 controls.
- [x] Resolve and persist the exact canonical private source commit and complete Git-tree Merkle identity.
- [x] Bind clean-room verification to the expected private Git root tree.
- [ ] Materially reconstruct/assemble the exact controlled `v0.1.0-alpha` distribution archive from the bound private Git tree.
- [ ] Calculate and persist the immutable package SHA-256 and final release manifest bound to source commit `677a28d87164379cb2a268e55cfc30302ebc44ab` and root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [ ] Run `distribution/clean_room_verify.py` against that exact real package, active licence and territorial policy and persist `CLEAN_ROOM_PASS`.
- [ ] Place the verified package in a private controlled package store and exercise the real controlled-delivery path.
- [ ] Verify authorized and denied deliveries, pre/post-delivery SHA equality, territorial resolution, authentication/authorization decisions and append-only audit-chain continuity against the real package.
- [ ] Execute reference/adversarial suites against the deployed/private-package environment and persist results/hashes.
- [ ] Add production operational controls appropriate to the selected hosting environment: TLS, secret/KMS handling, service isolation, ACLs, rate limiting, monitoring, backup/recovery and incident/revocation procedures as applicable.
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
Active runtime baseline: `85 controls`
Cross-runtime normalized proof SHA-256: `66b8e73171d66b753b5c0d5e1ed288999ea597f7026bba7c68ba4ac176e7b96e`

The final controlled package must receive its own immutable SHA-256, manifest SHA-256, licence version/hash, territorial-policy version/hash, build/verification record, delivery proof and audit checkpoint before release identity is frozen.
