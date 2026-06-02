# Vibe Coding Protocols

[English version](./README.md)

[![Версия repo](https://img.shields.io/badge/repo-v0.5.2-blue)](./CHANGELOG.md)
[![Методология](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

VCP — это управляемый workflow для AI-assisted разработки.
Когда AI помогает писать код, команда часто начинает двигаться быстрее, чем успевают собраться архитектура, review, stop conditions и release discipline.
VCP помогает сначала классифицировать проект, потом выбрать правильный route, взять только нужный adoption pack, провалидировать результат и прогнать review gate до следующего шага.

Пакет репозитория: `v0.5.2`

Веб-методология: `Vibe Coding Protocols v1.4`

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
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
npm run vcp -- doctor
```

## Это можно сразу отдать AI-агенту

Начинай с [AI_INTAKE.md](./AI_INTAKE.md), потом переходи в [START_HERE.md](./START_HERE.md). Если нужны agent rules, лучше брать [templates/AGENTS.md](./templates/AGENTS.md), а не копировать root `AGENTS.md`.
Если нужен готовый onboarding prompt, используй `python3 -m vcp_cli init --print-prompt` или [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md).

## В чем VCP помогает

- выбрать правильный route для реального репозитория, а не по умолчанию идти в Starter;
- держать production, regulated, public-site, maintenance и API-intake работу в безопасных границах;
- переносить небольшой релевантный набор файлов, а не копировать весь toolkit;
- прогонять validation перед merge, release или deploy;
- включать review gate после meaningful AI-generated изменений.

## Routes

| Ситуация | Route |
|---|---|
| Новый проект или идея | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Уже есть AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated или shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [Adoption Packs](./docs/adoption-packs.md) |
| Код работает, но его трудно менять | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| Расползся styling или ownership компонентов | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| Появился внешний API, SDK, webhook или SaaS | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Нужен приемочный gate для активного diff | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Публичный сайт, docs, trust или crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |

## Adoption Packs

Adoption Pack — это небольшой рекомендуемый набор файлов под конкретную ситуацию.
Например:
- Production Pack = hardening docs + audit backlog + security baseline + review gate.
- Shared Engine Pack = project map + architecture source of truth + cross-product release checks.
- Public Site Pack = `llms.txt` + `robots.txt` + schema.org + site-readiness checklist.

Если нужен быстрый вход, начни с [docs/adoption-packs.quickstart.md](./docs/adoption-packs.quickstart.md).

## Что VCP не делает

VCP — это не scanner, не pentest/offensive toolkit, не compliance certification и не замена human review. Это workflow и tooling layer для более безопасной AI-assisted delivery.

## Куда идти дальше

- [docs/cli.md](./docs/cli.md)
- [docs/npm.md](./docs/npm.md)
- [docs/windows.md](./docs/windows.md)
- [docs/init.md](./docs/init.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/roadmap.md](./docs/roadmap.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [docs/measured-impact.md](./docs/measured-impact.md)
- [docs/release-v0.5.2.md](./docs/release-v0.5.2.md)
