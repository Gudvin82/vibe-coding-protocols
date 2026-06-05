# pip Install

Recommended path:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
```

Fallback for restricted environments:

```bash
python3 -m venv --system-site-packages .venv
. .venv/bin/activate
python3 -m pip install . --no-build-isolation
```

This repository does not claim `pip install vcp-cli` from public PyPI unless that publication actually happens.
