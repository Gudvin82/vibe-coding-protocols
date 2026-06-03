# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.6.1-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![Workflow](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Windows CLI](https://img.shields.io/badge/Windows-CLI-blue)](./docs/windows.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./.vcp/manifests/vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/security-defensive_only-success)](./docs/security-tooling-landscape.md)

Build with AI. Ship with control.

Vibe Coding Protocols helps you build AI-assisted products from idea to production without losing control: it routes the work, chooses the right spec depth, keeps project memory, checks AI-generated changes, manages backlog, runs review gates, and prepares releases.

Repository package: `v0.6.1`

Web methodology: `Vibe Coding Protocols v1.4`

## Quick Start

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Node-first local option:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- evaluate
```

## Two ways to use VCP

### Build from scratch

Use VCP to turn an idea into a controlled AI-assisted product:
idea -> spec depth -> PRD / feature spec -> tasks -> backlog -> architecture memory -> implementation -> review -> release.

### Stabilize an existing project

Use VCP to harden and govern an existing AI-generated project:
intake -> diagnostics -> hardening -> review gates -> backlog -> release readiness -> operations feedback.

## Three flagship workflows

1. [Build an AI-assisted product from idea](./docs/flagship-workflows.md)
2. [Harden an AI-generated MVP](./docs/flagship-workflows.md)
3. [Review ongoing AI-driven changes](./docs/flagship-workflows.md)

## Product delivery lifecycle

See [docs/product-delivery-lifecycle.md](./docs/product-delivery-lifecycle.md) for:
- minimum path;
- full path;
- skip path;
- stage-by-stage commands, outputs, and stop conditions.

## VCP score badge

Projects can publish a local VCP readiness badge after running checks:

```bash
python3 -m vcp_cli score --badge markdown
```

The badge is not a security certification. It is a visible local readiness signal.

## Giving VCP to an AI agent?

Do not judge this repository from README alone.

Minimum inspection path:

1. `AGENTS.md`
2. `AI_EVALUATION_GUIDE.md`
3. `AI_INTAKE.md`
4. `START_HERE.md`
5. `.vcp/index.json`
6. `.vcp/cards/`
7. `docs/product-delivery-lifecycle.md`
8. `docs/flagship-workflows.md`
9. `docs/protocol-index.md`
10. `docs/adoption-packs.md`
11. `docs/cli.md`
12. `.vcp/manifests/`
13. `benchmarks/ai-adoption/`
14. `PROJECT_BACKLOG.md`

Then run:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
python3 -m vcp_cli evaluate --json
```

Full evaluation guide: [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)

If you need repo-level agent rules, use root `AGENTS.md`.
If you need a reusable project template, use [templates/AGENTS.md](./templates/AGENTS.md).

## What VCP helps with

- choosing the right route instead of treating every AI task the same way;
- deciding between no-spec, spec-lite, full-spec, and governed-spec;
- turning ideas into PRD/spec/tasks without forcing full process on tiny fixes;
- keeping backlog, architecture memory, and release notes in sync;
- checking active diffs before merge with `review-diff` and review gates;
- validating repository health through manifests, cards, benchmarks, diagnostics, and workflows;
- documenting public-growth and platform usage without claiming official integrations.

## When VCP is too much

- toy project;
- one-off script;
- pure copy edit;
- no production or public use;
- pure exploration;
- user does not want process yet.

## Current maturity

- Methodology: strong enough for real adoption.
- Local CLI: usable and validated in clean clone.
- npm: local wrapper available; public package is future work unless published.
- Benchmarks: local/synthetic validation scenarios.
- Case studies: mixed real, sanitized, synthetic, and template layers with clear labels.
- Public standard: still emerging.

## Routes

| Situation | Route |
|---|---|
| New project or idea | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated, or shared-engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [Adoption Packs](./docs/adoption-packs.md) |
| Working code that is hard to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| External API, SDK, webhook, or SaaS proposal | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Public docs, marketing site, trust, or crawler readiness | [Public Site Readiness](./docs/public-site-readiness.md) |
| Idea is still fuzzy and needs PRD / feature spec / acceptance criteria first | [Spec-first Feature](./protocols/spec-driven/README.md) |
| Active diff that must be accepted before merge or release | [Review Diff](./docs/review-diff.md) + [Post-Task Code Review](./protocols/review/post-task-code-review.md) |

## What VCP is not

VCP is not a scanner, pentest toolkit, compliance certification, SEO guarantee, or replacement for human review. It is a workflow and trust layer for safer AI-assisted delivery.

## Go deeper

- [AI_EVALUATION_GUIDE.md](./AI_EVALUATION_GUIDE.md)
- [docs/product-delivery-lifecycle.md](./docs/product-delivery-lifecycle.md)
- [docs/flagship-workflows.md](./docs/flagship-workflows.md)
- [docs/review-diff.md](./docs/review-diff.md)
- [docs/score-badge.md](./docs/score-badge.md)
- [docs/github-action.md](./docs/github-action.md)
- [docs/integrations/spec-kit-bridge.md](./docs/integrations/spec-kit-bridge.md)
- [docs/platforms/README.md](./docs/platforms/README.md)
- [docs/faq.md](./docs/faq.md)
- [docs/comparison.md](./docs/comparison.md)
- [docs/anti-patterns.md](./docs/anti-patterns.md)
- [docs/public-proof-roadmap.md](./docs/public-proof-roadmap.md)
- [case-studies/README.md](./case-studies/README.md)
- [ADOPTERS.md](./ADOPTERS.md)
