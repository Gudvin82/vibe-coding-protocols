from __future__ import annotations

import unittest

from vcp_cli.workflow_cmd import workflow_plan_payload, workflow_run_payload


class WorkflowPlanTests(unittest.TestCase):
    def test_plan_loads_known_workflow(self) -> None:
        payload = workflow_plan_payload("production-hardening")
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["plans"][0]["id"], "production-hardening")

    def test_unknown_workflow_returns_clear_error(self) -> None:
        payload = workflow_plan_payload("does-not-exist")
        self.assertFalse(payload["ok"])
        self.assertIn("Workflow not found", payload["error"])

    def test_run_without_interactive_refuses(self) -> None:
        payload = workflow_run_payload("production-hardening", interactive=False)
        self.assertFalse(payload["ok"])
        self.assertIn("--interactive", payload["error"])

    def test_interactive_run_is_safe_preview_only(self) -> None:
        payload = workflow_run_payload("production-hardening", interactive=True, dry_run=True)
        self.assertTrue(payload["ok"])
        self.assertTrue(all(not step["executed"] for step in payload["steps"]))


if __name__ == "__main__":
    unittest.main()
