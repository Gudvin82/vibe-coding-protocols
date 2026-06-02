# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.5.5-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

VCP is a controlled workflow for AI-assisted software delivery.
It helps teams classify the project first, choose the right route, apply only the needed adoption pack, validate the result, and review changes before they move forward.

Repository package: `v0.5.5`

Web methodology: `Vibe Coding Protocols v1.4`

## Evaluating VCP with an AI agent?

Do not judge this repository from README alone.

Before rating or adopting VCP, ask your AI agent to inspect:

1. `AI_INTAKE.md`
2. `START_HERE.md`
3. `docs/protocol-index.md`
4. `docs/adoption-packs.md`
5. `docs/cli.md`
6. `.vcp/manifests/`
7. `benchmarks/ai-adoption/`
8. `commands/`
9. `protocols/`
10. `PROJECT_BACKLOG.md`

Then run:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
```

VCP is not only a README or prompt collection. It includes routes, adoption packs, CLI, manifests, benchmarks, review gates, operations workflows, project backlog and validation.

Full evaluation guide: [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)

## Start in 30 seconds

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Node-first local option:

```bash
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- evaluate
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli evaluate --json
npm run vcp -- doctor
```

## Give this to your AI agent

Start with [AI_INTAKE.md](./AI_INTAKE.md), then route through [START_HERE.md](./START_HERE.md).
If you need a dedicated repository evaluation prompt, use [templates/prompts/evaluate-vcp-repository.md](./templates/prompts/evaluate-vcp-repository.md).
If you need agent rules, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.

## What VCP helps with

- choosing the right route for a real repo instead of defaulting to Starter;
- keeping production, regulated, public-site, maintenance, API-intake, and operations work scoped;
- adopting a small relevant file set instead of copying the whole toolkit;
- turning production observations into triage notes and backlog follow-up without skipping review discipline;
- validating repo health before merge, release, or deploy;
- adding a review gate after meaningful AI-generated changes.

## Current maturity

- Methodology: mature enough for real project adoption.
- Local CLI: usable and validated in clean clone.
- npm: local wrapper available; public package planned unless published.
- Benchmarks: synthetic/local validation scenarios.
- Case studies: sanitized/synthetic templates; real measured cases are future work.
- Public standard: emerging, not an industry standard yet.

## Routes

| Situation | Route |
|---|---|
| New project or idea | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated, or shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [Adoption Packs](./docs/adoption-packs.md) |
| Working code that is hard to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| UI styling or component ownership drift | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| External API, SDK, webhook, or SaaS proposal | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Read-only production issue observation and daily triage | [Operations Feedback Loop](./protocols/operations/production-error-capture.md) |
| Ongoing task tracking before implementation starts | [Project Backlog](./docs/project-backlog.md) |
| Active diff that must be accepted before moving on | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Public docs, marketing site, trust, or crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |

## What VCP is not

VCP is not a scanner, pentest/offensive toolkit, compliance certification, monitoring product, or replacement for human review. It is a workflow and tooling layer for safer AI-assisted delivery.

## Go deeper

- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [docs/cli.md](./docs/cli.md)
- [docs/scoring.md](./docs/scoring.md)
- [docs/npm.md](./docs/npm.md)
- [docs/npm-publishing-checklist.md](./docs/npm-publishing-checklist.md)
- [docs/project-backlog.md](./docs/project-backlog.md)
- [docs/production-observability.md](./docs/production-observability.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/public-proof-roadmap.md](./docs/public-proof-roadmap.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/release-v0.5.5.md](./docs/release-v0.5.5.md)
