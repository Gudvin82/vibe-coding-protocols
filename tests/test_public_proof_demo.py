from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicProofDemoTests(unittest.TestCase):
    def test_demo_files_exist(self) -> None:
        required = [
            'examples/public-proof/README.md',
            'examples/public-proof/before-raw-ai-mvp.md',
            'examples/public-proof/after-vcp-launch-control-package.md',
            'examples/public-proof/route-example.json',
            'examples/public-proof/risk-backlog-example.json',
            'examples/public-proof/pr-gate-example.json',
            'examples/public-proof/metrics-board-example.json',
            'examples/public-proof/launch-decision-example.md',
            'examples/public-proof/trust-check-example.json',
            'docs/public-proof-demo.md',
            'docs_ru/public-proof-demo.md',
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)


if __name__ == '__main__':
    unittest.main()
