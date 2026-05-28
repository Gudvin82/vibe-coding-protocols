# Vibe-Check Init Report

Use init-report when you want a smallest safe route suggestion without changing files.

```bash
bash scripts/vibe-check.sh --init-report
bash scripts/vibe-check.sh --init-report --json
```

## What it reports

- whether the current directory looks like a repository;
- whether code already exists;
- whether `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE_MAP.md` and `AUDIT_BACKLOG.md` exist;
- a suggested route;
- first files to copy;
- a first validation command.

## Route logic

- Lite: almost no structure yet
- Starter: first rails and planning
- Hardening: existing code plus review artifacts
- Extended: public or production-facing route

## Reminder

If stack choices or multiple surfaces are still unclear, create `ARCHITECTURE_MAP.md` before implementation.
