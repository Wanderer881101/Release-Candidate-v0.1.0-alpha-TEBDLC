# TEBDLC v0.1.0-alpha — Controlled Release Gate

**Jonathan Therrien, Marieville, Québec.**

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
- [x] Material private package assembled deterministically from the bound source commit and independently rechecked byte-for-byte.
- [x] Real package SHA-256 persisted: `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`.
- [x] Real package contains 139 tracked files and reconstructs the exact expected source root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [x] Final release manifest persisted privately; manifest SHA-256: `ee8cff12529b190b7f9fcf7028a61a32af50f68dc3bfa6c39b24411f85521826`.
- [x] Clean-room v0.2 materially completed against the exact real package with `tests_ok: true` and `source_tree_match: true`.

## Verification note

The active public reference/release-tooling battery contains **90 controls**. GitHub-hosted Python 3.11.16, 3.12.14 and 3.13.15 each execute all 90 successfully. Concordance matrix schema `tebdlc-runtime-concordance/0.4` reports the same normalized output SHA-256 across all three runtimes: `4dc648dfe39adfbd35b2d76783e9525ad52b82c9e82a1e0cad2cd1e141e90954`.

The private product candidate is materially bound at the Git-object level. Its exact source commit is `677a28d87164379cb2a268e55cfc30302ebc44ab`; the commit object points to root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`.

A real deterministic archive has been produced from that exact source. Its immutable SHA-256 is `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`, its tracked file count is 139, and independent reconstruction from the archive yields the same expected Git root tree.

The clean-room record reports `source_tree_match: true`, `tests_ok: true`, expected and observed root tree both `63658d334ae8c3d280e9ef2c29845fffce2747e6`, licence SHA-256 `86fddddedbd112c2c8b420d4b31802147a3bce702ff68db3683b816b39e69ac1`, territorial-policy SHA-256 `1e0a639c10ae2d124f4d535536788b19912903f310c9e494d57e6fbcba9b6090`, and manifest SHA-256 `ee8cff12529b190b7f9fcf7028a61a32af50f68dc3bfa6c39b24411f85521826`.

## Controlled-source distribution blockers

- [x] Materially confirm the active 90-control compatibility battery on Python 3.11 / 3.12 / 3.13.
- [x] Confirm cross-runtime semantic concordance for all 90 controls.
- [x] Resolve and persist the exact canonical private source commit and complete Git-tree Merkle identity.
- [x] Bind clean-room verification to the expected private Git root tree.
- [x] Implement and test the authenticated Git-object → canonical archive assembly path.
- [x] Materially produce the real `v0.1.0-alpha` archive from the bound private source.
- [x] Calculate and persist the immutable package SHA-256 and final release manifest bound to source commit `677a28d87164379cb2a268e55cfc30302ebc44ab` and root tree `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [x] Run `distribution/clean_room_verify.py` against that exact real package, active licence and territorial policy and persist the clean-room success record.
- [x] Place the verified package in a private controlled package store and exercise the real controlled-delivery path.
- [x] Verify authorized and denied deliveries, pre/post-delivery SHA equality, territorial resolution, authentication/authorization decisions and append-only audit-chain continuity against the real package.
- [x] Execute reference/adversarial suites against the deployed/private-package environment and persist results/hashes.
- [x] Complete applicable operational controls from `distribution/OPERATIONAL_ACCEPTANCE_v0.1.md` for the current deployment boundary: HTTPS transport, secrets handling, isolation, ACL/least privilege, abuse/rate-limit boundary, monitoring, backup/recovery and incident/revocation procedures.
- [x] Verify recipient/provenance records bind recipient identity, resolved territory, authorization decision, licence/policy versions, delivered package hash and audit checkpoint without storing raw secrets.
- [x] Preserve formal falsification attribution and contributor intellectual-property provenance in the isolated falsification registry.
- [x] Complete applicable mandatory-law/export/sanctions operational review and record required transaction-time adjustments in `distribution/LEGAL_MANDATORY_RULE_CHECKPOINT_v0.1.md`.
- [x] Persist immutable final distribution proof in private evidence as `FINAL_DISTRIBUTION_PROOF.json`.
- [x] Persist final audit checkpoint in private evidence as `FINAL_AUDIT_CHECKPOINT.json`, sequence `3`, checkpoint hash `64105fb03f89f28434bf565d55dd57302455a5eeccf1c7360ac65cf6e7221f00`.
- [x] Final consolidation/freeze readiness gate completed successfully.
- [x] Canonical Git tag `v0.1.0-alpha` frozen on the exact private source commit `677a28d87164379cb2a268e55cfc30302ebc44ab`; tag/source comparison is `identical` with `ahead_by=0`, `behind_by=0`.

## External legal status

The project licence is active as TEBDLC project policy. No claim is made that it has received governmental, judicial, or specialist legal certification. Mandatory applicable law prevails where required, without silently rewriting historical distribution provenance.

`distribution/LEGAL_MANDATORY_RULE_CHECKPOINT_v0.1.md` records the external fail-closed conditions. Real external controlled delivery remains transaction-dependent and requires current export-classification/destination/sanctions/privacy checks as applicable.

## Hard publication invariant

**DO NOT COPY THE COMPLETE CONTROLLED TEBDLC SOURCE PACKAGE TO PUBLIC `main`.**

The public repository may host intentionally global governance, policy, provenance formats, release metadata, hashes and documentation that do not disclose controlled source material.

## Release identity

Release identity: `v0.1.0-alpha`
Freeze status: `FROZEN`
Canonical private tag target: `677a28d87164379cb2a268e55cfc30302ebc44ab`
Private source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`
Private source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`
Real package SHA-256: `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`
Release manifest SHA-256: `ee8cff12529b190b7f9fcf7028a61a32af50f68dc3bfa6c39b24411f85521826`
Licence SHA-256: `86fddddedbd112c2c8b420d4b31802147a3bce702ff68db3683b816b39e69ac1`
Territorial policy SHA-256: `1e0a639c10ae2d124f4d535536788b19912903f310c9e494d57e6fbcba9b6090`
Active runtime baseline: `90 controls`
Cross-runtime normalized proof SHA-256: `4dc648dfe39adfbd35b2d76783e9525ad52b82c9e82a1e0cad2cd1e141e90954`
Clean-room status: `PASS`
Final distribution proof: `SEALED_FREEZE_READY`
Final audit checkpoint: `SEALED`
Tag freeze evidence: private `TAG_FREEZE_RECORD.json`, status `FROZEN`

All controlled-distribution blockers are closed for the frozen `v0.1.0-alpha` identity. Real external controlled delivery remains subject to the transaction-time mandatory-rule conditions documented in the legal checkpoint.
