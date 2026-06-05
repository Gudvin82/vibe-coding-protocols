# Synthetic Case: Post-Task Review Found Critical Issue

Synthetic or sanitized label: synthetic

## Scenario summary
A meaningful AI-generated diff looked complete but review found a blocking public-contract issue.

## Before
- active diff looked acceptable;
- validation alone did not catch the contract drift.

## VCP route selected
- Post-Task Code Review

## Artifacts used
- loop-code-review command
- prompt template
- code review report

## What changed
- blocking finding documented;
- fix applied;
- validation rerun;
- fresh acceptance review performed.

## Validation
- route-specific checks;
- review plus validation green.

## Remaining risks
- independent human review may still be needed for sensitive domains.

## Redaction checklist
- no real repo names;
- no real API details.
