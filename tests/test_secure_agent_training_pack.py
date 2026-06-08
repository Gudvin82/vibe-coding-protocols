from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SecureAgentTrainingPackTests(unittest.TestCase):
    def test_pack_exists(self) -> None:
        for rel in [
            'docs/secure-agent-training-pack.md',
            'docs_ru/secure-agent-training-pack.md',
            'templates/training/secure-agent-exercises.md',
            '.vcp/secure-agent-training-pack.json',
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_pack_has_ten_scenarios(self) -> None:
        payload = json.loads((ROOT / '.vcp' / 'secure-agent-training-pack.json').read_text(encoding='utf-8'))
        self.assertEqual(len(payload['scenarios']), 10)


if __name__ == '__main__':
    unittest.main()
