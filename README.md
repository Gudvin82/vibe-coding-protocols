# Vibe Coding Protocols

Практические протоколы и markdown-шаблоны для более безопасной AI-assisted / vibe coding разработки.

## Что это такое

Vibe Coding Protocols — это практическая методология для запуска, аудита и hardening AI-generated проектов.

Она помогает:
- начать AI-проект без хаоса;
- собрать Product Brief / ТЗ до генерации кода;
- выбрать стек и стартовый маршрут;
- определить active / deferred surfaces;
- завести `AGENTS.md`, `PROJECT_MAP.md` и `Architecture Source of Truth`;
- проверить AI-generated код перед merge / deploy;
- пройти security, supply-chain, self-protection и database/load readiness проверки;
- вести `AUDIT_BACKLOG.md`;
- безопаснее использовать Claude Code / Codex / Cursor / Windsurf и другие AI IDE.

## Автор

Создано Анатолием Малышевым.

Website: [https://anmalishev.ru/](https://anmalishev.ru/)

Анатолий Малышев — специалист по AI-решениям для бизнеса: AI-агенты, CRM/1С/BI-интеграции, сквозная аналитика, Telegram-боты и мини-приложения.

География: Санкт-Петербург, Москва и РФ.

## Официальная web-версия

- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth: [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)

Этот репозиторий — markdown/toolkit-версия публичной методологии с сайта `anmalishev.ru`.

## Quick Start

### Если у вас только идея

1. Откройте [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md)
2. Соберите Product Brief
3. Перейдите к [protocols/ai-project-starter-protocol.md](./protocols/ai-project-starter-protocol.md)

### Если у вас уже есть AI-generated код

1. Откройте [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md)
2. Начните с Light Hardening
3. Создайте или обновите [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md)

### Если вы хотите дать этот repo своему AI

Используйте:
- [prompts/master-prompt-short.md](./prompts/master-prompt-short.md)
- [prompts/master-prompt-full.md](./prompts/master-prompt-full.md)

Если AI не умеет читать ссылки, просто вставьте нужные markdown-файлы из этого репозитория вручную.

## Структура репозитория

- [`protocols/`](./protocols/) — markdown-версии хаба, Starter, Hardening и bridge-файлы
- [`prompts/`](./prompts/) — короткие и длинные prompt-блоки по стадиям
- [`templates/`](./templates/) — Artifact Pack и рабочие project templates
- [`agents/`](./agents/) — примеры адаптации под Claude Code / Codex / Cursor / Windsurf
- [`examples/`](./examples/) — короткие условные сценарии применения
- [`checklists/`](./checklists/) — быстрые operational checklists
- [`docs/`](./docs/) — versioning, attribution, public vs private docs и maintenance notes

## Для кого это

- solo founders;
- indie hackers;
- vibe coders;
- разработчики, использующие Claude Code / Codex / Cursor / Windsurf;
- CTO и команды, внедряющие AI-assisted development;
- люди, у которых уже есть AI-generated MVP и нужен hardening.

## Что это не заменяет

- не гарантия безопасности;
- не замена human review;
- не замена pentest;
- не замена юридической консультации;
- не магический prompt, который автоматически делает любой проект production-ready.

## License

Репозиторий в первом публичном релизе распространяется под `CC BY 4.0`.

Это хороший базовый вариант для методологии, markdown-протоколов и шаблонов: ими удобно пользоваться, адаптировать и форкать при обязательной attribution-связке с автором.

Если вы адаптируете этот toolkit, сохраняйте attribution на автора и ссылку на исходный репозиторий или сайт.

Если в репозитории позже появятся standalone executable scripts, для них может использоваться отдельная license.

Подробности: [LICENSE](./LICENSE)

## Disclaimer

Перед использованием обязательно прочитайте [DISCLAIMER.md](./DISCLAIMER.md).
