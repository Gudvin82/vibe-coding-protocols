from __future__ import annotations

import json
import unittest
from pathlib import Path

from vcp_cli import catalog_cmd

ROOT = Path(__file__).resolve().parents[1]


class ControlCatalogTests(unittest.TestCase):
    def test_docs_exist(self) -> None:
        for rel in ('docs/control-catalog.md', 'docs_ru/control-catalog.md', '.vcp/control-catalog.json'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_catalog_validates(self) -> None:
        self.assertEqual(catalog_cmd.validate(ROOT), [])

    def test_catalog_payload(self) -> None:
        payload = catalog_cmd.list_payload(ROOT)
        self.assertEqual(payload['version'], 'v0.9.1')
        self.assertGreaterEqual(payload['count'], 5)

    def test_catalog_explain_payload(self) -> None:
        payload = catalog_cmd.explain_payload('mvp-to-launch', ROOT)
        self.assertEqual(payload['entry']['id'], 'mvp-to-launch')


if __name__ == '__main__':
    unittest.main()
