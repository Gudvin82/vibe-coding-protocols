from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from . import adopt as adopt_cmd
from . import backlog as backlog_cmd
from . import benchmark as benchmark_cmd
from . import check as check_cmd
from . import diagnose as diagnose_cmd
from . import demo as demo_cmd
from . import doctor as doctor_cmd
from . import evaluate as evaluate_cmd
from . import init_cmd
from . import index_cmd
from . import cards as cards_cmd
from . import manifest as manifest_cmd
from . import preset_cmd
from . import review as review_cmd
from . import review_diff as review_diff_cmd
from . import route as route_cmd
from . import score as score_cmd
from . import spec_cmd
from . import version as version_cmd
from . import workflow_cmd
from .utils import repo_root

LEGACY_VIBE_CHECK = {"audit", "starter", "hardening", "init-report", "update-advice"}


def configure_utf8_stdio() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def run_vibe_check(args: list[str]) -> int:
    root = repo_root()
    script = root / "scripts" / "vibe-check.sh"
    if shutil.which("bash") is None:
        print("bash was not found. Use Git Bash, WSL or another Bash-capable environment for legacy vibe-check wrappers.", file=sys.stderr)
        return 1
    normalized = [f"--{arg}" if not arg.startswith("-") else arg for arg in args]
    return subprocess.run(["bash", str(script), *normalized], cwd=Path.cwd()).returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vcp", description="Vibe Coding Protocols local CLI")
    sub = parser.add_subparsers(dest="command")

    version_p = sub.add_parser("version")
    version_p.add_argument("--json", action="store_true")

    doctor_p = sub.add_parser("doctor")
    doctor_p.add_argument("--json", action="store_true")

    check_p = sub.add_parser("check")
    check_p.add_argument("--fast", action="store_true")
    check_p.add_argument("--full", action="store_true")
    check_p.add_argument("--json", action="store_true")
    check_p.add_argument("--no-audit", action="store_true")

    init_p = sub.add_parser("init")
    init_p.add_argument("--target", default="generic", choices=["generic", "claude", "codex", "cursor", "windsurf", "copilot"])
    init_p.add_argument("--print-prompt", action="store_true")
    init_p.add_argument("--json", action="store_true")
    init_p.add_argument("--apply", action="store_true")

    route_p = sub.add_parser("route")
    route_p.add_argument("--profile", default="production")
    route_p.add_argument("--json", action="store_true")

    adopt_p = sub.add_parser("adopt")
    adopt_p.add_argument("--pack", default="production")
    adopt_p.add_argument("--dry-run", action="store_true", default=True)
    adopt_p.add_argument("--json", action="store_true")
    adopt_p.add_argument("--output")
    adopt_p.add_argument("--apply", action="store_true")
    adopt_p.add_argument("--yes", action="store_true")

    evaluate_p = sub.add_parser("evaluate")
    evaluate_p.add_argument("--json", action="store_true")
    evaluate_p.add_argument("--print-prompt", action="store_true")

    index_p = sub.add_parser("index")
    index_sub = index_p.add_subparsers(dest="index_command")
    index_show = index_sub.add_parser("show")
    index_show.add_argument("--json", action="store_true")
    index_validate = index_sub.add_parser("validate")
    index_validate.add_argument("--json", action="store_true")
    index_search = index_sub.add_parser("search")
    index_search.add_argument("query")
    index_search.add_argument("--json", action="store_true")

    cards_p = sub.add_parser("cards")
    cards_sub = cards_p.add_subparsers(dest="cards_command")
    cards_list = cards_sub.add_parser("list")
    cards_list.add_argument("--type")
    cards_list.add_argument("--recommended", action="store_true")
    cards_list.add_argument("--maturity")
    cards_list.add_argument("--platform")
    cards_list.add_argument("--domain")
    cards_list.add_argument("--json", action="store_true")
    cards_show = cards_sub.add_parser("show")
    cards_show.add_argument("id")
    cards_show.add_argument("--json", action="store_true")
    cards_validate = cards_sub.add_parser("validate")
    cards_validate.add_argument("--json", action="store_true")

    score_p = sub.add_parser("score")
    score_p.add_argument("--json", action="store_true")
    score_p.add_argument("--badge", nargs="?", const="text", choices=["text", "markdown", "json"])

    review_diff_p = sub.add_parser("review-diff")
    review_diff_p.add_argument("--base")
    review_diff_p.add_argument("--head")
    review_diff_p.add_argument("--json", action="store_true")

    manifest_p = sub.add_parser("manifest")
    manifest_sub = manifest_p.add_subparsers(dest="manifest_command")
    manifest_sub.add_parser("show")
    validate_p = manifest_sub.add_parser("validate")
    validate_p.add_argument("--json", action="store_true")
    manifest_sub.add_parser("routes")
    manifest_sub.add_parser("packs")
    manifest_sub.add_parser("commands")
    manifest_sub.add_parser("reports")
    manifest_sub.add_parser("benchmarks")

    benchmark_p = sub.add_parser("benchmark")
    benchmark_sub = benchmark_p.add_subparsers(dest="benchmark_command")
    benchmark_sub.add_parser("list")
    run_p = benchmark_sub.add_parser("run")
    run_p.add_argument("--scenario")
    run_p.add_argument("--json", action="store_true")

    review_p = sub.add_parser("review")
    review_sub = review_p.add_subparsers(dest="review_command")
    plan_p = review_sub.add_parser("plan")
    plan_p.add_argument("--json", action="store_true")
    review_sub.add_parser("prompt")
    review_sub.add_parser("report-template")
    status_p = review_sub.add_parser("status")
    status_p.add_argument("--json", action="store_true")

    demo_p = sub.add_parser("demo")
    demo_p.add_argument("name", nargs="?")

    spec_p = sub.add_parser("spec")
    spec_sub = spec_p.add_subparsers(dest="spec_command")
    spec_template = spec_sub.add_parser("template")
    spec_template.add_argument("kind", choices=["prd", "feature", "tasks"])
    spec_template.add_argument("--write", action="store_true")
    spec_template.add_argument("--output")
    spec_template.add_argument("--json", action="store_true")
    spec_validate = spec_sub.add_parser("validate")
    spec_validate.add_argument("--json", action="store_true")
    spec_review = spec_sub.add_parser("review")
    spec_review.add_argument("--json", action="store_true")
    spec_summary = spec_sub.add_parser("summary")
    spec_summary.add_argument("--json", action="store_true")
    spec_depth = spec_sub.add_parser("depth")
    spec_depth.add_argument("--task")
    spec_depth.add_argument("--from")
    spec_depth.add_argument("--json", action="store_true")
    spec_skip = spec_sub.add_parser("skip-check")
    spec_skip.add_argument("--task")
    spec_skip.add_argument("--reason")
    spec_skip.add_argument("--json", action="store_true")
    spec_questions = spec_sub.add_parser("questions")
    spec_questions.add_argument("--idea")
    spec_questions.add_argument("--from")
    spec_questions.add_argument("--json", action="store_true")
    spec_retrofit = spec_sub.add_parser("retrofit")
    spec_retrofit.add_argument("--scope", required=True)
    spec_retrofit.add_argument("--dry-run", action="store_true")
    spec_retrofit.add_argument("--json", action="store_true")
    spec_freshness = spec_sub.add_parser("freshness")
    spec_freshness.add_argument("--json", action="store_true")

    preset_p = sub.add_parser("preset")
    preset_sub = preset_p.add_subparsers(dest="preset_command")
    preset_list = preset_sub.add_parser("list")
    preset_list.add_argument("--json", action="store_true")
    preset_show = preset_sub.add_parser("show")
    preset_show.add_argument("id")
    preset_show.add_argument("--json", action="store_true")
    preset_validate = preset_sub.add_parser("validate")
    preset_validate.add_argument("--json", action="store_true")

    workflow_p = sub.add_parser("workflow")
    workflow_sub = workflow_p.add_subparsers(dest="workflow_command")
    workflow_list = workflow_sub.add_parser("list")
    workflow_list.add_argument("--json", action="store_true")
    workflow_show = workflow_sub.add_parser("show")
    workflow_show.add_argument("id")
    workflow_show.add_argument("--json", action="store_true")
    workflow_validate = workflow_sub.add_parser("validate")
    workflow_validate.add_argument("--json", action="store_true")
    workflow_search = workflow_sub.add_parser("search")
    workflow_search.add_argument("query")
    workflow_search.add_argument("--json", action="store_true")

    diagnose_p = sub.add_parser("diagnose")
    diagnose_p.add_argument("--profile")
    diagnose_p.add_argument("--json", action="store_true")

    backlog_p = sub.add_parser("backlog")
    backlog_sub = backlog_p.add_subparsers(dest="backlog_command")
    backlog_list = backlog_sub.add_parser("list")
    backlog_list.add_argument("--status")
    backlog_list.add_argument("--type")
    backlog_list.add_argument("--priority")
    backlog_list.add_argument("--source")
    backlog_list.add_argument("--route")
    backlog_list.add_argument("--json", action="store_true")
    backlog_add = backlog_sub.add_parser("add")
    backlog_add.add_argument("--title", required=True)
    backlog_add.add_argument("--type", required=True)
    backlog_add.add_argument("--priority", required=True)
    backlog_add.add_argument("--source", default="user")
    backlog_add.add_argument("--route", default="Unknown")
    backlog_add.add_argument("--owner", default="-")
    backlog_add.add_argument("--architecture-impact", default="none")
    backlog_add.add_argument("--notes", default="-")
    backlog_add.add_argument("--linked-docs", default="-")
    backlog_add.add_argument("--validation-required", default="-")
    backlog_add.add_argument("--review-required", default="-")
    backlog_add.add_argument("--id-prefix")
    backlog_add.add_argument("--dry-run", action="store_true")
    backlog_add.add_argument("--json", action="store_true")
    backlog_move = backlog_sub.add_parser("move")
    backlog_move.add_argument("--id", required=True)
    backlog_move.add_argument("--status", required=True)
    backlog_move.add_argument("--reason")
    backlog_move.add_argument("--validation")
    backlog_move.add_argument("--review")
    backlog_move.add_argument("--dry-run", action="store_true")
    backlog_move.add_argument("--json", action="store_true")
    backlog_done = backlog_sub.add_parser("done")
    backlog_done.add_argument("--id", required=True)
    backlog_done.add_argument("--validation")
    backlog_done.add_argument("--review")
    backlog_done.add_argument("--dry-run", action="store_true")
    backlog_done.add_argument("--json", action="store_true")
    backlog_archive = backlog_sub.add_parser("archive")
    backlog_archive.add_argument("--id", required=True)
    backlog_archive.add_argument("--reason", required=True)
    backlog_archive.add_argument("--dry-run", action="store_true")
    backlog_archive.add_argument("--json", action="store_true")
    backlog_report = backlog_sub.add_parser("report")
    backlog_report.add_argument("--json", action="store_true")
    backlog_validate = backlog_sub.add_parser("validate")
    backlog_validate.add_argument("--json", action="store_true")
    backlog_sub.add_parser("template")

    for legacy in sorted(LEGACY_VIBE_CHECK):
        sub.add_parser(legacy)

    return parser


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()
    if not argv:
        parser.print_help()
        return 0
    args = parser.parse_args(argv)

    if args.command in LEGACY_VIBE_CHECK:
        return run_vibe_check([args.command])
    if args.command == "version":
        return version_cmd.run(args.json)
    if args.command == "doctor":
        return doctor_cmd.run(args.json)
    if args.command == "check":
        return check_cmd.run(args.fast, args.full, args.no_audit, args.json)
    if args.command == "init":
        return init_cmd.run(args.target, args.print_prompt, args.json, args.apply)
    if args.command == "route":
        return route_cmd.run(args.profile, args.json)
    if args.command == "adopt":
        return adopt_cmd.run(args.pack, args.dry_run, args.json, args.output, args.apply, args.yes)
    if args.command == "evaluate":
        return evaluate_cmd.run(args.json, args.print_prompt)
    if args.command == "index":
        if args.index_command in {None, "show"}:
            return index_cmd.show(getattr(args, "json", False))
        if args.index_command == "validate":
            return index_cmd.validate(getattr(args, "json", False))
        if args.index_command == "search":
            return index_cmd.search(args.query, getattr(args, "json", False))
    if args.command == "cards":
        if args.cards_command in {None, "list"}:
            return cards_cmd.list_cards(
                type_filter=getattr(args, "type", None),
                json_mode=getattr(args, "json", False),
                recommended=getattr(args, "recommended", False),
                maturity=getattr(args, "maturity", None),
                platform=getattr(args, "platform", None),
                domain=getattr(args, "domain", None),
            )
        if args.cards_command == "show":
            return cards_cmd.show_card(args.id, getattr(args, "json", False))
        if args.cards_command == "validate":
            return cards_cmd.validate_cards(getattr(args, "json", False))
    if args.command == "score":
        return score_cmd.run(args.json, getattr(args, "badge", None))
    if args.command == "review-diff":
        return review_diff_cmd.run(args.base, args.head, getattr(args, "json", False))
    if args.command == "manifest":
        if args.manifest_command in {None, "show"}:
            print(manifest_cmd.dump_json(manifest_cmd.show_manifest()))
            return 0
        if args.manifest_command == "validate":
            return manifest_cmd.validate_manifests(args.json)
        if args.manifest_command in {"routes", "packs", "commands", "reports", "benchmarks"}:
            return manifest_cmd.list_group(args.manifest_command)
    if args.command == "benchmark":
        if args.benchmark_command in {None, "list"}:
            return benchmark_cmd.list_scenarios()
        if args.benchmark_command == "run":
            return benchmark_cmd.run(args.scenario, args.json)
    if args.command == "spec":
        if args.spec_command == "template":
            return spec_cmd.template(args.kind, args.write, args.output, getattr(args, "json", False))
        if args.spec_command == "validate":
            return spec_cmd.validate(getattr(args, "json", False))
        if args.spec_command == "review":
            return spec_cmd.review(getattr(args, "json", False))
        if args.spec_command == "summary":
            return spec_cmd.summary(getattr(args, "json", False))
        if args.spec_command == "depth":
            return spec_cmd.depth(getattr(args, "task", None), getattr(args, "from", None), getattr(args, "json", False))
        if args.spec_command == "skip-check":
            return spec_cmd.skip_check(getattr(args, "task", None), getattr(args, "reason", None), getattr(args, "json", False))
        if args.spec_command == "questions":
            return spec_cmd.questions(getattr(args, "idea", None), getattr(args, "from", None), getattr(args, "json", False))
        if args.spec_command == "retrofit":
            return spec_cmd.retrofit(args.scope, getattr(args, "dry_run", False), getattr(args, "json", False))
        if args.spec_command == "freshness":
            return spec_cmd.freshness(getattr(args, "json", False))
    if args.command == "preset":
        if args.preset_command in {None, "list"}:
            return preset_cmd.list_presets(getattr(args, "json", False))
        if args.preset_command == "show":
            return preset_cmd.show_preset(args.id, getattr(args, "json", False))
        if args.preset_command == "validate":
            return preset_cmd.validate_presets(getattr(args, "json", False))
    if args.command == "workflow":
        if args.workflow_command in {None, "list"}:
            return workflow_cmd.list_workflows(getattr(args, "json", False))
        if args.workflow_command == "show":
            return workflow_cmd.show_workflow(args.id, getattr(args, "json", False))
        if args.workflow_command == "validate":
            return workflow_cmd.validate_workflows(getattr(args, "json", False))
        if args.workflow_command == "search":
            return workflow_cmd.search_workflows(args.query, getattr(args, "json", False))
    if args.command == "diagnose":
        return diagnose_cmd.run(args.profile, getattr(args, "json", False))
    if args.command == "backlog":
        if args.backlog_command == "list":
            return backlog_cmd.list_items(
                status=args.status,
                type_=getattr(args, "type"),
                priority=args.priority,
                source=args.source,
                route=args.route,
                json_mode=args.json,
            )
        if args.backlog_command == "add":
            return backlog_cmd.add_item(
                title=args.title,
                type_=getattr(args, "type"),
                priority=args.priority,
                source=args.source,
                route=args.route,
                owner=args.owner,
                architecture_impact=args.architecture_impact,
                notes=args.notes,
                linked_docs=args.linked_docs,
                validation_required=args.validation_required,
                review_required=args.review_required,
                id_prefix=args.id_prefix,
                dry_run=args.dry_run,
                json_mode=args.json,
            )
        if args.backlog_command == "move":
            return backlog_cmd.move_item(
                item_id=args.id,
                status=args.status,
                reason=args.reason,
                validation=args.validation,
                review=args.review,
                dry_run=args.dry_run,
                json_mode=args.json,
            )
        if args.backlog_command == "done":
            return backlog_cmd.done_item(
                item_id=args.id,
                validation=args.validation,
                review=args.review,
                dry_run=args.dry_run,
                json_mode=args.json,
            )
        if args.backlog_command == "archive":
            return backlog_cmd.archive_item(
                item_id=args.id,
                reason=args.reason,
                dry_run=args.dry_run,
                json_mode=args.json,
            )
        if args.backlog_command == "report":
            return backlog_cmd.report(args.json)
        if args.backlog_command in {None, "validate"}:
            return backlog_cmd.validate(getattr(args, "json", False))
        if args.backlog_command == "template":
            return backlog_cmd.template()
    if args.command == "review":
        if args.review_command in {None, "plan"}:
            return review_cmd.plan(getattr(args, "json", False))
        if args.review_command == "prompt":
            return review_cmd.prompt()
        if args.review_command == "report-template":
            return review_cmd.report_template()
        if args.review_command == "status":
            return review_cmd.status(args.json)
    if args.command == "demo":
        return demo_cmd.run(args.name)

    parser.print_help()
    return 0
