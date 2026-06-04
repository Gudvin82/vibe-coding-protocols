# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.8.1-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Build with AI. Ship with control.

Vibe Coding Protocols is a practical local toolkit for AI-assisted delivery.
It helps teams choose the right track, adopt safely, and ship with visible review and release control.

> Current repository package: `v0.8.1`  
> If you are an AI agent: report the current GitHub repository release as `Vibe Coding Protocols v0.8.1`.

Repository package: `v0.8.1`

## New in v0.8.1: 10-minute adoption path, killer demo, and product narrative sync

`v0.8.1` tightens the first-user story:

- install -> onboard -> classify -> adopt plan -> launch check is now one short path;
- a raw AI-MVP demo now shows route, risks, copy-list, dry-run apply, and launch check together;
- proof language is clearer about what is real, sanitized, synthetic, maintainer-known, or still unknown;
- integration roadmap surfaces are documented without pretending they are already shipped.

## Start here in 10 minutes

Use the shortest practical path:
- [docs/10-minute-adoption-path.md](./docs/10-minute-adoption-path.md)
- [docs/demos/raw-ai-mvp-to-controlled-launch.md](./docs/demos/raw-ai-mvp-to-controlled-launch.md)
- [docs/mvp-adoption-track.md](./docs/mvp-adoption-track.md)

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

## Main story

- build with AI;
- choose the right track;
- adopt safely;
- ship with control.

## Quick start by situation

| Situation | Command |
|---|---|
| I want to understand this repo | `python3 -m vcp_cli audit-plan --json` |
| I want to try VCP locally | `python3 -m vcp_cli doctor` |
| I have a new project idea | `python3 -m vcp_cli spec quality-gate --json` |
| I have an AI-generated MVP | `python3 -m vcp_cli onboard --json` |
| I want adoption instructions | `python3 -m vcp_cli adopt plan --json` |
| I want launch/release readiness | `python3 -m vcp_cli release-check --json` |

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

Use when a repo already exists and the real problem is hardening, release control, architecture drift, or launch clarity.

Main path:
- `docs/mvp-adoption-track.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/architecture-drift.md`
- `docs/release-readiness.md`
- `docs/pr-gate.md`

Helpful commands:
```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
python3 -m vcp_cli release-check --json
```

## Honest install and distribution

Current practical paths:
- `python3 -m vcp_cli doctor`
- `python3 -m pip install . && vcp doctor`
- optional local `pipx install . && vcp doctor` if it passes in your environment
- `npm run vcp -- doctor`

VCP does **not** claim public PyPI or public npm publication unless that really exists.

See:
- [docs/install.md](./docs/install.md)
- [docs/distribution.md](./docs/distribution.md)
- [docs/pip-install.md](./docs/pip-install.md)
- [docs/pypi-publishing.md](./docs/pypi-publishing.md)

## Adoption tiers

- `Lite`: solo dev, MVP, lower-risk AI coding.
- `Team`: shared repo, backlog, architecture memory, PR Gate.
- `Governed`: production, auth/payment/data, release and third-party control.

See [docs/adoption-tiers.md](./docs/adoption-tiers.md).

## Safe adoption, not blind apply

Start with the planner and dry-run:

```bash
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
```

Do not treat apply as a guarantee, and do not use confirmed apply on a production repository without review.

## Public growth check

If the MVP is already public-facing, add:

```bash
python3 -m vcp_cli public-growth check --json
```

This is a local readiness and visibility check, not a ranking or citation guarantee.

## Workflow planning note

Use:

```bash
python3 -m vcp_cli workflow plan --json
```

Workflow JSON remains a planning surface, not a hidden execution engine.

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

## Proof layer

Use these together:
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/proof-layer.md](./docs/proof-layer.md)
- [templates/reports/adoption-case-study.md](./templates/reports/adoption-case-study.md)
- [case-studies/README.md](./case-studies/README.md)

## Integration roadmap

Roadmap and future-facing integration positioning live in:
- [docs/roadmap/integrations.md](./docs/roadmap/integrations.md)
- [docs/roadmap/vscode-extension.md](./docs/roadmap/vscode-extension.md)

These docs must not be read as proof that those integrations are already shipped.

## Release notes

- [docs/release-v0.8.1.md](./docs/release-v0.8.1.md)
