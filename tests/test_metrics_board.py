from __future__ import annotations

import unittest

from vcp_cli.metrics_cmd import payload


class MetricsBoardTests(unittest.TestCase):
    def test_metrics_payload_includes_core_counts(self) -> None:
        data = payload()
        self.assertIn("cards_count", data)
        self.assertIn("benchmark_scenario_count", data)
        self.assertIn("integration_status_counts", data)
        self.assertIn("release_readiness", data)


if __name__ == "__main__":
    unittest.main()
