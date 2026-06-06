# Public Evaluation Kit

<!-- vcp-version: v0.9.2 -->
<!-- methodology-version: v1.4 -->

Read these 7 files.
Run these 4 commands.
Return an evaluation receipt.
Use this rubric.

Required files:
- `README.md`
- `START_HERE.md`
- `EVALUATE_THIS_REPO.md`
- `.vcp/evaluator-pack.json`
- `docs/integrations/agent-kits.md`
- `docs/proof-snapshot.md`
- `docs/control-spine.md`
- `docs/flagship-demo.md`

Commands:
```bash
python3 -m vcp_cli trust-check --json
python3 -m vcp_cli evaluator pack --json
python3 -m vcp_cli benchmark run --json
python3 -m vcp_cli catalog list --json
```

Rubric:
- category correctness
- shipped/optional/roadmap separation
- proof surfaces
- CLI/tooling
- adoption value
- limitations

Do not call the AI-tooling layer an official plugin suite unless the repository explicitly ships one.
