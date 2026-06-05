from __future__ import annotations

import unittest
from pathlib import Path


class PrGateActionDocsTests(unittest.TestCase):
    def test_pr_gate_workflow_template_exists(self) -> None:
        path = Path("ci-examples/github-actions/vcp-pr-gate.yml")
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("git+https://github.com/Gudvin82/vibe-coding-protocols.git@v0.8.3", text)
        self.assertIn("vcp review-diff --json", text)

    def test_pr_gate_docs_exist(self) -> None:
        for rel in ["docs/pr-gate.md", "docs/pr-gate-action.md", "docs/github-action.md"]:
            self.assertTrue(Path(rel).exists(), rel)


if __name__ == "__main__":
    unittest.main()
