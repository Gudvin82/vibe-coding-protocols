# npm Wrapper

VCP now includes an experimental Node wrapper.

Files:
- `package.json`
- `bin/vibe-check.js`

## Purpose

This is not a full CLI project.
It is a thin wrapper around `scripts/vibe-check.sh` so contributors can test a future `npx`-style entrypoint.

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
