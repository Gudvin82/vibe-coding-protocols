# Hardening Prompts

## Prompt 0 — Audit mode

Ты будешь проводить инженерный аудит AI-generated проекта.

Сначала не вноси изменения в код.

Определи режим:
- Light
- Standard
- Full

Если проект является первым vertical slice после Starter Protocol, оцени базовую связку и critical blockers, не требуй full production compliance без причины.

## Prompt 1 — Code Discovery / PROJECT_MAP

Проведи этап Code Discovery.

Цель:
- найти ключевые части проекта;
- составить compact evidence map;
- создать или обновить `PROJECT_MAP.md`.

## Prompt 2 — ARCHITECTURE

Проверь, есть ли актуальная архитектурная справка.

Если нет — создай или обнови `ARCHITECTURE.md` / `Architecture Source of Truth` по реальному проекту.

## Prompt 3 — Full audit

Проведи полный аудит проекта.

Проверь:
1. architecture
2. security
3. self-protection
4. supply chain / safe integration
5. scanners
6. database / load / scalability readiness
7. legal / payment applicability
8. device / browser QA
9. test / validation gaps
10. backlog / next steps

[SYSTEM INSTRUCTION: If the project is large, split the audit into 2-3 passes and start with the first pass. Do not attempt to complete the entire full audit in one uncontrolled response.]

## Prompt 4 — Dependencies and updates

Проверь внешние зависимости, templates, APIs, actions, images и update path.

Не одобряй `pull latest && deploy`.

## Prompt 5 — Scanners

Если scanners доступны — используй их.

Если нет:
- не имитируй запуск;
- пометь `not run`;
- начни с package manager audit, lockfile review, grep по secret patterns и `.gitignore` review.

## Prompt 6 — Fix plan

Составь fix plan по findings.

Исправляй только actionable issues.

Если в процессе найдешь смежные безопасные баги в той же зоне — можно исправить их, но крупные/risky изменения выноси в backlog и проси approval.

## Prompt 7 — Implement fixes

Перед изменениями:
- покажи changed files plan;
- предложи checkpoint, если правки широкие;
- не делай destructive commands без approval.

После изменений:
- покажи diff summary;
- покажи validation commands;
- выведи self-review.

## Prompt 8 — Final report

Собери short report и full report.

Short report:
- verdict;
- blockers;
- top risks;
- commands run / not run;
- next steps.

Full report:
- findings by severity;
- scanner status;
- self-protection status;
- database/load status;
- migration rollback status;
- tests status;
- accepted risks;
- backlog updates.
