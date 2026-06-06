
from __future__ import annotations
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ProofCountsSyncTests(unittest.TestCase):
    def test_canonical_file_exists(self):
        data = json.loads((ROOT / '.vcp' / 'proof-counts.json').read_text())
        self.assertEqual(data['version'], (ROOT / 'VERSION').read_text().strip())
        self.assertIn('counts', data)
