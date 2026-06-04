from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IntegrationRegistryTests(unittest.TestCase):
    def test_registry_has_required_entries(self) -> None:
        payload = json.loads((ROOT / '.vcp' / 'integrations.json').read_text(encoding='utf-8'))
        ids = {item['id'] for item in payload['items']}
        for required in {
            'python-cli',
            'installed-vcp-console-script',
            'npm-wrapper',
            'github-actions-pr-gate-template',
            'local-dashboard-artifact',
            'plugin-contract-draft',
            'pypi-publication',
            'npm-publication',
            'vs-code-extension',
            'hosted-dashboard',
            'plugin-marketplace',
            'go-cli-rewrite',
        }:
            self.assertIn(required, ids)


if __name__ == '__main__':
    unittest.main()
