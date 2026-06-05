# PR Gate Action Template

Use `ci-examples/github-actions/vcp-pr-gate.yml` as a copy-paste workflow template.

Local equivalent checks include:

```bash
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli release-check --json
python3 -m vcp_cli pr-gate explain --json
```

Warn and block states must still be interpreted by humans.
