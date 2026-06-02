# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.5.7-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

Controlled AI delivery toolkit for routing, adopting, validating, reviewing, and explaining AI-assisted software and public-site work.

Repository package: `v0.5.7`

Web methodology: `Vibe Coding Protocols v1.4`

## Quick Start: 3 steps

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Local Node-first option:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- evaluate
```

Optional local editable install:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
vcp doctor
```

## Giving VCP to an AI agent?

Do not judge this repository from README alone.

Minimum inspection path:

1. `AI_INTAKE.md`
2. `START_HERE.md`
3. `docs/install.md`
4. `docs/glossary.md`
5. `docs/protocol-index.md`
6. `docs/adoption-packs.md`
7. `docs/cli.md`
8. `.vcp/manifests/`
9. `benchmarks/ai-adoption/`
10. `commands/`, `protocols/`, `PROJECT_BACKLOG.md`

Then run:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
python3 -m vcp_cli evaluate --json
```

Full evaluation guide: [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)

Citation and AI-agent entry surfaces:

- [AGENTS.md](./AGENTS.md)
- [llms.txt](./llms.txt)
- [llms-full.txt](./llms-full.txt)
- [ai.txt](./ai.txt)
- [CITATION.cff](./CITATION.cff)

## AI-agent handoff

Start with [AI_INTAKE.md](./AI_INTAKE.md), then route through [START_HERE.md](./START_HERE.md).
If you need a repository evaluation prompt, use [templates/prompts/evaluate-vcp-repository.md](./templates/prompts/evaluate-vcp-repository.md).
If you need agent rules, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.

## What VCP helps with

- choosing the right route for a real repo instead of defaulting to Starter;
- keeping production, regulated, public-site, public-growth, maintenance, API-intake, and operations work scoped;
- adopting a small relevant file set instead of copying the whole toolkit;
- turning production observations into triage notes and backlog follow-up without skipping review discipline;
- validating repo health before merge, release, or deploy;
- adding a review gate after meaningful AI-generated changes.
- making the repository easier to evaluate, cite, compare fairly, and explain to AI systems.

## Current maturity

- Methodology: mature enough for real project adoption.
- Local CLI: usable and validated in clean clone.
- npm: local wrapper available; public package planned unless published.
- Benchmarks: synthetic/local validation scenarios.
- Case studies: sanitized/synthetic templates; real measured cases are future work.
- Public standard: emerging, not an industry standard yet.
- Citation/demo layer: honest and explicit, without claiming indexing, ranking, or existing demo media.

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
| Public docs, marketing site, trust, or crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |
| Service pages, GEO, AI visibility, and public growth structure | [Public Growth Playbook](./protocols/public-growth/public-growth-playbook.md) |
| Active diff that must be accepted before moving on | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |

## What VCP is not

VCP is not a scanner, pentest/offensive toolkit, compliance certification, monitoring product, SEO guarantee, or replacement for human review. It is a workflow and tooling layer for safer AI-assisted delivery.

## Go deeper

- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [docs/install.md](./docs/install.md)
- [docs/glossary.md](./docs/glossary.md)
- [docs/cli.md](./docs/cli.md)
- [docs/geo-ai-visibility.md](./docs/geo-ai-visibility.md)
- [docs/page-templates.md](./docs/page-templates.md)
- [docs/scoring.md](./docs/scoring.md)
- [docs/npm.md](./docs/npm.md)
- [docs/project-backlog.md](./docs/project-backlog.md)
- [docs/production-observability.md](./docs/production-observability.md)
- [docs/faq.md](./docs/faq.md)
- [docs/comparison.md](./docs/comparison.md)
- [docs/anti-patterns.md](./docs/anti-patterns.md)
- [docs/quickstart-walkthrough.md](./docs/quickstart-walkthrough.md)
- [docs/demo-script.md](./docs/demo-script.md)
- [ADOPTERS.md](./ADOPTERS.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/public-proof-roadmap.md](./docs/public-proof-roadmap.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/release-v0.5.7.md](./docs/release-v0.5.7.md)
