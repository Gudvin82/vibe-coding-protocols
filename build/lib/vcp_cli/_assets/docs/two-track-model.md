# Two-Track Model

Vibe Coding Protocols is designed around two core AI-assisted delivery tracks.

Short positioning:

`Build with AI. Ship with control.`

Core positioning:

`VCP helps build AI-assisted products from idea to production without losing control.`

## Core tracks

1. New Project Track
2. Existing Project Track

## Specialized guided paths

- MVP-to-Launch Path, under Existing Project Track
- Spec-driven Adoption Path, usually under New Project Track or early Existing Project Track depending context

## Track A - New Project Track

Flow:

```text
idea -> AI intake -> spec depth -> question engine -> product brief / PRD -> feature spec -> acceptance criteria -> tasks -> PROJECT_BACKLOG -> PROJECT_MAP -> ARCHITECTURE_SOURCE_OF_TRUTH -> implementation -> review gate -> release
```

Use when:

- new product;
- new feature platform;
- founder idea;
- greenfield MVP;
- product concept needs clarification;
- user wants to build with AI without losing control.

Short explanation:

New Project Track is for idea, spec, planning, and controlled implementation before substantial coding expands.

Main artifacts:

- `AI_INTAKE.md`
- `PRODUCT_BRIEF.md`
- `PRD.md`
- `FEATURE_SPEC.md`
- `ACCEPTANCE_CRITERIA.md`
- `TASKS.md`
- `PROJECT_BACKLOG.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- review reports.

## Track B - Existing Project Track

Flow:

```text
existing repo -> AI intake -> diagnose -> hardening route -> architecture drift check -> audit backlog -> review-diff -> PR Gate -> score -> release readiness -> operations/public growth
```

Use when:

- AI-generated MVP already exists;
- production readiness is unclear;
- project has architecture drift;
- backlog exists only in chat;
- third-party integrations were added without review;
- release is near;
- team needs governance before merge or production.

Main artifacts:

- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `AUDIT_BACKLOG.md`
- `PROJECT_BACKLOG.md`
- `THIRD_PARTY_REGISTRY.md`, when applicable;
- `review-diff` report;
- diagnostics report;
- release readiness report;
- PR Gate output.

Short explanation:

Existing Project Track is for a repo that already exists and now needs evaluation, adoption, hardening, review, release control, or launch clarity.

## MVP-to-Launch Path inside Existing Project Track

MVP-to-Launch is a specialized guided path for raw or semi-working AI-generated MVPs that already exist but are not yet launch-controlled.

Use it when the real question is:

- can I show this safely;
- can I route this before expanding it;
- what risks remain before PR, release, or launch;
- what is the smallest visible control layer I should adopt first.

Primary docs:

- `docs/mvp-to-launch-path.md`
- `docs/launch-decision-checklist.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/adoption-packs/saas-ai-mvp-hardening.md`
- `docs/demos/contracts-first-ai-mvp.md`

## Decision table

| User situation | Recommended path |
|---|---|
| I have only an idea/spec | New Project Track |
| I have an existing repo/product | Existing Project Track |
| I have an AI-built MVP and want to know if I can show/launch it | MVP-to-Launch Path |
| I need spec/plan/tasks before coding | Spec-driven Adoption Path |
| I need to harden an AI SaaS MVP | SaaS AI-MVP Hardening Pack |
| I need web/backend/contracts inspection | Contracts-first AI-MVP Demo/Path |

## How tracks combine

- A new project can start in the New Project Track and later move into Existing Project control once the repository and release pressure are real.
- An existing project can still need spec retrofit, question-engine clarification, and spec-quality checks before more AI implementation is safe.
- MVP-to-Launch stays inside Existing Project Track even when product or UX language describes it as a "third official path" for clarity.
- Both tracks share project memory, backlog discipline, review gates, and release discipline.

## Related docs

- `README.md`
- `README_ru.md`
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `AI_EVALUATION_GUIDE.md`
- `docs/spec-foundation.md`
- `docs/spec-quality-gate.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `docs/track-model.md`
- `docs/mvp-to-launch-path.md`
- `llms-full.txt`
