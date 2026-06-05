from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from vcp_cli.adopt import apply_payload


class AdoptApplyTests(unittest.TestCase):
    def test_apply_requires_target(self) -> None:
        code, payload = apply_payload("brownfield-rescue", target=None, confirm=True)
        self.assertEqual(code, 1)
        self.assertIn("--target", payload["error"])

    def test_apply_requires_confirm_without_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            code, payload = apply_payload("brownfield-rescue", target=tmp, confirm=False)
            self.assertEqual(code, 1)
            self.assertIn("--confirm", payload["error"])

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            code, payload = apply_payload("brownfield-rescue", target=str(target), confirm=False, dry_run=True)
            self.assertEqual(code, 0)
            self.assertEqual(payload["status"], "dry_run")
            self.assertIsNone(payload["log_written"])
            self.assertFalse(any(target.iterdir()))

    def test_existing_file_is_reported_as_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "PROJECT_MAP.md").write_text("existing\n", encoding="utf-8")
            code, payload = apply_payload("brownfield-rescue", target=str(target), confirm=True)
            self.assertEqual(code, 0)
            self.assertTrue(payload["conflicts"])
            self.assertTrue(any("PROJECT_MAP.md" in item for item in payload["conflicts"]))

    def test_log_is_written_on_confirmed_apply(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            code, payload = apply_payload("spec-foundation", target=str(target), confirm=True)
            self.assertEqual(code, 0)
            self.assertIsNotNone(payload["log_written"])
            self.assertTrue(Path(payload["log_written"]).exists())

    def test_env_files_are_never_copied(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            code, payload = apply_payload("production", target=tmp, confirm=True)
            self.assertEqual(code, 0)
            self.assertFalse(any(item.endswith(".env") for item in payload["copied"]))


if __name__ == "__main__":
    unittest.main()
