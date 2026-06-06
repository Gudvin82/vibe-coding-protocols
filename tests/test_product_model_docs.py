from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProductModelDocsTests(unittest.TestCase):
    def test_product_model_exists_and_is_linked(self) -> None:
        text = (ROOT / 'docs/product-model.md').read_text(encoding='utf-8')
        self.assertIn('## Core', text)
        self.assertIn('## Guided Paths', text)
        self.assertIn('## Optional Layers', text)
        self.assertIn('## Roadmap-only', text)
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/product-model.md', readme)


if __name__ == '__main__':
    unittest.main()
