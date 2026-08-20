# ProjectFramework Release Integrity and Certification Roadmap Design — SUPERSEDED

**Status:** `SUPERSEDED_BY_FRAMEWORK_1.1.5_CONCEPT_FIRST_INTENT`

**Original approval:** User explicit approval on 2026-08-20

**Superseded by:** `managing-project-source/references/framework-governance-amendment-260820-1024.md`

---

## Historical Purpose

This design originally explored a progression from Framework governance documentation into release provenance, repository hardening, an executable distribution validator, GitHub Actions, a Golden Reference Project, and fresh-agent certification.

The design produced one useful clarification that remains valid: exact Git provenance must never be fabricated, and a release descriptor must not try to embed the SHA of its own containing commit as a binding identity.

Framework `1.1.4` implemented the provenance portion of that design.

## Why This Roadmap Is Superseded

After real Project bootstrap usage, the user clarified the governing intent of ProjectFramework:

> ProjectFramework is primarily a **conceptual Project governance and planning framework**, not an enforcement-software project.

The prior roadmap over-weighted release engineering and treated mechanisms such as immutable Git tags, branch protection, validators, and CI as if they were part of Framework completion. That interpretation is retired.

## Current Direction

Framework `1.1.5` separates three independent dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

Normal ProjectFramework bootstrap and governance depend on `OPERATIONALLY_USABLE` semantics. Immutable Git provenance and repository hardening are optional assurance; they are not prerequisites unless a Project-Specific Rule explicitly requires them.

The canonical NEW-project flow is:

```text
canonical repository main
→ README
→ FRAMEWORK-RELEASE.yaml
→ SKILL
→ latest Framework amendment + Core Governance
→ Framework template + skeletons + mockup
→ Preview
→ explicit user approval
→ create active 00 first
→ mandatory 01–05 and 09–17
→ conditional 06–08 only when applicable
→ pin Framework/Schema locally
→ optionally record exact Git provenance when actually observed
```

## Retired Default Phase-B Scope

The following items are **not part of the default ProjectFramework roadmap anymore**:

```text
Python Framework validator
CLI enforcement tool
GitHub Actions / CI enforcement
migration engine
background automation
runtime enforcement daemon
branch protection as a Framework usability gate
immutable Git tag as a Framework usability gate
```

They may be designed later only if the user explicitly requests them as a **separate implementation scope**.

## Concept-First Integrity Contract

ProjectFramework still has integrity requirements. They are governance semantics, including:

- Framework/Schema declarations must be internally consistent;
- semantic slots `00–17` must retain their governed meanings;
- `06–08` remain conditional;
- `18–19` remain reserved;
- ChatGPT/Claude shared governance semantics remain equivalent;
- current Stable IDs resolve without archive dependency;
- existing Projects do not silently auto-upgrade;
- platform launchers never override active local `FRAMEWORK-001`;
- missing facts, authority, source, or provenance are never fabricated.

A Human or Agent may evaluate these requirements directly from current Framework sources. The existence of an Integrity Contract is not implicit authorization to build software enforcement.

## Still-Relevant Future Documentation Work

Documentation/concept work remains compatible with the Framework intent, for example:

- a synthetic **Golden Reference Project Source** showing how the core documents compose together;
- migration examples/cookbook expressed as governed documentation;
- clean-room ChatGPT/Claude usage evidence;
- additional platform instruction adapters when a real use case exists;
- further pressure scenarios and governance clarifications.

Each item should remain documentation/concept scope unless executable implementation is explicitly requested.

## Historical Preservation

The full original roadmap remains available in Git history before Framework `1.1.5`. This file intentionally records its supersession rather than continuing to present the retired enforcement-oriented roadmap as current approved direction.
