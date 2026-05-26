# Vibe Coding Protocols — русская версия

Этот репозиторий — markdown/toolkit-версия методологии `Vibe Coding Protocols` с сайта Анатолия Малышева.

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

## Какие проблемы это решает

Частые проблемы AI-generated проекта:
- AI начинает писать код до ясного product scope;
- изменения расползаются по слишком многим файлам;
- пакеты и внешние API подключаются без проверки;
- архитектура существует только в истории чата;
- security checks происходят слишком поздно;
- secrets, logs или internal docs становятся публичными;
- AI сжигает токены, читая весь repo подряд;
- непонятно, готов ли проект к merge / deploy.

Этот toolkit превращает эти риски в prompts, templates, checklists и lightweight automation.

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

## Какой маршрут выбрать

| Ситуация | С чего начать |
|---|---|
| Есть только идея | [Product Brief prompt](./prompts/product-brief-prompt.md) |
| Хочу начать новый AI-проект | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Уже есть AI-generated код | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Нужны переиспользуемые файлы | [Templates](./templates/README.md) |
| Нужна проектная документация | [Architecture Source of Truth](./templates/ARCHITECTURE_SOURCE_OF_TRUTH.md) |
| Нужна быстрая структурная проверка | [Automated Vibe Check](./docs/automated-vibe-check.md) |
| Нужны примеры | [examples/README.md](./examples/README.md) |

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
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

Смотрите:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)

## Бейджи для вашего проекта

Если вы используете toolkit, можете добавить бейдж в README своего проекта:

[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Hardened with VCP](https://img.shields.io/badge/Hardened%20with-VCP-green)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Uses VCP Templates](https://img.shields.io/badge/Uses-VCP%20Templates-purple)](https://github.com/Gudvin82/vibe-coding-protocols)

```markdown
[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)
```

```markdown
[![Hardened with VCP](https://img.shields.io/badge/Hardened%20with-VCP-green)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Uses VCP Templates](https://img.shields.io/badge/Uses-VCP%20Templates-purple)](https://github.com/Gudvin82/vibe-coding-protocols)
```

Другие варианты:
- [docs/badges.md](./docs/badges.md)

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
