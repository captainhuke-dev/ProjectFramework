# TASK-022 Project Graph + OpenViking Relation Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release Framework `1.6.0` with a standard conditional `92 Project Graph`, canonical `REL-*` relation semantics, and a derived-only/rebuildable AI-ControlTower/OpenViking integration contract while preserving Project-local authority and Schema `1.0.0`.

**Architecture:** Each Project owns authoritative `REL-*` assertions in conditional `92 Project Graph`, keyed by immutable `project_uuid`. AI-ControlTower/OpenViking consumes those records as a derived cross-Project index that may be incrementally updated or fully rebuilt but never overrides Project Source. Existing canonical homes (`DEP-*`, `DEC-*`, `REQ-*`, `DRIFT-*`, `CONFLICT-*`, `MIG-*`) remain unchanged and are linked rather than duplicated.

**Tech Stack:** Markdown/YAML governance artifacts, Git worktree/branch, Python text validation, Git verification; no OpenViking runtime, graph database, validator product, CLI, watcher, scheduler, crawler, sync daemon, or other executable Framework implementation.

**Spec:** `docs/superpowers/specs/2026-08-28-task022-project-graph-openviking-design.md`

## Global Constraints

- Target release: Framework `1.6.0` / Schema `1.0.0` / release format `3`.
- Standard namespace: `91 Project Management Control` conditional; `92 Project Graph` conditional; generic extension space becomes `93–99`; `18–19` remain RESERVED.
- `REL-*` assertion states are exactly `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`.
- Core relation vocabulary is exactly `PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO`; custom types require `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>`.
- Relation endpoints use immutable `project_uuid`; relation semantics never silently rewrite repository/workspace/runtime/integration/implementation bindings.
- OpenViking is AI-ControlTower-owned, derived-only, and rebuildable; Project Source remains reconstructable without OpenViking.
- Brownfield custom slot `92` is never overwritten; migration preserves identity/history/references and relocates only through existing governed `MIG-*` flow.
- Existing canonical homes remain authoritative; `92` does not duplicate `DEP-*`, `DEC-*`, `REQ-*`, `RISK-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, or identity/lineage payloads.
- Platform launcher shared marker bodies remain byte-identical and each complete launcher remains `<=4,500` Unicode characters.
- Existing historical amendments remain unchanged.
- Markdown/YAML-only Framework scope; `commit ≠ push`.
- Final completion requires one `RELEASE_FULL` on the unchanged `managing-project-source/` Framework `1.6.0` candidate plus an observed completion commit.

---

### Task 1: Release Identity, Amendment, and Migration Routing

**Files:**
- Modify: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Create: `managing-project-source/references/framework-governance-amendment-260828-task022.md`
- Modify: `managing-project-source/MIGRATION-NOTES.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: approved TASK-022 design spec and current Framework `1.5.0` descriptor/amendment chain.
- Produces: authoritative Framework `1.6.0` release identity, latest-amendment pointer, migration routing, and Task lifecycle `IN_PROGRESS` state used by all later tasks.

- [ ] **Step 1: Record implementation start in the Task source**

Update TASK-022 to:

```text
Status: IN_PROGRESS
Implementation Plan: docs/superpowers/plans/2026-08-28-task022-project-graph-openviking.md
Plan State: USER_APPROVED_PLAN / EXECUTING
Implementation Release: Framework 1.6.0 / Schema 1.0.0
Exact Next Step: Implement Task 1 release identity/amendment/migration routing in the isolated TASK-022 worktree.
```

- [ ] **Step 2: Write the Framework 1.6.0 amendment**

Create `framework-governance-amendment-260828-task022.md` with frontmatter:

```yaml
---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.5.0"
project_source_framework_version: "1.6.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-28"
compatibility: "BACKWARD_COMPATIBLE_FEDERATED_PROJECT_GRAPH_GOVERNANCE"
---
```

The amendment must normatively define: standard conditional slot `92`; `REL-*`; core relation types; exact assertion states; `project_uuid` endpoints; late binding; semantic nesting; non-duplication of existing canonical homes; OpenViking derived-only/rebuildable contract; merge/split relation reassessment; Brownfield custom-92 migration; and non-goals excluding graph/runtime automation.

- [ ] **Step 3: Update release descriptor**

Set:

```yaml
framework_version: "1.6.0"
schema_version: "1.0.0"
release_format_version: 3
latest_framework_amendment: "references/framework-governance-amendment-260828-task022.md"
```

Preserve canonical repository/branch, migration-notes pointer, upgrade policy, and assurance policy.

- [ ] **Step 4: Add migration notes for `1.5.0 → 1.6.0`**

Add a new current section before older notes. Affected surfaces must mention slot `92`, `REL-*`, OpenViking derived-only contract, templates, and Brownfield collision. Checklist must require Direct-to-Latest classification/Preview/approval, custom-slot-92 collision assessment, preservation of Project-specific rules/bindings/history, activation of `92` only when applicable, and final verification.

- [ ] **Step 5: Run Task-1 verification**

Run:

```bash
python -c "from pathlib import Path; import yaml; r=Path('managing-project-source'); d=yaml.safe_load((r/'FRAMEWORK-RELEASE.yaml').read_text(encoding='utf-8')); a=(r/'references/framework-governance-amendment-260828-task022.md').read_text(encoding='utf-8'); m=(r/'MIGRATION-NOTES.md').read_text(encoding='utf-8'); assert d['framework_version']=='1.6.0'; assert d['schema_version']=='1.0.0'; assert d['release_format_version']==3; assert d['latest_framework_amendment']=='references/framework-governance-amendment-260828-task022.md'; assert '92 Project Graph' in a and 'REL-*' in a and 'DERIVED' in a.upper() and '1.5.0 → 1.6.0' in m"
```

Expected: exit `0`.

- [ ] **Step 6: Commit Task 1**

```bash
git add managing-project-source/FRAMEWORK-RELEASE.yaml managing-project-source/references/framework-governance-amendment-260828-task022.md managing-project-source/MIGRATION-NOTES.md docs/superpowers/PROJECT-TASKS.md
git commit -m "docs: define framework 1.6 project graph release"
```

---

### Task 2: Core Governance, Skill, and README Semantics

**Files:**
- Modify: `managing-project-source/references/core-governance-rules.md`
- Modify: `managing-project-source/SKILL.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Task 1 amendment/release identity.
- Produces: current normative Project Graph rules, operator workflow/routing, and public release explanation used by templates and verification.

- [ ] **Step 1: Extend Core Governance namespace and canonical homes**

Update current namespace text so:

```text
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92 Project Graph                  CONDITIONAL / STANDARD IN 1.6.0+
93–99 Project-specific / Governance Extension unless governed otherwise later
```

Add a Project Graph section defining canonical `REL-*` ownership, exact relation/assertion vocabularies, reciprocal compatibility, late binding, semantic nesting, relation/location separation, existing-family reuse, OpenViking derived-only/rebuildable behavior, and Brownfield slot-92 migration. Preserve historical descriptions only where they explicitly describe the old release state.

- [ ] **Step 2: Update SKILL current distribution and Required References**

Set current distribution to `1.6.0 / 1.0.0`; put the TASK-022 amendment first after the descriptor; add Project Graph operational routing and quick-reference/red-flag entries. Current namespace/routing text must route `REL-* → 92` and generic extension space to `93–99`.

- [ ] **Step 3: Update README release identity and user-facing explanation**

Change current release to `1.6.0`, mention `92` in the TL;DR optional/conditional set, and add a `Framework 1.6.0 Federated Project Graph` section explaining: Project-local authoritative `REL-*`, AI-ControlTower/OpenViking derived index, late binding, rebuildability, and Brownfield slot-92 migration. Update current namespace/bootstrap statements from `92–99` to standard `92` plus `93–99`.

- [ ] **Step 4: Run Task-2 verification**

Run:

```bash
python -c "from pathlib import Path; files=[Path('README.md'),Path('managing-project-source/SKILL.md'),Path('managing-project-source/references/core-governance-rules.md')]; t='\n'.join(p.read_text(encoding='utf-8') for p in files); required=['Framework 1.6.0','92 Project Graph','REL-*','ASSERTED','CORROBORATED','CONFLICTED','RETIRED','PARENT_OF','CHILD_OF','PEER_OF','DEPENDS_ON','SUPPORTS','RELATED_TO','OpenViking','project_uuid','93–99']; [(_ for _ in ()).throw(AssertionError(x)) for x in required if x not in t]; assert 'framework-governance-amendment-260828-task022.md' in Path('managing-project-source/SKILL.md').read_text(encoding='utf-8')"
```

Expected: exit `0`.

- [ ] **Step 5: Commit Task 2**

```bash
git add README.md managing-project-source/SKILL.md managing-project-source/references/core-governance-rules.md
git commit -m "docs: add federated project graph governance"
```

---

### Task 3: Templates, Standard Slot 92, and Launcher Identity

**Files:**
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`
- Modify: `managing-project-source/templates/project-source-mockup/README.md`
- Modify: `managing-project-source/templates/project-source-mockup/01-Project-Source-Index.template.md`
- Modify: `managing-project-source/templates/project-source-mockup/14-Project-Source-Manifest.template.md`
- Modify: `managing-project-source/templates/project-source-mockup/16-Migration-Registry.template.md`
- Create: `managing-project-source/templates/project-source-mockup/92-Project-Graph.template.md`
- Modify: every existing `managing-project-source/templates/project-source-mockup/*.template.md` frontmatter release stamp from `1.5.0` to `1.6.0`
- Modify: `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md` first-line release header only unless a bootstrap-critical rule proves necessary
- Modify: `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md` first-line release header only unless a bootstrap-critical rule proves necessary

**Interfaces:**
- Consumes: Task 2 normative semantics.
- Produces: concrete starter representation and bootstrap metadata that instantiate the approved contract without requiring a graph product.

- [ ] **Step 1: Add Project Graph applicability to root template**

Add a bounded root block with:

```yaml
project_graph:
  applicability: "<APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
  relation_document_slot: "92"
  external_index:
    owner_scope: "AI_CONTROLTOWER"
    authority: "DERIVED_ONLY"
```

State that runtime endpoint/credentials are not root authority and relation changes do not rewrite Project Location Binding. Update namespace to standard `92` and extension `93–99`.

- [ ] **Step 2: Add the extended conditional skeleton**

Append `## 92 — Project Graph [CONDITIONAL / STANDARD IN 1.6.0+]` to `core-document-skeletons.md` with the exact `REL-*` minimum fields, core relation types, assertion states, reciprocal rules, non-duplication pointers, rebuild/index notes, and relation/location separation.

- [ ] **Step 3: Create the concrete `92` starter**

Create `92-Project-Graph.template.md` with normal Project metadata/frontmatter at Framework `1.6.0`, semantic slot `92`, conditional guidance, and a non-fabricated example schema using placeholders. Include sections for relation registry, reciprocal evidence, external derived-index status/pointers, conflicts/drift pointers, and rebuild notes. Do not include OpenViking credentials or runtime configuration.

- [ ] **Step 4: Update mockup routing/index/manifest/migration guidance**

In mockup README: list `92` in Standard Extended Starters, change extension row to `93–99`, and update bootstrap evaluation to include `92`. In `01`, route `REL-* → 92` when active. In `14`, include active `92` when required to interpret current truth. In `16`, add Brownfield custom-slot-92 collision preservation/relocation rules.

- [ ] **Step 5: Stamp starter metadata to 1.6.0 and update launcher headers**

Change every existing mockup `.template.md` frontmatter `project_source_framework_version` from `1.5.0` to `1.6.0`; update root template/skeleton release stamps; change only launcher first-line version headers from `1.5.0` to `1.6.0` unless implementation evidence shows a shared-contract change is strictly required.

- [ ] **Step 6: Run Task-3 verification**

Run:

```bash
python -c "from pathlib import Path; import re; root=Path('managing-project-source'); mock=root/'templates/project-source-mockup'; ts=list(mock.glob('*.template.md')); assert len(ts)==22, len(ts); bad=[p.name for p in ts if 'project_source_framework_version: \"1.6.0\"' not in p.read_text(encoding='utf-8')]; assert not bad,bad; p=(mock/'92-Project-Graph.template.md').read_text(encoding='utf-8'); [(_ for _ in ()).throw(AssertionError(x)) for x in ['semantic_slot: \"92\"','REL-*','ASSERTED','CORROBORATED','CONFLICTED','RETIRED','DERIVED_ONLY'] if x not in p]; c=(root/'CHATGPT-PROJECT-INSTRUCTIONS.md').read_text(encoding='utf-8'); d=(root/'CLAUDE-PROJECT-INSTRUCTIONS.md').read_text(encoding='utf-8'); assert c.splitlines()[0]=='# ChatGPT Project — F`1.6.0` / S`1.0.0`'; assert d.splitlines()[0]=='# Claude Project — F`1.6.0` / S`1.0.0`'; s='PROJECTFRAMEWORK-SHARED-CONTRACT:START'; e='PROJECTFRAMEWORK-SHARED-CONTRACT:END'; body=lambda x:x.split(s,1)[1].split(e,1)[0]; assert body(c)==body(d); assert len(c)<=4500 and len(d)<=4500,(len(c),len(d))"
```

Expected: exit `0`; template count `22`; launcher bodies byte-identical and both within ceiling.

- [ ] **Step 7: Commit Task 3**

```bash
git add managing-project-source/templates managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: add project graph slot 92 templates"
```

---

### Task 4: Pressure Scenarios 163–171

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: complete normative/template semantics from Tasks 1–3.
- Produces: regression/pressure coverage used by final RELEASE_FULL.

- [ ] **Step 1: Add Scenario 163 — Late Binding After Independent Creation**

Pass requires materializing `92` only when relation truth becomes applicable and adding `REL-*` without rebuilding either Project or changing UUIDs.

- [ ] **Step 2: Add Scenario 164 — OpenViking Never Becomes Canonical Authority**

Pass rejects overwriting Project Source from a newer/high-confidence central index and treats OpenViking as derived/rebuildable.

- [ ] **Step 3: Add Scenario 165 — Reciprocal Corroboration Is Evidence-Based**

Pass allows `CORROBORATED` only when compatible authoritative assertions with matching endpoint UUIDs are verified; a derived inverse edge is insufficient.

- [ ] **Step 4: Add Scenario 166 — Contradictory Relations Surface Conflict**

Pass marks relevant relation state `CONFLICTED` and routes managed conflict to existing `CONFLICT-*`; timestamp/ranking/confidence may not auto-pick a winner.

- [ ] **Step 5: Add Scenario 167 — Brownfield Custom Slot 92 Collision**

Pass opens/routes `MIG-*`, preserves custom identity/history/references, relocates only with governed approval, and activates standard `92` only afterward.

- [ ] **Step 6: Add Scenario 168 — Semantic Nesting Does Not Rewrite Location**

Pass keeps `PARENT_OF`/`CHILD_OF` independent from repository/local workspace/runtime topology and does not rewrite bindings.

- [ ] **Step 7: Add Scenario 169 — Merge/Split Relations Are Reassessed, Not Cloned**

Pass preserves existing UUID/lineage rules and evaluates each relation for the successor/descendant rather than bulk-copying graph edges.

- [ ] **Step 8: Add Scenario 170 — Full Rebuild From Project Sources**

Pass can discard a lost/corrupt derived graph and reconstruct it from current authoritative Project Sources without using OpenViking as hidden truth.

- [ ] **Step 9: Add Scenario 171 — Custom Relation Type Must Be Namespaced**

Pass rejects ungoverned free-text relation types and requires `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>` without redefining core relation types.

- [ ] **Step 10: Verify scenario numbering and uniqueness**

Run:

```bash
python -c "from pathlib import Path; import re,collections; t=Path('managing-project-source/tests/pressure-scenarios.md').read_text(encoding='utf-8'); nums=[int(x) for x in re.findall(r'^## Scenario (\d+) —',t,re.M)]; c=collections.Counter(nums); assert nums[-9:]==list(range(163,172)),nums[-9:]; assert all(c[n]==1 for n in range(1,172)),[(n,c[n]) for n in range(1,172) if c[n]!=1]"
```

Expected: exit `0`, scenarios `1–171` each exactly once.

- [ ] **Step 11: Commit Task 4**

```bash
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "test: add project graph pressure scenarios"
```

---

### Task 5: RELEASE_FULL, Evidence, and Verified Task Completion

**Files:**
- Create: `docs/superpowers/evidence/2026-08-28-task-022-project-graph-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: unchanged Framework 1.6.0 distribution candidate from Tasks 1–4.
- Produces: state-bound verification evidence and durable TASK-022 completion record; no push.

- [ ] **Step 1: Confirm candidate scope before RELEASE_FULL**

Run:

```bash
git status --short
git diff --check
git rev-parse HEAD
git rev-parse HEAD:managing-project-source
```

Expected: clean working tree; `git diff --check` exit `0`; record candidate commit and `managing-project-source` tree SHA.

- [ ] **Step 2: Run RELEASE_FULL verification**

Run a single Python verification command/script that checks all Global Constraints plus at least these assertions:

```text
Framework 1.6.0 / Schema 1.0.0 / release format 3
latest amendment pointer and SKILL first-latest-amendment alignment
README current release and 1.6.0 section
current namespace contains standard 92 and 93–99 extension
REL-* canonical home and no duplicated DEP/DEC/REQ authority
exact assertion states and core relation vocabulary
project_uuid endpoint identity
late binding / no mandatory empty 92
relation ≠ location/binding/runtime/integration authority
OpenViking AI-ControlTower derived-only and REBUILDABLE contract
Brownfield custom-92 collision fail-closed migration
merge/split relation reassessment
existing DRIFT-* / CONFLICT-* / MIG-* reuse
root/skeleton/mockup 92 support
all 22 mockup template metadata stamps at 1.6.0
01 routing and 14 current-snapshot inclusion for active 92
16 slot-92 migration guidance
launchers first-line identity, <=4500, byte-identical marker bodies
scenarios 1–171 exactly once
reserved 18–19 unchanged
historical TASK-021 amendment still present and unmodified by intent
Markdown/YAML-only Framework change scope
git diff --check clean
```

Record exact PASS count and any first-run finding. If any check fails, fix the candidate, commit the fix, invalidate the failed candidate evidence, and rerun the entire RELEASE_FULL once on the corrected unchanged candidate.

- [ ] **Step 3: Create release evidence**

Write `2026-08-28-task-022-project-graph-release-full.md` with: captured date/timezone; branch/base; Framework/Schema/release identity; implemented scope; implementation commits; candidate commit and `managing-project-source` tree SHA; actual RELEASE_FULL command/check count/result; launcher sizes; scenario range; known non-goals; and explicit `commit ≠ push` publication state.

- [ ] **Step 4: Close TASK-022 in durable Task source**

Set:

```text
Status: DONE
Design Spec: docs/superpowers/specs/2026-08-28-task022-project-graph-openviking-design.md
Implementation Plan: docs/superpowers/plans/2026-08-28-task022-project-graph-openviking.md
Plan State: IMPLEMENTATION_PLAN_EXECUTED
Implementation Release: Framework 1.6.0 / Schema 1.0.0
Implementation Commit(s): <observed commits>
Release Evidence: docs/superpowers/evidence/2026-08-28-task-022-project-graph-release-full.md
Verification Result: RELEASE_FULL <actual pass count>/<actual pass count> PASS
Completion criteria met: federated graph, standard slot 92, REL-*, late binding, rebuildability, Brownfield collision migration, templates, pressure scenarios, derived-only OpenViking boundary
Publication State: NOT_PUSHED
Completion Working Tree: CLEAN
Exact Next Step: Integrate the verified TASK-022 branch into local main if not already integrated; remote push remains separately gated.
```

Do not fabricate commit IDs or pass counts; fill only from observed Git/verification output.

- [ ] **Step 5: Commit completion evidence**

```bash
git add docs/superpowers/evidence/2026-08-28-task-022-project-graph-release-full.md docs/superpowers/PROJECT-TASKS.md
git commit -m "docs: record TASK-022 release evidence and completion"
```

- [ ] **Step 6: Verify completion checkpoint**

Run:

```bash
git status --short
git log -5 --oneline
```

Expected: clean working tree; completion evidence commit visible; no push performed.
