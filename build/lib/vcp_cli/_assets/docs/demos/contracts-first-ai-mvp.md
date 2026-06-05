# Contracts-first AI-MVP Demo

This is a specialized scenario inside the MVP-to-Launch Path when web/backend/contracts inspection matters.

## Target project shape

```text
raw-ai-mvp/
  apps/web/
  apps/api/
  packages/contracts/
  README.md
  .env.example
```

## Command path

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli release-check --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

## What VCP checks

- visible route and track;
- contracts risk and ownership;
- safe adoption copy-list;
- PR Gate and release readiness surfaces;
- local dashboard artifact for inspection.
- launch-decision inputs after contracts risk is visible.

## Contracts risk checklist

- shared contracts versioning;
- frontend/backend mismatch risk;
- environment variables;
- auth or billing boundaries;
- unreviewed generated API code.

## Boundaries

- not a guarantee of launch safety;
- not a contract test runner;
- not a hosted control plane.

## Continue with

- `docs/mvp-to-launch-path.md`
- `docs/launch-decision-checklist.md`
- `docs/adoption-packs/saas-ai-mvp-hardening.md`
