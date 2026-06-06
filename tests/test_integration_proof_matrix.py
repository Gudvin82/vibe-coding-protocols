
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class IntegrationProofMatrixTests(unittest.TestCase):
    def test_all_kits_present(self):
        data = json.loads((ROOT / '.vcp/integration-proof-matrix.json').read_text())
        ids = {item['id'] for item in data['items']}
        self.assertEqual(ids, {'claude','codex','cursor','copilot','github-actions'})
