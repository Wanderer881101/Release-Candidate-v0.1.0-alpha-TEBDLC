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
- [x] Executed suite totals: validator 8, resolver 13, authentication 8, authorization 8, controlled delivery 10, audit 5, adversarial distribution 18, adversarial end-to-end 11 — **81 controls total, all PASS** on GitHub-hosted Python 3.11.16.
- [x] First executable pass defects were identified and corrected: resolver direct-execution import mismatch, audit-chain naming compatibility, and obsolete clean-room audit-test filename.
- [x] Clean-room harness materially exercised with an isolated synthetic package and the real active licence/policy SHA-256 values; persisted `CLEAN_ROOM_PASS` in `validation/CLEAN_ROOM_HARNESS_EXECUTION.json`.
- [x] Validation workflow hardened to require the expected 81-control baseline and fail on silent test-count regression.
- [x] Python 3.11 / 3.12 / 3.13 compatibility matrix encoded in the validation workflow for the 81-control suite.
- [x] Material-proof boundary and private-package attempt recorded in `validation/MATERIAL_PROOF_STATUS.md`.

## Verification note

The public reference/distribution system is no longer merely reviewable code: it has been executed on GitHub-hosted Python 3.11.16, corrected from the first observed failures, and re-executed to a complete 81-control PASS. The territorial regression suite now explicitly protects Switzerland and Belgium as PRIVILEGED. The clean-room harness has also executed end-to-end and returned `CLEAN_ROOM_PASS` against material synthetic input bound to the active licence and territorial-policy hashes.

The 3.11/3.12/3.13 matrix is encoded as a required compatibility battery; a version is not to be described as materially confirmed until its corresponding execution result is available.

This does **not** substitute a synthetic artifact for the private TEBDLC product package.

A deterministic packaging attempt was made directly from the canonical private `Wanderer881101/TEBDLC` PR lineage. The private GitHub workflow reached workflow scheduling, but its Python 3.11/3.12/3.13 and C jobs terminated before any executable steps were exposed; the dependent package job was therefore skipped. No product failure is inferred from that non-executed private run. The private workflow was restored afterward to the quota-safe policy.

## Blocking before controlled source distribution

- [ ] Materially confirm the public 81-control compatibility battery on Python 3.12 and Python 3.13 (3.11 already PASS).
- [ ] Obtain an execution/archive path capable of reading the canonical private source tree as a whole and assemble the exact controlled `v0.1.0-alpha` source package.
- [ ] Calculate and persist the immutable package SHA-256 and final release manifest bound to the exact private source commit.
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

The final controlled package must receive its own immutable content hash, manifest, licence version, territorial-policy version, build/verification record and audit checkpoint before delivery.
