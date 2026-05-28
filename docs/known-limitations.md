# Known Limitations

Vibe Coding Protocols is intentionally lightweight.

## Current limitations

- no guaranteed security;
- no automatic model routing engine;
- no full Windows-native CLI yet;
- optional scanners are not bundled;
- examples are synthetic;
- no public real-world case study is claimed yet;
- bash-first toolkit;
- content validation is heuristic;
- wrappers and VS Code extension are experimental skeletons.

## What this means in practice

Use VCP as a workflow and repository toolkit.
Do not treat it as a substitute for testing, security review, legal review or production operations.

## Parsing and markdown limits

`vibe-check` relies on lightweight heuristics.
False positives and false negatives are possible.
If a warning is accepted intentionally, record that in `AUDIT_BACKLOG.md` instead of fighting the script blindly.

## Prompt drift risk

A giant `AGENTS.md` can become less reliable over time.
Use `PROJECT_MAP.md`, `ARCHITECTURE_MAP.md` and `AUDIT_BACKLOG.md` to carry project context instead of endlessly appending one massive prompt.
