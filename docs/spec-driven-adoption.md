# Spec-driven Adoption

Use this track when the request is still partly undefined and the real risk is shipping AI-generated output without a spec, adoption plan, or release gate.

## Flow

`idea/spec -> classify -> adoption plan -> task breakdown -> implementation check -> PR gate -> release check`

## When to use this track

- new feature scope is still ambiguous;
- AI generated an MVP but contracts or acceptance criteria are still fuzzy;
- a team wants a visible bridge from spec work into adoption and release control.

## How it differs from raw AI-MVP rescue

- raw AI-MVP rescue starts from an already messy repo and tries to stabilize it;
- spec-driven adoption starts earlier and keeps decisions reviewable before implementation expands;
- it is about safer adoption of spec artifacts, not about forcing heavyweight PRDs on every tiny change.

## Required surfaces

- feature spec;
- implementation plan;
- task breakdown;
- adoption proof;
- PR Gate result;
- release readiness output.

## CLI path

```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli spec quality-gate --json
python3 -m vcp_cli adopt plan --pack spec-foundation --json
python3 -m vcp_cli workflow plan --id spec-driven-adoption --json
python3 -m vcp_cli release-check --json
```

## Human review points

- confirm spec depth is appropriate;
- confirm acceptance criteria match the delivery slice;
- confirm task breakdown does not skip validation;
- confirm PR Gate state before merge;
- confirm release note and public surfaces before tagging.

## Boundaries

- not a guarantee of product success;
- not a hosted planning tool;
- not a replacement for human approval;
- not required for tiny, low-risk edits.
