#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
required = [
    'README_ru.md',
    'docs_ru/README.md',
    'docs_ru/install.md',
    'docs_ru/10-minute-adoption-path.md',
    'docs_ru/mvp-to-launch-path.md',
    'docs_ru/local-platform-flow.md',
    'docs_ru/dashboard.md',
    'docs_ru/integration-packs.md',
    'docs_ru/pr-gate.md',
    'docs_ru/comparisons.md',
    'docs_ru/product-model.md',
    'docs_ru/killer-workflow.md',
    'docs_ru/anti-misread-guide.md',
    'docs_ru/evaluator-architecture-map.md',
    'docs_ru/proof-snapshot.md',
    'docs_ru/external-evaluation.md',
    'docs_ru/public-surfaces.md',
    'docs_ru/demo-artifacts.md',
    'docs_ru/benchmark-report.md',
    'docs_ru/trust-check.md',
    'docs_ru/ai-tooling.md',
    'docs_ru/agent-model-routing.md',
    'docs_ru/evaluator-token-budget.md',
    'docs_ru/visuals.md',
    'docs_ru/visual-spec.md',
    'docs_ru/release-v0.8.8.md',
]
issues = []
for rel in required:
    path = ROOT / rel
    if not path.exists() or not path.read_text(encoding='utf-8').strip():
        issues.append(f'missing or empty {rel}')
        continue
    text = path.read_text(encoding='utf-8')
    if rel in {'README_ru.md', 'docs_ru/README.md', 'docs_ru/release-v0.8.8.md', 'docs_ru/benchmark-report.md', 'docs_ru/trust-check.md'} and CURRENT not in text:
        issues.append(f'{rel} missing current version {CURRENT}')
    if rel == 'docs_ru/README.md':
        for needle in (
            'Если вы даёте VCP своему ИИ-агенту',
            'Как не дать ИИ неправильно оценить VCP',
            'AGENTS.md',
            'AI_EVALUATION_GUIDE.md',
            'EVALUATE_THIS_REPO.md',
            'llms.txt',
            '.vcp/index.json',
            '.vcp/catalog.json',
            '.vcp/manifests/',
            '.vcp/cards/',
            '.vcp/workflows/',
            'docs/benchmark-report.md',
            'docs/trust-check.md',
            'shallow',
            'partial',
            'full',
            'английских docs',
            'agent-model-routing.md',
            'evaluator-token-budget.md',
        ):
            if needle not in text:
                issues.append(f'docs_ru/README.md missing required guidance: {needle}')
if issues:
    print('Russian docs parity check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)
print('Russian docs parity check passed.')
