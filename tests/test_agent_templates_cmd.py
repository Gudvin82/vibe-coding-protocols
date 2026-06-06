from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AgentTemplatesCommandTests(unittest.TestCase):
    def test_copilot_template_json(self) -> None:
        proc = subprocess.run([
            'python3', '-m', 'vcp_cli', 'agents', 'template', '--agent', 'copilot', '--json'
        ], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload['ok'])
        self.assertEqual(payload['agent'], 'copilot')
        self.assertIn('COPILOT_INSTRUCTIONS.md', payload['path'])

    def test_copilot_template_write(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / '.github' / 'copilot-instructions.md'
            proc = subprocess.run([
                'python3', '-m', 'vcp_cli', 'agents', 'template', '--agent', 'copilot', '--output', str(target), '--confirm', '--json'
            ], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertTrue(target.exists())
            self.assertIn('not an official Copilot plugin', target.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
