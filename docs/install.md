# Install

VCP is currently a local repository toolkit.
It does not claim public PyPI, public npm, Homebrew, or native installer distribution in `v0.6.3`.

## Honest install table

| Method | Status | Command |
|---|---|---|
| Clone + Python module | Stable local path | `python3 -m vcp_cli evaluate` |
| Editable Python install | Environment-dependent local dev path | `python3 -m pip install -e . && vcp evaluate` |
| Windows Python launcher | Supported local path | `py -m vcp_cli evaluate` |
| Local npm wrapper | Supported local wrapper | `npm run vcp -- evaluate` |
| npm link | Development path | `npm link && vcp evaluate` |
| Public npm / npx | Planned unless published | Do not claim available |
| PyPI package | Planned unless published | Do not claim available |

## Fastest local start

macOS and Linux:

```bash
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli cards list --recommended
python3 -m vcp_cli review-diff --json
```

Node-first local wrapper:

```bash
npm install
npm run vcp -- evaluate
npm run vcp -- index validate
```

Windows PowerShell:

```powershell
py -m vcp_cli evaluate --json
py -m vcp_cli cards list --recommended
npm run vcp -- evaluate
```

## Editable install

See [pip-install.md](./pip-install.md) for the full editable-install path.

## What works today

- `python3 -m vcp_cli ...`
- `py -m vcp_cli ...` on Windows
- `npm run vcp -- ...` inside this repository
- optional local editable Python install
- optional local `npm link`

## What is not claimed yet

- public `pip install vcp-cli`
- public `python -m pip install vcp-cli` from PyPI
- public `npm install -g vibe-coding-protocols`
- public `npx vcp`
- native GUI installers

## Related docs

- [demo.md](./demo.md)
- [pip-install.md](./pip-install.md)
- [npm.md](./npm.md)
- [cli.md](./cli.md)
- [windows.md](./windows.md)
- [npm-publishing-checklist.md](./npm-publishing-checklist.md)
