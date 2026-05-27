# Vibe-Check Init Report

Use `--init-report` when you want a route suggestion without changing files.

```bash
bash scripts/vibe-check.sh --init-report
bash scripts/vibe-check.sh --init-report --json
```

## What it reports

- whether the repository already has code;
- whether `AGENTS.md`, `PROJECT_MAP.md`, `AUDIT_BACKLOG.md` and security files exist;
- whether common stack markers such as `package.json` or `pyproject.toml` exist;
- which route looks most appropriate next;
- which files to copy first;
- which larger artifacts to defer.

## Good use cases

- first contact with an unfamiliar repository;
- deciding between Lite, Starter, Hardening or Extended;
- explaining the smallest safe next step to a teammate.
