<!-- vcp-version: v0.8.0 -->

<!-- vcp-artifact: CODE_REVIEW_REPORT -->
<!-- vcp-version: v0.8.0 -->
<!-- methodology-version: v1.4 -->

# Post-Task Code Review Report

## Review scope
Describe the task boundary, why this review was triggered, and what acceptance decision is being made.

## Worktree state
Record `git status --short`, whether staged or unstaged changes existed, and whether untracked files were included.

## Changed files reviewed
List the files or areas reviewed so the report is anchored to the real diff.

## Reviewer independence
State whether a fresh independent reviewer, subagent, fresh session, or fallback self-review path was used.
If independent review was unavailable, say so explicitly.

## Validation before review
List validation already available before findings were addressed.
Include command names and whether the results were green, warn-only or unavailable.

## Review pass 1 findings
List actionable findings ordered by severity.
Mark blocking vs non-blocking.
If none, say `No actionable findings`.

## Fixes applied
Describe what changed in response to actionable findings.
If no fixes were needed, say so.

## Validation after fixes
List the rerun validation commands and outcomes after meaningful fixes.
Note any validation that could not be rerun.

## Review pass 2 findings
Record the fresh follow-up review result.
If there was no second pass, explain why.

## Acceptance signal
Choose the current state:
- no actionable findings;
- score threshold met;
- validation green;
- independent reviewer unavailable;
- validation unavailable;
- partial review only.
Explain whether the change set is accepted, conditionally accepted or blocked.

## Findings intentionally not changed
Document any finding that was left unchanged, why, and what risk remains.
If none, say so.

## Public contracts preserved
State which observable behaviors, APIs, schemas, CLI surfaces or user-facing contracts were preserved.

## Security/privacy impact
State whether review found security or privacy impact.
If the diff touches sensitive areas, record whether escalation to Hardening or human review is needed.

## Tests/checks run
List exact commands and the final status of each one.

## Remaining risks
Describe residual uncertainty, missing validation or reasons confidence is reduced.

## Next action
State the smallest safe next step: accept, merge, run another review, escalate, or stop.

## Suggested commit message
Provide a short, accurate commit message if one is needed.
