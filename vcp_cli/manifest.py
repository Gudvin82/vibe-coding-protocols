from __future__ import annotations

from typing import Any

from .utils import dump_json, load_json, manifest_path, manifest_paths, print_output, repo_root

REQUIRED_API_INTAKE_PROTOCOL_ID = "third-party-api-intake"
REQUIRED_API_INTAKE_COMMAND_ID = "third-party-api-intake"
REQUIRED_API_INTAKE_REPORT_ID = "third-party-api-intake-report"
REQUIRED_API_INTAKE_PACK_ID = "third-party-api"
REQUIRED_API_INTAKE_BENCHMARK_ID = "third-party-api-intake"
REQUIRED_OPERATIONS_PROTOCOL_ID = "production-error-capture"
REQUIRED_BACKLOG_PROTOCOL_ID = "project-backlog-workflow"
REQUIRED_PUBLIC_GROWTH_PROTOCOL_ID = "public-growth-playbook"
REQUIRED_OPERATIONS_COMMAND_ID = "prod-log-monitor"
REQUIRED_BACKLOG_COMMAND_ID = "backlog-update"
REQUIRED_BACKLOG_LIST_COMMAND_ID = "backlog-list"
REQUIRED_BACKLOG_ADD_COMMAND_ID = "backlog-add"
REQUIRED_BACKLOG_MOVE_COMMAND_ID = "backlog-move"
REQUIRED_BACKLOG_DONE_COMMAND_ID = "backlog-done"
REQUIRED_BACKLOG_ARCHIVE_COMMAND_ID = "backlog-archive"
REQUIRED_BACKLOG_REPORT_COMMAND_ID = "backlog-report"
REQUIRED_BACKLOG_VALIDATE_COMMAND_ID = "backlog-validate"
REQUIRED_BACKLOG_TEMPLATE_COMMAND_ID = "backlog-template"
REQUIRED_ERROR_REPORT_ID = "production-error-capture-report"
REQUIRED_BACKLOG_REPORT_ID = "backlog-update-report"
REQUIRED_OPERATIONS_PACK_ID = "operations"
REQUIRED_BACKLOG_PACK_ID = "backlog"
REQUIRED_OPERATIONS_BENCHMARK_ID = "production-error-capture"
REQUIRED_BACKLOG_BENCHMARK_ID = "project-backlog-update"
REQUIRED_BACKLOG_ADD_BENCHMARK_ID = "backlog-add-idea"
REQUIRED_BACKLOG_DONE_BENCHMARK_ID = "backlog-move-done-with-review"
REQUIRED_BACKLOG_ARCHIVE_BENCHMARK_ID = "backlog-archive-not-taken"
REQUIRED_BACKLOG_ARCH_IMPACT_BENCHMARK_ID = "backlog-architecture-impact"
REQUIRED_EVALUATION_COMMAND_ID = "evaluate"
REQUIRED_EVALUATION_REPORT_ID = "vcp-repository-evaluation-report"
REQUIRED_PUBLIC_GROWTH_AUDIT_REPORT_ID = "public-growth-audit-report"
REQUIRED_AI_VISIBILITY_REPORT_ID = "ai-visibility-monitoring-report"
REQUIRED_PUBLIC_GROWTH_PACK_ID = "public-growth"
REQUIRED_EVALUATION_FULL_BENCHMARK_ID = "repository-evaluation-full"
REQUIRED_EVALUATION_SHALLOW_BENCHMARK_ID = "repository-evaluation-shallow"
REQUIRED_PUBLIC_GROWTH_BENCHMARK_ID = "public-growth-audit"
REQUIRED_GEO_AI_VISIBILITY_BENCHMARK_ID = "geo-ai-visibility"
REQUIRED_PAGE_TEMPLATE_SELECTION_BENCHMARK_ID = "page-template-selection"
REQUIRED_GLOSSARY_INSPECTION_BENCHMARK_ID = "glossary-inspection"
REQUIRED_INDEX_SHOW_COMMAND_ID = "index-show"
REQUIRED_INDEX_VALIDATE_COMMAND_ID = "index-validate"
REQUIRED_INDEX_SEARCH_COMMAND_ID = "index-search"
REQUIRED_CARDS_LIST_COMMAND_ID = "cards-list"
REQUIRED_CARDS_SHOW_COMMAND_ID = "cards-show"
REQUIRED_CARDS_VALIDATE_COMMAND_ID = "cards-validate"
REQUIRED_PROGRESSIVE_DISCLOSURE_BENCHMARK_ID = "progressive-disclosure-index"
REQUIRED_CARD_ROUTE_SELECTION_BENCHMARK_ID = "card-based-route-selection"
REQUIRED_PLATFORM_COMPATIBILITY_BENCHMARK_ID = "platform-compatibility-inspection"
REQUIRED_SPEC_PROTOCOL_ID = "spec-first-feature"
REQUIRED_SPEC_DRIVEN_PROTOCOL_ID = "spec-driven-development"
REQUIRED_SPEC_PACK_ID = "spec-first"
REQUIRED_SPEC_INTAKE_COMMAND_ID = "spec-intake"
REQUIRED_SPEC_REVIEW_COMMAND_ID = "spec-review"
REQUIRED_SPEC_TO_TASKS_COMMAND_ID = "spec-to-tasks"
REQUIRED_VCP_SPEC_COMMAND_ID = "vcp-spec"
REQUIRED_VCP_WORKFLOW_COMMAND_ID = "vcp-workflow"
REQUIRED_VCP_DIAGNOSE_COMMAND_ID = "vcp-diagnose"
REQUIRED_DIAGNOSTIC_REPORT_ID = "diagnostic-report"
REQUIRED_EVENT_REPORT_ID = "vcp-event-entry"
REQUIRED_SPEC_PRODUCT_BENCHMARK_ID = "spec-first-product-brief"
REQUIRED_PRD_GAP_BENCHMARK_ID = "prd-gap-review"
REQUIRED_FEATURE_TASK_BENCHMARK_ID = "feature-spec-to-tasks"
REQUIRED_WORKFLOW_PROD_BENCHMARK_ID = "workflow-production-hardening"
REQUIRED_WORKFLOW_PUBLIC_GROWTH_BENCHMARK_ID = "workflow-public-growth-audit"
REQUIRED_DIAGNOSTICS_BENCHMARK_ID = "diagnostics-layer-check"
REQUIRED_CATALOG_BENCHMARK_ID = "catalog-filter-selection"
REQUIRED_EVENT_SCHEMA_BENCHMARK_ID = "event-schema-review-finding"


def show_manifest(name: str | None = None) -> dict[str, Any]:
    root = repo_root()
    paths = manifest_paths(root)
    if name:
        return {name: load_json(paths[name])}
    return {key: load_json(path) for key, path in paths.items()}


def validate_manifests(json_mode: bool = False) -> int:
    root = repo_root()
    paths = manifest_paths(root)
    errors: list[str] = []
    details: dict[str, Any] = {}
    protocol_ids: set[str] = set()
    pack_ids: set[str] = set()
    command_ids: set[str] = set()
    report_ids: set[str] = set()
    benchmark_ids: set[str] = set()

    try:
        protocol_ids = {item.get("id") for item in load_json(paths["protocols"]).get("items", [])}
        pack_ids = {item.get("id") for item in load_json(paths["adoption-packs"]).get("items", [])}
        command_ids = {item.get("id") for item in load_json(paths["commands"]).get("items", [])}
        report_ids = {item.get("id") for item in load_json(paths["reports"]).get("items", [])}
        benchmark_ids = {item.get("id") for item in load_json(paths["benchmarks"]).get("items", [])}
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Manifest pre-load failed: {exc}")

    for key, path in paths.items():
        try:
            data = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Invalid JSON in {path.name}: {exc}")
            continue
        details[key] = {"path": str(path), "status": "ok"}
        for item in data.get("items", []):
            file_path = item.get("file")
            if file_path and not (root / file_path).exists():
                errors.append(f"Missing file for {key}:{item.get('id')}: {file_path}")
            for linked in item.get("related_docs", []):
                if not (root / linked).exists():
                    errors.append(f"Missing related doc for {key}:{item.get('id')}: {linked}")
            report_template = item.get("report_template")
            if isinstance(report_template, list):
                for template in report_template:
                    if not (root / template).exists():
                        errors.append(f"Missing report template for {key}:{item.get('id')}: {template}")
            elif isinstance(report_template, str) and report_template and not (root / report_template).exists():
                errors.append(f"Missing report template for {key}:{item.get('id')}: {report_template}")
            if key == "adoption-packs":
                for field in ["recommended_files", "optional_files", "merge_only_files"]:
                    for rel in item.get(field, []):
                        if rel.endswith((".md", ".json", ".sh", ".py", ".txt", ".ps1", ".cmd", ".yml", ".yaml")) and not (root / rel).exists():
                            errors.append(f"Missing pack path for {item.get('id')}:{field}: {rel}")
            if key == "benchmarks":
                scenario_file = item.get("scenario_file")
                if scenario_file and not (root / scenario_file).exists():
                    errors.append(f"Missing benchmark scenario for {item.get('id')}: {scenario_file}")
                expected_route = item.get("expected_route")
                expected_pack = item.get("expected_pack")
                if expected_route and expected_route not in protocol_ids:
                    errors.append(f"Unknown expected route in benchmarks:{item.get('id')}: {item.get('expected_route')}")
                if expected_pack and expected_pack not in pack_ids:
                    errors.append(f"Unknown expected pack in benchmarks:{item.get('id')}: {item.get('expected_pack')}")
        for top_key in ["entrypoints", "core_docs", "validation_scripts", "safety_boundaries", "route_docs", "known_limitations"]:
            for rel in data.get(top_key, []):
                if rel.endswith((".md", ".json", ".sh", ".py", ".yml", ".yaml", ".txt", ".ps1", ".cmd")) and not (root / rel).exists():
                    errors.append(f"Missing manifest path in {path.name}: {rel}")

    if REQUIRED_API_INTAKE_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: third-party-api-intake")
    if REQUIRED_OPERATIONS_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: production-error-capture")
    if REQUIRED_BACKLOG_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: project-backlog-workflow")
    if REQUIRED_PUBLIC_GROWTH_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: public-growth-playbook")
    if REQUIRED_SPEC_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: spec-first-feature")
    if REQUIRED_SPEC_DRIVEN_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: spec-driven-development")
    if REQUIRED_API_INTAKE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: third-party-api-intake")
    if REQUIRED_OPERATIONS_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: prod-log-monitor")
    if REQUIRED_BACKLOG_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-update")
    if REQUIRED_BACKLOG_LIST_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-list")
    if REQUIRED_BACKLOG_ADD_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-add")
    if REQUIRED_BACKLOG_MOVE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-move")
    if REQUIRED_BACKLOG_DONE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-done")
    if REQUIRED_BACKLOG_ARCHIVE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-archive")
    if REQUIRED_BACKLOG_REPORT_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-report")
    if REQUIRED_BACKLOG_VALIDATE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-validate")
    if REQUIRED_BACKLOG_TEMPLATE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: backlog-template")
    if REQUIRED_EVALUATION_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: evaluate")
    if REQUIRED_INDEX_SHOW_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: index-show")
    if REQUIRED_INDEX_VALIDATE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: index-validate")
    if REQUIRED_INDEX_SEARCH_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: index-search")
    if REQUIRED_CARDS_LIST_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: cards-list")
    if REQUIRED_CARDS_SHOW_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: cards-show")
    if REQUIRED_CARDS_VALIDATE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: cards-validate")
    if REQUIRED_SPEC_INTAKE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: spec-intake")
    if REQUIRED_SPEC_REVIEW_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: spec-review")
    if REQUIRED_SPEC_TO_TASKS_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: spec-to-tasks")
    if REQUIRED_VCP_SPEC_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: vcp-spec")
    if REQUIRED_VCP_WORKFLOW_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: vcp-workflow")
    if REQUIRED_VCP_DIAGNOSE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: vcp-diagnose")
    if REQUIRED_API_INTAKE_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: third-party-api-intake-report")
    if REQUIRED_ERROR_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: production-error-capture-report")
    if REQUIRED_BACKLOG_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: backlog-update-report")
    if REQUIRED_EVALUATION_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: vcp-repository-evaluation-report")
    if REQUIRED_PUBLIC_GROWTH_AUDIT_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: public-growth-audit-report")
    if REQUIRED_AI_VISIBILITY_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: ai-visibility-monitoring-report")
    if REQUIRED_DIAGNOSTIC_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: diagnostic-report")
    if REQUIRED_EVENT_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: vcp-event-entry")
    if REQUIRED_API_INTAKE_PACK_ID not in pack_ids:
        errors.append("Missing required adoption pack manifest entry: third-party-api")
    if REQUIRED_OPERATIONS_PACK_ID not in pack_ids:
        errors.append("Missing required adoption pack manifest entry: operations")
    if REQUIRED_BACKLOG_PACK_ID not in pack_ids:
        errors.append("Missing required adoption pack manifest entry: backlog")
    if REQUIRED_PUBLIC_GROWTH_PACK_ID not in pack_ids:
        errors.append("Missing required adoption pack manifest entry: public-growth")
    if REQUIRED_SPEC_PACK_ID not in pack_ids:
        errors.append("Missing required adoption pack manifest entry: spec-first")
    if REQUIRED_API_INTAKE_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: third-party-api-intake")
    if REQUIRED_OPERATIONS_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: production-error-capture")
    if REQUIRED_BACKLOG_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: project-backlog-update")
    if REQUIRED_BACKLOG_ADD_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: backlog-add-idea")
    if REQUIRED_BACKLOG_DONE_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: backlog-move-done-with-review")
    if REQUIRED_BACKLOG_ARCHIVE_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: backlog-archive-not-taken")
    if REQUIRED_BACKLOG_ARCH_IMPACT_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: backlog-architecture-impact")
    if REQUIRED_EVALUATION_FULL_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: repository-evaluation-full")
    if REQUIRED_EVALUATION_SHALLOW_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: repository-evaluation-shallow")
    if REQUIRED_PUBLIC_GROWTH_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: public-growth-audit")
    if REQUIRED_GEO_AI_VISIBILITY_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: geo-ai-visibility")
    if REQUIRED_PAGE_TEMPLATE_SELECTION_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: page-template-selection")
    if REQUIRED_GLOSSARY_INSPECTION_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: glossary-inspection")
    if REQUIRED_PROGRESSIVE_DISCLOSURE_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: progressive-disclosure-index")
    if REQUIRED_CARD_ROUTE_SELECTION_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: card-based-route-selection")
    if REQUIRED_PLATFORM_COMPATIBILITY_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: platform-compatibility-inspection")
    if REQUIRED_SPEC_PRODUCT_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: spec-first-product-brief")
    if REQUIRED_PRD_GAP_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: prd-gap-review")
    if REQUIRED_FEATURE_TASK_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: feature-spec-to-tasks")
    if REQUIRED_WORKFLOW_PROD_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: workflow-production-hardening")
    if REQUIRED_WORKFLOW_PUBLIC_GROWTH_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: workflow-public-growth-audit")
    if REQUIRED_DIAGNOSTICS_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: diagnostics-layer-check")
    if REQUIRED_CATALOG_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: catalog-filter-selection")
    if REQUIRED_EVENT_SCHEMA_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: event-schema-review-finding")

    payload = {
        "ok": not errors,
        "errors": errors,
        "manifests": details,
    }
    if json_mode:
        print_output(payload, True)
    else:
        if errors:
            for error in errors:
                print(error)
        else:
            print("Manifest validation passed.")
    return 0 if not errors else 1


def list_group(group: str) -> int:
    root = repo_root()
    lookup = {
        "routes": manifest_path(root, "protocols"),
        "packs": manifest_path(root, "adoption-packs"),
        "commands": manifest_path(root, "commands"),
        "reports": manifest_path(root, "reports"),
        "benchmarks": manifest_path(root, "benchmarks"),
    }
    data = load_json(lookup[group])
    print(dump_json(data.get("items", [])))
    return 0
