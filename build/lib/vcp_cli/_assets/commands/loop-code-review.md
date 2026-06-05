# /loop-code-review

This is a VCP command document.
It may not be a native slash command in every AI IDE.
If the IDE does not support slash commands, paste this command document or use the prompt template.

## What it does

Runs a post-task acceptance loop for active git changes:
- inspect worktree state;
- review staged, unstaged and in-scope untracked files;
- collect validation evidence;
- request independent read-only review;
- fix actionable findings;
- re-run validation;
- accept only when review and validation are green enough to proceed.

## When to invoke

Use after meaningful AI-generated work and before:
- next task;
- merge;
- release;
- deploy;
- tag;
- handoff.

## Required inputs

Provide:
- target repository state;
- active scope;
- validation commands already run or still needed;
- any known stop conditions;
- whether an independent reviewer path is available.

## Worktree inspection

Start with:

```bash
git status --short
git diff
git diff --cached
```

Include in-scope untracked files.
Do not hide unrelated user changes.
Do not stage, reset, stash, commit or push unless explicitly asked.

## Independent reviewer rules

Prefer a fresh independent reviewer or subagent.
Reviewer must be read-only and must inspect the repo state directly.
Reviewer should prioritize correctness, security, privacy, data integrity, tests, UX, accessibility, maintainability and public contract issues.

If no independent reviewer is available:
- use a fresh prompt pass if possible;
- avoid passing implementation rationale;
- mark the report as `independent reviewer unavailable`.

## Validation requirement

Before acceptance:
- run the smallest useful validation for the touched surface;
- rerun validation after meaningful fixes;
- do not accept a diff with failing validation just because review text sounds positive.

## Acceptance criteria

Accept only when:
- validation is green; and
- the latest review reports no actionable findings.

Optional score threshold:
- `9.5/10` if a numeric score is used.
- score alone does not override failing validation.

## Final report format

Use:
- [../templates/reports/code-review-report.md](../templates/reports/code-review-report.md)

Protocol:
- [../protocols/review/post-task-code-review.md](../protocols/review/post-task-code-review.md)
Prompt template:
- [../templates/prompts/loop-code-review.md](../templates/prompts/loop-code-review.md)
