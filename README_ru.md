# Vibe Coding Protocols

[English version](./README.md)

Build with AI. Choose the right track. Adopt safely. Ship with control.

Vibe Coding Protocols — это практический локальный toolkit для AI-assisted delivery.
Он помогает выбрать правильный трек, безопасно внедрять нужные слои и выпускать изменения с видимым review и release control.

> Текущий пакет репозитория: `v0.8.3`  
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.8.3`.

Repository package: `v0.8.3`

## Новое в v0.8.3

`v0.8.3` добавляет следующий control layer VCP:

- spec-driven adoption track;
- integrations list command;
- contracts-first AI-MVP demo;
- project memory и decision log;
- fail-closed safety boundary;
- generated agent instruction templates;
- SaaS AI-MVP hardening pack;
- starter control layer;
- run state и checkpoint model;
- audit backlog dedup и staleness;
- batch evaluation mode;
- docs-site scaffold;
- agent behavior quality gate.

Релиз не поставляет hosted dashboard, plugin marketplace, VS Code extension, Go rewrite, public PyPI/npm publication, telemetry, cloud sync, personal assistant memory или autonomous notifications.

## Старт за 10 минут

Используй самый короткий практический путь:
- [docs/10-minute-adoption-path.md](./docs/10-minute-adoption-path.md)
- [docs/demos/raw-ai-mvp-to-controlled-launch.md](./docs/demos/raw-ai-mvp-to-controlled-launch.md)
- [docs/mvp-adoption-track.md](./docs/mvp-adoption-track.md)

## Для AI-агентов: не оценивайте VCP только по README

Перед заявлением о полном аудите репозитория проверьте:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`
- `REPO_CAPABILITIES_INDEX.md`

Используйте root `AGENTS.md` как маршрут верхнего уровня для репозитория, а `templates/AGENTS.md` только как template surface для копируемых проектов.

Если вы не можете проверить эти файлы плюс `.vcp/`, `vcp_cli/`, templates и benchmarks, помечайте оценку как `partial` или `shallow`.
Не выдавайте WebFetch/README summary за полный аудит репозитория.

## Главная история

- build with AI;
- choose the right track;
- adopt safely;
- ship with control.

## Быстрый старт по ситуации

| Ситуация | Команда |
|---|---|
| Я хочу понять этот репозиторий | `python3 -m vcp_cli audit-plan --json` |
| Я хочу попробовать VCP локально | `python3 -m vcp_cli doctor` |
| У меня новая идея проекта | `python3 -m vcp_cli spec quality-gate --json` |
| У меня AI-generated MVP | `python3 -m vcp_cli onboard --json` |
| Мне нужны инструкции по внедрению | `python3 -m vcp_cli adopt plan --json` |
| Мне нужна launch/release readiness проверка | `python3 -m vcp_cli release-check --json` |

## Два трека

### New Project Track

Используй, когда стартуешь от идеи, product brief или greenfield MVP.

Основной путь:
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `protocols/spec-driven/spec-foundation.md`
- `docs/spec-quality-gate.md`
- `docs/walkthroughs/new-ai-product-from-idea.md`

Полезные команды:
```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli spec quality-gate --json
python3 -m vcp_cli adopt plan --pack spec-foundation --json
```

### Existing Project Track

Используй, когда репозиторий уже существует, а реальная проблема — hardening, release control, architecture drift или launch clarity.

Основной путь:
- `docs/mvp-adoption-track.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/architecture-drift.md`
- `docs/release-readiness.md`
- `docs/pr-gate.md`

Полезные команды:
```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
python3 -m vcp_cli release-check --json
```

## Честная установка и distribution

Практические пути сегодня:
- `python3 -m vcp_cli doctor`
- `python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install --upgrade pip setuptools wheel && python3 -m pip install . && vcp doctor`
- `python3 -m venv --system-site-packages .venv && . .venv/bin/activate && python3 -m pip install . --no-build-isolation && vcp doctor` для restricted environments, где local build dependencies уже доступны
- опционально локальный `pipx install . && vcp doctor`, если проходит в вашем окружении
- `npm run vcp -- doctor`

VCP **не** заявляет о public PyPI или public npm publication, пока этого реально нет.

Смотри:
- [docs/install.md](./docs/install.md)
- [docs/distribution.md](./docs/distribution.md)
- [docs/pip-install.md](./docs/pip-install.md)
- [docs/pypi-publishing.md](./docs/pypi-publishing.md)

## Тиры внедрения

- `Lite`: solo dev, MVP, lower-risk AI coding.
- `Team`: shared repo, backlog, architecture memory, PR Gate.
- `Governed`: production, auth/payment/data, release и third-party control.

Смотри [docs/adoption-tiers.md](./docs/adoption-tiers.md).

## Безопасное внедрение, а не blind apply

Сначала используй planner и dry-run:

```bash
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
```

Не воспринимай apply как guarantee и не используй confirmed apply на production-репозитории без review.

## Public growth check

Если MVP уже публично доступен, добавь:

```bash
python3 -m vcp_cli public-growth check --json
```

Это local readiness и visibility check, а не ranking или citation guarantee.

## Workflow planning note

Используй:

```bash
python3 -m vcp_cli workflow plan --json
```

Workflow JSON остается planning surface, а не hidden execution engine.

## Установить и запустить

Текущий стабильный локальный путь:

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor
vcp evaluate
```

Публичные PyPI/npm пакеты не заявляются, пока они реально не опубликованы.

## Добавить VCP в PR

Используйте workflow example в `ci-examples/github-actions/vcp-pr-gate.yml`.


## Agent control и project memory

Ключевые поверхности:
- [docs/spec-driven-adoption.md](./docs/spec-driven-adoption.md)
- [docs/project-memory.md](./docs/project-memory.md)
- [docs/decision-log.md](./docs/decision-log.md)
- [docs/safety/fail-closed.md](./docs/safety/fail-closed.md)
- [docs/agent-instructions.md](./docs/agent-instructions.md)
- [docs/agent-behavior-gate.md](./docs/agent-behavior-gate.md)
- [docs/starter-control-layer.md](./docs/starter-control-layer.md)
- [docs/run-state.md](./docs/run-state.md)
- [docs/audit-backlog.md](./docs/audit-backlog.md)
- [docs/batch-evaluation.md](./docs/batch-evaluation.md)
- [docs/docs-site.md](./docs/docs-site.md)

## Proof layer

Используй вместе:
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/proof-layer.md](./docs/proof-layer.md)
- [templates/reports/adoption-case-study.md](./templates/reports/adoption-case-study.md)
- [case-studies/README.md](./case-studies/README.md)

## Integration status и local dashboard

Шипнутые local-first scaffolds и их статусы лежат в:
- [docs/integrations/status-model.md](./docs/integrations/status-model.md)
- [.vcp/integrations.json](./.vcp/integrations.json)
- [docs/dashboard.md](./docs/dashboard.md)
- [docs/plugins/README.md](./docs/plugins/README.md)
- [docs/metrics-board.md](./docs/metrics-board.md)
- [docs/audit-backlog-visualization.md](./docs/audit-backlog-visualization.md)

Roadmap-only и not-shipped surfaces по-прежнему лежат в:
- [docs/roadmap/integrations.md](./docs/roadmap/integrations.md)
- [docs/roadmap/vscode-extension.md](./docs/roadmap/vscode-extension.md)

Эти docs нельзя читать как доказательство hosted services, official integrations или plugin marketplace.

## Release notes

- [docs/release-v0.8.3.md](./docs/release-v0.8.3.md)
