
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class GuidedAdoptionModesTests(unittest.TestCase):
    def test_modes_exist(self):
        data = json.loads((ROOT / '.vcp/guided-adoption-modes.json').read_text())
        self.assertEqual([item['id'] for item in data['items']], ['5-minute','30-minute','half-day','full-audit'])
