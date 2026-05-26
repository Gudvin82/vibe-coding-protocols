# AI-Specific Threat Model

AI-assisted delivery adds risks that normal code review can miss.
This document is a practical checklist, not a formal security model.

## Prompt injection

Risk:
- the model follows hostile instructions from retrieved content, issues, docs or user input.

Detection:
- tool output suddenly changes scope;
- external content asks the model to ignore prior rules.

Mitigation:
- keep tool permissions narrow;
- require approved routes and stop conditions;
- treat retrieved text as untrusted input.

Relevant VCP artifact:
- `AGENTS.md`
- `Starter Protocol`
- `Stop Conditions`

## Tool permission abuse

Risk:
- AI uses a broader tool action than the task really needs.

Detection:
- unexplained file sprawl;
- large diffs for a small request;
- risky shell or browser actions without approval gates.

Mitigation:
- smallest practical diff;
- explicit approval for risky areas;
- separate reviewer path.

Relevant VCP artifact:
- `AGENTS.md`
- `Independent Diff Review`
- `AUDIT_BACKLOG.md`

## Hallucinated dependencies / packages / APIs

Risk:
- AI invents a package, endpoint, SDK method or integration behavior.

Detection:
- docs do not match implementation;
- no official source;
- package or API cannot be verified.

Mitigation:
- `THIRD_PARTY_REGISTRY.md`;
- safe update / intake workflow;
- official docs before install.

Relevant VCP artifact:
- `THIRD_PARTY_REGISTRY.md`
- `safe-update-workflow.md`

## Context leakage through AI tools

Risk:
- secrets, private architecture, logs or internal endpoints leak through prompts, screenshots or shared chat.

Detection:
- prompts include raw secrets;
- screenshots show admin data;
- public repo contains internal docs.

Mitigation:
- sanitized docs;
- no secrets in prompts;
- public vs private docs policy.

Relevant VCP artifact:
- `public-vs-private-docs.md`
- `SECURITY_BASELINE.md`
- `Architecture Source of Truth`

## Conflicting AI sessions

Risk:
- two AI sessions change the same area with different assumptions.

Detection:
- duplicated fixes;
- unexplained regressions;
- conflicting PROJECT_MAP or backlog state.

Mitigation:
- one source of truth;
- explicit Memory Bank updates;
- reviewer should not inherit implementation rationale.

Relevant VCP artifact:
- `PROJECT_MAP.md`
- `PROMPTS.md`
- `multi-agent-workflows.md`

## AI-generated migrations

Risk:
- schema changes are generated quickly but not validated for rollback, data safety or deploy order.

Detection:
- destructive migration without rollback;
- no staging evidence;
- no backup point.

Mitigation:
- migration rollback checklist;
- staging validation;
- owner and rollback plan.

Relevant VCP artifact:
- `ai-generated-migrations-rollback.md`
- `MIGRATION_ROLLBACK_PLAN.md`

## AI cost / runaway loops

Risk:
- tool loops, repeated retries or broad repo reads burn budget and time.

Detection:
- repeated re-fixes on same area;
- large repeated prompts;
- no scoped discovery.

Mitigation:
- token-aware discovery;
- stop conditions;
- smaller diffs and explicit routes.

Relevant VCP artifact:
- `token-aware-code-discovery.md`
- `PROJECT_MAP.md`
- `vibe-metrics.md`

## Unsafe auto-fixes

Risk:
- AI “fixes” a warning by rewriting unrelated layers.

Detection:
- diff size much larger than problem size;
- architecture drift;
- tests no longer match behavior.

Mitigation:
- smallest practical diff;
- approval gates;
- independent review.

Relevant VCP artifact:
- `AGENTS.md`
- `ANTI_PATTERNS.md`

## Model overconfidence

Risk:
- AI states uncertain claims as facts.

Detection:
- no cited source;
- mismatch between docs and code;
- missing uncertainty notes.

Mitigation:
- evidence map;
- explicit unknowns;
- separate validation and review stage.

Relevant VCP artifact:
- `PROJECT_MAP.md`
- `PROMPTS.md`
- `AUDIT_BACKLOG.md`

## Generated tests that assert wrong behavior

Risk:
- AI writes tests that encode the bug instead of the intended behavior.

Detection:
- tests mirror implementation too closely;
- no product or contract check;
- only happy-path assertions.

Mitigation:
- start from product flow and boundaries;
- use testing cookbook patterns;
- include negative cases.

Relevant VCP artifact:
- `testing-cookbook.md`
- `Product Brief`
- `Architecture Source of Truth`
