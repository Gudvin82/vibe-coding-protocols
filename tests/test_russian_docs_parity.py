from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RussianDocsParityTests(unittest.TestCase):
    def test_russian_docs_parity_script(self) -> None:
        proc = subprocess.run(['python3', 'scripts/check-russian-docs-parity.py'], cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_docs_ru_readme_has_ai_agent_guidance(self) -> None:
        text = (ROOT / 'docs_ru/README.md').read_text(encoding='utf-8')
        self.assertIn('Если вы даёте VCP своему ИИ-агенту', text)
        self.assertIn('AGENTS.md', text)
        self.assertIn('AI_EVALUATION_GUIDE.md', text)
        self.assertIn('.vcp/index.json', text)
        self.assertIn('shallow', text)
        self.assertIn('partial', text)
        self.assertIn('full', text)
        self.assertIn('Как не дать ИИ неправильно оценить VCP', text)
        self.assertIn('EVALUATE_THIS_REPO.md', text)


if __name__ == '__main__':
    unittest.main()
