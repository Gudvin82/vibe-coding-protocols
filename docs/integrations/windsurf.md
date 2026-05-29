# Windsurf

## Status

- manual guide;
- rules/template copy workflow;
- prompt-oriented usage;
- no mature plugin yet.

## What to copy

- `START_HERE.md`
- route protocols relevant to the project;
- `templates/AGENTS.md` or an IDE-specific AGENTS variant when relevant;
- command docs and report templates for the selected route.
- `.windsurfrules` if present;
- `templates/AGENTS.windsurf.md` if present;
- route protocols, commands and report templates.

## Suggested prompt

```text
Read START_HERE.md first.
Choose the correct route for this project.
Do not read the entire repository unless needed.
Report the selected route, files needed, and files intentionally skipped.
Preserve user changes.
Run validation before final report.
```

## Validation

- run the smallest relevant repository checks;
- produce a route summary and a scoped final report;
- preserve user changes and unrelated diffs.

## Limitations

- no automatic plugin install is implied;
- IDE-specific behavior may vary;
- slash commands are documentation conventions unless the IDE natively supports them.
Windsurf behavior varies across Cascade-style flows.
Keep scope, route and validation constraints explicit.
