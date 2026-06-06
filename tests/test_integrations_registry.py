from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'shipped', 'local-template', 'experimental', 'roadmap', 'not-shipped'}


class IntegrationRegistryTests(unittest.TestCase):
    def test_registry_has_required_entries(self) -> None:
        payload = json.loads((ROOT / '.vcp' / 'integrations.json').read_text(encoding='utf-8'))
        ids = {item['id'] for item in payload['items']}
        for required in {
            'python-cli', 'installed-vcp-console-script', 'npm-wrapper', 'github-actions-pr-gate-template',
            'local-dashboard-artifact', 'plugin-contract-draft', 'pypi-publication', 'npm-publication',
            'vs-code-extension', 'hosted-dashboard', 'plugin-marketplace', 'go-cli-rewrite',
            'docs-site-scaffold', 'integration-packs-registry',
        }:
            self.assertIn(required, ids)

    def test_statuses_are_allowed(self) -> None:
        payload = json.loads((ROOT / '.vcp' / 'integrations.json').read_text(encoding='utf-8'))
        self.assertTrue(all(item['status'] in ALLOWED for item in payload['items']))
        vscode = next(item for item in payload['items'] if item['id'] == 'vs-code-extension')
        self.assertEqual(vscode['status'], 'roadmap')

    def test_integration_packs_registry_exists(self) -> None:
        payload = json.loads((ROOT / '.vcp' / 'integration-packs.json').read_text(encoding='utf-8'))
        self.assertEqual(payload['version'], 'v0.8.7')
        self.assertGreaterEqual(len(payload['items']), 8)
        self.assertTrue(all(item['status'] in ALLOWED for item in payload['items']))

if __name__ == '__main__':
    unittest.main()
