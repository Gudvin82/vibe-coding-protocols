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
    'docs_ru/mvp-to-launch-path.md',
    'docs_ru/dashboard.md',
    'docs_ru/integration-packs.md',
    'docs_ru/release-v0.8.5.md',
]
issues = []
for rel in required:
    path = ROOT / rel
    if not path.exists():
        issues.append(f'missing {rel}')
        continue
    text = path.read_text(encoding='utf-8')
    if rel.endswith('.md') and rel not in {'docs_ru/README.md', 'docs_ru/install.md', 'docs_ru/dashboard.md', 'docs_ru/integration-packs.md', 'docs_ru/mvp-to-launch-path.md'} and CURRENT not in text:
        issues.append(f'{rel} missing current version {CURRENT}')
if CURRENT not in (ROOT / 'README_ru.md').read_text(encoding='utf-8'):
    issues.append('README_ru.md missing current version')
if issues:
    print('Russian docs parity check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)
print('Russian docs parity check passed.')
