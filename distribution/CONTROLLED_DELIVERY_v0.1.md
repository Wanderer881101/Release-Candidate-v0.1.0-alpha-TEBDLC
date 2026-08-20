# TEBDLC Controlled Delivery v0.1

Status: REFERENCE IMPLEMENTATION / NOT A PUBLIC NETWORK SERVICE

## Purpose

`controlled_delivery.py` is the reference delivery primitive for the controlled TEBDLC package. It is intentionally designed around a private/local package path and an authorized output directory. It is not a public GitHub download mechanism and it does not create a public HTTP endpoint.

## Required chain

A successful delivery requires all of the following to agree:

`credential -> subject -> declared territory -> territorial state -> granted DOWNLOAD_PACKAGE right -> licence acceptance -> release manifest -> exact package SHA-256 -> atomic verified copy`

Any failed link produces `DENY`.

## Integrity requirements

The implementation verifies the package before copying, verifies the temporary delivered copy, and verifies the source again before the temporary copy is atomically promoted to its final destination. This is intended to detect package corruption or mutation during the delivery operation.

The acceptance record must bind to the authenticated subject, resolved territorial state, release ID, licence version/hash, territorial-policy version/hash, and exact package SHA-256 recorded by the release manifest.

## Path protections

The source must be a regular non-symlink file. Source and final destination may not resolve to the same path. Delivery uses a temporary file in the output filesystem and atomic replacement only after integrity verification succeeds.

## No secret persistence

`controlled_delivery.py` receives a presented secret for authentication but does not write that secret into the delivery result. Raw credentials must not be recorded in manifests, acceptance records, audit events, repository history, or logs.

## Delivery result

An allowed result records only the minimum delivery metadata required for provenance: subject identifier, credential identifier, territorial state, acceptance identifier, release identifier, package SHA-256, delivered filename, timestamp, reason code, and delivery-engine version.

A production system should transform this result into the versioned distribution-event record defined by the distribution schema and append it to an audit mechanism that preserves historical integrity.

## Fail-closed examples

Delivery is denied when authentication fails, territory is restricted, package hash differs, acceptance identity differs from the authenticated identity, acceptance territorial state differs from the newly resolved state, release IDs differ, licence/policy hashes differ, package is unavailable, or path integrity cannot be established.

## Deployment boundary

This reference implementation is suitable for integration into a controlled off-GitHub delivery service or operator workflow. The repository does not claim that such an external production deployment already exists merely because the reference primitive exists.
