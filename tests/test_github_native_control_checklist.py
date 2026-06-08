from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GitHubNativeControlChecklistTests(unittest.TestCase):
    def test_surfaces_exist(self) -> None:
        for rel in [
            'docs/github-native-control-checklist.md',
            'docs_ru/github-native-control-checklist.md',
            'templates/reports/github-native-control-checklist.md',
            '.vcp/github-native-control-checklist.example.json',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)


if __name__ == '__main__':
    unittest.main()
