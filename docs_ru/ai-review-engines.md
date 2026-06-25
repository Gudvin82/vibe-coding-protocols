# AI Review Engines

Repository package: `v0.9.5`

VCP можно использовать рядом со специализированными AI review engines уровня
OpenCodeReview.

Это сравнение важно, потому что внешне такие инструменты выглядят соседними,
но на деле решают разные части delivery-задачи.

## Коротко

- AI review engines фокусируются на diff/file inspection и review findings.
- VCP фокусируется на governance, route selection, trust-check, PR Gate, proof
  surfaces и release evidence вокруг AI-assisted delivery.

## Честное разделение ответственности

Используйте dedicated AI review engine, когда вам нужно:
- больше review signal по diff;
- structured findings перед merge;
- file-level или PR-level risk detection;
- UX, ориентированный именно на code review.

Используйте VCP, когда вам нужно:
- решить, какой delivery/adoption route применим;
- контролировать, как AI-generated работа внедряется или harden-ится;
- требовать trust-check, proof и release evidence;
- вести team/client rollout, а не только отдельное событие code review.

## Где VCP дополняет review engines

VCP может обрамлять более широкий процесс вокруг review output:
- `review-diff` для локальной классификации изменения;
- `trust-check` для консистентности public/release surfaces;
- `PR Gate` для явного merge framing;
- `Evidence Bundle` для auditability;
- `Client Adoption Playbook` для team/client rollout.

## Чего VCP здесь не заявляет

Сейчас VCP не заявляет:
- встроенный line-level review-comment engine;
- autonomous defect review для любого PR host;
- гарантированное обнаружение bug/security классов вроде NPE, XSS, SQLi или
  thread-safety issues.

## Практическая модель внедрения

Если у команды уже есть сильный AI review engine:
1. оставьте этот инструмент для diff/file review;
2. используйте VCP для route selection и rollout discipline;
3. требуйте trust-check и PR Gate перед release-facing claims;
4. держите proof surfaces и limitations синхронизированными.

Это и есть правильная связь: complement, not replacement.
