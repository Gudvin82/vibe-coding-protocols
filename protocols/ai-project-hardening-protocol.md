# AI Project Hardening Protocol

Markdown-версия `AI Project Hardening Protocol` для уже существующих AI-generated проектов.

## Режимы

### Light Hardening

Подходит, если проект только что пришел из Starter и содержит 1–2 первые фичи.

Проверяем:
- связку слоев;
- secrets hygiene;
- active / deferred surfaces;
- buildability;
- database / migrations тупики;
- наличие README / AGENTS / PROJECT_MAP / ARCHITECTURE;
- next backlog.

### Standard Hardening

Подходит для рабочего MVP перед staging / limited release.

### Full Hardening

Подходит перед production-ready claims, когда уже важны scanners, legal/payment, deeper self-protection и broad readiness.

## Если вы пришли из Starter

Используйте уже созданные артефакты:
- Product Brief;
- README.md;
- AGENTS.md;
- PROJECT_MAP.md;
- ARCHITECTURE.md / Architecture Source of Truth;
- SECURITY.md;
- docs/PROMPTS.md;
- AUDIT_BACKLOG.md.

Если этих файлов нет, сначала создайте минимум `PROJECT_MAP.md` и `ARCHITECTURE.md`.

## Code discovery

Начинайте audit с evidence map:
- key entrypoints;
- routes / endpoints;
- services;
- data model;
- auth;
- integrations;
- scripts / build / test commands;
- active / deferred surfaces.

## PROJECT_MAP / Architecture

Обновите или создайте:
- `PROJECT_MAP.md`
- `ARCHITECTURE.md` / `Architecture Source of Truth`

Архитектура должна описывать реальный проект, а не идеальную картинку после факта.

## Security baseline

Проверьте:
- secrets;
- auth / session boundaries;
- input validation;
- logs;
- uploads;
- debug mode;
- exposed docs / stack traces;
- approval gates для risky changes.

## Self-Protection

Проверьте, что проект защищает сам себя:
- `.env`, `.git`, backups, logs, source maps не торчат наружу;
- private docs не лежат в public webroot;
- admin / internal endpoints не доступны снаружи без нужных ограничений;
- scanner / worker / browser automation не работают с лишними правами.

## Supply-chain / Safe Integration

Любой внешний repo / package / action / image / dataset — это supply-chain risk.

Проверьте:
- origin;
- maintainer;
- license;
- install scripts;
- workflows;
- binaries / obfuscation;
- secrets access;
- quarantine process;
- safe update path.

## Scanners

### Full path

Если доступны, используйте реальные scanners:
- Trivy;
- Gitleaks;
- OSV-Scanner;
- dependency audit tools.

### Light fallback

Если полноценные scanners недоступны:
- не имитируйте запуск;
- пишите `not run`;
- начните с package manager audit;
- сделайте lockfile review;
- grep по `SECRET/API_KEY/TOKEN/PASSWORD`;
- проверьте `.env` / `.gitignore`;
- зафиксируйте manual follow-up commands.

## Database / Load / Scalability readiness

Проверьте:
- data model / ERD;
- migration history;
- indexes;
- unique constraints / FKs;
- N+1;
- pagination / limits;
- sync vs async operations;
- queue / worker model;
- retries / backoff;
- idempotency;
- rate limits;
- external API / LLM bottlenecks;
- backup / restore;
- scalability backlog.

## Legal / Payment checks

Если проекту это релевантно, проверьте:
- PDn / privacy contour;
- forms / consent;
- cookies;
- offer / terms;
- payment / fiscalization;
- refund / access wording.

## Device / Browser QA

Для большинства публичных web/MVP:
- Mobile viewport;
- Safari / iOS WebView;
- Chrome Android;
- Desktop Chrome / Firefox;
- then edge cases.

Для desktop/internal проектов приоритет может быть другим.

## Independent diff review

Отдельный reviewer смотрит только активный git diff.

Правила:
- reviewer не редактирует файлы;
- reviewer не наследует аргументацию основной сессии;
- reviewer смотрит `git status`, `git diff`, touched files и validation output;
- reviewer возвращает only actionable findings.

См. prompt: [../prompts/independent-diff-review-prompt.md](../prompts/independent-diff-review-prompt.md)

## Troubleshooting

Если AI пошел не туда:
- остановите задачу;
- вернитесь к AGENTS / plan;
- сравните diff;
- разбейте изменения на smaller steps;
- не имитируйте scanner results;
- если нужно — отложите risky branch в backlog.

## Emergency recovery

Если AI сломал working code:
1. зафиксируйте `git status` и список touched files;
2. соберите build/test/runtime error;
3. вернитесь к last working state осознанно;
4. не делайте destructive commands без approval;
5. сделайте smaller recovery plan;
6. добавьте incident note в `AUDIT_BACKLOG.md`.

## AI-generated migration rollback

Перед миграциями:
- backup;
- staging / copy-of-data test;
- down migration или rollback plan;
- destructive ops review;
- expand-and-contract для zero-downtime, если нужно;
- smoke test и monitoring после применения.

## AI-generated test strategy

Тесты должны покрывать:
- critical path;
- найденные regressions;
- auth / payment / webhook flows, если active;
- mocked external APIs / LLM.

Не добавляйте новый test framework без approval и не генерируйте flaky tests.

## Final report

Финальный отчет должен содержать:
- verdict;
- blockers;
- findings by severity;
- scanner status;
- self-protection status;
- database/load status;
- migration rollback status;
- tests run / not run;
- accepted risks;
- next steps;
- updated AUDIT_BACKLOG.

## Exit criteria

Проект прошел выбранный режим hardening, когда:
- режим выбран явно;
- audit report сформирован;
- blockers классифицированы;
- critical/high findings исправлены или accepted with reason;
- scanner status зафиксирован;
- self-protection проверен;
- database/load readiness оценены;
- legal/payment зоны проверены по применимости;
- independent diff review проведен или явно отложен;
- `AUDIT_BACKLOG.md` обновлен.

Важно: `Passed Light Hardening` не означает `production-ready`.
