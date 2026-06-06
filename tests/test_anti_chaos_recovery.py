
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class AntiChaosRecoveryTests(unittest.TestCase):
    def test_workflow_exists(self):
        data = json.loads((ROOT / '.vcp/workflows/anti-chaos-recovery.json').read_text())
        self.assertEqual(data['id'], 'anti-chaos-recovery')
