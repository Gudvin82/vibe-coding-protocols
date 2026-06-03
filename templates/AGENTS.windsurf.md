<!-- vcp-artifact: AGENTS_WINDSURF -->
<!-- vcp-version: v0.6.3 -->
<!-- methodology-version: v1.4 -->

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

## Model routing / token-aware discovery

When broad code discovery is needed:
1. read Memory Bank first;
2. use a read-only discovery pass when available;
3. require an evidence map with `path:line`, symbol, snippet, why it matters and confidence;
4. keep Cascade scoped to the files proved relevant by that map;
5. use a separate review pass before risky merge or deploy work.

## Remote safety

Before setup, template installation, push, PR, release or deploy:
- inspect `git remote -v`;
- confirm this is your project repository, not the source toolkit repository;
- do not push to the source toolkit repository by mistake;
- stop and ask when remote origin is unclear.
