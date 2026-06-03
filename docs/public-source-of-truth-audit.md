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
5. `README_ru.md`
6. `docs/versioning.md`
7. GitHub Releases
8. raw GitHub only as a weak supporting signal if it matches

For release-object questions, prefer direct release tag URLs over scraped release-list HTML.

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
grep -n "Repository package" README.md README_ru.md docs/versioning.md
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

## Public visibility findings after v0.6.4

As checked on June 3, 2026:

- `git ls-remote` and clean clone confirmed `main` and tag `v0.6.4` at `a2f789e5c37de9b17a851e7f1edb48d790ab5eea`.
- repository root HTML showed `README.md` with `Repository package: v0.6.4`.
- raw GitHub fetches were DNS-dependent from this environment and may be temporarily unavailable.
- GitHub Releases listing still showed `v0.6.3` as `Latest`.
- direct tag page for `v0.6.4` existed, which is weaker than a proper release object.

Interpretation:

GitHub HTML release listing may be cache/render dependent.
Stronger evidence: git refs, clean clone, raw `VERSION`, raw `README`, root repository sidebar, and direct release tag URL.

If the release listing still shows `v0.6.3` as Latest, that is not a repository-file failure.
It does mean the GitHub Release object for `v0.6.4` should be manually created or verified.

## Public source-of-truth verification order

1. verify git refs;
2. verify clean clone;
3. verify `VERSION`, `README.md`, `README_ru.md`, and `docs/versioning.md`;
4. verify CLI `version` and `evaluate`;
5. verify direct release tag URL;
6. verify GitHub Releases page and repository sidebar;
7. treat raw GitHub and scraped HTML as supporting signals, not the primary truth.

## Manual GitHub Release verification

After publishing a release object:

1. Open `https://github.com/Gudvin82/vibe-coding-protocols/releases`
2. Confirm the latest release title.
3. Confirm the tag points to the expected commit.
4. Confirm root repository sidebar shows the same latest release.
5. Confirm raw `VERSION` and raw `README.md` match.
6. If release listing appears stale in a bot or fetch path, prefer `git ls-remote`, clean clone, raw `VERSION`, and direct release tag URL as stronger evidence.
