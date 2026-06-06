from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CaseStudyTemplateTests(unittest.TestCase):
    def test_case_study_surfaces_exist(self) -> None:
        for rel in ('docs/case-studies.md', 'docs_ru/case-studies.md', 'case-studies/README.md', 'case-studies/TEMPLATE.md', 'case-studies/synthetic-vcp-public-proof.md'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_synthetic_marker_is_explicit(self) -> None:
        text = (ROOT / 'case-studies/synthetic-vcp-public-proof.md').read_text(encoding='utf-8')
        self.assertIn('synthetic', text)


if __name__ == '__main__':
    unittest.main()
