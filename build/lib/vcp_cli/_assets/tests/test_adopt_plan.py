from __future__ import annotations

import unittest

from vcp_cli.adopt import _copy_list_text, _patch_preview, plan_payload


class AdoptPlanTests(unittest.TestCase):
    def test_adopt_plan_is_non_destructive(self) -> None:
        data = plan_payload("production")
        self.assertFalse(data["writes_by_default"])
        self.assertTrue(data["safety_notes"])
        self.assertIn("selected_pack", data)

    def test_copy_list_and_patch_preview_render(self) -> None:
        data = plan_payload("spec-foundation")
        copy_text = _copy_list_text(data)
        patch_text = _patch_preview(data)
        self.assertIn("Copy", copy_text)
        self.assertTrue(patch_text.startswith("--- /dev/null") or patch_text.startswith("# No copyable"))


if __name__ == "__main__":
    unittest.main()
