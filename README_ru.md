# Vibe Coding Protocols

[English version](./README.md)

[![Версия repo](https://img.shields.io/badge/repo-v0.5.1-blue)](./CHANGELOG.md)
[![Методология](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)

**Это не коллекция промптов.**

VCP — это controlled AI delivery framework для AI-assisted разработки.
Он дает маршруты, protocols, adoption packs, validation, review gates, manifests, benchmarks и project memory, чтобы AI не менял код хаотично.

Пакет репозитория: `v0.5.1`

Веб-методология: `Vibe Coding Protocols v1.4`

## Отдаешь репозиторий AI-агенту?

Начинай с [AI_INTAKE.md](./AI_INTAKE.md), а не с поверхностного чтения `README.md`.
If agent rules are needed, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.
Потом смотри:
- [START_HERE.md](./START_HERE.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md)

## Windows и безопасность внешних API

Пользователи Windows могут идти по основному VCP-маршруту через Python CLI из PowerShell.
Bash-скрипты остаются поддержанными для legacy parity.
Если добавляется любой внешний API, сначала запускай Third-party API Intake, а уже потом пиши интеграционный код.
Public или free API не означает production-safe по умолчанию.

## С чего начать

| Ситуация | Куда идти |
|---|---|
| Новый проект или идея | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Уже есть AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated или shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [adoption packs](./docs/adoption-packs.md) |
| Код работает, но его трудно менять | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| Расползся UI styling ownership | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| Появился внешний API, SDK или webhook | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Нужен приемочный gate для активного diff | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Публичный сайт или docs | [Public Site Readiness](./docs/public-site-readiness.md) |

## Текущий CLI surface

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli check --fast
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli route --profile third-party-api --json
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run
python3 -m vcp_cli score --json
```

PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli check --fast
py -m vcp_cli route --profile production --json
```

## Что VCP не делает

- не hacking toolkit;
- не exploit framework;
- не pentest suite;
- не bug bounty automation suite;
- не public API directory;
- не public API recommendation engine;
- не production security certification;
- не legal compliance certification;
- не замена developers, tests, security review, legal review или human judgment.

## Ключевые ссылки

- [AI_INTAKE.md](./AI_INTAKE.md)
- [docs/cli.md](./docs/cli.md)
- [docs/windows.md](./docs/windows.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/release-v0.5.1.md](./docs/release-v0.5.1.md)
