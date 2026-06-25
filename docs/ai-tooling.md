# AI Tooling

Repository package: `v0.9.5`

Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/

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

## AI review engines

If you already use a dedicated AI review engine, keep the roles separate:
- let the review engine inspect diffs/files and emit review findings;
- let VCP handle route selection, trust-check, PR Gate, evidence bundle, and
  release framing.

VCP complements AI review engines. It does not pretend to replace them.

## Fast setup path

For practical adoption into another repository, start with:

- `docs/integrations/setup-playbook.md`
- `docs/integrations/agent-kits.md`
- `templates/AGENTS.claude.md`
- `templates/agents/CODEX.md`
- `templates/AGENTS.cursor.md`
- `templates/agents/COPILOT_INSTRUCTIONS.md`
- `ci-examples/github-actions/vcp-pr-gate.yml`

These are not official plugins. They are local-first, copy-ready templates and export paths.

## Generic guidance

- inspect before edit;
- do not overclaim shipped surfaces;
- do not say tests passed unless they ran;
- update machine-readable surfaces together with docs.


## Cost-aware routing

Use fast/cheap model tiers for search, reading, and low-risk discovery.
Use strong/reasoning model tiers for edits, manifests, tests, architecture, release prep, and safety-sensitive decisions.

See `docs/agent-model-routing.md` for adopter-facing routing and `docs/evaluator-token-budget.md` for evaluator-facing token budgeting.
