# Project Source Layered Governance Skill — Design Specification

```yaml
spec_status: APPROVED_DESIGN
spec_version: 1.0.0
generated_at: 2026-08-13T21:40:00+07:00
timezone: Asia/Bangkok
selected_architecture: LAYERED_GOVERNANCE_SKILL
decision_count: 94
design_sections: 6
implementation_status: NOT_STARTED
```

## 1. Purpose

เอกสารนี้เป็น written specification สำหรับ Skill กลางที่ใช้สร้างและดูแล `Project-Source/` ในทุก Project ให้มีโครงสร้าง, governance, naming, identity, authority, validation, handoff และ export semantics ไปในทิศทางเดียวกัน

Skill นี้ไม่ใช่เพียง Markdown generator แต่เป็น **Project Governance Bootstrap & Continuation System** ที่ต้องทำให้ Project ใด ๆ สามารถถูกเปิดโดย Human หรือ AI Agent ตัวใหม่แล้วตอบคำถามได้โดยไม่ต้องเดา:

1. **What is true now?**
2. **What is allowed now?**
3. **What must happen next?**

หลักกลาง:

> Identity must be stable. State must be explicit. History must be reconstructable. Authority must be attributable. Uncertainty must never be silently promoted to fact.

---

# 2. Selected Architecture

## 2.1 Layered Governance Skill

ผู้ใช้เรียก Skill เดียว แต่ภายในแบ่ง responsibility เป็นชั้นที่มี contract ชัดเจน:

```text
Project Source Skill
│
├── Interview & Discovery Layer
├── Governance Core
├── Identity / Authority Layer
├── Document & Object Model
├── Validation Engine
├── Lifecycle / Migration Engine
├── Handoff Engine
└── Export / Packaging Engine
```

Operational pipeline:

```text
REQUEST
  ↓
MODE RESOLUTION
  ↓
PROJECT DISCOVERY
  ↓
TRUTH DISCOVERY
  ↓
GOVERNANCE RESOLUTION
  ↓
PROJECT SOURCE MODEL
  ↓
VALIDATION
  ↓
PREVIEW / APPROVAL GATE
  ↓
CREATE / MIGRATE / IMPORT / UPDATE
  ↓
POSTFLIGHT
  ↓
HANDOFF / EXPORT
  ↓
COMPLETION REPORT
```

Architectural separations that must remain explicit:

```text
INTENT         ≠ IMPLEMENTATION
STATE          ≠ HISTORY
IDENTITY       ≠ AUTHORITY
VALID          ≠ OPERATIONALLY_READY
EXECUTED       ≠ VERIFIED_COMPLETE
ROLE           ≠ AUTHORITY
HANDOFF_ACCEPT ≠ AUTHORITY_TRANSFER
```

---

# 3. Governance Contract

## 3.1 Core + Project-Specific Rules

`00-Project Source Rule` มี 2 ชั้น:

1. **Core Rules** — มาตรฐานกลางข้าม Project
2. **Project-Specific Rules** — กฎเฉพาะ Project

ทั้งสองส่วนอยู่ภายใต้ Binding Governance และแก้ไขได้เมื่อได้รับ User Approval ตาม rule modification workflow เท่านั้น

## 3.2 Rule Precedence

ลำดับอำนาจ:

```text
1. User Explicit Instruction
2. Project-Specific Rules
3. Core Rules
4. Task / Handoff / Agent Instruction
```

Task, Handoff, Prompt, Agent Role หรือ Agent-to-Agent instruction ไม่มีสิทธิ์ override กฎระดับสูงกว่าเอง

## 3.3 Rule Modification

AI/Agent สามารถเสนอการแก้ `00-Project Source Rule` ได้ แต่ **ห้ามแก้จริงก่อน User Approval**

Core Rule ของแต่ละ Project เป็น **version-pinned snapshot** ไม่ auto-update ตาม Master Core รุ่นใหม่ ต้องใช้ `MIG-*` lifecycle เมื่อ upgrade

---

# 4. Filesystem Contract

## 4.1 Standard Location

ทุก Project ใช้ตำแหน่งมาตรฐาน:

```text
<Project-Root>/
└── Project-Source/
```

## 4.2 Core Structure

```text
<Project-Root>/
│
├── Project-Source/
│   │
│   ├── 00-Project Source Rule-r###-YYMMDD-HHMM.md
│   ├── 01-Project Source Index-r###-YYMMDD-HHMM.md
│   ├── 02-Project Overview-r###-YYMMDD-HHMM.md
│   ├── 03-Current State-r###-YYMMDD-HHMM.md
│   ├── 04-Decision Log-r###-YYMMDD-HHMM.md
│   ├── 05-Requirements-r###-YYMMDD-HHMM.md
│   ├── 06-Architecture-r###-YYMMDD-HHMM.md              # CONDITIONAL
│   ├── 07-Implementation Plan-r###-YYMMDD-HHMM.md       # CONDITIONAL
│   ├── 08-Open Issues-r###-YYMMDD-HHMM.md               # CONDITIONAL
│   ├── 09-Handoff-r###-YYMMDD-HHMM.md
│   ├── 10-Change Log-r###-YYMMDD-HHMM.md
│   ├── 11-Actor Registry-r###-YYMMDD-HHMM.md
│   ├── 12-Authorization Registry-r###-YYMMDD-HHMM.md
│   ├── 13-Evidence Registry-r###-YYMMDD-HHMM.md
│   ├── 14-Project Source Manifest-r###-YYMMDD-HHMM.md
│   ├── 15-Action Registry-r###-YYMMDD-HHMM.md
│   ├── 16-Migration Registry-r###-YYMMDD-HHMM.md
│   ├── 17-Secret Reference Registry-r###-YYMMDD-HHMM.md
│   │
│   ├── drafts/
│   ├── evidence/
│   │   ├── git/
│   │   ├── runtime/
│   │   ├── test/
│   │   ├── screenshot/
│   │   ├── data/
│   │   ├── external/
│   │   └── other/
│   ├── schema/
│   ├── import-staging/
│   └── archive/
│       ├── 00-19-core/YYYY/MM/
│       ├── 20-29-research/YYYY/MM/
│       ├── 30-39-design/YYYY/MM/
│       ├── 40-49-technical/YYYY/MM/
│       ├── 50-59-testing/YYYY/MM/
│       ├── 60-69-operations/YYYY/MM/
│       ├── 70-79-data/YYYY/MM/
│       ├── 80-89-reports/YYYY/MM/
│       └── 90-99-special/YYYY/MM/
│
├── src/
├── docs/
└── ...
```

`18–19` สงวนไว้สำหรับ future core governance expansion

## 4.3 Mandatory vs Conditional

**Mandatory:** `00–05`, `09–17`

**Conditional:**
- `06-Architecture`
- `07-Implementation Plan`
- `08-Open Issues`

Conditional documents ถูกสร้างโดย Agent ได้เมื่อ criteria ชัดเจน; ถ้า ambiguity สูงต้องถามผู้ใช้ก่อน ห้ามสร้างไฟล์เปล่าเพียงเพื่อให้ดูครบ

---

# 5. Global Number Taxonomy

```text
00–19  Core Governance Namespace
20–29  Research / Discovery
30–39  Business / Process / UX Design
40–49  Architecture / Technical / Integration
50–59  Testing / QA / Validation
60–69  Deployment / Operations / Infrastructure
70–79  Data / Migration / Analytics
80–89  Audit / Review / Assessment / Reports
90–99  Project-specific / Governance Extension
```

Reserved anchors:

```text
20 = General Research
30 = Business / Process Flow
40 = Technical Design
50 = Test Strategy
60 = Deployment Plan
70 = Data Model
80 = Review / Assessment Report
90 = Special Governance Extension
```

เอกสาร Extended ใช้ Stable Document ID เพื่อแยก identity ออกจาก taxonomy location

---

# 6. Filename and Revision Contract

## 6.1 Timestamp

Project Source / Handoff / Export / Package และ governed evidence/schema artifacts ที่สร้างใหม่ต้องลงท้าย basename ด้วย:

```text
-YYMMDD-HHMM
```

เวลาใช้ Project/User timezone โดย default; Project-Specific Rule สามารถกำหนด timezone อื่นได้

## 6.2 Revision

รูปแบบ:

```text
r001
r002
...
r999
r1000
r1001
```

Revision:
- monotonic
- ห้าม reuse
- metadata `revision` ต้องตรง filename
- revision 1000 ขึ้นไปขยายจำนวนหลักอัตโนมัติ

Core example:

```text
05-Requirements-r007-260813-2140.md
```

Extended example:

```text
22-RSCH-004-GPU-Benchmark-r003-260813-2140.md
```

Canonical implementation files เช่น `README.md`, `main.py`, `docker-compose.yml` ไม่ถูกบังคับ timestamp; timestamp ใช้กับ Project Source และ delivery/package layer

---

# 7. Document Responsibilities

| Slot | Document | Primary Responsibility |
|---|---|---|
| 00 | Project Source Rule | Governance contract |
| 01 | Project Source Index | Front Door + Routing + Generated Active Registry |
| 02 | Project Overview | Identity, objective, scope, context |
| 03 | Current State | Pure current snapshot |
| 04 | Decision Log | Canonical home of `DEC-*` |
| 05 | Requirements | Canonical home of `REQ-*` |
| 06 | Architecture | Current architecture when applicable |
| 07 | Implementation Plan | Current approved implementation plan |
| 08 | Open Issues | Canonical home of `ISS-*`, `DRIFT-*`, `CONFLICT-*` |
| 09 | Handoff | Current continuation contract |
| 10 | Change Log | Logical append-only `CHG-*` audit history |
| 11 | Actor Registry | `ACTOR-*`, `INST-*` |
| 12 | Authorization Registry | `AUTH-*`, `DEL-*` |
| 13 | Evidence Registry | `EVD-*` |
| 14 | Manifest | Current reconstructable snapshot inventory + hashes |
| 15 | Action Registry | `ACT-*` |
| 16 | Migration Registry | `MIG-*` |
| 17 | Secret Reference Registry | `SECRET-*` metadata only |

`03` และ `09` เป็น reference/snapshot views ไม่ใช่ authoritative registry ของ object

---

# 8. Canonical Object Homes

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
```

Object ที่ซับซ้อนสามารถมี Detail Document ใน Extended taxonomy ได้ แต่ authoritative identity/status/link ยังคงอยู่ที่ Canonical Home

---

# 9. YAML Metadata Contract

## 9.1 Scope

**Governed Project Source Markdown documents** ทุกไฟล์ต้องมี YAML Front Matter และผ่าน schema validation

Binary evidence, images, logs, JSON exports, schema snapshots หรือ non-Markdown artifacts ไม่ต้องมี YAML Front Matter ในตัวไฟล์ แต่ต้องถูกควบคุมผ่าน native structure + `EVD-*`/Manifest/Registry metadata ที่เกี่ยวข้อง

## 9.2 Universal Example

```yaml
---
project_uuid: "uuid"
project_id: "MCIT-MOBILE"
project_name: "MCIT Mobile Platform"

document_id: "STATE-001"
document_type: "CURRENT_STATE"
semantic_slot: "03"
revision: 9
document_status: "ACTIVE"

created_at: "2026-08-10T14:22:00+07:00"
updated_at: "2026-08-13T21:40:00+07:00"
created_by: "ACTOR-003"
created_by_instance: "INST-20260813-004"

base_revision: 8
base_document_hash: "sha256:..."

epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
verified_at: "2026-08-13T21:39:00+07:00"

project_source_rule_version: "1.0.0"
project_source_schema_version: "1.0.0"
compatible_rule_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
```

Fields ถูก classify เป็น `REQUIRED / CONDITIONAL / FORBIDDEN / DERIVED` ต่อ `document_type`

---

# 10. Project Identity and Lineage

## 10.1 Identity Layers

```text
project_uuid → immutable authoritative identity
project_id   → stable human-readable identity
project_name → mutable display name
```

Rename ไม่เปลี่ยน UUID

## 10.2 Identity History

Identity changes เป็น event-based history เช่น:

```text
CREATED
RENAMED
PROJECT_ID_CHANGED
ABSORBED
ABSORPTION_RECEIVED
TRUE_MERGE_CREATED
CARVE_OUT_CREATED
TRUE_SPLIT_CREATED
ARCHIVED
REACTIVATED
```

## 10.3 Merge

**Absorption:** Project หลักคง UUID เดิม; Project ที่ถูก absorb เก็บ UUID เดิมใน history และ lifecycle เป็น `ABSORBED`

**True Merge:** สร้าง UUID ใหม่; predecessors อยู่ใน lineage และ lifecycle historical ตาม merge semantics

## 10.4 Split

**Carve-out:** Project หลักคง UUID เดิม; Project ที่แยกออกได้ UUID ใหม่

**True Split:** Project เดิมจบ lifecycle; descendants ได้ UUID ใหม่ทั้งหมด

---

# 11. Project State Model

## 11.1 Lifecycle State

```text
DRAFT
ACTIVE
COMPLETED
CANCELLED
ARCHIVED
ABSORBED
MERGED
SPLIT
```

## 11.2 Execution State

```text
READY
IN_PROGRESS
WAITING
BLOCKED
IDLE
```

Lifecycle และ Execution State เป็นคนละแกน เช่น:

```yaml
lifecycle_state: ACTIVE
execution_state: BLOCKED
```

แต่ combination ที่เป็นไปไม่ได้ เช่น `ARCHIVED + IN_PROGRESS` ต้อง validation fail

---

# 12. Object Lifecycles

## REQ-*

```text
DRAFT → APPROVED → IMPLEMENTED → VERIFIED
side exits: REJECTED / SUPERSEDED
```

## DEC-*

```text
PROPOSED → APPROVED → SUPERSEDED
APPROVED → REVOKED
```

## ISS-*

```text
OPEN → BLOCKED → RESOLVED → CLOSED
OPEN → RESOLVED → CLOSED
```

## DRIFT-*

```text
OPEN → INVESTIGATING → RECONCILING → RECONCILED → CLOSED
```

## CONFLICT-*

```text
OPEN → RECONCILING → RESOLVED → CLOSED
```

## ACT-*

```text
TODO → IN_PROGRESS → DONE
side states: BLOCKED / CANCELLED
```

## AUTH-*

```text
PENDING → ACTIVE
ACTIVE ↔ SUSPENDED
ACTIVE → CONSUMED / EXPIRED / REVOKED
```

## DEL-*

```text
PENDING → ACTIVE → EXPIRED
ACTIVE → REVOKED / CONSUMED
```

## MIG-*

```text
CURRENT → ASSESSED → APPROVED → MIGRATING → VALIDATING → COMPLETED
side states: BLOCKED / ROLLED_BACK / CANCELLED
```

## Handoff

```text
DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED
```

---

# 13. Epistemic and Freshness Model

## 13.1 Epistemic Status

```text
VERIFIED
USER_CONFIRMED
INFERRED
ASSUMED
UNKNOWN
CONFLICTED
STALE
```

Agent ห้ามยกระดับ `ASSUMED`/`INFERRED` เป็น `VERIFIED` โดยไม่มี evidence/authoritative verification

## 13.2 Freshness Class

```text
IMMUTABLE
STABLE
CHANGEABLE
VOLATILE
```

`VOLATILE` ต้อง fresh-check ก่อนใช้กับ decision/mutation ที่เกี่ยวข้อง

---

# 14. Truth Domain Model

Canonical domains:

```text
GOVERNANCE
INTENT
REQUIREMENTS
IMPLEMENTATION
RUNTIME
DATA
IDENTITY
AUTHORITY
HISTORY
EXTERNAL
```

Authoritative mapping หลัก:

| Domain | Authoritative Source |
|---|---|
| GOVERNANCE | Approved `00` rules |
| INTENT | User-approved Project Source |
| REQUIREMENTS | `05-Requirements` |
| IMPLEMENTATION | Verified source tree / Git |
| RUNTIME | Fresh runtime observation |
| DATA | Actual authoritative datasource |
| IDENTITY | Identity metadata/history |
| AUTHORITY | `12-Authorization Registry` |
| HISTORY | `10-Change Log` + archived records |
| EXTERNAL | Verified external source/system |

เมื่อ Truth Domains ขัดกัน Skill ต้องเปิด `DRIFT-*` ไม่เลือกฝั่งเอง

---

# 15. DRIFT Contract

`DRIFT-*` ต้องมีอย่างน้อย:

- Expected Truth
- Observed Truth
- Truth Domains
- Evidence
- Impact
- Affected Scope
- Status
- Resolution Owner
- Mutation Block
- Freshness
- Related Objects

Drift block เป็น **scoped block** โดย default ไม่ freeze ทั้ง Project

ก่อน `RECONCILED` ต้องมี root cause, governed resolution, post-resolution evidence, Current State update, Change Log update และ revalidation

---

# 16. CONFLICT Contract

Canonical conflict types:

```text
CONCURRENT_REVISION
SEMANTIC_EDIT
IDENTITY_COLLISION
OBJECT_ID_COLLISION
IMPORT_COLLISION
MIGRATION_COLLISION
REFERENCE_COLLISION
```

Auto-resolve ได้เฉพาะ `NON_SEMANTIC` differences เช่น formatting/whitespace/deterministic sorting/typo ที่ไม่เปลี่ยน meaning

Semantic conflict ต้อง route ให้ User หรือ Authorized Decision Owner ผ่าน standardized conflict packet

---

# 17. Concurrency and Promotion

Formal Candidate Revision ต้องมี:

```yaml
base_revision: 7
base_document_hash: "sha256:..."
```

ก่อน promote ต้องตรวจ optimistic concurrency:

- base ตรง Active → promote ได้
- base stale → `CONFLICT-*`, ห้าม promote

Two-phase supersede:

```text
CREATE CANDIDATE
→ VALIDATE
→ BASE/HASH CHECK
→ PROMOTE NEW ACTIVE
→ MARK OLD SUPERSEDED
→ ARCHIVE OLD
→ UPDATE INDEX
→ UPDATE CHANGE LOG
→ REGENERATE MANIFEST
→ POSTFLIGHT
```

ห้ามปล่อย Project Source อยู่ในสภาพครึ่งเก่าครึ่งใหม่

---

# 18. Draft Model

```text
Scratch / exploratory draft → outside Project-Source/
Formal candidate draft       → Project-Source/drafts/
Active truth                 → Project-Source root
Historical revision          → Project-Source/archive/
```

`01-Index` ห้าม route formal draft เป็น Active Truth

---

# 19. Index Contract

`01-Project Source Index` มี 2 ส่วน:

## 19.1 Machine-generated Registry

ห้ามแก้มือ; derive จาก governed metadata จริง

ตรวจอย่างน้อย:
- Active docs ครบ
- ไม่มี archive/superseded path ถูก route Active
- document ID/revision/status/path ตรง
- mandatory docs ครบ
- ไม่มี Active Source of Truth ซ้ำ semantic slot

Manual edit ใน generated section = Governance Violation + validation failure + promotion blocked

## 19.2 Human/Agent Routing

ตัวอย่าง routing:

```text
Requirement Review: 00 → 01 → 03 → 04 → 05
Implementation:      00 → 01 → 03 → 04 → 05 → 06 → 07 → 12 → 15
Continuation:        00 → 01 → 03 → 09 → 11 → 12 → task-specific docs
```

---

# 20. Manifest Contract

`14-Project Source Manifest` ครอบคลุม **Current Reconstructable Snapshot**:

- Active documents
- continuation-relevant formal drafts
- registered evidence artifacts
- schema/validation contract snapshots
- generated assets ที่จำเป็นต่อ reconstruction

ไม่รวม historical archive ทั้งหมดใน Active Manifest

Manifest ต้องมี `document_id / path / revision / status / sha256` ตามชนิด artifact

**Self-reference rule:** Manifest ไม่ hash raw bytes ของไฟล์ manifest ตัวเองใน entry list เพื่อหลีกเลี่ยง recursive hash. หากต้องการตรวจ internal manifest integrity ให้ใช้ canonical payload hash ที่คำนวณจาก normalized manifest payload โดย exclude field ที่เก็บ hash ของตัวเอง

Manifest hash mismatch ต้องแยกว่าเป็น expected authorized mutation หรือ unexpected mutation; ห้าม regenerate แล้วถือว่าจบโดยไม่ตรวจ root cause

---

# 21. Change Log Contract

`10-Change Log` เป็น **logical append-only audit history**: `CHG-*` ที่เคยบันทึกแล้วห้าม rewrite/delete เพื่อเปลี่ยนประวัติ

ตัวไฟล์ `10-Change Log` เองยังอยู่ภายใต้ normal document revision model: revision ใหม่สามารถ append entries ใหม่และ archive revision เก่าได้ แต่ historical `CHG-*` content ต้องคง reconstructable และ immutable เชิงความหมาย

Substantive triggers เช่น:
- revision promotion
- requirement/decision state change
- identity/authority change
- DRIFT/CONFLICT change
- migration state change
- audit-relevant evidence/export

---

# 22. Actor and Instance Model

`ACTOR-*` = stable actor identity

`INST-*` = session/execution instance

Actor types:

```text
HUMAN
AI_AGENT
AUTOMATION
SERVICE
SYSTEM
```

Role ไม่เท่ากับ Authority

Mutation สำคัญต้อง trace ได้ทั้ง actor + instance

---

# 23. Authorization Model

Standing Authorization `AUTH-*` ต้องมี:

```text
WHO
WHAT
WHERE
RISK CEILING
START
END / TERMINATION CONDITION
GRANTED BY
```

ห้าม broad indefinite authorization แบบคลุมเครือ

Authorization lifecycle ใช้ Section 12

Authority = `CHANGEABLE`; R2/R3 preflight ต้อง fresh-read จาก `12-Authorization Registry`

---

# 24. Strict Non-transfer and Delegation

Authority ห้ามถ่ายโอนผ่าน:

```text
Prompt
Task
Handoff
Memory
Role name
Branch
Agent-to-Agent instruction
```

ถ้าจะ delegate ใช้ `DEL-*`

Invariants:

```text
Delegated Scope    <= Parent Scope
Delegated Risk     <= Parent Risk
Delegated Duration <= Parent Duration
Delegated Actions  ⊆ Parent Actions
```

Parent `AUTH-*` invalid → descendant `DEL-*` ใช้งานไม่ได้ทันที

---

# 25. Risk Model

```text
R0 — READ_ONLY
R1 — REVERSIBLE_LOCAL
R2 — SHARED_STATE
R3 — EXTERNAL_OR_IRREVERSIBLE
```

Effective Risk = action + target + reversibility + blast radius + external effect

## Approval Matrix

| Risk | Default Approval |
|---|---|
| R0 | None |
| R1 | Allowed within approved scope |
| R2 | Explicit approval or valid Standing Authorization |
| R3 | Explicit approval for that specific action |

Project-Specific Rule เพิ่มความเข้มได้

R3 Standing Authorization เพียงอย่างเดียวไม่พอโดย default เว้นแต่มี explicit user override ที่ครอบ action class นั้นโดยชัดเจน

---

# 26. Preflight Model

## 26.1 READ PREFLIGHT

ตรวจอย่างน้อย:

1. Project identity
2. `00`
3. `01`
4. `03`
5. Task scope
6. Relevant Truth Domain
7. Relevant freshness
8. Active DRIFT / CONFLICT / blocker

## 26.2 MUTATION PREFLIGHT

ตรวจเพิ่ม:

- Actor / Instance
- Authority
- Exact task/target
- Allowed paths
- Forbidden effects
- Risk
- Approval
- Relevant REQ/DEC
- Active blocks
- Base revision/hash
- Downstream impact
- Rollback/reversibility
- Evidence requirement

Mutation ถูก block เมื่อ identity/authority/approval/freshness/concurrency/scope/lifecycle/preconditions ไม่ผ่าน

---

# 27. Postflight Model

## R1

- intended change occurred
- unintended paths untouched
- schema/naming/references valid
- Index/Manifest synchronized as applicable

## R2

เพิ่ม:
- shared target state verified
- diff/commit/remote evidence as applicable
- forbidden effects absent
- registries updated
- `EVD-*` required

## R3

เพิ่ม:
- actual external/runtime resulting state verified
- exact applied/deployed version
- rollback state
- side effects
- affected scope
- approval evidence
- post-action freshness

Command exit code 0 ไม่เท่ากับ verified success

---

# 28. Evidence Model

`EVD-*` mandatory สำหรับหลักฐานสำคัญ เช่น:
- Major Decision evidence
- DRIFT
- R2/R3 mutation verification
- runtime/external state
- conflicts between sources

Raw artifacts เก็บใน `evidence/<category>/` และ timestamp filename

Evidence Registry เก็บ metadata/path/hash/supports references

R0 evidence optional; R1 when semantically important; R2 shared mutation evidence required; R3 evidence required

---

# 29. Secret Handling

ห้ามเก็บ actual secret ใน:

- Project Source Markdown
- Evidence artifact
- Manifest
- Export ZIP

ใช้ `SECRET-*` metadata only:

- secret type
- system/environment
- storage reference
- required authority
- status
- `secret_value_present: false`

Actual secret exposure อย่างน้อย `ERROR`; ถ้า shared/exfiltrated อาจ `CRITICAL`

---

# 30. Validation Engine

Validation 5 ชั้น:

```text
L1 Syntax
L2 Structural
L3 Referential
L4 Semantic
L5 Integrity / Operational
```

## L1 Syntax

YAML, types, timestamps, UUID, enum, filename/revision

## L2 Structural

Mandatory files, folders, draft/archive/evidence/schema/import staging placement

## L3 Referential

Stable IDs, canonical homes, supersedes, authority chains, evidence paths, detail document links

## L4 Semantic

Lifecycle transitions, authority escalation, lineage, Active Truth uniqueness, Handoff semantics

## L5 Operational

Index sync, Manifest integrity, routing, fresh volatility, evidence requirement, readiness

---

# 31. Validation Severity

```text
INFO
WARNING
ERROR
CRITICAL
```

- `INFO`: informational
- `WARNING`: should fix; unrelated work can continue
- `ERROR`: block affected mutation/promotion/export
- `CRITICAL`: integrity/identity/authority/governance failure; immediately block affected scope

Validation result และ Operational Readiness เป็นคนละ field

ตัวอย่าง valid state:

```yaml
validation_status: PASS
operational_readiness: NOT_READY
```

---

# 32. SAFE_FIX vs GOVERNED_FIX

## SAFE_FIX

Whitelist only:
- formatting
- deterministic sorting
- generated Index regeneration
- Manifest regeneration after authorized change
- path normalization
- deterministic derived metadata/hash refresh

## GOVERNED_FIX

ใช้ normal mutation workflow หากกระทบ:
- Requirement
- Decision
- Scope
- Authority
- Identity
- lineage
- Risk
- Source of Truth
- DRIFT
- CONFLICT
- lifecycle meaning

Validator ตรวจพบได้ แต่ห้ามตัดสิน semantic truth เอง

---

# 33. Adoption Modes

```text
GREENFIELD
BROWNFIELD
IMPORT
```

## GREENFIELD

สร้างมาตรฐานเต็มหลัง Preview → User Approval

## BROWNFIELD

Preserve-first:

```text
DISCOVER → INVENTORY → CLASSIFY → TRUTH-MAP → DRIFT-DETECT → PREVIEW → APPROVAL → GOVERNANCE LAYER → CONTROLLED NORMALIZATION
```

ห้าม move/rename/delete legacy source โดยอัตโนมัติ

Legacy migration states:

```text
LEGACY_DISCOVERED
LEGACY_REFERENCED
MIGRATION_PENDING
NORMALIZING
NORMALIZED
SUPERSEDED
PRESERVED_EXTERNAL
```

## IMPORT

Import ต้องเข้า `import-staging/` ก่อน และยังไม่เป็น trusted/active truth

Compatibility results:

```text
COMPATIBLE
UPGRADE_REQUIRED
CONFLICTED
INVALID
```

---

# 34. Evidence-weighted Brownfield Discovery

Skill ต้อง classify source ตาม:

- Truth Domain
- Epistemic Status
- Freshness
- Evidence quality

ห้ามใช้ “ไฟล์ใหม่สุดชนะ” หรือ “runtime ชนะทุกเรื่อง”

User-approved Decision authoritative ด้าน intent; fresh Git/source authoritative ด้าน implementation; fresh runtime authoritative ด้าน runtime; conflict → `DRIFT-*`

---

# 35. Migration Model

`MIG-*` canonical home = `16-Migration Registry`

ใช้กับ:
- Rule/Schema upgrade
- Brownfield normalization
- Import compatibility upgrade
- structural migration

Migration ต้องมี:
- source version/state
- target version/state
- compatibility assessment
- affected docs/objects
- steps
- rollback
- approval
- validation
- evidence

Classify reversibility:

```text
REVERSIBLE
PARTIALLY_REVERSIBLE
IRREVERSIBLE
```

Migration promotion เป็น two-phase; old Active Set ยังคง authoritative จน candidate set validate ผ่านและ promote สำเร็จ

---

# 36. Rule and Schema Versioning

ทุก Project pin:

```yaml
project_source_rule_version: "x.y.z"
project_source_schema_version: "x.y.z"
compatible_rule_range: "..."
compatible_schema_range: "..."
```

Project เก่าไม่ auto-upgrade

Core รุ่นใหม่:

```text
DETECT → COMPATIBILITY ASSESS → MIG-* → USER APPROVAL → MIGRATE → VALIDATE → PROMOTE
```

Project-Specific Rules ต้อง preserve หาก compatible; conflict ต้อง block migration จนตัดสิน

---

# 37. Schema and Validation Assets

แต่ละ Project เก็บ pinned validation contract/schema snapshot ใน:

```text
Project-Source/schema/
```

ชื่อ artifact ต้อง timestamp ตาม naming contract

Validator execution logic ใช้จาก Skill/Tool กลาง แต่ต้อง validate Project ตาม pinned contract ไม่ใช่ latest schema โดยอัตโนมัติ

Schema assets ต้องอยู่ใน Manifest

---

# 38. Handoff Contract

`09-Handoff` = Current Continuation Contract, ไม่ใช่แค่ chat summary

ต้องมี:
- handoff from/to
- previous handoff
- trigger
- current phase/state
- completed work
- pending work
- WIP/formal drafts
- active actions/issues/drifts/conflicts
- required read order
- authority references (`authority_transfer: false`)
- freshness warnings
- exact next action

Handoff trigger = event-driven + user-requested

---

# 39. Freshness-aware Handoff Acceptance

ก่อน `ACCEPTED` ผู้รับต้องอ่านขั้นต่ำ:

```text
00 → 01 → 03 → 09
```

และตรวจ:
- Actor
- `11`
- `12`
- relevant Actions/Issues/Drifts/Conflicts
- volatile state
- Handoff current revision

Semantic divergence → ห้าม silently accept; เปิด DRIFT/CONFLICT ตาม semantics

---

# 40. Export Profiles

```text
CURRENT
AUDIT
FULL
```

## CURRENT

Active snapshot + schema/manifest + current evidence + continuation-relevant formal drafts + current handoff

Formal drafts ต้องแยก path และ mark:

```text
NOT_ACTIVE_SOURCE_OF_TRUTH
```

## AUDIT

CURRENT + relevant historical revisions/evidence/change/identity/migration/handoffs

## FULL

Project-Source ทั้งหมดรวม archive ยกเว้น actual secrets

Filename:

```text
<Project-ID>-Project-Source-<PROFILE>-YYMMDD-HHMM.zip
```

---

# 41. Export Validation Gate

ก่อน export ต้อง validate:

- mandatory structure
- YAML/schema
- references
- semantic rules
- Index sync
- Manifest integrity
- secret scan
- profile completeness
- Active Truth uniqueness
- required evidence

Open Issue/DRIFT/CONFLICT ที่เปิดเผยถูกต้องไม่ทำให้ export fail โดยตัวมันเอง

Invalid package ห้ามใช้ standard valid export naming/metadata โดยไม่ระบุ invalid/staging semantics ชัดเจน

---

# 42. Retention Policy

Default preserve indefinitely:

- Project Source revisions
- Decisions
- Requirements
- Change Log
- Identity lineage

Evidence ใช้ Project-Specific retention

Scratch/obsolete drafts cleanup ได้ตาม lifecycle/policy

Historical purge ต้อง:
- authorized
- ไม่ถูก Active Object อ้าง
- auditable
- ไม่ทำลาย required reconstructability

---

# 43. Interview Model

Modes:

```text
FAST
GRILL
ADAPTIVE
```

Default = `ADAPTIVE`

- FAST: ถามเท่าที่จำเป็น
- GRILL: ปิด ambiguity เชิงลึก
- ADAPTIVE: ปรับตาม complexity/risk/multi-agent/production impact/context completeness

Ask vs infer:

```text
CAN VERIFY?              → VERIFY
CAN DERIVE SAFELY?       → INFERRED
NON-CRITICAL UNKNOWN?    → RECORD UNKNOWN
SEMANTIC DECISION?       → ASK USER
AUTHORITY REQUIRED?      → RESOLVE / ASK
DANGEROUS AMBIGUITY?     → BLOCK AFFECTED SCOPE
```

ห้ามถามข้อมูลที่ตรวจได้จาก source ที่เข้าถึงได้ และห้าม invent เพื่อหลีกเลี่ยงการถาม

---

# 44. Controlled Incomplete State

Project Source สามารถเป็น:

```text
VALID + NOT_OPERATIONALLY_READY
```

ได้หาก uncertainty ถูก model ชัดเจนด้วย:

```text
UNKNOWN
ASSUMED
STALE
CONFLICTED
VERIFICATION_REQUIRED
```

พร้อม `ACT-* / ISS-* / DRIFT-*` ตามความจำเป็น

ห้ามใช้ assumption เติมช่องว่างเพื่อทำให้เอกสารดู complete

---

# 45. Initial Creation Gate

ก่อน initial Project Source creation หรือ structural migration ครั้งใหญ่ Skill ต้องแสดง Preview อย่างน้อย:

- Adoption Mode
- Project Identity
- Files/directories to create
- Conditional files
- Known Decisions
- Known Assumptions
- Unknowns
- Expected Readiness
- Expected Risk
- Migration impact

ต้องมี User Approval ก่อน create/migrate

หลังสร้างแล้ว routine R1 update ใช้ Authority Matrix ปกติ

---

# 46. Operational Workflows

## 46.1 GREENFIELD

```text
REQUEST
→ MODE
→ DISCOVERY
→ IDENTITY
→ INTERVIEW
→ PREVIEW
→ USER APPROVAL
→ CREATE CORE
→ REGISTRIES
→ INDEX + MANIFEST
→ VALIDATE
→ POSTFLIGHT
→ READINESS
→ COMPLETION REPORT
```

## 46.2 BROWNFIELD

```text
REQUEST
→ READ-ONLY DISCOVERY
→ LEGACY INVENTORY
→ TRUTH MAP
→ FRESHNESS/EVIDENCE
→ DRIFT/CONFLICT
→ ADOPTION PREVIEW
→ USER APPROVAL
→ GOVERNANCE LAYER
→ CONTROLLED NORMALIZATION
→ VALIDATE
→ COMPLETION REPORT
```

## 46.3 IMPORT

```text
PACKAGE
→ IMPORT-STAGING
→ INTEGRITY
→ IDENTITY
→ COMPATIBILITY
→ COMPATIBLE / UPGRADE / CONFLICT / INVALID
→ PREVIEW / MIGRATION / RESOLUTION
→ APPROVAL
→ PROMOTE
```

## 46.4 NORMAL UPDATE

```text
READ PREFLIGHT
→ ROUTE CONTEXT
→ RISK
→ MUTATION PREFLIGHT
→ AUTHORITY / APPROVAL
→ CANDIDATE REVISION
→ VALIDATE
→ CONCURRENCY CHECK
→ TWO-PHASE PROMOTION
→ ARCHIVE OLD
→ REGENERATE INDEX / MANIFEST
→ POSTFLIGHT
→ CHANGE LOG
→ HANDOFF REFRESH IF TRIGGERED
```

---

# 47. Failure Semantics

Skill ต้องแยก:

```text
FAILED
BLOCKED
PARTIAL
INVALID
NOT_READY
```

- `FAILED`: operation execute แล้วแต่ไม่สำเร็จตาม contract
- `BLOCKED`: ยังไม่ execute เพราะ precondition/authority/conflict ไม่ผ่าน
- `PARTIAL`: บาง scope verify complete บาง scope ไม่เสร็จ
- `INVALID`: artifact/state ไม่ผ่าน validation contract
- `NOT_READY`: Project Source valid แต่ยังไม่ operationally ready

---

# 48. Completion Report

หลัง Create / Migrate / Import / Major Update / Handoff / Export ต้องมี Human-readable + Machine-readable summary

Canonical completion statuses:

```text
COMPLETE
PARTIAL
BLOCKED
FAILED
```

Machine summary ต้องมีอย่างน้อย:

- project_id / project_uuid
- operation
- Adoption Mode
- Rule/Schema versions
- validation status/severity counts
- operational readiness
- created/revised/archived docs
- active ACT/ISS/DRIFT/CONFLICT
- authority state
- UNKNOWN/STALE/VERIFICATION_REQUIRED
- exact next action
- export artifact if any

Completion claim ต้องแยก:

```text
ACTION_EXECUTED
VERIFICATION_PASSED
STATE_CONFIRMED
```

ห้ามประกาศ DONE/DEPLOYED/PUSHED/MIGRATED/VALID จน postflight ตาม risk tier ผ่าน

---

# 49. Operational Readiness

Readiness concepts:

```text
UNINITIALIZED
INVALID
VALID + NOT_OPERATIONALLY_READY
VALID + OPERATIONALLY_READY
```

Project Source ถือ `OPERATIONALLY_READY` เมื่อ:

- Mandatory documents ครบ
- Full Semantic Validation ผ่าน
- Index synchronized
- Manifest synchronized
- Identity/lineage valid
- Rule/schema compatibility valid
- Current State current enough
- relevant volatility fresh
- important Requirements/Decisions canonical
- Actor/Authority valid
- Active Actions registered
- Issues/DRIFT/CONFLICT disclosed
- current Handoff available when continuation exists
- Secret policy passes
- required Evidence exists
- no hidden ambiguity requiring guesswork
- exact next action determinable when Project continues

`OPERATIONALLY_READY` ไม่เท่ากับ “ไม่มี blocker” หรือ “Project เสร็จ”

---

# 50. Core Design Invariants

1. **One authoritative home per object type**
2. **One Active revision per semantic document identity**
3. **Stable IDs are never recycled**
4. **Revision numbers are monotonic and never reused**
5. **History remains reconstructable**
6. **Draft never silently becomes Active Truth**
7. **Index generated registry is derived, not manually authoritative**
8. **Manifest integrity failures require root-cause classification**
9. **Authority is explicit, scoped, fresh, attributable and non-transferable by default**
10. **R3 requires action-specific explicit approval by default**
11. **Execution alone does not prove completion**
12. **Truth conflicts become DRIFT, not silent reconciliation**
13. **Concurrent semantic edits become CONFLICT, not last-write-wins**
14. **Preserve before normalize**
15. **Validate before promote**
16. **Uncertainty stays explicit**
17. **Actual secrets never enter Project Source or exports**
18. **Project Source must remain context-complete enough for new-agent continuation**

---

# 51. Definition of Done for This Skill Design

Design ถือว่าปิดเมื่อ:

- 94 user decisions ถูก capture
- 6 design sections approved
- architecture selected = Layered Governance Skill
- filesystem/taxonomy defined
- metadata/object/lifecycle model defined
- authority/risk/preflight/postflight defined
- validation/drift/conflict/migration/import/brownfield defined
- handoff/export/completion/readiness defined
- no unresolved placeholders in this specification
- no known internal contradiction remains after self-review

Implementation ยัง **ไม่เริ่ม** จนกว่าผู้ใช้ review written specification และอนุมัติให้เข้าสู่ implementation planning

---

# Appendix A — Decision Register (94 Decisions)

| # | Selected | Binding Decision |
|---:|:---:|---|
| 1 | D | Timestamp applies to Project Source/Handoff/Export/Package; canonical implementation filenames remain canonical. |
| 2 | B | Core Rules + Project-Specific Rules. |
| 3 | C | `00-Project Source Rule` is Binding Rule. |
| 4 | B | Agent may propose rule changes; user approval required before modification. |
| 5 | B | Precedence: User Explicit > Project-Specific > Core > Task/Handoff. |
| 6 | C | Standard detailed Project Source taxonomy across Projects. |
| 7 | B | Mandatory minimum file set exists. |
| 8 | C | New revision + archive superseded revision. |
| 9 | A | Timestamp format = `YYMMDD-HHMM`. |
| 10 | B | Project Source is context-complete/self-contained for important context; detail may be referenced. |
| 11 | B | Human-readable content + structured metadata. |
| 12 | B | `01-Project Source Index` is mandatory Front Door. |
| 13 | B | Standard location = `/Project-Source/`. |
| 14 | C | Global numbering standard. |
| 15 | D | Core mandatory set with `06–08` conditional reserved slots. |
| 16 | D | Conditional files created automatically when clearly applicable; ask when ambiguous. |
| 17 | D | Two-layer Decision model: major/binding in Decision Log; details elsewhere. |
| 18 | C | Stable IDs for `REQ/DEC/ISS/ACT`. |
| 19 | D | Object-specific status schemas. |
| 20 | D | Current state + append-only audit Change Log. |
| 21 | A | `10-Change Log` mandatory. |
| 22 | C | Global semantic number-range taxonomy. |
| 23 | C | Number range + Stable Document ID. |
| 24 | D | All documents have stable ID in metadata; core filenames need not expose ID. |
| 25 | D | YAML Front Matter + schema validation for governed documents. |
| 26 | D | Human-readable `project_id` + immutable `project_uuid`. |
| 27 | D | Hybrid merge semantics: absorption vs true merge. |
| 28 | D | Full event-based identity history. |
| 29 | C | Hybrid split semantics: carve-out vs true split. |
| 30 | C | Separate Project Lifecycle State from Execution State. |
| 31 | D | `03-Current State` is pure snapshot; history lives in Change Log. |
| 32 | C | Truth Domain model; authoritative source varies by domain. |
| 33 | C | Drift causes scoped stop + Drift Record. |
| 34 | B | `DRIFT-*` is a formal object type. |
| 35 | C | Two-stage bootstrap: `00 → 01 → 03`, then route by task. |
| 36 | D | Two-tier Preflight: READ and MUTATION. |
| 37 | D | Risk-tiered Postflight Verification. |
| 38 | C | Risk model = `R0/R1/R2/R3`. |
| 39 | C | Approval matrix depends on Risk + Project Rule. |
| 40 | D | `AUTH-*` standing authorization requires explicit scope + expiry/termination. |
| 41 | D | Strict non-transfer; delegation requires explicit `DEL-*`. |
| 42 | D | Stable Actor Registry + per-session/instance identity. |
| 43 | D | Separate Actor Registry and Authorization Registry. |
| 44 | A | Both Actor and Authorization registries mandatory in every Project. |
| 45 | C | Thai human content + canonical English machine vocabulary. |
| 46 | C | Standard epistemic statuses. |
| 47 | C | Freshness classification: Immutable/Stable/Changeable/Volatile. |
| 48 | C | Formal `EVD-*` required for important evidence, not every fact. |
| 49 | C | `13-Evidence Registry` mandatory. |
| 50 | C | Evidence storage split by artifact type. |
| 51 | D | Archive structure = taxonomy + year/month. |
| 52 | C | Two-phase supersede promotion. |
| 53 | D | Hybrid draft model: scratch outside, formal candidates under `drafts/`. |
| 54 | C | Optimistic concurrency + base revision/hash check. |
| 55 | B | `CONFLICT-*` is a formal object type. |
| 56 | C | Agent auto-resolves only non-semantic conflicts. |
| 57 | C | One current Handoff + historical archived Handoffs. |
| 58 | D | Handoff refresh is event-driven + user-requested. |
| 59 | C | Handoff lifecycle: Draft→Offered→Acknowledged→Accepted→Superseded. |
| 60 | C | Handoff Acceptance is freshness-aware. |
| 61 | D | Index = generated registry + human-curated routing. |
| 62 | C | Manual edits to generated Index section are governance violations and block promotion. |
| 63 | C | `14-Project Source Manifest` mandatory. |
| 64 | C | Manifest covers current reconstructable snapshot, not full archive. |
| 65 | C | Export profiles = CURRENT / AUDIT / FULL. |
| 66 | C | CURRENT includes only continuation-relevant formal drafts. |
| 67 | C | Mandatory Export Validation Gate. |
| 68 | D | Canonical object home + optional Detail Document. |
| 69 | C | `15-Action Registry` mandatory and canonical home of `ACT-*`. |
| 70 | D | Adoption modes = GREENFIELD / BROWNFIELD / IMPORT. |
| 71 | C | IMPORT goes to quarantine/staging + compatibility assessment. |
| 72 | D | Full Rule/Schema compatibility contract. |
| 73 | D | Managed migration lifecycle via `MIG-*`. |
| 74 | C | `16-Migration Registry` mandatory. |
| 75 | B | Filename collision solved with `r###` before timestamp. |
| 76 | B | Revision starts `r001` with 3-digit padding. |
| 77 | C | Revision overflow expands automatically beyond `r999`. |
| 78 | C | Global number ranges + reserved anchor sub-slots. |
| 79 | C | Full Semantic Validation. |
| 80 | C | Validation severities = INFO / WARNING / ERROR / CRITICAL. |
| 81 | C | Validator remediation split SAFE_FIX vs GOVERNED_FIX. |
| 82 | C | Definition of Done = Operationally Ready, not merely structurally valid. |
| 83 | D | Interview modes = Adaptive + FAST / GRILL. |
| 84 | C | Default interview mode = ADAPTIVE. |
| 85 | C | Brownfield discovery is evidence-weighted, truth-domain aware. |
| 86 | C | Controlled incomplete Project Source allowed: VALID + NOT_OPERATIONALLY_READY. |
| 87 | D | Secret dependencies use metadata-only `SECRET-*`; never store actual secret. |
| 88 | B | `17-Secret Reference Registry` mandatory. |
| 89 | C | Default preserve + explicit purge policy. |
| 90 | C | Pin validation contract/schema snapshots in each Project; validator logic remains central. |
| 91 | D | Standard Completion Report includes human-readable + machine-readable summary. |
| 92 | C | Controlled Partial Completion allowed. |
| 93 | C | Initial creation/structural migration uses Preview → User Approval → Create. |
| 94 | C | Core Rule is version-pinned per Project and upgraded only by managed migration. |

---

# Appendix B — Approved Design Sections

## Section 1 — Architecture

Approved architecture: **Approach B — Layered Governance Skill**.

## Section 2 — Filesystem / Taxonomy / Object Homes

Approved: standardized `/Project-Source/`, Core `00–17`, reserved `18–19`, extended `20–99`, stable document IDs, revision/timestamp naming, canonical object homes, active/draft/archive separation, hybrid Index, Manifest.

## Section 3 — Metadata / Identity / Lifecycle / Truth

Approved: YAML metadata, stable project identity + lineage, separate lifecycle/execution, object lifecycle schemas, epistemic/freshness model, truth domains, DRIFT, reference/evidence/secret contracts.

## Section 4 — Actor / Authority / Risk / Preflight / Postflight

Approved: Actor+Instance, bounded authorization, strict non-transfer + delegation, R0–R3, approval matrix, scoped blocking, preflight, postflight, evidence thresholds, completion claim contract.

## Section 5 — Validation / DRIFT / CONFLICT / Migration / Brownfield / Import

Approved: five-layer validation, severity model, SAFE_FIX/GOVERNED_FIX, drift/conflict handling, preserve-first Brownfield, import quarantine, managed migration, failure semantics, operational readiness gate.

## Section 6 — Handoff / Export / Workflow / Definition of Done

Approved: continuation-contract Handoff, freshness-aware acceptance, CURRENT/AUDIT/FULL export, completion reporting, Greenfield/Brownfield/Import/Update workflows, controlled partial completion, interview policy, initial creation approval gate, retention and Operationally Ready definition.

---

# Appendix C — Spec Self-Review Notes

Self-review resolutions included in this specification:

1. **YAML Front Matter boundary clarified:** mandatory for governed Markdown documents; binary/non-Markdown artifacts use registry/native metadata instead.
2. **Manifest self-reference clarified:** Manifest does not recursively hash its own raw bytes; optional canonical payload hash excludes self-hash field.
3. **Append-only Change Log clarified:** `CHG-*` history is logically append-only even though the containing Markdown document follows the normal revision/archive model.
4. **AUTH lifecycle consolidated:** final lifecycle includes `SUSPENDED` as approved in Section 4.
5. **No Last-Write-Wins ambiguity:** optimistic concurrency and semantic conflict handling are authoritative.
6. **No auto-upgrade ambiguity:** Project-pinned Rule/Schema versions remain authoritative until approved `MIG-*` promotion.
7. **No secret-storage exception:** actual secrets remain forbidden in every export profile, including FULL.

