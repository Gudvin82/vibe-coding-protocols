from __future__ import annotations

import unittest
from pathlib import Path

from vcp_cli.version import get_version_info

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


class VersionSemanticsTests(unittest.TestCase):
    def test_repository_and_methodology_are_labeled(self) -> None:
        info = get_version_info()
        self.assertEqual(info["repository_package_version"], CURRENT)
        self.assertEqual(info["legacy_methodology_reference"], "v1.4")
        self.assertIn("current GitHub repository release", info["version_semantics_warning"])


if __name__ == "__main__":
    unittest.main()
