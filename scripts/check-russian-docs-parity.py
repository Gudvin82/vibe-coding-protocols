#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
required = [
    'README_ru.md',
    'docs_ru/README.md',
    'docs_ru/comparisons.md',
    'docs_ru/product-model.md',
    'docs_ru/killer-workflow.md',
    'docs_ru/demo-artifacts.md',
    'docs_ru/benchmark-report.md',
    'docs_ru/trust-check.md',
    'docs_ru/ai-tooling.md',
    'docs_ru/release-v0.8.6.md',
]
issues = []
for rel in required:
    path = ROOT / rel
    if not path.exists() or not path.read_text(encoding='utf-8').strip():
        issues.append(f'missing or empty {rel}')
        continue
    text = path.read_text(encoding='utf-8')
    if rel in {'README_ru.md', 'docs_ru/README.md', 'docs_ru/release-v0.8.6.md', 'docs_ru/benchmark-report.md', 'docs_ru/trust-check.md'} and CURRENT not in text:
        issues.append(f'{rel} missing current version {CURRENT}')
if issues:
    print('Russian docs parity check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)
print('Russian docs parity check passed.')
