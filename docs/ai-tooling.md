# AI Tooling

Repository package: `v0.8.6`

VCP is meant to be used alongside AI coding agents, not as a claim of official integrations.

## Cursor

- use local instruction templates and rules;
- run VCP commands locally;
- use dashboard output as a review surface.

## Claude Code

- use `templates/agents/CLAUDE.md`;
- require tests and trust-check in the final report;
- avoid broad unrelated rewrites.

## Codex

- use `templates/agents/CODEX.md`;
- require passed/warn/failed/not-run reporting;
- run version checks and trust-check before release claims.

## GitHub Copilot

- use VCP as a repository control layer;
- do not describe this as an official Copilot integration.

## Generic guidance

- inspect before edit;
- do not overclaim shipped surfaces;
- do not say tests passed unless they ran;
- update machine-readable surfaces together with docs.
