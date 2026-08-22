import subprocess
import sys
from pathlib import Path

import yaml


ALLOWED_SUFFIXES = {".md", ".yaml", ".yml"}
EXPECTED_ROOT_FILES = {
    "ADOPTION-GUIDE.md",
    "CHANGELOG.md",
    "CONSTITUTION-RELEASE.yaml",
    "INSTALL-UAAC.md",
    "LAW-MANIFEST.yaml",
    "MIGRATION-v4.2-TO-v5.0.md",
    "README.md",
    "UAAC-v5.0-CONSTITUTION.md",
}
EXPECTED_ROOT_DIRECTORIES = {"laws", "profiles", "templates"}
EXPECTED_ENTRYPOINT_HEADINGS = [
    "## Preamble",
    "## Identity and precedence",
    "## Applicability and navigation",
    "## Version and amendment",
    "## Law index",
]


def test_validator_cli_reports_current_boundary_findings(repo_root: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            "uaac-conformance/tools/validate_distribution.py",
            "--repository-root",
            ".",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 1
    assert "missing UAAC-v5.0-CONSTITUTION.md" in completed.stdout


def test_production_extensions_are_runtime_free(production_root: Path) -> None:
    bad = [
        path.relative_to(production_root).as_posix()
        for path in production_root.rglob("*")
        if path.is_file() and path.suffix.lower() not in ALLOWED_SUFFIXES
    ]
    assert bad == []


def test_production_root_layout_is_exact(production_root: Path) -> None:
    files = {path.name for path in production_root.iterdir() if path.is_file()}
    directories = {path.name for path in production_root.iterdir() if path.is_dir()}
    assert files == EXPECTED_ROOT_FILES
    assert directories == EXPECTED_ROOT_DIRECTORIES


def test_v5_entrypoint_replaces_v42_entrypoint(
    production_root: Path, required_file
) -> None:
    required_file(production_root / "UAAC-v5.0-CONSTITUTION.md")
    assert not (production_root / "UAAC-v4.2-CONSTITUTION.md").exists()


def test_entrypoint_has_only_permitted_sections(
    production_root: Path, required_file
) -> None:
    path = required_file(production_root / "UAAC-v5.0-CONSTITUTION.md")
    headings = [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ")
    ]
    assert headings == EXPECTED_ENTRYPOINT_HEADINGS


def test_release_identity_and_boundary_are_v5(production_root: Path) -> None:
    release = yaml.safe_load(
        (production_root / "CONSTITUTION-RELEASE.yaml").read_text(encoding="utf-8")
    )
    assert release["constitution"] == {"id": "UAAC-001", "version": "5.0.0"}
    assert release["normative"] == {"root": "laws", "law_count": 25}
    assert set(release["production_boundary"]["allowed_extensions"]) == ALLOWED_SUFFIXES


def test_manifest_is_navigation_for_exactly_25_laws(production_root: Path) -> None:
    manifest = yaml.safe_load(
        (production_root / "LAW-MANIFEST.yaml").read_text(encoding="utf-8")
    )
    assert manifest["status"] == "NON_NORMATIVE_NAVIGATION"
    assert manifest["constitution"]["version"] == "5.0.0"
    assert [entry["id"] for entry in manifest["laws"]] == [
        f"CONST-{number:03d}" for number in range(1, 26)
    ]


def test_production_has_no_conformance_dependency(production_root: Path) -> None:
    references = []
    for path in production_root.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            if "uaac-conformance/" in text or "uaac-conformance\\" in text:
                references.append(path.relative_to(production_root).as_posix())
    assert references == []
