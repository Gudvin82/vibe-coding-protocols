# GitHub Copilot instructions

- Read `README.md`, `AGENTS.md` and `PROJECT_MAP.md` before edits.
- Use Starter for new projects.
- Use Hardening for existing code.
- Use token-aware discovery before broad edits.
- Do not activate deferred surfaces.
- Ask before migrations, auth, payments or new dependencies.
- Keep diffs atomic.
- Report changed files and validation.
- Do not expose secrets.
- If broad discovery is needed, return an evidence map with `path:line`, symbol, snippet, why it matters and confidence before editing.
- Use an independent review pass before risky merge or deploy work.
