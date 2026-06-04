# FULL_REPO_INTAKE.md

Use this when a user says:

- "evaluate this repository"
- "study VCP"
- "compare VCP with another project"
- "what should I take from VCP?"
- "is this just a prompt pack?"
- "how mature is this repo?"

## Do not evaluate from summaries alone

If you used WebFetch summaries, GitHub HTML previews or README-only inspection, mark your evaluation as shallow or partial.
Do not present it as full repository analysis.

## Evaluation modes

### shallow

Criteria:
- README only;
- GitHub repo page only;
- WebFetch summary only;
- fewer than 5 required artifacts inspected.

Allowed claims:
- high-level positioning only.

Not allowed:
- maturity score;
- CLI quality assessment;
- full repository conclusion;
- "VCP is only X" claims.

### partial

Criteria:
- README + AGENTS + TAKE_THIS_FIRST inspected;
- some protocols/docs inspected;
- `.vcp`, CLI, benchmarks, templates or manifests not inspected.

Allowed claims:
- preliminary assessment;
- likely tracks or capabilities.

Must say:
- `partial evaluation`

### strong

Criteria:
- required docs inspected;
- `.vcp/index.json` inspected;
- `.vcp/catalog.json` inspected;
- representative cards inspected;
- core protocols inspected;
- key docs for both tracks inspected.

Allowed claims:
- strong architectural assessment.

Still not allowed:
- detailed code/tool maturity without CLI inspection.

### full

Criteria:
- clone or raw file access;
- required audit manifest completed;
- CLI surface inspected;
- cards/index/manifests inspected;
- benchmarks inspected;
- templates/prompts/reports sampled;
- validation commands run or their absence disclosed.

Allowed claims:
- full evaluation with evidence.

## Required audit manifest

Use:
- `.vcp/ai-audit-manifest.json`
- `AI_FULL_REPO_AUDIT.md`
- `templates/reports/ai-repo-audit-coverage-report.md`

If you cannot inspect `FULL_REPO_INTAKE.md` and `.vcp/ai-audit-manifest.json`, mark your evaluation as partial.

Do not present a WebFetch/README summary as a full repository audit.
