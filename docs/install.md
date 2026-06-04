# Install

VCP `v0.8.0` is designed to be installable from a local clone as a real CLI.
It still does not claim public PyPI, public npm, Homebrew, or native installer distribution unless those channels are actually published.

## Install from local clone

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m pip install .
vcp doctor
vcp evaluate
```

## Install with pipx from local clone

```bash
pipx install .
vcp doctor
```

If `pipx` is unavailable in the validation environment, treat this as packaging-supported but not locally verified in that environment.

## Honest install table

| Path | Status | Command | Notes |
|---|---|---|---|
| Clone + Python module | Stable | `python3 -m vcp_cli doctor` | Works without installation |
| Local package install | Stable if validation passes | `python3 -m pip install . && vcp doctor` | Main `v0.8.0` install path |
| Editable install | Dev path | `python3 -m pip install -e . && vcp doctor` | Useful for contributors |
| `pipx` local path | Supported if available and validation passes | `pipx install . && vcp doctor` | Local path only, not PyPI |
| Node local wrapper | Stable local wrapper | `npm run vcp -- doctor` | Local repo path |
| `npm link` | Dev path | `npm link && vcp doctor` | Local developer path |
| Public PyPI | Planned unless published | `pip install vcp-cli` | Do not claim available today |
| Public npm / `npx` | Planned unless published | `npx vcp` | Do not claim available today |

## Safe first commands

```bash
vcp doctor
vcp evaluate --json
vcp audit-plan --json
vcp onboard --json
vcp adopt plan --json
```

## Add VCP to PRs

Use the workflow example in `ci-examples/github-actions/vcp-pr-gate.yml`.

## Practical chain

1. install or run locally;
2. inspect with `onboard` and `classify`;
3. use `adopt plan` or `adopt apply --dry-run` instead of blind copying;
4. add PR Gate for diff visibility;
5. only treat public distribution as real after an actual PyPI or npm publication.
