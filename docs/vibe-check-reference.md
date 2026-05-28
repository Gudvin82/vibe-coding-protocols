# Vibe-Check Reference

The source script is [scripts/vibe-check.sh](../scripts/vibe-check.sh).
It is intentionally long because it bundles lightweight checks, doctor output, init routing and JSON modes in one Bash entrypoint.

## What it does

`vibe-check` provides:
- route-aware structure checks;
- safety-file checks;
- secret hygiene heuristics;
- content-quality warnings;
- artifact version hints;
- optional scanner integration;
- doctor and onboarding summaries.

## Main modes

- `--starter`
- `--hardening`
- `--audit`
- `--doctor`
- `--init-report`
- `--update-advice`

## Output fields

Key JSON fields include:
- `score`
- `core_score`
- `scanner_bonus`
- `placeholder_excluded`
- `artifact_version_warnings`
- `content_quality_warnings`
- `status`
- `mode`

## Known limitations

The checks are heuristic.
They do not replace:
- tests;
- human review;
- security review;
- legal or compliance review.

See also:
- [docs/vibe-check-scoring.md](./vibe-check-scoring.md)
- [docs/vibe-check-doctor.md](./vibe-check-doctor.md)
- [docs/vibe-check-init-report.md](./vibe-check-init-report.md)
- [docs/update-copied-artifacts.md](./update-copied-artifacts.md)
