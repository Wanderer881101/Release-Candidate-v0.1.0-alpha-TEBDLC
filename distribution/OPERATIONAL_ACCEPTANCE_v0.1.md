# TEBDLC v0.1.0-alpha — Operational Acceptance Gate

This document is additive to `RELEASE_GATE_v0.1.0-alpha.md`, `DEPLOYMENT_SPEC_v0.1.md`, `THREAT_MODEL_v0.1.md`, `AUTHORIZATION_SPEC_v0.1.md`, and `CONTROLLED_DELIVERY_v0.1.md`.

It defines the minimum material evidence required before a controlled TEBDLC package may be treated as operationally ready. A checkbox may be marked complete only from persisted evidence; intent, configuration text, or synthetic-only results are not substitutes.

## A. Immutable candidate identity

- [x] Candidate release identifier: `v0.1.0-alpha`.
- [x] Private source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Private source root-tree SHA-1: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [ ] Real canonical package SHA-256 persisted.
- [ ] Real package size and tracked-file count persisted.
- [ ] Final manifest SHA-256 persisted.
- [ ] Active licence SHA-256 persisted in the final manifest.
- [ ] Active territorial-policy SHA-256 persisted in the final manifest.

## B. Package construction and clean-room proof

- [x] Authenticated Git-object assembler implemented fail-closed.
- [x] Every fetched blob must match its Git blob SHA-1.
- [x] Rebuilt root tree must match the bound source root tree before packaging.
- [x] Canonical package rebuild must be byte-identical before acceptance.
- [x] Clean-room verifier binds archive contents back to the expected Git root tree.
- [ ] Real package assembled from the bound private Git objects.
- [ ] Real package passes clean-room verification.
- [ ] `CLEAN_ROOM_PASS` record persisted with package/tree/licence/policy hashes.

## C. Controlled store and transport

- [ ] Verified package stored outside globally public GitHub.
- [ ] Package store defaults to deny and exposes no anonymous listing/download path.
- [ ] TLS is enabled for every network hop carrying credentials, authorization records or package bytes.
- [ ] Storage and delivery service identities use least privilege.
- [ ] Package-at-rest access is constrained by ACL/service identity.
- [ ] Secrets/credentials are not committed, logged, embedded in manifests, or returned in audit records.
- [ ] Secret rotation and revocation procedure is documented and tested.
- [ ] Rate limiting / abuse throttling is active where the service is remotely reachable.

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

Material tests required:

- [ ] At least one permitted delivery completes with pre/post SHA equality.
- [ ] At least one policy-denied request produces no package delivery.
- [ ] At least one authentication failure produces no package delivery.
- [ ] At least one integrity mismatch/tamper scenario fails closed.
- [ ] Audit chain remains valid after ALLOW and DENY outcomes.

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
