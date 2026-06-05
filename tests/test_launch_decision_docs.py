from __future__ import annotations

import unittest
from pathlib import Path


class LaunchDecisionDocsTests(unittest.TestCase):
    def test_launch_decision_docs_exist(self) -> None:
        self.assertTrue(Path("docs/launch-decision-checklist.md").exists())
        self.assertTrue(Path("templates/reports/launch-decision.md").exists())

    def test_launch_decision_checklist_has_required_statuses(self) -> None:
        text = Path("docs/launch-decision-checklist.md").read_text(encoding="utf-8")
        for label in ["go", "go-with-warnings", "no-go", "needs-human-review", "not-applicable"]:
            self.assertIn(f"`{label}`", text)

    def test_launch_decision_template_is_local_aid(self) -> None:
        text = Path("templates/reports/launch-decision.md").read_text(encoding="utf-8")
        self.assertIn("local launch decision aid", text)
        self.assertIn("not a production certification", text)


if __name__ == "__main__":
    unittest.main()
