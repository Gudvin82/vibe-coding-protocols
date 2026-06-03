<!-- vcp-artifact: AGENTS_CLAUDE -->
<!-- vcp-version: v0.6.1 -->
<!-- methodology-version: v1.4 -->

# AGENTS for Claude Code

Use this variant when Claude Code or similar tools can use subagents and explicit tool approvals.

## Memory Bank

Read first:
- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`, when multiple surfaces need a compact plan
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening

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

## Stop Conditions

- stop on auth, payments, migrations or CI/CD changes without human review;
- stop when the diff becomes cross-layer or too wide;
- ask before new dependencies or destructive operations.

## Remote safety

Before setup, template installation, push, PR, release or deploy:
- inspect `git remote -v`;
- confirm this is your project repository, not the source toolkit repository;
- do not push to the source toolkit repository by mistake;
- stop and ask when remote origin is unclear.

## Prompt drift control

Keep this file short.
If the rules become too long, move details into `PROJECT_MAP.md`, `ARCHITECTURE_MAP.md`, `ARCHITECTURE_SOURCE_OF_TRUTH.md` and `AUDIT_BACKLOG.md` instead of endlessly appending one file.
