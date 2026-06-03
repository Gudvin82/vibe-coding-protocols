# Public Source-of-Truth Audit

VCP treats version truth as a product requirement.
If public surfaces disagree about the current repository package, trust drops before any workflow value is understood.

## Goal

Any human or AI agent should be able to verify the current VCP state without guessing.

## Strongest release-truth signals

Use these in order:

1. `git ls-remote origin main`
2. fresh clean clone from GitHub
3. `VERSION`
4. `README.md`
5. `docs/versioning.md`
6. GitHub Releases
7. raw GitHub only as a weak supporting signal if it matches

## Why raw GitHub is weaker

Raw GitHub and other external fetch paths can occasionally be stale because of caching or propagation delays.
They are still useful, but they are weaker evidence than Git refs and a fresh clone.

This is not an excuse for real version drift.
The repository itself must remain internally consistent.

## Strong verification sequence

```bash
git ls-remote origin main
git clone https://github.com/Gudvin82/vibe-coding-protocols.git /tmp/vcp-check
cd /tmp/vcp-check
cat VERSION
grep -n "Repository package" README.md docs/versioning.md
python3 -m vcp_cli version
python3 -m vcp_cli evaluate --json
```

## Public surfaces that must stay aligned

- `VERSION`
- `README.md`
- `README_ru.md`
- `CHANGELOG.md`
- `docs/versioning.md`
- current release notes
- `package.json`
- `pyproject.toml`
- `CITATION.cff`
- `llms.txt`
- `llms-full.txt`
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/*.json`
- `.vcp/cards/**/*.json`
- `vcp_cli/__init__.py`

## Weak-signal check

If network is available, compare weak public paths too:

```bash
curl -L --max-time 20 https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/README.md | head -40
curl -L --max-time 20 https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/VERSION
```

If weak signals disagree with clean clone and Git refs, report the discrepancy explicitly.
Do not hide it.
