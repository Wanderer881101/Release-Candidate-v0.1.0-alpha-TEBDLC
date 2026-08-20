import unittest
from resolve_territory import resolve


class TerritorialResolverTests(unittest.TestCase):
    def test_quebec_privileged(self):
        self.assertEqual(resolve("CA", "QC")["state"], "PRIVILEGED")

    def test_ottawa_restricted(self):
        self.assertEqual(resolve("CA", "ON", "Ottawa")["state"], "RESTRICTED")

    def test_france_privileged(self):
        self.assertEqual(resolve("FR")["state"], "PRIVILEGED")

    def test_florida_privileged(self):
        self.assertEqual(resolve("US", "FL")["state"], "PRIVILEGED")

    def test_new_york_restricted(self):
        self.assertEqual(resolve("US", "NY")["state"], "RESTRICTED")

    def test_jamaica_neutral(self):
        self.assertEqual(resolve("JM")["state"], "NEUTRAL")

    def test_puerto_rico_neutral(self):
        self.assertEqual(resolve("PR")["state"], "NEUTRAL")

    def test_israel_restricted(self):
        self.assertEqual(resolve("IL")["state"], "RESTRICTED")

    def test_iran_restricted(self):
        self.assertEqual(resolve("IR")["state"], "RESTRICTED")

    def test_unknown_fail_closed(self):
        result = resolve("ZZ")
        self.assertEqual(result["state"], "RESTRICTED")
        self.assertEqual(result["reason"], "DEFAULT_RESTRICTED")

    def test_missing_country_fail_closed(self):
        result = resolve("")
        self.assertEqual(result["state"], "RESTRICTED")
        self.assertEqual(result["reason"], "DENY_UNRESOLVED_TERRITORY")


if __name__ == "__main__":
    unittest.main()
