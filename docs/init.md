# Init

`vcp init` is the simplest CLI starting action in `v0.6.0`.
It is intentionally guidance-first.

## What it does

- points the user to `AI_INTAKE.md`;
- reminds the user to classify the project before copying anything;
- suggests `route` and `adopt --dry-run` next;
- nudges non-trivial unclear ideas toward the Spec Lane;
- can print a target-specific copy-paste prompt.

## Examples

```bash
python3 -m vcp_cli init
python3 -m vcp_cli init --print-prompt
python3 -m vcp_cli init --target codex
python3 -m vcp_cli init --target claude
python3 -m vcp_cli init --target cursor
python3 -m vcp_cli init --target windsurf
python3 -m vcp_cli init --target copilot
```

Node-first local option:

```bash
npm run vcp -- init
npm run vcp -- init --print-prompt
```

## Current limits

- `init` does not modify files by default;
- `init --apply` is intentionally not implemented in `v0.6.0`;
- prompts are guidance, not a substitute for route-specific docs.

## Repository evaluation note

If the task is evaluating VCP itself rather than onboarding a target repo, use:

```bash
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli evaluate --print-prompt
```

## Why this exists

The repository has grown beyond a single README skim.
`init` gives a short, safe onboarding step for humans and AI agents without pretending to be a full installer.

## Related docs

- [../AI_INTAKE.md](../AI_INTAKE.md)
- [../AI_EVALUATION_GUIDE.md](../AI_EVALUATION_GUIDE.md)
- [cli.md](./cli.md)
- [adoption-packs.quickstart.md](./adoption-packs.quickstart.md)
