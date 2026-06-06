from __future__ import annotations

import json
import unittest
from pathlib import Path

from vcp_cli import charter_cmd

ROOT = Path(__file__).resolve().parents[1]


class ProjectControlCharterTests(unittest.TestCase):
    def test_surfaces_exist(self) -> None:
        for rel in ('docs/project-control-charter.md', 'docs_ru/project-control-charter.md', 'templates/project-control-charter.md', 'schemas/project-control-charter.schema.json', '.vcp/project-control-charter.example.json'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_example_validates(self) -> None:
        data = json.loads((ROOT / '.vcp/project-control-charter.example.json').read_text(encoding='utf-8'))
        self.assertEqual(charter_cmd.validate_charter_data(data, ROOT), [])

    def test_validation_helper(self) -> None:
        payload = json.loads((ROOT / '.vcp/project-control-charter.example.json').read_text(encoding='utf-8'))
        self.assertEqual(charter_cmd.validate_charter_data(payload, ROOT), [])


if __name__ == '__main__':
    unittest.main()
