# Vibe Coding Protocols

[English version](./README.md)

Build with AI. Ship with control.

Vibe Coding Protocols помогает строить продукты через ИИ — от идеи до production — без потери контроля: выбирает маршрут, глубину ТЗ, хранит память проекта, проверяет AI-изменения, ведет backlog, запускает review gates и готовит релиз.

Repository package: `v0.6.1`

Web methodology: `Vibe Coding Protocols v1.4`

## Быстрый старт

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

## Два режима использования VCP

### Сборка с нуля

Идея -> глубина ТЗ -> PRD / feature spec -> задачи -> backlog -> память архитектуры -> реализация -> review -> релиз.

### Стабилизация существующего проекта

Intake -> diagnostics -> hardening -> review gates -> backlog -> release readiness -> operations feedback.

## Три флагманских workflow

1. [Собрать AI-assisted продукт от идеи](./docs/flagship-workflows.md)
2. [Укрепить AI-сгенерированный MVP](./docs/flagship-workflows.md)
3. [Проверять ongoing AI-driven changes](./docs/flagship-workflows.md)

## Где смотреть дальше

Если нужны правила именно для этого репозитория, используй root `AGENTS.md`.
Если нужен переиспользуемый шаблон для проекта, используй [templates/AGENTS.md](./templates/AGENTS.md).

- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [docs/product-delivery-lifecycle.md](./docs/product-delivery-lifecycle.md)
- [docs/flagship-workflows.md](./docs/flagship-workflows.md)
- [docs/review-diff.md](./docs/review-diff.md)
- [docs/score-badge.md](./docs/score-badge.md)
- [docs/github-action.md](./docs/github-action.md)
- [docs/integrations/spec-kit-bridge.md](./docs/integrations/spec-kit-bridge.md)
- [docs/platforms/README.md](./docs/platforms/README.md)
- [docs/faq.md](./docs/faq.md)
- [docs/comparison.md](./docs/comparison.md)
- [docs/anti-patterns.md](./docs/anti-patterns.md)

## Когда VCP избыточен

- игрушечный проект;
- одноразовый скрипт;
- чисто косметическая правка текста;
- нет production или public use;
- чистое исследование;
- пользователь пока не хочет процесс.
