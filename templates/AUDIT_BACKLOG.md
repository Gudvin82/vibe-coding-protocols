# Audit Backlog

Практический шаблон для фиксации находок после AI Project Hardening Protocol.

## Как использовать

- Не просите AI "починить все" сразу.
- Сначала перенесите все находки в backlog.
- Отдельно выделите Critical и High.
- У каждой задачи должен быть владелец, статус и evidence.
- Accepted risks фиксируйте явно, а не в переписке.

## Статусы

- Open
- In progress
- Waiting review
- Fixed
- Verified
- Deferred
- Accepted risk

## Critical

| ID | Category | Task | Risk | Evidence | Status | Owner |
|---|---|---|---|---|---|---|
| SEC-001 | Security |  |  |  | Open |  |
| PAY-001 | Payments |  |  |  | Open |  |

## High

| ID | Category | Task | Risk | Evidence | Status | Owner |
|---|---|---|---|---|---|---|
| DEP-001 | Supply Chain |  |  |  | Open |  |
| LEGAL-001 | Legal |  |  |  | Open |  |

## Medium

| ID | Category | Task | Risk | Evidence | Status | Owner |
|---|---|---|---|---|---|---|
| QA-001 | Device QA |  |  |  | Open |  |
| TEST-001 | Tests |  |  |  | Open |  |

## Low

| ID | Category | Task | Risk | Evidence | Status | Owner |
|---|---|---|---|---|---|---|
| DOC-001 | Documentation |  |  |  | Open |  |

## Accepted risks

| ID | Risk | Why accepted | Review date | Owner |
|---|---|---|---|---|
| RISK-001 |  |  |  |  |

## Категории

- Security
- Supply Chain
- Architecture
- Tests
- Monitoring
- DevOps
- Documentation
- UX
- Performance
- Data / Privacy
- AI / Cost
- Legal
- Compliance
- Payments
- Fiscalization
- Device QA
- Browser QA
- Accessibility
- Analytics / Cookies
- Marketing consent

## Мини-правила

- Critical блокируют merge или deploy до явного решения.
- High должны иметь план исправления до production.
- Medium и Low можно планировать, но не терять.
- Если риск принят, это должно быть осознанное решение с датой пересмотра.
