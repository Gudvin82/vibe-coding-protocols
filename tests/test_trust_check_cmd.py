from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TrustCheckCommandTests(unittest.TestCase):
    def test_trust_check_returns_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'trust-check', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn(payload['status'], {'pass', 'warn', 'fail'})
        self.assertEqual(payload['version'], 'v0.8.8')
        self.assertIn('checks', payload)
        self.assertIn('summary', payload)
        check_ids = {item['id'] for item in payload['checks']}
        self.assertIn('version-surfaces', check_ids)
        self.assertIn('roadmap-overclaim', check_ids)
        self.assertIn('changelog-hygiene', check_ids)
        self.assertIn('evaluator-pack', check_ids)
        self.assertIn('evaluator-surfaces', check_ids)
        details = {item['id']: item for item in payload['checks']}
        self.assertIn('token-budget', details['evaluator-surfaces']['summary'])


if __name__ == '__main__':
    unittest.main()
