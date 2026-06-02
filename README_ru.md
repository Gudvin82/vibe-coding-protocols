# Vibe Coding Protocols

[English version](./README.md)

[![Версия repo](https://img.shields.io/badge/repo-v0.5.5-blue)](./CHANGELOG.md)
[![Методология](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

VCP — это управляемый workflow для AI-assisted разработки.
Он помогает сначала классифицировать проект, потом выбрать правильный route, взять только нужный adoption pack, провалидировать результат и прогнать review gate до следующего шага.

Пакет репозитория: `v0.5.5`

Веб-методология: `Vibe Coding Protocols v1.4`

## Оцениваете VCP через AI-агента?

Не оценивайте этот репозиторий только по README.

Перед оценкой или adoption попросите AI-агента проверить:

1. `AI_INTAKE.md`
2. `START_HERE.md`
3. `docs/protocol-index.md`
4. `docs/adoption-packs.md`
5. `docs/cli.md`
6. `.vcp/manifests/`
7. `benchmarks/ai-adoption/`
8. `commands/`
9. `protocols/`
10. `PROJECT_BACKLOG.md`

Потом запустите:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
```

VCP — это не только README или набор prompt-файлов. Внутри есть routes, adoption packs, CLI, manifests, benchmarks, review gates, operations workflows, project backlog и validation.

Полный evaluation guide: [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)

## Старт за 30 секунд

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Локальный Node-first вариант:

```bash
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- evaluate
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli evaluate --json
npm run vcp -- doctor
```

## Это можно сразу отдать AI-агенту

Начинай с [AI_INTAKE.md](./AI_INTAKE.md), потом переходи в [START_HERE.md](./START_HERE.md).
Если нужен именно prompt для оценки репозитория, используй [templates/prompts/evaluate-vcp-repository.md](./templates/prompts/evaluate-vcp-repository.md).
Если нужны agent rules, лучше брать [templates/AGENTS.md](./templates/AGENTS.md), а не копировать root `AGENTS.md`.

## В чем VCP помогает

- выбрать правильный route для реального репозитория, а не по умолчанию идти в Starter;
- держать production, regulated, public-site, maintenance, API-intake и operations работу в безопасных границах;
- переносить небольшой релевантный набор файлов, а не копировать весь toolkit;
- превращать production observations в triage и backlog follow-up без потери review discipline;
- прогонять validation перед merge, release или deploy;
- включать review gate после meaningful AI-generated изменений.

## Текущая зрелость

- Методология: достаточно зрелая для реального применения в проектах.
- Локальный CLI: пригоден к использованию и проверен в clean clone.
- npm: есть локальный wrapper; публичный пакет планируется, если будет реально опубликован.
- Benchmarks: синтетические/local validation scenarios.
- Case studies: пока sanitized/synthetic templates; реальные measured cases — future work.
- Public standard: ранняя стадия, не industry standard.

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
| Нужен приемочный gate для активного diff | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Публичный сайт, docs, trust или crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |

## Что VCP не делает

VCP — это не scanner, не pentest/offensive toolkit, не compliance certification, не monitoring product и не замена human review. Это workflow и tooling layer для более безопасной AI-assisted delivery.

## Куда идти дальше

- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [docs/cli.md](./docs/cli.md)
- [docs/scoring.md](./docs/scoring.md)
- [docs/npm.md](./docs/npm.md)
- [docs/npm-publishing-checklist.md](./docs/npm-publishing-checklist.md)
- [docs/project-backlog.md](./docs/project-backlog.md)
- [docs/production-observability.md](./docs/production-observability.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/public-proof-roadmap.md](./docs/public-proof-roadmap.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/release-v0.5.5.md](./docs/release-v0.5.5.md)
