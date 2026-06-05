# Commands

Copyable VCP command patterns for AI IDEs.

These are not shell commands.
They are reusable AI instructions for Claude Code, Codex, Cursor, Windsurf and similar tools.

## Available command patterns

| Command | Use when | What it returns |
|---|---|---|
| [care-refactoring](./care-refactoring.md) | working project is risky to change | scoped maintenance plan |
| [ui-refactoring](./ui-refactoring.md) | UI ownership is drifting | UI ownership cleanup plan |
| [third-party-api-intake](./third-party-api-intake.md) | an external API or SDK is being proposed | intake report and registry decision |
| [prod-log-monitor](./prod-log-monitor.md) | production symptoms must be observed read-only | capture plan and observation report |
| [daily-error-triage](./daily-error-triage.md) | recent production issues need grouping and follow-up | triage report and backlog routing |
| [backlog-update](./backlog-update.md) | one shared project backlog must be updated before implementation | backlog change summary |
| [loop-code-review](./loop-code-review.md) | meaningful AI-generated changes need acceptance | review findings, fixes and acceptance signal |
