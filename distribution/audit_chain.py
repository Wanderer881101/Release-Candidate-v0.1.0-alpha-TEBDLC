#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
"""Compatibility import surface for the TEBDLC v0.1 audit chain.

Canonical implementation: audit_log.py
This shim preserves the originally referenced audit_chain module name while the
repository converges on one canonical naming convention.
"""
from audit_log import AUDIT_VERSION, GENESIS, append_event, verify_chain

__all__ = ["AUDIT_VERSION", "GENESIS", "append_event", "verify_chain"]
