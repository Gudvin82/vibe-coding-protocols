# AI Project Starter Protocol

Markdown-версия `AI Project Starter Protocol` для новых AI-проектов.

## Цель

Не дать AI сразу писать хаотичный код. Сначала — Product Brief, стек, active/deferred surfaces, Memory Bank, operational baseline и первый safe vertical slice.

## Шаг -1. Product Brief / ТЗ

Сначала зафиксируйте:
- что это за продукт;
- для кого он;
- какой первый measurable outcome;
- какие поверхности активны сейчас;
- какие поверхности явно deferred.

Используйте: [../prompts/product-brief-prompt.md](../prompts/product-brief-prompt.md)

## Prompt 0. Technical intake

До кода AI должен выяснить:
- стек;
- deployment target;
- runtime boundaries;
- active / deferred surfaces;
- integrations;
- auth / payment / PДн / legal-risk зоны;
- test / build / validation baseline.

См. [../prompts/starter-prompts.md](../prompts/starter-prompts.md)

## Stack Decision Framework

При выборе стека AI должен ответить:
- какая primary database нужна;
- какие таблицы / сущности вырастут первыми;
- нужна ли migration strategy;
- нужны ли background jobs сейчас или позже;
- нужен ли cache сейчас или позже;
- где likely bottleneck;
- что intentionally deferred.

Не добавляйте сложность без причины. Но если выбранный путь создает очевидный тупик при росте, AI должен это сказать.

## Active / Deferred Surfaces

Явно разделите:
- active now;
- deferred until later.

Примеры surfaces:
- web frontend;
- backend/API;
- database;
- bot / AI-agent;
- mobile / mini app;
- payments;
- admin;
- workers / queues.

## Operational baseline

До production стоит решить:
- где хранится Product Brief / ARCHITECTURE / PROJECT_MAP / AGENTS / SECURITY;
- какие документы могут жить в repo, а какие только private;
- где будут secrets;
- кто имеет доступ к secrets;
- нужны ли workers / scanners / browser automation;
- нужны ли outbound restrictions;
- где будут logs / alerts;
- нужен ли staging.

## Architecture docs storage policy

Architecture Source of Truth полезен, но это чувствительный документ.

Рекомендации:
- не держать полную архитектурную справку в public webroot;
- хранить local / private / sanitized / encrypted;
- ограничивать доступ по ролям;
- при публичной документации выпускать sanitized version без secrets, internal paths, IP, admin routes и private APIs.

## Safe third-party intake

Перед подключением внешнего repo / template / package / API:
- проверьте origin;
- проверьте license;
- проверьте активность проекта;
- проверьте install scripts / postinstall / prepare;
- проверьте workflows;
- не давайте production secrets;
- сначала запускайте в sandbox / staging;
- зафиксируйте version / commit / risks.

## Database / Load readiness

Scalability-ready не значит enterprise.

Минимум на старте:
- осознанно выбрать primary database;
- определить ключевые сущности;
- не смешивать доменные данные и временный мусор без причины;
- предусмотреть migrations;
- добавить индексы под ожидаемые query patterns;
- не делать тяжелые synchronous operations без причины;
- продумать rate limits, retries и idempotency, если есть API / payment / webhooks.

## Memory Bank

Минимальный Memory Bank:
- `README.md`
- `AGENTS.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE.md` или `Architecture Source of Truth`
- `SECURITY.md`
- `AUDIT_BACKLOG.md`
- `docs/PROMPTS.md`

## AGENTS.md

`AGENTS.md` должен задавать:
- role;
- stop conditions;
- approval gates;
- code discovery first;
- small / atomic diffs;
- reporting after changes;
- no destructive commands without approval.

См. шаблон: [../templates/AGENTS.md](../templates/AGENTS.md)

Для Claude Code проектов отдельно проверьте `.claude/settings.json` и tool permissions, если файл существует. Доступ к инструментам — это часть operational baseline.

## Stop conditions

Stop and ask for approval when:
- change touches more than 10 files;
- change touches more than 2 layers at once;
- change adds auth / payments / admin / worker / external API;
- change requires new dependency;
- change changes database schema;
- change rewrites architecture instead of making a small vertical slice;
- tests/build are red and the fix is not obvious.

## AI cost awareness

Не тратьте контекст впустую:
- не читайте весь repo без причины;
- начинайте с `PROJECT_MAP.md`;
- не запускайте LLM/API loops без лимитов;
- фиксируйте expensive loops в `AUDIT_BACKLOG.md` или `docs/PROMPTS.md`.

## Prompt versioning

Если проект ведется через AI — сохраняйте адаптированные prompts в `docs/PROMPTS.md`.

См. template: [../templates/PROMPTS.md](../templates/PROMPTS.md)

## AI-generated test strategy

AI не должен писать тесты на всё подряд.

Приоритет:
- critical path;
- regressions;
- existing test framework;
- mocked external APIs / LLM;
- no new test framework without approval;
- clearly deferred tests list.

## First safe iteration

Перед первым vertical slice AI должен:
- показать changed-files plan;
- сказать, какие запросы к БД появятся;
- указать, есть ли риск N+1;
- сказать, sync это будет или async;
- отметить внешний API / LLM в critical path;
- предложить checkpoint, если изменение risky.

После реализации AI должен вывести:
- какие таблицы / миграции появились;
- какие query patterns добавлены;
- какие индексы добавлены или отложены;
- какие bottlenecks ожидаются;
- что добавить в scalability backlog.

## Starter → Hardening

После первой safe iteration не начинайте бесконечно докидывать фичи.

Сначала переходите в Hardening:
- reuse Product Brief;
- update PROJECT_MAP;
- review ARCHITECTURE;
- expand SECURITY baseline;
- populate AUDIT_BACKLOG;
- run Light Hardening if this is still an early slice.

См. bridge: [starter-to-hardening-bridge.md](./starter-to-hardening-bridge.md)
