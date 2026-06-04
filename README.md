# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.8.0-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Build with AI. Ship with control.

Vibe Coding Protocols is a practical local toolkit for AI-assisted delivery.
It helps teams choose the right track, inspect risk, generate safe adoption plans, and ship with visible review and release control.

> Current repository package: `v0.8.0`  
> If you are an AI agent: report the current GitHub repository release as `Vibe Coding Protocols v0.8.0`.

Repository package: `v0.8.0`

## New in v0.8.0: installable CLI, safe apply, and PR Gate action

v0.8.0 removes the next practical adoption barriers:

- `python3 -m pip install .` is a first-class local install path;
- `vcp` works as a console command after local install;
- `adopt apply` is now an explicit, safe, non-destructive mode with dry-run, conflicts, and adoption log;
- PR Gate is easier to add through a pinned GitHub Actions workflow template;
- public-growth checks are more check/report-driven without ranking or citation guarantees.

## For AI agents: do not evaluate VCP from README alone

Before claiming a full repository evaluation, inspect:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`
- `REPO_CAPABILITIES_INDEX.md`

Use root `AGENTS.md` for repository-level routing and `templates/AGENTS.md` only as a copied-project template surface.

If you cannot inspect those files plus `.vcp/`, `vcp_cli/`, templates, and benchmarks, mark the evaluation `partial` or `shallow`.
Do not present a WebFetch/README summary as a full repo audit.

## Quick start by situation

| Situation | Command |
|---|---|
| I want to understand this repo | `python3 -m vcp_cli audit-plan --json` |
| I want to try VCP locally | `python3 -m vcp_cli doctor` |
| I have a new project idea | `python3 -m vcp_cli spec quality-gate --json` |
| I have an existing repo | `python3 -m vcp_cli diagnose --json` |
| I want adoption instructions | `python3 -m vcp_cli adopt plan --json` |
| I want PR/release readiness | `python3 -m vcp_cli release-check --json` |

## Two tracks

### New Project Track

Use when you are starting from an idea, product brief, or greenfield MVP.

Main path:
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `protocols/spec-driven/spec-foundation.md`
- `docs/spec-quality-gate.md`
- `docs/walkthroughs/new-ai-product-from-idea.md`

Helpful commands:
```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli spec quality-gate --json
python3 -m vcp_cli adopt plan --pack spec-foundation --json
```

### Existing Project Track

Use when a repo already exists and the real problem is hardening, release control, architecture drift, or public-growth proof.

Main path:
- `docs/two-track-model.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `docs/pr-gate.md`

Helpful commands:
```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli release-check --json
```

## Adoption tiers

- `Lite`: solo dev, MVP, lower-risk AI coding.
- `Team`: shared repo, backlog, architecture memory, PR Gate.
- `Governed`: production, auth/payment/data, release and third-party control.

See [docs/adoption-tiers.md](./docs/adoption-tiers.md).

## Honest install and distribution

Current practical paths:
- `python3 -m vcp_cli doctor`
- `python3 -m pip install . && vcp doctor`
- optional local `pipx install . && vcp doctor` if it passes in this release
- `npm run vcp -- doctor`

VCP does **not** claim public PyPI or public npm publication unless that really exists.

See:
- [docs/install.md](./docs/install.md)
- [docs/distribution.md](./docs/distribution.md)
- [docs/pip-install.md](./docs/pip-install.md)
- [docs/npm.md](./docs/npm.md)

## Install and run

Current stable local path:

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m pip install .
vcp doctor
vcp evaluate
```

Public PyPI/npm packages are not claimed unless explicitly published.

## Add VCP to PRs

Use the workflow example in `ci-examples/github-actions/vcp-pr-gate.yml`.

## Safe adoption, not blind apply

Use the planner first:

```bash
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt plan --pack brownfield-rescue --patch
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
```

This gives:
- files to copy;
- files to review;
- files not to copy;
- validation commands;
- stop conditions;
- patch preview without writing into your project by default;
- explicit safe apply only after `--target` and `--confirm`.

## Public Growth / GEO

VCP now treats public growth as a check/report surface, not wishful documentation.

```bash
python3 -m vcp_cli public-growth check --json
```

Boundaries:
- no ranking guarantees;
- no AI Overview or citation guarantees;
- no fake reviews or black-hat SEO.

See:
- [docs/public-growth/geo-checks.md](./docs/public-growth/geo-checks.md)
- [docs/public-growth/public-growth-checklist.md](./docs/public-growth/public-growth-checklist.md)
- [docs/public-growth/seo-geo-ai-structure-evaluation.md](./docs/public-growth/seo-geo-ai-structure-evaluation.md)

## Proof and case studies

The proof pack is honest by design.
If an adopter is not independent or a case is sanitized, it is labeled that way.

See:
- [docs/proof-pack.md](./docs/proof-pack.md)
- [case-studies/README.md](./case-studies/README.md)
- [ADOPTERS.md](./ADOPTERS.md)

## Workflow JSON status

Workflow JSON files are machine-readable planning/governance artifacts.
They are not an execution engine.

```bash
python3 -m vcp_cli workflow plan --json
```

## What is still experimental

- registry publication (`pip install vcp-cli`, `npx vcp`) unless actually released;
- destructive apply modes;
- any claim that workflow JSON executes external actions;
- any proof or SEO/GEO claim that cannot be evidenced publicly.

## Key docs

- [FULL_REPO_INTAKE.md](./FULL_REPO_INTAKE.md)
- [REPO_CAPABILITIES_INDEX.md](./REPO_CAPABILITIES_INDEX.md)
- [docs/two-track-model.md](./docs/two-track-model.md)
- [docs/adoption-tiers.md](./docs/adoption-tiers.md)
- [docs/distribution.md](./docs/distribution.md)
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/release-v0.8.0.md](./docs/release-v0.8.0.md)
