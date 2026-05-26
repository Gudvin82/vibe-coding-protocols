# AGENTS for Claude Code

Use this variant when Claude Code or similar tools can use subagents and explicit tool approvals.

## Focus
- keep discovery read-only first;
- use subagents only when they reduce risk;
- keep the implementation diff small;
- ask for approval before risky tool actions.

## Claude-specific notes
- prefer a read-only discovery subagent for broad repository mapping;
- pass only the evidence map to the implementation step;
- review tool permissions and `.claude/settings.json` if present;
- treat browser / shell / git write access as explicit operational scope.

## Model routing / token-aware discovery

When broad code discovery is needed:
1. do not start by reading the whole repository;
2. read `README.md`, `AGENTS.md`, `PROJECT_MAP.md` and architecture memory first;
3. use a cheaper or faster read-only discovery agent when available;
4. return only `path:line`, symbol, snippet, why it matters and confidence;
5. let the main implementation pass verify critical findings before editing;
6. keep independent diff review separate from implementation.

If Claude Code model routing is available:
- use Haiku or another cheaper or faster model for read-only discovery;
- use the main model for planning and implementation;
- use a separate review pass for independent diff review.
