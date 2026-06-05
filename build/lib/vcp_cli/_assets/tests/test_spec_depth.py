from __future__ import annotations

import unittest

from vcp_cli.spec_cmd import _classify_spec_depth


class SpecDepthTests(unittest.TestCase):
    def test_no_spec_keywords(self) -> None:
        payload = _classify_spec_depth("small docs typo only")
        self.assertEqual(payload["recommended_spec_depth"], "no-spec")

    def test_spec_lite_keywords(self) -> None:
        payload = _classify_spec_depth("build a customer dashboard with acceptance criteria and review notes")
        self.assertEqual(payload["recommended_spec_depth"], "spec-lite")

    def test_governed_keywords(self) -> None:
        payload = _classify_spec_depth("payments, personal data, compliance, release gate")
        self.assertEqual(payload["recommended_spec_depth"], "governed-spec")


if __name__ == "__main__":
    unittest.main()
