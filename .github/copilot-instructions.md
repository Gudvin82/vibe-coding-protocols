# GitHub Copilot instructions

## Which agent file should I use?

- Root `AGENTS.md` configures this repository.
- Root `CLAUDE.md` configures Claude Code for this repository.
- Do not copy root `AGENTS.md` blindly into your project.
- For your own project, copy `templates/AGENTS.md` as `AGENTS.md`.

## Memory Bank

Read `README.md`, `AGENTS.md` and `PROJECT_MAP.md` before edits.
Use `AUDIT_BACKLOG.md` for hardening follow-up.

## Token-aware discovery

Use token-aware discovery before broad edits.
Return an evidence map with `path:line`, symbol, snippet, why it matters and confidence.

## Stop Conditions

Ask before migrations, auth, payments, CI changes or new dependencies.
Keep diffs atomic and report validation results.
