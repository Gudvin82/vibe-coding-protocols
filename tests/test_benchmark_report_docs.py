from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()


class BenchmarkReportDocsTests(unittest.TestCase):
    def test_benchmark_report_has_current_version_and_command(self) -> None:
        text = (ROOT / 'docs/benchmark-report.md').read_text(encoding='utf-8')
        self.assertIn(CURRENT, text)
        self.assertIn('python3 -m vcp_cli benchmark run --json', text)


if __name__ == '__main__':
    unittest.main()
