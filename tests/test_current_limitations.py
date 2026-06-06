
from __future__ import annotations
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class CurrentLimitationsTests(unittest.TestCase):
    def test_docs_exist(self):
        self.assertTrue((ROOT / 'docs/current-limitations.md').exists())
        self.assertTrue((ROOT / 'docs_ru/current-limitations.md').exists())
