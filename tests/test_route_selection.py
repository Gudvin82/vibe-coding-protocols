from __future__ import annotations

import unittest

from vcp_cli.classify import classify_payload


class RouteSelectionTests(unittest.TestCase):
    def test_classify_returns_track_and_tier(self) -> None:
        payload = classify_payload()
        self.assertIn(payload["track"], {"New Project Track", "Existing Project Track"})
        self.assertIn(payload["suggested_tier"], {"Lite", "Team", "Governed"})
        self.assertIn("suggested_route", payload)


if __name__ == "__main__":
    unittest.main()
