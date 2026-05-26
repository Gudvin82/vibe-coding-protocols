# Multi-agent workflows

Use multiple AI agents only if their roles stay explicit and their handoffs stay visible.

## Roles

### Planner / Architect

Creates the route, constraints and approved plan.

### Code discovery agent

Returns an evidence map from the repository.

### Implementation agent

Works from the approved plan and makes the smallest practical diff.

### Independent reviewer

Reviews the diff without inheriting the implementation rationale.

### Test / validation agent

Runs checks, smoke tests and reports failures.

### Documentation agent

Updates Memory Bank files, prompts log and backlog notes.

## Rules

- one source of truth: Memory Bank;
- no hidden assumptions between agents;
- reviewer should not inherit implementation rationale;
- implementation agent should work from an approved plan;
- all agents should update or report into `AUDIT_BACKLOG.md`, `PROJECT_MAP.md` or `PROMPTS.md`.

## Example workflow

1. Planner creates the plan.
2. Discovery agent returns an evidence map.
3. Implementation agent makes the smallest practical diff.
4. Validation agent runs checks.
5. Reviewer agent reviews the diff.
6. Documentation agent updates the Memory Bank.
