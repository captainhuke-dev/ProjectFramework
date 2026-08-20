---
name: managing-project-source
description: Use when creating, adopting, importing, updating, reviewing, handing off, or exporting a Project Source; when a project needs consistent governance, naming, source-of-truth handling, continuation context, or cross-agent documentation.
---

# Managing Project Source

## Overview

Maintain a consistent `Project-Source/` governance layer. Make **current truth, current authority, and exact next action** explicit without inventing facts.

**Do not expand into validator/CLI/automation unless the user explicitly asks.**

## Required References

Before creating or materially changing Project Source, read:

- `FRAMEWORK-RELEASE.yaml` for the current distribution release descriptor and stable bootstrap ref
- `references/framework-governance-amendment-260820-0821.md`
- `references/framework-governance-amendment-260820-0735.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0707.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0646.md` (historical approved amendment)
- `references/framework-governance-amendment-260814-0808.md` (historical approved amendment)
- `references/core-governance-rules.md`
- `templates/00-project-source-framework.md`
- `templates/core-document-skeletons.md` for new Project Source
- `templates/project-source-mockup/README.md` to resolve semantic-slot/document mapping and starter filenames

Use the historical design spec only for rationale/edge cases; the latest Framework amendment wins on conflicts.

## Platform Project Bootstrap Entrypoints

The distribution provides two official platform launcher artifacts:

- `CHATGPT-PROJECT-INSTRUCTIONS.md` — paste into ChatGPT Project settings → Instructions.
- `CLAUDE-PROJECT-INSTRUCTIONS.md` — paste into Claude Project → Set project instructions.

Both files MUST contain the same byte-identical shared governance contract between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END`. Platform-specific wrapper text may identify the placement surface, but bootstrap semantics, local authority, migration behavior, provenance behavior, and scope boundaries must not diverge.

These platform instructions are **bootstrap/continuation launchers only**. If a valid local Project Source with active `FRAMEWORK-001` already exists, the locally pinned Project Source is authoritative. Platform instructions MUST NOT replace, weaken, bypass, or override the active local Framework.

For a NEW Project, platform instructions use `main` only as the discovery entrypoint, then read `FRAMEWORK-RELEASE.yaml`, resolve its declared `stable_release_tag`, and normally bootstrap from that immutable tagged source. Upstream is not a live auto-update source after initialization.

## Release Provenance Invariant

`FRAMEWORK-RELEASE.yaml` is Framework distribution metadata, not a Project Source semantic slot and not Root Governance. It declares the expected stable release ref for reproducible bootstrap.

For NEW Project bootstrap:

```text
read main discovery entrypoint
→ read FRAMEWORK-RELEASE.yaml
→ resolve stable_release_tag
→ read bootstrap source at that tag
→ Preview → explicit user approval → write
→ record framework_source_provenance locally
```

The Project-local provenance record contains the release tag and **actually resolved** commit SHA. Never predict or fabricate the containing release SHA. Never treat mutable `main` as equivalent to an immutable tag.

If immutable release resolution is unavailable, state the limitation and stop the affected governance mutation. Mutable-`main` bootstrap may proceed only with explicit user approval and must preserve degraded provenance such as `VERIFICATION_REQUIRED` / mutable-source warning. Existing Projects MUST NOT retroactively backfill an unobserved historical SHA merely to look complete.

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

The observed ambiguity applies directly to `DEC-*` in `04-Decision Log` and `REQ-*` in `05-Requirements`, and the invariant applies generally to current-state-bearing canonical object homes.

## Workflow

1. Classify `GREENFIELD`, `BROWNFIELD`, or `IMPORT`. For a platform Project, first use the matching canonical platform instruction artifact to determine whether a valid local Project Source already exists.
2. For `GREENFIELD`, read the canonical repository discovery entrypoint and `FRAMEWORK-RELEASE.yaml`; resolve `stable_release_tag` and normally continue from the immutable tagged source. If immutable source resolution fails, disclose the limitation and stop unless the user explicitly approves degraded mutable-source bootstrap.
3. Resolve explicit `FAST`/`GRILL`; otherwise use `ADAPTIVE`.
4. Confirm active `FRAMEWORK-001`; if missing in an existing Project Source, stop affected work and propose governed repair.
5. Existing Project: bootstrap `00 → 01 → 03`, then follow `01` routing. Do not silently replace the local pin with upstream `main` or a newer tag.
6. Inspect accessible project sources before asking; do not ask for facts you can verify.
7. Classify important claims by Truth Domain, Epistemic Status, and Freshness. Use `DRIFT-*` / `CONFLICT-*`; never silently reconcile.
8. Initial creation or major structural migration requires Preview → explicit user approval → write.
9. Follow Core Governance for naming, revisions, archive, canonical object homes, authority, handoff, evidence, and exports.
10. For new-project bootstrap, map semantic slots from `templates/project-source-mockup/README.md`: instantiate mandatory `00–05` and `09–17`, evaluate conditional `06–08`, keep `18–19` reserved, and create `20–99` only when applicable.
11. Record the actually resolved release ref and commit SHA in active `00` `framework_source_provenance` and matching `14-Manifest` continuation metadata; never fabricate missing provenance.
12. Pin the imported Framework/Schema locally after bootstrap. Existing Projects never auto-upgrade; an explicitly requested upgrade uses `MIG-*`.
13. Before readiness or `CURRENT` export claims, verify every referenced current Stable ID resolves within the Current Reconstructable Snapshot without archive traversal.
14. Never store actual secrets; use `SECRET-*` metadata references only.
15. Preserve history on substantive updates and finish with human + machine completion summary, readiness, and exact next action.

## Quick Reference

| Situation | Required behavior |
|---|---|
| ChatGPT Project bootstrap | Use `CHATGPT-PROJECT-INSTRUCTIONS.md`; NEW project resolves release descriptor/tag, initialized project uses local pin |
| Claude Project bootstrap | Use `CLAUDE-PROJECT-INSTRUCTIONS.md`; NEW project resolves release descriptor/tag, initialized project uses local pin |
| New project | Resolve immutable release → Preview → approval → Framework first → mandatory descendants; conditional only when applicable → record observed provenance |
| Stable tag inaccessible | Stop/disclose; mutable `main` requires explicit approval + degraded provenance / `VERIFICATION_REQUIRED` |
| Existing project | Preserve-first discovery; local pinned Project Source is authoritative; never fabricate historical SHA provenance |
| Framework upgrade | Never automatic; assess/execute through `MIG-*` with approval |
| Import | Quarantine/stage before promotion |
| Missing fact/source | `UNKNOWN` / `ASSUMED` / `STALE` or explicit access limitation; never fabricate |
| Truth mismatch | `DRIFT-*` |
| Semantic concurrent edit | `CONFLICT-*`; no last-write-wins |
| Current Stable-ID resolution | Resolve inside current snapshot; archive must not be required |
| Handoff | Authority does not transfer |
| R2/R3 mutation | Fresh authority + required postflight/evidence |

## Red Flags

- Removing/bypassing/demoting/weakening `FRAMEWORK-001`
- Creating governed descendants without Framework inheritance
- Claiming immutable Framework provenance without resolving the actual tag/SHA
- Treating mutable `main` as an immutable release identity or backfilling an unobserved SHA into an older Project
- Platform instruction drift: ChatGPT/Claude shared contracts differ, one platform auto-upgrades, or platform instructions are treated as authority over an active local Framework
- Reconstructing Framework rules, semantic slots, authority, or project facts from memory when required upstream/local source is inaccessible
- Mockup/namespace drift: guessing semantic slots, pre-creating empty conditional documents, materializing reserved slots, or following a stale mockup over Core Governance
- Archive-dependent Current Truth: a current Stable ID requires archived revision content to determine current semantics
- Turning documentation scope into software engineering without explicit request
- Writing before the initial approval gate
- Treating newest file, role, handoff, or memory as authority/truth by default
- Guessing missing facts or copying secrets
- Claiming completion without risk-appropriate verification
