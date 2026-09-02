# Core Governance Rules — Project Source

This reference is the operational contract used by the `managing-project-source` skill. Human-readable content is Thai-first; canonical machine vocabulary remains English.

## 1. Binding Governance

`00-Project Source Framework` is the non-removable root governance document. It contains:

1. **Framework Core** — root invariants shared across projects.
2. **Project-Specific Rules** — descendant constraints that inherit from the Framework and may only specialize it without weakening it.

Root inheritance and authority:

```text
0. User Explicit Instruction / Approval (external authority to revise governance)
1. 00-Project Source Framework (FRAMEWORK-001; root inside Project Source)
2. Framework-compliant Project-Specific Rules
3. Canonical Project Source documents / Decisions / Requirements
4. Task / Handoff / Prompt / Agent Instruction
```

`FRAMEWORK-001` MUST exist in every Project, MUST remain in semantic slot `00`, and MUST NOT be removed, bypassed, demoted, or replaced by descendant governance. All Project artifacts created after it are governed by and inherit from the Framework. Project Source artifacts inherit directly; implementation/external mutations inherit governance through Project identity, Requirements, Decisions, Actions, Authority, and Framework workflows. Descendants may extend/specialize/add constraints, but cannot weaken or contradict Framework invariants.

Governed Markdown descendants declare `inherits_from: ["FRAMEWORK-001"]`; non-Markdown artifacts inherit through their canonical Registry/Manifest metadata. Missing active Framework makes Project Source `INVALID + NOT_OPERATIONALLY_READY`.

Legacy rename migration: if a Brownfield Project still has `00-Project Source Rule`, treat it as the legacy predecessor of slot `00`. Do not delete it in place. Create a Framework candidate, promote it through governed revision/migration, then archive the predecessor only after active `FRAMEWORK-001` is established.

Agents may propose Framework changes but must not modify `00-Project Source Framework` without explicit user approval. Framework revision preserves stable identity `FRAMEWORK-001`, supersedes/archive the old revision, and never deletes the root. Each Project pins its approved Framework version; upgrades require governed migration.

## 2. Standard Location and Semantic Namespace

All Projects use:

```text
<Project-Root>/Project-Source/
```

Core namespace:

```text
00 Project Source Framework     MANDATORY / NON-REMOVABLE ROOT
01 Project Source Index         MANDATORY
02 Project Overview             MANDATORY
03 Current State                MANDATORY
04 Decision Log                 MANDATORY
05 Requirements                 MANDATORY
06 Architecture                 CONDITIONAL
07 Implementation Plan          CONDITIONAL
08 Open Issues                  CONDITIONAL
09 Handoff                      MANDATORY
10 Change Log                   MANDATORY
11 Actor Registry               MANDATORY
12 Authorization Registry       MANDATORY
13 Evidence Registry            MANDATORY
14 Project Source Manifest      MANDATORY
15 Action Registry              MANDATORY
16 Migration Registry           MANDATORY
17 Secret Reference Registry    MANDATORY
18–19                           RESERVED
```

Conditional files are created only when applicable; do not create empty files merely to look complete.

Extended taxonomy:

```text
20–29 Research / Discovery
30–39 Business / Process / UX Design
40–49 Architecture / Technical / Integration
50–59 Testing / QA / Validation
60–69 Deployment / Operations / Infrastructure
70–79 Data / Migration / Analytics
80–89 Audit / Review / Assessment / Reports
90–99 Project-specific / Governance Extension
```

Framework `1.2.0` standardizes these extended anchors:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension unless governed otherwise later
```

Framework `1.6.0` further standardizes:

```text
92 Project Graph                  CONDITIONAL / STANDARD IN 1.6.0+
93–99 Project-specific / Governance Extension unless governed otherwise later
```

`40`, `60`, `91`, and `92` do not join the mandatory `00–17` bootstrap set. They are materialized only when applicable. The Framework `1.2.0` statement above is historical for that release; current generic extension space is `93–99`.

Framework distribution artifacts exist outside the Project Source semantic namespace:

```text
Framework-Source/FRAMEWORK-RELEASE.yaml
Framework-Source/templates/PROJECT-BOOTSTRAP.md
Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md
Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
```

`FRAMEWORK-RELEASE.yaml` is distribution metadata, not Root Governance or a semantic slot. Platform instruction files are bootstrap/continuation launchers. Their shared governance contract MUST remain byte-identical and MUST NOT replace, weaken, bypass, or override active local `FRAMEWORK-001`.

### 2.1 Concept-First Framework Boundary

ProjectFramework is a **conceptual Project governance and planning framework first**. It defines governance semantics, namespace, technical/installation blueprints, management controls, integrity expectations, bootstrap, authority, migration, handoff, readiness, pressure scenarios, and maintained starter representations.

A technical or integrity requirement does not implicitly authorize executable implementation. Unless the user explicitly requests a separate implementation scope, do not create application code, Dockerfile, Compose/Kubernetes/Helm runtime artifacts, installer scripts, validator, CLI, CI/CD, migration engine, scheduler, background automation, dashboard, or runtime enforcement merely because a rule can be checked or implemented mechanically.

A real Project's current Project Source may document concrete verified commands, paths, ports, configuration keys, or operating procedures when those are actual Project truth. ProjectFramework itself does not invent executable commands for nonexistent software.

### 2.1.1 Framework 1.7 Project Root Bootstrap Semantics

Framework `1.7.0` standardizes `<Project-Root>/PROJECT-BOOTSTRAP.md` as the stable vendor-neutral discovery entrypoint for NEW Projects created under `1.7.0+`. The maintained distribution template is `templates/PROJECT-BOOTSTRAP.md`.

`PROJECT-BOOTSTRAP.md` is a discovery/locator artifact outside the `00–99` semantic-slot namespace. It has no Stable ID, owns no Project truth, and never replaces or outranks active `Project-Source/00` / `FRAMEWORK-001`.

Once Project-root access exists, the canonical route is:

```text
PROJECT-BOOTSTRAP.md
→ 00 / FRAMEWORK-001
→ 01 / Project Source Index
→ 03 / Current State
→ task-specific routing
→ 09 / Handoff when continuation applies
```

Validate the referenced `00` as active `FRAMEWORK-001` before treating it as authority. `01`, `03`, and `09` retain their existing canonical homes; the root bootstrap never duplicates their current payloads.

Keep bootstrap discovery separate from Project Location Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime Location, Authority, and Risk. Correct discovery location grants none of those permissions or authorities.

For GREENFIELD `1.7.0+`, the resulting approved Project MUST contain the root bootstrap. Existing initialized Projects MUST NOT receive it automatically; adoption is through governed `[Project Upgrade]` or another explicitly authorized root migration/repair flow. A pre-1.7 Project without the file is not invalid merely because upstream has advanced.

`PROJECT-CONFIG.md`, when present, remains an optional Bootstrap Location reference only. ChatGPT/Claude Project Settings, `AGENTS.md`, `CLAUDE.md`, and similar vendor surfaces are optional thin discovery adapters after Project-root access exists.

A missing target, invalid referenced `FRAMEWORK-001`, multiple canonical root bootstrap claims, or material contradiction with active Root/Location Binding fails closed for affected Material mutation. Read-only discovery may continue far enough to diagnose, but recency, ranking, cached paths, workspace IDs, or similar-name heuristics never resolve the ambiguity. The Framework does not claim root discovery when the Agent has no filesystem/repository access.


### 2.2 Bootstrap Location Semantics

Framework `1.2.6` defines a Project-specific **Bootstrap Location Block** as pre-`FRAMEWORK-001` discovery/execution routing input, not a second Root Governance object. When a valid local active `FRAMEWORK-001` is already available, resolve it first and use its governed Project Location state.

Keep the six bootstrap/execution concepts distinct:

```text
Framework Source
≠ Remote Location
≠ File Storage Location
≠ MCP Location
≠ Local Workspace
≠ current branch/worktree
≠ Repository / Project Location Binding authority
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
```

Resolution order when authority is not already resolved:

```text
read Project-specific Bootstrap Location Block when present
→ Framework Source for Framework bootstrap/read-through only
→ declared Local Workspace for read-only local active-FRAMEWORK-001 resolution
→ Remote Location for deterministic remote Project Source discovery when needed
→ MCP Location for applicable execution-boundary verification
→ File Storage Location(s) for their declared non-repository artifact scopes
→ fresh-observe current branch/worktree from Git whenever Material Git state matters
→ once active FRAMEWORK-001 resolves, use its governed Project Location Binding
→ apply independent Scope / AUTH / Risk / REQ / DEC / integration / implementation / runtime gates
```

`Framework Source` is Framework upstream/read-through only and never auto-upgrades an initialized Project. `Remote Location` is a discovery starting point, not Repository Location Binding or branch authority. Explicit discovery indirection may legitimately differ from the final governed repository; a direct identity contradiction that would route Material work elsewhere is a material mismatch.

`MCP Location` and `Local Workspace` are environment-scoped locators with different roles. MCP workspace IDs, editor handles, recent/active workspace lists, drive letters, mounts, and comparable runtime identifiers are evidence only. Host/container paths may differ when an explicit mapping plus repository/source identity proves the same governed Project.

`current branch/worktree` is volatile observed Git state. Bootstrap configuration may persist only dynamic intent such as `DYNAMIC / VERIFY_EACH_SESSION`, never a concrete branch as authority. When Material, freshly resolve repository identity, worktree path, branch/ref, HEAD, working-tree status, and applicable tracking state.

A bootstrap/root mismatch that would route Material work to an incompatible Project target fails closed for the affected mutation and is disclosed. Neither side is silently rewritten. Persistent location changes require explicit approval plus coordinated governed propagation. A one-off exact target remains action-specific. **Correct location does not grant Authority or reduce Risk.**


### 2.3 Project Location Binding

For an initialized Project, active local `00-Project Source Framework` / `FRAMEWORK-001` is the canonical home of **Project Location Binding**: the durable routing boundary that answers which GitHub repository, Google Drive project container, and environment-scoped **Local Workspace Binding** belongs to the Project for connector/local execution work. `03 Current State`, `09 Handoff`, `40 Technical Design`, plans, or MCP configuration MAY reference the active binding but MUST NOT maintain an independent authoritative copy.

Project Location Binding is distinct from implementation and Git integration authority:

```text
Repository Location Binding
  ≠ Local Workspace Binding
  ≠ current work branch/worktree
  ≠ Canonical Integration Target
  ≠ Canonical Implementation Source
  ≠ Runtime Location
```

Location Binding MUST NOT add `canonical_branch` or any equivalent parallel branch authority. Framework `1.2.2` Canonical Integration Target/Base Freshness semantics and Framework `1.2.3` Canonical Implementation Source/Runtime Authority semantics remain independently binding.

GitHub, Google Drive, and each applicable environment-scoped Local Workspace Binding are classified independently using exactly:

```text
BOUND
NOT_APPLICABLE
VERIFICATION_REQUIRED
```

`BOUND` requires sufficient durable routing identity for Material work:

```text
GitHub          → repository owner/name OR canonical repository URL
Google Drive    → project-root folder ID OR canonical folder URL
Local Workspace → verified/user-confirmed absolute canonical path for that environment; when Git-backed, repository identity SHOULD be cross-checked when practical
```

A display name, textual Drive path, chat memory, recent connector activity, search ranking, or discovery result alone is insufficient to establish `BOUND`. A Drive display path is descriptive only when a stable folder/file ID or canonical URL is available.

`VERIFICATION_REQUIRED` is **fail-closed for Material mutation**. Read/search/discovery, candidate comparison, and user confirmation needed to resolve the location MAY proceed, but Material mutation through the unresolved system is blocked by default. A User Explicit Instruction naming one exact target MAY authorize that one action when otherwise permitted; it does not persistently change the binding or promote it to `BOUND`.

`NOT_APPLICABLE` means the connector/system is outside the declared Project working-location contract. Material Project work through it is blocked by default until a governed binding/scope revision is explicitly approved.

When `BOUND`, the intended Material target MUST match the durable routing identity when comparison is possible. A material mismatch stops the affected mutation and is disclosed; use existing `DRIFT-*` semantics when Truth Domains that are expected to align materially disagree. Location Binding answers **where** Project work belongs; existing `AUTH-* / DEL-*`, approval, and Risk rules still answer **who may mutate what**.

Because Project Location Binding is part of `FRAMEWORK-001`, a persistent binding change is a **Root Governance mutation**. It requires User Explicit Approval plus the existing revision → validate → promote → supersede/archive flow. Connector discovery, recent activity, search ranking, or access to another Project location MUST NOT transfer authority or silently rewrite the binding.

For Material GitHub/Drive work in an initialized Project, operational preflight is:

```text
resolve active local FRAMEWORK-001
→ read applicable Project Location Binding state
→ if BOUND, compare intended target to durable routing identity when possible
→ if VERIFICATION_REQUIRED, discovery/read-only only by default; block Material mutation
→ if NOT_APPLICABLE, block Material Project work through that connector
→ preserve independent Authority/Risk gates
→ persist Material result to its source-native owner at a Logical Checkpoint
```

Project-specific repository, Drive-root, and designated-progress pointers belong in the local root binding, not platform launchers. Cross-system work continues to use source-native owners plus pointers rather than duplicated canonical content.


### 2.4 Governed File Storage Binding

Framework `1.2.6` extends Project Location Binding with purpose/content-scoped **File Storage Binding** for non-Google-Drive external Project files/objects. Generic governed storage may cover `S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER`.

File Storage Binding reuses exactly:

```text
binding_state: BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED
verification_status: VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED
```

`BOUND` requires sufficient provider-appropriate durable identity and MUST pair only with `VERIFIED` or `USER_CONFIRMED`, never `verification_status: VERIFICATION_REQUIRED`. Examples include S3 bucket+prefix/canonical URI, NAS/SMB server+share+governed path, NFS server+export+path, SharePoint stable site/library/folder identity, or comparable durable provider identity.

Known-applicable but unresolved storage is `VERIFICATION_REQUIRED`: read/search/discovery and user confirmation needed to resolve it may proceed, but Material mutation is blocked by default. A Project with no external/non-repository storage may omit generic storage entries; do not synthesize provider `NOT_APPLICABLE` entries merely to populate a template. Missing, empty, or unresolved storage never authorizes fallback to a recent/search-ranked/similarly named bucket, folder, share, mount, sync folder, cache, mirror, or backup.

Multiple storage bindings are valid for distinct governed content scopes. One governed content scope has one declared authoritative owner at a time. Backup/mirror/replica existence or content similarity never transfers current authority.

Framework `1.2.6` keeps the dedicated `project_location_binding.google_drive` block as the canonical Root Governance representation for Google Drive Project-root/content routing. A bootstrap `GOOGLE_DRIVE` File Storage Location maps to that dedicated Drive binding. Generic File Storage MUST NOT duplicate the same Drive target/content scope. Future Drive normalization, if ever approved, requires governed migration and history preservation.

Mounted, synced, or cached storage paths are routing/mapping evidence only. File Storage Binding does not automatically become Local Workspace, Canonical Implementation Source, Runtime/Data/Persistent-State authority, backup authority, or deployment authority. A physical target may hold multiple separately governed roles without collapsing their authority domains.

Actual storage credentials MUST NOT be stored in Bootstrap Location or Project Location metadata. Access keys, passwords, tokens, secret-bearing signed URLs, and comparable secrets remain external; use existing `SECRET-*` reference metadata when credential routing is needed.

File Storage preflight is:

```text
resolve active FRAMEWORK-001 after bootstrap discovery
→ resolve declared content scope and applicable storage owner
→ BOUND: compare intended target to durable provider identity when possible
→ VERIFICATION_REQUIRED: discovery/read-only only by default; block Material mutation
→ NOT_APPLICABLE: block Material work for that declared scope
→ absence: never infer/fallback; establish applicability/identity through governed flow when required
→ preserve independent Authority/Risk/implementation/runtime/persistence gates
```


### 2.5 Environment-Scoped Local Workspace Binding

**Local Workspace Binding** answers where a local execution surface (GPT-Web/MCP, Codex/local shell, another MCP, IDE/terminal, or equivalent) may perform Material Project work for a declared execution environment. It reuses `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED` and creates no MCP-specific state family.

A Project MAY have different local workspace paths across workstations, VMs, WSL distributions, Dev Containers, remote durable workspaces, or other environments. One global absolute path is not required. For `BOUND`, the applicable environment entry has a verified/user-confirmed absolute path; Git-backed work SHOULD cross-check repository owner/name or canonical URL when practical so a same-named wrong clone does not silently satisfy routing. If local execution is applicable but no verified entry can be resolved, the effective local binding is `VERIFICATION_REQUIRED`.

MCP `workspaceId`, editor handles, active/recent workspaces, search ranking, and similar tool/runtime identifiers are **routing evidence only**. They are not canonical Project identity and MUST NOT silently rewrite Project Location Binding. A one-off User Explicit Instruction naming an exact local target applies only to that otherwise-authorized action and does not persistently rewrite the binding. Persistent Local Workspace Binding change is a Root Governance mutation requiring User Explicit Approval and the normal `FRAMEWORK-001` revision/validate/promote/supersede/archive flow.

Before Material local/MCP mutation, preflight resolves the applicable environment-scoped Local Workspace Binding, compares the actual execution path and—when Git-backed/material—repository identity when practical, then preserves independent Authority/Risk, Canonical Integration Target, Canonical Implementation Source, and Runtime Truth gates.

### 2.6 Framework 1.2.6 Bootstrap Location Semantics and File Storage Binding

A Project-specific **Bootstrap Location Block** is a pre-`FRAMEWORK-001` discovery/execution preamble, not a semantic slot, Root Governance object, or competing steady-state Project authority. It keeps six bootstrap/execution concepts distinct:

```text
Framework Source
Remote Location
File Storage Location
MCP Location
Local Workspace
current branch/worktree
```

Required semantics:

- **Framework Source** → Framework upstream/read-through only. It never auto-upgrades an initialized Project or becomes consuming-Project authority merely because the values match.
- **Remote Location** → deterministic remote Project Source discovery start before active authority resolves. It defines no branch authority and is not Repository Location Binding, Canonical Integration Target, or Canonical Implementation Source. Explicit discovery/index indirection may differ from the final governed repository without automatic DRIFT when the relationship is intentional and verified.
- **File Storage Location** → zero-or-more bootstrap locators for durable Project-managed external file/object scopes. It is not itself File Storage Binding.
- **MCP Location** → environment-specific execution-adapter routing. MCP workspace IDs, recent/focused workspace lists, and similar runtime handles are evidence only.
- **Local Workspace** → environment-local Project-root/bootstrap locator. It remains distinct from governed Local Workspace Binding; explicit verified host/container/mount mappings may legitimately use different path syntax.
- **current branch/worktree** → volatile Git observation. Persist only dynamic intent such as `DYNAMIC / VERIFY_EACH_SESSION`; fresh-observe branch/ref, HEAD, worktree, status, and upstream/tracking state whenever material.

Resolution order is:

```text
read Project-specific Bootstrap Location Block when present
→ inspect declared Local Workspace read-only for valid active FRAMEWORK-001
→ valid active local FRAMEWORK-001 wins; read 00 → 01 → 03
→ otherwise use Framework Source only for Framework read-through and Remote Location for deterministic Project discovery
→ use MCP / Local / File Storage locators only for their declared roles
→ once active FRAMEWORK-001 resolves, its Project Location Binding governs repository, local-workspace, Drive, and applicable File Storage routing
→ fresh-observe current branch/worktree when material
→ preserve independent Scope / AUTH / DEL / Risk / REQ / DEC / integration / implementation / runtime gates
```

A material bootstrap/Root Governance contradiction that would route Material work to an incompatible Project target is fail-closed for the affected mutation and is surfaced; neither layer is silently rewritten. Benign syntax, mount, cache, container-path, or declared discovery-indirection differences are not DRIFT merely because strings differ when an explicit verified mapping proves the same governed Project/source identity.

For initialized Framework `1.2.6` Projects, generalized non-Google-Drive external storage is governed in active local `FRAMEWORK-001` under Project Location Binding as **File Storage Binding** / `file_storage_locations`. Framework `1.2.6` preserves the dedicated `project_location_binding.google_drive` block as the sole active Root Governance authority for Google Drive Project-root/content routing. A bootstrap `GOOGLE_DRIVE` locator maps to that dedicated block; the same Drive target/content scope MUST NOT be duplicated as generic File Storage authority.

Generic non-Drive provider/type vocabulary may include:

```text
S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER
```

Each applicable File Storage scope reuses exactly:

```text
BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED
```

Verification status reuses exactly:

```text
VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED
```

`BOUND` requires sufficient provider-appropriate durable identity and MUST pair only with `VERIFIED` or `USER_CONFIRMED`, never `verification_status: VERIFICATION_REQUIRED`. Durable identity SHOULD prefer source/provider-native identity where available: S3 bucket+prefix/canonical `s3://` URI; NAS/SMB server/share+governed path; NFS server/export+path; SharePoint stable site/library/folder identity; equivalent stable provider identifiers for other stores. Drive letters, local mounts, sync/cache paths, and display names are access/mapping evidence when a more durable identity exists.

Known-applicable but unresolved storage is `VERIFICATION_REQUIRED`: read/search/discovery/user confirmation needed to resolve it MAY proceed, but Material mutation is blocked by default. A Project with no external/non-repository storage MAY omit generic storage entries; do not synthesize provider `NOT_APPLICABLE` entries merely to fill a template. Missing/empty/unresolved storage never authorizes fallback to recent/search-ranked buckets, folders, shares, mounts, mirrors, or similarly named targets.

Multiple storage bindings are valid when content scopes are distinct; one governed content scope has one declared authoritative owner at a time. Backup, mirror, replica, archive, mounted, synced, cached, or copied content does not gain current storage/workspace/implementation authority by accessibility, recency, or content similarity.

File Storage Binding is Project file/object routing/content ownership and remains distinct from implementation/runtime authority:

```text
Repository Location Binding
≠ File Storage Binding
≠ Local Workspace Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location / Runtime Data / Persistent-State authority
```

A single physical S3/NAS/Drive/filesystem target may participate in more than one role only when each role is independently declared and governed. Source-code files existing in a storage copy do not make it Canonical Implementation Source. Project Location Binding MUST NOT add `canonical_branch` or another competing Git integration authority.

Actual storage credentials MUST NOT be stored in Bootstrap Location or Project Location metadata. Access keys, passwords, tokens, SAS tokens, secret-bearing signed URLs, and equivalent credential material remain outside Project Source; use existing `SECRET-*` external-reference metadata when credential routing must be referenced.

Location correctness never grants mutation authority. Existing `AUTH-*`, `DEL-*`, approval, scope, R0–R3 Risk, Requirements/Decisions, Base Freshness, Canonical Implementation Source, Runtime Truth, persistence, verification, and completion gates remain independently binding.

A one-off User Explicit Instruction naming an exact repository/workspace/storage target applies only to that otherwise-authorized action and does not persistently rewrite bootstrap or Root Governance locations. Persistent location change requires explicit approval and coordinated propagation; when active Project Location Binding changes, the existing `FRAMEWORK-001` revision → validate → promote → supersede/archive flow remains mandatory.

Existing initialized Projects stay pinned to their approved local Framework and do not auto-upgrade to `1.2.6`. Migration MUST NOT invent provider applicability, repository/storage identities, local paths, mappings, branch state, runtime roles, or verification status. Framework `1.2.6` adds no semantic slot, Stable-ID family, lifecycle/Git-freshness/Epistemic state, authority family, executable validator, selector, sync service, credential mechanism, or runtime enforcement automation.

### 2.7 Framework 1.6.0 Federated Project Graph

Framework `1.6.0` standardizes conditional `92 Project Graph` as the canonical home of current `REL-*` Project-relation assertions. A Project with no material relation truth does not create an empty `92`; it may materialize the document later when relations become applicable.

Relation endpoints use immutable `project_uuid` as authoritative Project identity. `project_id`, `project_name`, repository URL, local workspace path, MCP workspace ID, and OpenViking/index IDs remain labels or routing/index evidence only.

Core relation vocabulary is exactly:

```text
PARENT_OF
CHILD_OF
PEER_OF
DEPENDS_ON
SUPPORTS
RELATED_TO
```

Project/domain-specific relation types require the namespaced form `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>` and must not redefine a core type.

Current `REL-*` assertion state is exactly:

```text
ASSERTED
CORROBORATED
CONFLICTED
RETIRED
```

`ASSERTED` means the owning Project declares the relation. `CORROBORATED` requires verified compatible authoritative assertions with matching endpoint UUIDs; central index confidence or a derived inverse edge is not corroboration. `CONFLICTED` records irreconcilable authoritative Project assertions. `RETIRED` removes the relation from current topology while preserving its history.

Reciprocal compatibility includes `PARENT_OF ↔ CHILD_OF`, `CHILD_OF ↔ PARENT_OF`, `PEER_OF ↔ PEER_OF`, and `RELATED_TO ↔ RELATED_TO`. `DEPENDS_ON` and `SUPPORTS` are directional; a reciprocal record exists only when another Project independently asserts compatible truth. A derived inverse MAY be indexed for traversal but MUST NOT be written back as another Project's authoritative assertion.

`92` contains graph linkage and evidence/source pointers only. Canonical payloads remain in their existing homes: `DEP-*` in `91`, `DEC-*` in `04`, `REQ-*` in `05`, `ISS-* / DRIFT-* / CONFLICT-*` in `08`, and identity/lineage under existing root/change semantics. `REL-*` graph linkage ≠ `DEP-*` dependency-management payload.

Late binding is normal: Projects may begin independently, discover a relation later, create `92` when applicable, and add `REL-*` without reconstructing either Project or changing UUIDs. Relation topology change retires/supersedes relation records through normal history rather than rewriting the past.

Semantic nesting is independent from location/implementation/runtime roles:

```text
Project Relation
≠ Repository Location Binding
≠ File Storage Binding
≠ Local Workspace Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
```

`PARENT_OF` / `CHILD_OF` therefore does not require nested folders or repositories and never silently rewrites a binding or runtime topology.

Existing absorption/merge/split UUID and lineage rules remain authoritative. Relations of absorbed/predecessor Projects are reassessed for survivors/new descendants; they are not bulk-cloned. Material transformations use existing `MIG-*` and preserve history.

Cross-Project indexing/orchestration belongs at **AI-ControlTower** scope. OpenViking is `DERIVED_ONLY` and **REBUILDABLE** from authoritative Project Sources. It MAY discover/read relation records, normalize inverse/symmetric views, correlate reciprocal assertions, query/traverse, update affected nodes/edges, surface stale/orphan/conflicting derived state, and perform a full rebuild. It MUST NOT overwrite Project Source, infer authority from ranking/recency/similarity/confidence, synthesize authoritative reciprocal assertions, or become required to reconstruct current Project relation truth.

If Project Source and the derived index differ, Project Source remains authoritative. Reuse existing `DRIFT-*` for material stale/orphan projection mismatch and `CONFLICT-*` for managed authoritative disagreement; do not invent graph-specific parallel families. Timestamp/ranking/confidence never auto-resolves authoritative conflict.

Framework `1.5.0` permitted custom slot `92`. Brownfield upgrade to `1.6.0` MUST inspect slot occupancy and fail closed against overwrite: route `MIG-*`, preserve custom document identity/history/references, relocate only with governed approval to a free `93–99` or other semantically correct slot, then activate standard `92` only when applicable. Existing initialized Projects remain pinned and do not auto-upgrade.

This contract defines documentation/governance only and does not authorize OpenViking runtime/deployment, graph database selection, Graphify integration, crawler, watcher, webhook, scheduler, sync daemon, MCP graph service, validator/CLI, automatic discovery/promotion, or automatic conflict resolution.

## 3. Naming and Revision

Governed Project Source documents, Handoff, evidence/schema artifacts, exports, and packages created as Project Source artifacts end with:

```text
-YYMMDD-HHMM
```

Use Project/user local timezone unless Project-Specific Rules say otherwise. Document revisions use monotonic `r001`, `r002`, ... and never reuse a revision number.

Examples:

```text
05-Requirements-r007-260813-2237.md
40-Technical Design-r002-260820-1145.md
91-Project Management Control-r003-260820-1145.md
```

Canonical implementation filenames such as `README.md`, `main.py`, `docker-compose.yml`, and `SKILL.md` remain canonical when their ecosystem requires it.

## 4. Identity

Every Project has:

- `project_uuid` — immutable authoritative identity.
- `project_id` — stable human-readable identity.
- `project_name` — mutable display name.

Rename does not change `project_uuid`.

Merge semantics:

- **Absorption:** primary Project keeps UUID; absorbed Project retains its UUID historically and becomes `ABSORBED`.
- **True Merge:** create a new UUID; predecessors remain in lineage.

Split semantics:

- **Carve-out:** original keeps UUID; carved-out Project gets a new UUID.
- **True Split:** original lifecycle ends; descendants get new UUIDs.

Identity changes are event-based and reconstructable.

## 5. Current State vs History

`03-Current State` is a pure snapshot of now. Historical events belong in `10-Change Log` and archived revisions.

Project state has two axes:

```text
Lifecycle: DRAFT ACTIVE COMPLETED CANCELLED ARCHIVED ABSORBED MERGED SPLIT
Execution: READY IN_PROGRESS WAITING BLOCKED IDLE
```

Do not collapse them into one status.

## 6. Canonical Object Homes

```text
DEC-*       → 04-Decision Log
REQ-*       → 05-Requirements
ISS-*       → 08-Open Issues
DRIFT-*     → 08-Open Issues
CONFLICT-*  → 08-Open Issues
CHG-*       → 10-Change Log
ACTOR-*     → 11-Actor Registry
INST-*      → 11-Actor Registry
AUTH-*      → 12-Authorization Registry
DEL-*       → 12-Authorization Registry
EVD-*       → 13-Evidence Registry
ACT-*       → 15-Action Registry
MIG-*       → 16-Migration Registry
SECRET-*    → 17-Secret Reference Registry
RISK-*      → 91-Project Management Control
ASM-*       → 91-Project Management Control
MS-*        → 91-Project Management Control
OUT-*       → 91-Project Management Control
DEP-*       → 91-Project Management Control
CR-*        → 91-Project Management Control
GATE-*      → 91-Project Management Control
REL-*       → 92-Project Graph
```

One object type has one authoritative home. Other documents reference Stable IDs; they do not duplicate authoritative state. Detail documents may exist for large objects, but canonical status/identity stays in the canonical home.

### 6.1 Materialized Current State and Stable-ID Resolution

Active canonical object homes are **materialized current projections, not delta chains**. For every Stable ID that is active/current and referenced from Active/Current Project Source:

- current authoritative record MUST resolve within the **Current Reconstructable Snapshot**;
- record MUST contain sufficient current semantic payload to determine what is true now, or link to an active/current canonical Detail Document containing that payload;
- archived revisions MAY explain historical rationale/evolution, but MUST NOT be required to resolve Current Truth;
- `retain previous status`, `unchanged from rNNN`, `see archived revision`, or equivalent delta-only shorthand MUST NOT substitute for authoritative current payload;
- any active Detail Document required to interpret a current Stable ID is part of Current Reconstructable Snapshot and must be included in `CURRENT` export scope when needed.

This applies to `DEC-*`, `REQ-*`, Framework `1.2.0` management-control objects in `91`, and current `REL-*` records in active `92` equally. Failure to resolve a referenced current Stable ID without archive traversal is an integrity/readiness defect for the affected scope.

Stable IDs and revision numbers are never recycled.

### 6.2 Risk, Assumption, Milestone, Outcome, Dependency, Change, Gate

#### Risk vs Issue

`RISK-*` is a material uncertain future event/condition. `ISS-*` is a materialized/current problem. Risk materialization preserves `RISK-*` and links the resulting `ISS-*`; do not delete or rewrite the Risk into an Issue.

Risk statuses may include:

```text
IDENTIFIED OPEN MITIGATING MONITORING ACCEPTED MATERIALIZED CLOSED SUPERSEDED
```

`ACCEPTED` means remaining exposure is intentionally accepted. Material acceptance records the relevant decision/authority and review trigger where continued monitoring is needed.

Minimum Risk semantics include Risk Statement, Probability, Impact, Trigger/Early Warning, Mitigation, Contingency, Owner, Review Trigger/Review By, Status, related Stable IDs/evidence, and Materialized Issue when applicable.

#### Assumption

`ASM-*` is a proposition currently relied upon without sufficient verification to treat it as established truth.

```text
UNVERIFIED → VALIDATED / INVALIDATED / SUPERSEDED
```

Invalidation triggers impact assessment. Depending on affected truth, this may require `DRIFT-*`, `CR-*`, re-planning, Decision revalidation, Requirement revision, Risk update, or Issue creation. A validated assumption becomes verified truth only when an appropriate authoritative source/evidence supports promotion.

#### Action vs Milestone vs Outcome

```text
ACT-* = work/action
MS-*  = significant checkpoint/state
OUT-* = intended result/benefit/effect

ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED
```

Milestone and Outcome must be evaluated independently against their own criteria/evidence.

#### Dependency

`DEP-*` may represent `PERSON / TEAM / APPROVAL / DECISION / VENDOR / SYSTEM / API / DATA / CONTRACT / PROJECT / INFRASTRUCTURE / OTHER`.

`AVAILABLE` means the dependency is currently obtainable; `SATISFIED` means the governed dependency requirement has been fulfilled. A dependency failure may trigger a Risk, Issue, Change Request, or Health degradation based on impact.

#### Change Request vs Change Log

```text
CR-*  = proposed/material change + impact assessment + decision path
CHG-* = historical record of applied/observed change
```

A Change Request considers affected scope, Requirements, Decisions, Architecture, Tech Stack, source structure, configuration, installation/deployment modes, data/migration, security/authority, Milestones/Outcomes, Risks, Dependencies, schedule/effort, operations, and handoff when applicable. Approval authorizes only the governed scope; it does not grant unrelated implementation authority.

#### Review / Phase Gate

`GATE-*` is a governed checkpoint with Purpose, Affected Scope, Entry Criteria, Pass Criteria, Required Evidence, Review Owner, Required Authority, Status, Findings, Exceptions/Waiver, Next Action, and Reviewed At.

```text
PLANNED → READY_FOR_REVIEW → PASSED / FAILED / WAIVED
```

`WAIVED` requires explicit rationale plus applicable authority/decision reference. A Gate blocks only its governed scope unless a stricter Project-Specific Rule states otherwise.

### 6.3 Verified Task Completion Checkpoint

For a Material Task / `ACT-*` that materially mutates a Git-backed Canonical Implementation Source or another authoritative repository artifact, durable `DONE` requires a **Verified Task Completion Checkpoint**. Required scope is complete; applicable affected-scope/risk verification has passed; the required completed result is represented by observed Git commit(s); no required completed result exists only as uncommitted working-tree state; and any remaining working-tree changes are understood.

Read-only/no-repository-mutation Tasks require no synthetic commit. Failed, blocked, cancelled, or incomplete work cannot use commit existence to claim `DONE`; **WIP commit ≠ Task DONE**. One Task may use multiple coherent commits. **commit ≠ push**: remote publication remains a separate shared-state/authority action. Cross-environment handoff is continuation-safe only when the receiving environment can obtain the completion commit through the same durable repository or another governed transfer. Existing `ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED` remains binding.

## 7. Metadata

Governed Markdown documents have YAML Front Matter. Typical fields include:

```yaml
project_uuid: "..."
project_id: "..."
project_name: "..."
document_id: "STATE-001"
document_type: "CURRENT_STATE"
semantic_slot: "03"
revision: 1
document_status: "ACTIVE"
created_at: "2026-08-13T22:37:00+07:00"
updated_at: "2026-08-13T22:37:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-..."
epistemic_status: "USER_CONFIRMED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "<PINNED_FRAMEWORK_VERSION>"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
```

Binary/non-Markdown artifacts do not need embedded YAML; govern them via registries, paths, hashes, and Manifest metadata.

ProjectFramework uses agent/manual semantic validation by default. Do not invent runtime validator software unless explicitly requested as a separate implementation scope.

## 8. Truth, Uncertainty, and Freshness

Canonical Truth Domains:

```text
GOVERNANCE INTENT REQUIREMENTS IMPLEMENTATION RUNTIME DATA IDENTITY AUTHORITY HISTORY EXTERNAL
```

Authoritative source varies by domain:

- Governance → active approved `00-Project Source Framework` (`FRAMEWORK-001`).
- Intent → user-approved Project Source.
- Requirements → `05`.
- Implementation → verified source tree/Git.
- Runtime → fresh runtime observation.
- Data → actual authoritative datasource.
- Identity → identity metadata/history.
- Authority → `12`.
- History → `10` + archive.
- External → verified external source/system.

### 8.1 Canonical Implementation Source and Runtime Authority

เมื่อ implementation มีอยู่และความแตกต่างระหว่าง source กับ runtime มีผลต่อการพัฒนา, recovery, verification หรือ deployment Project MUST สามารถระบุ **Canonical Implementation Source** สำหรับ affected scope ได้: durable declared source location ที่ verified state ของมันเป็น authoritative `IMPLEMENTATION` Truth.

สำหรับ Git-backed Project โดยปกติคือ verified Git/source tree ตาม repository/workspace contract ของ Project. Canonical Implementation Source MUST durable เพียงพอต่อ development/recovery lifecycle ที่ Project ประกาศ; `durable` ในที่นี้หมายถึงไม่พึ่งการคงอยู่ของ runtime instance ที่ architecture ระบุว่า replace/recreate/dispose ได้ ไม่ได้หมายความว่า source MUST อยู่บน physical host filesystem เสมอ.

Valid topology อาจรวม:

```text
host filesystem Git repository
Git worktree
remote durable development workspace
VM-backed durable workspace
Dev Container + durable bind mount/workspace volume
other explicitly declared durable source location
```

**Runtime Truth remains distinct.** Fresh runtime observation authoritative สำหรับสิ่งที่กำลังรันอยู่จริง แต่ runtime execution/editing ไม่โอน Implementation authority โดยปริยาย.

```text
Implementation Truth → Canonical Implementation Source
Runtime Truth        → fresh runtime observation
```

ถ้า runtime/container filesystem มี code/config ที่ต่างจาก Canonical Implementation Source และสอง domain นี้ควร align ให้ใช้ `DRIFT-*` เมื่อ material. Runtime-only hotfix หรือ interactive edit MAY เป็น diagnosis/emergency intervention แต่ MUST NOT ถูกอ้างว่า canonical implementation update จน accepted intent ถูกนำกลับผ่าน governed change path เข้า Canonical Implementation Source และ reverify สำเร็จ.

Runtime component ที่ประกาศว่า disposable/recreatable MUST NOT เป็น sole authoritative implementation copy โดยอุบัติเหตุ. State ที่ `REQ-*`, `DEC-*`, `40 Technical Design` หรือ deployment contract กำหนดว่าต้อง survive expected runtime replacement MUST มี declared persistent-state authority/mechanism ที่สอดคล้องกับ lifecycle นั้น. Rebuildable cache/temp/scratch/generated state MAY remain ephemeral เมื่อไม่มี survival requirement.

Framework ไม่บังคับ Docker, host-local source, immutable image หรือ production source mount policy แบบ universal; topology เหล่านี้เป็น Project-specific/applicability-driven และต้อง preserve Truth/authority/persistence contracts ข้างต้น.

Epistemic Status:

```text
VERIFIED USER_CONFIRMED INFERRED ASSUMED UNKNOWN CONFLICTED STALE
```

Freshness:

```text
IMMUTABLE STABLE CHANGEABLE VOLATILE
```

Never promote `ASSUMED` or `INFERRED` to `VERIFIED` without evidence/authoritative verification. `VOLATILE` information must be fresh-checked before it materially drives a decision or mutation.

## 9. DRIFT and CONFLICT

Use `DRIFT-*` when Truth Domains that should align do not align. Record expected truth, observed truth, evidence, impact, affected scope, resolution owner, and mutation block. Drift blocks the affected scope, not the entire Project by default.

Use `CONFLICT-*` for competing document/semantic states, including concurrent revisions. Never use last-write-wins for semantic changes.

Formal candidates record `base_revision` and `base_document_hash`. If active base changed, promotion stops and a conflict is opened. Agents may auto-resolve only non-semantic differences such as formatting, whitespace, deterministic sorting, or a typo that cannot alter meaning.

For `SOURCE_AND_DOCKER`, unexpected feature/configuration/data/security/persistence divergence from the declared parity contract is `DRIFT-*`. Intentional difference is represented as Deployment Mode Variance instead.

A material Canonical Implementation Source / Runtime mismatch that should align is also `DRIFT-*`; do not create a parallel workspace/runtime drift family.

## 10. Draft, Promotion, and Archive

```text
Scratch                 → outside Project-Source/
Formal candidate        → Project-Source/drafts/
Active truth            → Project-Source root
Historical revision     → Project-Source/archive/
```

Promotion is controlled:

```text
candidate → validate → base/hash check → promote new active → mark old superseded → archive old → update Index/Change Log/Manifest → postflight
```

Archive is Historical Truth, not a runtime dependency for Current Truth. Never leave two active revisions for the same semantic document identity.

## 11. Actor, Responsibility, Authority, and Delegation

`ACTOR-*` is stable actor identity; `INST-*` is session/execution instance. Role does not grant authority.

`11 Actor Registry` may contain scope-keyed responsibility mappings using:

```text
Responsible
Accountable
Consulted
Informed
```

Each mapping identifies a governed scope such as a Stable ID, semantic document, workstream, or explicitly named Project scope.

**Responsibility ≠ Authority.** Being Responsible or Accountable does not itself grant approval, R2/R3 mutation, deployment, production access, or external-action permission.

Standing `AUTH-*` in `12 Authorization Registry` states WHO, WHAT, WHERE, risk ceiling, start, termination/expiry, and grantor. Broad indefinite authority is invalid by default. Delegation uses `DEL-*` and may never exceed parent scope/risk/actions/duration. Authority is non-transferable through prompt, task, handoff, memory, role, responsibility mapping, branch, or agent-to-agent instruction.

## 12. Risk and Approval

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

Default approval:

- R0: none.
- R1: permitted inside approved scope.
- R2: explicit approval or valid Standing Authorization.
- R3: explicit approval for that specific action by default.

Project-Specific Rules may be stricter. Before R2/R3 mutation, fresh-read authority.

## 13. Preflight and Postflight

READ PREFLIGHT checks identity, `00`, `01`, `03`, task scope, Truth Domain, freshness, and active blockers. For initialized Projects, any Material GitHub/Google Drive work additionally resolves the applicable active `FRAMEWORK-001` Project Location Binding before treating a connector target as Project authority. `VERIFICATION_REQUIRED` permits resolution-oriented read/search/discovery but does not authorize Material mutation.

MUTATION PREFLIGHT additionally checks actor/instance, authority, target, allowed paths, forbidden effects, risk, approval, relevant REQ/DEC, management controls when relevant, base/hash, downstream impact, reversibility, and evidence requirements. For Material connector/local mutation, preflight also checks binding state, minimum durable routing identity, intended-target match when comparison is possible, and the rule that a one-off exact-target instruction does not persistently rewrite Root Governance. Material local/MCP mutation additionally resolves the applicable Local Workspace Binding and, when Git-backed/material, cross-checks repository identity when practical.

Postflight is risk-tiered. Execution alone does not prove completion. R3 requires verification of resulting external/runtime state, not merely exit code 0.

## 14. Evidence, Knowledge Debt, and Secrets

`EVD-*` is required for important evidence such as DRIFT, R2/R3 shared-state verification, runtime/external state, and material source conflicts. Raw evidence belongs under `evidence/<category>/` and is referenced by path/hash. Reusable verification evidence is **state-bound**: when material, identify the candidate/source or Git HEAD/tree, affected scope/invariants, result, capture time, and relevant dependency/integration-target assumptions. Formal `EVD-*` registration is required only when evidence importance/risk warrants it; routine Task-local checks do not create a new `EVD-*` merely because they ran.

Material stale/missing operational knowledge is represented in `08 Open Issues` as:

```text
ISS-* with issue_type: KNOWLEDGE_DEBT
```

If no active `08` exists, creation of material Knowledge Debt makes `08` applicable. Knowledge debt may degrade Knowledge or Readiness health even if runtime currently succeeds.

Never place actual secrets in Project Source, evidence, Manifest, or exports. `SECRET-*` stores only metadata/reference to an external secret store, with `secret_value_present: false`.

## 15. Index, Manifest, and Conditional Extended Documents

`01-Project Source Index` is the Front Door. It contains a derived active document registry plus human/agent routing guidance. The generated registry is not manually authoritative.

When active, route:

```text
40 → Tech Stack / technical design / source/config/runtime blueprint
60 → installation / deployment / operations blueprint
92 → REL / Project relation assertions
91 → RISK / ASM / MS / OUT / DEP / CR / GATE
```

`14-Manifest` covers the Current Reconstructable Snapshot: active docs, continuation-relevant formal drafts, registered evidence, validation assets, necessary generated assets, and every active/current Detail Document required to interpret referenced current Stable IDs. If active `40`, `60`, `91`, or `92` is required to interpret current truth, it belongs in the Manifest and `CURRENT` export scope.

When Framework Source Provenance is tracked, `14` preserves the same observed state as active `00`. Missing optional exact Git provenance is not itself a Manifest defect; fabricated provenance is prohibited.

Manifest integrity mismatch requires root-cause classification; do not blindly regenerate to hide unexpected change.

## 16. Handoff

`09-Handoff` is the current continuation contract, not merely a chat summary.

```text
DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED
```

It records from/to, previous handoff, trigger, current phase/state, completed work, pending work, formal drafts/WIP, active objects, read order, freshness warnings, authority references, `authority_transfer: false`, and exact next action. When material to continuation, it also references the active Local Workspace Binding plus observed repository identity, current branch/worktree, verified HEAD, working-tree state, last completed Task/ACT, completion commit(s), verification result/evidence pointer, and remote reachability when the receiver needs it.

When applicable, surface continuation-critical `RISK-*`, invalid/unverified `ASM-*`, blocking `DEP-*`, upcoming/recent `MS-*`, Outcomes awaiting measurement, open/approved `CR-*`, upcoming/failed `GATE-*`, Technical/Deployment health warnings, Source/Docker variance, and Knowledge Debt.

Before `ACCEPTED`, recipient reads `00 → 01 → 03 → 09`, checks actor/authority, relevant active objects, volatile state, and current handoff revision.

### 16.1 Externalized Working Memory and Chat Lifecycle

**Externalized Working Memory** is the minimum durable continuation state maintained outside Chat in source-native Project storage. Chat remains a temporary interaction/execution surface; connector/MCP use does not make Chat persistent Project memory.

Canonical terms:

- **Material Project Work** — any connector-derived result or change needed for reliable continuation, governance, decision-making, or execution.
- **Transient MCP Activity** — reads, searches, comparisons, or intermediate connector detail that is discarded or not needed for later continuation.
- **Logical Checkpoint** — the coherent point after related connector activity where the current usable result can be persisted once without per-tool-call logging.
- **PERSISTED** — required durable continuation state has been successfully written to its source-native owner or approved continuation cache.
- **PERSISTENCE_PENDING** — required durable continuation state has not been successfully written; continuation safety must not be claimed.
- **CONTINUE_CURRENT_CHAT** / **START_NEW_CHAT** — the only Chat lifecycle recommendation vocabulary.

Binding behavior:

1. Material Project Work MUST be persisted at a Logical Checkpoint; Transient MCP Activity has no persistence requirement by default.
2. GitHub-backed Material Project Work persists to the repository artifact or canonical Project Source semantic home that owns the state.
3. Google Drive Material Project Work updates the existing designated Project progress `.md` when one exists. If none exists and durable continuation state is required, use one stable `PROJECT-PROGRESS.md` as a continuation cache, not as a new authoritative source.
4. Cross-system GitHub/Drive state uses references/pointers. Do not create a third duplicate source of truth.
5. Do not persist raw MCP/tool payloads, long search-result dumps, full diffs, repetitive intermediate state, or private intermediate reasoning merely for audit convenience. Include such detail only when explicitly requested or necessary for approval or ambiguity resolution.
6. `09-Handoff` remains a continuation contract, not an MCP transcript or execution log.
7. If required persistence fails, classify the state as `PERSISTENCE_PENDING`, disclose what remains unpersisted, and default to `CONTINUE_CURRENT_CHAT`.
8. `START_NEW_CHAT` is continuation-safe only after the durable state outside Chat includes current state, blocker/pending state, Exact Next Action, and Required Read location.
9. A new chat/session MUST be able to continue from persisted current state and Required Read pointers without the old chat transcript as a prerequisite.
10. A successful connector call alone is not a Logical Checkpoint and MUST NOT trigger one progress write per tool call.
11. Existing initialized Projects remain governed by their local pinned Framework and never auto-upgrade merely because upstream ProjectFramework changes.
12. A Logical Checkpoint proves durable continuation integrity; **Logical Checkpoint ≠ RELEASE_FULL**. Run only materially affected cross-surface checks at the checkpoint unless it is itself a semantic acceptance/release gate.

### 16.2 Progressive / Risk-Scoped Verification

Verification depth follows affected scope, dependency impact, and `R0 / R1 / R2 / R3` risk. Workflow labels `TASK_LOCAL_FAST`, `CHECKPOINT_INTEGRITY`, `RELEASE_FULL`, and `INTEGRATION_GATE` are operational vocabulary only—not lifecycle, Epistemic Status, Git freshness, or Stable-ID states.

- `TASK_LOCAL_FAST` → minimum sufficient affected-scope/risk checks before a Material Task can become `DONE`.
- `CHECKPOINT_INTEGRITY` → durable continuation checks plus only affected cross-surface integrity.
- `RELEASE_FULL` → full candidate/distribution verification at a completed Release Candidate or equivalent semantic acceptance boundary.
- `INTEGRATION_GATE` → fresh Canonical Integration Target/Base Freshness + validity of prior acceptance evidence.

Fresh state-bound evidence MAY be reused while its proven candidate/dependency/target assumptions remain materially unchanged. Candidate/source changes, materially changed dependencies, semantic target movement, changed acceptance criteria, contradicting evidence, or unbounded uncertainty invalidate affected evidence. If impact cannot be bounded safely, verification escalates.

### 16.3 Chat Closure Consistency and Mandatory Response Close

Framework `1.2.4` makes Chat closure deterministic while preserving the existing persistence gate and lifecycle vocabulary. Binding invariants are:

1. If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, `[Chat]` MUST be `START_NEW_CHAT`.
2. If `[Chat]` is `CONTINUE_CURRENT_CHAT`, `[Next Action]` MUST contain one concrete continuation action and MUST NOT be `ไม่มีขั้นตอนถัดไป`.
3. `PERSISTENCE_PENDING` MUST pair with `CONTINUE_CURRENT_CHAT` and one concrete persistence/recovery Next Action. `PERSISTENCE_PENDING + ไม่มีขั้นตอนถัดไป` and `PERSISTENCE_PENDING + START_NEW_CHAT` are invalid.
4. `START_NEW_CHAT` MAY pair with a concrete Next Action when required Material state is durably persisted and continuation is safe from external state plus Required Read pointers.
5. `START_NEW_CHAT` is a continuation-safety recommendation, not a claim that the platform forces navigation.

Every Framework-governed response MUST end with exactly these two headings, in order, with nothing after the second section. The canonical semantic field labels are `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:`. For Markdown output, use a presentation wrapper that keeps the labels visibly renderable rather than beginning a bare paragraph with reference-definition-like syntax:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Chat]:** CONTINUE_CURRENT_CHAT | START_NEW_CHAT

**[Reason]:** <concise reason>

**[Required Read]:** <canonical locations or ไม่มี>
```

The four semantic fields remain separate Markdown paragraphs. Bold or equivalent Markdown-safe wrapping is presentation-only; it does not rename the canonical labels or lifecycle tokens. Canonical lifecycle tokens remain exactly `CONTINUE_CURRENT_CHAT` and `START_NEW_CHAT` and stay unescaped.

Before emit, every Framework-governed assistant response MUST run a lightweight **Response Close Completeness Gate** on the assistant final-response representation: exactly the two mandatory headings in order; exactly one visible semantic `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:` field in separate paragraphs and in that order; one canonical lifecycle token in `[Chat]`; valid Chat Closure Consistency; and nothing after `[Required Read]`. Presentation wrappers are ignored for semantic field identity. Missing, duplicate, malformed, hidden/non-visible, out-of-order, or contradictory close content must be corrected before emit. The gate does not claim visibility into downstream transport/UI rendering; user-reported rendered omissions are regression evidence while the exact loss layer remains unverified unless independently observed.

Framework `1.12.1` TASK-042 makes this gate an explicit **unskippable final-response control-flow invariant**. Before the first Project-governed response in each chat/session, resolve the applicable Project Bootstrap when it is accessible so local governance is loaded before response generation; read-only, status, diagnostic, explanatory, and failure-report responses are not exempt merely because no Material mutation is planned. Before Material Project work, all existing binding, authority, Risk, and mutation gates still apply independently.

Every Project-governed final response MUST pass the Response Close Completeness Gate immediately before emit. **No early-return path may bypass it.** This includes ordinary success, read-only/status/diagnostic paths, tool/MCP failure or exception, connector unavailable/disconnected handling, timeout, partial-result/degraded-mode response, refusal or blocked-action response, persistence failure / `PERSISTENCE_PENDING`, exception-recovery, and bootstrap repair/verification-required responses when a Project-governed final response is being produced. Intermediate tool output/error payloads are not final responses. A tool/MCP or connector failure alone does not imply `PERSISTENCE_PENDING`; use that state only when required durable continuation state is actually unpersisted.

### 16.4 Registered Project Command Contract

Framework `1.3.1` extends the Framework `1.3.0` semantic command registry for common Project inspection and governed upgrade entry. Registered command identity includes literal `[` and `]` delimiters. Matching of the registered name inside the brackets is case-insensitive; missing brackets do not invoke the registered command token. This is a governance/interface contract, not authorization to create a parser service, updater, or other executable runtime.
Framework `1.8.0` TASK-039 further registers persistent `[Goal]` continuous-execution semantics by composing existing `OUT-* / AUTH-* / ACT-* / ENV-* / 09` homes; it adds no `GOAL-*` Stable-ID family or semantic slot.
Framework `1.8.0` TASK-024 further registers `[Meeting]` as a multi-model advisory command using a Thin Council Provider Adapter boundary; it adds no `MEETING-*` Stable-ID family, semantic slot, or provider authority home.
Framework `1.8.0` TASK-026 further defines a Compositional Disclosure Boundary for external-AI Project context using existing `AUTH-* / EVD-* / SECRET-*` homes; it adds no `DISC-*` Stable-ID family, semantic slot, mandatory per-object classification field, or runtime disclosure system.
Framework `1.9.0` TASK-041 further defines Portable Installation Bootstrap & Project Settings Handoff: current vendor Project Settings use a two-binding thin adapter while existing internal location semantics remain governed; root README gains a managed fallback; active local `FRAMEWORK-001` remains authority.
Framework `1.10.0` TASK-025 further defines the optional Project Knowledge Layer as derived/advisory Markdown outside Project Source authority, with provenance, maintenance-state, promotion, disclosure, and OpenViking content-class boundaries.


Initial registry:

```text
[Project Status] : fresh-read Project identity, Task state, Git sync/working-tree state, verification, blockers, and health
[Project Path]   : show/verify configured bootstrap path values and route explicit path-change requests through existing location governance
[Project Upgrade] : fresh-compare the active Project Framework with canonical upstream and offer governed upgrade preparation when they differ
[Session] : declare, show, or close the user-pre-approved scope of operations for the current session/task
[Goal] : create/show/change/cancel a persistent outcome and its bounded continuous-execution authorization
[Meeting] : convene a multi-model advisory council for a question using minimum authorized context; results are evidence/advice, never Project authority
```

Natural-language requests for available commands (for example “มีชุดคำสั่งอะไรบ้าง”, “command list”, or “available commands”) MUST list only commands registered by the active Framework/Project in `[XXX] : purpose` form. Do not invent commands merely because an Agent/tool could perform another action.

#### `[Project Status]`

`[Project Status]` is read-only and MUST fresh-observe available current sources rather than reuse chat memory as current evidence. Present applicable dimensions in this order: **Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers → Continuity**.

- Identity includes Project/repository, Workspace, current branch/ref, and observed HEAD when available.
- Health reuses existing `GREEN | AMBER | RED | UNKNOWN`; no competing `YELLOW` state is introduced.
- Remain Tasks comes from the applicable Task source and shows count plus Task ID/state/concise detail when exposed.
- Continuity reports the latest Resume Block freshness as `FRESH | STALE | NONE`, the active Envelope (`ENV-*`, valid/expired), and a repeated-break indicator when handoffs show the same link breaking across consecutive checkpoints (surfaced as an `ISS-* KNOWLEDGE_DEBT` candidate). All vocabulary reuses existing families.
- Git Sync reports remote/tracking target, ahead/behind/divergence, and remote freshness. A `VERIFIED` remote-freshness claim requires an applicable fresh remote observation; cached remote-tracking state alone is insufficient. `STALE` / `VERIFICATION_REQUIRED` may be used as diagnostic report labels without becoming new Framework lifecycle states.
- Working Tree reports `Waiting Commit: Yes | No` plus changed/staged/unstaged/untracked counts. Git file/change count MUST NOT be converted into logical Task count.
- Verification reports latest applicable `PASS | FAIL | NOT_RUN | UNKNOWN` plus evidence validity/context when available.
- Blockers report material blockers or `None` only when absence is actually supported.

Unavailable dimensions remain explicit `UNKNOWN` / `VERIFICATION_REQUIRED`; never fabricate status from memory, old tool output, search ranking, or an unverified remote ref.

#### `[Project Path]`

`[Project Path]` reads and verifies the applicable Framework/Git/Storage/MCP/Workspace location semantics from current Project Settings/bootstrap/internal location sources and active Project Location Binding. Framework `1.9.0` does not require the legacy five labels as current vendor Project Settings fields; their underlying roles remain governed. Any configured angle-bracket placeholder means **unset / not configured**, not a literal path. Missing/unset values never authorize fallback to recent, active, mounted, cached, search-ranked, or similarly named locations.

The command may include an explicit request to change one or more path values, but it grants no new mutation authority. A one-off exact target remains action-specific. Persistent Bootstrap Location or active Project Location Binding changes still require applicable User Explicit Approval and, when Root Governance is affected, the normal `FRAMEWORK-001` revision → validate → promote → supersede/archive flow.

#### `[Project Upgrade]`

`[Project Upgrade]` is read-only through current/target comparison and reporting. For an initialized Project, resolve the valid active local `FRAMEWORK-001` first and treat its locally pinned Framework/Schema identity as current Project authority. Then fresh-resolve the applicable canonical upstream Framework as a target candidate. Chat memory, prior command output, cached `origin/main`, recent/active workspace ranking, similarly named repositories, or other inferred fallbacks do not establish current upstream truth.

Minimum comparison considers current/target Framework version, Schema version, observable source/distribution identity, and freshness evidence. Report exactly one of these presentation-only labels when supported:

```text
UP_TO_DATE
UPGRADE_AVAILABLE
SOURCE_DIVERGENCE
VERIFICATION_REQUIRED
```

These are command-report labels only, not new lifecycle, Epistemic Status, Git freshness, authority, migration, or health state families. Equal version strings do not suppress a material source/distribution conflict; unresolved or conflicting inputs fail closed as `SOURCE_DIVERGENCE` or `VERIFICATION_REQUIRED` rather than being guessed `UP_TO_DATE`.

If a verified target differs from the current local pin, `UPGRADE_AVAILABLE` asks whether the user wants to **prepare** an upgrade. A positive answer authorizes cumulative current→target assessment and Preview preparation only; it does **not** authorize immediate Project mutation. Actual mutation still reuses the existing Direct-to-Latest flow: classify `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, preserve current truth/Stable IDs/Project-specific rules/bindings/history and applicable authority/Task state, include rollback/reversibility and verification in the Preview, obtain separate explicit mutation approval, run affected verification plus one final `RELEASE_FULL`, then promote while preserving history. Intermediate release execution remains non-mandatory and the latest starter remains non-destructive by default.

When the command reports `UPGRADE_AVAILABLE`, its report includes the target release's migration-notes pointer when `MIGRATION-NOTES.md` covers that target, and states their absence explicitly when it does not; affected surfaces therefore become visible before preparation is decided. Upgrade preparation uses `templates/upgrade-preview.md` as the standard Preview structure; deviation is permitted only with explicit reason recorded in the Preview.

**FAST_PATH verification scope rule.** For a Project classified `FAST_PATH`, when the exact target candidate tree already carries committed state-bound evidence — the recorded tree SHA equals the freshly observed target tree SHA — the upgrade may satisfy final verification through proportional resulting-state confirmation (release identity plus affected checks) instead of rerunning one full verification from scratch. This reuses Framework `1.2.5` evidence-reuse semantics. Evidence reuse fails closed whenever the candidate changed after its evidence was captured, the tree SHA does not match exactly, or evidence validity cannot be freshly confirmed; in those cases the existing one-final-`RELEASE_FULL` requirement applies unchanged. `ASSESSED_PATH` and `MAJOR_MIGRATION_REQUIRED` are never eligible for this substitution.

`[Project Upgrade]` grants no Bootstrap/Project Location mutation authority and no branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime, or Persistent-State authority.

`MIGRATION-NOTES.md` documents per-release upgrade guidance (affected surfaces, checklist). It is a routing/documentation aid — never normative authority — and Core Governance plus the latest amendment win on any conflict. Missing notes for a transition remain an explicit `UNKNOWN`; they are never invented retroactively.

### 16.5 Portable Installation Bootstrap & Project Settings Handoff

Framework `1.9.0` standardizes the target user-facing Project Settings adapter as:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before the first Project-governed response in each chat.
Read-only, status, diagnostic, and failure-report responses are not exempt.
Before Material Project work, also apply all existing binding, authority, risk, and mutation gates.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

Before the first Project-governed response in each chat/session, use the adapter/root README fallback to resolve Project Bootstrap when safely accessible. Read-only, `[Project Status]`, troubleshooting, diagnostic, and failure-report responses are not exempt. This first-response bootstrap is discovery/governance loading only; it grants no mutation authority.

`ProjectFramework Upstream` is Framework read-through/current-target evidence only; it is never the consuming Project repository, Integration Target, Implementation Source, Runtime Location, or Project authority. `Project Bootstrap` is environment-specific and MUST be verified before being presented as ready to paste. Unknown path = `VERIFICATION_REQUIRED`; memory, recent workspaces, editor/MCP handles, mounts, ranking, and lookalikes never fill it.

GREENFIELD Framework `1.9.0` resulting state includes root `PROJECT-BOOTSTRAP.md` plus exactly one valid consuming `README.md` managed fallback:

```md
<!-- PROJECTFRAMEWORK-BOOTSTRAP:START -->
## ProjectFramework Bootstrap

ProjectFramework Upstream:
https://github.com/captainhuke-dev/ProjectFramework

Project Bootstrap:
./PROJECT-BOOTSTRAP.md

AI / Agent:
Read `PROJECT-BOOTSTRAP.md` before Material Project work.
<!-- PROJECTFRAMEWORK-BOOTSTRAP:END -->
```

If README is absent, create it with the block. If README exists without the block, append the block while preserving existing content. With exactly one valid block, update only its managed body when required. Duplicate or malformed marker structures fail closed for automatic rewrite and require governed repair; never select by recency/position/similarity. ProjectFramework owns only bytes inside the marker pair for bootstrap maintenance.

Bootstrap resolution is: usable Project Settings Project Bootstrap → otherwise root README managed fallback → `PROJECT-BOOTSTRAP.md` → validate active `FRAMEWORK-001` → `01 → 03` and `09` when continuation applies. Settings, README, upstream, and root bootstrap are discovery/locator layers; active local `FRAMEWORK-001` is Project governance authority. A stale absolute Settings path after clone/move may use the relative README fallback; successful discovery does not rewrite Local Workspace Binding.

GREENFIELD installation uses fresh canonical upstream → required bootstrap sources → read-only Project/environment resolution → one Preview → explicit approval → active `00` first → mandatory `01–05` + `09–17` → applicable conditional docs → root bootstrap + managed README → local Framework/Schema pin → resulting-state verification → **Core Installation DONE** → mandatory copy-ready `Project Settings — Required User Handoff`. The approved Preview covers ordinary resulting files in the approved scope; do not re-prompt per file unless scope changes or a higher-level gate applies.

Core installation completion is distinct from external vendor-settings mutation/confirmation. Do not create a `PROJECT_SETTINGS_*` lifecycle family and do not claim vendor settings were changed without independent execution evidence.

The simplified adapter removes no internal capability: `framework_source`, `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, dynamic `current_branch_worktree`, `[Project Path]`, and active Project Location Binding semantics remain available. The legacy five Project Settings labels are no longer mandatory current adapter fields.

If valid active Project Source already exists, never perform GREENFIELD recreation. Brownfield adoption uses governed `[Project Upgrade]`, preserves local pin/truth/Stable IDs/bindings/history, Previews root/README/adapter effects, and returns a refreshed absolute Project Settings block without claiming UI mutation.

Neither bootstrap adapter, README fallback, root bootstrap, nor installation handoff stores actual secret values or grants disclosure/authorization. Installation does not synthesize Goal/Auth/ENV/Meeting/provider/disclosure/runtime/daemon state merely because ProjectFramework is installed.

### 16.6 Framework 1.10.0 Project Knowledge Layer

Framework `1.10.0` adds an optional Markdown-first **Project Knowledge Layer** for reusable synthesis while preserving the invariant `Project Knowledge ≠ Project Authority`. When applicable, a consuming Project may materialize root-level `Project-Knowledge/` outside the `Project-Source/00–99` semantic namespace. It is neither a semantic slot nor Root Governance and never precedes `PROJECT-BOOTSTRAP.md → active FRAMEWORK-001 → 01 → 03` authority resolution.

Canonical maintained layout is:

```text
Project-Knowledge/
├── README.md
├── index.md
├── log.md
└── pages/
```

A maintained Knowledge page uses compact YAML fields including `knowledge_page_id`, `title`, `knowledge_state`, `created_at`, `updated_at`, `source_refs`, `related_project_source_refs`, `related_knowledge`, and `review_trigger`. `knowledge_page_id` is Knowledge-layer identity only and does not become Project Source authority.

Exact maintenance state vocabulary is:

```text
CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED
```

Knowledge state describes maintenance/navigation state, not claim truth certainty. Material claim uncertainty remains explicit in prose and provenance.

Material synthesized claims require reconstructable `source_refs`. Raw/source material remains in its authoritative or source-native location by default; Knowledge references rather than obligatorily duplicates it. Any deliberate retained copy gains no authority merely from location.

`index.md` is navigation metadata, never truth ranking. `log.md` is chronological append-only history for material Knowledge operations using `ingest`, `query-file`, `lint`, or `maintain`; it is not an MCP/tool transcript, raw search dump, or private chain-of-thought store.

Knowledge operations are:

```text
ingest     → source/provenance → compare → page/link/index/log update → surface contradictions/promotion candidates
query-file → file reusable synthesis using the same provenance/link/index/log contract
lint       → advisory checks for staleness, contradiction, broken/orphan links, weak provenance, superseded sources, and unreviewed promotion candidates
```

No operation promotes Knowledge into Project Source automatically. Knowledge contradiction does not automatically create Project Source `CONFLICT-*`; authoritative `DRIFT-* / CONFLICT-*` semantics apply only when their existing threshold is met.

**Knowledge→Governance promotion gate:** identify the target canonical Project Source home → verify evidence → assess affected governed objects → obtain applicable authority/approval → mutate only the canonical owner through its normal revision/validation/promotion flow → preserve minimum evidence/linkage → update Knowledge to reference the governed result. A Knowledge page is never approval by itself and is not copied wholesale into Evidence by default.

Integration boundaries remain distinct:

- TASK-023/bootstrap resolves Project authority before Knowledge discovery/use.
- TASK-024 `[Meeting]` output remains advisory; material Meeting results may feed Knowledge only with provenance/limitations preserved.
- `EVD-*` remains reconstructable evidence basis; Project Knowledge remains derived/advisory synthesis.
- `03` / `09` may point to Knowledge only when material to current work; they do not mirror its content.
- Knowledge cross-links are advisory content links, not `REL-*`; Project Graph assertions remain canonical in `92`.
- TASK-026 disclosure still applies independently to external use of Knowledge; advisory/local status never grants outbound permission.
- AI-ControlTower/OpenViking indexing preserves explicit content classes `PROJECT_SOURCE_AUTHORITY` and `PROJECT_KNOWLEDGE_ADVISORY`; OpenViking remains `DERIVED_ONLY` and rebuildable. Retrieval rank, vector similarity, recency, graph centrality, or combined search never transfers authority.

GREENFIELD Project Knowledge is optional/applicability-driven and is created only when useful and approved after active `FRAMEWORK-001` exists. Brownfield Projects remain pinned; adoption is governed and never bulk-imports historical notes/chats/files as accepted Knowledge or Project truth without provenance review.

Actual secret values remain forbidden. Knowledge maintenance authority does not imply Project Source mutation, external disclosure, push/publication, Root/Binding, Decision, Risk acceptance, or runtime authority.

Framework `1.10.0` defines documentation/governance/templates only and creates no wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, validator/CLI, scheduler, or runtime automation.

### Continuation Contract and Resume Blocks

At every Logical Checkpoint on Material work, persist a **Resume Block** into `09 Handoff` (mirrored as a one-line status in `03 Current State`) containing exactly: active task ID, last completed step, next step, open blockers, and the active Envelope reference (`ENV-*`) if any. A fresh session — ChatGPT, Claude, or any agent with MCP access to the Project Source — MUST be able to resume Material work from the Resume Block alone within one read, with no chat-history dependency. Failure to persist follows existing `PERSISTENCE_PENDING` semantics; no new failure state exists.

### MCP Resume Semantics

Material MCP operations that mutate state SHOULD be structured as idempotent steps: re-executing an already-applied step produces no duplicate effect. Non-idempotent operations MUST record pre-execution intent in the current Checkpoint before the call, so a connection drop cannot cause silent double-execution without evidence. After any drop, resume from the last persisted Resume Block/Logical Checkpoint — never from memory of the dropped session. This is a contract for runtime implementations; this Framework defines it and implements none of it.

#### `[Session]`

`[Session]` declares (`declare`), displays (`show`), or ends early (`close`) a user-pre-approved scope of operations for the current session/task. `declare` records an explicit Envelope as an `ENV-*` entry in `15 Action Registry`: allowed operation types, target surfaces, expiry (session end / task completion / explicit time), and prohibited zones.

An Envelope never overrides fail-closed governance: location/binding changes, Root Governance mutation, schema/slot authority, secret handling, and push keep their own approval gates regardless of any Envelope. Ambiguous or out-of-scope operations fail closed to normal approval. One-off exact-target instructions remain action-specific as before. Envelopes are auditable records in `15`, not side-channel permissions.

## 17. Adoption Modes and Bootstrap
#### `[Goal]`

`[Goal]` creates, shows, changes, or cancels a **persistent** user-authorized outcome and its bounded continuous-execution authority. Literal brackets are required; registered-name matching inside them is case-insensitive. Unbracketed `goal` wording remains ordinary language and does not silently create persistent authority.

Canonical composition is: Goal outcome = `OUT-*` in `91`; persistent Goal authority = `AUTH-*` in `12`; executable work = `ACT-*` in `15`; session/task envelope = `ENV-*` in `15`; `03` summarizes current Goal state; `09` carries continuation pointers only and retains `authority_transfer: false`. No canonical `GOAL-*` family exists. `Outcome ≠ Action ≠ Authority ≠ Handoff` and `ACT DONE ≠ OUT ACHIEVED` remain binding.

Goal-specific `OUT-*` status is `ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED`. `BLOCKED` is non-terminal and is used only when a global blocker leaves no meaningful safe next action. `ACHIEVED` requires evidence for every declared success criterion; linked Actions being DONE is insufficient. `CANCELLED` or `SUPERSEDED` terminates/revokes dependent Goal `AUTH-*` prospectively while preserving completed history/evidence.

Unless the user explicitly narrows the Goal, persistent Goal `AUTH-*` MUST by default cover the bounded normal local-development workflow required for the stated outcome: local read/inspection/research, architecture/design, implementation planning, non-destructive in-scope file create/edit/move, tests/lint/typecheck/build/validation, debugging/corrective edits, local Git add/commit, Logical Checkpoints, and required Project Source continuation/evidence updates. An operation clearly covered by current valid Goal authority MUST NOT be re-prompted solely for **Framework-level** approval; continue to the next safe in-scope action while preserving Scope, Risk, binding, Git integration, verification, and higher-level controls.

The following effects are excluded by default and become Goal-authorized only through the exact stated opt-in boundary:

```text
push/publication       → explicit publish/push intent + governed target; fresh integration/target/evidence preflight still required
destructive operation  → explicit operation + target (+ stated conditions when applicable); never generalized
Root/Binding mutation  → explicit mutation + target; normal revision → validate → promote → supersede/archive → sync → verify lifecycle still required
external disclosure    → separate applicable disclosure authorization; Goal local execution authority never implies outbound AI/provider disclosure
```

Actual secret values remain forbidden in Goal records, Project Source, Handoff, Evidence, plans, logs, and exports; use governed `SECRET-*` references/provider boundaries when otherwise authorized. `commit ≠ push` remains binding.

An `ENV-*` derived from Goal authority may be created/refreshed without new user approval only when it is equal to or narrower than current valid parent `AUTH-*`, remains bounded by expiry and prohibited zones, and does not represent a mandatory platform/tool confirmation as waived. `ENV-*` never expands parent Goal authority.

Cross-chat resume uses `PROJECT-BOOTSTRAP.md → 00 → 01 → 03 → 09 → OUT-* / AUTH-* / ACT-* / ENV-*`, then fresh-checks mutable prerequisites before continuing the exact safe next action. Handoff never transfers authority and chat memory never substitutes for current `AUTH-*`.

If one operation is blocked but independent safe Goal work remains, block only that operation and continue the independent authorized work. Move the Goal to `BLOCKED` only when a global blocker prevents all meaningful safe progress. Goal authority never permits silent `REQ-*`, `DEC-*`, accepted-Risk, or architecture changes merely to make completion easier; route those changes through existing governance. Multiple Goals do not resolve by recency; incompatible scopes use explicit change/supersession or existing `CONFLICT-*` handling.

ProjectFramework-level Goal authorization cannot override system/developer instructions, product safety policy, MCP/tool confirmation requirements, authentication/external-system authorization, platform capability limits, or mandatory controls imposed above ProjectFramework. Such controls are reported as platform/tool gates rather than as absence of Project-level Goal authority.

GREENFIELD Framework `1.8.0` starters expose Goal semantics but do not synthesize an active Goal/`OUT-*`/Goal `AUTH-*`. Brownfield upgrade never creates a persistent Goal from old prose, backlog, Handoff, existing Outcomes, or prior “continue” text; persistent Goal authority begins only through explicit `[Goal]` invocation/adoption under the active contract.
#### `[Meeting]`

`[Meeting]` convenes a multi-model **advisory** council for an explicit question. Literal brackets are required and registered-name matching inside them is case-insensitive. Unbracketed meeting/council prose does not invoke the command. The explicit question supplied with `[Meeting]` is the default outbound payload.

ProjectFramework owns the command, disclosure boundary, normalized result, evidence rules, and advisory-authority separation. The council runtime remains an external provider implementation. The verified TASK-024 provider profile is `captainhuke-dev/llm-council` (`master` commit `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131`, observed tree `221d8afb6eca87537282d509971c505119390e0b`) using FastAPI/OpenRouter and Stage 1 independent responses → Stage 2 anonymized peer review/ranking → Stage 3 Chairman synthesis. That snapshot is provider-profile evidence, not immutable Framework truth; material provider/interface drift fails closed for the affected integration. Provider UI, runtime, repository, OpenRouter state, and `data/conversations/*.json` never become Project authority.

Additional Project context beyond the explicit Meeting question MUST be minimum necessary and covered by applicable outbound-disclosure authority. `[Meeting]`, `[Goal]`, `AUTH-*`, `ENV-*`, task scope, local access, or provider availability never imply blanket Project-context disclosure. Actual secret values remain prohibited; `SECRET-*` reference metadata is not permission to reveal a value. Unknown disclosure classification/authority blocks only the affected outbound context when other safe work can continue.

Normalized results preserve, when available, Topic/Question, Context Scope, Provider/Model Provenance, Independent Views, Agreement, Disagreement, Blind Spots/Risks, Peer-Review/Ranking Signal, Chairman/Synthesis, Recommended Interpretation, Limitations/Failed Models/Missing Stages, and an Advisory Authority Notice. Preserve meaningful disagreement rather than manufacture consensus.

Council output remains advisory:

```text
Council Recommendation ≠ User Approval ≠ AUTH-* ≠ DEC-* ≠ REQ-* change ≠ Project mutation permission
```

A majority is not a Decision; ranking is not a truth score; Chairman synthesis is not Project adjudication. Any adopted recommendation routes through the existing canonical owner and required authority.

Meeting execution may report `COMPLETE | PARTIAL | FAILED | UNAVAILABLE` as presentation/workflow labels only. Partial Stage-1 participation remains `PARTIAL`; missing Stage 2 leaves peer ranking incomplete; Chairman failure surfaces `SYNTHESIS_UNAVAILABLE` (or equivalent) and never fabricates consensus; provider/auth/network/runtime failure is provider failure, not council disagreement.

TASK-024 adds no `MEETING-*` family or semantic slot. Exploratory Meetings may remain transient. When materially used, persist minimum reconstructable advisory evidence through existing `EVD-*` / source-native evidence references in `13 Evidence Registry`; provider JSON storage is never canonical Project history.

GREENFIELD does not auto-create a Meeting/conversation/evidence/provider credential/runtime/disclosure authority. Brownfield upgrade does not synthesize Meetings from prior discussion, AI transcripts, backlog, Handoff, `EVD-*`, or provider JSON and does not require provider runtime installation merely to adopt governance semantics.

#### TASK-026 External AI Context & Disclosure Governance

TASK-026 defines one compositional disclosure boundary for Project context sent to external AI/model/provider/tool consumers. Canonical disclosure classes are exactly `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; provider/tool eligibility labels are exactly `ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED`. These are workflow semantics, not new Stable-ID or lifecycle families.

```text
Classification ≠ Authorization
Provider Eligibility ≠ Authority
Disclosure Permission ≠ Decision Authority ≠ Mutation Authority ≠ Binding Authority ≠ Runtime Authority
Secret Reference ≠ Secret Value Disclosure Permission
Unknown ≠ Safe
```

`EXTERNAL_OK` is eligibility under otherwise-valid provider/purpose/minimization/authorization conditions, not permission by itself. `EXTERNAL_REVIEW` requires current bounded disclosure authority. `DO_NOT_DISCLOSE` is excluded from ordinary external-AI workflows. `UNCLASSIFIED` fails closed for automatic protected outbound Project context while independent safe local work may continue. Actual secret values are effectively `DO_NOT_DISCLOSE`; a `SECRET-*` reference never authorizes value disclosure.

Standing disclosure permission reuses `AUTH-*` in `12`: provider/tool or provider class, content/source scope, allowed disclosure classes, purpose, minimum-context/redaction conditions, forbidden content/effects, validity/termination, risk ceiling when applicable, and evidence/approval reference remain bounded. An exact User Explicit Instruction may authorize one sufficiently identified provider/content/purpose disclosure action when otherwise allowed; it does not silently create standing authority or generalize to later calls.

Provider/tool eligibility is evaluated independently of classification and Project authority. Provider availability/model capability never proves eligibility. `VERIFICATION_REQUIRED` or `INELIGIBLE` blocks protected outbound context; provider identity/policy drift invalidates the affected provider-scoped basis until re-resolved.

Every external-AI consumer follows: identify purpose/provider → identify candidate context → classify each portion → remove secrets/`DO_NOT_DISCLOSE` → minimize → redact/generalize only when sufficient → resolve provider eligibility → resolve `AUTH-*` or exact one-off basis → partition mixed sensitivity → send only authorized + eligible subset → surface material omissions → persist `EVD-*` only when governance-relevant. Whole-repository/Project export is exceptional exact scope, never the convenience default.

Mixed-sensitivity context is partitioned, not promoted wholesale. Redaction uncertainty fails closed for the affected portion and must not leak through metadata, filenames, hashes, examples, attachments, prompts, or logs. If omitted context makes the external task materially misleading or unusable, fail closed rather than silently expanding disclosure.

Material disclosure evidence uses minimum reconstructable `EVD-*` / source-native pointers: consumer, purpose, provider/tool, eligibility evidence, bounded source/context scope, disclosure classes, authorization basis, minimization/redaction, blocked portions when material, result pointer, and epistemic status. Do not duplicate full sensitive payload merely for audit.

`[Meeting]` extra Project context routes through this boundary while the explicit user-supplied Meeting question remains its default action-specific input. Project Knowledge advisory status, OpenViking/`REL-*` visibility, `[Goal]`, `ENV-*`, Tool/MCP access, model capability, repository/workspace access, and provider availability never create or transfer disclosure authority. Cross-Project disclosure is evaluated under each source Project.

GREENFIELD creates no standing disclosure `AUTH-*`, provider eligibility grant, provider credential/account, redaction runtime, disclosure log, or blanket `EXTERNAL_OK`. Brownfield does not mass-classify historical content safe, synthesize disclosure authority from prior AI use/Meeting/Goal/chats/credentials, migrate actual secret values into Project Source/Evidence, or assume prior provider integrations are eligible.

TASK-026 remains documentation/governance-only: no `DISC-*` family/slot, runtime redactor, provider router/proxy, MCP disclosure gateway, interception layer, secret manager, DLP scanner, classification database, watcher/crawler, automatic outbound call, credential provisioning, or CI/CD/deployment automation is introduced.


### GREENFIELD

If environment is a ChatGPT Project or Claude Project, begin with the matching canonical platform Project instruction artifact. If no valid local Project Source exists, bootstrap from canonical repository `main` using:

```text
README.md
→ FRAMEWORK-RELEASE.yaml
→ SKILL.md
→ latest amendment
→ Core Governance
→ Framework template
→ skeletons
→ mockup
```

Then Discover → identity → adaptive interview → Preview → user approval → create governance layer → validate → readiness → completion report.

Because GREENFIELD has no active local `FRAMEWORK-001`, Project Location Binding uses a pre-binding exception:

```text
canonical Framework bootstrap read
→ read-only discovery/inspection of candidate GitHub/Drive locations when needed
→ Preview proposed GitHub/Drive binding state + durable identity
→ explicit user approval
→ first Material Project-Source write creates active 00 / FRAMEWORK-001 with approved binding
→ subsequent Material connector work resolves the active binding
```

The Preview MUST classify each applicable system as `BOUND`, `NOT_APPLICABLE`, or `VERIFICATION_REQUIRED`. Insufficient routing identity remains `VERIFICATION_REQUIRED`; never invent repository identity, Drive folder/file ID, or canonical URL merely to complete the bootstrap. Material mutation through an unresolved system remains fail-closed.

Create mandatory `00–05` and `09–17`; evaluate conditional `06–08`, `40`, `60`, `91`, and `92` by applicability. Keep `18–19` reserved. Do not create empty conditional files merely to look complete.

Exact Git tag/SHA provenance is optional assurance. If observed, record accurately; if unavailable, do not fabricate it and do not block otherwise valid bootstrap solely for that reason. If canonical Framework source itself is inaccessible, stop affected governance mutation instead of reconstructing Framework rules from memory.

### BROWNFIELD

Preserve first. Inventory and classify legacy sources by Truth Domain, Epistemic Status, Freshness, and evidence. Do not move/rename/delete legacy sources automatically. Build governance layer and normalize only approved scope.

### IMPORT

Place imported Project Source in `import-staging/` first. Assess identity, versions, compatibility, Manifest, hashes, mandatory docs, lineage, IDs, secret leakage, references, and active-revision ambiguity. Results: `COMPATIBLE`, `UPGRADE_REQUIRED`, `CONFLICTED`, `INVALID`.

## 18. Migration and Versioning

Each Project pins Framework/Schema version and compatibility range. Never auto-upgrade old Projects.

Managed migration uses `MIG-*` and covers source, target, compatibility assessment, affected documents/objects, steps, rollback, approval, validation, and evidence. Project-Specific Rules are preserved unless explicitly resolved otherwise.

### 18.1 Framework 1.3 Direct-to-Latest / Cumulative Target-State Upgrade

Framework `1.3.0` changes default upgrade **execution architecture** while preserving migration safety and history. The governing invariant is: **upgrade cost SHOULD scale with the affected semantic difference between current reconstructable Project state and the approved target Framework, not with the number of releases skipped.**

For an initialized Project, resolve the active locally pinned current state and compare it directly with an explicitly selected target Framework. Historical amendments/releases remain provenance/rationale and existing `MIG-*`/Git/history remain preserved; they are not mandatory sequential execution steps merely because their versions existed.

```text
resolve active current Project/local pin
→ materialize current reconstructable truth
→ resolve explicitly selected target Framework
→ compare current state directly with target required semantics
→ classify cumulative semantic delta
→ choose upgrade path
→ Preview cumulative delta + preservation + rollback
→ explicit approval
→ apply only required current→target changes
→ affected/risk-scoped verification
→ RELEASE_FULL once on final unchanged target candidate
→ promote target Framework revision and preserve superseded/history state
```

Cumulative assessment MAY label target semantics `ALREADY_SATISFIED | REQUIRED | NOT_APPLICABLE | VERIFICATION_REQUIRED | CONFLICT_REVIEW`; these are migration-assessment labels only, not new lifecycle/Epistemic/authority states.

Direct-upgrade path classes are exactly:

```text
FAST_PATH
ASSESSED_PATH
MAJOR_MIGRATION_REQUIRED
```

- `FAST_PATH` — current truth is reconstructable and compatible; target delta is bounded with no material unresolved conflict.
- `ASSESSED_PATH` — one cumulative `MIG-*` assessment/plan is required, but safe current→target migration does not require replaying each intermediate release.
- `MAJOR_MIGRATION_REQUIRED` — breaking schema/namespace/root semantics, non-reconstructable current truth, or material unresolved conflicts/unknowns prevent safe bounded direct migration.

Skipping intermediate **execution** never skips compatibility assessment, authority, Preview/approval, reversibility/rollback, validation, evidence, promotion, Stable-ID/current-truth preservation, Project-Specific Rules, bindings, or history. The maintained starter is the target representation for NEW Projects, not a default destructive rebuild path for initialized Projects. Full reconstruction requires an explicitly approved `MAJOR_MIGRATION_REQUIRED` preservation/mapping plan.

Reuse Progressive / Risk-Scoped Verification: affected checks during migration, `CHECKPOINT_INTEGRITY` at logical checkpoints, one `RELEASE_FULL` on the final unchanged candidate, then `INTEGRATION_GATE` for Base Freshness/evidence validity. Do not run `RELEASE_FULL` once per skipped historical release.

### 18.2 Framework 1.2.0 Slot-91 Migration Safety

Framework releases before `1.2.0` allowed `90–99` as Project-specific/Governance Extension space. A Brownfield Project may already use slot `91` for a custom document.

Migration MUST NOT overwrite it. Required flow:

```text
detect occupied 91
→ open MIG-* compatibility assessment
→ preserve custom document identity/history/references
→ propose suitable free 93–99 or other semantically correct location
→ obtain explicit approval
→ migrate/promote/archive through governed flow
→ only then activate standard 91 if applicable
```

Existing Projects that do not migrate remain unaffected.

### 18.3 No Automatic Free-Text Promotion

Existing prose mentioning risks, assumptions, dates, dependencies, scope changes, outcomes, or gates MUST NOT be automatically reinterpreted as new `RISK-*`, `ASM-*`, `MS-*`, `OUT-*`, `DEP-*`, `CR-*`, or `GATE-*` identities.

Promotion requires enough current semantics, status, ownership, and epistemic/evidence state to avoid fabrication. If identity/current truth cannot be established, preserve prose as historical/current context with explicit uncertainty rather than inventing a Stable ID.

### 18.4 Framework Operational Use and Optional Release Assurance

Treat Framework state as independent dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

A Framework MAY be operationally usable while exact Git provenance is `UNKNOWN/UNVERIFIED` or repository hardening is absent. These optional assurance states MUST NOT become blockers unless Project-Specific Rules explicitly require them.

When exact source provenance is actually observed, a Project may record:

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "<OBSERVED_REF_OR_MAIN>"
  release_tag: "<OPTIONAL_OBSERVED_TAG_OR_NONE>"
  resolved_commit_sha: "<OPTIONAL_OBSERVED_SHA_OR_UNKNOWN>"
  framework_version: "<PINNED_FRAMEWORK_VERSION>"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
  provenance_status: "<VERIFIED | PARTIAL | UNVERIFIED>"
```

Exact tag/SHA values come only from actual observation; never predict, fabricate, or retroactively backfill them.

### 18.5 Git Work Base Freshness and Forward-Port

เมื่อ Project ใช้ Git branch/worktree สำหรับงานที่ต้อง integrate กลับ canonical target ให้แยก **Git mergeability** ออกจาก **semantic acceptability**. Branch ที่ merge/rebase แบบไม่มี textual conflict ยังอาจใช้ Framework, authority, Requirements, routing หรือ contract รุ่นเก่าอยู่ได้.

Canonical terms:

- **Canonical Integration Target** — integration branch/ref ที่ verify แล้วว่าเป็น target ปัจจุบันของ Project; สำหรับ ProjectFramework คือ repository `main` (`origin/main` ใน local Git terminology).
- **Base Snapshot** — observed repository, target ref, base commit SHA, applicable Framework/Schema version และ captured time เมื่อข้อมูลเหล่านี้ material ต่อการ integrate.
- **Independent Work** — งานที่ไม่ต้องพึ่ง unmerged feature state อื่น.
- **STACKED_WORK** — feature-on-feature dependency ที่ตั้งใจและเปิดเผย parent ref/commit, dependency reason, invalidation condition และ expected integration order.
- **FRESH / STALE_NON_SEMANTIC / STALE_SEMANTIC / UNKNOWN** — Base Freshness vocabulary.
- **BASE_STALE** — workflow condition ของ work package; ไม่ใช่ Project Lifecycle/Execution state, Epistemic Status หรือ Stable-ID family ใหม่.
- **REBASE_REQUIRED** — disposition สำหรับ private/rewritable work เมื่อ drift เป็น non-semantic และ replay บน current target เหมาะสม; shared/public branch ใช้ history-preserving merge/update ได้แทน.
- **FORWARD_PORT_REQUIRED** — disposition เมื่อ semantic base เปลี่ยนจนงานเก่าต้อง re-evaluate กับ current target ก่อน integrate.

Binding behavior:

1. ก่อนสร้าง branch/worktree ใหม่ที่เป็น **Independent Work** ต้อง fresh-read/fetch Canonical Integration Target และสร้างงานจาก current observed target; ห้าม inherit จาก feature branch ที่บังเอิญ checkout อยู่โดย default. Local branch ชื่อ `main` ไม่ได้ prove ว่า current.
2. Feature-on-feature ancestry อนุญาตเฉพาะ explicit `STACKED_WORK`. Parent change ที่ material ต้อง trigger child base re-evaluation; parent merge/closure ไม่ได้ prove ว่า child fresh โดยอัตโนมัติ.
3. Base Freshness ต้องตรวจอย่างน้อยก่อนสร้าง independent work, ก่อนเริ่ม material implementation phase ใหม่เมื่อ upstream อาจขยับ, ก่อนเปิด/อัปเดต integration PR ที่ base อาจ stale, และ immediately before acceptance/merge เมื่อ target head เปลี่ยนหลัง review.
4. Commit count ไม่ใช่ semantic-staleness threshold. Classification ต้องดู impact ต่อ Framework/governance/schema/authority/Requirements/Decisions/interfaces/technical-deployment contracts/source-of-truth assumptions ที่งานพึ่งพา.
5. `STALE_NON_SEMANTIC` ใช้เมื่อ upstream change ไม่เปลี่ยน material assumption/contract ของงาน. ให้ mark `BASE_STALE` จนกว่า base จะถูก update ด้วยวิธีที่เหมาะสมและ affected verification จะผ่าน. Private/rewritable work อาจใช้ `REBASE_REQUIRED`; shared/public work ต้องรักษา published history ด้วย merge/update strategy ที่เหมาะสม. หลัง update + verification สำเร็จจึงกลับ `FRESH`.
6. `STALE_SEMANTIC` ใช้เมื่อ upstream เปลี่ยน applicable Framework/Root Governance/Schema/authority/routing/Requirements/Decisions/interfaces หรือ contract ที่งานพึ่งพา. ให้ mark `BASE_STALE`, หยุด affected new implementation scope, assess changed assumptions และใช้ `FORWARD_PORT_REQUIRED` โดย default.
7. Forward-Port ต้องเริ่ม clean branch/worktree จาก current Canonical Integration Target, treat stale branch เป็น source material/evidence ไม่ใช่ authority, แล้ว carry เฉพาะ still-valid accepted changes. Cherry-pick ได้เมื่อ commit boundary สะอาด; ถ้าไม่สะอาดให้ re-implement accepted intent บน current base.
8. Forward-Port ต้อง exclude temporary staging/transport artifacts, obsolete workflow, old version metadata, superseded assumptions และ unrelated experimental history ที่ไม่ใช่ current deliverable.
9. Large/old/experimental/stacked/semantically-drifted work ควร integrate ผ่าน clean integration branch จาก current target แล้ว validate current deliverable ก่อน PR/merge.
10. Pre-Merge Base Freshness Gate ต้อง re-resolve current target head และ classify `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`. `UNKNOWN`, unresolved semantic drift หรือ target movement ที่ material ต้อง block affected acceptance จน re-evaluated.
11. `git conflict = 0`, `mergeable = true`, successful rebase หรือ clean textual diff ไม่ override Base Freshness Gate. **Mergeable ≠ Acceptable.**
12. หาก Base Staleness กลายเป็น material Project truth ให้ใช้ object เดิมตาม semantics: `DRIFT-*` สำหรับ truth-domain misalignment, `CONFLICT-*` สำหรับ competing semantic states, `MIG-*` สำหรับ pinned Framework/Schema migration และ `CR-*` สำหรับ material governed change. ห้ามสร้าง parallel Stable-ID family เพียงเพื่อ Git base freshness.
13. Existing initialized Projects ยังคงใช้ local pinned `FRAMEWORK-001`; upstream Framework movement ไม่ auto-upgrade Project. กติกานี้ govern work-package integration; local Framework upgrade ยังใช้ `MIG-*` + assessment + approval + validation.
14. Framework กำหนด semantics เท่านั้น. ห้าม infer authorization ให้สร้าง Git hook, bot, GitHub Actions, validator, scheduler, merge queue หรือ branch-protection automation จากกติกานี้.

เมื่อ material สามารถบันทึก Base Snapshot / gate state ได้ เช่น:

```yaml
base_freshness_gate:
  target_ref: "<VERIFIED_CURRENT_TARGET>"
  target_head_sha: "<OBSERVED_SHA>"
  reviewed_feature_base_sha: "<OBSERVED_BASE_SHA>"
  freshness: "FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN"
  semantic_base_changed: true|false|unknown
  disposition: "ACCEPT | UPDATE_BASE | REBASE_REQUIRED | FORWARD_PORT_REQUIRED | BLOCK"
```

ค่า ref/SHA/version ต้องมาจาก observation เท่านั้น; ห้าม fabricate เพื่อให้ record ดู complete.

### 18.5 Framework 1.2.5 Integration Gate and Evidence Reuse

Immediately before integration, **INTEGRATION_GATE** re-resolves the current Canonical Integration Target, applies existing Framework `1.2.2` Base Freshness classification, and checks whether prior Task/Release verification evidence is still valid. Unchanged candidate + unchanged material assumptions MAY reuse fresh `RELEASE_FULL` evidence. Non-semantic target movement triggers only freshness/affected rechecks when it does not invalidate candidate assumptions. Candidate/tree change, semantic/unknown movement, conflict resolution, rebase result, merge-time edits, or unbounded impact invalidates affected/full evidence as required.

Exact fast-forward to an already verified candidate tree normally requires resulting-state confirmation (target/remote HEAD or tree identity and clean/understood workspace/shared state) rather than unconditional `RELEASE_FULL` rerun. `Mergeable ≠ Acceptable` remains binding.

### 18.6 Framework 1.2.4 Project Location Binding Migration

Existing initialized Projects do not auto-upgrade to Framework `1.2.4`. A governed migration MUST preserve the active prior `FRAMEWORK-001` until approval/promotion completes and MUST NOT invent Project locations.

Migration behavior:

1. Inventory actual Project sources and user-confirmed context for GitHub/Drive locations.
2. Classify GitHub and Drive independently as `BOUND`, `NOT_APPLICABLE`, or `VERIFICATION_REQUIRED`.
3. Require GitHub owner/repository or canonical repository URL before treating GitHub as `BOUND`; require Drive project-root folder ID or canonical folder URL before treating Drive as `BOUND`.
4. Record only observed/user-confirmed identities. Display names/paths remain descriptive and do not substitute for durable routing identity.
5. Do not create or migrate a `canonical_branch` field; preserve Framework `1.2.2` Canonical Integration Target semantics separately.
6. Preserve Canonical Implementation Source semantics independently.
7. Revise `FRAMEWORK-001` only through User Explicit Approval plus governed revision/validate/promote/supersede/archive flow.
8. Update continuation documents to reference the root binding rather than create a competing authoritative repository/folder copy.
9. Validate fail-closed behavior and Project Source integrity after promotion.

A Project that does not use a connector may mark it `NOT_APPLICABLE`; a Project that materially relies on a connector but cannot resolve durable routing identity remains `VERIFICATION_REQUIRED` for affected Material mutation.

### 18.7 Framework 1.2.5 Agent Continuity / Local Workspace Migration

Existing initialized Projects do not auto-upgrade. Migration to `1.2.5` MUST NOT invent local filesystem paths, environment-scope identity, completion-commit provenance, verification evidence, repository origins, or MCP workspace identifiers. For an applicable local environment: verified/user-confirmed path → `BOUND`; local execution applicable but unresolved → `VERIFICATION_REQUIRED`; local execution outside declared scope → `NOT_APPLICABLE`. Preserve Repository Location Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, and Runtime Location as distinct semantics.

### 18.8 Framework 1.6.0 Slot-92 Project Graph Migration Safety

Framework releases before `1.6.0` allowed slot `92` inside Project-specific/Governance Extension space. A Brownfield Project may therefore already use `92` for a custom document.

Migration MUST NOT overwrite it. Required flow:

```text
detect occupied custom 92
→ open/route MIG-* compatibility assessment
→ preserve custom document identity/history/references/current semantics
→ propose suitable free 93–99 or another semantically correct location
→ obtain the approval required by existing migration/root-governance rules
→ migrate/promote/archive through governed flow
→ only then activate standard 92 Project Graph if applicable
```

Migration does not invent `REL-*`, reciprocal assertions, relation applicability, OpenViking configuration, or relation evidence. Existing Projects that do not migrate remain unaffected.

## 19. Project Health and Review Cadence

Project Health is a **derived current assessment** in `03 Current State`, not a replacement for canonical records.

Standard dimensions:

```text
Scope
Progress / Schedule
Risk
Quality / Validation
Dependencies
Authority
Knowledge
Readiness
Technical / Deployment when applicable
```

States:

```text
GREEN AMBER RED UNKNOWN
```

Omit a non-applicable optional dimension rather than marking it `GREEN`. Each applicable dimension records/resolves:

```text
State
Reason
Supporting Stable IDs / Evidence
Owner
Last Reviewed
Next Review / Trigger when applicable
```

Framework defines no opaque automatic weighted health score. A Project-specific aggregate label may exist only if derivation/limitations are explicit and it does not replace dimensional view.

Review Cadence supports:

```text
TIME_BASED
EVENT_BASED
```

It may govern Current State Review, Risk Review, Assumption Review, Milestone/Outcome Review, Decision Revalidation, Technical Design Review, Deployment Readiness Review, and Handoff Refresh. ProjectFramework defines semantics only and does not create a scheduler/reminder runtime.

## 20. Decision Revalidation

`DEC-*` remains canonical in `04 Decision Log`. Current Decisions may record:

```text
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
```

Recommended statuses:

```text
NOT_DUE REVIEW_DUE REVALIDATED SUPERSEDED
```

Typical triggers include invalidated `ASM-*`, materially changed `DEP-*`, Requirement change, Tech Stack change, deployment-mode change, material approved `CR-*`, regulation/vendor-contract change, review date, or runtime evidence contradicting Decision basis.

A previously approved Decision is not assumed valid forever when its stated basis no longer holds.

## 21. Technical Design and Deployment Blueprint

### 21.1 `06 Architecture` vs `40 Technical Design`

`06 Architecture` remains the conditional major architecture view: major systems/components/interfaces, boundaries, data flow, constraints, and key architecture Decisions.

`40 Technical Design` is the deeper implementation-facing **blueprint** when meaningful software/technical detail exists. It deepens/references `06`; it must not fork the same authoritative payload.

A material Tech Stack entry records:

```text
Technology
Role / Responsibility
Version or Supported Range
Required / Optional
Why Used / Decision Reference
Used By Component(s)
Operational Dependency
Lifecycle / Support Constraint when material
Replacement Boundary when material
Epistemic / Verification State
```

`40` may also document Component Responsibility, Inputs/Outputs, Interfaces, Dependencies, Data/Storage interaction, Security/Authority boundaries, Runtime boundaries, source-structure responsibilities, Development Workspace Contract, Configuration Contract, and Runtime Requirements.

#### 21.1.1 Development Workspace Contract

When software development is material and workspace/runtime ambiguity could affect correctness, recovery, testing, deployment, or Agent operation, `40` SHOULD identify:

```text
Canonical Implementation Source
Repository / Source Identity when applicable
Development Workspace Type
Workspace Location / Boundary
Workspace Durability
Human / Agent Edit Location
Execution Environment
Source-to-Runtime Mapping
Dependency Isolation Strategy
Runtime Mutability Boundary
Persistent-State Boundary
Related REQ / DEC / RISK / ASM / DEP / CR / EVD
Verification / Drift Notes
```

Common descriptive workspace types MAY include `LOCAL_WORKSPACE`, `GIT_WORKTREE`, `REMOTE_DURABLE_WORKSPACE`, `DEV_CONTAINER_DURABLE_WORKSPACE`, and `OTHER_DECLARED_WORKSPACE`. Common mapping descriptions MAY include `DIRECT_EXECUTION`, `BIND_MOUNT`, `WORKSPACE_VOLUME`, `IMAGE_OR_ARTIFACT_BUILD`, `REMOTE_SYNC`, and `OTHER_DECLARED_MAPPING`. These are blueprint vocabulary only; they are not Project states or Stable-ID families.

A Project MAY use different source-to-runtime mappings for development, test/integration, staging, and production. Differences must remain compatible with applicable Requirements/Decisions and declared Technical/Deployment contracts.

Configuration semantics are independent from packaging mode and may include Application Settings, Environment-specific Settings, External Service Endpoints, Persistence Settings, Feature/Capability Settings, and Secret References. Actual secret values remain forbidden.

### 21.2 Deployment Support Model

A software Project declares one of:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

For `SOURCE_AND_DOCKER`, Source and Docker share one declared contract for:

```text
core application semantics
configuration meaning
required external dependencies
data compatibility
security assumptions
supported capability set
persistence semantics
upgrade compatibility
```

Packaging/runtime mechanics may differ. Intentional differences use **Deployment Mode Variance** with Affected Capability, Source Behavior, Docker Behavior, Reason, Impact, related Stable IDs, Owner, and Acceptance/Resolution State. Unexpected mismatch is `DRIFT-*`.

### 21.3 `07 Implementation Plan` vs `60 Deployment Plan`

`07 Implementation Plan` answers what work/actions are planned, sequence, dependencies, risks, verification, and rollback/reversibility.

`60 Deployment Plan` answers how the resulting system is installed, configured, started, stopped, verified, diagnosed, upgraded, rolled back, backed up/restored, cleaned up, and troubleshot in each supported deployment mode.

When applicable, `60` addresses:

```text
Prerequisites
Supported OS / Platform / Architecture
Deployment Source / Artifact Acquisition
Required Runtime / Container Runtime
External Services
Required Permissions
Configuration Inputs
Secret Requirements / SECRET-* references
Source-to-Runtime Mapping for the supported mode
Runtime Mutability Expectation
Persistent-State Boundary
Data / Storage Authority
Replacement / Recreation Expectation
Development-only vs Production Mapping Differences
Data / Storage Initialization
Installation / Initialization Procedure
Start / Stop Procedure
Verification / Health Check
Logs / Diagnostics
Upgrade
Rollback
Backup / Restore
Uninstall / Cleanup
Troubleshooting
Known Limitations / Deployment Mode Variance
```

Installation is not operationally ready merely because an install/start command returns success. Verification may include service availability, dependency reachability, storage initialization/persistence, configuration loading, secret resolution without exposure, health/runtime signal, core flow usability, running version identity, Source/Docker parity when applicable, and survival of state that the declared replacement/recreation lifecycle requires.

## 22. Framework Integrity Contract

Current Framework distribution integrity means at minimum:

- current Framework/Schema declarations are internally consistent;
- `00–17` meanings remain intact;
- `06–08` remain conditional;
- `18–19` remain reserved;
- `40`, `60`, `91`, and `92` remain conditional/applicability-driven;
- `91` is standard Project Management Control in `1.2.0+`, `92` is standard Project Graph in `1.6.0+`, and `93–99` remain extension space unless governed otherwise;
- current `REL-*` records resolve from active `92` without archive dependency and use immutable `project_uuid` endpoints;
- AI-ControlTower/OpenViking indexing remains derived/rebuildable and never replaces Project Source authority;
- Project relation topology remains distinct from repository/storage/local-workspace/integration/implementation/runtime authority;
- canonical object homes remain consistent across Framework, Core Governance, skeletons, `templates/project-source-mockup/`, and platform launchers;
- `templates/project-source-mockup/` is the single maintained concrete starter representation in the current distribution; a second full Project Source example/template tree is not maintained alongside it;
- ChatGPT and Claude shared governance contracts remain byte-identical;
- current Stable IDs resolve without archive dependency;
- existing Projects do not silently auto-upgrade;
- actual secrets remain forbidden;
- technical planning does not silently expand into implementation artifacts;
- Canonical Implementation Source and Runtime Truth remain distinct when the distinction is material;
- required-survival state has a persistence contract compatible with declared runtime replacement/recreation;
- Project Location Binding authority is held in active local `FRAMEWORK-001` for initialized Projects and is not inferred from chat memory, recency, ranking, or another accessible Project;
- `VERIFICATION_REQUIRED` and `NOT_APPLICABLE` fail closed for affected Material connector mutation, while `BOUND` has sufficient durable routing identity;
- Project Location Binding does not create a competing `canonical_branch`, Canonical Integration Target, or Canonical Implementation Source;
- persistent Project Location Binding changes require User Explicit Approval and governed Root Governance revision/promotion;
- `ไม่มีขั้นตอนถัดไป` pairs with `START_NEW_CHAT`, while `CONTINUE_CURRENT_CHAT` and `PERSISTENCE_PENDING` require a concrete Next Action consistent with the persistence gate;
- the mandatory response close preserves the two-heading structure and bracketed `[Next Action] / [Chat] / [Reason] / [Required Read]` fields;
- missing facts, authority, source, provenance, routing identity, or management-object identity are never fabricated.

These are semantic requirements and may be reviewed manually or by an Agent. They do not require executable enforcement tooling.

## 23. Export Profiles

```text
CURRENT — active continuation snapshot; includes current canonical records and required active/current Detail Documents without archive dependency
AUDIT   — current + relevant history/evidence
FULL    — complete Project-Source including archive, excluding actual secrets
```

Package name:

```text
<Project-ID>-Project-Source-<PROFILE>-YYMMDD-HHMM.zip
```

If active `40`, `60`, `91`, or `92` is needed to interpret current truth, it belongs in `CURRENT`. A `CURRENT` export is incomplete if omitted archive content is required to determine current semantics.

## 24. Retention and Readiness

Preserve Project Source revisions, Decisions, Requirements, Change Log, management-control history, and Identity lineage indefinitely by default. Evidence follows Project-Specific retention. Purge requires authorization, no active references, auditability, and retained reconstructability.

A Project Source may be `VALID + NOT_OPERATIONALLY_READY` when uncertainty is explicit. It is `OPERATIONALLY_READY` only when a new actor can determine current truth, current authority, active blockers, and exact next action without guessing.

Optional immutable-tag/SHA provenance or repository protection does not change readiness automatically unless Project-Specific Rules make it a requirement.

## 25. Interview Policy

Modes:

```text
FAST GRILL ADAPTIVE
```

Default = `ADAPTIVE`.

```text
Can verify?              → VERIFY
Can safely derive?       → INFERRED
Non-critical unknown?    → RECORD UNKNOWN
Semantic decision?       → ASK USER
Authority required?      → RESOLVE / ASK
Dangerous ambiguity?     → BLOCK AFFECTED SCOPE
```

Do not ask for information available from accessible Project sources. Do not fabricate information to reduce questions.

## 26. Initial Creation / Structural Migration Gate

Before first creation or major structural migration, show a preview containing at least Adoption Mode, Project Identity, files/directories to create, conditional files, known Decisions, known Assumptions, Unknowns, expected readiness, expected risk, and migration impact. Obtain explicit user approval before writing.

## 27. Completion Report

After Create, Migrate, Import, Major Update, Handoff, or Export, report human-readable and machine-readable results. Include Project identity, operation, adoption mode, versions, validation/readiness, created/revised/archived docs, active ACT/ISS/DRIFT/CONFLICT and relevant management controls, authority state, unknown/stale/verification-required items, export artifact if any, and exact next action.

Canonical completion states:

```text
COMPLETE PARTIAL BLOCKED FAILED
```

Do not claim `DONE`, `DEPLOYED`, `PUSHED`, `MIGRATED`, or `VALID` unless verification appropriate to the risk has passed.

## Framework 1.12.0 Set 1 Foundation Contracts

### Task Dependency & Portfolio Planning (TASK-033)

Development/backlog Task sequencing uses explicit Task-source planning metadata when applicable:

```text
depends_on
blocks
enables
parallelizable_with
priority: CRITICAL | HIGH | NORMAL | LOW | UNSET
readiness: READY | WAITING | BLOCKED | UNKNOWN
```

`Task dependency metadata ≠ Project-management DEP-* objects`; `Task readiness ≠ Task lifecycle status`; `Recommended order ≠ execution authority`; Task number/proximity never establishes dependency evidence.

`READY` means declared required Task dependencies are satisfied and no known blocker prevents start. `WAITING` means an explicit sequencing prerequisite remains. `BLOCKED` means a material blocker prevents work. `UNKNOWN` means dependency/readiness evidence is unresolved, contradictory, cyclic, stale, or references unknown Tasks. A Task may be `TODO + READY`; `READY` never means `DONE`.

Priority is advisory after dependency/safety constraints and never bypasses `depends_on`, authority, binding, Risk, review, or user decisions. Validation surfaces self-dependency, cycles, unknown references, stale/superseded targets, contradictory `parallelizable_with`, and unsupported READY claims; it never auto-repairs the graph.

`DEP-*` in `91` remains the canonical Project-management dependency object family and is never synthesized merely from Task planning edges. Agents may present recommended ordering/parallel groups, but TASK-033 creates no scheduler, queue daemon, automatic task executor, or agent orchestrator.

### Project Tool / MCP Execution Profile (TASK-027)

When applicable, Framework `1.12.0` supports optional `<Project-Root>/Project-Execution/` outside Project Source semantic slots. TASK-027 owns the initial `Project-Execution/README.md` and `tools.md` contract.

```text
Tool selection policy ≠ Tool availability ≠ Location ≠ Authority
Tool/MCP profile ≠ permission to mutate
```

`tools.md` declares `primary_tool` (`PRIMARY`), `allowed_tools`, `disallowed_tools`, `fallback_mode: NONE | ORDERED_ALLOW_LIST`, deterministic `fallback_order`, and `failure_policy: FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY`. `disallowed_tools` wins. `NONE` permits no automatic substitute. `ORDERED_ALLOW_LIST` never expands from recency/ranking/connected status.

Execution resolution is Project authority/location/binding → applicable tool profile → action/tool eligibility → availability/authentication/bound-target verification → PRIMARY or declared fallback → ordinary AUTH/Risk/shared-state/platform gates. An allowed tool cannot override a wrong/unverified Project target; a correctly connected but disallowed tool is not eligible.

`READ_ONLY_DIAGNOSTIC_ONLY` permits only bounded read-only diagnosis needed to explain or repair availability/identity; it never permits Material mutation through an undeclared substitute. Unavailable, unauthenticated, stale, renamed, or target-unverified tools use the declared fallback/failure policy and `VERIFICATION_REQUIRED` where identity cannot be proven.

`PROJECT-BOOTSTRAP.md` resolves active Project authority first; it does not embed full tool policy. `01`/task routing may point to `Project-Execution/tools.md` after authority resolves. The profile stores no credentials/secret values and creates no MCP router, automatic failover, `.lnwjud` mutation, daemon, vendor tool routing, or authority.

GREENFIELD/Brownfield adoption is applicability-driven and governed; prior tool use/vendor settings never auto-create restrictive/permissive policy.

### Agent / Model Capability Profile (TASK-034)

Framework `1.12.0` extends optional `Project-Execution/` with `capabilities.md`. Canonical capability classes are `REASONING | CODING | RESEARCH | REVIEW | COUNCIL`; execution-time capability availability is `FULL | DEGRADED | UNAVAILABLE | UNKNOWN`.

```text
Capability ≠ Authority
Capability eligibility ≠ Tool eligibility
Provider availability ≠ Disclosure permission
Model quality/ranking ≠ Project truth
```

A capability profile declares work-class `required_capabilities`, `preferred_capabilities`, `provider_scope: LOCAL_ONLY | LOCAL_OR_EXTERNAL | EXTERNAL_ALLOWED`, `independent_review: REQUIRED | OPTIONAL | NOT_REQUIRED`, `tool_profile_ref`, and `failure_mode: FAIL_CLOSED | DEGRADED_ALLOWED`.

`DEGRADED_ALLOWED` permits only the genuinely supported bounded subset; required review, Risk, authority, trust, tool, and disclosure gates remain. `UNKNOWN` fails closed for materially sensitive capability requirements. An allowed tool never proves model capability, and a capable model is not executable without an eligible tool path.

External provider use continues through TASK-026 disclosure/provider eligibility/minimization/redaction/secret rules. `[Meeting]` remains TASK-024 advisory behavior even when a `MEETING_COUNCIL` work class requires `COUNCIL + REASONING`.

`independent_review: REQUIRED` keeps a completion/integration gate until an eligible reviewer distinct from the primary producing instance is observed where practicable. Reviewer capability, availability, and independence are never fabricated; an allowed user waiver is action-specific evidence rather than a silent standing-profile rewrite.

The profile is optional/applicability-driven for GREENFIELD/Brownfield and adds no model router, provider API integration, benchmark runner, automatic delegation, council runtime, or permission engine.

### Project Release / Publication Contract (TASK-035)

Framework `1.12.0` reports publication truth through orthogonal dimensions rather than one linear lifecycle.

```text
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
Implementation authority ≠ publication authority
Release evidence ≠ deployment evidence
```

When material, dimensions are:

```text
Implementation: NOT_DONE | DONE
Integration: NOT_APPLICABLE | NOT_MERGED | MERGED
Repository Publication: NOT_APPLICABLE | NOT_PUSHED | PUSHED
Release: NOT_APPLICABLE | NOT_RELEASED | RELEASED
Artifact Publication: NOT_APPLICABLE | NOT_PUBLISHED | PUBLISHED
Deployment: NOT_APPLICABLE | NOT_DEPLOYED | DEPLOYED
```

These values create no new Stable-ID family. `PUSHED` does not imply `MERGED`; `MERGED` does not imply `RELEASED`; release/artifact/deployment truth stays independent.

A material Release Candidate is evidence-bound to source/repository identity, candidate commit/ref for Git-backed work, candidate tree/content digest when material, version/release identifier, schema compatibility where applicable, verification evidence, and material assumptions. Candidate/source/tree/material-assumption change invalidates prior evidence selectively under progressive verification rules; exact Git/tag provenance is never fabricated.

`RELEASE_FULL` verifies the candidate/distribution and performs no shared-state publication. `INTEGRATION_GATE` immediately precedes integration/publication dependent on a mutable target and re-resolves Base Freshness/evidence validity. Exact verified transport may use resulting-state confirmation without unconditional full rerun when candidate evidence remains valid.

Local implementation/commit authority never implies push; push never implies merge; merge never implies release/artifact publication; release never implies deployment. `[Goal]` includes publication only when explicitly scoped; `commit ≠ push` remains binding.

Material facts reuse `10`/`13 EVD-*`/`03`/`09`/`15`/`91` as applicable. Repository-native releases/tags/registries/deployments are source-native evidence, not Project authority by themselves.

Partial publication reports each dimension. External success followed by failed required local reconciliation uses `PERSISTENCE_PENDING` while retaining the observed external truth. Rollback, retraction, and supersession preserve history; unsupported retraction is recorded rather than fabricated. Immutable tags/signatures/checksums/attestations/protected branches are optional assurance unless Project requirements make them mandatory.

TASK-035 creates no CI/CD, release bot, tag/package publisher, deployment automation, or remote push.

### Security & Trust Boundary Contract (TASK-037)

Framework `1.12.0` completes optional `Project-Execution/` with `trust.md` and canonical trust classes `TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN`.

```text
Trust classification ≠ Authority
Trusted surface ≠ permission to disclose secrets
Tool eligibility ≠ trust equivalence
Capability ≠ trust ≠ authority
UNKNOWN trust for materially sensitive action → VERIFICATION_REQUIRED / fail closed
```

`trust.md` declares surface type, trust class, source-native pointer, allowed crossings, and review trigger. Crossing types include `DATA_READ`, `DATA_WRITE`, `CODE_EXECUTION`, `ARTIFACT_TRANSFER`, `EXTERNAL_DISCLOSURE`, and `PRIVILEGED_OPERATION`.

Material crossing resolution composes source/destination trust, crossing type, provenance/classification, TASK-027 Tool/MCP eligibility, TASK-034 capability eligibility, TASK-026 disclosure/secret rules when external context is involved, then existing AUTH/Risk/Decision/shared-state gates. No component subsumes another.

`PRIVILEGED` means elevated consequence, not more authority/trust. Material `PRIVILEGED_OPERATION` requires explicit authority plus applicable risk/review/evidence. `EXTERNAL` stays outside Project-local control and requires purpose-specific disclosure/authority review. `UNKNOWN` or materially contradictory trust for sensitive actions fails closed; recency/ranking/similarity never resolves trust.

Actual secret values remain prohibited; `17 Secret Reference Registry` stays reference-only. Code/artifacts/dependencies from `UNTRUSTED`, `LIMITED_TRUST`, `EXTERNAL`, or `UNKNOWN` do not become trusted because they exist in the workspace. Provenance/review remains proportional to impact.

TASK-035 publication dimensions remain factual lifecycle state: `PUSHED`, `PUBLISHED`, or `DEPLOYED` never prove trust/authority/provenance sufficiency. Signatures/tags may increase optional assurance but do not replace trust/authority evaluation.

`PROJECT-BOOTSTRAP.md` resolves Project authority first; Project-Execution policy is read afterward when applicable. GREENFIELD/Brownfield never invent trust from prior successful use. TASK-037 adds no scanner, sandbox enforcement, policy engine, runtime isolation, supply-chain automation, external security service, secret store, or privileged-operation executor.


Framework `1.12.1` TASK-042 further hardens response bootstrap/finalization: first Project-governed response resolves Project Bootstrap when accessible, non-Material diagnostics are not exempt, and no early-return/exception path may bypass the pre-emit Response Close Completeness Gate.
