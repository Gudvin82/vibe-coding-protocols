# Adoption Packs

An Adoption Pack is a small recommended file set for a situation.
It is not a command to copy the whole toolkit.
It is a scoped recommendation for humans and AI agents.

## Quick examples

- Production Pack = hardening docs + audit backlog + security baseline + review gate.
- Shared Engine Pack = project map + architecture source of truth + cross-product release checks.
- Public Site Pack = `llms.txt` + `robots.txt` + schema.org + site-readiness checklist.
- Third-party API Pack = API intake protocol + registry + intake report + review gate.

## Packs

| Pack | Use when | Review gate |
|---|---|---|
| `new-project` | new project or idea stage | recommended for meaningful changes |
| `existing-mvp` | working MVP before production | run before merge |
| `production` | real users or public production | required before merge or release |
| `regulated` | payments, personal data or compliance | required with independent review |
| `shared-engine` | one engine powers multiple products | required for cross-product regression risk |
| `maintenance` | working code is hard to change | required after refactoring slice |
| `ui-ownership` | pages own final component appearance | required after ownership cleanup |
| `third-party-api` | an external API, SDK, webhook, or SaaS integration is being proposed | required before production integration merge or release |
| `public-site` | public docs or marketing surfaces | lighter review for meaningful changes |
| `post-task-review` | active diff needs acceptance | this pack is the gate itself |

## Dry-run first

```bash
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json
npm run vcp -- adopt --pack production --dry-run
```

Use dry-run to see:
- files to copy;
- files to merge manually;
- protected files to avoid overwriting;
- review-gate requirement;
- validation commands.

## Protected files

Do not overwrite blindly:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_MAP.md`
- `SECURITY.md`
- `.env`
- package files
- CI files
- project-specific architecture docs

## Machine-readable catalog

The CLI reads pack metadata from:
- [../.vcp/manifests/adoption-packs.manifest.json](../.vcp/manifests/adoption-packs.manifest.json)

## Related docs

- [adoption-packs.quickstart.md](./adoption-packs.quickstart.md)
- [../AI_INTAKE.md](../AI_INTAKE.md)
- [../START_HERE.md](../START_HERE.md)
