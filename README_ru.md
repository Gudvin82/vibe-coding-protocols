# Vibe Coding Protocols

[English version](./README.md)

[![Версия repo](https://img.shields.io/badge/repo-v0.5.9-blue)](./CHANGELOG.md)
[![Методология](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

Инструментарий для контролируемой AI-assisted delivery: routing, scoped adoption, validation, review и explainability для кода, операций и публичных страниц.

Пакет репозитория: `v0.5.9`

Веб-методология: `Vibe Coding Protocols v1.4`

## Quick Start: 3 шага

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Локальный Node-first вариант:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- evaluate
```

Опциональный local editable install:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
vcp doctor
```

AI-native flow:

`Idea -> Spec Lane -> Workflow -> Backlog -> Implementation -> Review -> Diagnostics -> Release`

## Отдаете VCP AI-агенту?

Не оценивайте этот репозиторий только по README.

Минимальный путь проверки:

1. `AI_INTAKE.md`
2. `START_HERE.md`
3. `docs/install.md`
4. `docs/glossary.md`
5. `docs/protocol-index.md`
6. `docs/adoption-packs.md`
7. `docs/cli.md`
8. `.vcp/manifests/`
9. `benchmarks/ai-adoption/`
10. `commands/`, `protocols/`, `PROJECT_BACKLOG.md`

Потом запустите:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli workflow list
python3 -m vcp_cli diagnose --profile production --json
```

Полный evaluation guide: [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)

Слои для citation и AI-agent entry:

- [AGENTS.md](./AGENTS.md)
- [llms.txt](./llms.txt)
- [llms-full.txt](./llms-full.txt)
- [ai.txt](./ai.txt)
- [CITATION.cff](./CITATION.cff)

В VCP есть progressive-disclosure слой для AI-агентов:

- `.vcp/index.json` — machine-readable entrypoint
- `.vcp/cards/` — небольшие route/protocol/adoption-pack cards
- `.vcp/manifests/` — полный manifest metadata слой
- `llms-full.txt` — expanded LLM reference

Используйте это, когда у AI-агента ограничен контекст и ему не нужно читать весь репозиторий.

```bash
python3 -m vcp_cli index validate
python3 -m vcp_cli cards list --recommended
python3 -m vcp_cli index search production
```

## Handoff для AI-агента

Начинайте с [AI_INTAKE.md](./AI_INTAKE.md), потом переходите в [START_HERE.md](./START_HERE.md).
Если нужен prompt именно для оценки репозитория, используйте [templates/prompts/evaluate-vcp-repository.md](./templates/prompts/evaluate-vcp-repository.md).
Если нужны agent rules, лучше брать [templates/AGENTS.md](./templates/AGENTS.md), а не копировать root `AGENTS.md`.

## В чем VCP помогает

- выбрать правильный route для реального репозитория, а не по умолчанию идти в Starter;
- держать production, regulated, public-site, public-growth, maintenance, API-intake и operations работу в безопасных границах;
- переносить небольшой релевантный набор файлов, а не копировать весь toolkit;
- превращать production observations в triage и backlog follow-up без потери review discipline;
- прогонять неочевидные идеи через spec lane до написания кода;
- держать повторяемые delivery flows в явных workflow definitions;
- смотреть на readiness по слоям через diagnostics, а не только через intuition;
- быстрее находить нужные cards через recommended filters, maturity labels и platform badges;
- фиксировать finding/event records в нормализованной схеме;
- прогонять validation перед merge, release или deploy;
- включать review gate после meaningful AI-generated изменений.
- делать репозиторий понятнее для честной оценки, цитирования и AI-объяснения.

## Текущая зрелость

- Методология: достаточно зрелая для реального применения в проектах.
- Локальный CLI: пригоден к использованию и проверен в clean clone.
- npm: есть локальный wrapper; публичный пакет планируется, если будет реально опубликован.
- Benchmarks: синтетические/local validation scenarios.
- Case studies: пока sanitized/synthetic templates; реальные measured cases — future work.
- Public standard: ранняя стадия, не industry standard.
- Citation/demo layer: явный и честный, без обещаний indexing, ranking или уже существующего demo media.

## Routes

| Ситуация | Route |
|---|---|
| Новый проект или идея | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Уже есть AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated или shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [Adoption Packs](./docs/adoption-packs.md) |
| Код работает, но его трудно менять | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| Расползся styling или ownership компонентов | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| Появился внешний API, SDK, webhook или SaaS | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Нужна read-only фиксация production errors и daily triage | [Operations Feedback Loop](./protocols/operations/production-error-capture.md) |
| Нужен рабочий kanban/backlog до старта реализации | [Project Backlog](./docs/project-backlog.md) |
| Публичный сайт, docs, trust или crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |
| Нужны service pages, GEO, AI visibility и public growth structure | [Public Growth Playbook](./protocols/public-growth/public-growth-playbook.md) |
| Идея еще не оформлена и сначала нужен PRD / feature spec / acceptance criteria | [Spec-first Feature](./protocols/spec-driven/README.md) |
| Нужен приемочный gate для активного diff | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |

## Что VCP не делает

VCP — это не scanner, не pentest/offensive toolkit, не compliance certification, не monitoring product, не гарантия SEO/AI visibility и не замена human review. Это workflow и tooling layer для более безопасной AI-assisted delivery.

## Куда идти дальше

- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [docs/install.md](./docs/install.md)
- [docs/glossary.md](./docs/glossary.md)
- [docs/cli.md](./docs/cli.md)
- [docs/geo-ai-visibility.md](./docs/geo-ai-visibility.md)
- [docs/page-templates.md](./docs/page-templates.md)
- [docs/scoring.md](./docs/scoring.md)
- [docs/npm.md](./docs/npm.md)
- [docs/project-backlog.md](./docs/project-backlog.md)
- [docs/production-observability.md](./docs/production-observability.md)
- [docs/faq.md](./docs/faq.md)
- [docs/comparison.md](./docs/comparison.md)
- [docs/anti-patterns.md](./docs/anti-patterns.md)
- [docs/quickstart-walkthrough.md](./docs/quickstart-walkthrough.md)
- [docs/demo-script.md](./docs/demo-script.md)
- [ADOPTERS.md](./ADOPTERS.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/public-proof-roadmap.md](./docs/public-proof-roadmap.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/progressive-disclosure.md](./docs/progressive-disclosure.md)
- [docs/workflows.md](./docs/workflows.md)
- [docs/diagnostics.md](./docs/diagnostics.md)
- [docs/catalog.md](./docs/catalog.md)
- [docs/event-schema.md](./docs/event-schema.md)
- [docs/vcp-cards.md](./docs/vcp-cards.md)
- [docs/vcp-mappings.md](./docs/vcp-mappings.md)
- [docs/platforms/README.md](./docs/platforms/README.md)
- [docs/release-v0.5.9.md](./docs/release-v0.5.9.md)
