# CLI

VCP has practical local entrypaths:
- the Python CLI;
- the installed `vcp` console command after local package install;
- a thin local npm wrapper for Node-first usage.

It does not claim public PyPI or public npm publication unless those packages are actually released.

## Install and run

```bash
python3 -m pip install .
vcp doctor
vcp evaluate --json
```

## Productized starting commands

```bash
vcp onboard --json
vcp classify --json
vcp adopt plan --json
vcp adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
vcp release-check --json
vcp public-growth check --json
```

## Main command surfaces

- `onboard` — first practical next-step guide
- `classify` — classify repo, track, risk, tier, and route
- `adopt plan` — safe copy-list / patch preview planner
- `adopt apply` — explicit safe apply with `--target`, `--confirm`, dry-run, conflicts, and adoption log
- `spec quality-gate` — new-project entry check
- `diagnose` — existing-repo readiness by layer
- `review-diff` — pre-merge risk helper
- `release-check` — release surface quick check
- `public-growth check` — public-growth readiness check
- `workflow plan` — planning view for workflow JSON
- `workflow run --interactive --dry-run` — safe preview-only workflow runner
- `score` — local readiness signal

## Safety boundaries

The CLI:
- does not call external AI APIs;
- does not auto-apply adoption packs silently;
- does not silently write into another project;
- does not overwrite existing files by default in `adopt apply`;
- does not claim workflow JSON is an execution engine.
