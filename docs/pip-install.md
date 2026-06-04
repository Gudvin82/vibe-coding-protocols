# Python Install Paths

`v0.8.2` recommends a virtual environment first.

## Recommended path

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor
vcp evaluate --json
vcp audit-plan --json
vcp onboard --json
```

## Restricted environment fallback

```bash
python3 -m venv --system-site-packages .venv
. .venv/bin/activate
python3 -m pip install . --no-build-isolation
vcp doctor
```

Use the fallback only when local build dependencies are already available.

## Why this guidance exists

- build isolation may try to fetch build requirements;
- user-site installs may fail due to permissions;
- venv installs are more repeatable;
- `python3 -m vcp_cli doctor` remains the no-install fallback from a clone.

## Do not overclaim

Do not say:
- `pip install vcp-cli`
- `pipx install vcp-cli`

unless the package is actually published to PyPI.
