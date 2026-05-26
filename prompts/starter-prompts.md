# Starter Prompts

## Prompt -1 — Product Brief

Use [product-brief-prompt.md](./product-brief-prompt.md).

## Prompt 0 — Technical intake

Проведи technical intake перед генерацией кода.

Выясни:
- стек;
- deployment target;
- active / deferred surfaces;
- integrations;
- auth / payment / PДн / legal-risk зоны;
- build/test/validation baseline;
- operational baseline;
- database/load risks.

Не пиши код до подтверждения плана.

## Prompt 1 — Stack and boundaries

Выбери стек и границы проекта.

Отдельно выведи:
- primary database;
- expected growing tables/entities;
- migration strategy;
- index strategy;
- background jobs needed now/later;
- caching needed now/later;
- rate limits;
- external API quota risks;
- idempotency needs;
- first likely bottleneck;
- what is intentionally deferred.

## Prompt 2 — Active / Deferred surfaces

Определи active / deferred surfaces проекта.

Не активируй deferred surfaces без approval.

## Prompt 3 — Memory Bank and docs

Создай или обнови:
- `README.md`
- `AGENTS.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE.md` или `Architecture Source of Truth`
- `SECURITY.md`
- `docs/PROMPTS.md`

Отдельно определи:
- какие документы можно хранить в repo;
- какие должны быть private;
- какие нельзя публиковать в webroot;
- нужна ли encrypted/private storage policy.

## Prompt 4 — Safe third-party intake

Если предлагаешь внешний repo / template / package / API:
- сначала проведи safe third-party intake;
- не подключай и не запускай ничего до approval;
- зафиксируй origin, version/commit, license и risks.

## Prompt 5 — Operational baseline

Собери минимальный operational baseline:
- secrets policy;
- alerts/logs plan;
- worker/scanner policy;
- outbound restrictions;
- staging need;
- deployment path.

## Prompt 6 — Scalability-ready first path

Оцени, что может стать bottleneck уже на первом росте:
- data model;
- sync vs async operations;
- external API / LLM in critical path;
- rate limits;
- idempotency;
- migrations.

## Prompt 7 — First safe iteration

Перед изменениями:
- покажи changed files plan;
- если изменения рискованные — предложи checkpoint commit;
- не делай commit без approval;
- скажи, какие DB queries появятся;
- скажи, нужны ли индексы уже сейчас;
- скажи, есть ли риск N+1;
- укажи, sync это или async;
- укажи внешний API / LLM в critical path.

Если пишешь тесты:
- фокусируйся на critical path и regressions;
- не добавляй новый test framework без approval.

После выполнения:
- покажи `git status`;
- скажи, как откатиться;
- выведи self-review;
- перечисли, какие таблицы / миграции / индексы появились;
- что добавить в scalability backlog;
- что можно оставить простым сейчас;
- что нужно сделать перед production.
