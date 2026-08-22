# TEBDLC Controlled Distribution — Private Deployment Specification v0.1

**Jonathan Therrien, Marieville, Québec.**

Status: REFERENCE DEPLOYMENT CONTRACT

## Objective

Define the minimum operational boundary for a controlled TEBDLC distributor without making the globally public GitHub repository the controlled source endpoint.

## Trust boundary

The deployment must separate at least four zones:

1. **Public governance zone** — public GitHub policy/specification repository. Contains no controlled complete source package or recipient secrets.
2. **Authorization zone** — authentication registry, territorial resolver, rights engine, licence acceptance processing, and audit writer.
3. **Private package vault** — immutable controlled TEBDLC package(s) addressed by content hash. Not directly web-browsable and not mounted read-write by the public edge.
4. **Delivery zone** — short-lived authorized transfer path that receives an already-authorized immutable package identity and emits only that package.

The public governance zone must never be trusted as proof that a recipient is authorized.

## Minimum deployment properties

- fail closed on unavailable dependencies or ambiguous state;
- no raw recipient credential or package secret committed to Git;
- package vault defaults read-only to the distributor;
- package names are not sufficient identity: SHA-256 and release manifest are authoritative;
- authorization decision occurs before package bytes are exposed;
- output is generated from an immutable package identity;
- every allow/deny attempt generates an audit event;
- audit chain is persisted outside ephemeral process storage;
- package, licence and policy hashes are bound to the licence-acceptance record;
- privilege is not inferred from source IP;
- NEUTRAL cannot invoke the formal falsification right;
- RESTRICTED cannot receive the controlled package;
- public GitHub compromise must not grant controlled source access by itself.

## Suggested filesystem model

Example only; paths are implementation-specific:

```text
/srv/tebdlc/
  policy-ro/              # reviewed policy snapshot used by authorization service
  vault-ro/
    v0.1.0-alpha/
      <sha256>.pkg
      release-manifest.json
  auth-private/
    recipient-registry.json
  audit-append/
    distribution-events.jsonl
  staging-private/
  delivery-ephemeral/
```

Permissions should ensure the public-facing process cannot modify the package vault, policy snapshot, licence snapshot, or historical audit chain.

## Package-vault rules

1. Package content is immutable after manifest issuance.
2. Mutation requires a new package hash and new release/manifest identity.
3. File name is informational only.
4. The package is hashed immediately before delivery.
5. Delivery code must reject symbolic-link source packages.
6. A manifest may point to only one exact package SHA for one release assembly.
7. Vault backup and disaster-recovery copies must preserve package hashes.

## Authorization data

Recipient registry must be private. It should contain only the minimum attributes needed by the authorization engine. Raw passwords/tokens are forbidden in persistent registry data; use password verifiers or a dedicated authentication provider.

Territory is a declared/verified authorization attribute, not a transient-IP synonym.

## Licence acceptance

Acceptance must occur against the exact:

- licence version/hash;
- territorial-policy version/hash;
- TEBDLC release ID;
- package SHA-256;
- resolved territorial state.

Changing any bound item requires a new acceptance record unless the active licence expressly specifies otherwise.

## Delivery transaction

A delivery transaction should perform, in order:

1. authenticate recipient;
2. resolve recipient account and declared territory;
3. resolve territorial state;
4. authorize requested right;
5. validate licence acceptance and identity binding;
6. validate release manifest;
7. verify package source path and reject symlink/path collapse;
8. hash package and compare to manifest;
9. stage copy in private destination filesystem;
10. hash staged copy;
11. re-hash source to detect mutation during transfer;
12. atomically publish staged copy to authorized delivery destination;
13. append audit record;
14. return delivery receipt containing package hash and event identity.

Any failure before step 12 must produce no usable delivered package.

## Audit durability

The reference hash chain detects mutation/deletion but does not itself prevent an attacker with full storage control from replacing the entire log. A production deployment should anchor audit-chain checkpoints outside the distributor's writable trust boundary, for example in offline signed checkpoints or a separately administered append-only store.

## Network exposure

The current reference code is local-storage oriented and does not define a public HTTP API. A later network wrapper must not weaken the authorization transaction. In particular, signed URLs or object-store URLs must be minted only after successful authorization and should be short lived, single-purpose, and bound to the exact object/hash where the storage provider permits it.

## Secret management

Production secrets should be provided at runtime through an appropriate secret-management mechanism. They must not be stored in the public GitHub repository, release manifests, audit events, or distributed package.

## Backup/recovery

Recovery must preserve:

- controlled package bytes and hashes;
- release manifests;
- licence/policy snapshots and hashes;
- recipient authorization state as legally/operationally required;
- audit-chain continuity and external checkpoints.

A recovered system must re-run integrity verification before resuming delivery.

## Pre-activation requirement

The reference distributor may be considered implemented when its code exists. A **production controlled delivery** is not considered deployed until the package vault, private authorization registry, persistent audit store, runtime secret handling, access controls, backups, and adversarial tests are exercised in the actual target environment.
