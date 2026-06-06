<!-- vcp-version: v0.8.9 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: EVALUATE_VCP_REPOSITORY_PROMPT -->
<!-- vcp-version: v0.8.2 -->

You are evaluating Vibe Coding Protocols.

Do not judge from README alone.

First inspect:
- AI_EVALUATION_GUIDE.md
- AI_INTAKE.md
- START_HERE.md
- docs/install.md
- docs/glossary.md
- docs/protocol-index.md
- docs/adoption-packs.md
- docs/cli.md
- docs/geo-ai-visibility.md
- docs/page-templates.md
- docs/project-backlog.md
- .vcp/manifests/
- benchmarks/ai-adoption/
- commands/
- protocols/

Then run or review outputs for:
- python3 -m vcp_cli doctor
- python3 -m vcp_cli score --json
- python3 -m vcp_cli benchmark run
- python3 -m vcp_cli manifest validate

Return a structured evaluation with:
- version inspected
- files inspected
- commands run
- current capabilities
- limitations
- fair scores by category
- whether evaluation is full or shallow
- confidence level

If you skipped glossary or public-growth docs, say that terminology and public-maturity judgments are shallow.
