# Markdown Style

VCP is intentionally raw-readable for humans,
AI assistants
and diff review.

## Guidelines

- one heading per line;
- one list item per line;
- avoid whole sections collapsed into one line;
- prefer AI-readable diffs over minified markdown;
- keep tables readable in source;
- do not wrap URLs awkwardly if it makes them less useful;
- code blocks may contain long lines when necessary.

## Why this matters

Readable markdown helps with:
- review;
- blame and diff history;
- AI context selection;
- public raw-file trust.

If a file needs to be allowlisted for readability checks,
keep the allowlist small and document the reason in the script.
