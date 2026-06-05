# Post-Task Code Review Protocol

## Purpose

Use this protocol after a meaningful AI-generated task and before:
- the next task;
- merge;
- commit, if the user requires review before commit;
- release;
- deploy;
- tag;
- handoff.

Core principle:

Spend AI capacity on reviewing the change that is about to be accepted, not only on generating the next change.

## Why this exists

AI agents can produce useful code and still miss:
- correctness bugs;
- behavioral regressions;
- edge cases;
- security or privacy issues;
- data integrity problems;
- missing tests;
- public contract changes;
- UX or accessibility regressions;
- maintainability risks;
- changes outside scope.

Review is a delivery gate, not optional polish.

## When to use

Use after any task that changed:
- production code;
- public behavior;
- API contracts;
- database or persistence behavior;
- auth, session or permissions;
- payments or billing;
- personal data handling;
- security-sensitive logic;
- scoring or rules engines;
- shared engine code;
- UI flows;
- dependencies;
- CI, release or config behavior;
- non-trivial docs that affect user, security or deployment behavior.

Use before:
- the next feature;
- merge;
- deploy;
- release;
- tag;
- handoff.

## When lighter review is acceptable

A lighter review may be enough for:
- typo-only docs changes;
- formatting-only docs changes;
- version bumps after existing validation;
- link-only updates;
- release-note updates with no behavior change.

Even then, run cheap validation when available.

## Non-goals

This protocol is not:
- a replacement for human review;
- a security audit;
- a legal or compliance audit;
- a penetration test;
- proof of production safety;
- a reason to skip tests;
- an excuse to chase score-only polish;
- a broad refactor request;
- permission to expand scope.

## Review loop workflow

1. Inspect active worktree.
2. Determine review scope.
3. Collect validation output.
4. Run independent read-only review.
5. Receive findings.
6. Fix concrete actionable issues.
7. Re-run relevant validation.
8. Run a fresh independent review if needed.
9. Accept only when review and validation satisfy the acceptance criteria.
10. Report findings, fixes, validation and remaining risks.

Start with:

```bash
git status --short
git diff
git diff --cached
```

Rules:
- include untracked files if they are in scope;
- preserve unrelated user changes;
- do not stage, commit, reset, stash or push unless the user explicitly asks;
- do not include unrelated pre-existing issues unless the active changes make them worse.

## Independent reviewer

Best case:
use a fresh independent reviewer or subagent that does not inherit the implementation conversation.

Reviewer must:
- stay read-only;
- inspect repo state itself;
- inspect `git status`;
- inspect staged and unstaged diffs;
- inspect relevant files;
- inspect validation output;
- prioritize actionable findings;
- provide file and line references when possible;
- end with either actionable findings or no actionable findings;
- optionally provide a numeric score.

Reviewer must not:
- edit files;
- stage files;
- commit;
- reset;
- stash;
- push;
- rely on parent-agent explanations;
- rely on previous reviewer output;
- accept “the main agent said it works” as evidence.

If subagents are unavailable:
- use a fresh chat, session or model if possible;
- pass a self-contained review prompt;
- do not pass implementation rationale;
- do not pass previous reviewer output unless the task is specifically to verify a fix;
- mark the report as `independent reviewer unavailable` if no independent path exists.

## Acceptance criteria

Default acceptance requires:
1. relevant validation is green; and
2. the latest reviewer reports no actionable findings.

Optional score-based acceptance:
- if a numeric score is used, default threshold is `9.5/10`;
- score alone is not enough if validation is red;
- do not chase arbitrary polish if the reviewer reports no actionable findings;
- if a reviewer gives a low score but no actionable findings, ask once for concrete blocking issues;
- if no concrete blocking issues are given, accept as `no actionable findings` or run a fresh reviewer.

Validation failure blocks acceptance even if the review score is high.

## Findings handling

Fix findings that are:
- concrete;
- actionable;
- relevant to active changes;
- tied to correctness, security, privacy, data integrity, UX, tests, maintainability, accessibility or public contracts.

Do not blindly fix:
- stale findings;
- unrelated pre-existing issues;
- broad rewrites;
- subjective style-only suggestions;
- architecture-incompatible suggestions;
- changes that alter product behavior without approval;
- suggestions outside the accepted scope.

If a finding is intentionally not changed:
- document it;
- explain why;
- note risk if any;
- include it in the final report.

## Validation rules

After meaningful fixes, run the smallest useful validation for the touched surface.

Examples:
- docs: newline, link and version checks;
- CLI: wrapper smoke tests and unit tests if present;
- frontend: lint, typecheck, build or component tests;
- backend: unit or integration tests;
- DB: migration tests and rollback plan if available;
- security-sensitive changes: Hardening route checks;
- shared engine: validation for all affected products;
- public site: public-site readiness checks if available.

If validation cannot be run:
- explain why;
- lower confidence;
- do not claim full acceptance;
- provide the exact next validation step.

## Relationship to other routes

Use Maintenance Refactoring when the goal is behavior-preserving cleanup.
Use Hardening when the goal is production or security readiness.
Use Extended when public, operational or high-risk change management is broader than one diff.
Use Post-Task Code Review when the work is already changed and now needs acceptance discipline.
