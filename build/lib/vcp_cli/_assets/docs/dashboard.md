# Local Dashboard Artifact

The VCP dashboard is a local artifact, not a hosted dashboard.

## Command

```bash
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

## What it shows

- repository package and methodology;
- track model and MVP-to-Launch path link;
- workflow id and recommended command flow;
- selected route and pack if detectable;
- brownfield-rescue and saas-ai-mvp-hardening suggestions;
- launch decision checklist link;
- contracts-first demo link;
- 10-minute path links;
- MVP and spec-driven adoption links;
- integration status summary;
- PR Gate approval model links;
- audit backlog summary;
- project memory summary if present;
- run history summary if present;
- proof layer links;
- proof layer status if inferable;
- known limitations.

## Boundaries

- local artifact only;
- no hosted server;
- no auth;
- no telemetry;
- no cloud sync;
- no launch guarantee.
