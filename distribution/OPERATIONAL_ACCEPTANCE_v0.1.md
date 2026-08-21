# TEBDLC v0.1.0-alpha — Operational Acceptance Gate

This document is additive to `RELEASE_GATE_v0.1.0-alpha.md`, `DEPLOYMENT_SPEC_v0.1.md`, `THREAT_MODEL_v0.1.md`, `AUTHORIZATION_SPEC_v0.1.md`, and `CONTROLLED_DELIVERY_v0.1.md`.

It defines the minimum material evidence required before a controlled TEBDLC package may be treated as operationally ready. A checkbox may be marked complete only from persisted evidence; intent, configuration text, or synthetic-only results are not substitutes.

## A. Immutable candidate identity

- [x] Candidate release identifier: `v0.1.0-alpha`.
- [x] Private source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Private source root-tree SHA-1: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [x] Real canonical package SHA-256 persisted: `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`.
- [x] Real package size and tracked-file count persisted: `162053` bytes / `139` tracked files.
- [x] Final manifest SHA-256 persisted: `ee8cff12529b190b7f9fcf7028a61a32af50f68dc3bfa6c39b24411f85521826`.
- [x] Active licence SHA-256 persisted in the final manifest: `86fddddedbd112c2c8b420d4b31802147a3bce702ff68db3683b816b39e69ac1`.
- [x] Active territorial-policy SHA-256 persisted in the final manifest: `1e0a639c10ae2d124f4d535536788b19912903f310c9e494d57e6fbcba9b6090`.

Evidence: private branch `release-evidence-v0.1.0-alpha`, `PACKAGE_PROOF.json`, `RELEASE_MANIFEST.json`, `SHA256SUMS`.

## B. Package construction and clean-room proof

- [x] Authenticated Git-object assembler implemented fail-closed.
- [x] Every fetched blob must match its Git blob SHA-1.
- [x] Rebuilt root tree must match the bound source root tree before packaging.
- [x] Canonical package rebuild must be byte-identical before acceptance.
- [x] Clean-room verifier binds archive contents back to the expected Git root tree.
- [x] Real package assembled from the bound private Git objects.
- [x] Real package passes clean-room verification.
- [x] `CLEAN_ROOM_PASS` record persisted with package/tree/licence/policy hashes.

Evidence: `CLEAN_ROOM_RECORD.json`, `CLEAN_ROOM_STDOUT.txt`, package SHA-256 and source-tree identity above.

## C. Controlled store and transport

- [x] Verified package stored outside globally public GitHub source exposure, as a private GitHub Actions artifact associated with the private `TEBDLC` repository.
- [x] Package store defaults to deny and exposes no anonymous listing/download path. Material probe returned anonymous download HTTP `401` and anonymous artifact listing HTTP `404`.
- [ ] TLS is enabled for every network hop carrying credentials, authorization records or package bytes. GitHub-hosted HTTPS is used by the current store workflow, but an end-to-end production transport boundary has not yet been independently certified here.
- [ ] Storage and delivery service identities use least privilege across the final production deployment.
- [x] Package-at-rest access is constrained by the private repository / GitHub Actions artifact access boundary and authenticated service identity; anonymous readback is materially denied.
- [ ] Secrets/credentials are not committed, logged, embedded in manifests, or returned in audit records across the complete deployment. Existing persisted release/store/adversarial evidence records explicitly contain no raw secret, but a complete secret-leak scan remains required.
- [ ] Secret rotation and revocation procedure is documented and tested.
- [ ] Rate limiting / abuse throttling is active where the service is remotely reachable.

Controlled-store evidence: run `32436626437`, artifact `9430960453`, `CONTROLLED_STORE_RECORD.json`; pre-store and post-readback package SHA-256 are identical and byte-for-byte readback is true.

## D. Recipient decision and delivery proof

For each real delivery attempt, persist a non-secret record binding:

- recipient/account identifier;
- credential/key identifier (never the raw secret);
- resolved territory and policy version;
- authorization decision and reason;
- accepted licence version/hash;
- requested release identifier;
- expected package SHA-256;
- pre-delivery package SHA-256;
- post-delivery/destination SHA-256 when delivery occurs;
- audit event/checkpoint identifier;
- timestamp in UTC.

The current material adversarial package run proves the behavioral delivery gates below. A dedicated complete per-attempt provenance record covering every binding listed above remains required before Section D is wholly closed.

Material tests required:

- [x] At least one permitted delivery completes with pre/post SHA equality against the exact package `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`.
- [x] At least one policy-denied request produces no package delivery.
- [x] At least one authentication failure produces no package delivery.
- [x] At least one integrity mismatch/tamper scenario fails closed.
- [x] Audit chain remains valid after ALLOW and DENY outcomes; deliberate audit tampering is detected.

Evidence: `CONTROLLED_DISTRIBUTION_RECORD.json`, `ADVERSARIAL_PRIVATE_ENVIRONMENT_RECORD.json`, `PRIVATE_PACKAGE_ADVERSARIAL_RECORD.json`; adversarial run `32438606191`; 18 distribution + 11 end-to-end reference controls PASS plus 6 material real-package cases PASS.

## E. Falsification and intellectual-property provenance

- [ ] Formal falsification is accepted only under the territorial/rights policy in force.
- [ ] NEUTRAL users remain outside the formal falsification regime while retaining permitted ordinary evaluation rights.
- [ ] Every formal falsification record binds the original TEBDLC release identity and the falsifier/contributor identity/version provenance.
- [ ] Contributor/falsifier intellectual-property attribution is additive; TEBDLC origin/provenance is never removed or rewritten.
- [ ] Falsification records remain isolated from the controlled private source package and cannot silently alter the released candidate.

## F. Operations and resilience

- [ ] Monitoring detects authorization failures, integrity failures, repeated denied requests and delivery errors without recording raw secrets.
- [ ] Backup/recovery procedure exists for package store, policy/licence records and audit chain.
- [ ] Recovery is tested and preserves package hashes/audit continuity.
- [ ] Incident procedure defines package/credential revocation, audit preservation and recipient notification where applicable.
- [ ] Service isolation boundaries and filesystem/network permissions are documented from the actual deployment.

## G. Legal/mandatory-rule checkpoint

- [ ] Applicable mandatory law, export controls and sanctions constraints are reviewed for the actual distribution operation.
- [ ] Any required restriction/exception is recorded as an operational adjustment with date, scope and authority/source.
- [ ] No historical licence/policy/provenance record is silently rewritten after an external legal adjustment.

## H. Final freeze

Release identity MUST NOT be frozen/tagged until sections A–G are materially satisfied or explicitly documented as not applicable with evidence.

Final release binding must include at minimum:

`release_id ↔ source_commit ↔ source_tree_sha1 ↔ package_sha256 ↔ manifest_sha256 ↔ licence_sha256 ↔ territorial_policy_sha256 ↔ clean_room_record ↔ distribution/audit_checkpoint`

The release remains a candidate while any applicable item above is open.
