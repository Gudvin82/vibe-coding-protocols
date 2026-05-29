# CLI Status

VCP is currently script-first.
A unified `vcp` CLI is planned,
but the stable workflow today is built around documented scripts.

## Current stable entrypoints

Use these directly:
- `scripts/vibe-check.sh`
- `scripts/init-minimal.sh`
- `scripts/install-hooks.sh`
- `scripts/check-version-consistency.sh`
- `scripts/validate-links.sh`
- `scripts/check-newlines.py`
- `scripts/check-toolkit.sh`

## Experimental CLI and wrapper status

VCP also includes an early Python wrapper:
- `python -m vcp_cli doctor`
- `python -m vcp_cli audit`
- `python -m vcp_cli starter`

Current wrapper status:
- thin wrapper around `scripts/vibe-check.sh`;
- useful for users who prefer a Python entrypoint;
- not a mature standalone CLI product yet;
- not a replacement for the documented scripts.

Do not assume package-manager installation support unless it is explicitly documented.

## Recommended user path

Today the most reliable path is:
1. use the documented scripts directly;
2. use `scripts/install-hooks.sh` for local hooks when appropriate;
3. use the Python wrapper only for commands that are already documented and tested.

## Local hooks and CI

See:
- [pre-commit-hooks.md](./pre-commit-hooks.md)
- [tooling-roadmap.md](./tooling-roadmap.md)

## Windows note

VCP is still Bash-first.
If you are on Windows, start with [windows.md](./windows.md) to choose WSL, Git Bash or the limited PowerShell wrapper path.

## Future unified `vcp` command roadmap

Planned future surfaces may include:
- `vcp doctor`
- `vcp check`
- `vcp init`
- `vcp install-hooks`
- `vcp validate-links`
- `vcp version`
- `vcp route`
- `vcp protocol-index`
- `vcp public-site-check`

These are roadmap items,
not promises about current shipped functionality.
