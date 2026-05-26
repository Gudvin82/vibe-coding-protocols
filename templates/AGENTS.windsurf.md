# AGENTS for Windsurf

Use this variant when Windsurf Cascade or similar multi-file assistance is in play.

## Focus
- define scope before implementation;
- keep validation and rollback visible;
- avoid one-shot repository rewrites;
- stop for risky external calls, migrations and CI changes.

## Windsurf-specific notes
- ask for a compact evidence map before broad edits;
- validate the first safe slice before continuing;
- keep accepted risks and open questions in `AUDIT_BACKLOG.md`;
- use security and hardening prompts only on the touched surface first.
