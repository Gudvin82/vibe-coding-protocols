# CLI

VCP has two honest local entrypaths:
- the Python CLI, which remains the primary implementation;
- a thin local npm wrapper for Node-first users.

The repo is not claiming published npm, PyPI, Homebrew, or native installer distribution in `v0.5.9`.

## Start here

Linux and macOS:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli route --profile public-growth
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli evaluate --json
```

Local npm wrapper:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- route --profile public-growth
npm run vcp -- evaluate
npm run vcp -- manifest validate
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli init --print-prompt
py -m vcp_cli route --profile public-growth --json
py -m vcp_cli evaluate --json
npm run vcp -- doctor
```

## Current commands

- `version` — repository package, methodology, git info
- `doctor` — environment, repo, manifest, and wrapper status
- `check` — Python-native fast checks and optional Bash-backed full checks
- `init` — guidance-only onboarding and copy-paste prompt output
- `route` — choose the route for a target profile
- `adopt` — dry-run an Adoption Pack
- `evaluate` — summarize repository evaluation surfaces and print the evaluation prompt
- `spec` — print spec templates, validate spec artifacts, and summarize spec readiness
- `workflow` — browse and validate local workflow definitions
- `diagnose` — inspect project/process readiness by layer
- `backlog` — validate, list, add, move, complete, archive, and report backlog items
- `score` — local readiness heuristic summary
- `manifest` — show and validate machine-readable metadata
- `benchmark` — validate route and adoption scenarios
- `review` — helper for the Post-Task Code Review Gate
- `demo` — print small route/adoption demos

## Public growth helper

Use `public-growth` when public-facing pages, SEO/GEO, schema, AI visibility, or commercial page templates need structure.

```bash
python3 -m vcp_cli route --profile public-growth --json
python3 -m vcp_cli adopt --pack public-growth --dry-run --json
npm run vcp -- route --profile public-growth
```

This route is intentionally defensive:
- no claim of guaranteed indexing or rankings;
- no hidden FAQ content;
- no doorway pages or spam-link tactics;
- no fake reviews, ratings, or fabricated case proof.

## Spec, workflow, and diagnostics helpers

Use these when the feature is still unclear or the repo needs process-level readiness checks.

```bash
python3 -m vcp_cli route --profile spec-first --json
python3 -m vcp_cli spec template prd
python3 -m vcp_cli spec validate --json
python3 -m vcp_cli workflow list --json
python3 -m vcp_cli workflow validate --json
python3 -m vcp_cli diagnose --profile production --json
npm run vcp -- workflow validate
```

## Evaluation helper

Use `evaluate` when a human or external AI agent needs a fair repository-level picture.

```bash
python3 -m vcp_cli evaluate
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli evaluate --print-prompt
npm run vcp -- evaluate
```

`evaluate` reports:
- repository version;
- key evaluation files present;
- manifest directory;
- benchmark count;
- command and protocol counts;
- backlog and operations workflow status;
- public-growth and glossary layer status;
- known limitations link;
- prompt template path.

It does not call external AI APIs and does not pretend to be a vanity score.

## npm wrapper status

Local options that work inside this repository:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- route --profile public-growth
npm run vcp -- evaluate
npm run vcp -- manifest validate
```

Optional local linking:

```bash
npm link
vcp doctor
vcp evaluate
vcp init --print-prompt
```

Public npm and `npx` distribution are planned.
Current npm support is local wrapper only.

## Fast vs full

- `check --fast` is Python-native and is the preferred cross-platform path.
- `check --full` may call legacy Bash scripts when Bash is available.
- If Bash is missing, full legacy checks are skipped clearly instead of crashing.

## Init behavior

`vcp init` is guidance-only in `v0.5.9`.
It does not modify files by default.
Use it to:
- print the short onboarding flow;
- print a target-specific prompt with `--print-prompt`;
- steer an AI agent toward `AI_INTAKE.md`, `route`, and `adopt --dry-run`.

If the task is repository evaluation instead of repo adoption, use `vcp evaluate` instead of overloading `init`.

## Backlog workflow

Current backlog helpers:

```bash
python3 -m vcp_cli backlog validate
python3 -m vcp_cli backlog list --json
python3 -m vcp_cli backlog add --title "Triage API retries" --type bug --priority P1 --source review --dry-run --json
python3 -m vcp_cli backlog move --id VCP-001 --status doing --dry-run --json
python3 -m vcp_cli backlog done --id VCP-001 --validation "tests green" --review "accepted" --dry-run --json
python3 -m vcp_cli backlog archive --id VCP-002 --reason "Not in scope" --dry-run --json
python3 -m vcp_cli backlog report --json
```

Real writes create a backup in `.vcp/runtime/backups/` before `PROJECT_BACKLOG.md` is updated.
Dry-run stays non-destructive and returns a preview instead of writing.

## Manifest location

Machine-readable metadata lives in:
- `.vcp/manifests/`

The CLI prefers `.vcp/manifests/` and can still read legacy root manifests as a fallback if a repository has not been migrated yet.

## Safety boundaries

The CLI:
- does not require network;
- does not call external AI APIs;
- does not connect third-party APIs automatically;
- does not auto-apply Adoption Packs;
- does not run offensive tooling;
- does not replace human review.

## Related docs

- [install.md](./install.md)
- [glossary.md](./glossary.md)
- [geo-ai-visibility.md](./geo-ai-visibility.md)
- [page-templates.md](./page-templates.md)
- [../AI_EVALUATION_GUIDE.md](../AI_EVALUATION_GUIDE.md)
- [scoring.md](./scoring.md)
- [npm.md](./npm.md)
- [npm-publishing-checklist.md](./npm-publishing-checklist.md)
- [windows.md](./windows.md)
- [init.md](./init.md)
- [release-v0.5.9.md](./release-v0.5.9.md)
