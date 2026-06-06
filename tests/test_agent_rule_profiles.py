from __future__ import annotations

import json
import unittest
from pathlib import Path

from vcp_cli import profiles_cmd

ROOT = Path(__file__).resolve().parents[1]


class AgentRuleProfilesTests(unittest.TestCase):
    def test_profiles_exist(self) -> None:
        for rel in (
            'templates/agents/profiles/vcp-agent-rules.nano.md',
            'templates/agents/profiles/vcp-agent-rules.mini.md',
            'templates/agents/profiles/vcp-agent-rules.full.md',
            'templates/agents/profiles_ru/vcp-agent-rules.nano.md',
            'templates/agents/profiles_ru/vcp-agent-rules.mini.md',
            'templates/agents/profiles_ru/vcp-agent-rules.full.md',
            '.vcp/agent-rule-profiles.json',
            'docs/agent-rule-profiles.md',
            'docs_ru/agent-rule-profiles.md',
        ):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_profiles_validate(self) -> None:
        self.assertEqual(profiles_cmd.validate(ROOT), [])

    def test_profiles_payload(self) -> None:
        payload = profiles_cmd.list_payload(ROOT)
        self.assertEqual([item['id'] for item in payload['items']], ['nano', 'mini', 'full'])

    def test_profile_show_payload(self) -> None:
        payload = profiles_cmd.show_payload('mini', ROOT)
        self.assertEqual(payload['profile']['id'], 'mini')
        self.assertIn('Do not claim tests passed unless run.', payload['text'])


if __name__ == '__main__':
    unittest.main()
