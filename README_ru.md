# Vibe Coding Protocols — русская версия

Этот репозиторий — markdown/toolkit-версия методологии `Vibe Coding Protocols` с сайта Анатолия Малышева.

## Что это

Практический набор протоколов, prompts, шаблонов и чек-листов для более безопасной AI-assisted / vibe coding разработки.

Репозиторий помогает:
- начать AI-проект без хаоса;
- собрать Product Brief до генерации кода;
- определить active / deferred surfaces;
- завести `AGENTS.md`, `PROJECT_MAP.md` и `Architecture Source of Truth`;
- провести hardening AI-generated проекта перед merge / deploy / production;
- вести `AUDIT_BACKLOG.md` и безопаснее работать с AI IDE.

## Версии

- Версия репозитория: `v0.1.1`
- Версия web-методологии: `Vibe Coding Protocols v1.4`

Версии репозитория (`v0.x`) описывают упаковку GitHub toolkit.
Версии методологии (`v1.x`) относятся к web-протоколам на
`anmalishev.ru`.

## Кратко за 10 секунд

1. Start: превратите идею в Product Brief и первый безопасный vertical slice.
2. Build: используйте `AGENTS.md`, `PROJECT_MAP.md` и AI IDE rules, чтобы держать scope под контролем.
3. Harden: проверяйте AI-generated код перед merge / deploy / production.
4. Reuse: копируйте prompts, templates, checklists и examples в свой проект.

## Быстрый старт

### Если у вас только идея

1. Откройте [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md)
2. Соберите Product Brief
3. Перейдите к [protocols/ai-project-starter-protocol.md](./protocols/ai-project-starter-protocol.md)

### Если код уже существует

1. Откройте [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md)
2. Начните с Light Hardening
3. Создайте или обновите [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md)

### Если хотите дать repo своему AI

Используйте:
- [CLAUDE.md](./CLAUDE.md)
- [AGENTS.md](./AGENTS.md)
- [.cursorrules](./.cursorrules)
- [.windsurfrules](./.windsurfrules)
- [.github/copilot-instructions.md](./.github/copilot-instructions.md)

## Основные ссылки

- Website: [https://anmalishev.ru/](https://anmalishev.ru/)
- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening:
  [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)

## Примеры

Смотрите synthetic walkthroughs:
- [examples/todo-app-vibe/](./examples/todo-app-vibe/)
- [examples/telegram-bot-vibe/](./examples/telegram-bot-vibe/)
- [examples/landing-page-vibe/](./examples/landing-page-vibe/)
- [examples/saas-backend-vibe/](./examples/saas-backend-vibe/)

Все примеры synthetic / sanitized. Это не реальные клиентские проекты.

## Полезные материалы

- [ANTI_PATTERNS.md](./ANTI_PATTERNS.md)
- [docs/multi-agent-workflows.md](./docs/multi-agent-workflows.md)
- [docs/vibe-metrics.md](./docs/vibe-metrics.md)
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [docs/pre-commit-hooks.md](./docs/pre-commit-hooks.md)
- [docs/community-issues.md](./docs/community-issues.md)
- [ROADMAP.md](./ROADMAP.md)

## Автор

Автор: Анатолий Малышев

Анатолий Малышев — специалист по AI-решениям для бизнеса, AI-агентам, CRM/1С/BI-интеграциям, сквозной аналитике, Telegram-ботам и мини-приложениям.

География: Санкт-Петербург, Москва и РФ.
