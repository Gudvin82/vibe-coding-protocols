# Install

VCP is a local repository toolkit in `v0.7.1`.
It does not claim public PyPI, public npm, Homebrew, or native installer distribution unless those channels are actually released.

## Honest install table

| Path | Status | Command | Notes |
|---|---|---|---|
| Clone + Python module | Stable | `python3 -m vcp_cli doctor` | Current reliable path |
| Editable Python install | Tested in this release if passing | `python3 -m pip install -e . && vcp doctor` | Only document as supported if validation passes |
| `pipx` local path | Tested if passing | `pipx install . && vcp doctor` | Local path only, not PyPI |
| Node local wrapper | Stable local wrapper | `npm run vcp -- doctor` | Local repo path |
| `npm link` | Dev path | `npm link && vcp doctor` | Local developer path |
| Public PyPI | Planned unless published | `pipx install vcp-cli` | Do not claim available today |
| Public npm / `npx` | Planned unless published | `npx vcp` | Do not claim available today |

## Fastest local tryout

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --json
```

## Practical chain

1. install or run locally;
2. inspect with `onboard` and `classify`;
3. use `adopt plan` instead of blind copying;
4. run `review-diff`, `release-check`, and `score` before claiming readiness.
