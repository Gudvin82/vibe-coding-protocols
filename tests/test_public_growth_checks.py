from __future__ import annotations

import unittest

from vcp_cli.public_growth import payload


class PublicGrowthCheckTests(unittest.TestCase):
    def test_public_growth_payload_has_no_guarantees(self) -> None:
        data = payload()
        self.assertIn("technical_seo_readiness", data)
        self.assertIn("No ranking guarantees.", data["guarantees"])
        self.assertIn(data["network"]["status"], {"not_requested", "ok", "network_unavailable", "http_error"})


if __name__ == "__main__":
    unittest.main()
