# Install

VCP `v0.8.2` is installable from a local clone as a real CLI.
It still does not claim public PyPI, public npm, Homebrew, or native installer distribution unless those channels are actually published.

If you want the fastest first-use route after install, continue with `docs/10-minute-adoption-path.md`.

## Recommended install path

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor
vcp evaluate
```

## Restricted or offline-leaning fallback

Use this only when local build dependencies are already available:

```bash
python3 -m venv --system-site-packages .venv
. .venv/bin/activate
python3 -m pip install . --no-build-isolation
vcp doctor
```

## No-install fallback from clone

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli evaluate --json
```

## Important honesty notes

- build isolation can require build dependencies such as `setuptools` and `wheel`;
- `--no-build-isolation` is a fallback, not the default recommendation;
- direct user-site installs can fail because of permissions;
- a virtual environment is the recommended path.

## Honest install table

| Path | Status | Command | Notes |
|---|---|---|---|
| Clone + Python module | Stable | `python3 -m vcp_cli doctor` | Works without installation |
| Local package install in venv | Stable if validation passes | `python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install --upgrade pip setuptools wheel && python3 -m pip install . && vcp doctor` | Main `v0.8.2` install path |
| Local no-build-isolation fallback | Supported if local build deps already exist | `python3 -m venv --system-site-packages .venv && . .venv/bin/activate && python3 -m pip install . --no-build-isolation && vcp doctor` | Restricted environments only |
| Editable install | Dev path | `python3 -m pip install -e . && vcp doctor` | Useful for contributors |
| `pipx` local path | Supported if available and validation passes | `pipx install . && vcp doctor` | Local path only, not PyPI |
| Node local wrapper | Stable local wrapper | `npm run vcp -- doctor` | Local repo path |
| Public PyPI | Roadmap unless published | `pip install vcp-cli` | Do not claim available today |
| Public npm / `npx` | Roadmap unless published | `npx vcp` | Do not claim available today |

## Safe first commands

```bash
vcp doctor
vcp evaluate --json
vcp audit-plan --json
vcp onboard --json
vcp adopt plan --json
```
