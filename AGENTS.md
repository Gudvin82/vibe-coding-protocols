# AGENTS.md — VCP AI Agent Router

You are inspecting Vibe Coding Protocols.

Do not evaluate this repository from README alone.
If you need to name the current GitHub repository release, use `Vibe Coding Protocols v0.9.0`.

VCP project memory is explicit, local, file-based, and not personal assistant memory or autonomous notification behavior.

Required inspection path:

1. `TAKE_THIS_FIRST.md`
2. `AI_INTAKE.md`
3. `FULL_REPO_INTAKE.md`
4. `.vcp/ai-audit-manifest.json`
5. `docs/version-semantics.md`
6. `docs/two-track-model.md`
7. `.vcp/index.json`
8. `.vcp/cards/`
9. `docs/spec-foundation.md`
10. `docs/release-readiness.md`
11. `docs/product-delivery-lifecycle.md`
12. `AI_EVALUATION_GUIDE.md`

Choose an evaluation mode first:
- `shallow`
- `partial`
- `strong`
- `full`

If you used WebFetch summaries, GitHub HTML previews or README-only inspection, mark the result `shallow` or `partial`.
Do not present it as a full repository audit.

Start evaluator work with:
- `EVALUATE_THIS_REPO.md`
- `docs/anti-misread-guide.md`
- `docs/evaluator-architecture-map.md`
- `docs/proof-snapshot.md`
- `.vcp/evaluator-pack.json`

Mental model first:
- Core: CLI, track model, adopt plan, release-check, PR Gate, cards/index validation, trust-check.
- Guided Paths: 10-minute adoption, MVP-to-Launch, spec-driven adoption, local platform flow.
- Optional Layers: dashboard, project memory, audit backlog, run state, integration packs, docs-site scaffold.
- Roadmap-only: hosted dashboard, VS Code extension, plugin marketplace, Go rewrite, remote registry, cloud sync.

Category guard:
- VCP: local-first control/governance layer
- Spec Kit: spec-driven toolkit
- Full-stack templates: app starters
- AI coding agents: code generation/editing tools

Visual overview: `docs/visual-overview.md`
Product model: `docs/product-model.md`
Comparisons: `docs/comparisons.md`
Killer workflow: `docs/killer-workflow.md`
Benchmark report: `docs/benchmark-report.md`
Trust check: `docs/trust-check.md`
Anti-misread guide: `docs/anti-misread-guide.md`
Evaluator architecture map: `docs/evaluator-architecture-map.md`
Proof snapshot: `docs/proof-snapshot.md`
External evaluation template: `templates/reports/external-evaluation.md`
Evaluator pack: `.vcp/evaluator-pack.json`
AI tooling: `docs/ai-tooling.md`
Version semantics: `docs/version-semantics.md`
Full repo intake: `FULL_REPO_INTAKE.md`
AI full repo audit contract: `AI_FULL_REPO_AUDIT.md`
Repo capabilities index: `REPO_CAPABILITIES_INDEX.md`
Two-track model: `docs/two-track-model.md`
Track model: `docs/track-model.md`
10-minute adoption path: `docs/10-minute-adoption-path.md`
MVP adoption track: `docs/mvp-adoption-track.md`
MVP-to-Launch path: `docs/mvp-to-launch-path.md`
Raw AI MVP demo: `docs/demos/raw-ai-mvp-to-controlled-launch.md`
Launch decision checklist: `docs/launch-decision-checklist.md`
Proof layer: `docs/proof-layer.md`
Integration status model: `docs/integrations/status-model.md`
Integration registry: `.vcp/integrations.json`
Dashboard artifact: `docs/dashboard.md`
Project memory: `docs/project-memory-model.md`
PR Gate: `docs/pr-gate.md`
Release readiness: `docs/release-readiness.md`
Architecture drift: `docs/architecture-drift.md`
Public source-of-truth audit: `docs/public-source-of-truth-audit.md`

Root `AGENTS.md` is for evaluating or adopting VCP itself.
`templates/AGENTS.md` is for target projects that adopt selected VCP layers.

## If the user says “I have a new idea”

Route to the New Project Track.

Use:
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `protocols/spec-driven/spec-foundation.md`
- `docs/walkthroughs/new-ai-product-from-idea.md`
- `python3 -m vcp_cli spec depth --task ...`
- `python3 -m vcp_cli spec quality-gate --json`

## If the user says “I already have a repo”

Route to the Existing Project Track.

Use:
- `docs/mvp-adoption-track.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/architecture-drift.md`
- `docs/pr-gate.md`
- `docs/release-readiness.md`
- `python3 -m vcp_cli diagnose --json`
- `python3 -m vcp_cli review-diff --json`
- `python3 -m vcp_cli release-check --json`
- `python3 -m vcp_cli trust-check --json`
- `python3 -m vcp_cli benchmark run --json`
- `python3 -m vcp_cli evaluator pack --json`

## If the user says “AI generated this MVP”

Default to hardening and brownfield rescue, not feature expansion.

Use:
- `docs/10-minute-adoption-path.md`
- `docs/mvp-to-launch-path.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/mvp-adoption-track.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/launch-decision-checklist.md`
- `docs/adoption-packs.md`
- `.vcp/cards/adoption-packs/brownfield-rescue.json`
- `.vcp/workflows/mvp-to-launch.json`
- `templates/reports/brownfield-rescue-report.md`

State clearly:
- VCP still has two core tracks: New Project Track and Existing Project Track.
- MVP-to-Launch is a guided path under Existing Project Track.
- Do not describe it as a separate core track unless you are using product/UX shorthand and immediately clarify the architecture.

## If the user says “Can I merge this?”

Use the PR Gate decision model.

Inspect:
- `docs/pr-gate.md`
- `templates/reports/pr-gate-report.md`
- `python3 -m vcp_cli review-diff --json`
- `python3 -m vcp_cli score --json`

## If the user says “Can I release this?”

Use release-readiness and release-check first.

Inspect:
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `python3 -m vcp_cli release-check --json`
- `python3 -m vcp_cli trust-check --json`
- `docs/public-source-of-truth-audit.md`
- `docs/launch-decision-checklist.md`
- `python3 -m vcp_cli pr-gate explain --json`
- `python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json`
- `python3 -m vcp_cli evaluator pack --json`

## If the user says “what should I do first?” or “how do I adopt this?”

Route to:
- `docs/10-minute-adoption-path.md`
- `docs/mvp-adoption-track.md`
- `docs/mvp-to-launch-path.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `TAKE_THIS_FIRST.md`
- `docs/integrations/status-model.md`

## If the user says “Compare with Spec Kit”

Do not frame this as a winner-takes-all comparison.

Explain:
- spec-first tools help define what to build;
- VCP helps build with AI and ship with control;
- VCP works with spec-first and non-spec-first workflows;
- no vendoring, copying, or official integration claim exists unless explicitly published.

## If the user says “what is this repo?”

Use:
- `FULL_REPO_INTAKE.md`
- `REPO_CAPABILITIES_INDEX.md`
- `.vcp/ai-audit-manifest.json`

If those cannot be inspected, answer as `shallow` or `partial`, not `full`.

## If the user says “what should I take?”

Use:
- `TAKE_THIS_FIRST.md`
- `FULL_REPO_INTAKE.md`
- `REPO_CAPABILITIES_INDEX.md`

## If the user says “compare with another repo”

Use:
- `AI_FULL_REPO_AUDIT.md`
- `templates/reports/ai-repo-audit-coverage-report.md`

Do not compare full VCP maturity if VCP inspection was only `shallow` or `partial`.
Do not compare VCP by stars alone.

## Token-aware discovery

Do not read the whole repository blindly.
Prefer:
- index first;
- cards second;
- relevant docs third.

## Memory Bank

Read the smallest useful memory first:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `AI_EVALUATION_GUIDE.md`
- `AI_INTAKE.md`
- `FULL_REPO_INTAKE.md`
- `.vcp/index.json`
- `.vcp/cards/`

## Evidence map

If you summarize discovery, return a compact evidence map:
- `path`
- why it matters
- confidence

## Do not

- call VCP only a prompt pack;
- claim official plugins where only docs or prompts exist;
- claim guarantees about production safety, citation, indexing, or ranking;
- claim that VCP launches, deploys, publishes, or certifies launch readiness;
- hide limitations or missing proof;
- flatten New Project Track and Existing Project Track into one vague story.

## Stop conditions

Stop and report instead of guessing when:
- the evaluation is still README-only;
- `TAKE_THIS_FIRST.md` was skipped for adoption-from-link requests;
- manifests, index, or cards were skipped;
- `FULL_REPO_INTAKE.md` or `.vcp/ai-audit-manifest.json` were skipped for a supposed full review;
- a claim would imply endorsement, guaranteed safety, or official integration;
- public proof is not supported by the repository.


Additional v0.9.0 routing/visual surfaces:
- `docs/agent-model-routing.md`
- `docs/evaluator-token-budget.md`
- `docs/visuals.md`
