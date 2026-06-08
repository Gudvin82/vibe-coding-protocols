from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AIEcosystemWatchlistTests(unittest.TestCase):
    def test_docs_and_json_exist(self) -> None:
        for rel in [
            'docs/ai-ecosystem-watchlist.md',
            'docs_ru/ai-ecosystem-watchlist.md',
            '.vcp/ai-ecosystem-watchlist.json',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_cli_watchlist_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'ecosystem', 'watchlist', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload['ok'])
        self.assertEqual(payload['version'], 'v0.9.4')
        self.assertGreaterEqual(payload['count'], 1)


if __name__ == '__main__':
    unittest.main()
