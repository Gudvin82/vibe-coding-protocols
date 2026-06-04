from __future__ import annotations

from pathlib import Path
from shutil import copy2, copytree, rmtree

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py

PACKAGE_NAME = "vcp_cli"
ASSET_ROOT = Path(PACKAGE_NAME) / "_assets"
TOP_LEVEL_FILES = [
    "VERSION",
    "METHODOLOGY_VERSION",
    "ROADMAP.md",
    "README.md",
    "README_ru.md",
    "CHANGELOG.md",
    "AGENTS.md",
    "AI_EVALUATION_GUIDE.md",
    "AI_FULL_REPO_AUDIT.md",
    "AI_INTAKE.md",
    "FULL_REPO_INTAKE.md",
    "REPO_CAPABILITIES_INDEX.md",
    "TAKE_THIS_FIRST.md",
    "START_HERE.md",
    "CITATION.cff",
    "ADOPTERS.md",
    "PROJECT_BACKLOG.md",
    "PROJECT_MAP.md",
    "package.json",
    "pyproject.toml",
    "setup.py",
    "llms.txt",
    "llms-full.txt",
    "ai.txt",
]
ASSET_DIRS = [
    ".vcp",
    ".github",
    "assets",
    "benchmarks",
    "bin",
    "case-studies",
    "ci-examples",
    "commands",
    "docs",
    "examples",
    "protocols",
    "schemas",
    "scripts",
    "templates",
    "tests",
]


class build_py(_build_py):
    def run(self) -> None:
        super().run()
        repo_root = Path(__file__).resolve().parent
        build_root = Path(self.build_lib).resolve()
        target_root = build_root / ASSET_ROOT

        if target_root.exists():
            rmtree(target_root)
        target_root.mkdir(parents=True, exist_ok=True)

        for rel in TOP_LEVEL_FILES:
            source = repo_root / rel
            if source.exists():
                destination = target_root / rel
                destination.parent.mkdir(parents=True, exist_ok=True)
                copy2(source, destination)

        for rel in ASSET_DIRS:
            source_dir = repo_root / rel
            if source_dir.exists():
                copytree(source_dir, target_root / rel, dirs_exist_ok=True)


setup(cmdclass={"build_py": build_py})
