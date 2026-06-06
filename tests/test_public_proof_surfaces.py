from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicProofSurfacesTests(unittest.TestCase):
    def test_proof_strip_visible(self) -> None:
        bench = json.loads((ROOT / '.vcp/manifests/benchmarks.manifest.json').read_text(encoding='utf-8'))
        reports = json.loads((ROOT / '.vcp/manifests/reports.manifest.json').read_text(encoding='utf-8'))
        commands = json.loads((ROOT / '.vcp/manifests/commands.manifest.json').read_text(encoding='utf-8'))
        cards_count = len(list((ROOT / '.vcp/cards').rglob('*.json')))
        tests_count = unittest.defaultTestLoader.discover(str(ROOT / 'tests')).countTestCases()
        required = [
            f"benchmark scenarios: `{len(bench['items'])}`",
            f"cards: `{cards_count}`",
            f"CLI commands in manifest: `{len(commands['items'])}`",
            f"tests: `{tests_count}`",
            f"report templates: `{len(reports['items'])}`",
            'trust-check: yes',
            'evaluator pack: yes',
        ]
        for rel in ('README.md', 'README_ru.md', 'docs/proof-snapshot.md', 'docs_ru/proof-snapshot.md'):
            text = (ROOT / rel).read_text(encoding='utf-8')
            for needle in required:
                self.assertIn(needle, text, f'{rel}: {needle}')


if __name__ == '__main__':
    unittest.main()
