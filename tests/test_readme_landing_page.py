from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeLandingPageTests(unittest.TestCase):
    def test_readme_contains_landing_page_sections(self) -> None:
        text = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('AI agents can generate MVPs quickly', text)
        self.assertIn('## 5-minute demo', text)
        self.assertIn('## Before / after', text)
        self.assertIn('## Use with your AI tools', text)
        self.assertIn('docs/comparisons.md', text)
        self.assertIn('docs/product-model.md', text)
        self.assertIn('EVALUATE_THIS_REPO.md', text)
        self.assertIn('docs/anti-misread-guide.md', text)
        self.assertIn('docs/proof-snapshot.md', text)
        self.assertIn('docs/agent-model-routing.md', text)
        self.assertIn('docs/evaluator-token-budget.md', text)
        self.assertIn('docs/evaluation-receipt.md', text)
        self.assertIn('docs/public-proof-demo.md', text)
        self.assertIn('docs/community-and-adoption-status.md', text)
        self.assertIn('assets/diagrams/vcp-control-layer-map.svg', text)
        self.assertIn('v0.8.9', text)
        self.assertIn('Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/', text)


if __name__ == '__main__':
    unittest.main()
