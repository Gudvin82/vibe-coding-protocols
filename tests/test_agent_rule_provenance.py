from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'shipped', 'optional', 'experimental', 'roadmap-only', 'not-shipped'}


class AgentRuleProvenanceTests(unittest.TestCase):
    def test_docs_and_json_exist(self) -> None:
        for rel in ('docs/agent-rule-provenance.md', 'docs_ru/agent-rule-provenance.md', '.vcp/agent-rule-provenance.json'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_profiles_listed_and_statuses_valid(self) -> None:
        profiles = json.loads((ROOT / '.vcp/agent-rule-profiles.json').read_text(encoding='utf-8'))
        provenance = json.loads((ROOT / '.vcp/agent-rule-provenance.json').read_text(encoding='utf-8'))
        self.assertEqual({item['id'] for item in profiles['items']}, {item['id'] for item in provenance['items']})
        self.assertTrue(all(item['status'] in ALLOWED for item in provenance['items']))


if __name__ == '__main__':
    unittest.main()
