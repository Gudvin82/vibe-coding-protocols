from __future__ import annotations

import html
from pathlib import Path
from typing import Any

from . import classify as classify_cmd
from . import metrics_cmd
from .utils import dump_json, load_json, methodology_version, print_output, repo_root, repo_version

OUTPUT_FILES = [
    "index.html",
    "README.md",
    "dashboard.md",
    "metrics.json",
    "audit-backlog-summary.json",
    "release-readiness.json",
    "launch-readiness.json",
    "integration-status.json",
    "project-map.json",
    "run-history.json",
]


def _integration_payload(root: Path) -> dict[str, Any]:
    path = root / ".vcp" / "integrations.json"
    if not path.exists():
        return {"version": repo_version(root), "items": []}
    return load_json(path)


def _release_payload(metrics: dict[str, Any]) -> dict[str, Any]:
    return metrics["release_readiness"]


def _backlog_payload(metrics: dict[str, Any]) -> dict[str, Any]:
    return metrics["audit_backlog"]


def _project_memory_payload(root: Path) -> dict[str, Any]:
    live_path = root / ".vcp" / "project-memory.json"
    example_path = root / ".vcp" / "project-memory.example.json"
    path = live_path if live_path.exists() else example_path
    if not path.exists():
        return {"present": False, "source": None, "decision_count": 0, "risk_count": 0, "blocker_count": 0}
    data = load_json(path)
    return {
        "present": True,
        "source": str(path.relative_to(root)),
        "decision_count": len(data.get("decisions", [])),
        "risk_count": len(data.get("risks", [])),
        "blocker_count": len(data.get("blockers", [])),
    }


def _run_history_payload(root: Path) -> dict[str, Any]:
    runs_dir = root / ".vcp" / "runs"
    items = sorted(runs_dir.glob("*.json")) if runs_dir.exists() else []
    latest = items[-1].name if items else None
    source = "live" if items and any(path.name != "example-run-state.json" for path in items) else "example-only" if items else "missing"
    return {"present": runs_dir.exists(), "count": len(items), "latest": latest, "source": source}


def _project_map_payload(root: Path, metrics: dict[str, Any], integrations: dict[str, Any]) -> dict[str, Any]:
    return {
        "repository_package_version": metrics["repository_package_version"],
        "methodology_version": metrics["methodology_version"],
        "core_story": "Build with AI. Choose the right track. Adopt safely. Ship with control.",
        "tracks": {
            "core": ["New Project Track", "Existing Project Track"],
            "guided_paths": ["MVP-to-Launch Path"],
        },
        "key_docs": [
            "docs/10-minute-adoption-path.md",
            "docs/mvp-to-launch-path.md",
            "docs/local-platform-flow.md",
            "docs/launch-decision-checklist.md",
            "docs/integration-packs.md",
            "docs/dashboard.md",
        ],
        "workflows": [
            ".vcp/workflows/mvp-to-launch.json",
        ],
        "project_memory_source": metrics["project_memory"]["source"],
        "run_history_source": metrics["run_history"]["source"],
        "cards_count": metrics["cards_count"],
        "benchmark_scenario_count": metrics["benchmark_scenario_count"],
        "command_count": metrics["command_count"],
        "integration_entry_count": len(integrations.get("items", [])),
        "dashboard_artifacts": OUTPUT_FILES,
    }


def _russian_docs_payload(root: Path) -> dict[str, Any]:
    index = root / "docs_ru" / "README.md"
    return {
        "present": index.exists(),
        "index": "docs_ru/README.md" if index.exists() else None,
    }


def _dashboard_readme(metrics: dict[str, Any], root: Path) -> str:
    russian = _russian_docs_payload(root)
    lines = [
        "# VCP Dashboard Artifact",
        "",
        "This folder is a local, static dashboard artifact generated from repository data already present on disk.",
        "",
        f"- Repository package: `{metrics['repository_package_version']}`",
        f"- Methodology version: `{metrics['methodology_version']}`",
        "- Local-only: yes",
        "- Hosted dashboard: no",
        "- Telemetry: no",
        "- Cloud sync: no",
        "- Launch guarantee: no",
        "",
        "## Included files",
        "- `index.html`: local dashboard homepage",
        "- `dashboard.md`: markdown view of the same control surfaces",
        "- `metrics.json`: local readiness and coverage summary",
        "- `audit-backlog-summary.json`: backlog snapshot",
        "- `release-readiness.json`: release readiness payload",
        "- `launch-readiness.json`: launch-decision alias payload",
        "- `integration-status.json`: shipped/template/roadmap integration registry view",
        "- `project-map.json`: local platform/project map summary",
        "- `run-history.json`: run/checkpoint summary",
    ]
    if russian["present"]:
        lines.extend(["", "## Russian docs", f"- `{russian['index']}`"])
    return "\n".join(lines) + "\n"


def _dashboard_markdown(metrics: dict[str, Any], integrations: dict[str, Any], root: Path) -> str:
    links = [
        "- docs/track-model.md",
        "- docs/10-minute-adoption-path.md",
        "- docs/mvp-adoption-track.md",
        "- docs/mvp-to-launch-path.md",
        "- docs/launch-decision-checklist.md",
        "- docs/spec-driven-adoption.md",
        "- docs/pr-gate.md",
        "- docs/pr-gate-approval-model.md",
        "- docs/proof-layer.md",
        "- docs/proof-pack.md",
        "- docs/integrations/status-model.md",
        "- docs/project-map.md",
        "- docs/dashboard.md",
    ]
    project_memory = metrics["project_memory"]
    run_history = metrics["run_history"]
    selected_route = metrics["selected_route"] or "not-detected"
    proof_layer_status = "present" if (root / "docs" / "proof-layer.md").exists() else "missing"
    russian = _russian_docs_payload(root)
    return "\n".join(
        [
            "# VCP Local Dashboard Artifact",
            "",
            "Local dashboard artifact only.",
            "",
            f"Repository package: `{metrics['repository_package_version']}`",
            f"Methodology version: `{metrics['methodology_version']}`",
            "",
            "## Local platform flow",
            "- `intake -> classify -> plan -> memory/backlog -> PR gate -> dashboard -> launch decision`",
            "- Flow doc: `docs/local-platform-flow.md`",
            "",
            "## Track model",
            "- Core tracks: `New Project Track`, `Existing Project Track`",
            "- Guided path: `MVP-to-Launch` under `Existing Project Track`",
            "- Workflow id: `mvp-to-launch`",
            "",
            "## MVP-to-Launch",
            "- Path doc: `docs/mvp-to-launch-path.md`",
            "- Launch checklist: `docs/launch-decision-checklist.md`",
            "- Workflow file: `.vcp/workflows/mvp-to-launch.json`",
            "- Recommended command flow:",
            "  - `vcp doctor --json`",
            "  - `vcp onboard --json`",
            "  - `vcp classify --json`",
            "  - `vcp adopt plan --pack brownfield-rescue --copy-list`",
            "  - `vcp adopt plan --pack saas-ai-mvp-hardening --json`",
            "  - `vcp pr-gate explain --json`",
            "  - `vcp dashboard build --output ./vcp-dashboard --json`",
            "- Suggested packs: `brownfield-rescue`, `saas-ai-mvp-hardening`",
            "- Related scenario: `docs/demos/contracts-first-ai-mvp.md`",
            "",
            "## Adoption path links",
            *links,
            "",
            "## Current route and readiness summary",
            f"- Selected route: `{selected_route}`",
            f"- Suggested adoption pack: `{metrics['suggested_pack'] or 'not-detected'}`",
            f"- Release readiness: `{metrics['release_readiness']['status']}`",
            f"- Cards: `{metrics['cards_count']}`",
            f"- Benchmarks: `{metrics['benchmark_scenario_count']}`",
            f"- Commands: `{metrics['command_count']}`",
            "- PR Gate doc: `docs/pr-gate.md`",
            "- PR Gate approval model: `docs/pr-gate-approval-model.md`",
            "- Launch decision checklist: `docs/launch-decision-checklist.md`",
            "",
            "## Audit backlog summary",
            f"- Total backlog items: `{metrics['audit_backlog']['total']}`",
            f"- Status counts: `{metrics['audit_backlog']['status_counts']}`",
            "",
            "## Project memory summary",
            f"- Present: `{project_memory['present']}`",
            f"- Source: `{project_memory['source']}`",
            f"- Decisions: `{project_memory['decision_count']}`",
            f"- Risks: `{project_memory['risk_count']}`",
            f"- Blockers: `{project_memory['blocker_count']}`",
            "",
            "## Run history summary",
            f"- Present: `{run_history['present']}`",
            f"- Run files: `{run_history['count']}`",
            f"- Latest: `{run_history['latest']}`",
            f"- Source: `{run_history['source']}`",
            "",
            "## Integration status counts",
            f"- `{metrics['integration_status_counts']}`",
            "- Integration packs doc: `docs/integration-packs.md`",
            "",
            "## Proof layer links",
            "- `docs/proof-layer.md`",
            "- `docs/proof-pack.md`",
            f"- Status: `{proof_layer_status}`",
            "",
            "## Russian docs",
            f"- Present: `{russian['present']}`",
            f"- Index: `{russian['index']}`",
            "",
            "## Known limitations",
            "- local artifact only;",
            "- not a hosted dashboard;",
            "- not a hosted launch platform;",
            "- no telemetry;",
            "- no cloud sync;",
            "- no launch or readiness guarantee;",
            f"- integration entries listed: `{len(integrations.get('items', []))}`.",
            "",
        ]
    ) + "\n"


def _dashboard_html(metrics: dict[str, Any], integrations: dict[str, Any], root: Path) -> str:
    project_memory = metrics["project_memory"]
    run_history = metrics["run_history"]
    selected_route = metrics["selected_route"] or "not-detected"
    proof_layer_status = "present" if (root / "docs" / "proof-layer.md").exists() else "missing"
    russian = _russian_docs_payload(root)
    integration_rows = "\n".join(
        f"<tr><td>{html.escape(item.get('name', ''))}</td><td>{html.escape(item.get('status', ''))}</td><td>{html.escape(item.get('surface', ''))}</td><td>{html.escape(', '.join(item.get('claims', [])))}</td></tr>"
        for item in integrations.get("items", [])
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>VCP Local Dashboard</title>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <style>
    :root {{ color-scheme: light; --bg: #f6f3ea; --card: #fffdf8; --ink: #1f2937; --accent: #a44b22; --line: #d8cdbf; }}
    body {{ margin: 0; font-family: Georgia, 'Iowan Old Style', serif; background: linear-gradient(180deg, #f8f3e7, #efe7d4); color: var(--ink); }}
    main {{ max-width: 1100px; margin: 0 auto; padding: 32px 20px 48px; }}
    h1, h2 {{ margin: 0 0 12px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 16px; margin: 20px 0; }}
    .card {{ background: var(--card); border: 1px solid var(--line); border-radius: 18px; padding: 18px; box-shadow: 0 12px 30px rgba(56, 38, 18, 0.06); }}
    .pill {{ display: inline-block; padding: 4px 10px; border-radius: 999px; background: #fce9dc; color: var(--accent); font-weight: 700; }}
    table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 18px; overflow: hidden; }}
    th, td {{ border-bottom: 1px solid var(--line); text-align: left; padding: 12px; vertical-align: top; }}
    ul {{ margin-top: 8px; }}
    code {{ background: #f4ebdf; padding: 2px 6px; border-radius: 6px; }}
  </style>
</head>
<body>
  <main>
    <p class=\"pill\">Local dashboard artifact only</p>
    <h1>VCP Dashboard</h1>
    <p>Build with AI. Choose the right track. Adopt safely. Ship with control.</p>
    <div class=\"grid\">
      <section class=\"card\"><h2>Version</h2><p>Repository package: <code>{html.escape(metrics['repository_package_version'])}</code><br>Methodology: <code>{html.escape(metrics['methodology_version'])}</code></p></section>
      <section class=\"card\"><h2>Readiness</h2><p>Status: <code>{html.escape(metrics['release_readiness']['status'])}</code><br>Route: <code>{html.escape(selected_route)}</code><br>Cards: <code>{metrics['cards_count']}</code><br>Benchmarks: <code>{metrics['benchmark_scenario_count']}</code></p></section>
      <section class=\"card\"><h2>Backlog</h2><p>Total items: <code>{metrics['audit_backlog']['total']}</code><br>Status counts: <code>{html.escape(str(metrics['audit_backlog']['status_counts']))}</code></p></section>
      <section class=\"card\"><h2>Limits</h2><ul>{''.join(f'<li>{html.escape(item)}</li>' for item in metrics['limits'])}</ul></section>
    </div>
    <section class=\"card\">
      <h2>Local platform flow</h2>
      <p><code>intake -&gt; classify -&gt; plan -&gt; memory/backlog -&gt; PR gate -&gt; dashboard -&gt; launch decision</code><br>
      Doc: <code>docs/local-platform-flow.md</code></p>
    </section>
    <section class=\"card\">
      <h2>Track model</h2>
      <p>Core tracks: <code>New Project Track</code>, <code>Existing Project Track</code><br>
      Guided path: <code>MVP-to-Launch</code> under Existing Project Track<br>
      Workflow id: <code>mvp-to-launch</code></p>
    </section>
    <section class=\"card\">
      <h2>MVP-to-Launch</h2>
      <ul>
        <li>docs/mvp-to-launch-path.md</li>
        <li>docs/launch-decision-checklist.md</li>
        <li>.vcp/workflows/mvp-to-launch.json</li>
        <li>brownfield-rescue</li>
        <li>saas-ai-mvp-hardening</li>
      </ul>
    </section>
    <section class=\"card\">
      <h2>Adoption links</h2>
      <ul>
        <li>docs/track-model.md</li>
        <li>docs/10-minute-adoption-path.md</li>
        <li>docs/mvp-adoption-track.md</li>
        <li>docs/mvp-to-launch-path.md</li>
        <li>docs/launch-decision-checklist.md</li>
        <li>docs/spec-driven-adoption.md</li>
        <li>docs/pr-gate.md</li>
        <li>docs/pr-gate-approval-model.md</li>
        <li>docs/integrations/status-model.md</li>
        <li>docs/project-map.md</li>
        <li>docs/dashboard.md</li>
        <li>docs/proof-layer.md</li>
      </ul>
    </section>
    <section class=\"card\" style=\"margin-top: 18px;\">
      <h2>Project memory and runs</h2>
      <p>Project memory source: <code>{html.escape(str(project_memory['source']))}</code><br>
      Decisions: <code>{project_memory['decision_count']}</code><br>
      Risks: <code>{project_memory['risk_count']}</code><br>
      Proof layer: <code>{html.escape(proof_layer_status)}</code><br>
      Run files: <code>{run_history['count']}</code><br>
      Latest run: <code>{html.escape(str(run_history['latest']))}</code><br>
      Run source: <code>{html.escape(str(run_history['source']))}</code></p>
    </section>
    <section class=\"card\" style=\"margin-top: 18px;\">
      <h2>Russian docs</h2>
      <p>Present: <code>{html.escape(str(russian['present']))}</code><br>
      Index: <code>{html.escape(str(russian['index']))}</code></p>
    </section>
    <section style=\"margin-top: 18px;\">
      <h2>Integration status</h2>
      <table>
        <thead><tr><th>Name</th><th>Status</th><th>Surface</th><th>Claims</th></tr></thead>
        <tbody>{integration_rows}</tbody>
      </table>
    </section>
  </main>
</body>
</html>
"""


def build_payload(output: str, dry_run: bool = False, root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    output_dir = Path(output)
    if not output_dir.is_absolute():
        output_dir = (Path.cwd() / output_dir).resolve()
    metrics = metrics_cmd.payload(root)
    classification = classify_cmd.classify_payload(root)
    metrics["selected_route"] = classification.get("suggested_route")
    metrics["suggested_pack"] = classification.get("suggested_pack")
    metrics["project_memory"] = _project_memory_payload(root)
    metrics["run_history"] = _run_history_payload(root)
    integrations = _integration_payload(root)
    release = _release_payload(metrics)
    backlog = _backlog_payload(metrics)
    project_map = _project_map_payload(root, metrics, integrations)
    files = {
        "README.md": _dashboard_readme(metrics, root),
        "metrics.json": dump_json(metrics),
        "audit-backlog-summary.json": dump_json(backlog),
        "release-readiness.json": dump_json(release),
        "launch-readiness.json": dump_json(release),
        "integration-status.json": dump_json(integrations),
        "project-map.json": dump_json(project_map),
        "run-history.json": dump_json(metrics["run_history"]),
        "dashboard.md": _dashboard_markdown(metrics, integrations, root),
        "index.html": _dashboard_html(metrics, integrations, root),
    }
    written: list[str] = []
    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            target = output_dir / name
            target.write_text(content + ("" if content.endswith("\n") else "\n"), encoding="utf-8")
            written.append(str(target))
    return {
        "ok": True,
        "repository_package_version": repo_version(root),
        "methodology_version": methodology_version(root),
        "output_dir": str(output_dir),
        "dry_run": dry_run,
        "generated_files": OUTPUT_FILES,
        "written_files": written,
        "notes": [
            "Local dashboard artifact only.",
            "No hosted server, auth, telemetry, or network calls.",
            "Generated from repository data already present locally.",
        ],
    }


def run_build(output: str, dry_run: bool = False, json_mode: bool = False) -> int:
    data = build_payload(output, dry_run=dry_run)
    print_output(data, json_mode)
    return 0
