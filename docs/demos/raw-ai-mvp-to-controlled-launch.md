# Raw AI MVP to Controlled Launch

This is the short killer demo for VCP practical adoption.

In `v0.8.7`, this demo is the short practical story for `docs/mvp-to-launch-path.md`.

Scenario:
“I have a raw AI-generated MVP. I need to understand what it is, what I should adopt first, what can break, and whether I can launch it with control.”

## Demo path

```bash
python3 -m pip install .
vcp doctor
vcp onboard --json
vcp classify --json
vcp adopt plan --pack brownfield-rescue --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
vcp release-check --json
vcp pr-gate explain --json
vcp dashboard build --output ./vcp-dashboard --json
```

## What this demo proves

- VCP gives a first route instead of a vague doc dump.
- VCP classifies whether the project is a new idea or an existing MVP.
- VCP produces a copy-list before any write action.
- VCP can preview safe adoption apply without mutating the target project.
- VCP surfaces release and launch-control gaps before a risky launch.
- VCP can turn that review into a local MVP-to-Launch dashboard and checklist path.

## What VCP detects in this story

- missing or weak project memory;
- missing review and release-control surfaces;
- unclear adoption boundary;
- missing launch/readiness checks.

## What VCP prevents in this story

- blind copy/paste adoption;
- unreviewed destructive writes;
- treating a raw AI MVP as ready just because it appears functional;
- flattening hardening, route selection, and launch checks into one vague “ship it” answer.

## Boundaries

This demo does not claim:
- production safety guarantees;
- launch guarantees;
- public package publication;
- automatic deployment;
- automatic architecture repair;
- guaranteed growth, ranking, or citation outcomes.

## Continue with

- `docs/mvp-to-launch-path.md`
- `docs/launch-decision-checklist.md`
- `docs/adoption-packs/saas-ai-mvp-hardening.md`
