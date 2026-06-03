# npm Wrapper

`v0.6.3` keeps the local npm entrypoint for JS/Node-first users.
It is still a thin wrapper around the Python CLI.

## What works now

Inside this repository:

```bash
npm install
npm run vcp -- evaluate
npm run vcp -- index validate
npm run vcp -- cards validate
```

Optional local link:

```bash
npm link
vcp evaluate
vcp score --badge markdown
```

## What the wrapper does

- resolves the repository root;
- detects `python3`, `python`, or `py` depending on platform;
- forwards all arguments to `python -m vcp_cli`;
- prints a useful error if Python is not available.

## Public npm status

Public npm and `npx` distribution are planned.
Current npm support is local wrapper only.

That means `v0.6.3` does not claim:
- a published npm package;
- `npx vcp` from the public registry;
- `npm install -g` support from a published package;
- parity with a future standalone JavaScript implementation.

## Recommended usage

- use `python3 -m vcp_cli ...` if Python-first is normal for the team;
- use `npm run vcp -- ...` if the repo is Node-first and you want shorter local commands;
- use `npm link` only for local convenience, not as a publication signal.

## Related docs

- [install.md](./install.md)
- [pip-install.md](./pip-install.md)
- [cli.md](./cli.md)
- [npm-publishing-checklist.md](./npm-publishing-checklist.md)
