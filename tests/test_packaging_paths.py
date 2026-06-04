from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vcp_cli import utils


class PackagingPathTests(unittest.TestCase):
    def test_runtime_root_prefers_repository_in_source_checkout(self) -> None:
        root = utils.runtime_root()
        self.assertTrue((root / "VERSION").exists())
        self.assertTrue((root / "METHODOLOGY_VERSION").exists())

    def test_project_root_uses_current_project_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "demo"
            nested = project / "src" / "feature"
            nested.mkdir(parents=True)
            (project / "pyproject.toml").write_text("[project]\nname='demo'\n", encoding="utf-8")
            detected = utils.project_root(nested)
            self.assertEqual(detected, project.resolve())


if __name__ == "__main__":
    unittest.main()
