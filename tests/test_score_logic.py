from __future__ import annotations

import unittest

from vcp_cli.score import _build_payload


class ScoreLogicTests(unittest.TestCase):
    def test_score_payload_contains_categories(self) -> None:
        payload = _build_payload()
        self.assertIn("score", payload)
        self.assertGreaterEqual(payload["score"], 0)
        names = {item["name"] for item in payload["categories"]}
        self.assertIn("Public growth and AI visibility", names)


if __name__ == "__main__":
    unittest.main()
