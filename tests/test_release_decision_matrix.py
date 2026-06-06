
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ReleaseDecisionMatrixTests(unittest.TestCase):
    def test_states_exist(self):
        data = json.loads((ROOT / '.vcp/release-decision-matrix.example.json').read_text())
        self.assertTrue(any(item['id'] == 'can-ship-public' for item in data['states']))
