from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()


class StarterAdoptionMatrixTests(unittest.TestCase):
    def test_docs_and_json_exist(self) -> None:
        for rel in ('docs/starter-template-adoption.md', 'docs_ru/starter-template-adoption.md', '.vcp/starter-adoption-matrix.json'):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_matrix_shape_and_boundaries(self) -> None:
        payload = json.loads((ROOT / '.vcp/starter-adoption-matrix.json').read_text(encoding='utf-8'))
        self.assertEqual(payload['version'], CURRENT)
        self.assertFalse(payload['official_integrations_claimed'])
        self.assertGreaterEqual(len(payload['items']), 10)
        for item in payload['items']:
            self.assertIn('recommended_path', item)
            self.assertIn('first_commands', item)
            self.assertTrue(item['first_commands'])


if __name__ == '__main__':
    unittest.main()
