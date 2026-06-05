from __future__ import annotations

DEMOS = {
    "shared-engine": {
        "route": "Full Hardening",
        "pack": "Shared Engine / Multi-product",
        "gate": "Post-Task Code Review before next feature",
        "action": "Create PROJECT_MAP and Architecture Source of Truth before code changes",
        "score": "90/100 local framework readiness",
    },
    "production": {
        "route": "Full Hardening",
        "pack": "Production",
        "gate": "Post-Task Code Review before merge/release",
        "action": "Confirm release gate, security scope and validation path",
        "score": "88/100 local framework readiness",
    },
    "third-party-api": {
        "route": "Third-party API Intake / Integrations",
        "pack": "Third-party API Intake Pack",
        "gate": "Required before production integration merge or release.",
        "action": "Classify auth, data flow, terms, fallback and owner before implementation.",
        "score": "90/100 local framework readiness",
    },
    "public-site": {
        "route": "Public Site Readiness",
        "pack": "Public Site",
        "gate": "Light review for meaningful docs/config changes",
        "action": "Check canonical docs, llms.txt and publishing checklist",
        "score": "84/100 local framework readiness",
    },
    "review": {
        "route": "Post-Task Code Review",
        "pack": "Post-task Review",
        "gate": "Independent read-only review plus green validation",
        "action": "Inspect git diff and collect validation output",
        "score": "92/100 local framework readiness",
    },
}


def run(name: str | None = None) -> int:
    if name is None:
        for key in DEMOS:
            print(key)
        return 0
    if name not in DEMOS:
        print(f"Unknown demo: {name}")
        return 1
    data = DEMOS[name]
    print(f"Route: {data['route']}")
    print(f"Adoption pack: {data['pack']}")
    print(f"Review gate: {data['gate']}")
    print(f"First action: {data['action']}")
    print(f"Sample score: {data['score']}")
    return 0
