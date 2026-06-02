# Start Here

Use this file to choose the correct VCP route before copying artifacts or writing code.

## Fast path

If you want the shortest guided start:

```bash
python3 -m vcp_cli init
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Node-first local option:

```bash
npm run vcp -- init
npm run vcp -- route --profile production
```

## Route chooser

| If this is your situation | Start here |
|---|---|
| I am starting a new project | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| I already have an AI-generated project and need production readiness or security work | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| The project already works but is getting risky or messy to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| The main problem is frontend styling or component ownership drift | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| A feature depends on an external API, SDK, webhook, or SaaS | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| I need a read-only production error capture loop and daily triage | [Operations Feedback Loop](./protocols/operations/production-error-capture.md) |
| I need a shared project kanban before implementation starts | [Project Backlog](./docs/project-backlog.md) |
| The active diff needs acceptance before merge or release | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| The main surface is a public docs/marketing site | [Public Site Readiness](./docs/public-site-readiness.md) |
| I am not sure yet | [AI_INTAKE.md](./AI_INTAKE.md) |

## Adoption Packs

After route selection, use an Adoption Pack dry-run instead of copying everything blindly. If you need agent rules, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.
Start with [docs/adoption-packs.quickstart.md](./docs/adoption-packs.quickstart.md).
