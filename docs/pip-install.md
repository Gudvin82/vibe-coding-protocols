# Python Install Paths

`v0.8.1` is the first release that treats `python3 -m pip install .` as a first-class local install path.

## Install from local clone

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m pip install .
vcp doctor
vcp evaluate --json
vcp audit-plan --json
vcp onboard --json
```

## Editable install

```bash
python3 -m pip install -e .
vcp doctor
vcp evaluate --json
vcp onboard --json
```

## `pipx` local install

If `pipx` is available, local path testing can use:

```bash
pipx install .
vcp doctor
```

This remains a local repository install path, not a public PyPI claim.

Do not say:
- `pip install vcp-cli`
- `pipx install vcp-cli`

unless the package is actually published to PyPI.
