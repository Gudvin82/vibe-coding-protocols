# Automated Vibe Check

`vibe-check` is a lightweight repository check.

It does not replace the Hardening Protocol, human review, scanners or security work.

## What it checks

- presence of baseline project files;
- missing `README.md`, `AGENTS.md`, `PROJECT_MAP.md` or `AUDIT_BACKLOG.md` depending on mode;
- whether `.env.example` is expected;
- whether `.env` appears in the repository;
- whether `.gitignore` exists;
- whether architecture or project-map docs may need review in a public webroot context.

## Modes

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
```

## How to use in your own project

1. Copy `scripts/vibe-check.sh` into your repository.
2. Run it locally before merge or PR.
3. Optionally add it to CI.

## CI note

The GitHub workflow in this repository checks the toolkit itself, not arbitrary target applications.
