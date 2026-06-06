# First-Time Adoption

<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

## VCP in 60 seconds

VCP is a local-first control layer for AI-built projects.

Use it when:
- AI made an MVP and you need to harden it;
- requirements are fuzzy;
- architecture drift started;
- you need PR Gates, audit backlog, release readiness, and proof;
- you want AI agents to follow a controlled workflow.

Start:
1. Read `START_HERE.md`
2. Run `python3 -m vcp_cli trust-check --json`
3. Choose a path: new / existing / MVP-to-Launch / launch / deep hardening
4. Open the Control Catalog
5. Run the flagship demo

## What is required first

Required:
- `START_HERE.md`
- `docs/control-spine.md`
- `docs/surface-priority-model.md`
- `docs/scope-boundary.md`
- `python3 -m vcp_cli trust-check --json`

Recommended:
- `docs/flagship-demo.md`
- `docs/control-catalog.md`
- `docs/adaptive-rigor-modes.md`

Optional:
- dashboard artifact
- public proof demo
- case studies

Advanced:
- evaluator receipt
- full benchmark run
- delivery graph
- work package lifecycle

Roadmap-only:
- hosted dashboard
- marketplace
- cloud sync
- autonomous orchestration

## Do not start by reading everything

Do not start by reading the entire repository. Use the route selector, control catalog, and token-budgeted evaluator path.

## Fast route

1. Read `START_HERE.md`
2. Run `python3 -m vcp_cli onboard --json`
3. Run `python3 -m vcp_cli catalog list --json`
4. Run `python3 -m vcp_cli workflow plan --id mvp-to-launch --json` if you already have an MVP
5. Run `python3 -m vcp_cli trust-check --json` before calling anything release-ready
