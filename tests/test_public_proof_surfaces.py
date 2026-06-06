from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicProofSurfacesTests(unittest.TestCase):
    def test_proof_strip_visible(self) -> None:
        required = [
            'benchmark scenarios: `151`',
            'cards: `287`',
            'CLI commands in manifest: `76`',
            'tests: `107`',
            'report templates: `44`',
            'trust-check: yes',
            'evaluator pack: yes',
        ]
        for rel in ('README.md', 'README_ru.md', 'docs/proof-snapshot.md', 'docs_ru/proof-snapshot.md'):
            text = (ROOT / rel).read_text(encoding='utf-8')
            for needle in required:
                self.assertIn(needle, text, f'{rel}: {needle}')


if __name__ == '__main__':
    unittest.main()
