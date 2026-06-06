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
    ('landing positioning', ['Build with AI. Choose the right track. Adopt safely. Ship with control.'], ['Build with AI. Choose the right track. Adopt safely. Ship with control.']),
    ('problem statement', ['AI agents can generate MVPs quickly'], ['AI-агенты могут быстро генерировать MVP']),
    ('5-minute demo', ['## 5-minute demo'], ['## Демонстрация за 5 минут']),
    ('before after', ['## Before / after'], ['## До / после']),
    ('ai tooling section', ['## Use with your AI tools'], ['## Использование с AI tools']),
    ('comparison links', ['docs/comparisons.md', 'docs/product-model.md', 'docs/killer-workflow.md'], ['docs_ru/comparisons.md', 'docs_ru/product-model.md', 'docs_ru/killer-workflow.md']),
    ('trust-check link', ['docs/trust-check.md'], ['docs_ru/trust-check.md']),
    ('russian docs index', ['docs_ru/README.md'], ['docs_ru/README.md']),
    ('local platform flow', ['docs/local-platform-flow.md'], ['docs/local-platform-flow.md']),
    ('mvp to launch', ['docs/mvp-to-launch-path.md'], ['docs/mvp-to-launch-path.md']),
    ('install and run', ['python3 -m pip install .'], ['python3 -m pip install .']),
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
