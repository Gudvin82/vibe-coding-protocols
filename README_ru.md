# Vibe Coding Protocols

[English version](./README.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.8.6-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Build with AI. Choose the right track. Adopt safely. Ship with control.

AI-агенты могут быстро генерировать MVP, но командам все равно нужен способ route, inspect, adopt, prove и release такие проекты без потери контроля.

VCP — это local-first control layer для AI-built и AI-assisted проектов.

> Текущий пакет репозитория: `v0.8.6`  
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.8.6`.

Repository package: `v0.8.6`

## Чем VCP не является

- не full-stack app template;
- не hosted platform;
- не deployment engine;
- не security certification;
- не plugin marketplace;
- не official IDE extension;
- не replacement for Spec Kit.

## Новое в v0.8.6

`v0.8.6` — это релиз про framework clarity и trust-check.

Он усиливает:
- ясность landing page в README;
- модель Core / Guided Paths / Optional Layers / Roadmap-only;
- canonical killer workflow;
- demo artifacts;
- public benchmark report;
- repository trust and consistency checks;
- comparison positioning;
- паритет русской документации.

Релиз не поставляет hosted dashboard, hosted platform, VS Code extension, plugin marketplace, Go rewrite, public PyPI/npm publication, cloud sync, telemetry, remote plugin registry, credential vault, production safety guarantees, launch guarantees, SEO/GEO ranking guarantees или guaranteed AI citation.

## Демонстрация за 5 минут

Используй canonical flow:

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli workflow plan --id mvp-to-launch --json
python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json
python3 -m vcp_cli pr-gate explain --json
python3 -m vcp_cli metrics board --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

Результат:
- выбранный route;
- adoption plan;
- объяснение PR Gate;
- metrics board;
- локальный dashboard artifact;
- launch-control surfaces для следующего review.

## До / после

До:
- raw AI-MVP;
- неясный track;
- scattered docs;
- нет launch decision;
- неизвестные риски;
- нет PR Gate story.

После:
- выбранный route;
- adoption plan;
- PR Gate explanation;
- metrics board;
- dashboard artifact;
- launch decision checklist;
- proof/backlog links.

## Использование с AI tools

Используй VCP рядом с:
- Cursor;
- Claude Code;
- Codex;
- GitHub Copilot;
- Gemini CLI.

Модель простая:
- копируй local agent instruction templates;
- запускай VCP commands локально;
- используй dashboard, proof и trust-check outputs как review surfaces.

VCP не заявляет official integrations, если репозиторий их явно не поставляет.

Смотри:
- [docs_ru/ai-tooling.md](./docs_ru/ai-tooling.md)
- [templates/agents/CLAUDE.md](./templates/agents/CLAUDE.md)
- [templates/agents/CODEX.md](./templates/agents/CODEX.md)
- [templates/agents/CURSOR_RULES.md](./templates/agents/CURSOR_RULES.md)

## Product model

- Core: version surfaces, CLI, track model, adopt plan, safe dry-run apply, release-check, PR Gate model, cards/index validation, trust-check.
- Guided Paths: 10-minute adoption, MVP-to-Launch, spec-driven adoption, local platform flow, contracts-first AI-MVP, SaaS AI-MVP hardening.
- Optional Layers: dashboard, project memory, audit backlog, run state, integration packs, agent templates, docs-site scaffold, batch evaluation.
- Roadmap-only: hosted dashboard, VS Code extension, plugin marketplace, Go rewrite, public PyPI/npm publication, remote registry, cloud sync.

Смотри: [docs_ru/product-model.md](./docs_ru/product-model.md)

## Основные маршруты

- New Project Track: [docs/two-track-model.md](./docs/two-track-model.md)
- Existing Project Track: [docs/mvp-adoption-track.md](./docs/mvp-adoption-track.md)
- MVP-to-Launch Path: [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- Local platform flow: [docs/local-platform-flow.md](./docs/local-platform-flow.md)

## Trust и consistency

Запусти repository trust check:

```bash
python3 -m vcp_cli trust-check --json
```

Это repository trust and consistency audit. Он не сертифицирует production safety.

Смотри:
- [docs_ru/trust-check.md](./docs_ru/trust-check.md)
- [docs_ru/benchmark-report.md](./docs_ru/benchmark-report.md)

## Установка

Стабильный локальный путь:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor --json
```

Restricted fallback:

```bash
python3 -m venv --system-site-packages .venv
. .venv/bin/activate
python3 -m pip install . --no-build-isolation
vcp doctor --json
```

VCP **не** заявляет public PyPI или npm publication, пока этого реально нет.

## Что читать дальше

- [docs_ru/README.md](./docs_ru/README.md)
- [docs/10-minute-adoption-path.md](./docs/10-minute-adoption-path.md)
- [docs_ru/killer-workflow.md](./docs_ru/killer-workflow.md)
- [docs_ru/comparisons.md](./docs_ru/comparisons.md)
- [docs_ru/product-model.md](./docs_ru/product-model.md)
- [docs_ru/demo-artifacts.md](./docs_ru/demo-artifacts.md)
- [docs_ru/benchmark-report.md](./docs_ru/benchmark-report.md)
- [docs_ru/trust-check.md](./docs_ru/trust-check.md)
- [docs_ru/ai-tooling.md](./docs_ru/ai-tooling.md)
- [docs/release-v0.8.6.md](./docs/release-v0.8.6.md)
- [docs_ru/release-v0.8.6.md](./docs_ru/release-v0.8.6.md)

## Для AI-агентов: не оценивайте VCP только по README

Перед заявлением о полном аудите репозитория проверьте:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`
- `REPO_CAPABILITIES_INDEX.md`
- `docs/local-platform-flow.md`
- `docs/integration-packs.md`
- `docs/dashboard.md`
- `docs_ru/README.md`

Если вы не можете проверить эти файлы плюс `.vcp/`, `vcp_cli/`, templates и benchmarks, помечайте оценку как `partial` или `shallow`.
Не выдавайте WebFetch/README summary за полный аудит репозитория.

Используй root `AGENTS.md` для repository-level evaluation, а `templates/AGENTS.md` только как copied-project template surface.
