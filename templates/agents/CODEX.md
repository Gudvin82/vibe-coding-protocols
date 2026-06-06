<!-- vcp-version: v0.8.8 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

# CODEX.md

- Read repository routing files first.
- Prefer minimal diffs over rewrites.
- Do not overclaim shipped capabilities.
- Do not say tests passed unless they were run.
- Cite changed files in the final report.
- Preserve README, VERSION, manifests, and release surfaces together.
- Use dry-run and non-destructive paths first.

## Cost-aware model routing

Use a fast model tier for:
- discovery;
- grep/search;
- reading files;
- locating commands;
- summarizing logs.

Use a strong model tier for:
- mutation;
- patch writing;
- architecture changes;
- schema/manifest/test updates;
- complex debugging;
- release prep.

Do not claim tests passed unless they ran.
Do not perform broad rewrites.
Fail closed on unsafe operations.
