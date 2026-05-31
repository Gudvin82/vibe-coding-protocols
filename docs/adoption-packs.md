# Adoption Packs

Adoption packs help humans and AI agents choose the right VCP file set for a target repository.

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
| `third-party-api` | an external API, SDK or webhook is being proposed | required before production integration merge or release |
| `public-site` | public docs or marketing surfaces | lighter review for meaningful changes |
| `post-task-review` | active diff needs acceptance | this pack is the gate itself |

## Third-party API safety

Use `third-party-api` when a feature proposal depends on an external API.
Do not write integration code first.
Classify the provider, auth, data flow, terms, rate limits and fallback before implementation.

## Use the CLI

```bash
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json
python3 -m vcp_cli route --profile third-party-api --json
```

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

See also [../adoption-packs.manifest.json](../adoption-packs.manifest.json).
