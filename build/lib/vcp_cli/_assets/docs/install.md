# Install

Preferred local install path:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor
```

Restricted environment fallback:

```bash
python3 -m venv --system-site-packages .venv
. .venv/bin/activate
python3 -m pip install . --no-build-isolation
vcp doctor
```

Notes:
- build isolation may require build dependencies;
- no-build-isolation should only be used when local build deps are already present;
- direct user-site installs can fail due to permissions;
- `python3 -m vcp_cli doctor` remains the no-install fallback.
