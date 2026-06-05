# AI IDE Compatibility

Методология vendor-neutral, но workflows у разных AI IDE отличаются.

## Matrix

| Tool | Что обычно удобно | Что адаптировать | Если AI не читает ссылки |
|---|---|---|---|
| Claude Code | code discovery, subagents, repo workflow | следить за scope и stop conditions | вставлять нужные markdown blocks вручную |
| Codex | diff-oriented task work, precise edits, structured reports | не давать уходить в broad rewrites | вставить prompt и relevant files прямо в чат |
| Cursor | composer / inline edits | дробить большие изменения | копировать prompts вручную и фиксировать smaller plan |
| Windsurf | Cascade / iterative coding | явно задавать active/deferred surfaces | давать scope, commands и expected output явно |
| Any other AI | can work as playbook consumer | нужен больший ручной контроль контекста | дать README + protocol + template вручную |

## Safe usage defaults

Для любой AI IDE полезно:
- не писать код до подтверждения маршрута;
- сначала выбрать `Starter` или `Hardening`;
- работать небольшими итерациями;
- использовать stop conditions;
- сохранять prompts в `docs/PROMPTS.md`.
