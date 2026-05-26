# Pre-commit hook examples

Pre-commit hooks should stay fast.

Heavy scanners are usually better in CI than in a local pre-commit step.

## Simple git hook

```bash
#!/usr/bin/env bash
set -e
npm test
npm run lint
```

## Husky example

```bash
npx husky init
echo "npm test && npm run lint" > .husky/pre-commit
```

## Python project example

```bash
python -m pytest
ruff check .
```

## VCP hook idea

```bash
bash scripts/vibe-check.sh --starter
```
