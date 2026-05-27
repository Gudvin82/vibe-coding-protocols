# Vibe-Check Scoring

`vibe-check` reports a lightweight readiness score.
It does not claim security certification.

| Category | Points | What it means |
|---|---:|---|
| Structure | 25 | Required project files, route coverage and core memory references |
| Safety files | 25 | `.gitignore`, env policy and baseline docs |
| Secret hygiene | 25 | Obvious leak prevention and public exposure checks |
| Optional scanners | bonus | Extra scanner signal, not part of the core score |

## Interpretation

- `core_score` is the main readiness signal.
- the current core score is normalized from structure, safety files and secret hygiene checks.
- `scanner_bonus` is optional and separate.
- `WARN` means attention is required, not failure by default.
- `FAIL` means fix before merge or deploy.
- `--strict` changes warning behavior.
- score is not a security certification.

## Placeholder transparency

- `placeholder_excluded` shows how many lines were filtered because they looked like obvious placeholders such as `example`, `changeme`, `sample` or `[FILL IN]`.
- if the count is high, review whether the filter might be hiding a false negative.

## Artifact version warnings

- `artifact_version_warnings` helps surface copied files that may be stale or missing markers.
- this is a review hint, not proof that the file is wrong.
