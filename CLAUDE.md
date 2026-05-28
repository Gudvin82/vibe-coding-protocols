# CLAUDE.md

## Which agent file should I use?

- Root `AGENTS.md` configures this repository.
- Root `CLAUDE.md` configures Claude Code for this repository.
- Do not copy root `AGENTS.md` blindly into your project.
- For your own project, copy `templates/AGENTS.md` as `AGENTS.md`.
- For Claude Code, use `templates/AGENTS.claude.md` or adapt it into your project's `CLAUDE.md`.

## Memory Bank

Read first:
- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`, when multiple surfaces need a compact plan
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening
- `docs/PROMPTS.md` or `PROMPTS.md`, if prompts are tracked
- `SECURITY.md` or `SECURITY_BASELINE.md`, for public or production projects

## Token-aware discovery

Use token-aware discovery before broad edits.
Return an evidence map, not a full search transcript.

## Model routing

When broad discovery is needed:
- use a cheaper or faster read-only discovery pass when available;
- keep the main implementation pass focused on decisions and edits;
- use an independent review pass before risky merge or deploy work.

## Stop Conditions

Respect the repository Stop Conditions from `AGENTS.md`.
Pause on auth, payments, migrations, CI/CD changes, large cross-layer diffs or unclear scope.

## Remote safety

Before setup, template installation, push, PR, release or deploy:
- inspect `git remote -v`;
- confirm this is the user's project repository, not the source toolkit repository;
- do not push to the source toolkit repository by mistake;
- stop and ask when remote origin is unclear.
