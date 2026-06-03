from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root, run_command

DEFAULT_VALIDATION_COMMANDS = [
    "python3 -m vcp_cli cards validate",
    "python3 -m vcp_cli index validate",
    "python3 -m vcp_cli manifest validate",
    "python3 -m vcp_cli benchmark run",
]

AREA_RULES = [
    ("docs", lambda rel: rel.endswith(".md") or rel.startswith("llms") or rel in {"README.md", "README_ru.md", "AGENTS.md", "AI_EVALUATION_GUIDE.md", "AI_INTAKE.md", "START_HERE.md", "CITATION.cff", "ADOPTERS.md"}),
    ("cli", lambda rel: rel.startswith("vcp_cli/") or rel.startswith("bin/")),
    ("templates", lambda rel: rel.startswith("templates/")),
    ("protocols", lambda rel: rel.startswith("protocols/")),
    ("manifests", lambda rel: rel.startswith(".vcp/manifests/")),
    ("workflows", lambda rel: rel.startswith(".vcp/workflows/") or rel == "docs/workflows.md"),
    ("cards", lambda rel: rel.startswith(".vcp/cards/")),
    ("tests", lambda rel: rel.startswith("tests/") or rel.startswith("scripts/tests/")),
    ("public-growth", lambda rel: rel.startswith("protocols/public-growth/") or rel.startswith("templates/public-growth/") or rel.startswith("examples/public-growth/") or "public-growth" in rel or "geo-ai" in rel or "llms" in rel),
]

KEYWORD_RISK_RULES = [
    ("production-critical", ("payment", "payments", "billing", "checkout", "fiscal", "auth", "oauth", "token", "secret", "credential", "session", "jwt", "customer-data", "pii", "gdpr")),
    ("high", ("workflow", "release", "manifest", "schema", "benchmark", "diagnostic", "review-diff")),
    ("medium", ("protocol", "template", "backlog", "architecture", "public-growth", "spec")),
]

ARTIFACT_HINTS = [
    ("PROJECT_BACKLOG.md", ("protocols/", "templates/", "commands/", "vcp_cli/", "tests/", "benchmarks/")),
    ("PROJECT_MAP.md", ("protocols/", "vcp_cli/", ".vcp/workflows/", ".vcp/diagnostics/")),
    ("templates/ARCHITECTURE_SOURCE_OF_TRUTH.md", ("protocols/", "vcp_cli/", "schemas/", ".vcp/workflows/")),
    ("AUDIT_BACKLOG.md", ("protocols/review/", "docs/security", "schemas/vcp-event.schema.json")),
    ("templates/THIRD_PARTY_REGISTRY.md", ("protocols/integrations/", "commands/third-party-api-intake.md")),
    ("docs/release notes", ("README", "docs/", "llms", "CHANGELOG.md", "VERSION")),
    (".vcp/manifests + cards + index", (".vcp/", "vcp_cli/cards.py", "vcp_cli/index_cmd.py", "schemas/vcp-card.schema.json")),
]


def _git_changed_files(root: Path, base: str | None, head: str | None) -> tuple[list[str], str]:
    comparisons: list[tuple[list[str], str]] = []
    if base:
        target_head = head or "HEAD"
        comparisons.extend(
            [
                (["git", "diff", "--name-only", f"{base}...{target_head}"], f"git diff {base}...{target_head}"),
                (["git", "diff", "--name-only", base, target_head], f"git diff {base} {target_head}"),
            ]
        )
    if head and not base:
        comparisons.append((["git", "diff", "--name-only", head], f"git diff {head}"))
    comparisons.extend(
        [
            (["git", "diff", "--name-only", "--cached"], "git diff --name-only --cached"),
            (["git", "diff", "--name-only"], "git diff --name-only"),
        ]
    )
    last_success = ("no git diff data available", [])
    for command, source in comparisons:
        result = run_command(command, root)
        if result.returncode == 0:
            files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            deduped = sorted(set(files))
            last_success = (source, deduped)
    status = run_command(["git", "status", "--short"], root)
    if status.returncode == 0:
        files = sorted({line[3:].strip() for line in status.stdout.splitlines() if len(line) > 3})
        combined = sorted(set(last_success[1]) | set(files))
        if combined:
            source = f"{last_success[0]} + git status --short"
            return combined, source
    return last_success[1], last_success[0]


def _classify_areas(changed_files: list[str]) -> list[str]:
    areas: set[str] = set()
    for rel in changed_files:
        for area, matcher in AREA_RULES:
            if matcher(rel):
                areas.add(area)
    return sorted(areas)


def _estimate_risk(changed_files: list[str], impacted_areas: list[str]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    joined = "\n".join(changed_files).lower()
    risk = "low"
    for candidate, keywords in KEYWORD_RISK_RULES:
        if any(keyword in joined for keyword in keywords):
            risk = candidate
            reasons.append(f"matched keywords for {candidate}: {', '.join(k for k in keywords if k in joined)}")
            break
    if risk == "low" and {"manifests", "cards", "workflows"} & set(impacted_areas):
        risk = "medium"
        reasons.append("changed repository control surfaces")
    if risk == "medium" and {"cli", "protocols", "tests"} <= set(impacted_areas) and "manifests" in impacted_areas:
        risk = "high"
        reasons.append("cross-layer repo changes affect tooling, protocols, tests, and manifests")
    if risk == "high" and any("production" in rel or "release" in rel for rel in changed_files):
        risk = "production-critical"
        reasons.append("production/release-sensitive files changed")
    if not reasons:
        reasons.append("changes stay within low-risk documentation or local tooling scope")
    return risk, reasons


def _spec_recommendation(risk: str, impacted_areas: list[str], changed_files: list[str]) -> tuple[str, str]:
    if not changed_files:
        return "no-spec", "No changed files detected."
    if risk == "production-critical":
        return "governed-spec", "Production/auth/payment/data-sensitive changes need explicit governance."
    if risk == "high":
        return "full-spec", "Cross-layer control-surface changes need a fuller spec and review path."
    if risk == "medium":
        return "spec-lite", "Non-trivial repo changes benefit from scope notes before merge."
    if impacted_areas == ["docs"] or impacted_areas == ["docs", "public-growth"]:
        return "no-spec", "Documentation-only changes can usually take the no-spec path with validation."
    return "spec-lite", "Small but meaningful changes should still capture intent before merge."


def _artifact_hints(changed_files: list[str]) -> list[str]:
    hints: list[str] = []
    for artifact, prefixes in ARTIFACT_HINTS:
        if any(rel.startswith(prefix) or rel == prefix for rel in changed_files for prefix in prefixes):
            hints.append(artifact)
    if any(rel.startswith(("docs/", "README", "llms", "CHANGELOG.md", "VERSION")) for rel in changed_files):
        if "docs/release notes" not in hints:
            hints.append("docs/release notes")
    return hints


def _validation_commands(impacted_areas: list[str], changed_files: list[str]) -> list[str]:
    commands = list(DEFAULT_VALIDATION_COMMANDS)
    if "cli" in impacted_areas:
        commands.extend(
            [
                "python3 -m vcp_cli --help",
                "bash scripts/tests/test-vcp-cli.sh",
                "python3 scripts/tests/test-vcp-cli-windows-parity.py",
            ]
        )
    if "docs" in impacted_areas:
        commands.insert(0, "python3 scripts/validate-links.sh")
    if "manifests" in impacted_areas or "cards" in impacted_areas:
        commands.insert(0, "bash scripts/check-toolkit.sh")
    if any(rel.startswith("docs/platforms/") for rel in changed_files):
        commands.append("python3 -m vcp_cli cards list --type platform --json")
    return list(dict.fromkeys(commands))


def build_payload(base: str | None = None, head: str | None = None) -> dict[str, object]:
    root = repo_root()
    changed_files, diff_source = _git_changed_files(root, base, head)
    impacted_areas = _classify_areas(changed_files)
    risk_level, risk_reasons = _estimate_risk(changed_files, impacted_areas)
    spec_recommendation, spec_reason = _spec_recommendation(risk_level, impacted_areas, changed_files)
    payload = {
        "base": base,
        "head": head,
        "diff_source": diff_source,
        "changed_files": changed_files,
        "changed_file_count": len(changed_files),
        "impacted_areas": impacted_areas,
        "risk_level": risk_level,
        "risk_reasons": risk_reasons,
        "recommended_spec_depth": spec_recommendation,
        "spec_reason": spec_reason,
        "artifacts_to_check": _artifact_hints(changed_files),
        "validation_commands": _validation_commands(impacted_areas, changed_files),
        "notes": [
            "review-diff is a local pre-merge helper; it does not approve, reject, or edit the diff.",
            "No network calls, no automatic fixes, and no destructive writes are performed.",
        ],
    }
    return payload


def run(base: str | None = None, head: str | None = None, json_mode: bool = False) -> int:
    payload = build_payload(base, head)
    if json_mode:
        print_output(payload, True)
        return 0
    print("Review diff summary")
    print(f"Diff source: {payload['diff_source']}")
    print(f"Changed files: {payload['changed_file_count']}")
    print(f"Impacted areas: {', '.join(payload['impacted_areas']) or 'none'}")
    print(f"Risk level: {payload['risk_level']}")
    print(f"Recommended spec depth: {payload['recommended_spec_depth']}")
    if payload["changed_files"]:
        print("Changed files:")
        for rel in payload["changed_files"]:
            print(f"- {rel}")
    if payload["artifacts_to_check"]:
        print("Artifacts to check:")
        for rel in payload["artifacts_to_check"]:
            print(f"- {rel}")
    print("Validation commands:")
    for command in payload["validation_commands"]:
        print(f"- {command}")
    return 0
