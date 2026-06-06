from __future__ import annotations

import json
import unittest
from pathlib import Path

from vcp_cli import change_cmd

ROOT = Path(__file__).resolve().parents[1]


class ChangeIntentTests(unittest.TestCase):
    def test_surfaces_exist(self) -> None:
        for rel in ('docs/change-intent.md', 'docs_ru/change-intent.md', 'schemas/change-intent.schema.json', '.vcp/change-intent.example.json', 'templates/reports/change-intent.md'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_example_validates(self) -> None:
        data = json.loads((ROOT / '.vcp/change-intent.example.json').read_text(encoding='utf-8'))
        self.assertEqual(change_cmd.validate_change_intent_data(data, ROOT), [])

    def test_intent_payload(self) -> None:
        payload = change_cmd.example_payload(ROOT)
        self.assertEqual(payload['version'], 'v0.9.2')

    def test_validation_payload(self) -> None:
        payload = json.loads((ROOT / '.vcp/change-intent.example.json').read_text(encoding='utf-8'))
        self.assertEqual(change_cmd.validate_change_intent_data(payload, ROOT), [])


if __name__ == '__main__':
    unittest.main()
