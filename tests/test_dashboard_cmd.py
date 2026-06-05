from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vcp_cli import dashboard_cmd


class DashboardCommandTests(unittest.TestCase):
    def test_build_payload_dry_run_keeps_output_clean(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'dashboard'
            data = dashboard_cmd.build_payload(str(output), dry_run=True)
            self.assertTrue(data['ok'])
            self.assertFalse(output.exists())
            self.assertIn('index.html', data['generated_files'])

    def test_build_writes_required_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'dashboard'
            marker = Path(tmp) / 'outside.txt'
            marker.write_text('keep', encoding='utf-8')
            data = dashboard_cmd.build_payload(str(output), dry_run=False)
            required = {
                'index.html', 'README.md', 'dashboard.md', 'metrics.json', 'integration-status.json',
                'audit-backlog-summary.json', 'project-map.json', 'run-history.json', 'launch-readiness.json',
                'release-readiness.json',
            }
            self.assertTrue(required.issubset({p.name for p in output.iterdir()}))
            self.assertEqual(marker.read_text(encoding='utf-8'), 'keep')
            for path in data['written_files']:
                self.assertTrue(Path(path).is_relative_to(output))

    def test_dashboard_markdown_includes_local_platform_and_russian_docs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'dashboard'
            dashboard_cmd.build_payload(str(output), dry_run=False)
            text = (output / 'dashboard.md').read_text(encoding='utf-8')
            self.assertIn('## MVP-to-Launch', text)
            self.assertIn('## Local platform flow', text)
            self.assertIn('docs/integration-packs.md', text)
            self.assertIn('docs_ru/README.md', text)
            self.assertIn('Local dashboard artifact only.', text)


if __name__ == '__main__':
    unittest.main()
