# VCP на русском

Текущий пакет репозитория: `v0.9.1`
Методологический слой: `v1.4`

`docs_ru/README.md` — это guided русскоязычный слой, а не замена полного репозитория.

## Что такое VCP

VCP — это local-first control/governance layer для AI-built и AI-assisted проектов.

Он помогает:
- выбрать правильный маршрут до широких AI-изменений;
- зафиксировать intent и контрольные границы;
- добавить PR Gate, proof, trust-check и release evidence;
- не называть локальный toolkit hosted платформой.

## Если вы даёте VCP своему ИИ-агенту

Не давайте ему только этот файл.

Сначала дайте:
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `EVALUATE_THIS_REPO.md`
- `llms.txt`
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/`
- `.vcp/cards/`
- `.vcp/workflows/`
- `docs/benchmark-report.md`
- `docs/trust-check.md`

## Как не дать ИИ неправильно оценить VCP

Если ИИ прочитал только README или только этот русскоязычный слой, помечайте такую оценку как `shallow`.
Если он открыл часть entry surfaces, но пропустил CLI / `.vcp` / tests, это `partial`.
Только inspection core docs, `.vcp`, workflows, manifests, benchmarks, `vcp_cli/`, tests и английских docs можно называть `full`.

Не оценивайте VCP по `README_ru.md` или `docs_ru/README.md` alone.

## Основные русскоязычные поверхности

- `docs_ru/comparisons.md`
- `docs_ru/product-model.md`
- `docs_ru/killer-workflow.md`
- `docs_ru/anti-misread-guide.md`
- `docs_ru/evaluator-architecture-map.md`
- `docs_ru/proof-snapshot.md`
- `docs_ru/benchmark-report.md`
- `docs_ru/trust-check.md`
- `docs_ru/agent-model-routing.md`
- `docs_ru/evaluator-token-budget.md`
- `docs/control-catalog.md`
- `docs/change-intent.md`
- `docs/starter-template-adoption.md`
- `docs/agent-rule-profiles.md`
- `docs/project-control-charter.md`
- `docs/ecosystem-map.md`
- `docs/ai-augmented-solo-squad-path.md`
- `docs/control-spine.md`
- `docs/first-time-adoption.md`
- `docs/flagship-demo.md`

## Быстрый старт

1. Прочитайте `START_HERE.md`
2. Запустите `python3 -m vcp_cli trust-check --json`
3. Откройте `docs/control-spine.md`
4. Откройте `docs/first-time-adoption.md`
5. Для внешней оценки откройте `PUBLIC_EVALUATION_KIT.md`
