from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SoloSquadPathTests(unittest.TestCase):
    def test_docs_and_workflow_exist(self) -> None:
        for rel in ('docs/ai-augmented-solo-squad-path.md', 'docs_ru/ai-augmented-solo-squad-path.md', '.vcp/workflows/ai-augmented-solo-squad.json', 'templates/reports/solo-squad-control-plan.md'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_path_is_human_led(self) -> None:
        text = (ROOT / 'docs/ai-augmented-solo-squad-path.md').read_text(encoding='utf-8')
        self.assertIn('human-led', text)
        self.assertIn('does not claim autonomous orchestration', text)
        payload = json.loads((ROOT / '.vcp/workflows/ai-augmented-solo-squad.json').read_text(encoding='utf-8'))
        self.assertEqual(payload['version'], 'v0.9.1')


if __name__ == '__main__':
    unittest.main()
