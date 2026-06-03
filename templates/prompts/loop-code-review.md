<!-- vcp-artifact: LOOP_CODE_REVIEW_PROMPT -->
<!-- vcp-version: v0.6.2 -->
<!-- methodology-version: v1.4 -->

# Loop Code Review Prompt

Use this as a copy-paste prompt for Claude Code, Codex, Cursor, Windsurf, GitHub Copilot Chat or another coding agent.

## Independent review prompt

```text
Review the active git changes independently.
Stay read-only.
Do not edit files, stage files, commit, reset, stash or push.

Inspect:
- git status --short
- staged and unstaged diffs
- in-scope untracked files
- relevant changed files
- validation output already available

Prioritize actionable findings related to:
- correctness
- security
- privacy
- data integrity
- UX or accessibility
- tests and validation gaps
- maintainability risk
- public contract changes

Ignore unrelated pre-existing issues unless the active changes clearly make them worse.

Return findings ordered by severity.
Include file and line references when possible.
Mark each finding as blocking or non-blocking.
If there are no actionable findings, say so explicitly.
Optional: include a score from 1 to 10.
State what blocks acceptance, if anything.
```

## Fresh reviewer prompt for repeated pass

```text
Review the current active git changes as a fresh reviewer.
Stay read-only.
Do not rely on previous review output unless the request explicitly says to verify one specific fix.

Inspect the current worktree state, diffs, changed files and validation output.
Return only current actionable findings.
If no actionable findings remain, say that directly.
Optional: include a score from 1 to 10, but explain any blocking issue concretely.
```
