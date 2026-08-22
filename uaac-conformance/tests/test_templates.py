import copy
from pathlib import Path

import jsonschema
import pytest


PAIR = {
    "id": "uaac-adoption",
    "template": "universal-ai-agent-constitution/templates/UAAC-ADOPTION.yaml",
    "schema": "uaac-conformance/schemas/uaac-adoption.schema.json",
    "negative_mutation": {
        "operation": "add_root_key",
        "key": "runtime_status",
        "value": "active",
    },
}
FORBIDDEN_ROOT_FIELDS = (
    "runtime_status",
    "epoch",
    "boot_receipt",
    "claim_token",
    "boot_mode",
    "runtime_state",
    "validation_result",
    "adapter_registry",
    "capability_graph",
    "registry",
    "tool_config",
)


def _errors(instance, schema) -> list[str]:
    validator = jsonschema.Draft202012Validator(schema)
    return sorted(error.message for error in validator.iter_errors(instance))


def test_template_schema_map_is_complete(repo_root: Path, required_yaml) -> None:
    mapping = required_yaml(repo_root / "uaac-conformance/template-schema-map.yaml")
    assert mapping == {
        "document_type": "UAAC_TEMPLATE_SCHEMA_MAP",
        "status": "DEVELOPER_ONLY_NON_NORMATIVE",
        "pairs": [PAIR],
    }


def test_declared_template_validates(repo_root: Path, required_yaml) -> None:
    instance = required_yaml(repo_root / PAIR["template"])
    schema = required_yaml(repo_root / PAIR["schema"])
    assert _errors(instance, schema) == []


def test_declared_pair_rejects_its_independent_corruption(
    repo_root: Path, required_yaml
) -> None:
    instance = copy.deepcopy(required_yaml(repo_root / PAIR["template"]))
    schema = required_yaml(repo_root / PAIR["schema"])
    mutation = PAIR["negative_mutation"]
    instance[mutation["key"]] = mutation["value"]
    assert _errors(instance, schema)


@pytest.mark.parametrize("forbidden", FORBIDDEN_ROOT_FIELDS)
def test_adoption_schema_rejects_runtime_machinery(
    repo_root: Path, required_yaml, forbidden: str
) -> None:
    instance = copy.deepcopy(required_yaml(repo_root / PAIR["template"]))
    schema = required_yaml(repo_root / PAIR["schema"])
    instance[forbidden] = {"enabled": True}
    assert _errors(instance, schema)


def test_adoption_schema_allows_only_minimal_top_level_semantics(
    repo_root: Path, required_yaml
) -> None:
    schema = required_yaml(repo_root / PAIR["schema"])
    assert schema["additionalProperties"] is False
    assert set(schema["required"]) == {"project", "constitution"}
    assert set(schema["properties"]) == {
        "project",
        "constitution",
        "project_rules",
        "canonical_sources",
        "continuation",
        "profiles",
    }


def test_canonical_template_omits_unused_optional_sections(
    repo_root: Path, required_yaml
) -> None:
    instance = required_yaml(repo_root / PAIR["template"])
    assert set(instance) == {"project", "constitution"}
    assert set(instance["project"]) == {"id", "boundary"}
    assert set(instance["constitution"]) == {
        "id",
        "version",
        "local_locator",
        "immutable_identity",
    }
