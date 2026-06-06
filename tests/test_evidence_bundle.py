
from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class EvidenceBundleTests(unittest.TestCase):
    def test_example_exists(self):
        data = json.loads((ROOT / '.vcp/evidence-bundle.example.json').read_text())
        self.assertIn('bundle_sections', data)
