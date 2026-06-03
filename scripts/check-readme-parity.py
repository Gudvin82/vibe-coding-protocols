#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
README_EN = (ROOT / 'README.md').read_text(encoding='utf-8')
README_RU = (ROOT / 'README_ru.md').read_text(encoding='utf-8')

CHECKS = [
    (
        'repository package version',
        ['Repository package:', 'v0.6.3'],
        ['Repository package:', 'v0.6.3'],
    ),
    (
        'AI shallow evaluation warning',
        ['do not evaluate VCP from README alone'],
        ['не оценивайте VCP только по README'],
    ),
    (
        'TAKE_THIS_FIRST entrypoint',
        ['TAKE_THIS_FIRST.md'],
        ['TAKE_THIS_FIRST.md'],
    ),
    (
        '2-minute demo',
        ['Try VCP in 2 minutes'],
        ['Попробовать VCP за 2 минуты'],
    ),
    (
        'what VCP covers table',
        ['What VCP actually covers'],
        ['Что реально покрывает VCP'],
    ),
    (
        'install link',
        ['docs/install.md'],
        ['docs/install.md'],
    ),
    (
        'score badge mention',
        ['score --badge markdown', 'local readiness signal'],
        ['score --badge markdown', 'локальный readiness-сигнал'],
    ),
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
