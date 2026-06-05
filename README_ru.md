# Vibe Coding Protocols

[English version](./README.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.8.5-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Build with AI. Choose the right track. Adopt safely. Ship with control.

Vibe Coding Protocols — это практический локальный набор инструментов для AI-assisted delivery.
Он помогает выбрать правильный трек, безопасно внедрять нужные слои и выпускать изменения с видимым review и release control.

> Текущий пакет репозитория: `v0.8.5`  
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.8.5`.

Repository package: `v0.8.5`

## Новое в v0.8.5

`v0.8.5` объединяет запланированную работу по local platform UX и integration packs в один релиз.

Он усиливает:
- UX локального dashboard;
- local platform flow;
- project map и run history представления;
- integration packs;
- ясность IDE roadmap;
- docs-site scaffold;
- AI-readable docs;
- паритет русской документации.

Релиз не поставляет hosted dashboard, hosted platform, VS Code extension, plugin marketplace, Go rewrite, public PyPI/npm publication, cloud sync, telemetry, remote plugin registry, credential vault, production safety guarantees, launch guarantees, SEO/GEO ranking guarantees или guaranteed AI citation.

## Старт за 10 минут

Используй самый короткий практический путь:
- [docs/10-minute-adoption-path.md](./docs/10-minute-adoption-path.md)
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- [docs/local-platform-flow.md](./docs/local-platform-flow.md)
- [docs/demos/raw-ai-mvp-to-controlled-launch.md](./docs/demos/raw-ai-mvp-to-controlled-launch.md)
- [docs/mvp-adoption-track.md](./docs/mvp-adoption-track.md)
- [docs_ru/README.md](./docs_ru/README.md)

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
| Я хочу попробовать VCP локально | `python3 -m vcp_cli doctor --json` |
| У меня новая идея проекта | `python3 -m vcp_cli spec quality-gate --json` |
| У меня AI-generated MVP | `python3 -m vcp_cli onboard --json` |
| Мне нужны инструкции по внедрению | `python3 -m vcp_cli adopt plan --json` |
| Мне нужна launch/release readiness проверка | `python3 -m vcp_cli release-check --json` |
| Мне нужен локальный dashboard | `python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json` |
| Мне нужен статус интеграций | `python3 -m vcp_cli integrations list --json` |

## Два трека

Смотри также:
- [docs/track-model.md](./docs/track-model.md)
- [docs/two-track-model.md](./docs/two-track-model.md)

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

Специализированный guided path, который часто стартует отсюда:
- `docs/spec-driven-adoption.md`

### Existing Project Track

Используй, когда репозиторий уже существует, а реальная проблема — hardening, release control, architecture drift или launch clarity.

Основной путь:
- `docs/mvp-adoption-track.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/architecture-drift.md`
- `docs/release-readiness.md`
- `docs/pr-gate.md`

Специализированный guided path внутри этого трека:
- `docs/mvp-to-launch-path.md`
- `.vcp/workflows/mvp-to-launch.json`
- `docs/launch-decision-checklist.md`

Полезные команды:
```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json
python3 -m vcp_cli release-check --json
python3 -m vcp_cli pr-gate explain --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

## MVP-to-Launch внутри Existing Project Track

Рекомендуемый command path:

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp workflow plan --id mvp-to-launch --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp adopt plan --pack saas-ai-mvp-hardening --json
vcp pr-gate explain --json
vcp metrics board --json
vcp dashboard build --output ./vcp-dashboard --json
```

Это локальный launch-control flow, а не deploy platform.

## Local platform flow

В `v0.8.5` VCP должен ощущаться как связная локальная control platform, но он остается local-first и reviewable.

Смотри:
- [docs/local-platform-flow.md](./docs/local-platform-flow.md)
- [docs/dashboard.md](./docs/dashboard.md)
- [docs/project-map.md](./docs/project-map.md)
- [docs/run-state.md](./docs/run-state.md)
- [docs/batch-evaluation.md](./docs/batch-evaluation.md)

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

## Integration packs

Используй integration packs, когда нужен локальный копируемый setup bundle без заявления об official marketplace integration.

Основные поверхности:
- [docs/integration-packs.md](./docs/integration-packs.md)
- [docs/integrations/status-model.md](./docs/integrations/status-model.md)
- [.vcp/integrations.json](./.vcp/integrations.json)
- `.vcp/integration-packs.json`

Полезные команды:
```bash
python3 -m vcp_cli integrations list --json
python3 -m vcp_cli integrations list --status shipped --json
python3 -m vcp_cli integrations packs --json
```

## Безопасное внедрение, а не blind apply

Сначала используй planner и dry-run:

```bash
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
```

Не воспринимай apply как guarantee и не используй confirmed apply на production-репозитории без review.

## Batch/workspace flow

Если у тебя несколько AI-generated MVP или workspace с несколькими пакетами:

```bash
python3 -m vcp_cli batch evaluate --targets ./targets.txt --json
```

Этот путь остается локальным, детерминированным и не меняет targets.

## Добавить VCP в PR

Используй workflow example в `ci-examples/github-actions/vcp-pr-gate.yml`.
Читай:
- [docs/pr-gate.md](./docs/pr-gate.md)
- [docs/pr-gate-approval-model.md](./docs/pr-gate-approval-model.md)
- [docs/launch-decision-checklist.md](./docs/launch-decision-checklist.md)

## Русская документация

Русская документация — это публичная user-facing часть релиза.
Стартуй отсюда:
- [README_ru.md](./README_ru.md)
- [docs_ru/README.md](./docs_ru/README.md)
- [docs_ru/install.md](./docs_ru/install.md)
- [docs_ru/mvp-to-launch-path.md](./docs_ru/mvp-to-launch-path.md)
- [docs_ru/dashboard.md](./docs_ru/dashboard.md)
- [docs_ru/integration-packs.md](./docs_ru/integration-packs.md)

## Proof layer

Используй вместе:
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/proof-layer.md](./docs/proof-layer.md)
- [templates/reports/adoption-case-study.md](./templates/reports/adoption-case-study.md)
- [case-studies/README.md](./case-studies/README.md)

## Release notes

- [docs/release-v0.8.5.md](./docs/release-v0.8.5.md)
- [docs_ru/release-v0.8.5.md](./docs_ru/release-v0.8.5.md)
