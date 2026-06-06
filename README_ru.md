# Vibe Coding Protocols

[English version](./README.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.9.1-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Создавайте с AI. Контролируйте то, что AI построил. Внедряйте безопасно. Запускайте с доказательствами.

Создавайте с AI. Выбирайте правильный маршрут. Внедряйте безопасно. Запускайте под контролем.

AI-агенты могут быстро генерировать MVP, но командам всё равно нужен способ маршрутизировать, проверять, внедрять, доказывать и выпускать такие проекты без потери контроля.

VCP — это local-first control/governance layer для AI-built и AI-assisted проектов.

Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/

> Текущий пакет репозитория: `v0.9.1`  
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.9.1`.

Repository package: `v0.9.1`

VCP — это local-first AI control platform для AI-built и AI-assisted проектов.

Local platform означает локальные файлы, CLI-команды, manifests, reports, dashboards, rules и evidence surfaces.
Это не hosted SaaS, не cloud dashboard, не marketplace и не managed service.

Methodology: `v1.4`

## Оцениваете этот репозиторий?

Честная оценка VCP должна заканчиваться evaluation receipt.

- Если вы прочитали только README, это shallow review.
- Если вы прочитали `README.md` + `EVALUATE_THIS_REPO.md` + `.vcp/evaluator-pack.json`, это Level 0.
- Если вы открыли docs и proof surfaces, это Level 1.
- Если вы открыли `.vcp/`, `vcp_cli/`, `tests/` и прогнали `trust-check` / `benchmark`, это Level 2+.
- Только Level 3 можно называть full.

Не оценивайте VCP только по `README_ru.md`.
Если у вас на руках только этот файл, не оценивайте репозиторий как fully reviewed.

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

Если вы смотрели только README, помечайте такую оценку как `shallow`.

## Что VCP не делает

- не является full-stack app template;
- не является hosted platform;
- не является deployment engine;
- не является security certification;
- не является plugin marketplace;
- не является official IDE extension;
- не заменяет Spec Kit;
- не является personal prompt repository.

## Новое в v0.9.1

`v0.9.1` добавляет более ясный product spine и first-time adoption layer:
- product spine и control spine;
- first-time adoption и чистый route selector;
- adaptive rigor modes и tiny VCP pipeline;
- flagship demo и public evaluation kit;
- portable control pack;
- work package, review-accept-merge, mission retrospective и delivery graph surfaces.

## Platform Surfaces

- [Product Spine](./docs/product-spine.md)
- [Control Spine](./docs/control-spine.md)
- [First-Time Adoption](./docs/first-time-adoption.md)
- [Adaptive Rigor Modes](./docs/adaptive-rigor-modes.md)
- [Tiny VCP Pipeline](./docs/tiny-vcp-pipeline.md)
- [Flagship Demo](./docs/flagship-demo.md)
- [Portable Control Pack](./docs/portable-control-pack.md)
- [Surface Priority Model](./docs/surface-priority-model.md)
- [Work Package Lifecycle](./docs/work-package-lifecycle.md)
- [Review / Accept / Merge](./docs/review-accept-merge.md)
- [Mission Retrospective](./docs/mission-retrospective.md)
- [Delivery Graph](./docs/delivery-graph.md)
- [Public Evaluation Kit](./docs/public-evaluation-kit.md)
- [Scope Boundary](./docs/scope-boundary.md)
- [Control Catalog](./docs/control-catalog.md)
- [Change Intent](./docs/change-intent.md)
- [Starter Adoption Matrix](./docs/starter-template-adoption.md)
- [Agent Rule Profiles](./docs/agent-rule-profiles.md)
- [Project Control Charter](./docs/project-control-charter.md)
- [Ecosystem Map](./docs/ecosystem-map.md)
- [AI-Augmented Solo/Squad Path](./docs/ai-augmented-solo-squad-path.md)
- [docs_ru/README.md](./docs_ru/README.md)

## License

- Code/CLI/scripts/tests: MIT
- Docs/methodology/diagrams/presentations: CC BY 4.0

## Proof surfaces

Proof surfaces:
- benchmark scenarios: `162`
- cards: `302`
- CLI commands in manifest: `76`
- tests: `107`
- report templates: `48`
- trust-check: yes
- evaluator pack: yes
- visual diagrams: yes
- Russian docs: yes

See:
- [docs_ru/proof-snapshot.md](./docs_ru/proof-snapshot.md)
- [docs_ru/trust-check.md](./docs_ru/trust-check.md)
- [docs_ru/benchmark-report.md](./docs_ru/benchmark-report.md)
- [examples/flagship-demo/README.md](./examples/flagship-demo/README.md)

![VCP control layer map](./assets/diagrams/vcp-control-layer-map.svg)

## Демонстрация за 5 минут

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli catalog list --json
python3 -m vcp_cli workflow plan --id mvp-to-launch --json
python3 -m vcp_cli pr-gate explain --json
python3 -m vcp_cli trust-check --json
python3 -m vcp_cli evaluator pack --json
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
- control spine;
- work package;
- PR Gate explanation;
- proof snapshot;
- evaluation kit;
- explicit scope boundary.

## Использование с AI tools

Используйте VCP вместе с:
- Cursor;
- Claude Code;
- Codex;
- GitHub Copilot;
- Gemini CLI.

При внедрении VCP в другой репозиторий не копируйте root `AGENTS.md` blindly.
Используйте `templates/AGENTS.md` или agent templates под вашу среду.

См.:
- [docs_ru/comparisons.md](./docs_ru/comparisons.md)
- [docs_ru/product-model.md](./docs_ru/product-model.md)
- [docs_ru/killer-workflow.md](./docs_ru/killer-workflow.md)
- [docs_ru/trust-check.md](./docs_ru/trust-check.md)
- [docs_ru/anti-misread-guide.md](./docs_ru/anti-misread-guide.md)
- [docs_ru/evaluator-architecture-map.md](./docs_ru/evaluator-architecture-map.md)
- [docs_ru/proof-snapshot.md](./docs_ru/proof-snapshot.md)
- [docs_ru/ai-tooling.md](./docs_ru/ai-tooling.md)
- [docs_ru/integration-setup.md](./docs_ru/integration-setup.md)
- [docs_ru/evaluation-receipt.md](./docs_ru/evaluation-receipt.md)
- [docs_ru/public-proof-demo.md](./docs_ru/public-proof-demo.md)
- [docs_ru/community-and-adoption-status.md](./docs_ru/community-and-adoption-status.md)

## Экономьте AI-токены

Для evaluators:
используйте `EVALUATE_THIS_REPO.md`, `PUBLIC_EVALUATION_KIT.md` и `.vcp/evaluator-pack.json` до случайного чтения файлов.

См.:
- [docs_ru/agent-model-routing.md](./docs_ru/agent-model-routing.md)
- [docs_ru/evaluator-token-budget.md](./docs_ru/evaluator-token-budget.md)
- [docs_ru/visuals.md](./docs_ru/visuals.md)
- [docs/local-platform-flow.md](./docs/local-platform-flow.md)
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- `python3 -m pip install .`

## Roadmap-only

- hosted dashboard
- VS Code extension
- plugin marketplace
- cloud sync
