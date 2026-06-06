from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ChangelogHygieneTests(unittest.TestCase):
    def test_changelog_heading_and_latest_version(self) -> None:
        text = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
        lines = [line for line in text.splitlines() if line.strip()]
        self.assertEqual(lines[0], '# Changelog')
        match = re.search(r'^##\s+(v\d+\.\d+\.\d+)\b', text, re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), 'v0.8.6')


if __name__ == '__main__':
    unittest.main()
