
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class EvaluationStatusBadgesTests(unittest.TestCase):
    def test_badges_are_honest(self):
        data = json.loads((ROOT / '.vcp/evaluation-status-badges.json').read_text())
        self.assertTrue(any(item['id'] == 'client-rollout-ready' for item in data['items']))
