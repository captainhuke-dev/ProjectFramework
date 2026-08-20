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
project_source_framework_version: "1.1.3"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Root Governance / Non-Removable Framework:** เอกสารนี้คือกฎสูงสุดภายใน Project Source และเป็น Root Governance ของ Project นี้ ทุก AI/Agent ต้องอ่าน `00 → 01 → 03` ก่อนเริ่มงาน และทุก Project Source artifact ที่สร้างหลังจากนี้ถือว่า inherit จาก `FRAMEWORK-001`. ห้ามลบ, bypass, demote, replace ด้วย child rule, หรือทำให้ Framework นี้ไม่มี Active revision. การแก้ Framework ทำได้เฉพาะเมื่อมี User Explicit Approval และต้องใช้ revision/supersede/archive flow.

## 1. Framework Authority, Inheritance, and Precedence

### 1.1 Root Invariant

`00-Project Source Framework` ต้องมีในทุก Project และใช้ Stable Identity:

```yaml
framework_document_id: "FRAMEWORK-001"
framework_root: true
inherits_from: []
```

Project Source ที่ไม่มี Active `FRAMEWORK-001` ถือว่า:

```text
INVALID + NOT_OPERATIONALLY_READY
```

ห้าม descendant artifact/rule ทำสิ่งต่อไปนี้:

- ลบหรือย้าย Framework ออกจาก semantic slot `00`
- bypass bootstrap ที่เริ่มจาก `00`
- demote Framework ให้มีอำนาจต่ำกว่า child rule
- replace Framework ด้วย Project-Specific Rule, Handoff, Task, Prompt หรือ Agent instruction
- weaken/contradict Framework invariant ผ่าน child override

### 1.2 Inheritance Contract

Governed Markdown ที่สร้างหลัง Framework ต้องประกาศ:

```yaml
inherits_from:
  - "FRAMEWORK-001"
```

Non-Markdown Project Source artifacts inherit ผ่าน canonical registry/Manifest entry ที่อ้าง `FRAMEWORK-001`.

Implementation artifacts เช่น source code, config, deployment/runtime changes ไม่จำเป็นต้องฝัง YAML inheritance หรือเปลี่ยน canonical filename แต่ยังอยู่ใต้ Framework ผ่าน Project identity + related `REQ-*` / `DEC-*` / `AUTH-*` / `ACT-*` และ workflow ที่ Framework กำหนด.

ดังนั้น “inherit” ครอบคลุมทั้ง Project: child governance/documentation inherit โดยตรง และ implementation/external mutation inherit governance ผ่าน traceability/authority chain.

Inheritance หมายความว่า child สามารถ **extend / specialize / add constraints** ได้ แต่ห้ามลดทอน Root Framework. หากต้องเปลี่ยน Root invariant ต้องแก้ `00-Project Source Framework` โดยตรงด้วย User Approval, รักษา `FRAMEWORK-001`, เพิ่ม revision และ archive revision เดิม.

### 1.3 Authority Order

```text
0. User Explicit Instruction / Approval (external authority to revise governance)
1. 00-Project Source Framework (root governance inside Project Source)
2. Framework-compliant Project-Specific Rules
3. Canonical Project Source documents / Decisions / Requirements
4. Task / Handoff / Prompt / Agent Instruction
```

User Explicit Instruction สามารถอนุมัติการแก้ Framework ได้ แต่ child artifact ไม่สามารถอ้างคำสั่งเก่า/คลุมเครือเพื่อ bypass Framework เอง.

## 2. Project Identity

```yaml
project_uuid: "<PROJECT_UUID>"   # immutable
project_id: "<PROJECT_ID>"       # stable human-readable ID
project_name: "<PROJECT_NAME>"   # mutable display name
```

Rename ห้ามเปลี่ยน `project_uuid`. Merge/Split ต้องบันทึก lineage แบบ event-based และห้ามทำ provenance หาย

## 3. Project Source Location

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

Conditional documents สร้างเฉพาะเมื่อ applicable; ห้ามสร้างไฟล์ว่างเพื่อให้ดูครบ

Canonical bootstrap mockup อยู่ที่ `templates/project-source-mockup/`. ใช้เพื่อดู mapping เลข `00–17` และ starter filenames เท่านั้น; normative authority ยังคงเป็น Framework + Core Governance + document skeletons. Mockup มี template ของ `06–08` เพื่อ discoverability แต่ไม่ได้บังคับให้สร้าง active files. `18–19` ยัง RESERVED และ `20–99` สร้างเมื่อมี use case เท่านั้น.

Platform Project bootstrap launchers อยู่ที่ `CHATGPT-PROJECT-INSTRUCTIONS.md` และ `CLAUDE-PROJECT-INSTRUCTIONS.md` ใน Framework distribution. ไฟล์เหล่านี้ใช้ชี้ Agent ไปยัง canonical bootstrap source หรือ local pinned Project Source เท่านั้น และห้ามทำหน้าที่แทน/override/weakening `FRAMEWORK-001` เมื่อ Project Source ถูก initialize แล้ว.

## 4. Naming and Revision

Project Source artifacts ใช้ timestamp ท้าย basename:

```text
-YYMMDD-HHMM
```

Document revision ใช้ `r001`, `r002`, ... และห้าม reuse

ตัวอย่าง:

```text
00-Project Source Framework-r001-<YYMMDD-HHMM>.md
05-Requirements-r004-<YYMMDD-HHMM>.md
22-RSCH-004-Model-Benchmark-r002-<YYMMDD-HHMM>.md
```

Canonical implementation files ที่ ecosystem บังคับชื่อ เช่น `README.md`, `main.py`, `docker-compose.yml`, `SKILL.md` คงชื่อ canonical

## 5. Bootstrap and Routing

ทุก session/task ต้องอ่านขั้นต่ำ:

```text
00 → 01 → 03
```

จากนั้น `01-Project Source Index` route ไปเอกสารที่เกี่ยวข้องกับ task

สำหรับ GREENFIELD bootstrap ให้ resolve semantic-slot mapping จาก `templates/project-source-mockup/README.md` ก่อน instantiate files; สร้าง mandatory `00–05, 09–17`, evaluate conditional `06–08`, และห้าม materialize `18–19`.

ถ้าเริ่มจาก ChatGPT Project หรือ Claude Project ให้ใช้ platform instruction artifact ที่ตรงกับ platform เป็น launcher เพื่อแยกกรณี NEW Project ออกจาก initialized Project. NEW Project bootstrap จาก canonical repository `main`; initialized Project ต้องใช้ local pinned Project Source เป็น authority และห้าม auto-upgrade จาก upstream. ถ้า required upstream/local source เข้าถึงไม่ได้ ให้หยุด governance mutation ที่ได้รับผลกระทบและรายงาน limitation แทนการ reconstruct จาก memory.

ห้ามใช้ Handoff, memory, README เก่า หรือไฟล์ “ล่าสุด” แทน bootstrap นี้โดยปริยาย

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

กฎ:

- ห้ามยกระดับ `ASSUMED/INFERRED` เป็น `VERIFIED` โดยไม่มีหลักฐาน
- `VOLATILE` ต้อง fresh-check เมื่อมีผลต่อ decision/mutation
- Truth Domain ขัดกัน → `DRIFT-*`
- Concurrent/competing semantic state → `CONFLICT-*`
- ห้าม silent reconciliation หรือ last-write-wins สำหรับ semantic conflict

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
```

หนึ่ง object มี authoritative home เดียว เอกสารอื่น reference Stable ID เท่านั้น

### 7.1 Materialized Current State and Stable-ID Resolution

Active canonical registry ต้องเป็น **materialized current projection, not delta chain**. ทุก Stable ID ที่เป็น current/active และถูก reference จาก Active Project Source ต้อง resolve ได้ภายใน **Current Reconstructable Snapshot** ไปยัง current authoritative record โดยไม่ต้องเปิด archived revision.

Current authoritative record ต้องมี semantic payload เพียงพอที่จะตอบว่า “ตอนนี้จริงอะไร” หรือ link ไปยัง active/current canonical Detail Document ที่เก็บ payload นั้น. ถ้า Detail Document จำเป็นต่อการตีความ Stable ID เอกสารนั้นต้องอยู่ใน Current Reconstructable Snapshot และต้องรวมใน `CURRENT` export เมื่อ export Stable ID ดังกล่าว.

ข้อความแบบ `retain previous status`, `unchanged from rNNN`, `see archived revision` หรือ delta-only shorthand อื่น ห้ามใช้แทน current authoritative payload ถ้า semantic content จริงอยู่เฉพาะใน archive. Archive ใช้สำหรับ Historical Truth/rationale/evolution เท่านั้น ไม่ใช่ dependency ของ Current Truth.

กรณีที่ต้องตรวจชัดเจน:

- `DEC-*` ใน `04` ต้อง materialize current Decision/Status semantics หรือ link ไป active/current canonical Detail Document
- `REQ-*` ใน `05` ต้อง materialize current Requirement/Status/Acceptance semantics หรือ link ไป active/current canonical Detail Document

Referential validation: ทุก Stable ID ที่ถูก reference จาก Active/Current snapshot **MUST** resolve ไป current authoritative record ภายใน Current Reconstructable Snapshot โดยไม่ต้องใช้ archived revision. ถ้า resolve current truth ไม่ได้ affected scope = integrity/readiness defect และ `NOT_OPERATIONALLY_READY`.

## 8. Current State and History

`03-Current State` = pure snapshot ของ “ตอนนี้”

`10-Change Log` = logical append-only history

ห้ามยัด timeline ย้อนหลังลง `03` จนแยก current state ไม่ออก

## 9. Actor and Authority

`ACTOR-*` = stable actor identity

`INST-*` = session/execution instance

Role ไม่เท่ากับ Authority

Standing Authorization ใช้ `AUTH-*` และต้องมี scope + expiry/termination. Authority ห้าม transfer ผ่าน Handoff, prompt, memory, role, branch, หรือ agent instruction

Delegation ใช้ `DEL-*` และห้ามกว้างกว่า parent authority

## 10. Risk and Approval

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

Default:

- R0 → ไม่ต้อง approval
- R1 → ทำได้ใน approved scope
- R2 → explicit approval หรือ valid Standing Authorization
- R3 → explicit approval สำหรับ action นั้นโดยตรง

Project-Specific Rules เพิ่มความเข้มได้

## 11. Preflight and Postflight

READ PREFLIGHT: identity, `00`, `01`, `03`, scope, truth, freshness, blockers

MUTATION PREFLIGHT เพิ่ม: actor/instance, authority, target, allowed/forbidden effects, risk, approval, relevant REQ/DEC, base/hash, reversibility, evidence

Postflight ต้องตรวจ resulting state ตาม risk. `exit code 0` ไม่เท่ากับ verified completion

## 12. Draft, Promotion, Archive

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

ห้าม Active revision ซ้ำ semantic identity เดียวกัน

Archive ใช้ taxonomy + `YYYY/MM` และเป็น Historical Truth เท่านั้น; ห้ามทำให้ current Stable-ID resolution ต้องพึ่ง archive

## 13. Index and Manifest

`01` = Front Door + derived Active registry + human routing

Generated registry ห้ามถือ manual edit เป็น authoritative

`14` = Current Reconstructable Snapshot inventory + hashes รวม active/current Detail Documents ที่จำเป็นต่อการตีความ referenced current Stable IDs; snapshot ห้ามพึ่ง omitted archive เพื่อ resolve Current Truth

Manifest mismatch ต้องหาสาเหตุก่อน regenerate

## 14. Evidence and Secrets

Important evidence ใช้ `EVD-*`; raw artifacts อยู่ `evidence/<category>/`

**ห้ามเก็บ actual secret** ใน Project Source / Evidence / Manifest / Export

`SECRET-*` เก็บ metadata/reference เท่านั้น และต้องมี:

```yaml
secret_value_present: false
```

## 15. Handoff

`09-Handoff` = Current Continuation Contract

Lifecycle:

```text
DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED
```

Handoff ต้องมี current/pending work, active objects, required read order, freshness warnings, authority references, `authority_transfer: false`, และ exact next action

Acceptance ต้อง fresh-check `00 → 01 → 03 → 09`, actor/authority และ volatile state ที่เกี่ยวข้อง

## 16. Adoption Mode

```text
GREENFIELD BROWNFIELD IMPORT
```

- GREENFIELD → preview → user approval → create
- BROWNFIELD → preserve-first; ห้าม move/rename/delete legacy source อัตโนมัติ
- IMPORT → quarantine ที่ `import-staging/` ก่อน promotion

## 17. Migration and Version Pinning

Project pin Framework/Schema version. ห้าม auto-upgrade

Framework upgrade/normalization/import upgrade ใช้ `MIG-*` + assessment + approval + validation + promotion

Legacy compatibility: หากพบ `00-Project Source Rule` รุ่นเดิม ให้ถือเป็น legacy predecessor ของ slot `00`; ห้ามลบทิ้งตรง ๆ. สร้าง `00-Project Source Framework` candidate, ทำ governed promotion, แล้ว archive predecessor หลัง Framework ใหม่ Active สำเร็จ.

## 18. Export

Profiles:

```text
CURRENT AUDIT FULL
```

ชื่อ ZIP:

```text
<Project-ID>-Project-Source-<PROFILE>-YYMMDD-HHMM.zip
```

Actual secrets ห้ามอยู่ในทุก export profile

`CURRENT` ต้อง include current canonical records และ active/current Detail Documents ที่จำเป็นต่อการตีความ exported current Stable IDs และต้อง resolve current truth ได้โดยไม่ต้องเปิด archive

## 19. Retention

Preserve revisions, Decisions, Requirements, Change Log และ Identity lineage indefinitely โดย default

Purge ต้อง authorized, ไม่มี Active Object อ้างถึง, audit ได้ และไม่ทำลาย reconstructability

## 20. Readiness

Project Source สามารถเป็น:

```text
VALID + NOT_OPERATIONALLY_READY
```

เมื่อ uncertainty ถูก model ชัดเจน

`OPERATIONALLY_READY` หมายถึง Agent ใหม่ตอบได้โดยไม่เดา:

1. What is true now, including resolution of referenced current Stable IDs without archive traversal?
2. What is allowed now?
3. What must happen next?

## 21. Initial Creation / Structural Migration Gate

ก่อนสร้าง Project Source ครั้งแรกหรือ structural migration ครั้งใหญ่ ต้อง Preview อย่างน้อย:

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

ต้องได้รับ User Approval ก่อน write

## 22. Completion Reporting

หลัง Create / Migrate / Import / Major Update / Handoff / Export ต้องรายงาน Human + Machine summary

Completion state:

```text
COMPLETE PARTIAL BLOCKED FAILED
```

ต้องแยก Execution ออกจาก Verification และ State Confirmation

---

# Project-Specific Rules

> ส่วนนี้เป็น child governance ที่ inherit จาก `FRAMEWORK-001`. ใช้เพิ่ม constraint เฉพาะ Project ได้ แต่ห้ามลดทอน/ขัด Root Framework. หากต้องเปลี่ยน Root invariant ต้องแก้ Framework โดยตรงผ่าน User Approval.

## PSR-001 — <TITLE>

- **Status:** `<ACTIVE / SUPERSEDED>`
- **Rule:** <PROJECT-SPECIFIC RULE>
- **Reason:** <WHY>
- **Approved By:** <USER / AUTHORIZED DECISION OWNER>
- **Approved At:** <ISO8601>
- **Related:** <DEC-### / REQ-### / AUTH-### / etc.>

<!-- เพิ่ม PSR-* ตามความจำเป็น ห้ามเพิ่ม rule ใหม่โดยไม่มี user approval และห้ามใช้ PSR เพื่อ override/weakening FRAMEWORK-001 -->
