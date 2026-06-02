# npm Wrapper

`v0.5.2` adds a local npm entrypoint for JS/Node-first users.
It is a thin wrapper around the Python CLI.

## What works now

Inside this repository:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- manifest validate
```

Optional local link:

```bash
npm link
vcp doctor
vcp init --print-prompt
```

## What the wrapper does

- resolves the repository root;
- detects `python3`, `python`, or `py` depending on platform;
- forwards all arguments to `python -m vcp_cli`;
- prints a useful error if Python is not available.

## What this does not mean

`v0.5.2` does not claim:
- a published npm package;
- `npx vcp` from the public registry;
- `npm install -g` support from a published package;
- parity with a future standalone JavaScript implementation.

Those are roadmap items, not current distribution claims.

## Recommended usage

- use `python3 -m vcp_cli ...` if Python-first is already normal for the team;
- use `npm run vcp -- ...` if the repo is Node-first and you want shorter local commands;
- use `npm link` only for local convenience, not as a publication signal.

## Related docs

- [cli.md](./cli.md)
- [windows.md](./windows.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
