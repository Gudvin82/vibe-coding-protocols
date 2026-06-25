# AI Review Engines

Repository package: `v0.9.5`

VCP can be used alongside dedicated AI review engines such as
OpenCodeReview-style tools.

That comparison matters because these tools look adjacent from the outside, but
they solve different parts of the delivery problem.

## Short version

- AI review engines focus on diff/file inspection and review findings.
- VCP focuses on governance, route selection, trust-check, PR Gate, proof
  surfaces, and release evidence around AI-assisted delivery.

## Honest split of responsibility

Use a dedicated AI review engine when you want:
- more review signal over a diff;
- structured findings before merge;
- file-level or PR-level risk detection;
- a review-focused UX.

Use VCP when you want:
- to decide which delivery/adoption route applies;
- to control how AI-generated work is adopted or hardened;
- to require trust-check, proof, and release evidence;
- to guide a team/client rollout, not only a code review event.

## Where VCP complements review engines

VCP can wrap the wider process around review output:
- `review-diff` for local change classification;
- `trust-check` for public/release surface consistency;
- `PR Gate` for explicit merge framing;
- `Evidence Bundle` for auditability;
- `Client Adoption Playbook` for team/client rollout.

## What VCP does not claim here

VCP does not currently claim:
- a built-in line-level review-comment engine;
- autonomous defect review across every PR host;
- guaranteed detection of bug/security classes such as NPE, XSS, SQLi, or
  thread-safety issues.

## Practical adoption model

If a team already has a strong AI review engine:
1. keep that tool for diff/file review;
2. use VCP for route selection and rollout discipline;
3. require trust-check and PR Gate before release-facing claims;
4. keep proof surfaces and limitations synced.

That is the intended relationship: complement, not replacement.
