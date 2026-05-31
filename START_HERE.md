# Start Here

Use this file as the canonical route chooser.

If an AI agent is evaluating VCP for an existing repository,
start with [AI_INTAKE.md](./AI_INTAKE.md).
If agent rules are needed, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.

## Main routes

- Starter — new project
- Hardening — existing AI-generated code
- Maintenance Refactoring — working code that is hard to change
- UI Component Ownership — frontend ownership cleanup
- Third-party API Intake — external API or SDK dependency review before implementation
- Post-Task Code Review — acceptance gate for active changes
- Extended / Full Hardening — production, regulated or shared-engine risk
- Public Site Readiness — public docs, trust and crawler readiness

## Quick table

| Situation | Route | First action |
|---|---|---|
| Idea only | Starter | Product Brief + PROJECT_MAP |
| Existing MVP | Hardening | Risk map and dependency review |
| Production or regulated repo | Full Hardening | Security Review Scope + release gate |
| Shared engine across products | Shared Engine Pack + Full Hardening | Create PROJECT_MAP and Architecture Source of Truth |
| Code works but is messy | Maintenance Refactoring | Narrow one safe refactor slice |
| UI styling drift | UI Ownership | Pick one component ownership slice |
| New external API, SDK or webhook | Third-party API Intake | Classify auth, data flow, terms and fallback before code |
| Active diff needs acceptance | Post-Task Code Review | Inspect git status, diff and validation |
| Public docs/site work | Public Site Readiness | Check publishing and trust checklist |

## Rule after meaningful AI changes

After meaningful AI-generated code changes,
run Post-Task Code Review before the next feature,
merge,
release,
deploy,
tag
or handoff.

## CLI shortcuts

```bash
python3 -m vcp_cli route --profile shared-engine
python3 -m vcp_cli route --profile third-party-api
python3 -m vcp_cli adopt --pack third-party-api --dry-run
python3 -m vcp_cli review plan
```
