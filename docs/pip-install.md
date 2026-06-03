# Editable Python Install

This page documents the local editable install path for VCP.
It is not a claim that VCP is already published to PyPI.

Status:
- environment-dependent local development path;
- may require standard Python packaging/build tooling such as `setuptools` and `wheel`;
- in restricted or offline environments, prefer `python3 -m vcp_cli ...`.

## macOS / Linux

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
vcp evaluate
vcp score --badge markdown
```

## Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e .
vcp evaluate
vcp score --badge markdown
```

## What this means

- local development path when packaging prerequisites are available;
- convenient if you want a `vcp` command in a checked-out repo;
- not the same as public `pip install` from PyPI.
