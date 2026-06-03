# Product Delivery Lifecycle

VCP can support both new products and existing AI-assisted projects.

```text
Idea
↓
AI Intake
↓
Route
↓
Spec Depth
↓
PRD / Feature Spec / No-spec
↓
Tasks
↓
Project Backlog
↓
Architecture Memory
↓
Implementation
↓
Review Diff / Post-Task Review
↓
Diagnostics
↓
Release Gate
↓
Operations / Public Growth
```

## Minimum path

```text
route -> backlog -> review -> validation
```

## Full path

```text
intake -> spec depth -> spec -> backlog -> architecture -> workflow -> review -> diagnostics -> release
```

## Skip path

```text
tiny fix -> skip-check -> validation -> done
```

## Stage guide

### Idea
- Purpose: capture what the user is trying to build or change.
- Key files: `AI_INTAKE.md`, `START_HERE.md`
- CLI: `python3 -m vcp_cli init`
- Output: initial direction
- Stop conditions: scope is still unclear or risky assumptions remain

### AI Intake
- Purpose: classify the project and risk shape.
- Key files: `AI_INTAKE.md`
- CLI: `python3 -m vcp_cli route --profile production --json`
- Output: route candidate
- Stop conditions: production, payments, auth, or public claims are still unclassified

### Route
- Purpose: choose the right VCP workflow.
- Key files: `docs/protocol-index.md`, `docs/adoption-packs.md`
- CLI: `python3 -m vcp_cli route --profile spec-first --json`
- Output: route + pack recommendation
- Stop conditions: route is still ambiguous

### Spec Depth
- Purpose: choose no-spec, spec-lite, full-spec, or governed-spec.
- Key files: `docs/adaptive-spec-depth.md`
- CLI: `python3 -m vcp_cli spec depth --task "build a customer portal" --json`
- Output: recommended spec depth
- Stop conditions: risk signals conflict with a tiny-fix assumption

### PRD / Feature Spec / No-spec
- Purpose: match artifact depth to risk.
- Key files: `templates/specs/PRD.md`, `templates/specs/FEATURE_SPEC.md`
- CLI: `python3 -m vcp_cli spec questions --idea "build a customer portal" --json`
- Output: clarified spec path
- Stop conditions: requirements or validation are still fuzzy

### Tasks
- Purpose: turn scope into executable tasks.
- Key files: `templates/specs/TASKS.md`
- CLI: `python3 -m vcp_cli spec summary --json`
- Output: task breakdown
- Stop conditions: validation tasks are missing

### Project Backlog
- Purpose: keep delivery state visible.
- Key files: `PROJECT_BACKLOG.md`
- CLI: `python3 -m vcp_cli backlog report --json`
- Output: prioritized next work
- Stop conditions: follow-up remains only in chat

### Architecture Memory
- Purpose: keep cross-layer decisions visible.
- Key files: `PROJECT_MAP.md`, `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- CLI: no dedicated writer; check through route discipline
- Output: updated memory
- Stop conditions: cross-layer impact is undocumented

### Implementation
- Purpose: make the change.
- Key files: route-specific docs and selected pack files
- CLI: `python3 -m vcp_cli adopt --pack spec-first --dry-run --json`
- Output: implemented diff
- Stop conditions: scope drift or unsafe assumptions appear

### Review Diff / Post-Task Review
- Purpose: check what changed before merge.
- Key files: `docs/review-diff.md`, `protocols/review/post-task-code-review.md`
- CLI: `python3 -m vcp_cli review-diff --json`
- Output: risk and follow-up guidance
- Stop conditions: validation is missing or risk is understated

### Diagnostics
- Purpose: assess project/process readiness by layer.
- Key files: `docs/diagnostics.md`
- CLI: `python3 -m vcp_cli diagnose --json`
- Output: readiness warnings
- Stop conditions: high-priority gaps remain unresolved

### Release Gate
- Purpose: verify repo-level readiness.
- Key files: `docs/github-action.md`, `docs/release-checklist.md`
- CLI: `python3 -m vcp_cli score --json`
- Output: release readiness signal
- Stop conditions: manifests, cards, workflows, or validation are broken

### Operations / Public Growth
- Purpose: support post-release loops.
- Key files: `protocols/operations/production-error-capture.md`, `protocols/public-growth/public-growth-playbook.md`
- CLI: `python3 -m vcp_cli diagnose --profile production --json`
- Output: operational or public-growth follow-up
- Stop conditions: evidence is still anecdotal or claims are unsupported
