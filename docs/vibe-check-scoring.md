# Vibe-Check Scoring

`vibe-check` reports a lightweight readiness score.
It does not claim security certification.

| Category | Points | What it means |
|---|---:|---|
| Structure | 25 | Required project files, route coverage and core memory references |
| Safety files | 25 | `.gitignore`, env policy, baseline docs and checksum coverage |
| Secret hygiene | 25 | Obvious leak prevention and public exposure checks |
| Content quality | warnings | Empty or barely filled key docs should not look like a strong pass |
| Optional scanners | bonus | Extra scanner signal, not part of the core score |

## Interpretation

- `core_score` is the main readiness signal.
- `scanner_bonus` is optional and separate.
- `placeholder_excluded` shows how many lines were filtered because they looked like obvious placeholders.
- `artifact_version_warnings` helps surface copied files that may be stale or missing markers.
- `content_quality_warnings` highlights files that exist but still look empty or non-actionable.
- `WARN` means attention is required, not failure by default.
- `FAIL` means fix before merge or deploy.
- `--strict` changes warning behavior.
- score is not a security certification.
