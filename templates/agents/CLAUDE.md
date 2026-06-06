<!-- vcp-version: v0.9.3 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

# CLAUDE.md

- Inspect before editing.
- Avoid broad rewrites.
- Keep diffs minimal and reviewable.
- Do not claim tests passed unless they actually ran.
- Report failed and not-run checks clearly.
- Keep shipped vs roadmap separate.
- Preserve version surfaces and machine-readable sync.
- Fail closed on unsafe operations.

## Model routing

Use a fast/cheap model tier, such as Haiku, for:
- grep/search;
- reading files;
- locating commands;
- summarizing logs;
- checking whether something exists.

Use a strong/reasoning model tier, such as Sonnet, for:
- writing patches;
- architecture changes;
- release prep;
- schema/manifest/test updates;
- debugging complex failures;
- safety-sensitive decisions.

If the current model is too weak for the next step, stop and ask the user to switch models before editing.
