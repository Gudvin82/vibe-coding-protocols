<!-- vcp-version: v0.6.6 -->
<!-- methodology-version: v1.4 -->
# Spec Foundation Protocol

## Goal

Turn a rough idea into enough product structure, project memory, backlog state, and review discipline before AI implementation begins.

## Minimum path

Use when:

- the task is meaningful but still small;
- no production-critical risk exists;
- the team needs a fast brief before implementation.

Required outputs:

- feature brief;
- acceptance criteria;
- validation plan;
- backlog item.

## Full path

Use when:

- multiple flows or actors are involved;
- architecture impact is possible;
- user data, integrations, or rollout complexity appear.

Required outputs:

- `PRODUCT_BRIEF.md`
- `PRD.md`
- `FEATURE_SPEC.md`
- `ACCEPTANCE_CRITERIA.md`
- `TASKS.md`
- backlog linkage
- architecture-memory update note.

## Governed path

Use when:

- auth, payment, privacy, persistence, or production rollout are involved.

Required outputs:

- full path outputs;
- release-readiness note;
- rollback or migration note;
- third-party review, when relevant;
- PR Gate decision path.

## Stop conditions

- the idea still hides the main user or operator;
- acceptance criteria are absent;
- production/data impact is still unknown;
- external dependencies remain unstated.
