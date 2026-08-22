from pathlib import Path


V42_RELEASE_COMMIT = "5a309d8d38046bf3e8cd4beb2fc82a872f211cad"
V42_PACKAGE_TREE = "3e62912bcbd88d91339dfa772dc6776ee95c77c5"
V42_REFERENCE_COMMIT = "5cc9488427c8034a67f4898ace5f1c5806760b85"


def test_historical_core_tree_is_immutable(git_stdout) -> None:
    assert (
        git_stdout("rev-parse", f"{V42_RELEASE_COMMIT}:universal-ai-agent-constitution")
        == V42_PACKAGE_TREE
    )


def test_completed_reference_fixture_is_immutable(git_stdout) -> None:
    paths = git_stdout(
        "ls-tree", "-r", "--name-only", V42_REFERENCE_COMMIT, "--", "uaac-v4.2-reference-project"
    ).splitlines()
    assert len(paths) == 27


def test_current_reference_fixture_has_no_mutable_remote_locator(repo_root: Path) -> None:
    root = repo_root / "uaac-v4.2-reference-project"
    forbidden = ("blob/hz-framework", "ref: hz-framework", "canonical_ref_policy: hz-framework")
    findings = []
    for path in root.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for value in forbidden:
                if value in text:
                    findings.append(f"{path.relative_to(root).as_posix()}: {value}")
    assert findings == []


def test_current_reference_core_routes_are_commit_qualified(repo_root: Path) -> None:
    root = repo_root / "uaac-v4.2-reference-project"
    unsafe = []
    for path in root.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            if "universal-ai-agent-constitution/" in text and V42_RELEASE_COMMIT not in text:
                unsafe.append(path.relative_to(root).as_posix())
    assert unsafe == []


def test_history_inventory_records_all_reconstruction_identities(
    repo_root: Path, required_yaml
) -> None:
    inventory = required_yaml(repo_root / "docs/uaac-history/v4.2/REFERENCE-INVENTORY.yaml")
    assert inventory["release_commit"] == V42_RELEASE_COMMIT
    assert inventory["package_tree"] == V42_PACKAGE_TREE
    assert inventory["reference_fixture_commit"] == V42_REFERENCE_COMMIT
    assert set(inventory["historical_categories"]) == {
        "runbooks",
        "schemas",
        "validators",
        "fixtures_and_scenarios",
        "threat_and_system_reviews",
        "registers",
        "skills",
        "templates",
        "validation_output",
    }
