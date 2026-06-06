from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ControlLayerCommandTests(unittest.TestCase):
    def test_pr_gate_explain(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'pr-gate', 'explain', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn('pass', payload['states'])

    def test_safety_check(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'safety', 'check', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn('default_policy', payload)

    def test_memory_validate(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'memory', 'validate', '/.vcp/project-memory.example.json'.replace('/.', str(ROOT) + '/.'), '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_runs_validate(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'runs', 'validate', '/.vcp/runs/example-run-state.json'.replace('/.', str(ROOT) + '/.'), '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_agents_template_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'agents', 'template', '--agent', 'codex', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload['agent'], 'codex')

    def test_agents_template_copilot_json(self) -> None:
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'agents', 'template', '--agent', 'copilot', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload['agent'], 'copilot')

    def test_agent_behavior_check(self) -> None:
        report = ROOT / 'tests' / 'fixtures' / 'agent-report.md'
        proc = subprocess.run(['python3', '-m', 'vcp_cli', 'agent-behavior', 'check', '--report', str(report), '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertIn(payload['status'], {'pass', 'warn'})

    def test_batch_evaluate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            targets = Path(tmp) / 'targets.txt'
            targets.write_text(str(ROOT) + '\n', encoding='utf-8')
            proc = subprocess.run(['python3', '-m', 'vcp_cli', 'batch', 'evaluate', '--targets', str(targets), '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual(payload['summary']['passed'], 1)

if __name__ == '__main__':
    unittest.main()
