# UAAC v4.2 Adoption Guide

## Constitution versus installation versus adoption

- **Constitution:** universal invariants—what must be true
- **Installation:** materializes Project binding, front door, registries, procedures, continuation, adapters and evidence
- **Validation:** proves the installed system resolves and behaves as required
- **Adoption/EFFECTIVE:** Project authority puts the pinned release and Project Law into force

```text
COPIED ≠ INSTALLED ≠ INSTALLATION_VALIDATED ≠ EFFECTIVE
```

## Recommended dependency model

Use an immutable vendored snapshot or equivalent exact pin inside each Project:

```text
Project-A/vendor/uaac/v4.2.0/
```

Do not make Project runtime governance depend on a mutable upstream branch. Upstream is for discovery, upgrade and provenance; the Project front door routes to its locally pinned Constitution

Git submodules can be supported by Project Law but are not the default because uninitialized/drifted submodules create cross-agent byte mismatches

## Greenfield

Create Project definition/requirements, governance, adapters and continuation before feature work. Human authority supplies intent and approval; Agent must not invent Project purpose merely to complete templates

## Brownfield

Inventory and map existing rules/PRD/current state/history first. Preserve one canonical source per semantic role/state class. Conflicts remain explicit and block only affected work

## Monorepo and nested Projects

One effective front door applies per declared Project boundary, not per repository. Child Project binding/front door must be explicit and excluded from parent scans; shared source may be referenced through declared authority maps

## Agent collaboration

ChatGPT and Codex do not synchronize private memory. They converge by resolving:

```text
Project Binding
pinned Constitution
Project Law
State Authority Map
Project Document Registry
Capability/Adapter/Skill Registries
Continuation Index + lineage pointer
artifact base and exact next action
```

Receiver-visible canonical access is mandatory before handoff/continuation is claimed shared

## Upgrade

Install new releases side-by-side, assess law/schema/procedure impacts, rerun generator/validators/scenarios, update adapters and Project Law where needed, then change adoption identity through authorized promotion. Prior lineages retain the governing identities under which they ran
