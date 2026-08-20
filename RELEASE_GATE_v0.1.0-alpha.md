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
- [x] Public executable validation persisted in `validation/LAST_EXECUTION.json` with `overall_pass: true`.
- [x] Executed suite totals: validator 8, resolver 13, authentication 8, authorization 8, controlled delivery 10, audit 5, adversarial distribution 18, adversarial end-to-end 11 — **81 controls total**.
- [x] First executable pass defects were identified and corrected: resolver direct-execution import mismatch, audit-chain naming compatibility, and obsolete clean-room audit-test filename.
- [x] Clean-room harness materially exercised with an isolated synthetic package and the real active licence/policy SHA-256 values; persisted `CLEAN_ROOM_PASS` in `validation/CLEAN_ROOM_HARNESS_EXECUTION.json`.
- [x] Validation workflow hardened to require the expected 81-control baseline and fail on silent test-count regression.
- [x] GitHub-hosted compatibility proof materially completed on Python 3.11.16, 3.12.14 and 3.13.15: **81/81 PASS on all three runtimes**.
- [x] Cross-runtime semantic concordance v0.2 confirmed: 3.11 / 3.12 / 3.13 produce the same normalized output SHA-256 after removing Python-version and unittest wall-clock noise.
- [x] Exact private source candidate bound to PR #4 branch `proof/r6-executable-invariants`, commit `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Exact private Git root-tree Merkle identity persisted: `63658d334ae8c3d280e9ef2c29845fffce2747e6`; recursive private tree query returned `truncated:false`.
- [x] Public non-disclosing source-tree proof persisted in `validation/PRIVATE_SOURCE_TREE_PROOF.json`.
- [x] Material-proof boundary and private-package attempts recorded without substituting synthetic/package-placeholder hashes for the real package.

## Verification note

The public reference/distribution system is materially exercised, not merely reviewable. GitHub-hosted Python 3.11.16, 3.12.14 and 3.13.15 each execute the full 81-control battery successfully. The v0.2 concordance matrix reports identical normalized output hashes across all three runtimes.

The private product candidate is now also materially bound at the Git-object level. Its exact source commit is `677a28d87164379cb2a268e55cfc30302ebc44ab`; the commit object points to root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`. A recursive authenticated Git-tree query for that candidate is complete (`truncated:false`). This establishes exact Merkle identity of the tracked private source content without publishing that source.

This Git tree proof is **not** the same object as the final distribution archive SHA-256. The archive must still be materially assembled and hashed before controlled release.

A private GitHub Actions packaging job was installed and scheduled for the canonical PR lineage, but the hosted private runner failed before exposing any executable step and produced no artifact/log blob. No product or packaging-script failure is inferred from that non-execution. The authenticated Git-object API is therefore being used as the source-reading path instead of pretending the runner succeeded.

## Blocking before controlled source distribution

- [x] Materially confirm the public 81-control compatibility battery on Python 3.11 / 3.12 / 3.13.
- [x] Resolve and persist the exact canonical private source commit and complete Git-tree Merkle identity.
- [ ] Materially reconstruct/assemble the exact controlled `v0.1.0-alpha` distribution archive from the bound private Git tree.
- [ ] Calculate and persist the immutable package SHA-256 and final release manifest bound to source commit `677a28d87164379cb2a268e55cfc30302ebc44ab` and root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [ ] Run the already-proven `distribution/clean_room_verify.py` against that exact real package, active licence and territorial policy and persist `CLEAN_ROOM_PASS`.
- [ ] Deploy/operate the controlled-delivery reference outside globally public GitHub against a private controlled package store.
- [ ] Execute the reference/adversarial suites against that deployed/private-package environment and persist results/hashes.
- [ ] Add production operational controls appropriate to the selected hosting environment (TLS, secret/KMS handling, service isolation, ACLs, rate limiting, monitoring and backup/recovery as applicable).
- [ ] Applicable mandatory-law/export/sanctions review and any required operational adjustment.
- [ ] Persist immutable release manifest, real-package verification record, policy/licence hashes and final audit checkpoint for the delivered candidate.

## External legal status

The project licence is active as TEBDLC project policy. No claim is made that it has received governmental, judicial, or specialist legal certification. Mandatory applicable law prevails where required, without silently rewriting historical distribution provenance.

## Hard publication invariant

**DO NOT COPY THE COMPLETE CONTROLLED TEBDLC SOURCE PACKAGE TO PUBLIC `main` WHILE ANY CONTROLLED-DISTRIBUTION BLOCKER ABOVE REMAINS OPEN.**

The public repository may continue to host intentionally global governance, policy, provenance formats, release metadata, and documentation that does not disclose controlled source material.

## Release identity

Candidate: `v0.1.0-alpha`
Private source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`
Private source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`

The final controlled package must receive its own immutable SHA-256, manifest, licence version, territorial-policy version, build/verification record and audit checkpoint before delivery.
