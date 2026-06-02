# Init

`vcp init` is the simplest CLI starting action in `v0.5.4`.
It is intentionally guidance-first.

## What it does

- points the user to `AI_INTAKE.md`;
- reminds the user to classify the project before copying anything;
- suggests `route` and `adopt --dry-run` next;
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
- `init --apply` is intentionally not implemented in `v0.5.4`;
- prompts are guidance, not a substitute for route-specific docs.

## Why this exists

The repository has grown beyond a single README skim.
`init` gives a short, safe onboarding step for humans and AI agents without pretending to be a full installer.

## Related docs

- [../AI_INTAKE.md](../AI_INTAKE.md)
- [cli.md](./cli.md)
- [adoption-packs.quickstart.md](./adoption-packs.quickstart.md)
