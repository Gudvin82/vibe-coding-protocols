# Killer Workflow

Repository package: `v0.8.6`

## One-minute explanation

VCP turns a raw AI MVP into a reviewable launch-control package: route, risk, plan, PR Gate, metrics, dashboard, and launch decision.

## Scenario

You have a small, messy AI-generated MVP and want to know:
- whether it is demoable;
- what risks remain;
- what the next launch-control actions should be.

## Inputs

- an existing repository or cloned project;
- an AI-generated MVP or partially governed codebase;
- no hosted platform assumptions.

## Commands

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp workflow plan --id mvp-to-launch --json
vcp adopt plan --pack saas-ai-mvp-hardening --json
vcp pr-gate explain --json
vcp metrics board --json
vcp dashboard build --output ./vcp-dashboard --json
```

Fallback from a cloned repo:

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli workflow plan --id mvp-to-launch --json
python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json
python3 -m vcp_cli pr-gate explain --json
python3 -m vcp_cli metrics board --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

## Expected outputs

- route and project classification;
- adoption plan;
- PR Gate explanation;
- metrics board summary;
- local dashboard artifact;
- launch-control references for proof, backlog, and checklist surfaces.

## How to interpret results

- `doctor`: confirms local repository/runtime health.
- `onboard` + `classify`: show which track and path fit best.
- `workflow plan`: turns the situation into a guided path.
- `adopt plan`: explains what to copy or govern next.
- `pr-gate explain`: shows warn/block logic before launch.
- `metrics board`: gives a compact review surface.
- `dashboard build`: turns the state into a reviewable local artifact.

## Stop conditions

Stop and review before broader adoption when:
- the route is unclear;
- PR Gate warns about unresolved blockers;
- the MVP still lacks launch decision clarity;
- you are tempted to treat the dashboard as a hosted control plane.

## Next actions

- inspect `docs/launch-decision-checklist.md`;
- review `docs/proof-layer.md` and `docs/audit-backlog.md`;
- use `docs/comparisons.md` if the team needs positioning clarity.

## What VCP does not do

VCP does not:
- deploy the product;
- host a dashboard;
- certify production safety;
- replace engineering review.
