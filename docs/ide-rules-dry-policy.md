# IDE Rules DRY Policy

Use this file to keep AI IDE rules aligned
without introducing a generator or symlink strategy yet.

## Repo-local files

These files configure this repository itself:
- `AGENTS.md`
- `CLAUDE.md`
- `.cursorrules`
- `.windsurfrules`
- `.github/copilot-instructions.md`
- `agents/*.example`

## Copy-ready templates

These files are for user projects:
- `templates/AGENTS.md`
- `templates/AGENTS.claude.md`
- `templates/AGENTS.cursor.md`
- `templates/AGENTS.windsurf.md`

## What should stay synchronized

The following ideas should stay aligned across repo-local
and copy-ready AI IDE files:
- Stop Conditions
- Memory Bank
- token-aware discovery
- evidence map workflow
- approval gates for risky changes

## Allowed differences

The following differences are intentional:
- root files describe this repository;
- template files describe what users should copy into their own project;
- Claude, Cursor, Windsurf and Copilot files can mention tool-specific behavior;
- Cursor and Windsurf files may be shorter if the IDE format is constrained.

## What `check-ide-rules-consistency.sh` checks

The script confirms that the main repo-local
and template files still contain the expected baseline phrases.

It is not a semantic diff.
It is a lightweight guard against drift.
