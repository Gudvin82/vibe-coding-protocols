from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vcp_cli import dashboard_cmd


class DashboardCommandTests(unittest.TestCase):
    def test_build_payload_dry_run_keeps_output_clean(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "dashboard"
            data = dashboard_cmd.build_payload(str(output), dry_run=True)
            self.assertTrue(data["ok"])
            self.assertFalse(output.exists())
            self.assertIn("index.html", data["generated_files"])

    def test_build_writes_only_inside_output_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "dashboard"
            marker = Path(tmp) / "outside.txt"
            marker.write_text("keep", encoding="utf-8")
            data = dashboard_cmd.build_payload(str(output), dry_run=False)
            self.assertTrue((output / "index.html").exists())
            self.assertTrue((output / "metrics.json").exists())
            self.assertEqual(marker.read_text(encoding="utf-8"), "keep")
            for path in data["written_files"]:
                self.assertTrue(Path(path).is_relative_to(output))

    def test_metrics_json_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "dashboard"
            dashboard_cmd.build_payload(str(output), dry_run=False)
            metrics = json.loads((output / "metrics.json").read_text(encoding="utf-8"))
            self.assertIn("repository_package_version", metrics)
            self.assertIn("integration_status_counts", metrics)
            self.assertIn("audit_backlog", metrics)

    def test_dashboard_markdown_includes_mvp_to_launch_section(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "dashboard"
            dashboard_cmd.build_payload(str(output), dry_run=False)
            text = (output / "dashboard.md").read_text(encoding="utf-8")
            self.assertIn("## MVP-to-Launch", text)
            self.assertIn("docs/mvp-to-launch-path.md", text)
            self.assertIn(".vcp/workflows/mvp-to-launch.json", text)
            self.assertIn("Local dashboard artifact only.", text)


if __name__ == "__main__":
    unittest.main()
