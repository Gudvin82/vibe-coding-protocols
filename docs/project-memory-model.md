# Project Memory Model

VCP uses project memory as a file-based control layer.
It does not add a hidden runtime memory database.

## What VCP means by project memory

VCP memory is the set of explicit project files that preserve decisions, architecture, backlog, current context, accepted risks, and release state.

This memory is:
- file-based;
- reviewable;
- project-local;
- suitable for human review and AI-assisted work.

## Core memory files

At minimum, inspect and maintain these files when they exist:

- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `PROJECT_BACKLOG.md`
- `AUDIT_BACKLOG.md`
- `AI_INTAKE.md`
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- current release notes
- case-study or proof surfaces when they affect public claims
- `THIRD_PARTY_REGISTRY.md` when external dependencies exist

Spec memory also matters when the spec lane is active:

- `PRD`
- `FEATURE_SPEC`
- `ACCEPTANCE_CRITERIA`
- `TASKS`
- `SPEC_REVIEW`
- `OBSERVED_SPEC`
- `SPEC_GAPS`

## Memory update rules

- update memory when architecture changes;
- update backlog when new tasks or risks appear;
- update architecture truth when behavior crosses layers;
- update the third-party registry when adding SDK, API, auth, analytics, or external services;
- update release notes when public or release behavior changes;
- do not store secrets;
- do not store private customer data;
- do not use memory files as a dumping ground.

## AI agent rules

AI agents should:
- read memory before changing code;
- update only relevant memory;
- state when memory is stale;
- add a TODO or backlog item instead of silently ignoring gaps;
- preserve human review.
