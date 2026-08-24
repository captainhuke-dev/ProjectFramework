---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "FRAMEWORK-001"
document_type: "PROJECT_SOURCE_FRAMEWORK"
semantic_slot: "00"
revision: 1
document_status: "ACTIVE"
framework_root: true
inherits_from: []
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.3.1"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Root Governance / Non-Removable Framework:** เอกสารนี้คือกฎสูงสุดภายใน Project Source และเป็น Root Governance ของ Project นี้ ทุก AI/Agent ต้องอ่าน `00 → 01 → 03` ก่อนเริ่มงาน ทุก Project Source artifact ที่สร้างหลังจากนี้ inherit จาก `FRAMEWORK-001`. ห้ามลบ, bypass, demote, replace ด้วย child rule หรือปล่อยให้ Framework ไม่มี Active revision. การแก้ Framework ต้องมี User Explicit Approval และใช้ revision/supersede/archive flow.

## 1. Framework Authority, Inheritance, and Precedence

### 1.1 Root Invariant

```yaml
framework_document_id: "FRAMEWORK-001"
framework_root: true
inherits_from: []
```

Project Source ที่ไม่มี Active `FRAMEWORK-001` ถือว่า:

```text
INVALID + NOT_OPERATIONALLY_READY
```

ห้าม descendant artifact/rule:

- ลบหรือย้าย Framework ออกจาก semantic slot `00`
- bypass bootstrap ที่เริ่มจาก `00`
- demote Framework ต่ำกว่า child rule
- replace Framework ด้วย Project-Specific Rule, Handoff, Task, Prompt หรือ Agent instruction
- weaken/contradict Framework invariant ผ่าน child override

### 1.2 Inheritance Contract

Governed Markdown descendants declare:

```yaml
inherits_from:
  - "FRAMEWORK-001"
```

Non-Markdown Project Source artifacts inherit ผ่าน canonical Registry/Manifest entry. Implementation artifacts เช่น source code/config/runtime ไม่จำเป็นต้องฝัง YAML inheritance แต่ยังอยู่ใต้ Framework ผ่าน Project identity + related `REQ-*` / `DEC-*` / `AUTH-*` / `ACT-*` และ governance workflow.

Descendants may extend/specialize/add constraints แต่ห้ามลดทอน Root Framework. หากต้องเปลี่ยน Root invariant ต้องแก้ `FRAMEWORK-001` โดยตรงผ่าน User Approval และ preserve history.

### 1.3 Authority Order

```text
0. User Explicit Instruction / Approval
1. 00 Project Source Framework
2. Framework-compliant Project-Specific Rules
3. Canonical Project Source documents / Decisions / Requirements
4. Task / Handoff / Prompt / Agent Instruction
```

## 2. Project Identity

```yaml
project_uuid: "<PROJECT_UUID>"   # immutable
project_id: "<PROJECT_ID>"       # stable human-readable ID
project_name: "<PROJECT_NAME>"   # mutable display name
```

Rename ห้ามเปลี่ยน `project_uuid`. Merge/Split ต้อง preserve lineage แบบ reconstructable.

### 2.1 Project Location Binding

Active local `FRAMEWORK-001` เป็น canonical governance home ของ **Project Location Binding** สำหรับ routing ข้าม connector. `03 Current State` และ `09 Handoff` อ้างอิง binding นี้ได้ แต่ห้ามเก็บ authoritative copy แยกต่างหาก.

```yaml
project_location_binding:
  github:
    binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
    repository: "<OWNER/REPOSITORY_OR_UNKNOWN>"
    repository_url: "<CANONICAL_REPOSITORY_URL_OR_UNKNOWN>"
    project_source_path: "<PROJECT_SOURCE_PATH_OR_UNKNOWN>"
    verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
    last_verified_at: "<ISO8601_OR_UNKNOWN>"

  google_drive:
    binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
    project_root_id: "<FOLDER_ID_OR_UNKNOWN>"
    project_root_url: "<CANONICAL_FOLDER_URL_OR_UNKNOWN>"
    display_path: "<OPTIONAL_HUMAN_READABLE_PATH_OR_UNKNOWN>"
    designated_progress_file: "<EXISTING_PROGRESS_MD | PROJECT-PROGRESS.md | NOT_APPLICABLE | UNKNOWN>"
    designated_progress_file_id: "<FILE_ID_OR_UNKNOWN>"
    designated_progress_file_url: "<CANONICAL_FILE_URL_OR_UNKNOWN>"
    verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
    last_verified_at: "<ISO8601_OR_UNKNOWN>"

  local_workspaces:
    - environment_scope: "<USER_CONFIRMED_ENVIRONMENT_SCOPE>"
      binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
      canonical_path: "<ABSOLUTE_LOCAL_PATH_OR_UNKNOWN>"
      repository: "<OWNER/REPOSITORY_OR_UNKNOWN_OR_NOT_APPLICABLE>"
      repository_url: "<CANONICAL_REPOSITORY_URL_OR_UNKNOWN_OR_NOT_APPLICABLE>"
      verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
      last_verified_at: "<ISO8601_OR_UNKNOWN>"

  file_storage_locations:
    - storage_key: "<PROJECT_DEFINED_STORAGE_KEY>"
      binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
      storage_type: "<S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER>"
      canonical_locator: "<PROVIDER_APPROPRIATE_DURABLE_LOCATOR_OR_UNKNOWN_OR_NOT_APPLICABLE>"
      content_scope: "<DECLARED_CONTENT_SCOPE>"
      authoritative_scope: "<OWNED_PROJECT_FILE_OBJECT_SCOPE>"
      verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
      last_verified_at: "<ISO8601_OR_UNKNOWN>"
```

Generic `file_storage_locations` ใช้เฉพาะ non-Google-Drive external storage scopes; Google Drive ยังคง canonical ใน dedicated `google_drive` block และห้าม duplicate target/content scope เดียวกัน. `BOUND` ต้องมี provider-appropriate durable identity และ pair เฉพาะ `VERIFIED` หรือ `USER_CONFIRMED`; known-applicable unresolved = `VERIFICATION_REQUIRED`. Project ที่ไม่มี external storage omit list นี้ได้; absence/unresolved ห้าม fallback ไป recent/search-ranked/mounted target. Multiple stores ใช้ได้เมื่อ content scopes distinct และหนึ่ง governed content scope มี authoritative owner เดียว ณ เวลาเดียว. Actual credentials ห้ามเก็บที่นี่; ใช้ `SECRET-*` reference. Mount/sync/cache path เป็น routing evidence ไม่ใช่ Local Workspace, Canonical Implementation Source หรือ Runtime/Persistent-State authority โดยอัตโนมัติ.

Binding state ของ GitHub, Google Drive และแต่ละ environment-scoped Local Workspace Binding ต้อง resolve แยกกันเป็น exactly `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`:

- `BOUND` ต้องมี durable routing identity อย่างน้อย GitHub owner/repository หรือ canonical repository URL; Drive project-root folder ID หรือ canonical folder URL; Local Workspace ต้องมี verified/user-confirmed absolute path ของ environment นั้น และ Git-backed workspace ควร cross-check repository identity เมื่อ practical.
- `VERIFICATION_REQUIRED` เป็น **fail-closed สำหรับ Material mutation**; read/search/discovery เพื่อ resolve candidate ทำได้ แต่ห้าม Material write ไป unresolved target โดย default.
- `NOT_APPLICABLE` block Material Project work ผ่าน connector นั้นจนกว่าจะมี approved Root Governance binding/scope change.
- User Explicit Instruction ที่ระบุ exact target อาจ authorize action เดียวเมื่อ otherwise allowed แต่ไม่ persistently rewrite binding.
- การเปลี่ยน active binding เป็น Root Governance mutation: ต้อง User Explicit Approval และใช้ `FRAMEWORK-001` revision → validate → promote → supersede/archive flow. Connector discovery, recency หรือ ranking ไม่ transfer authority.
- Repository Location Binding `≠` File Storage Binding `≠` Local Workspace Binding `≠` current work branch/worktree `≠` Canonical Integration Target `≠` Canonical Implementation Source `≠` Runtime Location / Runtime Data / Persistent-State authority. Project Location Binding ห้ามสร้าง `canonical_branch` หรือ branch authority คู่ขนาน; Git integration target ยัง governed โดย Framework `1.2.2` Base Freshness contract.

GREENFIELD ที่ยังไม่มี active `FRAMEWORK-001` อ่าน Project-specific Bootstrap Location Block เมื่อมี → ใช้ read-only discovery เมื่อจำเป็น → Preview proposed GitHub/Drive/local-workspace/generic-file-storage binding states/identities ตาม applicability → explicit user approval → first Material Project-Source write creates active `00` with approved binding. Binding uncertainty ห้ามถูกเดาจาก chat memory, recent activity หรือ search result. MCP `workspaceId`, editor handle, active/recent workspace เป็น routing evidence เท่านั้น ไม่ใช่ canonical Project identity; missing applicable local environment = `VERIFICATION_REQUIRED` โดย default. Persistent Local Workspace Binding change ยังเป็น Root Governance mutation และ one-off exact local target ไม่ persistently rewrite binding.
## 3. Project Source Location and Semantic Namespace

Project Source อยู่ที่:

```text
<Project-Root>/Project-Source/
```

Core documents:

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

Framework `1.2.0` standardizes extended documents:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension
```

Conditional documents สร้างเฉพาะเมื่อ applicable; ห้ามสร้างไฟล์ว่างเพื่อให้ดูครบ. `18–19` ห้าม materialize เป็น default/active starter.

Framework distribution artifacts `FRAMEWORK-RELEASE.yaml`, ChatGPT Project Instructions, และ Claude Project Instructions อยู่นอก Project Source semantic namespace. NEW Project bootstrap จาก canonical repository `main`; initialized Project ใช้ local pinned Project Source เป็น authority. Git tag/SHA/branch protection เป็น optional assurance ไม่ใช่ prerequisite ของ normal bootstrap.

## 4. Naming and Revision

Project Source artifacts ใช้ suffix:

```text
-YYMMDD-HHMM
```

Document revisions ใช้ monotonic `r001`, `r002`, ... และห้าม reuse. Canonical implementation filenames ที่ ecosystem บังคับชื่อคงชื่อ canonical.

## 5. Bootstrap and Routing

ทุก session/task อ่านขั้นต่ำ:

```text
00 → 01 → 03
```

จากนั้น `01` route ไปเอกสารที่เกี่ยวข้อง.

GREENFIELD bootstrap:

```text
canonical main
→ README
→ FRAMEWORK-RELEASE.yaml
→ SKILL
→ latest amendment
→ Core Governance
→ 00 template
→ core skeletons
→ mockup
→ Preview
→ explicit user approval
→ create active 00 first
→ mandatory 01–05 + 09–17
→ evaluate conditional 06–08 / 40 / 60 / 91
→ pin Framework/Schema locally
```

หาก canonical Framework source เข้าถึงไม่ได้ ให้หยุด affected governance mutation และรายงาน limitation; ห้าม reconstruct จาก memory. การไม่มี immutable tag, exact SHA หรือ branch protection ไม่ใช่เหตุให้ block bootstrap ถ้า canonical source ยังเข้าถึงได้.

### 5.1 Framework Source Provenance — Optional Assurance

Exact Git provenance เป็น enhanced assurance ไม่ใช่ prerequisite ของ normal Framework use. หาก track ให้บันทึกเฉพาะ observed values:

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "<OBSERVED_REF_OR_MAIN>"
  release_tag: "<OPTIONAL_OBSERVED_TAG_OR_NONE>"
  resolved_commit_sha: "<OPTIONAL_OBSERVED_SHA_OR_UNKNOWN>"
  framework_version: "1.3.1"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
  provenance_status: "<VERIFIED | PARTIAL | UNVERIFIED>"
```

ห้าม predict/fabricate/backfill exact tag/SHA. หาก exact provenance ไม่มี ให้ใช้ `UNKNOWN / UNVERIFIED` เมื่อจำเป็นต้อง represent state. Absence ของ optional exact provenance เพียงอย่างเดียวไม่ทำให้ Project `NOT_OPERATIONALLY_READY`.

### 5.2 Concept-First Technical / Tooling Boundary

ProjectFramework เป็น **conceptual governance/planning framework first**. Tech Stack, installation, Docker, integrity หรือ automation concepts อธิบาย roles/contracts/interfaces/verification ได้ แต่ไม่ถือเป็น implicit authorization ให้สร้าง implementation artifacts.

ห้ามสร้างโดยอัตโนมัติ:

```text
application source code
Dockerfile
Compose / Kubernetes / Helm runtime files
install scripts
validator / CLI
GitHub Actions / CI/CD
migration engine
scheduler / reminder runtime
background automation
dashboard / runtime enforcement
```

A real Project อาจมี artifacts เหล่านี้อยู่แล้ว และ Project Source สามารถ document/reference/govern/verify ได้. การสร้างหรือแก้ implementation จริงต้องเป็น separate explicit scope.

### 5.3 Registered Project Commands

Framework `1.3.1` registers bracketed Project inspection commands. Literal `[` and `]` are required; matching inside brackets is case-insensitive. Current registry:

```text
[Project Status]  : fresh read-only Project/Task/Git/verification/blocker dashboard
[Project Path]    : show/verify configured Project path values and route explicit change requests through existing location governance
[Project Upgrade] : fresh-compare the active Project Framework with canonical upstream and offer governed upgrade preparation when they differ
```

Natural-language command-help requests list only registered commands as `[XXX] : purpose`; do not invent commands. `[Project Status]` fresh-observes Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers, reuses `GREEN | AMBER | RED | UNKNOWN`, and keeps Task count distinct from Git change count. `[Project Path]` treats angle-bracket values such as `<STORAGE>` / `<WS>` as unset, never literal paths or fallback authority. `[Project Upgrade]` keeps the active local `FRAMEWORK-001` pin as current authority, fresh-resolves canonical upstream as target evidence, reports `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`, and asks before preparing an upgrade when a verified difference exists. A positive answer authorizes assessment/Preview only, not Project mutation; persistent path/binding changes retain existing explicit approval + Root Governance revision flow.

Markdown response-close presentation SHOULD keep canonical labels visibly renderable, e.g. `**[Chat]:** CONTINUE_CURRENT_CHAT`; wrapping is presentation-only and does not rename `[Chat]:` or lifecycle tokens.

## 6. Truth and Uncertainty

Truth Domains:

```text
GOVERNANCE INTENT REQUIREMENTS IMPLEMENTATION RUNTIME DATA IDENTITY AUTHORITY HISTORY EXTERNAL
```

Epistemic Status:

```text
VERIFIED USER_CONFIRMED INFERRED ASSUMED UNKNOWN CONFLICTED STALE
```

Freshness:

```text
IMMUTABLE STABLE CHANGEABLE VOLATILE
```

ห้ามยกระดับ `ASSUMED/INFERRED` เป็น `VERIFIED` โดยไม่มี evidence; `VOLATILE` ต้อง fresh-check เมื่อมีผลต่อ decision/mutation. Truth mismatch ใช้ `DRIFT-*`; competing semantic state ใช้ `CONFLICT-*` และห้าม last-write-wins.

### 6.1 Canonical Implementation Source and Runtime Authority

เมื่อ implementation มีอยู่และ distinction นี้ material ต่อ development/recovery/verification/deployment Project MUST ระบุ **Canonical Implementation Source** สำหรับ affected scope ได้. Canonical Implementation Source คือ durable declared source location ที่ verified state เป็น authoritative `IMPLEMENTATION` Truth; สำหรับ Git-backed Project โดยปกติคือ verified Git/source tree ตาม repository/workspace contract.

`durable` หมายถึง source ต้อง survive lifecycle ที่ Project อ้างว่าสามารถ replace/recreate runtime ได้ โดยไม่พึ่ง runtime instance ที่ disposable/recreatable เป็น sole copy. ไม่ได้บังคับว่า source ต้องอยู่ physical host filesystem. Valid topology อาจเป็น host Git repo, Git worktree, remote/VM durable workspace หรือ Dev Container ที่ใช้ durable bind mount/workspace volume.

```text
Implementation Truth → Canonical Implementation Source
Runtime Truth        → fresh runtime observation
```

Runtime execution/editing ไม่ transfer Implementation authority โดยปริยาย. Runtime-only hotfix/interactive edit ไม่ใช่ canonical implementation completion จน accepted intent ถูกนำกลับผ่าน governed change path เข้า Canonical Implementation Source และ reverify สำเร็จ. หาก Implementation กับ Runtime ควร align แต่ต่างกัน materially ให้ใช้ `DRIFT-*`; ห้ามสร้าง parallel workspace/runtime drift family.

Runtime component ที่ประกาศ disposable/recreatable ห้ามกลายเป็น sole authoritative implementation copy โดยอุบัติเหตุ. State ที่ `REQ-*`, `DEC-*`, `40` หรือ deployment contract กำหนดว่าต้อง survive expected replacement ต้องมี declared persistent-state authority/mechanism. Rebuildable cache/temp/scratch state สามารถ ephemeral ได้เมื่อไม่มี survival requirement.

Docker, host-local source, immutable image และ production source mount ไม่ใช่ universal requirement/prohibition; topology เป็น Project-specific/applicability-driven และต้อง preserve Truth/authority/persistence contract นี้.

## 7. Canonical Object Homes

```text
DEC-*       → 04
REQ-*       → 05
ISS-*       → 08
DRIFT-*     → 08
CONFLICT-*  → 08
CHG-*       → 10
ACTOR-*     → 11
INST-*      → 11
AUTH-*      → 12
DEL-*       → 12
EVD-*       → 13
ACT-*       → 15
MIG-*       → 16
SECRET-*    → 17
RISK-*      → 91
ASM-*       → 91
MS-*        → 91
OUT-*       → 91
DEP-*       → 91
CR-*        → 91
GATE-*      → 91
```

หนึ่ง object type มี authoritative home เดียว. เอกสารอื่น reference Stable ID เท่านั้น.

### 7.1 Materialized Current State and Stable-ID Resolution

Active canonical registries เป็น **materialized current projections, not delta chains**. ทุก referenced current Stable ID ต้อง resolve ภายใน Current Reconstructable Snapshot โดยไม่เปิด archive. Record ต้องมี current semantic payload หรือ link ไป active/current canonical Detail Document ที่เก็บ payload นั้น. Archive เป็น Historical Truth/rationale/evolution เท่านั้น.

Delta-only shorthand เช่น `retain previous status`, `unchanged from rNNN`, `see archived revision` ใช้แทน current authoritative payload ไม่ได้เมื่อ semantics จริงอยู่เฉพาะ archive.

กฎนี้ใช้กับ `DEC-*`, `REQ-*`, และ `RISK/ASM/MS/OUT/DEP/CR/GATE` ใน `91` เท่ากัน. Failure = integrity/readiness defect ของ affected scope.

## 8. Project Management Control — `91`

`91 Project Management Control` เป็น STANDARD CONDITIONAL ใน Framework `1.2.0+`. สร้างเมื่อมี management-control object ที่ materially applicable อย่างน้อยหนึ่งรายการ.

### 8.1 Risk

`RISK-*` = uncertain future event/condition. `ISS-*` = problem ที่ materialized/current แล้ว.

```text
IDENTIFIED OPEN MITIGATING MONITORING ACCEPTED MATERIALIZED CLOSED SUPERSEDED
```

Risk materialization ต้อง preserve `RISK-*` และ link `ISS-*`; ห้าม delete/rewrite Risk เป็น Issue. `ACCEPTED` exposure ต้องมี relevant decision/authority + review trigger เมื่อ material.

Minimum semantics: Risk Statement, Probability, Impact, Trigger/Early Warning, Mitigation, Contingency, Owner, Review Trigger/Review By, Status, related IDs/evidence, Materialized Issue when applicable.

### 8.2 Assumption

`ASM-*` = proposition ที่ยังพึ่งพาอยู่แต่ evidence ยังไม่พอเป็น established truth.

```text
UNVERIFIED → VALIDATED / INVALIDATED / SUPERSEDED
```

INVALIDATED ต้อง impact-assess และอาจ trigger `DRIFT-*`, `CR-*`, replanning, Decision revalidation, Requirement revision, Risk/Issue update.

### 8.3 Action vs Milestone vs Outcome

```text
ACT-* = work/action
MS-*  = significant checkpoint/state
OUT-* = intended result/benefit/effect

ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED
```

### 8.4 Dependency

`DEP-*` รองรับ `PERSON / TEAM / APPROVAL / DECISION / VENDOR / SYSTEM / API / DATA / CONTRACT / PROJECT / INFRASTRUCTURE / OTHER`.

`AVAILABLE` = source/resource obtainable; `SATISFIED` = governed dependency requirement fulfilled.

### 8.5 Change Request vs Change Log

```text
CR-*  = proposed/material change + impact assessment + decision path
CHG-* = historical record of applied/observed change
```

CR impact assessment พิจารณา Scope, REQ, DEC, Architecture, Tech Stack, Source Structure, Configuration, Deployment Modes, Data/Migration, Security/Authority, MS/OUT, RISK, DEP, effort/schedule, operations/handoff เมื่อ applicable. CR approval ไม่ grant unrelated implementation authority.

### 8.6 Review Gate

`GATE-*` = governed checkpoint.

```text
PLANNED → READY_FOR_REVIEW → PASSED / FAILED / WAIVED
```

Minimum semantics: Purpose, Affected Scope, Entry/Pass Criteria, Required Evidence, related IDs, Review Owner, Required Authority, Status, Findings, Exceptions/Waiver, Next Action, Reviewed At. `WAIVED` ต้องมี rationale + authority/decision reference.

## 9. Project Health and Review Cadence

Project Health อยู่ใน `03 Current State` เป็น **derived assessment**, ไม่ใช่ replacement ของ canonical objects.

Dimensions:

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

Optional dimension ที่ not applicable ให้ omit ไม่ใช่ mark GREEN. แต่ละ dimension record/resolve:

```text
State
Reason
Supporting Stable IDs / Evidence
Owner
Last Reviewed
Next Review / Trigger when applicable
```

Framework ไม่ define opaque automatic aggregate score.

Review Cadence:

```text
TIME_BASED
EVENT_BASED
```

ใช้กับ Current State, Risk, Assumption, Milestone/Outcome, Decision Revalidation, Technical Design, Deployment Readiness, Handoff Refresh ได้. Framework กำหนด semantics เท่านั้น ไม่สร้าง scheduler/reminder runtime.

## 10. Decision Revalidation

`DEC-*` ยัง canonical ใน `04`. เพิ่ม current fields:

```text
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
```

Statuses:

```text
NOT_DUE REVIEW_DUE REVALIDATED SUPERSEDED
```

Triggers อาจเป็น invalidated `ASM-*`, materially changed `DEP-*`, Requirement/Tech Stack/deployment-mode change, material approved `CR-*`, external regulation/vendor change, review date, หรือ runtime evidence contradicting Decision basis.

## 11. Responsibility and Authority

`11 Actor Registry` สามารถเก็บ scope-keyed Responsibility Mapping:

```text
Responsible
Accountable
Consulted
Informed
```

**Responsibility ≠ Authority.** Role/RACI ไม่ grant permission สำหรับ R2/R3 mutation, approval, deployment, production access หรือ external action. Actual authority อยู่ใน `12` ผ่าน `AUTH-* / DEL-*`.

Authority ห้าม transfer ผ่าน Handoff, prompt, memory, role, responsibility mapping, branch หรือ agent instruction.

## 12. Risk and Approval

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

Default:

- R0 → no approval
- R1 → allowed inside approved scope
- R2 → explicit approval หรือ valid Standing Authorization
- R3 → explicit approval for that action by default

Project-Specific Rules ทำให้ stricter ได้. Before R2/R3 mutation, fresh-read authority.

## 13. Preflight and Postflight

READ PREFLIGHT: identity, `00`, `01`, `03`, scope, truth, freshness, blockers.

MUTATION PREFLIGHT เพิ่ม actor/instance, authority, target, allowed/forbidden effects, risk, approval, relevant REQ/DEC, management controls when relevant, base/hash, reversibility, evidence.

Postflight ต้อง verify resulting state ตาม risk; execution success อย่างเดียวไม่ prove completion.

## 14. Draft, Promotion, Archive

```text
Scratch            → outside Project-Source/
Formal candidate   → drafts/
Active truth       → Project-Source root
Historical         → archive/
```

Promotion:

```text
candidate → validate → base/hash check → promote → supersede old → archive old → sync Index/Change Log/Manifest → postflight
```

Archive เป็น Historical Truth; current resolution ห้ามพึ่ง archive. ห้าม Active revision ซ้ำ semantic identity เดียวกัน.

## 15. Index and Manifest

`01` = Front Door + derived Active registry + human/agent routing.

เมื่อ active:

```text
40 → Tech Stack / technical / source / config / runtime blueprint
60 → installation / deployment / operations
91 → RISK / ASM / MS / OUT / DEP / CR / GATE
```

`14` = Current Reconstructable Snapshot inventory. ถ้า `40`, `60`, `91` active/current และจำเป็นต่อ current truth ต้องรวมใน Manifest/CURRENT export.

ถ้า Framework Source Provenance ถูก track, `14` preserve observed state เดียวกับ active `00`; ห้าม invent missing provenance. Manifest mismatch ต้อง root-cause ก่อน regenerate.

## 16. Evidence, Knowledge Debt, and Secrets

Important evidence ใช้ `EVD-*`; raw artifacts อยู่ `evidence/<category>/`.

Material stale/missing knowledge ใช้:

```text
ISS-* in 08
issue_type: KNOWLEDGE_DEBT
```

ถ้าไม่มี active `08`, material Knowledge Debt ทำให้ `08` applicable. Runtime success ไม่ได้ลบ Knowledge Debt โดยอัตโนมัติ; Health/Readiness อาจ downgrade เมื่อ material.

**ห้ามเก็บ actual secret** ใน Project Source / Evidence / Manifest / Export. `SECRET-*` เก็บ external-reference metadata เท่านั้น:

```yaml
secret_value_present: false
```

## 17. Handoff

`09-Handoff` = Current Continuation Contract.

```text
DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED
```

Handoff ต้องมี current/pending work, active objects, required read order, freshness warnings, authority refs, `authority_transfer: false`, exact next action.

เมื่อ applicable ให้ surface active/high `RISK-*`, invalid/unverified `ASM-*`, blocking `DEP-*`, next/recent `MS-*`, Outcomes awaiting measurement, open/approved `CR-*`, upcoming/failed `GATE-*`, Technical/Deployment warnings, Source/Docker variance, Knowledge Debt.

### 17.1 Externalized Working Memory and Chat Lifecycle

Project-local binding contract:

```text
Material connector work → persist at logical checkpoint to source-native durable state.
Transient connector reads/searches → no persistence requirement by default.
GitHub → repository/canonical Project Source owner.
Drive → existing designated progress .md, else one stable PROJECT-PROGRESS.md when needed.
Persistence failure → PERSISTENCE_PENDING; no safe START_NEW_CHAT recommendation.
Chat lifecycle → CONTINUE_CURRENT_CHAT | START_NEW_CHAT.
New chat → bootstrap from persisted current state, not old transcript.
```

`Material Project Work` คือ connector-derived result/change ที่ต้องใช้ต่อเพื่อ reliable continuation, governance, decision-making หรือ execution; `Transient MCP Activity` คือ intermediate read/search/comparison ที่ไม่ต้องใช้ต่อ. Persist Material work ครั้งเดียวต่อ `Logical Checkpoint`, ไม่ใช่ทุก tool call. `PROJECT-PROGRESS.md` เป็น continuation cache เมื่อไม่มี designated progress Markdown เดิมและ durable continuation state จำเป็น; ไม่ใช่ source of truth ใหม่. Existing initialized Projects ใช้ local pinned Framework ต่อไปและไม่ auto-upgrade จาก upstream.

## 18. Technical Design — `40`

`06 Architecture` = major architecture view. `40 Technical Design` = deeper implementation-facing blueprint; deepen/reference `06`, ห้าม fork authoritative payload ซ้ำ.

Tech Stack entry เมื่อ material:

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

`40` อาจเก็บ Component Responsibility, Inputs/Outputs, Interfaces, Dependencies, Data/Storage interaction, Security/Authority Boundary, Runtime Boundary, Source Structure Blueprint, Development Workspace Contract, Configuration Contract, Runtime Requirements.

### 18.1 Development Workspace Contract

เมื่อ material ให้ `40` ระบุ/resolve:

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

Workspace/mapping labels เช่น `LOCAL_WORKSPACE`, `GIT_WORKTREE`, `REMOTE_DURABLE_WORKSPACE`, `DEV_CONTAINER_DURABLE_WORKSPACE`, `DIRECT_EXECUTION`, `BIND_MOUNT`, `WORKSPACE_VOLUME`, `IMAGE_OR_ARTIFACT_BUILD`, `REMOTE_SYNC` เป็น descriptive blueprint vocabulary ไม่ใช่ lifecycle state หรือ Stable-ID family ใหม่.

Project อาจใช้ mapping ต่างกันระหว่าง Development/Test/Staging/Production ได้ แต่ต้อง explicit เมื่อ material และไม่ขัด REQ/DEC/Technical/Deployment contracts.

Configuration Contract แยก semantic meaning ออกจาก packaging mode:

```text
Application Settings
Environment-specific Settings
External Service Endpoints
Persistence Settings
Feature / Capability Settings when material
Secret References
```

## 19. Deployment Plan — `60`

Deployment support state:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

### 19.1 Source/Docker Parity

`SOURCE_AND_DOCKER` ต้อง share one declared contract for:

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

Intentional difference ใช้ Deployment Mode Variance: Affected Capability, Source Behavior, Docker Behavior, Reason, Impact, Related IDs, Owner, Acceptance/Resolution State. Unexpected mismatch → `DRIFT-*`.

### 19.2 Installation / Operations Contract

`60` ตอบว่า resulting system ติดตั้ง/configure/start/stop/verify/diagnose/upgrade/rollback/backup/restore/cleanup/troubleshoot อย่างไรใน supported modes.

เมื่อ applicable ต้อง cover:

```text
Prerequisites
Supported OS / Platform / Architecture
Deployment Source / Artifact Acquisition
Required Runtime / Container Runtime
External Services
Required Permissions
Configuration Inputs
Secret Requirements / SECRET-* references
Source-to-Runtime Mapping
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

Install/start command success ไม่เท่ากับ operational readiness. Verification พิจารณา service availability, dependency reachability, storage initialization/persistence, configuration loaded, secrets resolved without exposure, health/runtime signal, core flow usability, running version identity, Source/Docker parity และ required-survival state ตาม declared recreation lifecycle เมื่อ applicable.

## 20. Adoption Mode and Migration

```text
GREENFIELD BROWNFIELD IMPORT
```

- GREENFIELD → canonical main bootstrap → Preview → approval → create mandatory core → evaluate conditional docs → pin Framework/Schema
- BROWNFIELD → preserve-first; ห้าม move/rename/delete legacy source อัตโนมัติ
- IMPORT → quarantine `import-staging/` ก่อน promotion

Project pin Framework/Schema version. ห้าม auto-upgrade. Framework `1.3.0` ใช้ Direct-to-Latest / Cumulative Target-State Upgrade สำหรับ upgrade ที่ได้รับอนุมัติ: compare current reconstructable Project โดยตรงกับ selected target, migrate เฉพาะ cumulative semantic delta, preserve Stable IDs/current truth/Project-Specific Rules/bindings/history, และไม่บังคับ execute intermediate release migrations. Classify exactly `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`. Skipping intermediate execution ไม่ skip assessment, Preview/approval, rollback, validation, evidence หรือ promotion. Latest starter ไม่ใช่ default destructive rebuild path สำหรับ initialized Project. ใช้ affected verification ระหว่างงานและ `RELEASE_FULL` ครั้งเดียวบน final unchanged target candidate.

### 20.1 Brownfield Slot `91` Collision

Pre-1.2.0 Project อาจใช้ `91` เป็น custom extension อยู่แล้ว. ห้าม overwrite.

```text
detect occupied 91
→ MIG-* compatibility assessment
→ preserve identity/history/references
→ propose suitable free 92–99 or other semantically correct slot
→ explicit approval
→ governed migration
→ then standard 91 activation if applicable
```

### 20.2 No Automatic Free-Text Promotion

Old prose mentioning risk/assumption/date/dependency/scope/outcome/gate ห้าม auto-create Stable IDs. Promote เป็น `RISK/ASM/MS/OUT/DEP/CR/GATE` ได้เมื่อ current semantics, status, ownership และ epistemic/evidence state เพียงพอเท่านั้น. ถ้าไม่พอ ให้ preserve uncertainty แทน fabricate identity.

Legacy `00-Project Source Rule` migration ยังใช้ preserve-first governed promotion เช่นเดิม.

### 20.3 Git Work Base Freshness and Forward-Port

เมื่อ Project ใช้ Git branch/worktree เพื่อสร้าง work package ที่จะ integrate กลับ canonical target ให้ใช้ contract นี้:

```text
Independent Git work → fresh Canonical Integration Target
Feature-on-feature dependency → explicit STACKED_WORK
STALE_NON_SEMANTIC → BASE_STALE → update/rebase appropriately → reverify → FRESH
STALE_SEMANTIC → BASE_STALE + FORWARD_PORT_REQUIRED
Before merge → Base Freshness Gate against current target head
Git conflict-free / mergeable → ไม่เท่ากับ semantic acceptance
```

Binding semantics:

1. **Independent Work** ต้องเริ่มจาก current observed Canonical Integration Target; ห้ามสร้างจาก feature branch ที่ checkout อยู่โดย default. Local `main` ไม่ได้ prove ว่า current จนกว่าจะ fresh-check canonical target.
2. Feature-on-feature dependency อนุญาตเฉพาะ explicit `STACKED_WORK` พร้อม parent ref/commit, dependency reason, invalidation condition และ expected integration order. Parent change ต้อง re-evaluate child base เมื่อ material.
3. Base Freshness vocabulary คือ `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`. `BASE_STALE` เป็น workflow condition เท่านั้น ไม่ใช่ Project state, Epistemic Status หรือ Stable-ID family.
4. Commit count ไม่ใช่ semantic threshold. ให้ดูว่า upstream เปลี่ยน Framework/Root Governance/Schema/authority/routing/REQ/DEC/interfaces/technical-deployment contracts หรือ assumption ที่งานพึ่งพาหรือไม่.
5. `STALE_NON_SEMANTIC`: ให้ mark `BASE_STALE` จนกว่า base จะถูก update ด้วยวิธีที่เหมาะสมและ affected verification จะผ่าน. Private/rewritable work อาจใช้ `REBASE_REQUIRED`; shared/public branch ใช้ history-preserving merge/update strategy ได้. หลัง update + verification สำเร็จจึงกลับ `FRESH`.
6. `STALE_SEMANTIC`: หยุด affected new implementation scope, assess changed assumptions และใช้ `FORWARD_PORT_REQUIRED` โดย default. Forward-Port ต้องสร้าง clean branch/worktree จาก current target แล้ว carry เฉพาะ still-valid accepted changes; temporary staging/transport, obsolete workflow/version metadata, superseded assumptions และ unrelated experiment ไม่ควรถูกนำเข้าเพียงเพราะอยู่ใน stale branch.
7. ก่อน acceptance/merge ต้อง fresh-resolve current target head อีกครั้ง. Target movement หลัง review อาจทำให้ review/gate เดิม stale และต้อง re-evaluate.
8. `git conflict = 0`, `mergeable = true` หรือ successful rebase ไม่ override semantic gate. **Mergeable ≠ Acceptable.**
9. เมื่อ base staleness materialize เป็น Project truth ให้ใช้ `DRIFT-* / CONFLICT-* / MIG-* / CR-*` เดิมตาม semantics; ห้ามสร้าง parallel ID family.
10. Existing Project ยังคง pinned local `FRAMEWORK-001`; upstream movement ไม่ auto-upgrade. กติกานี้ไม่ authorize Git hooks, bots, Actions, validator, scheduler หรือ branch-protection automation.

## 21. Export

Profiles:

```text
CURRENT AUDIT FULL
```

`CURRENT` ต้อง include current canonical records และ active/current Detail Documents รวม `40/60/91` เมื่อจำเป็นต่อ current truth โดยไม่พึ่ง archive. Actual secrets ห้ามอยู่ในทุก export profile.

## 22. Retention and Readiness

Preserve revisions, Decisions, Requirements, Change Log, management-control history, Identity lineage indefinitely by default. Purge ต้อง authorized, ไม่มี active refs, audit ได้ และไม่ทำลาย reconstructability.

`OPERATIONALLY_READY` หมายถึง Agent ใหม่ตอบได้โดยไม่เดา:

1. What is true now?
2. What is allowed now?
3. What must happen next?

Optional Git/repository assurance ไม่เปลี่ยน readiness โดยอัตโนมัติ เว้นแต่ Project-Specific Rule กำหนด.

## 23. Initial Creation / Structural Migration Gate

ก่อน first creation หรือ major structural migration ต้อง Preview อย่างน้อย Adoption Mode, Identity, files/directories, conditional files, known Decisions/Assumptions, Unknowns, expected readiness/risk, migration impact. ต้อง User Approval ก่อน write.

## 24. Completion Reporting

หลัง Create / Migrate / Import / Major Update / Handoff / Export ต้องรายงาน Human + Machine summary.

```text
COMPLETE PARTIAL BLOCKED FAILED
```

ต้องแยก Execution, Verification, State Confirmation. ห้าม claim DONE/DEPLOYED/MIGRATED/VALID โดยไม่มี risk-appropriate verification.

---

# Project-Specific Rules

> Child governance นี้ inherit จาก `FRAMEWORK-001`. ใช้เพิ่ม Project-specific constraint ได้ แต่ห้าม weaken/contradict Root Framework.

## PSR-001 — <TITLE>

- **Status:** `<ACTIVE / SUPERSEDED>`
- **Rule:** <PROJECT-SPECIFIC RULE>
- **Reason:** <WHY>
- **Approved By:** <USER / AUTHORIZED DECISION OWNER>
- **Approved At:** <ISO8601>
- **Related:** <DEC-### / REQ-### / AUTH-### / etc.>
