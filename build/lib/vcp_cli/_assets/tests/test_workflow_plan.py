from __future__ import annotations

import unittest

from vcp_cli.workflow_cmd import workflow_plan_payload, workflow_run_payload


class WorkflowPlanTests(unittest.TestCase):
    def test_plan_loads_known_workflow(self) -> None:
        payload = workflow_plan_payload("production-hardening")
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["plans"][0]["id"], "production-hardening")

    def test_mvp_to_launch_workflow_plan_has_expected_steps(self) -> None:
        payload = workflow_plan_payload("mvp-to-launch")
        self.assertTrue(payload["ok"])
        plan = payload["plans"][0]
        self.assertEqual(plan["id"], "mvp-to-launch")
        self.assertEqual(
            [step["id"] for step in plan["steps"]],
            [
                "intake",
                "classify",
                "surface-scan",
                "adoption-plan",
                "risk-backlog",
                "proof-check",
                "pr-gate-approval",
                "dashboard-build",
                "launch-decision",
            ],
        )

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

    def test_mvp_to_launch_run_stays_non_executing(self) -> None:
        payload = workflow_run_payload("mvp-to-launch", interactive=True, dry_run=True)
        self.assertTrue(payload["ok"])
        self.assertTrue(all(not step["executed"] for step in payload["steps"]))
        self.assertTrue(all(step["status"] == "planned" for step in payload["steps"]))


if __name__ == "__main__":
    unittest.main()
