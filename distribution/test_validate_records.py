#!/usr/bin/env python3
import copy
import unittest
from validate_records import ValidationError, validate_acceptance, validate_event, validate_manifest

H = "a" * 64
C = "b" * 40

class ValidatorTests(unittest.TestCase):
    def acceptance(self, state="PRIVILEGED"):
        return {
            "acceptance_id":"ACC-00000001","authorization_identity":"user-1","declared_territory":"Québec, Canada",
            "territorial_state":state,"licence_version":"0.1","licence_sha256":H,
            "territorial_policy_version":"0.1","territorial_policy_sha256":H,"tebdlc_release":"v0.1.0-alpha",
            "package_sha256":H,"accepted_at":"2026-08-20T13:00:00Z","acceptance_mechanism_version":"0.1"
        }

    def event(self, state="PRIVILEGED", action="DELIVER_PACKAGE", decision="ALLOW", reason="ALLOW_PRIVILEGED"):
        return {
            "event_id":"EVT-00000001","acceptance_id":"ACC-00000001","authorization_identity":"user-1",
            "declared_territory":"Québec, Canada","territorial_state":state,"policy_version":"0.1",
            "policy_sha256":H,"licence_version":"0.1","licence_sha256":H,"tebdlc_release":"v0.1.0-alpha",
            "package_sha256":H,"requested_action":action,"decision":decision,"reason_code":reason,
            "timestamp":"2026-08-20T13:01:00Z","authorization_engine_version":"0.1"
        }

    def manifest(self):
        return {
            "manifest_version":"0.1","release_id":"v0.1.0-alpha","source_commits":[C],"package_sha256":H,
            "assembly_procedure_version":"0.1","licence_version":"0.1","licence_sha256":H,
            "territorial_policy_version":"0.1","territorial_policy_sha256":H,"verification_record_sha256":H,
            "created_at":"2026-08-20T13:02:00Z"
        }

    def test_privileged_allow(self):
        validate_acceptance(self.acceptance())
        validate_event(self.event())

    def test_neutral_allow_non_falsification(self):
        validate_acceptance(self.acceptance("NEUTRAL"))
        validate_event(self.event("NEUTRAL", "TEST", "ALLOW", "ALLOW_NEUTRAL"))

    def test_neutral_falsification_denied(self):
        validate_event(self.event("NEUTRAL", "FALSIFY", "DENY", "DENY_RIGHT_NOT_GRANTED"))
        bad = self.event("NEUTRAL", "FALSIFY", "ALLOW", "ALLOW_NEUTRAL")
        with self.assertRaises(ValidationError):
            validate_event(bad)

    def test_restricted_must_deny(self):
        e = self.event("RESTRICTED", "DELIVER_PACKAGE", "DENY", "DENY_RESTRICTED_TERRITORY")
        e.pop("acceptance_id")
        validate_event(e)
        with self.assertRaises(ValidationError):
            validate_event(self.event("RESTRICTED", "DELIVER_PACKAGE", "ALLOW", "ALLOW_PRIVILEGED"))

    def test_restricted_acceptance_forbidden(self):
        with self.assertRaises(ValidationError):
            validate_acceptance(self.acceptance("RESTRICTED"))

    def test_bad_hash_rejected(self):
        a = self.acceptance(); a["package_sha256"] = "bad"
        with self.assertRaises(ValidationError):
            validate_acceptance(a)

    def test_manifest(self):
        validate_manifest(self.manifest())
        m = self.manifest(); m["source_commits"] = [C, C]
        with self.assertRaises(ValidationError):
            validate_manifest(m)

    def test_unknown_field_rejected(self):
        e = self.event(); e["surprise"] = True
        with self.assertRaises(ValidationError):
            validate_event(e)

if __name__ == "__main__":
    unittest.main(verbosity=2)
