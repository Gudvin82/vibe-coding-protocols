from __future__ import annotations

import unittest

from vcp_cli.review_diff import _classify_areas, _estimate_risk


class ReviewDiffRiskTests(unittest.TestCase):
    def test_manifest_change_is_high_risk(self) -> None:
        changed = [".vcp/manifests/vcp.manifest.json"]
        areas = _classify_areas(changed)
        risk, reasons = _estimate_risk(changed, areas)
        self.assertEqual(risk, "high")
        self.assertTrue(any("manifest" in reason.lower() for reason in reasons))

    def test_docs_only_is_low_risk(self) -> None:
        changed = ["docs/install.md"]
        areas = _classify_areas(changed)
        risk, _ = _estimate_risk(changed, areas)
        self.assertEqual(risk, "low")


if __name__ == "__main__":
    unittest.main()
