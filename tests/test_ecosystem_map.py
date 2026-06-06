from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EcosystemMapTests(unittest.TestCase):
    def test_docs_exist(self) -> None:
        for rel in ('docs/ecosystem-map.md', 'docs_ru/ecosystem-map.md'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_boundaries_are_respectful(self) -> None:
        text = (ROOT / 'docs/ecosystem-map.md').read_text(encoding='utf-8')
        self.assertIn('VCP complements adjacent tools and does not replace them.', text)
        self.assertIn('Spec Kit', text)
        self.assertIn('OpenSpec-like tools', text)
        self.assertNotIn('official integration', text.lower())


if __name__ == '__main__':
    unittest.main()
