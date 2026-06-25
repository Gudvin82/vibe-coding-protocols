# Agent Rule Profiles

Repository package: `v0.9.4`

VCP ships three context profiles for AI coding sessions:

- `nano`: tiny always-on constraints for any session
- `mini`: default profile for most work
- `full`: audit, release, evaluation, and full-repo inspection

Each profile is constraint-first:
- do not edit before inspection;
- do not claim tests passed unless run;
- do not broaden scope;
- do not treat roadmap as shipped;
- do not skip trust-check for release-sensitive changes.

## Files

- `templates/agents/profiles/vcp-agent-rules.nano.md`
- `templates/agents/profiles/vcp-agent-rules.mini.md`
- `templates/agents/profiles/vcp-agent-rules.full.md`
- `.vcp/agent-rule-profiles.json`

## CLI

- `python3 -m vcp_cli profiles list --json`
- `python3 -m vcp_cli profiles show --id mini --json`
