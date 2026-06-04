# Distribution

VCP `v0.8.0` makes the Python package PyPI-ready without pretending that public publication already exists.

## Current honest distribution status

| Path | Status | Command | Notes |
|---|---|---|---|
| Clone + Python module | Stable | `python3 -m vcp_cli doctor` | No install required |
| Local package install | Stable if validation passes | `python3 -m pip install . && vcp doctor` | Primary installable CLI path |
| `pipx` local path | Supported if available and validation passes | `pipx install . && vcp doctor` | Local path only, not PyPI |
| Node local wrapper | Stable local wrapper | `npm run vcp -- doctor` | Local repo path |
| `npm link` | Dev path | `npm link && vcp doctor` | Local developer path |
| Public PyPI | Manual future publication | `pip install vcp-cli` | Do not claim available until actually published |
| Public npm / `npx` | Planned unless published | `npx vcp` | Do not claim available today |

## PyPI-ready, not auto-published

`v0.8.0` includes:
- Python packaging metadata suitable for local build/install;
- a `vcp` console script entrypoint;
- a GitHub workflow scaffold for PyPI publication after maintainer approval;
- documentation for token/trusted-publishing setup.

It does not automatically publish to PyPI and does not claim public PyPI availability unless that publication is real.

## Publication checklist

1. Confirm package name availability for `vcp-cli`.
2. Create a PyPI account and API token.
3. Add `PYPI_API_TOKEN` only if token-based publishing is chosen.
4. Test `python -m build` locally.
5. Publish only after maintainer approval.

See `docs/pypi-publishing.md`.
