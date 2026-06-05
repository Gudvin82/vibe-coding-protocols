# Vibe Coding Protocols v0.4.2 — Developer Experience, Integrations, and Public Site Readiness

v0.4.2 improves developer experience,
integration guidance,
public-site readiness,
ecosystem positioning,
and markdown/raw readability checks.
It clarifies current CLI/plugin/tooling limits,
adds per-IDE integration docs,
adds public-site readiness templates,
and strengthens defensive-only security positioning.

## What changed

- added `docs/cli.md` for the current script-first CLI story;
- added Windows guidance tables and practical shell fallback notes;
- added per-IDE integration docs for Claude Code,
  Codex,
  Cursor,
  Windsurf,
  GitHub Copilot
  and JetBrains/Junie;
- added `docs/ide-plugins.md` to separate manual integration from plugin maturity;
- added `docs/boundary-linting.md` to clarify current checks vs future AST/boundary work;
- added community feedback and Discussions guidance;
- strengthened `scripts/check-newlines.py` for markdown/raw readability;
- added ecosystem and security-tooling positioning docs;
- added a compact protocol index and metadata template;
- added public-site,
  crawler
  and schema templates;
- added synthetic bad-to-good examples.

## Defensive-only positioning

VCP is a controlled AI delivery toolkit.
It is not a hacking toolkit,
exploit framework,
pentest suite,
bug bounty automation suite,
red-team operator,
DDoS,
RAT,
phishing
or offensive security bundle.

## CLI and tooling honesty

VCP remains script-first.
A unified `vcp` CLI is still roadmap work,
and wrappers should be treated as experimental unless a command is explicitly documented and tested.

See:
- [cli.md](./cli.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
- [boundary-linting.md](./boundary-linting.md)

## Public site readiness

See:
- [public-site-readiness.md](./public-site-readiness.md)
- [seo-ai-crawler-readiness.md](./seo-ai-crawler-readiness.md)
- [../templates/public-site/README.md](../templates/public-site/README.md)

## Validation

Recommended checks:
- `python3 scripts/check-newlines.py`
- `python3 scripts/validate-links.sh`
- `bash scripts/check-version-consistency.sh`
- `bash scripts/check-toolkit.sh`
- `bash scripts/vibe-check.sh --audit --json`

## Known WARN-only items

Typical WARN-only items may still include:
- `API_KEY` marker in git history;
- `SECRET` marker in git history;
- public root `AGENTS.md`;
- public root `PROJECT_MAP.md`.
