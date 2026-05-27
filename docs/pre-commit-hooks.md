# Pre-Commit Hooks

Use pre-commit hooks as local guardrails, not as a replacement for review.

## Install the optional hook

```bash
bash scripts/install-hooks.sh --mode starter
bash scripts/install-hooks.sh --mode hardening
bash scripts/install-hooks.sh --mode audit
bash scripts/install-hooks.sh --mode starter --dry-run
```

The installed hook:
- blocks commits that stage `.env` or `.env.*` files;
- allows `.env.example`;
- warns when the staged diff touches many files;
- runs `bash scripts/vibe-check.sh --starter`, `--hardening` or `--audit`
  depending on the selected mode.

Default behavior:
- installs in `starter` mode;
- prints a reminder that `hardening` and `audit` are better for existing or
  production-bound projects.

It does not:
- push;
- create commits;
- change production configs;
- install dependencies.

## Why keep it optional?

Some teams prefer only CI enforcement. Others want a local reminder before a risky commit.
This repository keeps the hook optional so it does not force one workflow on every project.
