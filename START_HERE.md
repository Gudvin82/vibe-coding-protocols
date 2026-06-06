# Start Here

Use this file to choose the correct VCP path before copying artifacts or writing code.

## VCP in 60 seconds

VCP is a local-first control layer for AI-built and AI-assisted projects.

It helps teams:
- choose the right route before AI edits expand;
- define intent and control boundaries;
- add PR Gate, proof, trust-check, and release evidence;
- avoid pretending a local toolkit is a hosted platform.

## Fast path

If you want the shortest honest start:

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli catalog list --json
python3 -m vcp_cli trust-check --json
```

If you are evaluating the repository itself:

```bash
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli evaluator pack --json
python3 -m vcp_cli benchmark run --json
python3 -m vcp_cli trust-check --json
```

Node wrapper from this same repo:

```bash
npm run vcp -- doctor
npm run vcp -- evaluate
```

## Route selector

| If this is your situation | Start here |
|---|---|
| I am brand new to VCP | [docs/first-time-adoption.md](./docs/first-time-adoption.md) |
| I need the product spine first | [docs/product-spine.md](./docs/product-spine.md) |
| I want the core control chain | [docs/control-spine.md](./docs/control-spine.md) |
| I already have an AI-built MVP and need control before release | [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md) |
| I want the fastest end-to-end walkthrough | [docs/flagship-demo.md](./docs/flagship-demo.md) |
| I need to know which surfaces matter first | [docs/surface-priority-model.md](./docs/surface-priority-model.md) |
| I need a copyable local governance starter | [docs/portable-control-pack.md](./docs/portable-control-pack.md) |
| I need the work unit / review / release chain | [docs/work-package-lifecycle.md](./docs/work-package-lifecycle.md) |
| I am evaluating VCP itself | [PUBLIC_EVALUATION_KIT.md](./PUBLIC_EVALUATION_KIT.md) |
| I want the classic route chooser | [AI_INTAKE.md](./AI_INTAKE.md) |

## Required / recommended / optional

Required first:
- `README.md`
- `docs/first-time-adoption.md`
- `docs/control-spine.md`
- `docs/scope-boundary.md`
- `python3 -m vcp_cli trust-check --json`

Recommended next:
- `docs/flagship-demo.md`
- `docs/control-catalog.md`
- `docs/adaptive-rigor-modes.md`
- `PUBLIC_EVALUATION_KIT.md`

When you adopt VCP into another repo, do not copy root `AGENTS.md` blindly.
Prefer `templates/AGENTS.md` or the more specific agent templates first.

Optional layers:
- dashboard artifact
- docs-site scaffold
- presentations destination
- public proof demo

Roadmap-only, not shipped:
- hosted dashboard
- marketplace
- cloud sync
- autonomous orchestration
