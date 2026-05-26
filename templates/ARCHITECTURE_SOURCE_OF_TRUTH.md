# Architecture Source of Truth

Универсальный шаблон архитектурной справки проекта.

Этот документ не должен быть презентацией или marketing-summary. Это working engineering-control document: единый источник правды для разработки, безопасности, деплоя, rollback, передачи проекта другому инженеру и production readiness review.

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

### Sensitive operations
- Payments:
- User data changes:
- Deletion flows:
- AI tool calls:
- Export / reporting:

## 9. Third-Party / Integrations Registry

| Integration | Origin | Owner | Purpose | Direction | Auth | Data touched | Version / commit | License | Scan date | Risk level | Update policy | Rollback |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | inbound / outbound |  |  |  |  |  | low / medium / high |  |  |

### Notes
- Unknown integrations:
- Deprecated integrations:
- Sandbox / test integrations:

## 9A. Safe Update Policy

- Quarantine before integration:
- Required scans:
- Staging required:
- PR only:
- Approval required from:
- Rollback point:
- Changelog / diff summary:
- Signature / checksum verification, если есть:

## 10. Data Contracts / API Contracts

### Public API contracts
- Endpoint:
- Method:
- Request schema:
- Response schema:
- Auth required:
- Versioning strategy:

### Internal contracts
- Worker payloads:
- Queue messages:
- Webhook contracts:
- External provider contracts:

### Validation rules
- Schema validation:
- Backward compatibility policy:
- Breaking change policy:

## 11. Freshness / Degradation Policy

- Какие данные должны быть real-time:
- Какие данные допустимо кешировать:
- Что считается stale-but-acceptable:
- Что делать при partial outage:
- Что отключать первым при деградации:
- Что можно перевести в read-only:

## 12. Caching / Coalescing Strategy

- HTTP caching:
- Application caching:
- DB query caching:
- CDN caching:
- Cache invalidation strategy:
- Stampede protection / request coalescing:
- Sensitive data caching restrictions:

## 13. Security Model / Threat Model

### Security model
- Auth method:
- Session / token strategy:
- Roles / permissions:
- Rate limiting:
- Webhook verification:
- Secrets management:
- Security headers:
- Scanner coverage:

### Threat model
- Prompt injection:
- Data exfiltration:
- IDOR / access control:
- SSRF / RCE / path traversal:
- Supply-chain risk:
- CI/CD secrets:
- Payment abuse:
- Insider / misconfiguration risk:

### Mitigations
- 
- 
- 

## 14. Privacy / Data Governance

- Какие ПДн собираются:
- Где они хранятся:
- Кто имеет доступ:
- Log redaction:
- Retention policy:
- Deletion / export process:
- Third-party processors:
- Cross-border transfer:
- AI prompt / analytics / tracker exposure risks:

## 15. Domain-Specific Safety Boundary

- Что в домене проекта считается unsafe action:
- Какие действия требуют human approval:
- Какие операции нельзя автоматизировать без review:
- Какие ошибки наиболее дорогие для бизнеса:
- Как выглядит emergency stop:

## 16. Data / Domain Model

### Core entities
| Entity | Purpose | Key fields | Sensitive fields | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

### Domain notes
- Source of truth per entity:
- Derived data:
- Eventual consistency zones:
- Deletion / archival model:

## 17. Data Layer / DB / Migrations

- Main database:
- Read replicas:
- Search index:
- Object storage:
- Migration tool:
- Zero-downtime migration policy:
- Expand / contract notes:
- Destructive migration policy:
- Seed / fixture policy:
- High-growth tables:
- Index policy:
- Constraint policy:
- Retention / archival policy:
- Backup / restore dependency:

## 17A. Background Jobs / Queue Strategy

- Worker model:
- Retry:
- Backoff:
- Idempotency:
- Dead-letter handling:
- Scheduling:
- Monitoring:
- Who can run jobs manually:

## 17B. Load / Critical Flows

- Critical user flows:
- Hot endpoints:
- Sync vs async operations:
- External API dependency:
- LLM / API cost risk:
- Rate limits:
- Timeout / retry / backoff:
- Degradation mode:

## 17C. Scalability Boundaries

- What is simple now:
- What is intentionally deferred:
- First likely bottleneck:
- Scaling path:
- What would require refactor:
- What must not be hardcoded:

## 18. Backup / Restore / DR

- Backup coverage:
- Frequency:
- Storage location:
- Encryption:
- Restore test cadence:
- RPO:
- RTO:
- Disaster recovery plan:
- Who approves restore:

## 19. Observability

- Logging:
- Metrics:
- Tracing:
- Error tracking:
- Healthchecks:
- Synthetic checks:
- Business KPI alerts:
- Security alerts:
- Payment alerts:
- AI cost alerts:

## 20. Performance / Capacity / Budget

- Current expected load:
- Peak assumptions:
- CPU / memory constraints:
- DB bottlenecks:
- Queue throughput constraints:
- Expensive external APIs:
- Cost-sensitive paths:
- Capacity plan before next release:
- Target response time:
- Max payload size:
- Slow query policy:
- Alert thresholds:

## 21. Testing Matrix

| Layer | Coverage now | Required before release | Notes |
|---|---|---|---|
| Unit |  |  |  |
| Integration |  |  |  |
| E2E |  |  |  |
| Security |  |  |  |
| Contract |  |  |  |
| Device / Browser QA |  |  |  |
| Legal / Payment checks |  |  |  |

## 22. Release / Rollback Lifecycle

- Release strategy:
- Release gatekeepers:
- Required checks before merge:
- Required checks before deploy:
- Smoke tests after deploy:
- Rollback trigger:
- Rollback owner:
- Post-incident update path:

## 23. Billing / Payments, если есть

- Payment providers:
- Order state model:
- Webhook signature verification:
- Idempotency:
- Refund flow:
- Fiscalization:
- Check issuance:
- Reconciliation:
- Failed payment / failed fiscalization alerts:

## 24. AI Governance, если есть AI

- Which models are used:
- Tool calling rules:
- Prompt storage:
- PII redaction in prompts:
- Cost limits:
- Token limits:
- Fallback model strategy:
- Runaway loop protection:
- Human approval gates:
- Audit trail for agent actions:

## 25. SEO / Publication Architecture, если публичный сайт

- Canonical strategy:
- Sitemap strategy:
- Index / noindex zones:
- Structured data:
- Publication workflow:
- Content ownership:
- Analytics / tracker notes:
- Multi-language strategy:

## 26. ADR Registry

| ADR | Decision | Status | Date | Why | Related risks |
|---|---|---|---|---|---|
| ADR-001 |  | proposed / accepted / deprecated |  |  |  |

## 27. Ownership Matrix

| Area | Primary owner | Secondary owner | Reviewer | Notes |
|---|---|---|---|---|
| Architecture |  |  |  |  |
| Security |  |  |  |  |
| Payments |  |  |  |  |
| Legal / Privacy |  |  |  |  |
| DevOps |  |  |  |  |
| AI layer |  |  |  |  |

## 28. Known Risks / Technical Debt

| ID | Risk / Debt | Severity | Why it exists | Mitigation | Target review date |
|---|---|---|---|---|---|
| RISK-001 |  | low / medium / high / critical |  |  |  |

## 29. Priority Action Register

### P0 — block release
- 
- 

### P1 — fix before production growth
- 
- 

### P2 — planned hardening / optimization
- 
- 

## 30. Production Readiness Gates

- Architecture reviewed
- PROJECT_MAP.md updated
- Security review completed
- Supply-chain review completed
- Scanner results triaged
- README current
- Deploy path documented
- Rollback documented
- Device / Browser QA completed
- Legal / privacy questions tracked
- Payment flow reviewed, если есть
- Monitoring / alerting ready
- Accepted risks documented

## 31. Update Governance

- Кто обновляет документ:
- Когда обновлять обязательно:
- Как документ проверяется:
- Где хранится source of truth:
- Как синхронизируется с README / PROJECT_MAP / runbooks:

## 32. Короткая версия чек-листа

- [ ] Документ отражает реальный проект, а не желаемую архитектуру
- [ ] Public / internal surfaces перечислены
- [ ] Интеграции и contracts описаны
- [ ] Threat model и privacy notes обновлены
- [ ] Payments / AI / legal sections заполнены, если применимо
- [ ] Rollback и readiness gates описаны
- [ ] P0 / P1 / P2 action register актуален
- [ ] Known risks и accepted risks не спрятаны в переписке
- [ ] Назначены owners и даты пересмотра
- [ ] Документ обновлен после последнего значимого change / incident / release
