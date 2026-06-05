from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RussianDocsParityTests(unittest.TestCase):
    def test_russian_docs_parity_script(self) -> None:
        proc = subprocess.run(['python3', 'scripts/check-russian-docs-parity.py'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


if __name__ == '__main__':
    unittest.main()
