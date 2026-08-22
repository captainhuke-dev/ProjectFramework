from pathlib import Path


LAW_IDS = tuple(f"CONST-{number:03d}" for number in range(1, 26))
LAW_HEADINGS = [
    "## Constitutional requirements",
    "## Compliance",
    "## Non-prescription",
]
REQUIRED_CONCEPTS = {
    "CONST-001": ("universal constitutional scope", "applicable constraints", "substrate"),
    "CONST-002": ("identity", "responsibility", "capability", "authority", "permission"),
    "CONST-003": ("human-origin authority", "delegation", "revocation", "accountability"),
    "CONST-004": ("truthful identity", "agent", "entity", "impersonat"),
    "CONST-005": ("current truth", "uncertainty", "conflict", "memory != current truth"),
    "CONST-006": ("proportional evidence", "traceability", "unverifiable"),
    "CONST-007": ("instruction authority", "untrusted input", "conflict"),
    "CONST-008": ("bounded set", "materially required", "sufficient complete coverage", "cannot establish complete coverage"),
    "CONST-009": ("recover", "canonical source", "before guessing", "unavailable"),
    "CONST-010": ("risk", "authority limit", "safe escalation", "reversib"),
    "CONST-011": ("honest capability", "limitation", "invent access"),
    "CONST-012": ("decision basis", "countercase", "uncertainty", "change conditions"),
    "CONST-013": ("semantic fidelity", "abridgment", "conceal"),
    "CONST-014": ("durable continuation", "materially", "sufficient recovery"),
    "CONST-015": ("safe handoff", "receiver verification", "authority transfer"),
    "CONST-016": ("artifact identity", "freshness", "synchronization", "conflict"),
    "CONST-017": ("execution", "verification", "acceptance", "publication", "deployment", "closure"),
    "CONST-018": ("scoped fail-closed", "non-compliance", "unaffected work"),
    "CONST-019": ("proportional reproducibility", "reconstruction", "limits"),
    "CONST-020": ("tools", "frameworks", "optional", "subordinate", "presence is not authority"),
    "CONST-021": ("minimal adoption", "local constitution", "actual routes", "explicitly adopted profiles"),
    "CONST-022": ("amendment", "version", "migration", "rollback", "source-appropriate", "immutable or verifiable identity"),
    "CONST-023": ("reusable procedures", "optional", "automatically consider", "native skill"),
    "CONST-024": ("retrieval", "memory", "derived context", "non-authoritative", "source verification"),
    "CONST-025": ("claim != proof", "epistemic honesty", "evidence-backed status"),
}
FORBIDDEN_NORMATIVE_MECHANISMS = (
    "boot receipt",
    "state authority map",
    "capability pack",
    "adapter registry",
    "skill registry",
    "claim contract registry",
    "document registry",
    "continuation index",
    "lineage epoch",
    "llm wiki",
    "json schema",
    "validator cli",
    "projectframework",
)


def _law_paths(production_root: Path) -> list[Path]:
    return sorted((production_root / "laws").glob("CONST-*.md"))


def _requirements(text: str) -> str:
    start = text.find("## Constitutional requirements")
    end = text.find("## Compliance")
    assert start >= 0 and end > start
    return text[start:end].lower()


def test_law_ids_are_exact_and_unique(production_root: Path) -> None:
    assert tuple(path.stem for path in _law_paths(production_root)) == LAW_IDS


def test_each_law_has_one_uniform_normative_shape(production_root: Path) -> None:
    for path in _law_paths(production_root):
        headings = [
            line
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.startswith("## ")
        ]
        assert headings == LAW_HEADINGS, path.name


def test_each_law_preserves_its_universal_property(production_root: Path) -> None:
    for path in _law_paths(production_root):
        requirements = _requirements(path.read_text(encoding="utf-8"))
        missing = [
            concept for concept in REQUIRED_CONCEPTS[path.stem] if concept not in requirements
        ]
        assert missing == [], f"{path.name}: {missing}"


def test_normative_requirements_do_not_prescribe_v42_machinery(
    production_root: Path,
) -> None:
    for path in _law_paths(production_root):
        requirements = _requirements(path.read_text(encoding="utf-8"))
        leaked = [term for term in FORBIDDEN_NORMATIVE_MECHANISMS if term in requirements]
        assert leaked == [], f"{path.name}: {leaked}"


def test_const_008_bounds_reading_without_false_coverage(production_root: Path) -> None:
    requirements = _requirements(
        (production_root / "laws" / "CONST-008.md").read_text(encoding="utf-8")
    )
    assert "search" in requirements
    assert "summary" in requirements
    assert "cannot establish complete coverage" in requirements
    assert "every applicable canonical source" not in requirements


def test_const_022_has_no_universal_hash_requirement(production_root: Path) -> None:
    requirements = _requirements(
        (production_root / "laws" / "CONST-022.md").read_text(encoding="utf-8")
    )
    assert "source-appropriate" in requirements
    assert "no particular identity or integrity mechanism is universally mandatory" in requirements
    assert "must hash" not in requirements
