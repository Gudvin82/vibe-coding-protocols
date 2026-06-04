# Local Dashboard Artifact

`v0.8.2` ships a local dashboard artifact path.
It does not ship a hosted dashboard.

## What it is

The dashboard command generates local static artifacts from data already present in the repository.
Its purpose is review, demos, and local project status inspection.

```bash
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

Generated files include:
- `index.html`
- `dashboard.md`
- `metrics.json`
- `audit-backlog-summary.json`
- `release-readiness.json`
- `integration-status.json`

## Boundaries

The dashboard is:
- local-only;
- deterministic;
- based on existing repository data;
- safe for demos and review.

The dashboard is not:
- a hosted dashboard;
- a SaaS;
- a control plane;
- a telemetry pipeline;
- a guarantee of project safety or launch readiness.

## Intended uses

Use it when you want to:
- demo VCP in one local artifact;
- inspect release-readiness and backlog shape quickly;
- show integration status without pretending hosted infrastructure exists;
- export conservative local status artifacts for a review thread.
