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
    ('landing positioning', ['Build with AI. Choose the right track. Adopt safely. Ship with control.'], ['Создавайте с AI. Выбирайте правильный маршрут. Внедряйте безопасно. Запускайте под контролем.']),
    ('problem statement', ['AI agents can generate MVPs quickly'], ['AI-агенты могут быстро генерировать MVP']),
    ('5-minute demo', ['## 5-minute demo'], ['## Демонстрация за 5 минут']),
    ('before after', ['## Before / after'], ['## До / после']),
    ('ai tooling section', ['## Use with your AI tools'], ['## Использование с AI tools']),
    ('comparison links', ['docs/comparisons.md', 'docs/product-model.md', 'docs/killer-workflow.md'], ['docs_ru/comparisons.md', 'docs_ru/product-model.md', 'docs_ru/killer-workflow.md']),
    ('trust-check link', ['docs/trust-check.md'], ['docs_ru/trust-check.md']),
    ('evaluator shortcut', ['EVALUATE_THIS_REPO.md', 'docs/anti-misread-guide.md', 'docs/evaluator-architecture-map.md', 'docs/proof-snapshot.md'], ['EVALUATE_THIS_REPO.md', 'docs_ru/anti-misread-guide.md', 'docs_ru/evaluator-architecture-map.md', 'docs_ru/proof-snapshot.md']),
    ('token saving docs', ['docs/agent-model-routing.md', 'docs/evaluator-token-budget.md', 'docs/visuals.md'], ['docs_ru/agent-model-routing.md', 'docs_ru/evaluator-token-budget.md', 'docs_ru/visuals.md']),
    ('visual layer', ['assets/diagrams/vcp-control-layer-map.svg'], ['assets/diagrams/vcp-control-layer-map.svg']),
    ('russian docs index', ['docs_ru/README.md'], ['docs_ru/README.md']),
    ('local platform flow', ['docs/local-platform-flow.md'], ['docs/local-platform-flow.md']),
    ('mvp to launch', ['docs/mvp-to-launch-path.md'], ['docs/mvp-to-launch-path.md']),
    ('install and run', ['python3 -m pip install .'], ['python3 -m pip install .']),
    ('public methodology hub', ['Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/'], ['Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/']),
    ('readme warning', [], ['Не оценивайте VCP только по `README_ru.md`']),
    ('inspection depth note', ['mark your review as `shallow`'], ['помечайте такую оценку как `shallow`']),
    ('token save block', ['## Save AI tokens'], ['## Экономьте AI-токены']),
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
