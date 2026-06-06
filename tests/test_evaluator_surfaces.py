from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EvaluatorSurfacesTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [
            'EVALUATE_THIS_REPO.md',
            '.vcp/evaluator-pack.json',
            'docs/anti-misread-guide.md',
            'docs_ru/anti-misread-guide.md',
            'docs/proof-snapshot.md',
            'docs_ru/proof-snapshot.md',
            'docs/evaluator-architecture-map.md',
            'docs_ru/evaluator-architecture-map.md',
            'templates/reports/external-evaluation.md',
            'docs/agent-model-routing.md',
            'docs_ru/agent-model-routing.md',
            'docs/evaluator-token-budget.md',
            'docs_ru/evaluator-token-budget.md',
            'docs/visuals.md',
            'docs/visual-spec.md',
            'assets/diagrams/vcp-control-layer-map.svg',
            'assets/diagrams/vcp-product-model.svg',
            'assets/diagrams/vcp-comparison-map.svg',
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_readme_links_evaluator_shortcut(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        readme_ru = (ROOT / 'README_ru.md').read_text(encoding='utf-8')
        self.assertIn('EVALUATE_THIS_REPO.md', readme)
        self.assertIn('EVALUATE_THIS_REPO.md', readme_ru)
        self.assertIn('docs/evaluator-token-budget.md', readme)
        self.assertIn('docs_ru/evaluator-token-budget.md', readme_ru)


if __name__ == '__main__':
    unittest.main()
