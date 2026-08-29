# Project Source Framework Governance Amendment — 1.1.5

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.1.4"
project_source_framework_version: "1.1.5"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-20T10:24:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_CONCEPT_FIRST_INTENT_CLARIFICATION"
```

## Purpose

Restore the intended boundary of ProjectFramework: it is a **conceptual Project governance and planning framework first**. It defines source-of-truth semantics, semantic slots, bootstrap behavior, authority, readiness, migration, integrity expectations, pressure scenarios, and reference examples. It does not become an enforcement-software project merely because those concepts can be checked mechanically.

This amendment also separates Framework usability from optional Git/repository assurance so release-engineering mechanics do not block normal Project Source adoption.

## Binding Changes

1. `main` is the canonical upstream bootstrap source for **NEW** Project Source creation.
2. A NEW Project may bootstrap directly from the current approved Framework on `main`; an immutable Git tag is **not required** for operational use.
3. Exact Git provenance such as release tag and resolved commit SHA is optional assurance. Record it when actually observed; never invent or backfill it.
4. Missing tag/SHA provenance MUST NOT by itself block Framework bootstrap, Project Source creation, readiness, or normal Framework use.
5. Git tag creation, branch protection, rulesets, CI, and similar repository controls are optional release/repository assurance. They are not Project Source semantic prerequisites.
6. Framework status dimensions are independent:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

`OPERATIONALLY_USABLE` answers whether the Framework can correctly bootstrap/govern a Project. `REPRODUCIBLY_RELEASED` is optional assurance that an immutable source identity has been preserved. `REPOSITORY_HARDENED` is optional assurance about repository mutation controls. Absence of either optional assurance does not make an otherwise usable Framework unusable.
7. ProjectFramework defines **Integrity Contracts as governance semantics**. Agents/humans may evaluate those contracts from the distribution. The Framework MUST NOT automatically expand an integrity requirement into executable validators, CLIs, CI workflows, migration engines, background automation, or enforcement software.
8. Executable enforcement tooling may be designed only when the user explicitly requests it as a separate implementation scope. A conceptual integrity rule is not implicit authorization to build software.
9. Existing Projects remain locally pinned and never auto-upgrade from upstream. Upgrade continues through governed `MIG-*` assessment and explicit approval.
10. Project Source Schema remains `1.0.0`.

## Concept-First Integrity Contract

Framework distribution integrity means, at minimum:

- current Framework/Schema declarations are internally consistent;
- semantic slots `00–17` retain their governed meanings;
- `06–08` remain conditional;
- `18–19` remain reserved;
- ChatGPT and Claude shared governance semantics remain equivalent;
- active/current Stable IDs resolve without archive dependency;
- existing Projects do not silently auto-upgrade;
- platform launchers never override active local `FRAMEWORK-001`;
- missing facts, authority, source, or provenance are never fabricated.

These are **semantic requirements**. They may be checked manually or by an Agent using the current Framework sources. They do not require a software validator to exist.

## Bootstrap Contract

```text
NEW Project
→ read canonical repository main
→ README
→ FRAMEWORK-RELEASE.yaml
→ SKILL
→ latest amendment + Core Governance
→ Framework template + skeletons + mockup
→ Preview
→ explicit user approval
→ create active 00 first
→ mandatory 01–05 and 09–17
→ conditional 06–08 only when applicable
→ pin Framework/Schema locally
→ optionally record exact Git provenance when observed
```

If exact Git tag/SHA provenance is unavailable, continue normal bootstrap from the verified canonical source. Record provenance as `UNKNOWN`, `UNVERIFIED`, or equivalent only when provenance tracking is material; do not fabricate a value.

## Operational vs Assurance State

Examples:

```text
OPERATIONALLY_USABLE + REPRODUCIBLE_PROVENANCE_UNVERIFIED
OPERATIONALLY_USABLE + REPOSITORY_HARDENING_NOT_CONFIGURED
```

are valid states. Optional assurance gaps may be reported, but they are not blockers unless a Project-Specific Rule explicitly makes them blockers.

## Supersession of Prior Roadmap Interpretation

Framework `1.1.4` remains historical truth for the provenance clarification it introduced, especially the rule against fabricated Git identity. However, any interpretation of `1.1.4` that makes immutable tags, exact commit provenance, branch protection, executable integrity validators, or CI enforcement prerequisites for normal Framework usability is superseded by this `1.1.5` amendment.

The previously proposed executable Phase-B validator/CI roadmap is **retired from the default ProjectFramework roadmap**. Such tooling is future optional scope only if explicitly requested as a separate implementation project.

## Non-Goals

This amendment does not add executable validation code, GitHub Actions, a CLI, a migration engine, background automation, repository-protection mutations, Claude Code instructions, Codex-specific instructions, or Gemini-specific instructions.

## Precedence

This `1.1.5` amendment is the latest binding clarification for Framework intent, bootstrap usability, release assurance, and tooling scope. Earlier amendments remain binding for their non-conflicting subjects, including platform launcher equivalence, bootstrap namespace semantics, Materialized Current State, Stable-ID resolution, Manifest/CURRENT completeness, archive independence, and preservation of historical truth.
