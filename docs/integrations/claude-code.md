# Claude Code

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
- `templates/AGENTS.claude.md` if you want a Claude-specific starting point;
- `commands/care-refactoring.md` and `commands/ui-refactoring.md` for named maintenance workflows.

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
Claude Code works well with route-oriented prompts,
subagent patterns
and repository-local instruction files,
but VCP does not assume any built-in installer.
