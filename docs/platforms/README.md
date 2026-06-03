# Platforms

VCP is documented for 25+ AI coding tools and workflows.
That does not mean 25+ official plugins.

## Status taxonomy

- `tested-local`: local CLI workflow was exercised directly
- `documented`: repository workflow is documented and supported in docs/cards
- `prompt-compatible`: works through pasted prompts or repo docs
- `rules-compatible`: works through rules files plus repo docs
- `cli-compatible`: works well when shell/CLI access is available
- `experimental`: guidance exists but real-world coverage is still thinner
- `not-official-plugin`: no official vendor plugin or marketplace claim

| Platform | Status | Best VCP entrypoint | Official plugin? |
|---|---|---|---|
| Claude Code | `documented` | `AGENTS.md` + `.vcp/index.json` | No |
| Codex CLI | `cli-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Cursor | `rules-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Windsurf | `rules-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| GitHub Copilot | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Gemini CLI | `documented` | `AGENTS.md` + `.vcp/index.json` | No |
| JetBrains Junie | `experimental` | `AGENTS.md` + `.vcp/index.json` | No |
| Cline | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Roo Code | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Continue | `rules-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Aider | `cli-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| OpenHands | `experimental` | `AGENTS.md` + `.vcp/index.json` | No |
| Devin | `documented` | `AGENTS.md` + `.vcp/index.json` | No |
| Replit Agent | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Lovable | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Bolt.new | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| v0 by Vercel | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Trae | `experimental` | `AGENTS.md` + `.vcp/index.json` | No |
| Zed AI | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Tabnine | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Sourcegraph Cody | `documented` | `AGENTS.md` + `.vcp/index.json` | No |
| Amazon Q Developer | `documented` | `AGENTS.md` + `.vcp/index.json` | No |
| Google Jules | `experimental` | `AGENTS.md` + `.vcp/index.json` | No |
| Qwen Code | `prompt-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| VS Code AI Assistants | `rules-compatible` | `AGENTS.md` + `.vcp/index.json` | No |
| Ollama Local Coding | `experimental` | `AGENTS.md` + `.vcp/index.json` | No |
| LM Studio Local Workflow | `experimental` | `AGENTS.md` + `.vcp/index.json` | No |

## How to use these pages

Each platform page should tell you:
- status;
- best entrypoint;
- what to paste into the tool;
- whether CLI use is recommended;
- limitations;
- whether an official integration exists.

If a page does not state official integration explicitly, assume the answer is no.
