<!-- vcp-version: v0.6.7 -->

<!-- vcp-artifact: ARCHITECTURE_SOURCE_OF_TRUTH -->
<!-- vcp-version: v0.6.6 -->
<!-- methodology-version: v1.4 -->

# Architecture Source of Truth

Универсальный шаблон архитектурной справки проекта.

Этот документ не должен быть презентацией или marketing-summary. Это working engineering-control document: единый источник правды для разработки, безопасности, деплоя, rollback, передачи проекта другому инженеру и production readiness review.

## Fill levels

You do not need to fill the whole document on day one.

### MVP

Fill sections:
- project purpose
- active/deferred surfaces
- main flows
- key files
- env/secrets policy
- deploy path
- known risks

### Pre-production

Also fill:
- auth
- data model
- integrations
- rollback
- monitoring
- testing

### Production / client-facing

Fill all sections, including:
- security operations
- incident recovery
- third-party registry
- compliance
- accepted risks

## Architecture Map

Link to the compact map:

- `ARCHITECTURE_MAP.md`

Use the map for quick orientation.
Use this document for details, decisions, risks and operations.

## Backlog synchronization rule

If a backlog item has architecture impact `cross-layer` or `production-critical`, this document must be updated in the same task or a linked follow-up backlog item must be created.
If that is not possible, stop and ask the user.

## Как использовать

- Заполняйте только то, что реально существует в проекте.
- Если информации не хватает, помечайте это как `Unknown` или `To уточнить`.
- Не придумывайте архитектуру задним числом: документ должен описывать фактический проект.
- Обновляйте файл после крупных архитектурных изменений, инцидентов, новых интеграций и перед релизом.

---

## 1. Назначение документа

- Название проекта:
- Репозиторий:
- Владельцы документа:
- Дата создания:
- Последнее обновление:
- Статус: Draft / Active / Review / Archived
- Для чего нужен документ:
- Кто основная аудитория: founders / developers / security / DevOps / QA / product / compliance

## 2. Executive Summary

- Что делает проект:
- Для кого проект:
- Что считается core user flow:
- Какая текущая стадия: prototype / MVP / pre-production / production
- Главные архитектурные ограничения:
- Главные риски сейчас:
- Что блокирует production, если блокирует:

## 3. Product Scope / Boundaries

### In scope
- 
- 
- 

### Not in scope
- 
- 
- 

### Platforms
- Web:
- API / Backend:
- Mobile:
- Admin:
- Landing:
- Bot / AI-agent:

## 4. Архитектурные цели, NFR и SLO

### Архитектурные цели
- Управляемость изменений
- Безопасный deploy
- Предсказуемый rollback
- Наблюдаемость
- Минимизация ручного хаоса

### NFR
- Availability:
- Performance:
- Security:
- Scalability:
- Maintainability:
- Auditability:
- Cost efficiency:

### SLO
- p95 latency:
- Error budget:
- Availability target:
- Recovery target:
- Queue/job latency target:
- Payment confirmation target, если применимо:

## 5. C4 Architecture

### Context
- Пользователи:
- Внешние системы:
- Платежные сервисы:
- CRM / BI / Email / SMS / AI API:

### Container view
- `apps/web`:
- `apps/api`:
- `apps/mobile`:
- `packages/shared`:
- `infra`:
- External storage / DB / queues:

### Component view
- Главные модули:
- Auth:
- Payments:
- Notifications:
- AI layer:
- Data ingestion / ETL:

### Code map reference
- PROJECT_MAP.md:
- Entry points:
- Sensitive zones:

## 6. Runtime Topology / Environments

- Local:
- CI:
- Staging:
- Production:
- Multi-region / single-region:
- VPS / cloud / managed platform:
- Runtime types: Node / Python / PHP / serverless / workers / cron

### Environment notes
- Secrets source:
- Config source:
- Feature flags:
- Rate limiting:
- Firewall / WAF, если есть:

## 6A. Storage and Access Policy

- Где хранится документ:
- Кто имеет доступ:
- Public / private / sanitized version:
- Encryption required: yes / no
- Private docs storage:
- Не хранить в public webroot:
- Не индексировать через robots/sitemap:
- Какие поля нельзя публиковать: internal paths / IP / secrets / tokens / admin routes / private APIs

## 6B. Self-Protection / Internal Security

- Public exposure rules:
- Sensitive file denylist:
- Admin / internal endpoints:
- Scanner / browser / worker isolation:
- Outbound restrictions:
- Alerting:
- Logs retention:
- Public headers disclosure policy:

## 7. Stack / Dependencies

### Core stack
- Frontend:
- Backend:
- Database:
- Queue / broker:
- Infra:
- Observability:
- AI providers:

### Dependency rules
- Package manager:
- Lockfile policy:
- New dependency review process:
- License review process:
- Auto-update process:

## 8. Public / Internal Surface

### Public surface
- Public routes:
- Public APIs:
- Webhooks:
- Static assets:

### Internal surface
- Admin routes:
- Internal APIs:
- Background workers:
- Internal dashboards:
- Cron jobs:
