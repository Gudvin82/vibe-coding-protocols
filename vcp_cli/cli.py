from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from . import __version__
from . import adopt as adopt_cmd
from . import benchmark as benchmark_cmd
from . import check as check_cmd
from . import demo as demo_cmd
from . import doctor as doctor_cmd
from . import manifest as manifest_cmd
from . import review as review_cmd
from . import route as route_cmd
from . import score as score_cmd
from . import version as version_cmd
from .utils import repo_root

LEGACY_VIBE_CHECK = {"audit", "starter", "hardening", "init-report", "update-advice"}


def run_vibe_check(args: list[str]) -> int:
    root = repo_root()
    script = root / "scripts" / "vibe-check.sh"
    if shutil.which("bash") is None:
        print("bash was not found. Use Git Bash, WSL or another Bash-capable environment.", file=sys.stderr)
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

    score_p = sub.add_parser("score")
    score_p.add_argument("--json", action="store_true")

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

    for legacy in sorted(LEGACY_VIBE_CHECK):
        sub.add_parser(legacy)

    return parser


def main(argv: list[str] | None = None) -> int:
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
    if args.command == "route":
        return route_cmd.run(args.profile, args.json)
    if args.command == "adopt":
        return adopt_cmd.run(args.pack, args.dry_run, args.json, args.output, args.apply, args.yes)
    if args.command == "score":
        return score_cmd.run(args.json)
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
    if args.command == "review":
        if args.review_command in {None, "plan"}:
            return review_cmd.plan(getattr(args, 'json', False))
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
