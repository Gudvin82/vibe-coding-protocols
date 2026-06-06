from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ['claude', 'codex', 'cursor', 'copilot', 'github-actions']


class AgentKitsCommandTests(unittest.TestCase):
    def test_all_targets_json(self) -> None:
        for target in TARGETS:
            with self.subTest(target=target):
                proc = subprocess.run([
                    'python3', '-m', 'vcp_cli', 'agents', 'kit', '--target', target, '--json'
                ], cwd=ROOT, text=True, capture_output=True, check=False)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                payload = json.loads(proc.stdout)
                self.assertTrue(payload['ok'])
                self.assertEqual(payload['target'], target)
                self.assertTrue(payload['not_official_plugin'])
                self.assertTrue(payload['files'])

    def test_write_mode_requires_confirm(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'vcp-copilot-kit'
            proc = subprocess.run([
                'python3', '-m', 'vcp_cli', 'agents', 'kit', '--target', 'copilot', '--output', str(target), '--json'
            ], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertNotEqual(proc.returncode, 0)
            payload = json.loads(proc.stdout)
            self.assertIn('requires --confirm', payload['error'])

    def test_dry_run_does_not_write(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'vcp-copilot-kit'
            proc = subprocess.run([
                'python3', '-m', 'vcp_cli', 'agents', 'kit', '--target', 'copilot', '--output', str(target), '--confirm', '--dry-run', '--json'
            ], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertTrue(payload['dry_run'])
            self.assertFalse(target.exists())

    def test_write_mode_writes_expected_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'vcp-copilot-kit'
            proc = subprocess.run([
                'python3', '-m', 'vcp_cli', 'agents', 'kit', '--target', 'copilot', '--output', str(target), '--confirm', '--json'
            ], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertTrue((target / 'README.md').exists())
            self.assertTrue((target / 'copilot-instructions.md').exists())
            self.assertTrue((target / 'github-workflow-vcp-pr-gate.yml').exists())

    def test_no_overwrite_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'vcp-copilot-kit'
            target.mkdir()
            (target / 'README.md').write_text('existing', encoding='utf-8')
            proc = subprocess.run([
                'python3', '-m', 'vcp_cli', 'agents', 'kit', '--target', 'copilot', '--output', str(target), '--confirm', '--json'
            ], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertNotEqual(proc.returncode, 0)
            payload = json.loads(proc.stdout)
            self.assertIn('overwrite', payload['error'])


if __name__ == '__main__':
    unittest.main()
