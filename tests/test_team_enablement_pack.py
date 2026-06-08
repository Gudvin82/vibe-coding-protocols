from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TeamEnablementPackTests(unittest.TestCase):
    def test_pack_exists(self) -> None:
        for rel in [
            'docs/team-enablement-pack.md',
            'docs_ru/team-enablement-pack.md',
            'templates/training/team-enablement-plan.md',
            '.vcp/team-enablement-pack.json',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_module_count(self) -> None:
        payload = json.loads((ROOT / '.vcp' / 'team-enablement-pack.json').read_text(encoding='utf-8'))
        self.assertEqual(len(payload['modules']), 10)


if __name__ == '__main__':
    unittest.main()
