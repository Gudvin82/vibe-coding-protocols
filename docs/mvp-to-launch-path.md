# MVP-to-Launch Path

Repository package: `v0.8.9`

The MVP-to-Launch Path is a short, guided path for a raw or semi-working AI-generated MVP that already exists but is not yet launch-controlled.

It is a specialized guided path under Existing Project Track.

## Path

```text
intake -> classify -> surface scan -> route -> risk backlog -> proof check -> PR Gate approval -> launch decision
```

## Recommended command flow

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp adopt plan --pack saas-ai-mvp-hardening --json
vcp release-check --json
vcp pr-gate explain --json
vcp dashboard build --output ./vcp-dashboard --json
```

Optional if project memory and backlog surfaces are in use:

```bash
vcp memory validate .vcp/project-memory.example.json --json
vcp backlog summarize .vcp/audit-backlog.example.json --json
vcp metrics board --json
```

## Step-by-step meaning

- `doctor`: confirm the repo has the minimum local VCP surfaces and detect obvious setup gaps.
- `onboard`: produce the shortest practical orientation path for the current repo.
- `classify`: decide whether the repo behaves like a new project or an existing MVP and suggest a route.
- `adopt plan --pack brownfield-rescue --copy-list`: surface the minimal adoption slice before any write action.
- `adopt plan --pack saas-ai-mvp-hardening --json`: inspect SaaS-specific control gaps when auth, billing, data, or shared-user risk is involved.
- `release-check`: summarize launch and release-control gaps that still need review.
- `pr-gate explain`: make the approval model explicit before merge or launch decisions.
- `dashboard build`: generate a local review artifact that ties route, packs, proof, backlog, and launch view together.
- `memory validate`, `backlog summarize`, `metrics board`: optionally confirm that memory, backlog, and local metrics reflect reality.

## When to use this path

Use it when:
- an AI-built MVP already exists;
- the MVP kind of works, but safety or launch readiness is unclear;
- a user asks, “can I show this?”, “can I launch this?”, or “what risks remain?”;
- you need a reviewable local launch-control path instead of another vague planning document.

## When not to use this path

Do not use it when:
- there is only an idea or spec and no real repo yet;
- the work is purely a spec/planning exercise;
- the task expects VCP to deploy, publish, or certify production readiness.

## Required inputs

- a repository or working MVP;
- enough local files to inspect project shape;
- human willingness to review route, backlog, proof, and PR Gate outputs.

## Expected outputs

- an initial route decision;
- adoption pack recommendations;
- a copy-list or adoption plan;
- a release-check summary;
- a PR Gate review framing;
- a local dashboard artifact;
- a launch decision aid.

## Stop conditions

Stop and escalate when:
- install/run path is still broken;
- required environment variables are unknown;
- auth, billing, or data boundaries are high-risk and still undocumented;
- proof layer is missing for claims that sound stronger than the evidence;
- PR Gate status is still `block` or `needs-human-review`.

## Human review points

Human review is required for:
- route and pack choice when risk is ambiguous;
- PR Gate interpretation;
- launch decision status;
- any confirmed apply step into a real target repository;
- any claim that sounds like launch approval or production certification.

## Safe launch boundaries

VCP does not launch, deploy, publish, or guarantee readiness.
It provides a local, reviewable launch-control path.

## Relationship to nearby docs

- `docs/10-minute-adoption-path.md`: the shortest entry before deeper launch control.
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`: the short demo version of this path.
- `docs/adoption-packs/saas-ai-mvp-hardening.md`: the SaaS-focused pack inside this path when business-risk boundaries are present.
- `docs/demos/contracts-first-ai-mvp.md`: a specialized scenario inside this path when web/backend/contracts drift matters.
- `docs/launch-decision-checklist.md`: the final review artifact once route, proof, backlog, and PR Gate state are visible.
- `.vcp/workflows/mvp-to-launch.json`: the machine-readable planning view of the path.
