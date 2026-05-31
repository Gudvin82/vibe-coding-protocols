# Vibe Coding Protocols

[English version](./README.md)

[![Версия repo](https://img.shields.io/badge/repo-v0.5.0-blue)](./CHANGELOG.md)
[![Методология](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)

**Это не коллекция промптов.**

VCP — это controlled AI delivery framework для AI-assisted разработки.
Он дает маршруты,
protocols,
adoption packs,
validation,
review gates,
manifests,
benchmarks
и project memory,
чтобы AI не менял код хаотично.

Пакет репозитория: `v0.5.0`

Веб-методология: `Vibe Coding Protocols v1.4`

## Отдаешь репозиторий AI-агенту?

Начинай с [AI_INTAKE.md](./AI_INTAKE.md), а не с поверхностного чтения `README.md`.
If agent rules are needed, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.
Потом смотри:
- [START_HERE.md](./START_HERE.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md)

## Попробуй product layer

```bash
python3 -m vcp_cli route --profile shared-engine
python3 -m vcp_cli adopt --pack shared-engine --dry-run
python3 -m vcp_cli review plan
python3 -m vcp_cli score
python3 -m vcp_cli benchmark run
```

## С чего начать

| Ситуация | Куда идти |
|---|---|
| Новый проект или идея | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Уже есть AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated или shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [adoption packs](./docs/adoption-packs.md) |
| Код работает, но его трудно менять | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| Расползся UI styling ownership | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| Нужен приемочный gate для активного diff | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Публичный сайт или docs | [Public Site Readiness](./docs/public-site-readiness.md) |

## Что стало product-grade в v0.5.0

- единый локальный CLI surface
- machine-readable manifests
- route chooser
- adoption dry-run planner
- helper для post-task review gate
- heuristic score report
- AI adoption benchmark scenarios
- demo output
- sanitized case-study structure

## Новое: Post-Task Code Review Gate

После значимых AI-generated изменений не начинай сразу следующую фичу.
Запусти `/loop-code-review` или используй Post-Task Code Review Protocol:
посмотри активный diff,
исправь actionable findings,
прогони validation
и принимай состояние только после green review плюс validation.

## Что VCP не делает

- не hacking toolkit;
- не exploit framework;
- не pentest suite;
- не bug bounty automation suite;
- не red-team operator;
- не DDoS, RAT, phishing или payload toolkit;
- не production security certification;
- не legal compliance certification;
- не замена developers, tests, security review, legal review или human judgment.

## Ключевые ссылки

- [AI_INTAKE.md](./AI_INTAKE.md)
- [docs/cli.md](./docs/cli.md)
- [docs/route-map.md](./docs/route-map.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [docs/public-site-readiness.md](./docs/public-site-readiness.md)
- [docs/seo-ai-crawler-readiness.md](./docs/seo-ai-crawler-readiness.md)
- [docs/community-feedback.md](./docs/community-feedback.md)
- [docs/release-v0.5.0.md](./docs/release-v0.5.0.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
