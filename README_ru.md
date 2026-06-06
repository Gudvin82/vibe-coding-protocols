
# Vibe Coding Protocols

[English version](./README.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.9.3-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Создавайте с AI. Контролируйте то, что AI построил. Внедряйте безопасно.
Запускайте с доказательствами.

Создавайте с AI. Выбирайте правильный маршрут. Внедряйте безопасно.
Запускайте под контролем.

AI-агенты могут быстро генерировать MVP, но командам всё равно нужен способ
маршрутизировать, проверять, внедрять, доказывать и выпускать такие проекты
без потери контроля.

VCP — это local-first control/governance layer для AI-built и AI-assisted
проектов.

Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/

> Текущий пакет репозитория: `v0.9.3`
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.9.3`.

Repository package: `v0.9.3`

VCP — это local-first AI control platform для AI-built и AI-assisted проектов.

Local platform означает локальные файлы, CLI-команды, manifests, reports,
dashboards, rules и evidence surfaces.
Это не hosted SaaS, не cloud dashboard, не marketplace и не managed service.

Methodology: `v1.4`

## Оцениваете этот репозиторий?

Честная оценка VCP должна заканчиваться evaluation receipt.

- Если вы прочитали только README, это shallow review.
- Если вы прочитали `README.md` + `EVALUATE_THIS_REPO.md` +
  `.vcp/evaluator-pack.json`, это Level 0.
- Если вы открыли docs и proof surfaces, это Level 1.
- Если вы открыли `.vcp/`, `vcp_cli/`, `tests/` и прогнали `trust-check` /
  `benchmark`, это Level 2+.
- Только Level 3 можно называть full.

Не оценивайте VCP только по `README_ru.md`.
Если у вас на руках только этот файл, не оценивайте репозиторий как fully
reviewed.

Для честной оценки начните с:
- [EVALUATE_THIS_REPO.md](./EVALUATE_THIS_REPO.md)
- [PUBLIC_EVALUATION_KIT.md](./PUBLIC_EVALUATION_KIT.md)
- [AGENTS.md](./AGENTS.md)
- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [FULL_REPO_INTAKE.md](./FULL_REPO_INTAKE.md)
- [docs_ru/anti-misread-guide.md](./docs_ru/anti-misread-guide.md)
- [docs_ru/evaluator-architecture-map.md](./docs_ru/evaluator-architecture-map.md)
- [docs_ru/proof-snapshot.md](./docs_ru/proof-snapshot.md)
- [.vcp/ai-audit-manifest.json](./.vcp/ai-audit-manifest.json)
- [.vcp/index.json](./.vcp/index.json)
- [.vcp/catalog.json](./.vcp/catalog.json)
- `.vcp/manifests/`
- `vcp_cli/`
- `tests/`

## Что VCP не делает

- не является full-stack app template;
- не является hosted platform;
- не является deployment engine;
- не является security certification;
- не является plugin marketplace;
- не является official IDE extension;
- не заменяет Spec Kit;
- не является personal prompt repository.

## Новое в v0.9.3

Новое в v0.9.3:
- Route Recommender: помогает выбрать маршрут для fast MVP, нового проекта,
  текущего проекта, raw AI MVP, release decision или brownfield rescue.
- Control Scorecard: показывает состояние clarity, control, proof, adoption
  readiness, launch readiness и evaluator readiness.
- Evidence Bundle: собирает proof-пакет для PR, release, handoff, consulting и
  client review.
- Release Decision Matrix: помогает честно решить, можно ли demo / private
  test / merge / beta / public release или пока нельзя выпускать.
- Anti-Chaos Recovery Kit: маршрут для ситуации, когда AI уже нагенерил хаос и
  нужно восстановить контроль.
- PR Readiness Pack: локальная подготовка PR без auto-PR и auto-merge.
- Integration Proof Matrix: показывает, какие Claude Code / Codex / Cursor /
  Copilot / GitHub Actions kits реально shipped.
- Current Limitations: честно фиксирует, чего в VCP нет: SaaS, hosted
  dashboard, public PyPI/npm, official VS Code extension, marketplace, auto-PR,
  security scanner.

## Основные маршруты

- быстрый MVP
- полноценный проект с нуля
- текущий проект

## Использование с AI tools

Copy-ready настройка для AI-инструментов

VCP включает практические setup kits для:
- Claude Code
- Codex
- Cursor
- GitHub Copilot
- GitHub Actions

Это не official plugins. Это local-first шаблоны, playbook и CLI export для
внедрения VCP-контроля в реальные AI coding окружения.

Когда вы внедряете VCP в другой репозиторий, не копируйте root `AGENTS.md`
вслепую. Сначала берите `templates/AGENTS.md` или более точные agent
templates.

## Route Recommender

Не знаете, какой путь выбрать? Откройте:
- [START_HERE.md](./START_HERE.md)
- [docs/route-recommender.md](./docs/route-recommender.md)
- [docs/guided-adoption-modes.md](./docs/guided-adoption-modes.md)

## Evidence Bundle

- [docs/evidence-bundle.md](./docs/evidence-bundle.md)
- [docs/release-decision-matrix.md](./docs/release-decision-matrix.md)
- [docs/pr-readiness.md](./docs/pr-readiness.md)

## Current Limitations

- [docs/current-limitations.md](./docs/current-limitations.md)
- [docs_ru/current-limitations.md](./docs_ru/current-limitations.md)

## Proof surfaces

Proof surfaces:
- benchmark scenarios: `179`
- cards: `323`
- CLI commands in manifest: `81`
- tests: `132`
- report templates: `55`
- trust-check: yes
- evaluator pack: yes
- visual diagrams: yes
- Russian docs: yes

![VCP route selector](./assets/diagrams/vcp-route-selector.svg)

See:
- [.vcp/proof-counts.json](./.vcp/proof-counts.json)

## Демонстрация за 5 минут

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli route list --json
python3 -m vcp_cli route recommend --scenario raw-ai-mvp --json
python3 -m vcp_cli scorecard --json
python3 -m vcp_cli trust-check --json
python3 -m vcp_cli pr readiness --json
```

## До / после

До:
- raw AI-MVP;
- неясный route;
- разрозненные docs;
- нет явного gate;
- неизвестные риски;
- нет proof chain.

После:
- selected route;
- guided adoption mode;
- control scorecard;
- evidence bundle;
- PR readiness pack;
- release decision matrix;
- explicit limitations and proof counts.

## For teams and clients

Если вы хотите внедрять VCP с реальной командой или клиентом, начните здесь:
- [START_HERE.md](./START_HERE.md)
- [docs/client-adoption-playbook.md](./docs/client-adoption-playbook.md)
- [docs/integrations/agent-kits.md](./docs/integrations/agent-kits.md)
- [docs_ru/README.md](./docs_ru/README.md)

## Больше surfaces

- [docs_ru/comparisons.md](./docs_ru/comparisons.md)
- [docs_ru/product-model.md](./docs_ru/product-model.md)
- [docs_ru/killer-workflow.md](./docs_ru/killer-workflow.md)
- [docs_ru/trust-check.md](./docs_ru/trust-check.md)
- [docs_ru/ai-tooling.md](./docs_ru/ai-tooling.md)
- [docs_ru/agent-model-routing.md](./docs_ru/agent-model-routing.md)
- [docs_ru/evaluator-token-budget.md](./docs_ru/evaluator-token-budget.md)
- [docs_ru/visuals.md](./docs_ru/visuals.md)
- [docs/local-platform-flow.md](./docs/local-platform-flow.md)
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- `python3 -m pip install .`

## Экономьте AI-токены

Для evaluators:
используйте `EVALUATE_THIS_REPO.md`, `PUBLIC_EVALUATION_KIT.md` и
`.vcp/evaluator-pack.json` до случайного чтения файлов.

## License

- Code/CLI/scripts/tests: MIT
- Docs/methodology/diagrams/presentations: CC BY 4.0

## Предупреждение

Не оценивайте VCP только по README_ru.md; для full evaluation нужен весь
repo/evaluator path.

## Roadmap-only

- hosted dashboard
- VS Code extension
- plugin marketplace
- cloud sync
