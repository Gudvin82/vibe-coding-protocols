from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BacklogModelTests(unittest.TestCase):
    def test_audit_backlog_validate(self) -> None:
        path = ROOT / '.vcp' / 'audit-backlog.example.json'
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'backlog', 'validate', str(path), '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload['ok'])

    def test_audit_backlog_summarize(self) -> None:
        path = ROOT / '.vcp' / 'audit-backlog.example.json'
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'backlog', 'summarize', str(path), '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload['count'], 2)

if __name__ == '__main__':
    unittest.main()
