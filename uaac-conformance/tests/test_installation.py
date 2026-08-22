from pathlib import Path

import jsonschema
import pytest
import yaml


def _text(path: Path, required_file) -> str:
    return required_file(path).read_text(encoding="utf-8")


def test_installer_defines_the_runtime_free_minimum(
    production_root: Path, required_file
) -> None:
    text = _text(production_root / "INSTALL-UAAC.md", required_file).lower()
    for required in (
        "persistent launcher",
        "governance/uaac.md",
        "governance/uaac-adoption.yaml",
        "locally readable pinned constitution",
    ):
        assert required in text
    assert "installing uaac does not install or upgrade projectframework" in text


def test_installer_keeps_project_rules_conditional(
    production_root: Path, required_file
) -> None:
    text = _text(production_root / "INSTALL-UAAC.md", required_file).lower()
    assert "reuse" in text and "existing project rules" in text
    assert "do not create an empty" in text


def test_installer_defaults_to_local_offline_release(
    production_root: Path, required_file
) -> None:
    text = _text(production_root / "INSTALL-UAAC.md", required_file).lower()
    assert "network" in text and "unavailable" in text
    assert "vendor" in text
    assert "remote" in text and "provenance" in text


def test_project_router_is_small_and_non_authoritative(
    production_root: Path, required_file
) -> None:
    text = _text(production_root / "templates" / "PROJECT-UAAC.md", required_file).lower()
    for required in (
        "non-authoritative",
        "bounded set",
        "materially required",
        "sufficient complete coverage",
        "local",
        "auto-boot",
    ):
        assert required in text
    for forbidden in ("boot receipt", "runtime state", "independent authority"):
        assert forbidden not in text


def test_platform_launchers_route_only_to_project_router(
    production_root: Path, required_file
) -> None:
    platform = production_root / "templates" / "platform"
    for name in (
        "AGENTS.md",
        "CHATGPT-PROJECT-INSTRUCTIONS.md",
        "GENERIC-AGENT-INSTRUCTIONS.md",
    ):
        text = _text(platform / name, required_file).lower()
        assert "governance/uaac.md" in text
        assert "without requiring the user to restate uaac" in text
        assert "independent authority" in text


def test_no_python_constitutional_acceptance_has_exact_scenarios(
    repo_root: Path, required_file
) -> None:
    path = required_file(repo_root / "uaac-conformance/CONSTITUTIONAL-ACCEPTANCE.md")
    text = path.read_text(encoding="utf-8")
    ids = [line.split()[1] for line in text.splitlines() if line.startswith("## CA-")]
    assert ids == [f"CA-{number:02d}" for number in range(1, 12)]
    for heading in ("Given", "When", "Then", "Required reading", "No executable prerequisite"):
        assert text.count(f"**{heading}:**") == 11


def test_greenfield_fixture_has_only_required_adoption(
    repo_root: Path, required_file
) -> None:
    root = repo_root / "uaac-conformance/fixtures/greenfield"
    adoption = yaml.safe_load(
        _text(root / "governance" / "UAAC-ADOPTION.yaml", required_file)
    )
    assert set(adoption) == {"project", "constitution"}
    assert not (root / "governance" / "PROJECT-RULES.md").exists()
    assert "continuation" not in adoption


def test_brownfield_fixture_reuses_real_sources(
    repo_root: Path, required_file
) -> None:
    root = repo_root / "uaac-conformance/fixtures/brownfield"
    adoption = yaml.safe_load(
        _text(root / "governance" / "UAAC-ADOPTION.yaml", required_file)
    )
    assert adoption["project_rules"] == [{"locator": "governance/PROJECT-RULES.md"}]
    assert adoption["canonical_sources"] == [
        {"role": "product_definition", "locator": "project-docs/PRD.md"},
        {"role": "current_state", "locator": "project-docs/CURRENT-STATE.md"},
    ]
    assert adoption["continuation"] == {"locator": "project-docs/CURRENT-STATE.md"}


def test_migration_fixture_preserves_old_pin_and_qualified_rollback(
    repo_root: Path, required_file
) -> None:
    root = repo_root / "uaac-conformance/fixtures/migration-v4.2"
    mapping = yaml.safe_load(_text(root / "MIGRATION-MAP.yaml", required_file))
    rollback = _text(root / "ROLLBACK-NOTES.md", required_file).lower()
    assert mapping["v4_2_release_commit"] == "5a309d8d38046bf3e8cd4beb2fc82a872f211cad"
    assert mapping["v5_local_locator"].endswith("UAAC-v5.0-CONSTITUTION.md")
    assert "compatibility" in rollback and "remap" in rollback


@pytest.mark.parametrize("fixture_name", ["greenfield", "brownfield"])
def test_project_fixture_adoption_validates_and_local_constitution_resolves(
    repo_root: Path, required_file, fixture_name: str
) -> None:
    fixture_root = repo_root / "uaac-conformance" / "fixtures" / fixture_name
    adoption = yaml.safe_load(
        _text(fixture_root / "governance" / "UAAC-ADOPTION.yaml", required_file)
    )
    schema = yaml.safe_load(
        _text(repo_root / "uaac-conformance/schemas/uaac-adoption.schema.json", required_file)
    )
    errors = sorted(
        error.message
        for error in jsonschema.Draft202012Validator(schema).iter_errors(adoption)
    )
    assert errors == []
    local_constitution = (
        fixture_root / adoption["constitution"]["local_locator"]
    ).resolve()
    assert local_constitution.is_file()
    assert local_constitution.name == "UAAC-v5.0-CONSTITUTION.md"


def test_root_readme_separates_current_products_and_support_boundaries(
    repo_root: Path, required_file
) -> None:
    text = _text(repo_root / "README.md", required_file).lower()
    for required in (
        "project source framework 1.2.5",
        "universal ai agent constitution (uaac) 5.0.0",
        "install uaac != install or upgrade projectframework",
        "developer-only conformance",
        "historical/reference v4.2",
    ):
        assert required in text


def test_root_uaac_navigation_routes_current_and_historical_material(
    repo_root: Path, required_file
) -> None:
    text = _text(repo_root / "UAAC.md", required_file)
    for locator in (
        "universal-ai-agent-constitution/UAAC-v5.0-CONSTITUTION.md",
        "universal-ai-agent-constitution/INSTALL-UAAC.md",
        "universal-ai-agent-constitution/MIGRATION-v4.2-TO-v5.0.md",
        "universal-ai-agent-constitution/profiles/",
        "uaac-conformance/",
        "docs/uaac-history/v4.2/",
    ):
        assert locator in text


def test_root_human_walkthrough_uses_v5_minimum(
    repo_root: Path, required_file
) -> None:
    text = _text(repo_root / "HUMAN-INSTALL-WALKTHROUGH-TH.md", required_file).lower()
    for required in (
        "governance/uaac.md",
        "governance/uaac-adoption.yaml",
        "uaac-v5.0-constitution.md",
        "project rules",
        "conditional",
        "does not install or upgrade projectframework",
    ):
        assert required in text


def test_root_navigation_links_patch_audit_artifacts(
    repo_root: Path, required_file
) -> None:
    report = "docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-REPORT.md"
    state = "docs/uaac-repair/UAAC-CONSTITUTION-FIRST-PATCH-STATE.yaml"
    for navigation in (repo_root / "README.md", repo_root / "UAAC.md"):
        text = _text(navigation, required_file)
        assert report in text
        assert state in text
