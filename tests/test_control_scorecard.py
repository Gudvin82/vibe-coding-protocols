
from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ControlScorecardTests(unittest.TestCase):
    def test_scorecard_json(self):
        proc = subprocess.run(['python3','-m','vcp_cli','scorecard','--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data['version'], (ROOT / 'VERSION').read_text().strip())
