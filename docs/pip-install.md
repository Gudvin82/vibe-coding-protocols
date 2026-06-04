# Python Install Paths

The most reliable current path is still repository-local execution:

```bash
python3 -m vcp_cli doctor
```

## Editable install

Use only if it passes in this release:

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

This is still a local repository install, not a PyPI release claim.
