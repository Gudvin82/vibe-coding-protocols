
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class AIToolModePacksTests(unittest.TestCase):
    def test_mode_packs_exist(self):
        data = json.loads((ROOT / '.vcp/ai-tool-mode-packs.json').read_text())
        self.assertGreaterEqual(len(data['items']), 4)
