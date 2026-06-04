# Distribution

VCP is productizing its local adoption paths without pretending that registry publication already exists.

## Honest distribution table

| Path | Status | Command | Notes |
|---|---|---|---|
| Clone + Python module | Stable | `python3 -m vcp_cli doctor` | Current reliable path |
| Editable Python install | Tested in this release if passing | `python3 -m pip install -e . && vcp doctor` | Only supported if validation passes |
| `pipx` local path | Tested if passing | `pipx install . && vcp doctor` | Local path only, not PyPI |
| Node local wrapper | Stable local wrapper | `npm run vcp -- doctor` | Local repo path |
| `npm link` | Dev path | `npm link && vcp doctor` | Local developer path |
| Public PyPI | Planned unless published | `pipx install vcp-cli` | Do not claim available today |
| Public npm / `npx` | Planned unless published | `npx vcp` | Do not claim available today |

## Future publication checklist

- confirm PyPI package name availability;
- confirm npm package name availability;
- prepare release credentials and provenance path;
- validate package metadata and license compatibility;
- smoke test install from a clean environment;
- publish only after maintainer approval.
