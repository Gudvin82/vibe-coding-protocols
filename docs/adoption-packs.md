# Adoption Packs

Adoption packs help teams take a focused slice of VCP instead of copying the whole repository.

## Core packs

### New Project Pack

Use when:
- idea stage;
- founder brief;
- greenfield MVP;
- new AI-assisted product needs structure before implementation.

Start with:
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `protocols/spec-driven/spec-foundation.md`
- `docs/walkthroughs/new-ai-product-from-idea.md`

### Existing MVP Pack

Use when:
- there is already a working app before production;
- validation exists, but architecture and review control are weak.

Start with:
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/pr-gate.md`
- `docs/release-readiness.md`

### Brownfield Rescue Pack

Use when:
- a repository already exists;
- AI-generated changes are real but discipline is weak;
- architecture drift, hidden backlog, or release confusion are already visible.

Start with:
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/architecture-drift.md`
- `docs/release-readiness.md`
- `templates/reports/brownfield-rescue-report.md`

Do not use when:
- the project is still only an idea and no repository exists yet.

### Production Pack

Use when:
- real users exist;
- release pressure exists;
- PR Gate and release-control discipline must be visible.

## Selection principle

Pick the smallest pack that gives you control.

If you are not sure, first classify the repository by track:
- New Project Track
- Existing Project Track

Then choose the pack.
