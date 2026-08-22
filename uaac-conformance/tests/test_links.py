from pathlib import Path
from urllib.parse import unquote


def _local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target.split("#", 1)[0])
    return (source.parent / target).resolve()


def test_current_markdown_links_resolve(
    repo_root: Path, production_root: Path, markdown_targets
) -> None:
    roots = [
        repo_root / "README.md",
        repo_root / "UAAC.md",
        repo_root / "HUMAN-INSTALL-WALKTHROUGH-TH.md",
        production_root,
        repo_root / "docs/uaac-history/v4.2",
    ]
    broken = []
    sources = []
    for root in roots:
        if root.is_file():
            sources.append(root)
        elif root.exists():
            sources.extend(root.rglob("*.md"))
    for source in sources:
        for raw_target in markdown_targets(source):
            target = _local_target(source, raw_target)
            if target is not None and not target.exists():
                broken.append(
                    f"{source.relative_to(repo_root).as_posix()} -> {raw_target}"
                )
    assert broken == []


def test_manifest_law_locators_resolve(production_root: Path, required_yaml) -> None:
    manifest = required_yaml(production_root / "LAW-MANIFEST.yaml")
    broken = [
        entry["locator"]
        for entry in manifest["laws"]
        if not (production_root / entry["locator"]).is_file()
    ]
    assert broken == []
