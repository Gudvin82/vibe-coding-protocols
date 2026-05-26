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

## Automated Vibe Check

`vibe-check` — это lightweight-проверка структуры и базовых
workflow-сигналов для проектов, которые используют toolkit.

Она не заменяет тесты, сканеры, human review и полный Hardening
Protocol, но помогает рано заметить отсутствующие memory files,
audit-файлы и явные workflow gaps.

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
```

Пример вывода:

```text
PASS: README.md exists
PASS: AGENTS.md or CLAUDE.md exists
PASS: .gitignore exists
WARN: AUDIT_BACKLOG.md is missing for hardening mode
WARN: public root AGENTS.md exists; make sure public docs are sanitized
SUMMARY: 3 pass, 2 warn, 0 fail
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

Смотрите:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)

## Бейджи для вашего проекта

Если вы используете toolkit, можете добавить бейдж в README своего
проекта:

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

## Полезные материалы

- [ANTI_PATTERNS.md](./ANTI_PATTERNS.md)
- [docs/multi-agent-workflows.md](./docs/multi-agent-workflows.md)
- [docs/vibe-metrics.md](./docs/vibe-metrics.md)
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [docs/pre-commit-hooks.md](./docs/pre-commit-hooks.md)
- [docs/community-issues.md](./docs/community-issues.md)
- [ROADMAP.md](./ROADMAP.md)

## Автор

Методологию собрал и поддерживает **Анатолий Малышев**.

Сайт: [https://anmalishev.ru/](https://anmalishev.ru/)

Анатолий Малышев занимается практическими AI-решениями для бизнеса:
AI-агентами, CRM/1С/BI-интеграциями, сквозной аналитикой,
Telegram-ботами, mini apps и инженерной доводкой AI-generated
проектов.

Этот toolkit вырос из практической работы с проектами, которые
создаются через AI/IDE: от формулировки идеи и Product Brief до
архитектурной справки, аудита сгенерированного кода,
security/supply-chain проверок и подготовки проекта к merge/deploy.

География: Санкт-Петербург, Москва и РФ.
