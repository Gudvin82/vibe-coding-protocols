# MVP Adoption Track

Use this track when you already have a raw or semi-working AI-generated MVP and the real problem is safe control, not more feature sprawl.

Track path:
`intake -> active surfaces -> first user journey -> scope boundary -> launch check`

## 1. Intake

Goal: understand what the project is before changing it.

Use:
- `python3 -m vcp_cli onboard --json`
- `python3 -m vcp_cli classify --json`
- `docs/two-track-model.md`

Questions to answer:
- is this New Project Track or Existing Project Track;
- is the real blocker architecture, release control, environment clarity, or missing validation;
- is the MVP safe enough for a bounded adoption slice.

## 2. Active surfaces

Goal: identify the surfaces that already govern the MVP.

Inspect:
- README and install path;
- environment/setup path;
- architecture memory and backlog;
- tests or validation path;
- release/readiness surfaces;
- PR Gate and proof surfaces.

Map them to VCP surfaces such as:
- `docs/architecture-drift.md`
- `docs/release-readiness.md`
- `docs/pr-gate.md`
- `docs/proof-pack.md`
- `docs/10-minute-adoption-path.md`

## 3. First user journey

Goal: define the first real path a user must complete.

Examples:
- sign up -> first value;
- upload -> review -> publish;
- prompt -> generated output -> approval;
- intake form -> answer -> share/export.

Do not overbuild this step.
Use it to decide where VCP should add control first.

## 4. Scope boundary

Goal: keep the first adoption slice small and safe.

Prefer:
- route selection;
- copy-list generation;
- dry-run apply preview;
- release/readiness checks;
- PR Gate visibility.

Avoid:
- broad repo rewrites;
- destructive adoption apply;
- pretending the MVP is production-safe because tooling exists.

## 5. Launch check

Goal: decide whether the MVP is ready for a controlled next release.

Use:
- `python3 -m vcp_cli release-check --json`
- `python3 -m vcp_cli review-diff --json`
- `python3 -m vcp_cli public-growth check --json`

Expected output:
- main risks surfaced;
- first control slice defined;
- launch blockers visible;
- next safe step clear.
