from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EcosystemScoutingWorkflowTests(unittest.TestCase):
    def test_surfaces_exist(self) -> None:
        for rel in [
            'docs/ecosystem-scouting-workflow.md',
            'docs_ru/ecosystem-scouting-workflow.md',
            'templates/reports/ecosystem-scouting-note.md',
            '.vcp/ecosystem-scouting-workflow.json',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_cli_scout(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'ecosystem', 'scout', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload['ok'])
        self.assertIn('steps', payload)


if __name__ == '__main__':
    unittest.main()
