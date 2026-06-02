# Install

VCP is currently a local repository toolkit.
It does not claim public PyPI, public npm, Homebrew, or native installer distribution in `v0.5.7`.

## Fastest local start

macOS and Linux:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli evaluate --json
```

Node-first local wrapper:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- evaluate
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli evaluate --json
npm run vcp -- doctor
```

## Optional editable install

If you want a local `vcp` command without claiming package publication:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
vcp doctor
vcp evaluate
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e .
vcp doctor
vcp evaluate
```

This is a local development install only.
It is not a signal that VCP is already published to PyPI.

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

## Recommended verification

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile public-growth --json
python3 -m vcp_cli adopt --pack public-growth --dry-run --json
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli manifest validate
```

## Related docs

- [cli.md](./cli.md)
- [npm.md](./npm.md)
- [windows.md](./windows.md)
- [npm-publishing-checklist.md](./npm-publishing-checklist.md)
