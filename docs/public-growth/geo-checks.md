# GEO Checks

`vcp public-growth check` is the practical CLI surface for public-growth readiness.

It checks repository evidence for:
- AI-readable files like `llms.txt`, `llms-full.txt`, and `ai.txt`;
- citation and trust metadata;
- glossary, FAQ, comparison, and proof surfaces;
- public-growth checklists and case-study presence;
- source-of-truth and release evidence.

## Output model

The command now returns:
- `pass`
- `warn`
- `block`

It also lists:
- missing signals;
- ready signals;
- recommendations;
- network limits when `--site` is used.

## Boundaries

- no ranking guarantees;
- no AI Overview or answer-engine citation guarantees;
- no fake reviews;
- no black-hat SEO.

## Optional network mode

If `--site` is used, the command may attempt a simple fetch.
If network is unavailable, it must return `network_unavailable` instead of pretending success or failure.

Treat `network_unavailable` as a visibility limit, not as proof that a site is broken.
