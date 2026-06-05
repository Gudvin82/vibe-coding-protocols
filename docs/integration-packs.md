# Integration Packs

Integration packs are local, copyable, documented setup bundles.
They are not official third-party integrations, marketplace installs, or hosted services.

## Status model

Allowed statuses:
- `shipped`
- `local-template`
- `experimental`
- `roadmap`
- `not-shipped`

See also:
- [integrations status model](./integrations/status-model.md)
- `.vcp/integrations.json`
- `.vcp/integration-packs.json`

## Current packs

1. GitHub Actions PR Gate Pack
   - status: `local-template`
   - file: `ci-examples/github-actions/vcp-pr-gate.yml`
   - docs: `docs/pr-gate.md`

2. Agent Instructions Pack
   - status: `shipped`
   - files: `templates/agents/*.md`
   - local copy only

3. Dashboard Artifact Pack
   - status: `shipped`
   - command: `vcp dashboard build --output ./vcp-dashboard --json`
   - static local artifacts only

4. Docs Site Scaffold Pack
   - status: `experimental`
   - files: `docs-site/README.md`
   - optional scaffold, not required for CLI

5. SaaS AI-MVP Hardening Pack
   - status: `shipped`
   - docs: `docs/adoption-packs/saas-ai-mvp-hardening.md`
   - not a hosted SaaS app template

6. Contracts-first AI-MVP Pack
   - status: `local-template`
   - docs: `docs/demos/contracts-first-ai-mvp.md`
   - local path/template guidance only

7. Future IDE Pack
   - status: `roadmap`
   - docs: `docs/roadmap/vscode-extension.md`
   - no extension shipped

8. PyPI Readiness Pack
   - status: `local-template`
   - docs: `docs/pypi-publishing.md`
   - readiness only, not public publication

## CLI

```bash
python3 -m vcp_cli integrations list --json
python3 -m vcp_cli integrations list --status shipped --json
python3 -m vcp_cli integrations packs --json
```

## Boundaries

Do not claim:
- official marketplace support;
- remote plugin registry;
- hosted dashboard;
- public PyPI/npm publication unless actually published;
- official IDE extension.
