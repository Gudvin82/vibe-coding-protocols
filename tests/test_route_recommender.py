
from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class RouteRecommenderTests(unittest.TestCase):
    def test_route_recommend_json(self):
        proc = subprocess.run(['python3','-m','vcp_cli','route','recommend','--scenario','raw-ai-mvp','--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data['scenario'], 'raw-ai-mvp')
    def test_route_list_json(self):
        proc = subprocess.run(['python3','-m','vcp_cli','route','list','--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
