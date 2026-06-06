# Integrations

These guides explain how to use VCP with current AI IDEs and chat-assisted coding environments.

Current status:
- manual guides;
- prompt workflows;
- copy-ready rules and templates;
- no mature plugin suite yet.

## Guides

- [setup-playbook.md](./setup-playbook.md)
- [claude-code.md](./claude-code.md)
- [codex.md](./codex.md)
- [cursor.md](./cursor.md)
- [windsurf.md](./windsurf.md)
- [github-copilot.md](./github-copilot.md)
- [jetbrains-junie.md](./jetbrains-junie.md)
- [../ide-plugins.md](../ide-plugins.md)

## Shared integration prompt

```text
Read START_HERE.md first.
Choose the correct route for this project.
Do not read the entire repository unless needed.
Report the selected route, files needed, and files intentionally skipped.
Preserve user changes.
Run validation before final report.
```

## Important note

VCP command names such as `/care-refactoring` and `/ui-refactoring`
are documentation conventions unless your IDE supports native slash commands.
Treat them as named workflows,
not as proof of built-in IDE support.

If you want the fastest practical installation path, start with [setup-playbook.md](./setup-playbook.md).
