# Local Dashboard Artifact

The VCP dashboard is a local dashboard artifact, not a hosted dashboard.

## Command

```bash
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

## Required generated artifacts

- `index.html`
- `README.md`
- `dashboard.md`
- `metrics.json`
- `integration-status.json`
- `audit-backlog-summary.json`
- `project-map.json`
- `run-history.json`
- `launch-readiness.json`
- `release-readiness.json`

## Sections

1. current package version and methodology;
2. core story;
3. track model;
4. quick start / 10-minute path;
5. MVP-to-Launch flow;
6. current project map;
7. run history / checkpoints;
8. audit backlog;
9. proof layer;
10. PR Gate approval model;
11. integration status;
12. agent control / safety boundary;
13. Russian docs link;
14. limitations and non-goals.

## Boundaries

- local artifact only;
- no hosted server;
- no auth;
- no telemetry;
- no cloud sync;
- no remote registry;
- no production certification.
