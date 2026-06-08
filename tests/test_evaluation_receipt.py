from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

from vcp_cli import evaluator_cmd

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()


class EvaluationReceiptTests(unittest.TestCase):
    def test_schema_and_example_exist(self) -> None:
        self.assertTrue((ROOT / 'schemas/evaluation-receipt.schema.json').exists())
        self.assertTrue((ROOT / '.vcp/evaluation-receipt.example.json').exists())

    def test_example_validates(self) -> None:
        data = json.loads((ROOT / '.vcp/evaluation-receipt.example.json').read_text(encoding='utf-8'))
        self.assertEqual(evaluator_cmd.validate_receipt_data(data, ROOT), [])

    def test_cli_receipt_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'evaluator', 'receipt', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload['version'], CURRENT)

    def test_cli_receipt_validate_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'evaluator', 'receipt', 'validate', '.vcp/evaluation-receipt.example.json', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload['ok'])


if __name__ == '__main__':
    unittest.main()
