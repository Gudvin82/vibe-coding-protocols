from __future__ import annotations

from pathlib import Path
from typing import Any
from urllib import error, request

from .utils import print_output, repo_root

LOCAL_CHECKS = {
    "llms_txt": "llms.txt",
    "llms_full_txt": "llms-full.txt",
    "ai_txt": "ai.txt",
    "citation": "CITATION.cff",
    "glossary": "docs/glossary.md",
    "comparison": "docs/comparison.md",
    "faq": "docs/faq.md",
    "proof_pack": "docs/proof-pack.md",
    "public_growth_checklist": "docs/public-growth/public-growth-checklist.md",
    "geo_checks": "docs/public-growth/geo-checks.md",
    "source_of_truth": "docs/public-source-of-truth-audit.md",
}


def _bool_check(root: Path, rel: str) -> dict[str, object]:
    path = root / rel
    return {
        "path": rel,
        "present": path.exists(),
    }


def payload(site: str | None = None, root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    checks = {name: _bool_check(root, rel) for name, rel in LOCAL_CHECKS.items()}
    sitemap = (root / "sitemap.xml").exists()
    robots = (root / "robots.txt").exists()
    case_studies_dir = root / "case-studies"
    case_count = len(list(case_studies_dir.rglob("README.md"))) if case_studies_dir.exists() else 0

    ready = [name for name, result in checks.items() if result["present"]]
    missing = [name for name, result in checks.items() if not result["present"]]

    network: dict[str, object] = {"requested": bool(site), "status": "not_requested"}
    if site:
        try:
            with request.urlopen(site, timeout=5) as response:  # noqa: S310
                network = {
                    "requested": True,
                    "status": "ok",
                    "site": site,
                    "http_status": getattr(response, "status", None),
                }
        except Exception as exc:  # noqa: BLE001
            status = "network_unavailable"
            if isinstance(exc, error.HTTPError):
                status = "http_error"
            network = {
                "requested": True,
                "status": status,
                "site": site,
                "reason": str(exc),
            }

    return {
        "repository_package_version": (root / "VERSION").read_text(encoding="utf-8").strip(),
        "legacy_methodology_reference": (root / "METHODOLOGY_VERSION").read_text(encoding="utf-8").strip(),
        "technical_seo_readiness": {
            "robots_txt_present": robots,
            "sitemap_xml_present": sitemap,
            "citation_present": checks["citation"]["present"],
        },
        "geo_answer_engine_readiness": {
            "llms_txt_present": checks["llms_txt"]["present"],
            "llms_full_txt_present": checks["llms_full_txt"]["present"],
            "ai_txt_present": checks["ai_txt"]["present"],
            "entity_clarity_docs": [
                checks["glossary"]["path"],
                checks["comparison"]["path"],
                checks["faq"]["path"],
            ],
        },
        "public_proof": {
            "case_study_readme_count": case_count,
            "proof_pack_present": checks["proof_pack"]["present"],
            "source_of_truth_present": checks["source_of_truth"]["present"],
        },
        "checks": checks,
        "network": network,
        "ready_signals": ready,
        "missing_signals": missing,
        "guarantees": [
            "No ranking guarantees.",
            "No AI overview or citation guarantees.",
            "No fake reviews or black-hat SEO allowed.",
        ],
        "next_steps": [
            "Use the local checks first before making public claims.",
            "Treat network_unavailable as a visibility limit, not as proof of failure.",
            "Generate a structured report before changing public growth content.",
        ],
    }


def run(site: str | None = None, json_mode: bool = False) -> int:
    data = payload(site)
    if json_mode:
        print_output(data, True)
    else:
        print("Public Growth Check")
        print(f"Repository package: {data['repository_package_version']}")
        print(f"Ready signals: {len(data['ready_signals'])}")
        print(f"Missing signals: {len(data['missing_signals'])}")
        if site:
            print(f"Network status: {data['network']['status']}")
    return 0
