# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.8.5-blue)](./CHANGELOG.md)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)

Build with AI. Choose the right track. Adopt safely. Ship with control.

Vibe Coding Protocols is a practical local toolkit for AI-assisted delivery.
It helps teams choose the right track, adopt safely, and ship with visible review and release control.

> Current repository package: `v0.8.5`  
> If you are an AI agent: report the current GitHub repository release as `Vibe Coding Protocols v0.8.5`.

Repository package: `v0.8.5`

## New in v0.8.5

`v0.8.5` combines the planned local platform UX and integration-pack work into one release.

It improves:
- local dashboard UX;
- local platform flow;
- project map and run history views;
- integration packs;
- IDE roadmap clarity;
- docs-site scaffold;
- AI-readable docs;
- Russian documentation parity.

It does not ship a hosted dashboard, hosted platform, VS Code extension, plugin marketplace, Go rewrite, public PyPI/npm publication, cloud sync, telemetry, remote plugin registry, credential vault, production safety guarantees, launch guarantees, SEO/GEO ranking guarantees, or guaranteed AI citation.

## Start here in 10 minutes

Use the shortest practical path:
- [docs/10-minute-adoption-path.md](./docs/10-minute-adoption-path.md)
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- [docs/local-platform-flow.md](./docs/local-platform-flow.md)
- [docs/demos/raw-ai-mvp-to-controlled-launch.md](./docs/demos/raw-ai-mvp-to-controlled-launch.md)
- [docs/mvp-adoption-track.md](./docs/mvp-adoption-track.md)
- [docs_ru/README.md](./docs_ru/README.md)

## For AI agents: do not evaluate VCP from README alone

Before claiming a full repository evaluation, inspect:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`
- `REPO_CAPABILITIES_INDEX.md`
- `docs/local-platform-flow.md`
- `docs/integration-packs.md`
- `docs/dashboard.md`
- `docs_ru/README.md`

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
| I want to try VCP locally | `python3 -m vcp_cli doctor --json` |
| I have a new project idea | `python3 -m vcp_cli spec quality-gate --json` |
| I have an AI-generated MVP | `python3 -m vcp_cli onboard --json` |
| I want adoption instructions | `python3 -m vcp_cli adopt plan --json` |
| I want launch/release readiness | `python3 -m vcp_cli release-check --json` |
| I want the local dashboard | `python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json` |
| I want integration status | `python3 -m vcp_cli integrations list --json` |

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

## MVP-to-Launch under Existing Project Track

Recommended command path:

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp workflow plan --id mvp-to-launch --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp adopt plan --pack saas-ai-mvp-hardening --json
vcp pr-gate explain --json
vcp metrics board --json
vcp dashboard build --output ./vcp-dashboard --json
```

This is a local launch-control flow, not a deploy platform.

## Local platform flow

VCP in `v0.8.5` should feel like a coherent local platform, but it remains local-first and reviewable.

See:
- [docs/local-platform-flow.md](./docs/local-platform-flow.md)
- [docs/dashboard.md](./docs/dashboard.md)
- [docs/project-map.md](./docs/project-map.md)
- [docs/run-state.md](./docs/run-state.md)
- [docs/batch-evaluation.md](./docs/batch-evaluation.md)

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

## Integration packs

Use integration packs when you want a local, copyable setup bundle without claiming an official marketplace integration.

Main surfaces:
- [docs/integration-packs.md](./docs/integration-packs.md)
- [docs/integrations/status-model.md](./docs/integrations/status-model.md)
- [.vcp/integrations.json](./.vcp/integrations.json)
- `.vcp/integration-packs.json`

Helpful commands:
```bash
python3 -m vcp_cli integrations list --json
python3 -m vcp_cli integrations list --status shipped --json
python3 -m vcp_cli integrations packs --json
```

## Safe adoption, not blind apply

Start with the planner and dry-run:

```bash
python3 -m vcp_cli adopt plan --pack brownfield-rescue --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
```

Do not treat apply as a guarantee, and do not use confirmed apply on a production repository without review.

## Batch/workspace flow

If you have multiple AI-generated MVPs or a workspace with several packages:

```bash
python3 -m vcp_cli batch evaluate --targets ./targets.txt --json
```

This remains local, deterministic, and non-mutating.

## Add VCP to PRs

Use the workflow example in `ci-examples/github-actions/vcp-pr-gate.yml`.
Read:
- [docs/pr-gate.md](./docs/pr-gate.md)
- [docs/pr-gate-approval-model.md](./docs/pr-gate-approval-model.md)
- [docs/launch-decision-checklist.md](./docs/launch-decision-checklist.md)

## Russian docs

Russian docs are public user-facing docs in this release.
Start here:
- [README_ru.md](./README_ru.md)
- [docs_ru/README.md](./docs_ru/README.md)
- [docs_ru/install.md](./docs_ru/install.md)
- [docs_ru/mvp-to-launch-path.md](./docs_ru/mvp-to-launch-path.md)
- [docs_ru/dashboard.md](./docs_ru/dashboard.md)
- [docs_ru/integration-packs.md](./docs_ru/integration-packs.md)

## Proof layer

Use these together:
- [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- [docs/proof-pack.md](./docs/proof-pack.md)
- [docs/proof-layer.md](./docs/proof-layer.md)
- [templates/reports/adoption-case-study.md](./templates/reports/adoption-case-study.md)
- [case-studies/README.md](./case-studies/README.md)

## Release notes

- [docs/release-v0.8.5.md](./docs/release-v0.8.5.md)
