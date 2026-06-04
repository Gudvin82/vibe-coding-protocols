from __future__ import annotations

import unittest

from vcp_cli.version import get_version_info


class VersionSemanticsTests(unittest.TestCase):
    def test_repository_and_methodology_are_labeled(self) -> None:
        info = get_version_info()
        self.assertEqual(info["repository_package_version"], "v0.7.0")
        self.assertEqual(info["methodology_layer"], "v1.4")
        self.assertIn("Do not confuse", info["version_semantics_warning"])


if __name__ == "__main__":
    unittest.main()
