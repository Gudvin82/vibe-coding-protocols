#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
README_EN = (ROOT / 'README.md').read_text(encoding='utf-8')
README_RU = (ROOT / 'README_ru.md').read_text(encoding='utf-8')
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()

CHECKS = [
    ('repository package version', ['Repository package:', CURRENT], ['Repository package:', CURRENT]),
    ('ai release naming guard', ['report the current GitHub repository release as', CURRENT], ['называй текущий GitHub-релиз репозитория как', CURRENT]),
    ('AI shallow evaluation warning', ['do not evaluate VCP from README alone'], ['не оценивайте VCP только по README']),
    ('full repo intake marker', ['FULL_REPO_INTAKE.md', '.vcp/ai-audit-manifest.json'], ['FULL_REPO_INTAKE.md', '.vcp/ai-audit-manifest.json']),
    ('v0.8.5 release block', ['New in v0.8.5'], ['Новое в v0.8.5']),
    ('10-minute path', ['Start here in 10 minutes'], ['Старт за 10 минут']),
    ('local platform flow', ['docs/local-platform-flow.md'], ['docs/local-platform-flow.md']),
    ('integration packs', ['docs/integration-packs.md'], ['docs/integration-packs.md']),
    ('russian docs', ['docs_ru/README.md'], ['docs_ru/README.md']),
    ('mvp-to-launch', ['docs/mvp-to-launch-path.md'], ['docs/mvp-to-launch-path.md']),
    ('install and run', ['python3 -m pip install .'], ['python3 -m pip install .']),
    ('pr gate workflow link', ['ci-examples/github-actions/vcp-pr-gate.yml'], ['ci-examples/github-actions/vcp-pr-gate.yml']),
]

missing: list[str] = []
for label, en_needles, ru_needles in CHECKS:
    if not all(needle in README_EN for needle in en_needles):
        missing.append(f'EN missing {label}')
    if not all(needle in README_RU for needle in ru_needles):
        missing.append(f'RU missing {label}')

if missing:
    print('README parity check failed:')
    for item in missing:
        print(f'- {item}')
    sys.exit(1)

print('README parity check passed.')
