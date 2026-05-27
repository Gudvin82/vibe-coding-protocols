# Vibe Coding Protocols — русская версия

**Agent harness и операционный слой для AI-assisted разработки, а не просто коллекция prompt-ов.**

Этот репозиторий — markdown/toolkit-версия методологии `Vibe Coding Protocols` с сайта Анатолия Малышева.

Toolkit помогает фаундерам, solo builders и командам превратить AI-assisted coding в контролируемый delivery workflow: Product Brief, Memory Bank, AI IDE rules, Starter, Hardening, vibe-check, security operations и audit backlog.

Пакет репозитория: `v0.1.11`  
Веб-методология: `Vibe Coding Protocols v1.4`

Decision wizard: [START_HERE.md](./START_HERE.md)

## С чего начать

| У меня есть... | Куда идти | Что копировать первым | Что запустить |
|---|---|---|---|
| Только идея | Product Brief | `prompts/product-brief-prompt.md` | — |
| Новый AI-проект | Starter Protocol | `AGENTS.md` + `templates/PROJECT_MAP.md` | `bash scripts/vibe-check.sh --starter` |
| Уже есть AI-generated код | Hardening Protocol | `templates/AUDIT_BACKLOG.md` | `bash scripts/vibe-check.sh --hardening` |
| Публичный / production проект | Extended path | `SECURITY_OPERATIONS_BASELINE.md` + perimeter checklist | `bash scripts/vibe-check.sh --audit` |
| Хочу дать repo своему AI | AI entry prompt | `prompts/use-this-repo-prompt.md` | — |

## Старт за 2 минуты

### Новый проект

1. Скопируйте [AGENTS.md](./AGENTS.md) в свой repo.
2. Скопируйте [templates/PROJECT_MAP.md](./templates/PROJECT_MAP.md) как `PROJECT_MAP.md`.
3. Откройте [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md).
4. Вставьте Product Brief prompt в свою AI IDE.
5. Запустите:

```bash
bash scripts/vibe-check.sh --starter
```

### Уже существующий AI-generated проект

1. Скопируйте [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md).
2. Откройте [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md).
3. Запустите:

```bash
bash scripts/vibe-check.sh --hardening
```

### Review-first minimal setup

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
less init-minimal.sh
bash init-minimal.sh --starter
```

Fast track для пустых репозиториев. Выше — рекомендуемый review-first flow.

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh | bash -s -- --starter
```

Optional local guardrail:

```bash
bash scripts/install-hooks.sh --mode starter
```

## Кратко за 10 секунд

1. Start: превратите идею в Product Brief и первый безопасный vertical slice.
2. Build: используйте `AGENTS.md`, `PROJECT_MAP.md` и AI IDE rules, чтобы держать scope под контролем.
3. Harden: проверяйте AI-generated код перед merge / deploy / production.
4. Reuse: копируйте prompts, templates, checklists и examples в свой проект.

## Зачем это нужно

AI IDE быстро пишут код, но без operating layer проект часто разваливается на практике:
контекст живет в чате, архитектура не зафиксирована, зависимости появляются без review,
security вспоминают поздно, а готовность к merge/deploy никто не может оценить честно.

Toolkit добавляет поверх AI-assisted разработки:
- Product Brief до кода;
- Memory Bank files;
- Starter и Hardening маршруты;
- self-protection и perimeter checks;
- safe third-party intake;
- token-aware code discovery;
- validation и review gates.

## Agent Harness

Этот репозиторий можно использовать как agent harness для AI-assisted delivery.

Он объединяет:
- Memory Bank files;
- AI IDE rules;
- model routing;
- token-aware discovery;
- stop conditions;
- validation checks;
- security baselines;
- review loops;
- backlog и release handoff.

Смотрите:
- [docs/agent-harness.md](./docs/agent-harness.md)
- [docs/model-routing.md](./docs/model-routing.md)
- [commands/README.md](./commands/README.md)
- [docs/auth-session-security.md](./docs/auth-session-security.md)
- [checklists/auth-abuse-checklist.md](./checklists/auth-abuse-checklist.md)

## Commands

Переиспользуемые AI command patterns лежат в [commands/](./commands/README.md).
Это не shell-команды, а copyable инструкции для AI IDE.

## Core vs Extended

### Core path — для 80% пользователей

- Product Brief
- AGENTS.md
- PROJECT_MAP.md
- Starter Protocol
- Hardening Protocol
- AUDIT_BACKLOG.md
- vibe-check

### Extended path — для production / teams

- Architecture Source of Truth
- Security Operations Baseline
- Perimeter Security Checklist
- External Exposure Checklist
- Third-Party Registry
- Safe Update Workflow
- Secret Rotation and Storage
- Independent Diff Review

## Какие security layers покрываются

1. **Внутренняя безопасность проекта**
   Secrets, env files, logs, backups, admin routes, workers, browser automation и private docs.

2. **Perimeter и внешний exposure**
   Public endpoints, closed ports, admin allowlists, WAF/CDN, rate limits, bot abuse,
   security headers и recurring exposure checks.

3. **Supply-chain и integrations**
   Внешние APIs, packages, repositories, templates, GitHub Actions, Docker images и update workflows.

4. **Безопасность архитектуры и документации**
   `PROJECT_MAP.md`, `AGENTS.md`, `Architecture Source of Truth`, private / sanitized / encrypted storage policy.

5. **Token-aware AI workflow**
   Memory Bank, read order, scoped code discovery и independent diff review.

## Artifact map

| Artifact | Purpose | Required? | Use when |
|---|---|---|---|
| Product Brief | Проясняет, что строить до кода | Core | Любой новый проект |
| AGENTS.md | Правила для AI agents | Core | Любой AI IDE workflow |
| PROJECT_MAP.md | Карта файлов и кодового контекста | Core | Любой repo с кодом |
| AUDIT_BACKLOG.md | Findings и follow-up задачи | Core for hardening | Уже существующий AI-generated код |
| ARCHITECTURE_SOURCE_OF_TRUTH.md | Архитектурная справка | Extended | Production, команда, handoff |
| SECURITY_OPERATIONS_BASELINE.md | Recurring security checks | Extended | Public/production проекты |
| THIRD_PARTY_REGISTRY.md | Внешние packages/APIs/repos | Extended | Любые integrations |
| vibe-check.sh | Lightweight structural check | Optional but recommended | Local/CI sanity check |

## Дайте этот repo своему AI

Используйте [prompts/use-this-repo-prompt.md](./prompts/use-this-repo-prompt.md),
если хотите, чтобы AI сначала выбрал маршрут, нужные файлы и риски,
а уже потом предлагал код.

## Вставьте это в свою AI IDE

```text
Study this repository:
https://github.com/Gudvin82/vibe-coding-protocols

Do not write code yet.

First tell me:
1. Which route fits my project: Starter, Hardening, Templates, Architecture Source of Truth, or Security Operations?
2. Which files I should copy first.
3. Which questions are missing.
4. Which risks I may be underestimating.
5. What is the smallest safe next step?

If you cannot open GitHub links, ask me to paste README.md and prompts/use-this-repo-prompt.md.
```

Полный файл:
- [prompts/use-this-repo-prompt.md](./prompts/use-this-repo-prompt.md)

## Почему AI IDE files лежат в root?

Root files специально сделаны как copy-ready entrypoints для AI IDE:

- `AGENTS.md`
- `CLAUDE.md`
- `.cursorrules`
- `.windsurfrules`
- `.github/copilot-instructions.md`

Это не “мусор в корне”, а готовые файлы, которые можно копировать
в свой repo или использовать как примеры правил для AI-assisted delivery.

## Чего не стоит делать вначале

- Не вставляйте весь репозиторий целиком в AI-чат.
- Не запускайте installer без просмотра скрипта.
- Не воспринимайте `vibe-check` как security scanner.
- Не публикуйте реальную архитектурную справку, secrets или internal endpoints.
- Не позволяйте AI переписывать много слоев без approval.

## Что копировать первым

- Новый проект:
  [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md) +
  [protocols/ai-project-starter-protocol.md](./protocols/ai-project-starter-protocol.md)
- Уже существующий AI-generated проект:
  [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md) +
  [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md)
- Настройка AI IDE:
  [AGENTS.md](./AGENTS.md), [CLAUDE.md](./CLAUDE.md), [.cursorrules](./.cursorrules),
  [.windsurfrules](./.windsurfrules), [.github/copilot-instructions.md](./.github/copilot-instructions.md)
- Perimeter / security operations:
  [checklists/perimeter-security-checklist.md](./checklists/perimeter-security-checklist.md) +
  [templates/SECURITY_OPERATIONS_BASELINE.md](./templates/SECURITY_OPERATIONS_BASELINE.md)

## CI/CD integration

В repo есть lightweight GitHub Action для `vibe-check`.

Он запускается на:
- `push`
- `pull_request`

Он проверяет:
- структуру toolkit;
- локальные markdown links;
- placeholder / secrets-like examples;
- сигналы starter / hardening / audit mode.

Это не замена тестам, сканерам, pentest или human review.

Смотрите:
- [.github/workflows/vibe-check.yml](./.github/workflows/vibe-check.yml)
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)

Более глубокие engineering links:
- [START_HERE.md](./START_HERE.md)
- [docs/hardening-thresholds.md](./docs/hardening-thresholds.md)
- [docs/testing-cookbook.md](./docs/testing-cookbook.md)
- [docs/ai-specific-threat-model.md](./docs/ai-specific-threat-model.md)
- [docs/scanner-integration.md](./docs/scanner-integration.md)
- [docs/agent-harness.md](./docs/agent-harness.md)
- [docs/model-routing.md](./docs/model-routing.md)
- [commands/README.md](./commands/README.md)
- [docs/auth-session-security.md](./docs/auth-session-security.md)
- [checklists/auth-abuse-checklist.md](./checklists/auth-abuse-checklist.md)

## Mermaid и fallback previews

Mermaid-диаграммы остаются в основном [README.md](./README.md).

Fallback previews:
- ![Workflow preview](./assets/workflow-mermaid-preview.png)
- ![Stop conditions flow preview](./assets/stop-conditions-flow-preview.png)

## Что такое perimeter / self-protection / safe integration

- **Self-protection** — чтобы `.env`, `.git`, backups, logs, source maps, admin/internal docs и debug routes не торчали наружу.
- **Perimeter** — чтобы были понятны public endpoints, subdomains, closed ports, WAF/CDN, rate limits, bot abuse controls и recurring exposure checks.
- **Safe integration** — чтобы внешние repo, packages, APIs, actions и images подключались только через review, pinning, quarantine, scanners и rollback plan.

## Automated Vibe Check

`vibe-check` — это lightweight-проверка структуры и базовых workflow-сигналов для проектов, которые используют toolkit.

Она не заменяет тесты, сканеры, human review и полный Hardening Protocol, но помогает рано заметить отсутствующие memory files,
audit-файлы и явные workflow gaps.

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --json
bash scripts/init-minimal.sh --dry-run
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

Смотрите:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)
- [scripts/init-minimal.sh](./scripts/init-minimal.sh)
- [scripts/install-hooks.sh](./scripts/install-hooks.sh)

## Token-aware discovery

Для больших проектов сначала собирайте compact evidence map, а уже потом переходите к реализации.

Смотрите:
- [docs/token-aware-code-discovery.md](./docs/token-aware-code-discovery.md)
- [prompts/modules/token-aware-discovery.md](./prompts/modules/token-aware-discovery.md)

## Бейджи для вашего проекта

Если вы используете toolkit, можете добавить бейдж в README своего проекта:

[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Hardened with VCP](https://img.shields.io/badge/Hardened%20with-VCP-green)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Uses VCP Templates](https://img.shields.io/badge/Uses-VCP%20Templates-purple)](https://github.com/Gudvin82/vibe-coding-protocols)

Другие варианты:
- [docs/badges.md](./docs/badges.md)

## Для кого это

### Для founders

Начните с Product Brief + Starter Protocol, чтобы превратить идею
в первый safe slice до того, как недели уйдут на хаотичный AI-generated код.

### Для solo builders

Скопируйте `AGENTS.md` + `PROJECT_MAP.md` и запустите `vibe-check`,
чтобы держать Claude Code, Codex, Cursor или Windsurf в рамках scope.

### Для product teams

Используйте Core vs Extended как lightweight Definition of Ready / Definition of Done
для AI-generated изменений.

### Для agencies и client work

Используйте Architecture Source of Truth + AUDIT_BACKLOG + Security Operations Baseline,
чтобы оставлять после себя понятную project memory и safer handoff materials.

## Versioning

У проекта есть две связанные линии версий:

- **Версия пакета репозитория** (`v0.1.x`) — отражает упаковку GitHub toolkit: README, scripts, examples, CI, installer, docs и release polish.
- **Версия веб-методологии** (`v1.4`) — отражает публичные страницы на `anmalishev.ru`.

Текущее состояние:
- Пакет репозитория: `v0.1.6`
- Веб-методология: `Vibe Coding Protocols v1.4`

Будущая версия репозитория `v1.0.0` возможна только после внешней обратной связи,
реальных сигналов adoption и стабильного интерфейса toolkit.

## Автор

Методологию собрал и поддерживает **Анатолий Малышев**.

Сайт: [https://anmalishev.ru/](https://anmalishev.ru/)

Анатолий Малышев занимается практическими AI-решениями для бизнеса:
AI-агентами, CRM/1С/BI-интеграциями, сквозной аналитикой,
Telegram-ботами, mini apps и инженерной доводкой AI-generated проектов.

Этот toolkit вырос из практической работы с проектами, которые создаются через AI/IDE:
от формулировки идеи и Product Brief до архитектурной справки, аудита сгенерированного кода,
security / supply-chain проверок и подготовки проекта к merge / deploy.

География: Санкт-Петербург, Москва и РФ.
