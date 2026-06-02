# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.5.2-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

VCP is a controlled workflow for AI-assisted software delivery.
When AI helps write code, teams often move faster than their architecture, review, stop conditions, and release discipline can keep up.
VCP helps by classifying the project first, choosing the right route, applying only the needed adoption pack, validating the result, and reviewing changes before they move forward.

Repository package: `v0.5.2`

Web methodology: `Vibe Coding Protocols v1.4`

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
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
npm run vcp -- doctor
```

## Give this to your AI agent

Start with [AI_INTAKE.md](./AI_INTAKE.md), then route through [START_HERE.md](./START_HERE.md). If you need agent rules, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.
If you want a ready onboarding prompt, run `python3 -m vcp_cli init --print-prompt` or use [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md).

## What VCP helps with

- choosing the right route for a real repo instead of defaulting to Starter;
- keeping production, regulated, public-site, maintenance, and API-intake work scoped;
- adopting a small relevant file set instead of copying the whole toolkit;
- validating repo health before merge, release, or deploy;
- adding a review gate after meaningful AI-generated changes.

## Routes

| Situation | Route |
|---|---|
| New project or idea | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated, or shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [Adoption Packs](./docs/adoption-packs.md) |
| Working code that is hard to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| UI styling or component ownership drift | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| External API, SDK, webhook, or SaaS proposal | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Active diff that must be accepted before moving on | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Public docs, marketing site, trust, or crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |

## Adoption Packs

An Adoption Pack is a small recommended file set for a situation.
For example:
- Production Pack = hardening docs + audit backlog + security baseline + review gate.
- Shared Engine Pack = project map + architecture source of truth + cross-product release checks.
- Public Site Pack = `llms.txt` + `robots.txt` + schema.org + site-readiness checklist.

Use [docs/adoption-packs.quickstart.md](./docs/adoption-packs.quickstart.md) if you want the short explanation first.

## What VCP is not

VCP is not a scanner, pentest/offensive toolkit, compliance certification, or replacement for human review. It is a workflow and tooling layer for safer AI-assisted delivery.

## Go deeper

- [docs/cli.md](./docs/cli.md)
- [docs/npm.md](./docs/npm.md)
- [docs/windows.md](./docs/windows.md)
- [docs/init.md](./docs/init.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/roadmap.md](./docs/roadmap.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [docs/measured-impact.md](./docs/measured-impact.md)
- [docs/release-v0.5.2.md](./docs/release-v0.5.2.md)
