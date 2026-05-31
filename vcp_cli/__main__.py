from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from . import __version__

REPO_VERSION = f"v{__version__}"

ROUTE_PROFILES = {
    "production": {
        "route": "Hardening Full",
        "next_gate": "Run /loop-code-review before merge, release or deploy.",
    },
    "shared-engine": {
        "route": "Shared Engine or Multi-product Pack + Hardening Full",
        "next_gate": "Run /loop-code-review before accepting cross-product changes.",
    },
    "regulated": {
        "route": "Hardening Full + Security Review Scope",
        "next_gate": "Run /loop-code-review plus independent human/security review before release.",
    },
    "maintenance": {
        "route": "Maintenance Refactoring",
        "next_gate": "Run /loop-code-review after the refactoring slice before the next feature.",
    },
    "ui": {
        "route": "UI Component Ownership",
        "next_gate": "Run /loop-code-review after component extraction or ownership cleanup.",
    },
    "mvp": {
        "route": "Starter or Existing MVP Pack",
        "next_gate": "Use lighter post-task review before merge when changes are meaningful.",
    },
}

ADOPTION_PACKS = {
    "production": {
        "files": [
            "AI_INTAKE.md",
            "docs/adoption-packs.md",
            "protocols/ai-project-hardening-protocol.md",
            "protocols/review/post-task-code-review.md",
            "commands/loop-code-review.md",
            "templates/reports/code-review-report.md",
        ],
        "gate": "Require post-task review before merge/release.",
    },
    "shared-engine": {
        "files": [
            "PROJECT_MAP.md",
            "templates/ARCHITECTURE_SOURCE_OF_TRUTH.md",
            "protocols/review/post-task-code-review.md",
            "templates/reports/code-review-report.md",
        ],
        "gate": "Require post-task review for cross-product regression risk.",
    },
    "regulated": {
        "files": [
            "templates/reports/security-review-scope.md",
            "protocols/review/post-task-code-review.md",
            "templates/reports/code-review-report.md",
        ],
        "gate": "Require independent review plus validation before release.",
    },
}


def locate_repo_root() -> Path | None:
    cwd = Path.cwd().resolve()
    search_roots = [cwd, Path(__file__).resolve().parents[1], *cwd.parents]
    for base in search_roots:
        if (base / "scripts" / "vibe-check.sh").exists() and (base / "VERSION").exists():
            return base
    return None


def locate_script(repo_root: Path) -> Path:
    return repo_root / "scripts" / "vibe-check.sh"


def print_help() -> None:
    print(
        "VCP Python wrapper (experimental)\n"
        "\n"
        "Stable path: use documented scripts directly.\n"
        "This wrapper adds a small convenience surface and delegates to vibe-check where appropriate.\n"
        "\n"
        "Usage:\n"
        "  python -m vcp_cli doctor\n"
        "  python -m vcp_cli audit\n"
        "  python -m vcp_cli route production\n"
        "  python -m vcp_cli adopt --pack production --dry-run\n"
        "  python -m vcp_cli score --json\n"
        "  python -m vcp_cli manifest validate\n"
        "  python -m vcp_cli version\n"
    )


def run_vibe_check(repo_root: Path, args: list[str]) -> int:
    if shutil.which("bash") is None:
        print("bash was not found. Use Git Bash, WSL or another Bash-capable environment.", file=sys.stderr)
        return 1
    script = locate_script(repo_root)
    normalized = [f"--{arg}" if not arg.startswith("-") else arg for arg in args]
    result = subprocess.run(["bash", str(script), *normalized], cwd=Path.cwd())
    return result.returncode


def manifest_validate(repo_root: Path) -> int:
    required = [
        "protocols/review/README.md",
        "protocols/review/post-task-code-review.md",
        "commands/loop-code-review.md",
        "templates/prompts/loop-code-review.md",
        "templates/reports/code-review-report.md",
        "examples/review/README.md",
    ]
    missing = [path for path in required if not (repo_root / path).is_file()]
    if missing:
        for path in missing:
            print(f"Missing review manifest surface: {path}", file=sys.stderr)
        return 1
    print("Review manifest references look valid.")
    return 0


def score(json_mode: bool) -> int:
    payload = {
        "wrapper": "experimental",
        "categories": [
            {"name": "Route selection", "status": "documented"},
            {"name": "Adoption packs", "status": "documented"},
            {"name": "Post-task review gate", "status": "documented"},
            {"name": "Validation scripts", "status": "script-first"},
        ],
        "notes": [
            "Score output is informational and not a replacement for route-specific validation.",
            "Post-task review still depends on independent reviewer quality and validation coverage.",
        ],
    }
    if json_mode:
        print(json.dumps(payload, indent=2))
    else:
        print("VCP score surfaces:")
        for category in payload["categories"]:
            print(f"- {category['name']}: {category['status']}")
    return 0


def route(profile: str) -> int:
    info = ROUTE_PROFILES.get(profile)
    if info is None:
        print(f"Unknown route profile: {profile}", file=sys.stderr)
        return 1
    print(f"Profile: {profile}")
    print(f"Recommended route: {info['route']}")
    print(f"Next gate: {info['next_gate']}")
    return 0


def adopt(pack: str, dry_run: bool) -> int:
    info = ADOPTION_PACKS.get(pack)
    if info is None:
        print(f"Unknown adoption pack: {pack}", file=sys.stderr)
        return 1
    header = "Dry-run adoption plan" if dry_run else "Adoption plan"
    print(f"{header}: {pack}")
    print("Files:")
    for path in info["files"]:
        print(f"- {path}")
    print(f"Gate: {info['gate']}")
    return 0


def main() -> int:
    repo_root = locate_repo_root()
    if repo_root is None:
        print(
            "Could not locate a VCP repository root. Use this wrapper inside a VCP-enabled repository or clone the toolkit first.",
            file=sys.stderr,
        )
        return 1

    args = sys.argv[1:]
    if not args or args[0] in {"-h", "--help", "help"}:
        print_help()
        return 0

    command = args[0]

    if command == "version":
        print(REPO_VERSION)
        return 0

    if command == "route":
        profile = args[1] if len(args) > 1 else "production"
        return route(profile)

    if command == "adopt":
        pack = "production"
        dry_run = False
        rest = args[1:]
        for idx, value in enumerate(rest):
            if value == "--pack" and idx + 1 < len(rest):
                pack = rest[idx + 1]
            if value == "--dry-run":
                dry_run = True
        return adopt(pack, dry_run)

    if command == "score":
        return score("--json" in args[1:])

    if command == "manifest" and len(args) > 1 and args[1] == "validate":
        return manifest_validate(repo_root)

    return run_vibe_check(repo_root, args)


if __name__ == "__main__":
    raise SystemExit(main())
