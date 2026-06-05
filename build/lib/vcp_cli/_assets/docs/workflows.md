# Workflows

Repository package: `v0.8.4`

VCP workflow JSON files are machine-readable planning and governance artifacts.
They are **not** an execution engine.

## What workflow JSON is for

- capture trigger -> route -> steps -> validation -> stop conditions;
- keep repeated AI delivery flows visible to humans, CLI, and CI;
- help AI agents plan without pretending the repo can execute production actions.

## Practical CLI surface

```bash
python3 -m vcp_cli workflow list --json
python3 -m vcp_cli workflow validate --json
python3 -m vcp_cli workflow plan --json
python3 -m vcp_cli workflow plan --id mvp-to-launch --json
python3 -m vcp_cli workflow run --id production-hardening --interactive --dry-run --json
```

`workflow plan` is still the default non-executing surface.

`workflow run --interactive` in `v0.8.4` is a safe runner/planner:
- requires `--interactive`;
- supports `--dry-run`;
- previews only safe local VCP steps;
- does not deploy;
- does not publish;
- does not modify files;
- does not access secrets.

Workflow JSON still does not become a hidden automation engine.

## MVP-to-Launch workflow

`mvp-to-launch` is a planning-only workflow for a raw or semi-working AI-generated MVP that needs launch control.

It covers:
- `intake`
- `classify`
- `surface-scan`
- `adoption-plan`
- `risk-backlog`
- `proof-check`
- `pr-gate-approval`
- `dashboard-build`
- `launch-decision`

See:
- `.vcp/workflows/mvp-to-launch.json`
- `docs/mvp-to-launch-path.md`
- `docs/launch-decision-checklist.md`
