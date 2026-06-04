# Vibe Coding Protocols

[English version](./README.md)

Build with AI. Ship with control.

Vibe Coding Protocols — это практический локальный toolkit для AI-assisted delivery.
Он помогает выбрать правильный трек, безопасно внедрять нужные слои и выпускать изменения с видимым review и release control.

> Текущий пакет репозитория: `v0.8.1`  
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.8.1`.

Repository package: `v0.8.1`

## Новое в v0.8.1: 10-minute adoption path, killer demo и product narrative sync

`v0.8.1` делает первую пользовательскую историю короче и понятнее:

- install -> onboard -> classify -> adopt plan -> launch check теперь собраны в один короткий путь;
- появился killer demo для raw AI-generated MVP с route, risks, copy-list, dry-run apply и launch check;
- proof language теперь яснее разделяет real, sanitized, synthetic, maintainer-known и unknown;
- integration roadmap описан без притворства, что он уже shipped.

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
- `python3 -m pip install . && vcp doctor`
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
python3 -m pip install .
vcp doctor
vcp evaluate
```

Публичные PyPI/npm пакеты не заявляются, пока они реально не опубликованы.

## Добавить VCP в PR

Используйте workflow example в `ci-examples/github-actions/vcp-pr-gate.yml`.

## Proof layer

Используй вместе:
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/proof-layer.md](./docs/proof-layer.md)
- [templates/reports/adoption-case-study.md](./templates/reports/adoption-case-study.md)
- [case-studies/README.md](./case-studies/README.md)

## Integration roadmap

Roadmap и future-facing integration positioning лежат в:
- [docs/roadmap/integrations.md](./docs/roadmap/integrations.md)
- [docs/roadmap/vscode-extension.md](./docs/roadmap/vscode-extension.md)

Эти docs нельзя читать как доказательство, что такие integrations уже shipped.

## Release notes

- [docs/release-v0.8.1.md](./docs/release-v0.8.1.md)
