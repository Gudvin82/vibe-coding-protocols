# Vibe Coding Hub

`Vibe Coding Protocols` — это методология управления AI-assisted разработкой: от Product Brief и первого vertical slice до hardening-аудита, архитектурной справки, шаблонов и readiness checks.

## Когда идти в Starter

Открывайте Starter, если:
- у вас только идея;
- проект еще не структурирован;
- AI еще не начал писать код;
- нужно определить active / deferred surfaces;
- нужен Product Brief, Memory Bank и стартовая архитектура.

Файл: [ai-project-starter-protocol.md](./ai-project-starter-protocol.md)

## Когда идти в Hardening

Открывайте Hardening, если:
- AI уже сгенерировал код;
- проект надо проверить перед merge / deploy;
- есть fear of regressions;
- нужно проверить security, scanners, self-protection, migrations, payment/legal зоны или device/browser QA.

Файл: [ai-project-hardening-protocol.md](./ai-project-hardening-protocol.md)

## Когда использовать Templates

Templates нужны, когда надо быстро разложить проект по рабочим артефактам:
- findings backlog;
- scanner report;
- legal checklist;
- payment checklist;
- architecture source of truth;
- prompts log;
- project map;
- third-party registry.

Файлы: [../templates/](../templates/)

## Когда нужен Architecture Source of Truth

Architecture Source of Truth нужен, если проект уже больше, чем маленький однофайловый MVP:
- есть backend/API;
- есть database;
- есть integrations;
- есть mobile / bot / payment / worker / queue surfaces;
- проект передается другому инженеру;
- нужна ясная rollout / rollback / ownership картина.

Файл: [../templates/ARCHITECTURE_SOURCE_OF_TRUTH.md](../templates/ARCHITECTURE_SOURCE_OF_TRUTH.md)

## Memory Bank

Memory Bank — это не обязательно отдельная папка. Это набор файлов, который сохраняет устойчивый контекст между AI-сессиями и людьми.

Минимум:
- `README.md`
- `AGENTS.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE.md` или `Architecture Source of Truth`
- `SECURITY.md`
- `AUDIT_BACKLOG.md`
- `docs/PROMPTS.md`

## AI IDE Compatibility Matrix

| Tool | Что обычно удобно | Что адаптировать |
|---|---|---|
| Claude Code | code discovery, subagents, repo workflow | проверять, что agent не уходит в massive rewrite |
| Codex | сильная работа с задачами и diff | если не читает внешние URL — вставлять prompt-блоки вручную |
| Cursor | composer / inline edits | дробить большие изменения, фиксировать Stop Conditions |
| Windsurf | итерации через Cascade | явно задавать scope, active/deferred surfaces |
| Other AI IDE | можно использовать как playbook | дать контекст, файлы, команды, ограничения |

Если AI не умеет открывать ссылку — вставляйте markdown-файл или prompt-block вручную.

## Bot / AI-agent / Mobile mini-checklists

### Bot / AI-agent
- prompt injection;
- tool permissions;
- rate limits;
- cost limits;
- logging;
- user data;
- fallback / manual override;
- abuse cases;
- external API keys.

### Mobile / Telegram Mini App
- mobile viewport;
- touch targets;
- Safari / WebView issues;
- offline / degraded mode;
- auth / session;
- deep links;
- payment / webhook safety;
- device QA.

## Для команд и CTO

Методологию можно использовать как внутренний стандарт для AI-generated changes:
- Definition of Ready;
- Definition of Done;
- AGENTS.md;
- review gates;
- audit backlog;
- stop conditions;
- evidence before merge.

## Short / Full prompts

- [master-prompt-short.md](../prompts/master-prompt-short.md)
- [master-prompt-full.md](../prompts/master-prompt-full.md)

## Public vs private warning

Публичные templates на сайте и в этом repo — это не реальные private project docs.

Реальные архитектурные и operational документы проекта нужно хранить private / sanitized / encrypted.

## Official links

- Website: [https://anmalishev.ru/](https://anmalishev.ru/)
- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth: [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)
