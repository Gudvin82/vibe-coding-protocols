# Starter → Hardening Bridge

## Какие артефакты переходят из Starter в Hardening

- `Product Brief` → проверяется на соответствие реализации
- `README.md` → используется как onboarding context
- `AGENTS.md` → становится правилами для аудита и фиксов
- `PROJECT_MAP.md` → обновляется после code discovery
- `ARCHITECTURE.md` / `Architecture Source of Truth` → проверяется и расширяется
- `SECURITY.md` → уточняется после security pass
- `docs/PROMPTS.md` → помогает понять, какими AI-инструкциями создавался проект
- `AUDIT_BACKLOG.md` → наполняется findings из Hardening

## Что обновлять

Перед Hardening проверьте, что актуальны:
- routes / endpoints;
- data model;
- auth / roles;
- integrations;
- deploy path;
- workers / queues;
- external APIs;
- payment flow;
- security model;
- database migrations;
- storage / files;
- public / internal boundaries.

## Что проверить

- есть ли минимальный Memory Bank;
- не перепутаны ли active / deferred surfaces;
- есть ли checkpoint перед risky AI changes;
- нужен ли Light Hardening вместо Full.

## Если артефактов нет

Если `PROJECT_MAP.md` и `ARCHITECTURE.md` отсутствуют:
1. сначала соберите минимальный `PROJECT_MAP.md`;
2. затем создайте минимальный `ARCHITECTURE.md` / `Architecture Source of Truth`;
3. только потом идите в полный audit.
