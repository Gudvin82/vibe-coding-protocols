from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicProofSurfacesTests(unittest.TestCase):
    def test_proof_strip_visible(self) -> None:
        proof = json.loads((ROOT / '.vcp/proof-counts.json').read_text(encoding='utf-8'))['counts']
        required = [
            f"benchmark scenarios: `{proof['benchmark_scenarios']}`",
            f"cards: `{proof['cards']}`",
            f"CLI commands in manifest: `{proof['cli_commands_in_manifest']}`",
            f"tests: `{proof['tests']}`",
            f"report templates: `{proof['report_templates']}`",
            'trust-check: yes',
            'evaluator pack: yes',
        ]
        for rel in ('README.md', 'README_ru.md', 'docs/proof-snapshot.md', 'docs_ru/proof-snapshot.md'):
            text = (ROOT / rel).read_text(encoding='utf-8')
            for needle in required:
                self.assertIn(needle, text, f'{rel}: {needle}')


if __name__ == '__main__':
    unittest.main()
