# Two-Track Model

Vibe Coding Protocols is designed for two primary AI-assisted delivery tracks.

Short positioning:

`Build with AI. Ship with control.`

Core positioning:

`VCP helps build AI-assisted products from idea to production without losing control.`

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

## How tracks combine

- A new project can start in the New Project Track and later move into Existing Project control once the repository and release pressure are real.
- An existing project can still need spec retrofit, question-engine clarification, and spec-quality checks before more AI implementation is safe.
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
- `llms-full.txt`
