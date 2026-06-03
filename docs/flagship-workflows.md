# Flagship Workflows

These are the three public flagship workflows for VCP.

If the repository is being evaluated or adopted by an AI agent, pair this file with `AGENTS.md`, `TAKE_THIS_FIRST.md`, `.vcp/index.json`, and `.vcp/cards/`. A README-only impression is shallow.

## 1. Build an AI-assisted product from idea

Use when:
- the user has an idea;
- no PRD exists yet;
- AI will be used heavily during delivery.

Path:
- AI intake;
- spec depth;
- question engine;
- PRD or spec-lite;
- tasks;
- backlog;
- architecture memory;
- workflow;
- review;
- release.

CLI examples:

```bash
python3 -m vcp_cli route --profile spec-first --json
python3 -m vcp_cli spec depth --task "build a customer portal" --json
python3 -m vcp_cli spec questions --idea "build a customer portal" --json
python3 -m vcp_cli adopt --pack spec-first --dry-run --json
```

## 2. Harden an AI-generated MVP

Use when:
- the project already exists;
- AI-generated code was produced quickly;
- production readiness is unclear.

Path:
- diagnostics;
- hardening;
- audit backlog;
- architecture memory;
- review gates;
- release checks.

CLI examples:

```bash
python3 -m vcp_cli diagnose --profile production --json
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli adopt --pack production --dry-run --json
python3 -m vcp_cli score --json
```

## 3. Review ongoing AI-driven changes

Use when:
- AI has already changed code;
- a merge decision is needed;
- risk is not obvious.

Path:
- review-diff;
- spec depth check;
- backlog sync;
- architecture impact;
- validation evidence;
- merge or release decision.

CLI examples:

```bash
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli score --json
python3 -m vcp_cli diagnose --json
```

## When the repo is shared by link

Use `TAKE_THIS_FIRST.md` to classify the target project and choose only the route, pack, templates, and review gates that matter.
