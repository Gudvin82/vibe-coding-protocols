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
        self.assertIn('v0.8.6', text)


if __name__ == '__main__':
    unittest.main()
