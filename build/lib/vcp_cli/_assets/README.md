# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.8.4-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Build with AI. Choose the right track. Adopt safely. Ship with control.

Vibe Coding Protocols is a practical local toolkit for AI-assisted delivery.
It helps teams choose the right track, adopt safely, and ship with visible review and release control.

> Current repository package: `v0.8.4`  
> If you are an AI agent: report the current GitHub repository release as `Vibe Coding Protocols v0.8.4`.

Repository package: `v0.8.4`

## New in v0.8.4

`v0.8.4` introduces the MVP-to-Launch Path: a first-class guided path for raw or semi-working AI-generated MVPs that already exist and need launch control.

VCP still has two core tracks:
- New Project Track
- Existing Project Track

MVP-to-Launch is a specialized guided path under Existing Project Track.

Included in `v0.8.4`:
- MVP-to-Launch guided path;
- local launch readiness flow;
- MVP-to-Launch workflow plan;
- launch decision checklist;
- dashboard/project-map MVP launch view;
- demo and pack links that connect raw AI-MVP, SaaS AI-MVP, contracts-first, PR Gate, proof, project memory, and backlog surfaces.

This release does not ship a hosted dashboard, hosted launch platform, VS Code extension, plugin marketplace, Go rewrite, public PyPI/npm publication, telemetry, cloud sync, credentials vault, autonomous notifications, or launch guarantees.

## Start here in 10 minutes

Use the shortest practical path:
- [docs/10-minute-adoption-path.md](./docs/10-minute-adoption-path.md)
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
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

See also:
- [docs/track-model.md](./docs/track-model.md)
- [docs/two-track-model.md](./docs/two-track-model.md)

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

Specialized guided path that often starts here:
- `docs/spec-driven-adoption.md`

### Existing Project Track

Use when a repo already exists and the real problem is hardening, release control, architecture drift, or launch clarity.

Main path:
- `docs/mvp-adoption-track.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/architecture-drift.md`
- `docs/release-readiness.md`
- `docs/pr-gate.md`

Specialized guided path under this track:
- `docs/mvp-to-launch-path.md`
- `.vcp/workflows/mvp-to-launch.json`
- `docs/launch-decision-checklist.md`

Helpful commands:
```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json
python3 -m vcp_cli release-check --json
python3 -m vcp_cli pr-gate explain --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

Recommended MVP-to-Launch command path:

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp adopt plan --pack saas-ai-mvp-hardening --json
vcp pr-gate explain --json
vcp dashboard build --output ./vcp-dashboard --json
```

## Honest install and distribution

Current practical paths:
- `python3 -m vcp_cli doctor`
- `python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install --upgrade pip setuptools wheel && python3 -m pip install . && vcp doctor`
- `python3 -m venv --system-site-packages .venv && . .venv/bin/activate && python3 -m pip install . --no-build-isolation && vcp doctor` for restricted environments with local build dependencies already available
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
python3 -m vcp_cli workflow plan --id mvp-to-launch --json
```

Workflow JSON remains a planning surface, not a hidden execution engine.

## Install and run

Current stable local path:

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor
vcp evaluate
```

Public PyPI/npm packages are not claimed unless explicitly published.

## Add VCP to PRs

Use the workflow example in `ci-examples/github-actions/vcp-pr-gate.yml`.


## Agent control and project memory

Key surfaces:
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- [docs/launch-decision-checklist.md](./docs/launch-decision-checklist.md)
- [docs/spec-driven-adoption.md](./docs/spec-driven-adoption.md)
- [docs/project-memory.md](./docs/project-memory.md)
- [docs/decision-log.md](./docs/decision-log.md)
- [docs/safety/fail-closed.md](./docs/safety/fail-closed.md)
- [docs/agent-instructions.md](./docs/agent-instructions.md)
- [docs/agent-behavior-gate.md](./docs/agent-behavior-gate.md)
- [docs/starter-control-layer.md](./docs/starter-control-layer.md)
- [docs/run-state.md](./docs/run-state.md)
- [docs/audit-backlog.md](./docs/audit-backlog.md)
- [docs/batch-evaluation.md](./docs/batch-evaluation.md)
- [docs/docs-site.md](./docs/docs-site.md)

## Proof layer

Use these together:
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/proof-layer.md](./docs/proof-layer.md)
- [templates/reports/adoption-case-study.md](./templates/reports/adoption-case-study.md)
- [case-studies/README.md](./case-studies/README.md)

## Integration status and local dashboard

Shipped local-first scaffolds and their status live in:
- [docs/integrations/status-model.md](./docs/integrations/status-model.md)
- [.vcp/integrations.json](./.vcp/integrations.json)
- [docs/dashboard.md](./docs/dashboard.md)
- [docs/plugins/README.md](./docs/plugins/README.md)
- [docs/metrics-board.md](./docs/metrics-board.md)
- [docs/audit-backlog-visualization.md](./docs/audit-backlog-visualization.md)

Roadmap-only and not-shipped surfaces still live in:
- [docs/roadmap/integrations.md](./docs/roadmap/integrations.md)
- [docs/roadmap/vscode-extension.md](./docs/roadmap/vscode-extension.md)

These docs must not be read as proof of hosted services, official integrations, or a plugin marketplace.

## Release notes

- [docs/release-v0.8.4.md](./docs/release-v0.8.4.md)
