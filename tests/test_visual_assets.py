from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class VisualAssetsTests(unittest.TestCase):
    def test_visual_assets_or_spec_exist(self) -> None:
        assets = [
            ROOT / 'assets/diagrams/vcp-control-layer-map.svg',
            ROOT / 'assets/diagrams/vcp-product-model.svg',
            ROOT / 'assets/diagrams/vcp-comparison-map.svg',
        ]
        for path in assets:
            self.assertTrue(path.exists(), str(path))
            self.assertTrue(path.read_text(encoding='utf-8').strip())
        self.assertTrue((ROOT / 'docs/visual-spec.md').exists())
        self.assertTrue((ROOT / 'docs_ru/visual-spec.md').exists())
