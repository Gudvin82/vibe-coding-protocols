# Code Discovery Command

Use when the AI needs to find relevant code before editing.

Prompt:

Before editing, perform token-aware code discovery.

Return a compact evidence map only:
- `path:line`
- symbol / component / route
- snippet / signature
- why it matters
- confidence

Do not modify files.
Do not read the whole repository unless `PROJECT_MAP.md` is missing or unreliable.
