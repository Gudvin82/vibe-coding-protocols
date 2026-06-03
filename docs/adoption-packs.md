# Adoption Packs

An Adoption Pack is a small recommended file set for one situation.
It is not a command to copy the whole toolkit.
It is a scoped recommendation for humans and AI agents.

## Quick examples

- Production Pack = hardening docs + audit backlog + security baseline + review gate.
- Shared Engine Pack = project map + architecture source of truth + cross-product release checks.
- Public Site Pack = `llms.txt` + `robots.txt` + schema.org + site-readiness checklist.
- Public Growth Pack = page brief + page templates + GEO/AI visibility guidance + schema honesty checks.
- Spec-first Pack = PRD + feature spec + acceptance criteria + tasks + spec review before coding.
- Third-party API Pack = API intake protocol + registry + intake report + review gate.
- Operations Pack = read-only capture workflow + daily triage + observability boundaries + backlog follow-up.
- Backlog Pack = `PROJECT_BACKLOG.md` + update prompt + backlog report + review trigger.

## Packs

| Pack | Use when | Review gate |
|---|---|---|
| `new-project` | new project or idea stage | recommended for meaningful changes |
| `spec-first` | requirements are unclear and the feature needs PRD / feature spec / acceptance criteria first | recommended before implementation; required once the feature turns into meaningful code work |
| `existing-mvp` | working MVP before production | run before merge |
| `production` | real users or public production | required before merge or release |
| `regulated` | payments, personal data or compliance | required with independent review |
| `shared-engine` | one engine powers multiple products | required for cross-product regression risk |
| `maintenance` | working code is hard to change | required after refactoring slice |
| `ui-ownership` | pages own final component appearance | required after ownership cleanup |
| `third-party-api` | an external API, SDK, webhook, or SaaS integration is being proposed | required before production integration merge or release |
| `operations` | production observations must be captured and triaged without mutation | required only when follow-up becomes code work |
| `backlog` | ongoing delivery work needs one shared kanban/backlog | required once meaningful implementation starts |
| `public-site` | public docs or marketing surfaces | lighter review for meaningful changes |
| `public-growth` | public-facing growth pages, SEO/GEO, AI visibility, or content structure work | recommended for meaningful page changes; required when trust or commercial claims change |
| `post-task-review` | active diff needs acceptance | this pack is the gate itself |

## Dry-run first

```bash
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli adopt --pack spec-first --dry-run --json
python3 -m vcp_cli adopt --pack public-growth --dry-run --json
python3 -m vcp_cli adopt --pack operations --dry-run --json
python3 -m vcp_cli adopt --pack backlog --dry-run --json
npm run vcp -- adopt --pack public-growth --dry-run
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
- [project-backlog.md](./project-backlog.md)
- [../protocols/spec-driven/README.md](../protocols/spec-driven/README.md)
- [production-observability.md](./production-observability.md)
- [geo-ai-visibility.md](./geo-ai-visibility.md)
- [page-templates.md](./page-templates.md)
- [../AI_INTAKE.md](../AI_INTAKE.md)
- [../START_HERE.md](../START_HERE.md)
