from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IntegrationsCommandTests(unittest.TestCase):
    def test_list_all(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'integrations', 'list', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn('count', payload)
        self.assertIn('counts', payload)

    def test_filter_by_status(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'integrations', 'list', '--status', 'shipped', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload['status_filter'], 'shipped')

    def test_packs_list(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'integrations', 'packs', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn('count', payload)
        self.assertIn('items', payload)

    def test_invalid_status_fails(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'integrations', 'list', '--status', 'bogus', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertNotEqual(proc.returncode, 0)

if __name__ == '__main__':
    unittest.main()
