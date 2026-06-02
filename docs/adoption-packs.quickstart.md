# Adoption Packs Quickstart

## What is an Adoption Pack?

An Adoption Pack is a small recommended file set for a situation.
It helps you avoid two bad defaults:
- copying nothing useful;
- copying the entire toolkit blindly.

## When should I use one?

Use a pack when you already know the target situation:
- production hardening;
- shared engine work;
- external API intake;
- maintenance cleanup;
- public-site readiness.

If you do not know the situation yet, start with:
- `AI_INTAKE.md`
- `vcp init`
- `vcp route --profile ...`

## First command

```bash
python3 -m vcp_cli adopt --pack production --dry-run
```

Node-first local option:

```bash
npm run vcp -- adopt --pack production --dry-run
```

## How to merge safely

1. run the pack in dry-run mode;
2. inspect the recommended files;
3. merge only the files that fit the target repo;
4. keep project-specific `AGENTS.md`, `PROJECT_MAP.md`, `SECURITY.md`, package files and CI files under manual review;
5. run validation before accepting AI-generated changes.

## Why not copy everything?

Because the right route depends on the repo.
A public production system, a local MVP, a shared engine, and a public site do not need the same VCP surface.
