from __future__ import annotations

from .utils import load_json, print_output, repo_root, repo_version


def payload() -> dict[str, object]:
    root = repo_root()
    manifest = load_json(root / ".vcp" / "ai-audit-manifest.json")
    return {
        "repository_package_version": repo_version(root),
        "legacy_methodology_reference": manifest.get("methodology_version", "v1.4"),
        "evaluation_modes": manifest.get("evaluation_modes", {}),
        "required_for_full_evaluation": manifest.get("required_for_full_evaluation", []),
        "minimum_raw_files": manifest.get("minimum_raw_files", []),
        "must_report": manifest.get("must_report", []),
        "failure_contract": manifest.get("failure_contract", []),
        "report_template": "templates/reports/ai-repo-audit-coverage-report.md",
        "note": "Do not call shallow summaries a full repository evaluation.",
    }


def run(json_mode: bool = False) -> int:
    data = payload()
    if json_mode:
        print_output(data, True)
        return 0

    print(f"Repository package: {data['repository_package_version']}")
    print("Report the current GitHub repository release using the repository package version above.")
    print("Evaluation modes:")
    for name, description in data["evaluation_modes"].items():
        print(f"- {name}: {description}")
    print("Required for full evaluation:")
    for item in data["required_for_full_evaluation"]:
        print(f"- {item}")
    print("Minimum raw files:")
    for item in data["minimum_raw_files"]:
        print(f"- {item}")
    print("Must report:")
    for item in data["must_report"]:
        print(f"- {item}")
    print("Failure contract:")
    for item in data["failure_contract"]:
        print(f"- {item}")
    print(f"Report template: {data['report_template']}")
    print(data["note"])
    return 0
