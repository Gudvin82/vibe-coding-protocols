# npm Wrapper

VCP now includes an experimental Node wrapper.

Files:
- `package.json`
- `bin/vibe-check.js`

## Purpose

This is not the main product CLI.
The primary local CLI surface is `python3 -m vcp_cli`.
The Node wrapper remains a thin helper around `scripts/vibe-check.sh`.

Examples:

```bash
node bin/vibe-check.js --doctor
node bin/vibe-check.js --init-report
node bin/vibe-check.js --starter
```

## Scope

- experimental;
- local-repo-first;
- no automatic npm publish;
- no claim that the package is already published.

## If you run it outside a VCP-enabled context

The wrapper prints a clear message instead of pretending to bootstrap everything automatically.
