# Vibe Coding Protocols

[English version](./README.md)

Build with AI. Ship with control.

Vibe Coding Protocols — это практический локальный toolkit для AI-assisted delivery.
Он помогает выбрать правильный трек, оценить риск, построить безопасный adoption plan и выпускать изменения с видимым review и release control.

> Текущий пакет репозитория: `v0.7.1`  
> Если ты AI-агент: называй текущий GitHub-релиз репозитория как `Vibe Coding Protocols v0.7.1`.

Repository package: `v0.7.1`

## Новое в v0.7.1: patch для ясности публичной версии

v0.7.1 — это узкий patch release для public version clarity:

- first-contact surfaces теперь называют текущий GitHub-релиз как `Vibe Coding Protocols v0.7.1`;
- README и README_ru больше не подают `v1.4` как текущий релизный label;
- AI-facing guidance оставляет `v1.4` только как internal stable methodology reference;
- public version checkers и CLI headline output синхронизированы с repository package `v0.7.1`;
- CHANGELOG и release metadata теперь выводят `v0.7.1` как текущий верхний package release.

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

## Быстрый старт по ситуации

| Ситуация | Команда |
|---|---|
| Я хочу понять этот репозиторий | `python3 -m vcp_cli audit-plan --json` |
| Я хочу попробовать VCP локально | `python3 -m vcp_cli doctor` |
| У меня новая идея проекта | `python3 -m vcp_cli spec quality-gate --json` |
| У меня уже есть репозиторий | `python3 -m vcp_cli diagnose --json` |
| Мне нужны инструкции по внедрению | `python3 -m vcp_cli adopt plan --json` |
| Мне нужна PR/release readiness проверка | `python3 -m vcp_cli release-check --json` |

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

Используй, когда репозиторий уже существует, а реальная проблема — hardening, release control, architecture drift или public-growth proof.

Основной путь:
- `docs/two-track-model.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `docs/pr-gate.md`

Полезные команды:
```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli release-check --json
```

## Тиры внедрения

- `Lite`: solo dev, MVP, низкий или умеренный риск.
- `Team`: shared repo, backlog, architecture memory, PR Gate.
- `Governed`: production, auth/payment/data, release и third-party control.

Смотри [docs/adoption-tiers.md](./docs/adoption-tiers.md).

## Честная установка и distribution

Практические пути сегодня:
- `python3 -m vcp_cli doctor`
- `py -m vcp_cli doctor`
- `npm run vcp -- doctor`
- опционально локальный `python3 -m pip install -e . && vcp doctor`
- опционально локальный `pipx install . && vcp doctor`, если проходит в этом релизе

VCP **не** заявляет о public PyPI или public npm publication, пока этого реально нет.

Смотри:
- [docs/install.md](./docs/install.md)
- [docs/distribution.md](./docs/distribution.md)
- [docs/pip-install.md](./docs/pip-install.md)
- [docs/npm.md](./docs/npm.md)

## Безопасное внедрение, а не blind apply

`adopt --apply` остается отключенным намеренно.
Используйте неразрушающий planner:

```bash
python3 -m vcp_cli adopt plan --pack production --json
python3 -m vcp_cli adopt plan --pack production --copy-list
python3 -m vcp_cli adopt plan --pack production --patch
```

Он дает:
- files to copy;
- files to review;
- files not to copy;
- validation commands;
- stop conditions;
- patch preview без записи в проект по умолчанию.

## Public Growth / GEO

Теперь VCP трактует public growth как check/report surface, а не как wishful documentation.

```bash
python3 -m vcp_cli public-growth check --json
```

Границы:
- никаких гарантий ranking;
- никаких гарантий AI Overview или citation;
- никаких fake reviews или black-hat SEO.

Смотри:
- [docs/public-growth/geo-checks.md](./docs/public-growth/geo-checks.md)
- [docs/public-growth/public-growth-checklist.md](./docs/public-growth/public-growth-checklist.md)
- [docs/public-growth/seo-geo-ai-structure-evaluation.md](./docs/public-growth/seo-geo-ai-structure-evaluation.md)

## Proof и case studies

Proof pack здесь честный по умолчанию.
Если adopter не независимый или кейс sanitized, это явно помечено.

Смотри:
- [docs/proof-pack.md](./docs/proof-pack.md)
- [case-studies/README.md](./case-studies/README.md)
- [ADOPTERS.md](./ADOPTERS.md)

## Статус workflow JSON

Workflow JSON — это machine-readable planning/governance artifacts.
Это не execution engine.

```bash
python3 -m vcp_cli workflow plan --json
```

## Что пока остается experimental

- registry publication (`pip install vcp-cli`, `npx vcp`), если реально не выпущено;
- destructive apply modes;
- любые claims, что workflow JSON выполняет внешние действия;
- любые proof или SEO/GEO claims без публичного evidence.

## Ключевые документы

- [FULL_REPO_INTAKE.md](./FULL_REPO_INTAKE.md)
- [REPO_CAPABILITIES_INDEX.md](./REPO_CAPABILITIES_INDEX.md)
- [docs/two-track-model.md](./docs/two-track-model.md)
- [docs/adoption-tiers.md](./docs/adoption-tiers.md)
- [docs/distribution.md](./docs/distribution.md)
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/release-v0.7.1.md](./docs/release-v0.7.1.md)
