import subprocess
import sys
from pathlib import Path
import shutil

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


def _copy_developer_validation_fixture(repo_root: Path, destination: Path) -> None:
    shutil.copytree(
        repo_root / "universal-ai-agent-constitution",
        destination / "universal-ai-agent-constitution",
    )
    conformance = destination / "uaac-conformance"
    conformance.mkdir()
    shutil.copy2(
        repo_root / "uaac-conformance/template-schema-map.yaml",
        conformance / "template-schema-map.yaml",
    )
    shutil.copytree(
        repo_root / "uaac-conformance/schemas",
        conformance / "schemas",
    )


def _run_validator(repo_root: Path, target_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "-B",
            str(repo_root / "uaac-conformance/tools/validate_distribution.py"),
            "--repository-root",
            str(target_root),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )


def test_validator_cli_reports_runtime_extensions(repo_root: Path, tmp_path: Path) -> None:
    production = tmp_path / "universal-ai-agent-constitution"
    production.mkdir()
    (production / "UAAC-v5.0-CONSTITUTION.md").write_text(
        "# Controlled fixture\n", encoding="utf-8"
    )
    (production / "runtime.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
    completed = _run_validator(repo_root, tmp_path)

    assert completed.returncode == 1
    assert "runtime extension: universal-ai-agent-constitution/runtime.py" in completed.stdout


def test_validator_cli_rejects_missing_stable_law(repo_root: Path, tmp_path: Path) -> None:
    _copy_developer_validation_fixture(repo_root, tmp_path)
    (tmp_path / "universal-ai-agent-constitution/laws/CONST-025.md").unlink()

    completed = _run_validator(repo_root, tmp_path)

    assert completed.returncode == 1
    assert "law IDs differ from CONST-001..CONST-025" in completed.stdout


def test_validator_cli_rejects_corrupt_canonical_template(
    repo_root: Path, tmp_path: Path
) -> None:
    _copy_developer_validation_fixture(repo_root, tmp_path)
    template_path = (
        tmp_path / "universal-ai-agent-constitution/templates/UAAC-ADOPTION.yaml"
    )
    instance = yaml.safe_load(template_path.read_text(encoding="utf-8"))
    instance["runtime_status"] = "active"
    template_path.write_text(yaml.safe_dump(instance, sort_keys=False), encoding="utf-8")

    completed = _run_validator(repo_root, tmp_path)

    assert completed.returncode == 1
    assert "template/schema violation: uaac-adoption" in completed.stdout


def test_validator_cli_accepts_current_distribution(repo_root: Path) -> None:
    completed = _run_validator(repo_root, repo_root)
    assert completed.returncode == 0
    assert completed.stdout.strip() == "UAAC_CONFORMANCE_PASS"


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
    operational_paths = [
        production_root / "UAAC-v5.0-CONSTITUTION.md",
        production_root / "INSTALL-UAAC.md",
        *sorted((production_root / "laws").glob("*.md")),
        *sorted((production_root / "templates").rglob("*")),
    ]
    for path in operational_paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "uaac-conformance/" in text or "uaac-conformance\\" in text:
            references.append(path.relative_to(production_root).as_posix())
    assert references == []
