from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ModelRoutingDocsTests(unittest.TestCase):
    def test_routing_docs_exist(self) -> None:
        for rel in (
            'docs/agent-model-routing.md',
            'docs_ru/agent-model-routing.md',
            'docs/evaluator-token-budget.md',
            'docs_ru/evaluator-token-budget.md',
        ):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_templates_mention_cost_aware_routing(self) -> None:
        for rel in (
            'templates/agents/CLAUDE.md',
            'templates/agents/CODEX.md',
            'templates/agents/CURSOR_RULES.md',
            'templates/agents/AGENTS.md',
        ):
            text = (ROOT / rel).read_text(encoding='utf-8')
            self.assertIn('model routing', text.lower())

    def test_evaluator_pack_has_token_budget_levels(self) -> None:
        payload = json.loads((ROOT / '.vcp/evaluator-pack.json').read_text(encoding='utf-8'))
        self.assertEqual([item['level'] for item in payload['token_budget_levels']], [0, 1, 2, 3])
