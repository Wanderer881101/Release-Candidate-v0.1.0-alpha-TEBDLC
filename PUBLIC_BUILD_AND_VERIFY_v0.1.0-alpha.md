# TEBDLC v0.1.0-alpha — Public Build and Verification Clarification

**Jonathan Therrien, Marieville, Québec.**

Status: **ACTIVE PUBLIC-RELEASE OVERLAY**

This document clarifies how `docs/BUILD_AND_VERIFY.md` is interpreted for the first public `v0.1.0-alpha` Release Candidate while preserving the canonical `docs/` subtree unchanged.

## Local product contract remains active

The local product commands documented in `docs/BUILD_AND_VERIFY.md` remain the supported verification contract for this Release Candidate:

```text
make setup
make build
make test
make verify
make sanitize
make clean
```

The Python, C11, GMP, OpenSSL/libcrypto, zlib and Clang prerequisites documented there remain applicable to the corresponding targets.

## Public GitHub workflow status

The statement in section 7 of `docs/BUILD_AND_VERIFY.md` describing a CI workflow that directly reproduces `make test-python`, `make test-c` and `make sanitize` reflects the earlier source/development state and is not the active public-repository workflow configuration.

For this public Release Candidate, the two workflows currently retained under `.github/workflows/` are historical controlled-distribution validation workflows. They are manual `workflow_dispatch` only and do not automatically execute on pushes to `main`.

They must not be represented as the primary product-build proof for this public Release Candidate.

## Pre-release decisions

The earlier open decisions listed in section 8 of `docs/BUILD_AND_VERIFY.md` are resolved for this Release Candidate only to the extent explicitly covered by the active public-release documents, including the active licence, `.gitignore`, release model and publication gate. Unresolved platform-support or signing questions must not be silently presented as completed unless separately recorded.

## Preservation rule

This overlay does not rewrite the canonical `docs/` subtree. It records the public-release interpretation needed because the publication architecture evolved after that canonical document was frozen.
