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
    ('v0.8.4 release block', ['New in v0.8.4'], ['Новое в v0.8.4']),
    ('quick start by situation', ['Quick start by situation'], ['Быстрый старт по ситуации']),
    ('two tracks', ['New Project Track', 'Existing Project Track'], ['New Project Track', 'Existing Project Track']),
    ('adoption tiers', ['docs/adoption-tiers.md'], ['docs/adoption-tiers.md']),
    ('safe adoption plan', ['adopt plan --json', 'adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json'], ['adopt plan --json', 'adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json']),
    ('public growth check', ['public-growth check --json'], ['public-growth check --json']),
    ('proof pack', ['docs/proof-pack.md', 'case-studies/README.md'], ['docs/proof-pack.md', 'case-studies/README.md']),
    ('workflow planning note', ['workflow plan --json'], ['workflow plan --json']),
    ('install and distribution links', ['docs/install.md', 'docs/distribution.md'], ['docs/install.md', 'docs/distribution.md']),
    ('install and run', ['Install and run', 'python3 -m pip install .', 'Public PyPI/npm packages are not claimed unless explicitly published.'], ['Установить и запустить', 'python3 -m pip install .', 'Публичные PyPI/npm пакеты не заявляются, пока они реально не опубликованы.']),
    ('pr gate workflow link', ['Add VCP to PRs', 'ci-examples/github-actions/vcp-pr-gate.yml'], ['Добавить VCP в PR', 'ci-examples/github-actions/vcp-pr-gate.yml']),
    ('integration scaffold links', ['docs/integrations/status-model.md', 'docs/dashboard.md', 'docs/plugins/README.md'], ['docs/integrations/status-model.md', 'docs/dashboard.md', 'docs/plugins/README.md']),
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
