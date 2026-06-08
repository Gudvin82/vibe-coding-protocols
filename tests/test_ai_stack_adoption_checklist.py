from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AIStackAdoptionChecklistTests(unittest.TestCase):
    def test_surfaces_exist(self) -> None:
        for rel in [
            'docs/ai-stack-adoption-checklist.md',
            'docs_ru/ai-stack-adoption-checklist.md',
            'templates/reports/ai-stack-adoption-checklist.md',
            '.vcp/ai-stack-adoption-checklist.example.json',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)


if __name__ == '__main__':
    unittest.main()
