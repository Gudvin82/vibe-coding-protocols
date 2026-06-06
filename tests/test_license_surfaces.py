from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LicenseSurfacesTests(unittest.TestCase):
    def test_dual_license_files_exist(self) -> None:
        for rel in ('LICENSE', 'LICENSE-CODE-MIT', 'LICENSE-DOCS-CC-BY-4.0', 'NOTICE', 'docs/license.md', 'docs_ru/license.md'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_python_and_node_metadata_use_mit(self) -> None:
        pyproject = (ROOT / 'pyproject.toml').read_text(encoding='utf-8')
        package = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))
        self.assertIn('MIT', pyproject)
        self.assertIn('License :: OSI Approved :: MIT License', pyproject)
        self.assertEqual(package['license'], 'MIT')

    def test_readmes_mention_dual_license(self) -> None:
        for rel in ('README.md', 'README_ru.md'):
            text = (ROOT / rel).read_text(encoding='utf-8')
            self.assertIn('Code/CLI/scripts/tests: MIT', text)
            self.assertIn('CC BY 4.0', text)


if __name__ == '__main__':
    unittest.main()
