# TASK-023 Self-Bootstrapping Project Contract — Design

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-023`
Design state: `USER_APPROVED_DESIGN / SPEC_APPROVED`
Approval basis: user approved the TASK-023 architecture and explicitly authorized continuous development through Framework `1.7.0` completion on `2026-08-29`, without additional approval prompts unless a governance fail-closed condition is encountered.

## 1. Problem

ProjectFramework bootstrap relies too heavily on vendor/product-specific Project Settings or launcher surfaces. An Agent that can access a Project repository/root but lacks those settings may miss the locally pinned Project Source before doing work.

Framework `1.7.0` must make the Project itself sufficient for bootstrap discovery once an Agent can access the Project root, without claiming discovery when filesystem/repository access is absent and without creating a second governance root.

Existing invariants remain binding: active local `Project-Source/00` / `FRAMEWORK-001` is authoritative; discovery is distinct from bindings/branch/integration/implementation/runtime/Authority; initialized Projects never auto-upgrade; portable bootstrap artifacts contain no secrets or mutable runtime state; vendor launchers never outrank Root Governance.

## 2. Chosen architecture: root-native thin bootstrap

Framework `1.7.0` standardizes one stable Project-root discovery file:

```text
<Project-Root>/PROJECT-BOOTSTRAP.md
```

`PROJECT-BOOTSTRAP.md` is a **discovery/locator contract only**. It is outside the `00–99` Project Source semantic-slot namespace, has no Stable ID, owns no current Project truth, and never supersedes or competes with `FRAMEWORK-001`.

Canonical route:

```text
PROJECT-BOOTSTRAP.md
→ Project-Source/00 / FRAMEWORK-001
→ Project-Source/01 / Project Source Index
→ Project-Source/03 / Current State
→ task-specific routing
→ Project-Source/09 / Handoff when continuation applies
```

## 3. Bootstrap file contract

The deployed filename is always `PROJECT-BOOTSTRAP.md`; revision/date suffixes are forbidden. The maintained distribution template is `managing-project-source/templates/PROJECT-BOOTSTRAP.md`.

The file contains only bounded discovery semantics: Project Source relative root; first-read route; continuation routing; `FRAMEWORK-001` precedence; fail-closed behavior for missing/contradictory targets; no-secrets rule; and optional vendor-adapter guidance.

It MUST NOT own `REQ-*`, `DEC-*`, `AUTH-*`, `RISK-*`, `REL-*`, Project Location Binding, branch/worktree, Integration Target, Implementation Source, Runtime authority, credentials, or a second copy of current Project state.

## 4. Discovery algorithm

1. From an accessible Project root, look for `PROJECT-BOOTSTRAP.md`.
2. Read it as a locator only.
3. Resolve the declared Project Source root and read `00`.
4. Validate active `FRAMEWORK-001` before treating it as authority.
5. Read `01` for canonical routing.
6. Read `03` for current state.
7. For continuation, resolve `09 Handoff` through current routing.
8. Continue task-specific reads from authoritative sources.

A known Brownfield/pre-1.7 Project without the file may use legacy/vendor discovery only to locate its active Project Source; the Agent must not silently create the file or infer an upgrade. A Project claiming `1.7.0+` adoption with a missing/contradictory required bootstrap fails closed for Material mutation until governed repair/upgrade resolves it.

## 5. Authority and location separation

Precedence is explicit:

```text
PROJECT-BOOTSTRAP.md = discovery/locator
FRAMEWORK-001        = Project governance authority
01                   = current routing/index
03                   = current-state summary
09                   = continuation/handoff
vendor adapters      = optional discovery convenience
```

A bootstrap locator never wins a conflict against valid active `FRAMEWORK-001`. Correct discovery location never grants Authority, Risk approval, implementation, push, runtime, binding, or deployment permission.

## 6. Bootstrap Location and `PROJECT-CONFIG.md`

Framework `1.2.6` Bootstrap Location semantics remain distinct. `templates/project-location-bootstrap.md` continues to define pre-authority environment/location locators; `PROJECT-BOOTSTRAP.md` defines how to enter this Project's canonical Project Source from the root.

Optional `PROJECT-CONFIG.md` remains a legacy/optional location-reference representation only. It is not promoted to canonical discovery and is not auto-deleted. If both exist, `PROJECT-BOOTSTRAP.md` owns root discovery, `PROJECT-CONFIG.md` may supply optional location values, and active `FRAMEWORK-001` remains authority. Contradictions are surfaced, never resolved by recency.

## 7. GREENFIELD behavior

For NEW Projects created under Framework `1.7.0+`, `PROJECT-BOOTSTRAP.md` is mandatory. Governed creation remains Preview → required approval → create active `00 / FRAMEWORK-001` → create approved starter set → materialize root bootstrap from the maintained template → verify that it resolves the created active Project Source.

The file is mandatory in the resulting NEW Project but never replaces `00` as the governance root.

## 8. Brownfield adoption

Existing initialized Projects do not receive the file automatically. `1.6.0 → 1.7.0` adoption uses `[Project Upgrade]` and Direct-to-Latest cumulative target-state rules: fresh-resolve current/target, classify, Preview root-bootstrap creation, preserve local rules/bindings/Stable IDs/history/optional `PROJECT-CONFIG.md`, obtain existing upgrade mutation authority, create the root bootstrap, verify it resolves active `FRAMEWORK-001`, and record material `MIG-*`/evidence/change history.

## 9. Vendor adapters

ChatGPT Project Settings, Claude Project Settings, `AGENTS.md`, `CLAUDE.md`, and similar surfaces become optional thin discovery adapters. They help an Agent reach the root bootstrap/canonical sources but are not required for reconstructing governance once the Project root is accessible.

Official launchers retain byte-identical shared marker bodies, `<=4,500` Unicode-character limits, canonical command/lifecycle/close tokens, no Project-specific paths/secrets in the shared body, and subordination to active `FRAMEWORK-001`. Framework `1.7.0` wording prefers `PROJECT-BOOTSTRAP.md` when present while preserving legacy/pre-1.7 discovery compatibility.

## 10. Project Source routing surfaces

`00` gains a bounded rule that the root bootstrap is a non-authoritative locator. `01` remains the authoritative routing index after `00`. `03` retains current-state ownership. `09` retains Resume/Handoff content and is only referenced by the root bootstrap. `14` may describe the required external bootstrap artifact for `1.7.0+` GREENFIELD Projects but must not assign it a fake semantic slot or Stable ID.

## 11. Failure handling

Affected Material mutation fails closed when the root bootstrap points to a missing Project Source, referenced `00` is not valid active `FRAMEWORK-001`, multiple canonical bootstrap locations are claimed, routing materially contradicts active root binding, a `1.7.0+` Project expected to carry the mandatory file lacks it without a governed exception, or a vendor adapter/optional `PROJECT-CONFIG.md` materially conflicts with the resolved active Project Source.

Read-only discovery may continue far enough to diagnose. Recency, search ranking, active workspace IDs, cached paths, or similar-name heuristics never resolve the ambiguity.

## 12. Distribution surfaces

Implementation affects `FRAMEWORK-RELEASE.yaml`; new `references/framework-governance-amendment-260829-task023.md`; Core Governance; `SKILL.md`; `README.md`; `MIGRATION-NOTES.md`; new `templates/PROJECT-BOOTSTRAP.md`; `templates/project-location-bootstrap.md`; root `00` template; core skeletons; mockup README and affected routing/manifest starters; current starter release stamps; both platform launchers; pressure scenarios; Task registry; and release evidence. Historical amendments remain immutable.

## 13. Release classification

TASK-023 is a backward-compatible Framework minor semantic expansion:

```text
Framework 1.7.0
Schema 1.0.0
release format 3
```

It adds a mandatory external bootstrap artifact for NEW Projects plus governed Brownfield adoption, without changing Project Source metadata schema, slot identity, Stable-ID grammar, or initialized-Project pinning. A genuine incompatible schema/authority break must stop and reclassify rather than silently force `1.7.0`.

## 14. Verification strategy

Affected verification must prove: current release identity `1.7.0 / 1.0.0 / 3`; descriptor root-bootstrap entrypoint; stable template/deployed filename; exact `PROJECT-BOOTSTRAP.md → 00 → 01 → 03` route plus `09` continuation; non-authoritative bootstrap and `FRAMEWORK-001` precedence; discovery/location/binding/branch/integration/implementation/runtime/Authority separation; mandatory GREENFIELD file; `[Project Upgrade]`-only Brownfield adoption; optional-only `PROJECT-CONFIG.md`; fail-closed contradictions; no secret/volatile authority in bootstrap; aligned `00`/skeleton/mockup routing/manifest; current starter version stamps; launcher root-bootstrap preference, parity, size and token invariants; unique pressure scenarios covering the new contract; historical TASK-022 amendment blob unchanged; Markdown/YAML-only implementation; `git diff --check`; and one final `RELEASE_FULL` on the unchanged `1.7.0` candidate.

## 15. Non-goals

No filesystem watcher/daemon, automatic discovery service, MCP runtime/tool routing, code-generation engine, vendor plugin runtime, automatic Brownfield upgrade, secret store, automatic path/binding repair, CI/CD/deployment automation, or TASK-024+ implementation is authorized.

## 16. Acceptance criteria

Framework `1.7.0` is acceptable when an Agent with Project-root access can find one stable root bootstrap; NEW 1.7+ Projects include it; it routes to `00 → 01 → 03` and `09` when applicable; `FRAMEWORK-001` remains authority; Brownfield Projects do not auto-upgrade; vendor settings are optional adapters; `PROJECT-CONFIG.md` stays optional location reference; contradictions fail closed without guessing; launchers retain size/parity/token invariants; and current Project truth remains reconstructable from Project Source without vendor-specific settings.
