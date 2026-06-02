# npm Wrapper

`v0.5.5` keeps the local npm entrypoint for JS/Node-first users.
It is still a thin wrapper around the Python CLI.

## What works now

Inside this repository:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- evaluate
npm run vcp -- manifest validate
```

Optional local link:

```bash
npm link
vcp doctor
vcp evaluate
vcp init --print-prompt
```

## What the wrapper does

- resolves the repository root;
- detects `python3`, `python`, or `py` depending on platform;
- forwards all arguments to `python -m vcp_cli`;
- prints a useful error if Python is not available.

## Public npm status

Public npm and `npx` distribution are planned.
Current npm support is local wrapper only.

That means `v0.5.5` does not claim:
- a published npm package;
- `npx vcp` from the public registry;
- `npm install -g` support from a published package;
- parity with a future standalone JavaScript implementation.

## Publication readiness

The wrapper is now closer to publish-ready metadata, but publication is still a separate step.
See [npm-publishing-checklist.md](./npm-publishing-checklist.md).

Suggested rehearsal:

```bash
npm run vcp -- doctor
npm run vcp -- evaluate
npm run vcp -- manifest validate
npm pack --dry-run
```

## Recommended usage

- use `python3 -m vcp_cli ...` if Python-first is already normal for the team;
- use `npm run vcp -- ...` if the repo is Node-first and you want shorter local commands;
- use `npm link` only for local convenience, not as a publication signal.

## Related docs

- [cli.md](./cli.md)
- [npm-publishing-checklist.md](./npm-publishing-checklist.md)
- [windows.md](./windows.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
