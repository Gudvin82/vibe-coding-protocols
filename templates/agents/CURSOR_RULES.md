<!-- vcp-version: v0.8.9 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

# CURSOR_RULES.md

- Inspect context before editing.
- Avoid unrelated rewrites.
- Keep reviewable diffs.
- Separate shipped vs roadmap.
- Report not-run checks honestly.

## Cost-aware model routing

Use a fast model for:
- file discovery;
- reading docs;
- locating commands;
- simple summaries.

Use a strong model for:
- code edits;
- architecture decisions;
- manifest/schema updates;
- release-risk changes;
- complex debugging.

Do not claim automatic model switching.
Do not claim tests passed unless run.
