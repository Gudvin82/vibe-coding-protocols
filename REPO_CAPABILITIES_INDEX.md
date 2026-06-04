# REPO_CAPABILITIES_INDEX.md

## What VCP is

Vibe Coding Protocols is a two-track operating layer for AI-assisted delivery: New Project Track and Existing Project Track. It helps teams build new products from idea to controlled implementation and helps existing repositories add hardening, review gates, release discipline, and public-proof boundaries without pretending every project needs the same process depth.

## Capability map

| Capability | What it does | Evidence files |
|---|---|---|
| Two-track model | New projects + existing projects | `docs/two-track-model.md` |
| Spec Foundation | idea -> PRD/spec/backlog | `docs/spec-foundation.md` |
| Spec Quality Gate | checks if specs are implementation-ready | `docs/spec-quality-gate.md` |
| Brownfield hardening | controls AI-generated MVPs | `docs/walkthroughs/ai-mvp-hardening.md` |
| Review Diff | checks changed surfaces before merge | `vcp_cli/review_diff.py`, `docs/review-diff.md` |
| PR Gate | decision surface before merge | `docs/pr-gate.md` |
| Release Readiness | release checks | `docs/release-readiness.md` |
| Architecture Drift | catches memory/architecture mismatch | `docs/architecture-drift.md` |
| Score Badge | local readiness signal | `docs/score-badge.md` |
| Public Growth | SEO/GEO/AI visibility structure | `docs/public-growth/` |
| Project Memory | file-backed project memory | `docs/project-memory-model.md` |
| Pack Security | trust model for packs | `docs/protocol-pack-security.md` |
| Cards/Index | machine-readable discovery | `.vcp/index.json`, `.vcp/cards/` |
| Benchmarks | scenario validation | `benchmarks/ai-adoption/scenarios/` |

## What not to miss

- `.vcp/`
- `vcp_cli/`
- `templates/`
- `benchmarks/`
- `docs/walkthroughs/`
- `docs/public-growth/`

## What cannot be claimed without inspection

- no CLI maturity claim without CLI code/docs;
- no benchmark claim without benchmark inspection;
- no full evaluation without the audit manifest;
- no "just a prompt pack" claim without `.vcp`, CLI, workflows, benchmarks, review gates, and manifests inspection.
