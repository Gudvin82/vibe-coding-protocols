# Hardening Prompts

## Discovery step

Before proposing fixes:
- read the project memory first;
- identify active and deferred surfaces;
- use token-aware discovery;
- return an evidence map first;
- avoid reading the whole repository unless the project map is missing or unreliable.

Evidence map format:
- `path:line`
- symbol / route / component
- relevant snippet or signature
- why it matters

## Hardening intake prompt

Use this when AI-generated code already exists.

1. Do not rewrite the project.
2. Find the highest-risk surfaces first.
3. Separate blockers from later improvements.
4. Open or update `AUDIT_BACKLOG.md`.
5. Call out missing evidence, missing tests and risky assumptions.

## Independent review prompt

Use after implementation and before merge or deploy:
- review changed files first;
- look for regressions, security gaps and missing validation;
- challenge accepted risks;
- recommend rollback notes where needed.
