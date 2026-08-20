---
name: managing-project-source
description: Use when creating, adopting, importing, updating, reviewing, handing off, or exporting a Project Source; when a project needs consistent governance, naming, source-of-truth handling, continuation context, or cross-agent documentation.
---

# Managing Project Source

## Overview

Maintain a consistent `Project-Source/` governance layer. Make **current truth, current authority, and exact next action** explicit without inventing facts.

ProjectFramework is **conceptual governance/planning first**. Integrity requirements are semantic contracts. **Do not expand documentation/governance/integrity work into validator, CLI, CI, migration engine, background automation, or enforcement software unless the user explicitly requests a separate implementation scope.**

## Required References

Before creating or materially changing Project Source, read:

- `FRAMEWORK-RELEASE.yaml` for the current distribution identity and bootstrap policy
- `references/framework-governance-amendment-260820-1024.md`
- `references/framework-governance-amendment-260820-0821.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0735.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0707.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0646.md` (historical approved amendment)
- `references/framework-governance-amendment-260814-0808.md` (historical approved amendment)
- `references/core-governance-rules.md`
- `templates/00-project-source-framework.md`
- `templates/core-document-skeletons.md` for new Project Source
- `templates/project-source-mockup/README.md` to resolve semantic-slot/document mapping and starter filenames

Use historical design/spec files only for rationale/edge cases. The latest Framework amendment wins on conflicts.

## Platform Project Bootstrap Entrypoints

The distribution provides two official platform launcher artifacts:

- `CHATGPT-PROJECT-INSTRUCTIONS.md` — paste into ChatGPT Project settings → Instructions.
- `CLAUDE-PROJECT-INSTRUCTIONS.md` — paste into Claude Project → Set project instructions.

Both files MUST contain the same byte-identical shared governance contract between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END`. Platform-specific wrapper text may identify the placement surface, but bootstrap semantics, local authority, migration behavior, optional provenance behavior, and scope boundaries must not diverge.

These platform instructions are **bootstrap/continuation launchers only**. If a valid local Project Source with active `FRAMEWORK-001` already exists, the locally pinned Project Source is authoritative. Platform instructions MUST NOT replace, weaken, bypass, or override the active local Framework.

For a NEW Project, canonical upstream bootstrap begins from repository `main`. Exact Git tag/SHA provenance is optional assurance; absence of that assurance does not block normal Framework bootstrap.

## Concept-First Intent

ProjectFramework defines:

- Project governance concepts;
- semantic namespace `00–99`;
- source-of-truth and uncertainty rules;
- actor/authority/risk semantics;
- bootstrap and initial creation gates;
- Current Truth / archive independence;
- handoff, migration, export, readiness, and retention semantics;
- integrity contracts, pressure scenarios, mockups, and reference examples.

It does **not** automatically implement enforcement software. A statement such as “Framework versions must agree” means the distribution must semantically satisfy that requirement; it does not implicitly authorize writing a Python validator or GitHub Actions workflow.

Executable tooling is a separate project/scope requiring explicit user request.

## Operational Use vs Optional Assurance

Treat these as independent dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

- `OPERATIONALLY_USABLE` — the Framework can correctly bootstrap/govern a Project from the canonical source.
- `REPRODUCIBLY_RELEASED` — optional assurance that an immutable source identity (for example a tag + commit) was preserved.
- `REPOSITORY_HARDENED` — optional assurance such as branch protection/rulesets.

Missing optional release/repository assurance MUST NOT by itself block Project Source creation or make an otherwise usable Framework unusable unless Project-Specific Rules explicitly require it.

## Optional Source Provenance

`FRAMEWORK-RELEASE.yaml` is Framework distribution metadata, not a Project Source semantic slot and not Root Governance.

For NEW Project bootstrap:

```text
read canonical main
→ README
→ FRAMEWORK-RELEASE.yaml
→ SKILL + latest amendment + Core Governance
→ Framework template + skeletons + mockup
→ Preview → explicit user approval → write
→ pin Framework/Schema locally
→ optionally record exact Git provenance when actually observed
```

If tag/SHA provenance is actually observed, record it accurately in active `00` and corresponding `14-Manifest` continuation metadata when material. If exact provenance is unavailable, do not fabricate it and do not stop otherwise valid bootstrap solely because that optional assurance is missing. Use `UNKNOWN`, `UNVERIFIED`, or equivalent when provenance state must be represented.

Existing Projects MUST NOT retroactively backfill an unobserved historical SHA merely to look complete.

## Root Framework Invariant

`00-Project Source Framework` (`FRAMEWORK-001`) is the **non-removable Root Governance** of every Project Source. It MUST remain active in semantic slot `00`. Missing Framework means `INVALID + NOT_OPERATIONALLY_READY`.

Every Project artifact created after it is governed by and inherits from the Framework. Project Source artifacts inherit directly; implementation code/config/runtime artifacts inherit governance through linked Requirements, Decisions, Authority, and Project identity. Markdown descendants declare:

```yaml
inherits_from:
  - "FRAMEWORK-001"
```

Non-Markdown artifacts inherit through their canonical Registry/Manifest entry.

Descendants may **extend or specialize** but MUST NOT remove, bypass, demote, replace, weaken, or contradict Framework invariants. To change a Root invariant, revise the Framework itself with explicit user approval, preserve `FRAMEWORK-001`, and archive the superseded revision.

## Materialized Current State Invariant

Active canonical registries are **materialized current projections, not delta chains**. Every active/current Stable ID referenced by the current Project Source MUST resolve from the **Current Reconstructable Snapshot** to a current authoritative record. Archive may explain historical rationale or evolution, but it MUST NOT be required to determine Current Truth.

For current authoritative payload, shorthand such as `retain previous status`, `unchanged from rNNN`, or `see archived revision` is insufficient when the actual semantics exist only in archive. The active canonical record must contain enough current semantic payload to identify what is true now, or it must link to an active/current canonical Detail Document that contains that payload. Any such required Detail Document is part of the Current Reconstructable Snapshot and must travel with a `CURRENT` export when needed to interpret the Stable ID.

This applies directly to `DEC-*` in `04-Decision Log` and `REQ-*` in `05-Requirements`, and generally to current-state-bearing canonical object homes.

## Concept-First Integrity Contract

At minimum, current Framework distribution integrity means:

1. current Framework/Schema declarations agree across current distribution artifacts;
2. semantic slots `00–17` retain their governed meanings;
3. `06–08` remain conditional;
4. `18–19` remain reserved;
5. ChatGPT/Claude shared governance semantics remain equivalent;
6. referenced current Stable IDs resolve without archive traversal;
7. existing Projects never silently auto-upgrade;
8. platform launchers never outrank or override active local `FRAMEWORK-001`;
9. missing facts, authority, source, or provenance are never fabricated.

A human or Agent may review these contracts directly from Framework sources. Do not infer an executable enforcement requirement from them.

## Workflow

1. Classify `GREENFIELD`, `BROWNFIELD`, or `IMPORT`. For a platform Project, first use the matching canonical platform instruction artifact to determine whether a valid local Project Source already exists.
2. For `GREENFIELD`, read canonical repository `main` in the governed bootstrap order. Exact Git provenance may be captured when observed but is not required for normal bootstrap.
3. Resolve explicit `FAST`/`GRILL`; otherwise use `ADAPTIVE`.
4. Confirm active `FRAMEWORK-001`; if missing in an existing Project Source, stop affected work and propose governed repair.
5. Existing Project: bootstrap `00 → 01 → 03`, then follow `01` routing. Do not silently replace the local pin with upstream `main`.
6. Inspect accessible project sources before asking; do not ask for facts you can verify.
7. Classify important claims by Truth Domain, Epistemic Status, and Freshness. Use `DRIFT-*` / `CONFLICT-*`; never silently reconcile.
8. Initial creation or major structural migration requires Preview → explicit user approval → write.
9. Follow Core Governance for naming, revisions, archive, canonical object homes, authority, handoff, evidence, and exports.
10. For new-project bootstrap, map semantic slots from `templates/project-source-mockup/README.md`: instantiate mandatory `00–05` and `09–17`, evaluate conditional `06–08`, keep `18–19` reserved, and create `20–99` only when applicable.
11. Pin imported Framework/Schema locally after bootstrap. Existing Projects never auto-upgrade; an explicitly requested upgrade uses `MIG-*`.
12. If exact Git provenance is observed and material, record it consistently in `00` and `14`; otherwise preserve an explicit unknown/unverified state if needed and never invent a value.
13. Before readiness or `CURRENT` export claims, verify every referenced current Stable ID resolves within the Current Reconstructable Snapshot without archive traversal.
14. Never store actual secrets; use `SECRET-*` metadata references only.
15. Preserve history on substantive updates and finish with human + machine completion summary, readiness, and exact next action.

## Quick Reference

| Situation | Required behavior |
|---|---|
| ChatGPT Project bootstrap | Use `CHATGPT-PROJECT-INSTRUCTIONS.md`; NEW project bootstraps from canonical `main`, initialized project uses local pin |
| Claude Project bootstrap | Use `CLAUDE-PROJECT-INSTRUCTIONS.md`; NEW project bootstraps from canonical `main`, initialized project uses local pin |
| New project | Preview → approval → Framework first → mandatory descendants; conditional only when applicable |
| Exact Git provenance unavailable | Continue normal bootstrap if canonical source is accessible; do not fabricate tag/SHA; record unknown/unverified only when material |
| Existing project | Preserve-first discovery; local pinned Project Source is authoritative |
| Framework upgrade | Never automatic; assess/execute through `MIG-*` with approval |
| Integrity requirement | Treat as governance semantics; do not build validator/CI/CLI unless explicitly requested separately |
| Import | Quarantine/stage before promotion |
| Missing fact/source | `UNKNOWN` / `ASSUMED` / `STALE` / `VERIFICATION_REQUIRED`; never fabricate |
| Truth mismatch | `DRIFT-*` |
| Semantic concurrent edit | `CONFLICT-*`; no last-write-wins |
| Current Stable-ID resolution | Resolve inside current snapshot; archive must not be required |
| Handoff | Authority does not transfer |
| R2/R3 mutation | Fresh authority + required postflight/evidence |

## Red Flags

- Removing/bypassing/demoting/weakening `FRAMEWORK-001`
- Creating governed descendants without Framework inheritance
- Treating Git tag/SHA or branch protection as a prerequisite for normal Framework usability without an explicit stricter Project-Specific Rule
- Claiming exact provenance that was not actually observed
- Turning an Integrity Contract into Python/CLI/CI/automation/enforcement software without an explicit separate implementation request
- Platform instruction drift: ChatGPT/Claude shared contracts differ, one platform auto-upgrades, or platform instructions are treated as authority over an active local Framework
- Reconstructing Framework rules, semantic slots, authority, or project facts from memory when required canonical source is inaccessible
- Mockup/namespace drift: guessing semantic slots, pre-creating empty conditional documents, materializing reserved slots, or following a stale mockup over Core Governance
- Archive-dependent Current Truth: a current Stable ID requires archived revision content to determine current semantics
- Writing before the initial approval gate
- Treating newest file, role, handoff, or memory as authority/truth by default
- Guessing missing facts or copying secrets
- Claiming completion without risk-appropriate verification
