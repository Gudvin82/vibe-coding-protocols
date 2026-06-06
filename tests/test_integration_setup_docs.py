from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IntegrationSetupDocsTests(unittest.TestCase):
    def test_setup_playbook_mentions_supported_targets(self) -> None:
        text = (ROOT / 'docs' / 'integrations' / 'setup-playbook.md').read_text(encoding='utf-8')
        for needle in (
            'Claude Code',
            'Codex',
            'Cursor',
            'GitHub Copilot',
            'GitHub Actions',
            'python3 -m vcp_cli agents template --agent claude',
            'python3 -m vcp_cli agents template --agent codex',
            'python3 -m vcp_cli agents template --agent cursor',
            'python3 -m vcp_cli agents template --agent copilot',
            'ci-examples/github-actions/vcp-pr-gate.yml',
        ):
            self.assertIn(needle, text)

    def test_russian_setup_guide_exists(self) -> None:
        text = (ROOT / 'docs_ru' / 'integration-setup.md').read_text(encoding='utf-8')
        for needle in ('Claude Code', 'Codex', 'Cursor', 'GitHub Copilot', 'GitHub Actions'):
            self.assertIn(needle, text)

    def test_agent_kit_docs_state_boundary(self) -> None:
        en = (ROOT / 'docs' / 'integrations' / 'agent-kits.md').read_text(encoding='utf-8')
        ru = (ROOT / 'docs_ru' / 'agent-kits.md').read_text(encoding='utf-8')
        self.assertIn('not official plugins', en)
        self.assertIn('Это не official plugins', ru)


if __name__ == '__main__':
    unittest.main()
