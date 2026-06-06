from __future__ import annotations

import unittest

from vcp_cli.audit_plan import payload


class AuditPlanTests(unittest.TestCase):
    def test_audit_plan_payload_has_required_fields(self) -> None:
        data = payload()
        self.assertEqual(data["repository_package_version"], "v0.9.0")
        self.assertIn("required_for_full_evaluation", data)
        self.assertIn("failure_contract", data)
        self.assertTrue(data["must_report"])


if __name__ == "__main__":
    unittest.main()
