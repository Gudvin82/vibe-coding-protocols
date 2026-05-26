# Audit Backlog

Практический шаблон для фиксации находок после AI Project Hardening Protocol.

## Как использовать

- Не просите AI "починить все" сразу.
- Сначала перенесите все находки в backlog.
- Отдельно выделите Critical и High.
- У каждой задачи должен быть владелец, статус, evidence и источник находки.
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

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| SEC-001 | Security | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |
| PAY-001 | Payments | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## High

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| DEP-001 | Supply Chain | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |
| LEGAL-001 | Legal | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## Medium

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| QA-001 | Device QA | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |
| TEST-001 | Tests | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## Low

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| DOC-001 | Documentation | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## Accepted risks

| ID | Risk | Why accepted | Review date | Owner |
|---|---|---|---|---|
| RISK-001 | [FILL IN: accepted risk] | [FILL IN: why accepted] | [FILL IN] | [FILL IN] |

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
