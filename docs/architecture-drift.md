# Architecture Drift

Architecture Drift check helps catch when AI-assisted changes alter project structure without updating project memory.

## Drift indicators

- new top-level directory not reflected in `PROJECT_MAP.md`;
- dependency or package changes without registry or update note;
- new API or integration without third-party intake;
- cross-layer changes without architecture note;
- changed public surface without docs or release note;
- new workflow or CI behavior without PR Gate note;
- spec or task changed but backlog was not updated.

## Output

The report should capture:

- observed change;
- expected memory update;
- risk;
- next action;
- accepted-risk option.

## Why it matters

Architecture drift is one of the most common ways AI-assisted repositories lose control while still looking productive.

## Related files

- `templates/reports/architecture-drift-report.md`
- `docs/project-memory-model.md`
- `docs/release-readiness.md`
- `docs/pr-gate.md`
