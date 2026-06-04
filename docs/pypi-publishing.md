# PyPI Publishing

`v0.8.0` makes the Python package PyPI-ready, but publication remains a manual maintainer action.

## Before publishing

1. Create or confirm a PyPI account.
2. Check package name availability for `vcp-cli`.
3. Create a PyPI API token or configure trusted publishing.
4. Add `PYPI_API_TOKEN` only if token-based publication is chosen.
5. Test the package locally:

```bash
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install .
vcp doctor
```

## GitHub workflow

This repository includes:

- `.github/workflows/publish-pypi.yml`

It is intentionally conservative:
- triggered on GitHub Release publication;
- builds the package;
- publishes only after maintainer configuration;
- does not assume secrets already exist.

## Important honesty rules

Do not claim:
- `pip install vcp-cli`
- `pipx install vcp-cli`

until public PyPI publication is real.
