# CLI

VCP has practical local entrypaths:
- the Python CLI, which remains the main implementation;
- a thin local npm wrapper for Node-first usage.

It does not claim public PyPI or public npm publication unless those packages are actually released.

## Productized starting commands

```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --json
python3 -m vcp_cli release-check --json
python3 -m vcp_cli public-growth check --json
```

## Main command surfaces

- `onboard` — first practical next-step guide
- `classify` — classify repo, track, risk, tier, and route
- `adopt plan` — safe copy-list / patch preview planner
- `spec quality-gate` — new-project entry check
- `diagnose` — existing-repo readiness by layer
- `review-diff` — pre-merge risk helper
- `release-check` — release surface quick check
- `public-growth check` — public-growth readiness check
- `workflow plan` — planning view for workflow JSON
- `score` — local readiness signal

## Safety boundaries

The CLI:
- does not call external AI APIs;
- does not auto-apply adoption packs;
- does not silently write into another project;
- does not claim workflow JSON is an execution engine.
