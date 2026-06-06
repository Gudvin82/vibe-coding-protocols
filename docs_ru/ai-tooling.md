# AI Tooling

Repository package: `v0.8.6`

VCP предназначен для использования рядом с AI coding agents, а не как заявление об official integrations.

## Cursor

- используй локальные instruction templates и rules;
- запускай VCP commands локально;
- используй dashboard output как review surface.

## Claude Code

- используй `templates/agents/CLAUDE.md`;
- требуй tests и trust-check в финальном report;
- избегай broad unrelated rewrites.

## Codex

- используй `templates/agents/CODEX.md`;
- требуй отчет в формате passed/warn/failed/not-run;
- запускай version checks и trust-check перед release claims.

## GitHub Copilot

- используй VCP как repository control layer;
- не называй это official Copilot integration.

## Общие правила

- inspect before edit;
- не overclaim shipped surfaces;
- не писать, что tests passed, если они не запускались;
- обновлять machine-readable surfaces вместе с docs.
