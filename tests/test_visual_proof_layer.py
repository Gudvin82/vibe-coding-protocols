
from __future__ import annotations
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class VisualProofLayerTests(unittest.TestCase):
    def test_diagrams_exist(self):
        for rel in ['assets/diagrams/vcp-route-selector.svg','assets/diagrams/vcp-evidence-bundle.svg','assets/diagrams/vcp-pr-readiness-flow.svg','assets/diagrams/vcp-release-decision-matrix.svg','assets/diagrams/vcp-anti-chaos-recovery.svg']:
            self.assertTrue((ROOT / rel).exists(), rel)
