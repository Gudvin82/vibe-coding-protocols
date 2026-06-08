from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ModelToolGovernanceTests(unittest.TestCase):
    def test_surfaces_exist(self) -> None:
        for rel in [
            'docs/model-tool-governance.md',
            'docs_ru/model-tool-governance.md',
            'schemas/model-tool-dependency.schema.json',
            '.vcp/model-tool-dependencies.example.json',
            'templates/reports/model-tool-dependency-review.md',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_cli_example_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'model-tools', 'example', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload['ok'])
        self.assertEqual(payload['version'], 'v0.9.4')
        self.assertTrue(payload['items'])


if __name__ == '__main__':
    unittest.main()
