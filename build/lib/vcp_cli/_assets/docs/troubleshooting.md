# Troubleshooting

## AI cannot open a GitHub link

Paste `README.md` and `START_HERE.md` first, then continue with the smallest relevant docs.

## GitHub raw looks stale

Use the commit-specific raw URL instead of `main` when you need proof right after push.

## `vibe-check` shows WARN

WARN means attention is needed, not automatic failure by default.
Read the warning before deciding whether the route is still acceptable.

## Optional scanners are missing

That is allowed.
Use `--scanners` for local exploration and install scanners only when they fit your workflow.

## Content quality warnings appear

A file can exist and still be too empty to count as actionable project memory.
Add real findings, routes, owners, integrations or recurring checks before treating the artifact as complete.

## Content validation seems wrong

The parser is heuristic.
Headings such as `## Audit Backlog`, `### Audit Backlog`, `Findings`, `Risks` and `Tasks` are tolerated, but false positives or false negatives are still possible.
If you intentionally keep a non-standard structure, record the warning in `AUDIT_BACKLOG.md`.

## PowerShell or Windows shell issues

Use Git Bash or WSL, or run the wrapper in `scripts/vibe-check.ps1`.

## Permission denied on scripts

Run `chmod +x` on the shell script or call it through `bash script-name.sh`.

## `sha256sum` is missing on macOS

Use `shasum -a 256` instead.

## README tables are not rendering

Check that the separator row exists and that code fences are properly closed.

## CI changed-files guardrail fails

Split the PR if possible, or raise repository variable `MAX_CHANGED_FILES` for a planned larger change.

## `vibe-check` JSON is not what you expected

Use `bash scripts/vibe-check.sh --audit --json` and confirm that your shell is not mixing other output into stdout.

## I am not sure which repository I am editing

Run `git remote -v` and confirm whether you are inside:
- your project repository;
- a copied starter template;
- or the source toolkit repository itself.

Do not push to the source toolkit or template repository by mistake.
