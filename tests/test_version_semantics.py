from __future__ import annotations

import unittest

from vcp_cli.version import get_version_info


class VersionSemanticsTests(unittest.TestCase):
    def test_repository_and_methodology_are_labeled(self) -> None:
        info = get_version_info()
        self.assertEqual(info["repository_package_version"], "v0.9.0")
        self.assertEqual(info["legacy_methodology_reference"], "v1.4")
        self.assertIn("current GitHub repository release", info["version_semantics_warning"])


if __name__ == "__main__":
    unittest.main()
