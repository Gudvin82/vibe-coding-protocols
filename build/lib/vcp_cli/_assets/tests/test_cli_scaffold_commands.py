from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CliScaffoldCommandTests(unittest.TestCase):
    def test_dashboard_build_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run(
                ['python3', '-m', 'vcp_cli', 'dashboard', 'build', '--output', str(Path(tmp) / 'dash'), '--json'],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertTrue(payload['ok'])
            self.assertIn('index.html', payload['generated_files'])

    def test_plugins_list_json(self) -> None:
        proc = subprocess.run(
            ['python3', '-m', 'vcp_cli', 'plugins', 'list', '--json'],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertGreaterEqual(len(payload['items']), 1)

    def test_metrics_board_json(self) -> None:
        proc = subprocess.run(
            ['python3', '-m', 'vcp_cli', 'metrics', 'board', '--json'],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn('cards_count', payload)


if __name__ == '__main__':
    unittest.main()
