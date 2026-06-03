# Vibe Coding Protocols v0.6.4 — Source-of-Truth, PR Gate, and Public Trust Polish

v0.6.4 strengthens VCP’s public trust and adoption surfaces.
It adds a public source-of-truth audit, a strict version surface checker, first-class PR Gate / GitHub Action onboarding, a clearer install-to-PR-check-to-score-badge workflow, stronger proof walkthroughs, and refined Spec Kit bridge positioning without adding a new methodology layer.

## Included in this release

- Public source-of-truth audit guidance for Git refs, clean clone, docs, and weak public fetch paths.
- Strict `check-public-version-surfaces.py` coverage for current-version trust markers.
- PR Gate as a first-class adoption path with repo workflow and CI example alignment.
- A cleaner install -> run -> PR check -> badge adoption chain.
- Stronger proof walkthrough docs without fake metrics or guarantee language.
- More explicit complementary positioning for spec-first and non-spec-first workflows.
- Synced cards, index, manifests, and benchmark metadata for trust-surface validation.

## Boundaries preserved

- no new major methodology layer;
- no weakening of adaptive spec depth, review-diff, score, AI intake, or visual onboarding;
- no npm, npx, PyPI, or GitHub Marketplace publication claims unless actually published;
- no raw GitHub cache-forcing claims;
- no fake proof, KPI, compliance, or safety guarantees.

## Manual GitHub Release verification

After publishing a release object:

1. Open `https://github.com/Gudvin82/vibe-coding-protocols/releases`
2. Confirm the latest release title.
3. Confirm the tag points to the expected commit.
4. Confirm root repository sidebar shows the same latest release.
5. Confirm raw `VERSION` and raw `README.md` match.
6. If release listing appears stale in a bot or fetch path, prefer `git ls-remote`, clean clone, raw `VERSION`, and direct release tag URL as stronger evidence.
