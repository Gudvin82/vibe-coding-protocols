from __future__ import annotations

from pathlib import Path

from .utils import load_json, manifest_dir, manifest_paths, print_output, repo_root, repo_version

KEY_FILES = [
    "AI_EVALUATION_GUIDE.md",
    "AGENTS.md",
    "README.md",
    "AI_INTAKE.md",
    "START_HERE.md",
    "llms.txt",
    "llms-full.txt",
    "ai.txt",
    "CITATION.cff",
    "ADOPTERS.md",
    ".vcp/index.json",
    ".vcp/cards/README.md",
    ".vcp/presets/README.md",
    "docs/adaptive-spec-depth.md",
    "docs/spec-escape-hatch.md",
    "docs/question-engine.md",
    "docs/spec-retrofit.md",
    "docs/spec-freshness.md",
    "docs/packs-and-presets.md",
    "docs/integrations/spec-kit-bridge.md",
    "docs/protocol-index.md",
    "docs/adoption-packs.md",
    "docs/cli.md",
    "docs/install.md",
    "docs/glossary.md",
    "docs/progressive-disclosure.md",
    "docs/vcp-cards.md",
    "docs/vcp-mappings.md",
    "docs/platforms/README.md",
    "docs/geo-ai-visibility.md",
    "docs/page-templates.md",
    "docs/faq.md",
    "docs/comparison.md",
    "docs/anti-patterns.md",
    "docs/quickstart-walkthrough.md",
    "docs/demo-script.md",
    "docs/workflows.md",
    "docs/diagnostics.md",
    "docs/catalog.md",
    "docs/event-schema.md",
    "docs/project-backlog.md",
    "docs/production-observability.md",
    "docs/known-limitations.md",
    "PROJECT_BACKLOG.md",
]

CLI_COMMANDS = [
    "version",
    "doctor",
    "check",
    "init",
    "route",
    "adopt",
    "score",
    "manifest",
    "benchmark",
    "review",
    "backlog",
    "index",
    "cards",
    "evaluate",
    "spec",
    "workflow",
    "diagnose",
    "preset",
]

PROMPT_PATH = "templates/prompts/evaluate-vcp-repository.md"
KNOWN_LIMITATIONS_PATH = "docs/known-limitations.md"


def _count_markdown_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for child in path.rglob("*.md") if child.is_file())


def _benchmark_count(root: Path) -> int:
    benchmarks_manifest = load_json(manifest_paths(root)["benchmarks"])
    return len(benchmarks_manifest.get("items", []))


def evaluate_payload() -> dict[str, object]:
    root = repo_root()
    manifests = manifest_paths(root)
    protocols_manifest = load_json(manifests["protocols"])
    commands_manifest = load_json(manifests["commands"])
    reports_manifest = load_json(manifests["reports"])

    key_files = [{"path": rel, "present": (root / rel).exists()} for rel in KEY_FILES]
    protocols_dir = root / "protocols"
    commands_dir = root / "commands"
    operations_ready = all(
        (root / rel).exists()
        for rel in [
            "protocols/operations/production-error-capture.md",
            "protocols/operations/daily-error-triage.md",
            "docs/production-observability.md",
            "PROJECT_BACKLOG.md",
        ]
    )
    public_growth_ready = all(
        (root / rel).exists()
        for rel in [
            "protocols/public-growth/public-growth-playbook.md",
            "protocols/public-growth/seo-geo-ai-visibility.md",
            "docs/geo-ai-visibility.md",
            "docs/page-templates.md",
            "templates/public-growth/public-growth-checklist.md",
        ]
    )
    spec_lane_ready = all(
        (root / rel).exists()
        for rel in [
            "protocols/spec-driven/README.md",
            "templates/specs/PRD.md",
            "vcp_cli/spec_cmd.py",
        ]
    )
    adaptive_spec_ready = all(
        (root / rel).exists()
        for rel in [
            "docs/adaptive-spec-depth.md",
            "docs/spec-escape-hatch.md",
            "docs/question-engine.md",
            "docs/spec-retrofit.md",
            "docs/spec-freshness.md",
            "protocols/spec-driven/adaptive-spec-depth.md",
            "protocols/spec-driven/spec-escape-hatch.md",
            "protocols/spec-driven/question-engine.md",
            "protocols/spec-driven/spec-retrofit.md",
            "protocols/spec-driven/spec-freshness.md",
        ]
    )
    presets_ready = all(
        (root / rel).exists()
        for rel in [
            ".vcp/presets/README.md",
            "docs/packs-and-presets.md",
            "schemas/vcp-preset.schema.json",
            "vcp_cli/preset_cmd.py",
        ]
    )
    workflow_layer_ready = all(
        (root / rel).exists()
        for rel in [
            ".vcp/workflows/README.md",
            "docs/workflows.md",
            "vcp_cli/workflow_cmd.py",
        ]
    )
    diagnostics_ready = all(
        (root / rel).exists()
        for rel in [
            ".vcp/diagnostics/layers.json",
            "docs/diagnostics.md",
            "vcp_cli/diagnose.py",
        ]
    )
    catalog_ready = all(
        (root / rel).exists()
        for rel in [
            ".vcp/catalog.json",
            "docs/catalog.md",
            "vcp_cli/cards.py",
        ]
    )
    event_schema_ready = all(
        (root / rel).exists()
        for rel in [
            "schemas/vcp-event.schema.json",
            "docs/event-schema.md",
            "templates/reports/vcp-event-entry.md",
        ]
    )

    payload = {
        "repository_package": repo_version(root),
        "evaluation_guide_present": (root / "AI_EVALUATION_GUIDE.md").exists(),
        "key_files": key_files,
        "manifest_directory": str(manifest_dir(root)),
        "benchmark_count": _benchmark_count(root),
        "protocol_count": len(protocols_manifest.get("items", [])),
        "protocol_markdown_files": _count_markdown_files(protocols_dir),
        "command_count": len(commands_manifest.get("items", [])),
        "command_markdown_files": _count_markdown_files(commands_dir),
        "report_template_count": len(reports_manifest.get("items", [])),
        "cli_commands": CLI_COMMANDS,
        "project_backlog_present": (root / "PROJECT_BACKLOG.md").exists(),
        "operations_workflow_present": operations_ready,
        "public_growth_layer_present": public_growth_ready,
        "spec_lane_present": spec_lane_ready,
        "adaptive_spec_depth_present": adaptive_spec_ready,
        "presets_layer_present": presets_ready,
        "workflow_layer_present": workflow_layer_ready,
        "diagnostics_layer_present": diagnostics_ready,
        "catalog_layer_present": catalog_ready,
        "event_schema_present": event_schema_ready,
        "platform_doc_count": len(list((root / "docs" / "platforms").glob("*.md"))) if (root / "docs" / "platforms").exists() else 0,
        "platform_card_count": len(list((root / ".vcp" / "cards" / "platforms").glob("*.json"))) if (root / ".vcp" / "cards" / "platforms").exists() else 0,
        "llm_reference_present": all(
            (root / rel).exists()
            for rel in ["AGENTS.md", "llms.txt", "llms-full.txt", "ai.txt", "CITATION.cff"]
        ),
        "adopters_doc_present": (root / "ADOPTERS.md").exists(),
        "glossary_present": (root / "docs/glossary.md").exists(),
        "install_doc_present": (root / "docs/install.md").exists(),
        "progressive_disclosure_present": all(
            (root / rel).exists()
            for rel in [
                ".vcp/index.json",
                ".vcp/cards/README.md",
                "docs/progressive-disclosure.md",
                "docs/vcp-cards.md",
                "docs/vcp-mappings.md",
                "docs/platforms/README.md",
            ]
        ),
        "known_limitations": KNOWN_LIMITATIONS_PATH,
        "suggested_evaluation_prompt": PROMPT_PATH,
        "note": "This helper supports external evaluation. It is not a market-maturity score.",
    }
    return payload


def run(json_mode: bool = False, print_prompt: bool = False) -> int:
    root = repo_root()
    if print_prompt:
        print((root / PROMPT_PATH).read_text(encoding="utf-8"))
        return 0

    payload = evaluate_payload()
    if json_mode:
        print_output(payload, True)
        return 0

    print(f"Repository package: {payload['repository_package']}")
    print(f"Evaluation guide present: {'yes' if payload['evaluation_guide_present'] else 'no'}")
    print(f"Manifest directory: {payload['manifest_directory']}")
    print(f"Benchmark scenarios: {payload['benchmark_count']}")
    print(f"Protocols in manifest: {payload['protocol_count']}")
    print(f"Commands in manifest: {payload['command_count']}")
    print(f"Report templates in manifest: {payload['report_template_count']}")
    print(f"PROJECT_BACKLOG.md: {'yes' if payload['project_backlog_present'] else 'no'}")
    print(f"Operations workflow present: {'yes' if payload['operations_workflow_present'] else 'no'}")
    print(f"Public growth layer present: {'yes' if payload['public_growth_layer_present'] else 'no'}")
    print(f"Spec lane present: {'yes' if payload['spec_lane_present'] else 'no'}")
    print(f"Adaptive spec depth present: {'yes' if payload['adaptive_spec_depth_present'] else 'no'}")
    print(f"Presets layer present: {'yes' if payload['presets_layer_present'] else 'no'}")
    print(f"Workflow layer present: {'yes' if payload['workflow_layer_present'] else 'no'}")
    print(f"Diagnostics layer present: {'yes' if payload['diagnostics_layer_present'] else 'no'}")
    print(f"Catalog layer present: {'yes' if payload['catalog_layer_present'] else 'no'}")
    print(f"Event schema present: {'yes' if payload['event_schema_present'] else 'no'}")
    print(f"Platform docs: {payload['platform_doc_count']}")
    print(f"Platform cards: {payload['platform_card_count']}")
    print(f"LLM reference layer present: {'yes' if payload['llm_reference_present'] else 'no'}")
    print(f"Adopters doc present: {'yes' if payload['adopters_doc_present'] else 'no'}")
    print(f"Glossary present: {'yes' if payload['glossary_present'] else 'no'}")
    print(f"Install doc present: {'yes' if payload['install_doc_present'] else 'no'}")
    print(f"Progressive disclosure present: {'yes' if payload['progressive_disclosure_present'] else 'no'}")
    print(f"Known limitations: {payload['known_limitations']}")
    print(f"Suggested evaluation prompt: {payload['suggested_evaluation_prompt']}")
    print("Key files:")
    for item in payload["key_files"]:
        status = "PASS" if item["present"] else "FAIL"
        print(f"- {status}: {item['path']}")
    print("CLI commands:")
    for command in payload["cli_commands"]:
        print(f"- {command}")
    print(payload["note"])
    return 0
