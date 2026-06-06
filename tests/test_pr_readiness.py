
from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class PRReadinessTests(unittest.TestCase):
    def test_pr_readiness_json(self):
        proc = subprocess.run(['python3','-m','vcp_cli','pr','readiness','--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn('checks', data)
