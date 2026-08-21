---
document_type: UAAC_PRECOMMIT_SYSTEMS_REVIEW
review_id: UAAC-PRECOMMIT-20260821-001
status: APPROVED_AND_IMPLEMENTED
normative: false
authority_effect: NONE
truth_authority: NONE
agent_execution: DO_NOT_EXECUTE_AS_INSTALL_PROTOCOL
intended_audience:
  - PROJECT_OWNER
  - UAAC_EDITOR
  - IMPLEMENTER
  - REVIEWER
repository: captainhuke-dev/ProjectFramework
authorized_branch: hz-framework
observed_hz_framework_sha: 34f2d8ee391fbced8e4f3be980ce47ddbdf460e7
observed_main_sha: a9b2bb0ea95e6dd6cc33c9bd295dff48406d50d4
baseline_candidate: UAAC-v4.1.0-FINAL.zip
baseline_candidate_sha256: e7a4d196693235c98f68b6a69cc5eada88c46d6b83fb90310eecc3c8ad3459e9
recommended_release_target: 4.2.0
approved_at: 2026-08-21
implementation_release: 4.2.0
observed_at: 2026-08-21T18:28:29+07:00
commit_performed: PENDING_REMOTE_PUBLICATION
---

> **Implementation status note (2026-08-21):** Owner subsequently approved this design for implementation as UAAC v4.2.0. Statements such as `commit_now: NO` below record the pre-approval decision point and are retained for audit history; they are not current execution instructions.

# UAAC Installation and Shared-Agent Architecture
## Pre-Commit Systems Review — จุดอ่อน รากเหตุ และข้อสรุปก่อนแก้/commit

> **เอกสารนี้เป็น Design/Review Record สำหรับมนุษย์และผู้ implement เท่านั้น**  
> ไม่ใช่ `INSTALL-UAAC.md`, ไม่ใช่กฎหมาย, ไม่ใช่ Current Truth ของ Project ปลายทาง และ Agent ห้ามนำตัวอย่างในเอกสารนี้ไป execute โดยอัตโนมัติ

---

# 1. จุดประสงค์ของการทบทวน

การทบทวนรอบนี้ต้องตอบให้ชัดว่า ระบบ “ติดตั้งรัฐธรรมนูญ Project” จะทำให้ Human, ChatGPT, Codex, Claude, Hermes และ CLI Agent ทำงานร่วมกันได้จริงหรือไม่ โดยไม่ต้องให้ผู้ใช้เตือนกฎหมายหรือชื่อ Skill ทุกครั้ง และไม่เกิดความเข้าใจผิดว่า Agent หลายตัวเห็น state เดียวกัน ทั้งที่จริงกำลังอ่านคนละ repository, branch, worktree, Project boundary หรือ continuation epoch

เป้าหมายสุดท้ายคือ:

```text
ผู้ใช้สั่ง “งาน” ตามปกติ
        ↓
Agent รู้เองว่าต้อง Auto-Boot
        ↓
resolve Project + กฎหมาย + PRD + state + authority + Skills
        ↓
ทำงานจาก canonical Project state
        ↓
checkpoint / publish / handoff อย่างตรวจสอบได้
        ↓
Agent ตัวอื่นรับต่อได้ แม้ไม่มี conversation เดิม
```

เราไม่ได้ทำให้ Agent ทุกตัวมีความจำเดียวกัน แต่ทำให้ Agent ทุกตัวกลับมาอ่าน **Project identity, governance, documents, artifacts และ continuation state ที่ตรวจสอบได้ชุดเดียวกัน**

---

# 2. Evidence Snapshot — สถานะจริงที่ตรวจพบ

## 2.1 Remote `hz-framework` ยังไม่ใช่ release state

สถานะที่ตรวจสด:

```text
branch: hz-framework
head: 34f2d8ee391fbced8e4f3be980ce47ddbdf460e7
message: temp: retrigger UAAC assembly workflow
```

Current tree ยังมี:

```text
.github/workflows/assemble-uaac.yml
.uaac-upload/
UAAC.md
```

แต่ path ต่อไปนี้ยังไม่มีบน branch:

```text
universal-ai-agent-constitution/README.md
universal-ai-agent-constitution/INSTALL-UAAC.md
```

ดังนั้น `UAAC.md` ปัจจุบันชี้ไปยัง target ที่ยังไม่อยู่ใน effective tree จริง เป็น **partial publication** ไม่ใช่ `PUBLISHED_AND_REMOTE_VERIFIED`

## 2.2 Assembly workflow มีข้อบกพร่องเชิงโครงสร้าง

Workflow ใช้:

```bash
tar -xJf /tmp/uaac-payload.tar.xz -C universal-ai-agent-constitution
```

แต่ไม่มีขั้น:

```bash
mkdir -p universal-ai-agent-constitution
```

เมื่อ target directory ยังไม่มี การ extraction มีโอกาส fail ก่อน package ถูกสร้าง และเพราะ workflow ลบ staging files เฉพาะเมื่อทุกขั้นสำเร็จ จึงทิ้ง branch ไว้ใน temporary state

นอกจากนั้น workflow ยัง:

- self-modify และ self-delete
- commit/push กลับ branch เดิม
- ไม่มี base-freshness check
- ไม่มี force-with-lease/predecessor guard สำหรับ competing publication
- ทำให้ canonical branch มีช่วงเวลาที่ front door มีอยู่แต่ package ไม่มี
- สำหรับ `pull_request` กลับ checkout `hz-framework` แทน PR head

สรุป: ปัญหาไม่ใช่ “ขาดคำสั่งหนึ่งบรรทัด” เท่านั้น แต่คือ **publication architecture ไม่ atomic และวาง transport staging ไว้บน effective branch**

## 2.3 Branch ฐานล้าหลังและ diverged

ตรวจพบ:

```text
main:         a9b2bb0ea95e6dd6cc33c9bd295dff48406d50d4
Framework:    1.2.2
hz-framework: 34f2d8ee391fbced8e4f3be980ce47ddbdf460e7
merge base:   b1ff1cf89f5cdbc0f0e4bb6ca02a6c55fb9ed2b2
compare:      diverged
hz ahead:     40 commits
hz behind:    4 commits
```

`main` เพิ่ม Base Freshness / Forward-Port governance ใน 1.2.2 แต่ `hz-framework` ยังแสดง Framework 1.2.0 การ commit ต่อบน branch เดิมโดยไม่ forward-port จะทำให้ UAAC ขัดกับ framework ล่าสุดและอาจลบ/มองข้ามกฎฐานใหม่

## 2.4 Local UAAC v4.1 candidate

ตรวจ package local candidate:

```text
files:                 155
canonical laws:        25
conformance scenarios: 131
package validator:     PASS
ZIP SHA-256:           e7a4d196693235c98f68b6a69cc5eada88c46d6b83fb90310eecc3c8ad3459e9
```

อย่างไรก็ตาม แนวคิดล่าสุดที่ตกลงภายหลัง เช่น Auto-Boot ทุก material task, Human Walkthrough classification, Bootstrap Kernel, Project Binding, TOCTOU precondition, canonical visibility และ monorepo boundary **ยังไม่อยู่ครบใน candidate นี้**

การรัน installation tests แบบทั้งไฟล์ใน environment นี้ค้างก่อนจบ หลังแสดง 15/16 tests ขณะที่ test สุดท้ายรันเดี่ยวผ่าน จึงยังไม่สามารถประกาศ full-suite result จากรอบนี้ว่า PASS ได้ ต้องรันใน clean isolated environment พร้อม per-process timeout และ duration report ก่อน commit

---

# 3. คำตัดสินก่อนลงมือ

```yaml
current_remote_branch: NOT_RELEASE_READY
current_uaac_md_links: PARTIALLY_BROKEN
current_publication_pipeline: REJECT
current_base_freshness: STALE_SEMANTIC
local_v4_1_candidate: VALID_BASELINE_NOT_FINAL
latest_design_changes: MATERIAL
recommended_release_version: 4.2.0
commit_now: NO
```

**ห้ามเพิ่ม Human Walkthrough แล้ว commit ต่อบน current temporary branch โดยตรง**

ลำดับที่ถูกต้องคือ:

1. ล็อก design รอบนี้ในเอกสารนี้
2. ให้ Owner ตรวจทาน/อนุมัติ
3. สร้าง clean implementation workspace จาก `main` 1.2.2 ล่าสุด
4. ยก UAAC baseline เข้ามาอย่าง atomic
5. apply architecture fixes ทั้งหมดด้านล่าง
6. bump เป็น UAAC 4.2.0 เพราะมี normative behavior ใหม่
7. regenerate manifest/coverage/receipts
8. รัน test suite + Windows + ChatGPT/Codex convergence
9. จึง publish ไป `hz-framework` ด้วย clean, lease-guarded release update

---

# 4. System Purpose และ Success Condition

## 4.1 System Purpose

ระบบต้องทำให้:

- Human ใช้คำสั่งง่าย เช่น “ติดตั้งรัฐธรรมนูญ Project” หรือสั่งงานธรรมดา
- Installer Agent แยก Human tutorial ออกจาก Agent protocol
- ทุก Agent resolve Project boundary และ identity เดียวกัน
- ทุก Agent ใช้ UAAC/Project Law/PRD/Current State/Skills ที่ถูกต้อง
- local work ที่ยังไม่ publish ไม่ถูก ChatGPT เข้าใจว่าเป็น canonical remote state
- งานสำเร็จ ค้าง หยุด ล้มเหลว ยกเลิก หรือถูกแทนที่ ยัง reconstruct ได้
- Agent เลือก applicable Skill เองโดยไม่ให้ผู้ใช้ prompt กฎหมายซ้ำ
- ก่อน write/commit/publish Agent ตรวจว่า context ที่เริ่มงานยัง current
- monorepo/nested Project ไม่จับ front door ผิดตัว

## 4.2 Ultimate Acceptance Test

```text
Day 1:
Codex ทำงานครึ่งหนึ่งบน Windows แล้วหยุด
→ เขียน checkpoint / continuation
→ publish canonical-visible state

Day 2:
เปิด ChatGPT Project session ใหม่ทั้งหมด
ผู้ใช้ถามเพียง “งานนี้ทำถึงไหนแล้ว ทำต่อได้ไหม”

PASS เมื่อ ChatGPT:
- เปิด canonical UAAC-BOOT ได้จริง
- resolve Project ที่ถูกต้อง
- เห็น continuation/artifact เดียวกับ Codex
- บอก completed/pending/blocker/exact next action ถูกต้อง
- ไม่ต้องอ่านข้อความแชต Codex เดิม
```

---

# 5. Actors และหน้าที่

| Actor/Component | หน้าที่ | สิ่งที่ห้ามอนุมาน |
|---|---|---|
| Project Owner | อนุมัติ Project purpose, authority, Project Law, effective adoption | tool access ไม่ใช่ approval |
| Human user | สร้าง/เลือก Project, connector และ copy prompt | walkthrough ไม่ใช่ canonical protocol |
| Installer Agent | inventory, reconcile, stage, validate | ห้ามสร้าง PRD/authority เองเพื่อให้ครบ template |
| Bootstrap Kernel | หา Project/front door/registry ก่อน Skill system พร้อม | ไม่ใช่ Skill, law หรือ authority |
| UAAC-BOOT procedure | classify task, freshness, scope, select applicable procedures | ห้าม blind-load ทุก Skill/ทุก law |
| Codex/Claude/Hermes/CLI | local implementation/verification ตาม capability | local work ไม่ใช่ shared state จน publish |
| ChatGPT Project | remote analysis/coordination ผ่าน canonical surface | URL/prompt ไม่พิสูจน์ว่า connector อ่านได้จริง |
| Git/GitHub | source/governance/publication surface ตาม State Authority Map | branch label ไม่ใช่ immutable identity |
| Continuation store | current/recent lineage state | last-write-wins ไม่ใช่ conflict resolution |
| Skill Registry | route ไป reusable procedure ที่ ACTIVE | file existence ไม่พิสูจน์ว่า platform invoke ได้ |
| Project Document Registry | map semantic roles ไป source จริง | PRD ชื่อมาตรฐานไม่ใช่ requirement |
| Context substrate/Wiki | navigation/recall | memory/retrieval ไม่ใช่ Current Truth |
| Reviewer/Verifier | ตรวจ exact artifact และ claim contract | second model/session ไม่เท่ากับ independence |

---

# 6. ระบบที่แนะนำหลังแก้

## 6.1 Human path และ Agent path ต้องแยกกัน

```text
                              README
                         ┌──────┴──────┐
                         ▼             ▼
                  HUMAN PATH       AGENT PATH
                         │             │
 HUMAN-INSTALL-WALKTHROUGH-TH.md   INSTALL-UAAC.md
      explanation/examples          canonical protocol
                         │             │
                  copy prompt         ▼
                         └──────► Installer Agent
                                       │
                                       ▼
                                    Project
```

`HUMAN-INSTALL-WALKTHROUGH-TH.md` ต้องมี metadata:

```yaml
document_type: UAAC_HUMAN_INSTALL_WALKTHROUGH
audience: HUMAN
normative: false
authority_effect: NONE
truth_authority: NONE
agent_execution: DO_NOT_EXECUTE
canonical_agent_install_protocol: INSTALL-UAAC.md
example_values_are_current_truth: false
```

Agent execution graph ต่อไปนี้ต้องไม่มี Human Walkthrough เป็น dependency:

```text
UAAC-BOOT
AGENTS.md / CLAUDE.md / ChatGPT Instructions
Skill Registry
Capability Pack
INSTALL-UAAC.md
```

## 6.2 Bootstrap Kernel แก้ circular dependency

ปัญหาเดิม:

```text
ต้องใช้ UAAC-BOOT Skill เพื่อหา Skill Registry
แต่ต้องอ่าน Skill Registry ก่อนรู้ว่า UAAC-BOOT Skill อยู่ไหน
```

ข้อสรุป:

```text
Platform Launcher
      ↓
Minimal Bootstrap Kernel
      ↓
resolve Project binding + governance/UAAC-BOOT.md
      ↓
resolve Skill Registry
      ↓
invoke full UAAC-BOOT procedure
      ↓
select applicable procedures
```

Bootstrap Kernel:

- เป็น byte-identical shared contract ระหว่าง platform wrappers
- ไม่ใช่ Skill
- ไม่ใช่ Constitution/Project Law
- ไม่มี authority effect
- รู้เพียงวิธี resolve Project/front door/registry และ stop conditions
- ห้ามฝัง PRD, current task, branch หรือ volatile truth

## 6.3 Runtime flow ต่อ material task

```text
Ordinary user request
      ↓
Bootstrap Kernel
      ↓
Project Binding Check
      ↓
Boot Freshness Check
      ├── identities unchanged → reuse verified boot receipt
      └── changed/unknown      → fresh-read affected scope
      ↓
Materiality + Risk + Authority classification
      ↓
Full UAAC-BOOT
      ↓
Applicable Skills
      ↓
Create/refresh attempt preconditions
      ↓
Work
      ↓
Pre-write context recheck
      ├── match    → write/commit/publish/checkpoint
      └── mismatch → TASK_CONTEXT_STALE / stop affected write
      ↓
Canonical visibility + receiver access check
      ↓
Handoff / receiver verification
```

---

# 7. Weakness Register และข้อแก้ที่เลือก

## W-01 — Temporary branch ถูกใช้เหมือน canonical release

**Severity:** BLOCKER  
**Root cause:** staging transport/workflow ถูกวางใน `hz-framework` ซึ่งเป็น branch ที่คน/Agent เปิดใช้งานจริง  
**Impact:** links broken, partial truth, false publication claims  
**Resolution:** ห้าม staging บน effective branch; build/validate ใน isolated worktree/temp branch แล้วอัปเดต `hz-framework` ด้วย final atomic tree เท่านั้น  
**Test:** final branch ไม่มี `.uaac-upload`, staging workflow หรือ broken links

## W-02 — Self-mutating assembly workflow

**Severity:** BLOCKER  
**Root cause:** workflow reconstructs, validates, deletes itself, commits และ pushes กลับ branch เดิม  
**Impact:** partial state เมื่อ fail; re-trigger/race; debug ยาก  
**Resolution:** ยกเลิก workflow นี้ ใช้ local/CI build ที่สร้าง final tree ก่อน ref update; publication ใช้ expected-old-SHA/force-with-lease  
**Test:** simulate build failure แล้ว effective branch SHA ต้องไม่เปลี่ยน

## W-03 — Base freshness / forward-port missing

**Severity:** BLOCKER  
**Root cause:** UAAC branch diverged จาก `main` 1.2.2  
**Impact:** release ตกหล่น Framework 1.2.1/1.2.2 และมี semantic conflict  
**Resolution:** implementation workspace ต้องเริ่มจาก current `main` SHA; record `base_observed_sha`; recheck ก่อน publication  
**Test:** `BASE_FRESHNESS=FRESH`; main head recheck ก่อน ref update

## W-04 — Version identity collision

**Severity:** BLOCKER  
**Root cause:** Auto-Boot, binding, TOCTOU, visibility, materiality และ monorepo เป็น normative behavior ใหม่ แต่ถูกพูดถึงภายใต้ 4.1.0  
**Impact:** สอง bytes/semantics ต่างกันใช้ version เดียวกัน; pin/reconstruction เสีย  
**Resolution:** release target ต้องเป็น **UAAC 4.2.0**; 4.1.0 baseline เก็บ immutable  
**Test:** normative law/manifest hashes ต่างต้องมี version ใหม่

## W-05 — Human walkthrough อาจถูก Agent execute

**Severity:** HIGH  
**Root cause:** Markdown examples คล้าย runbook/commands  
**Impact:** Agent ใช้ `C:\Projects\Project-A`, `main`, example repo หรือคำสั่งสร้าง repoเป็น truth  
**Resolution:** metadata `audience:HUMAN`, `normative:false`, `agent_execution:DO_NOT_EXECUTE`; section labels `HUMAN ACTION`, `AGENT ACTION — DESCRIPTIVE`, `COPY/PASTE PROMPT`; Agent protocol route กลับ `INSTALL-UAAC.md`  
**Test:** `S-INSTALL-14`

## W-06 — Bootstrap paradox

**Severity:** HIGH  
**Root cause:** Auto-Boot ถูกนิยามเป็น Skill ขณะที่ Skill Registry ต้องถูกค้นผ่าน Boot  
**Impact:** circular dependency / platform improvisation  
**Resolution:** Minimal Bootstrap Kernel ใน launcher แยกจาก full UAAC-BOOT procedure  
**Test:** remove Skill Registry route; Kernel ต้องหยุดด้วย `BOOTSTRAP_KERNEL_RESOLUTION_FAILED` ไม่ improvise

## W-07 — Wrong Project Binding

**Severity:** HIGH  
**Root cause:** path/URL/filename เดียวกันไม่ได้พิสูจน์ Project identity  
**Impact:** Codex เขียน Project B ขณะที่ ChatGPT Project ชี้ Project A  
**Resolution:** Boot เปรียบเทียบ launcher target, `project_id`, Project root/path scope, adoption repository/ref, local git remote/worktree และ front-door identity  
**Failure token:** `PROJECT_BINDING_MISMATCH`  
**Test:** `S-INSTALL-15`

## W-08 — Monorepo / nested Project ambiguity

**Severity:** HIGH  
**Root cause:** “one front door per repository” ไม่ถูกเมื่อ repo มีหลาย Project  
**Impact:** nearest-file selection อาจจับ parent/child ผิด  
**Resolution:** invariant คือ **one effective front door per declared Project boundary**; adoption ต้องมี `project_root`, include/exclude scope, parent_project_id เมื่อมี; overlap ที่ไม่ชัดต้อง explicit active Project  
**Test:** `S-INSTALL-19`

## W-09 — TOCTOU: context เปลี่ยนก่อน write

**Severity:** HIGH  
**Root cause:** Boot ตรวจ state ตอนเริ่ม แต่ไม่มี task-wide precondition recheck  
**Impact:** Agent commit จาก stale PRD/governance/continuation/base commit  
**Resolution:** lineage pointer/checkpoint เพิ่ม `attempt_id` และ `attempt_preconditions`:

```yaml
attempt_preconditions:
  governance_identity:
  project_document_registry_identity:
  continuation_index_identity:
  continuation_index_epoch:
  lineage_pointer_identity:
  lineage_pointer_epoch:
  artifact_base_identity:
  observed_at:
```

ก่อน material write/publish/handoff ต้อง recheck; mismatch → `TASK_CONTEXT_STALE`  
**Test:** `S-INSTALL-16`

## W-10 — Local-only work ถูก remote Agentเข้าใจว่า current

**Severity:** HIGH  
**Root cause:** local Codex state และ GitHub-visible state เป็นคนละ surface  
**Impact:** ChatGPT รายงาน/ทำต่อจาก state เก่า หรือ duplicate effect  
**Resolution:** continuation/checkpoint/handoff เพิ่ม visibility:

```yaml
visibility:
  scope: LOCAL_ONLY | SHARED_CANONICAL | REMOTE_VERIFIED
  canonical_locator:
  observed_identity:
  intended_receivers: []
  receiver_access: NOT_RUN | PASS | FAIL
```

Handoff ข้าม Agent ต้องมี shared canonical surface และ receiver access PASS  
**Failure token:** `CANONICAL_SURFACE_NOT_VISIBLE`  
**Test:** `S-INSTALL-17`

## W-11 — Auto-Boot literal ทำให้โหลดทุกอย่างซ้ำ

**Severity:** MEDIUM/HIGH  
**Root cause:** “fresh-read before every material task” ถูกตีความว่าอ่านทุก law/PRD/Skill ทุกครั้ง  
**Impact:** latency/context exhaustion; ผู้ใช้ปิด governance เพราะช้า  
**Resolution:** แบ่ง boot mode:

```text
FULL_BOOT  = new session, resume, handoff, binding change, high-risk action
DELTA_BOOT = material task; compare identities and load changed/applicable scope
LIGHT_BOOT = non-material question; verify Project binding and relevant source only
```

Reuse ได้เฉพาะ boot receipt ที่ identities ยังตรง; invalidation เมื่อ governance, Project docs, continuation, authority, branch/base หรือ context binding เปลี่ยน  
**Test:** `S-INSTALL-18`

## W-12 — `material task` ยังไม่ชัด

**Severity:** HIGH  
**Root cause:** Agent สามารถเรียกงานว่า non-material เพื่อไม่ Boot  
**Resolution:** floor:

งานเป็น material หากอย่างน้อยหนึ่งข้อจริง:

- แก้ source/artifact
- commit/push/merge/release
- เปลี่ยน Project state/continuation
- เปลี่ยน PRD/requirements/design/Project Law
- สร้าง decision/recommendation ที่มีผลต่อ Project
- emit governance/status token
- checkpoint/handoff
- external effect/publish/deploy
- ใช้/เปลี่ยน authority หรือ secrets

`UNKNOWN_MATERIALITY -> MATERIAL` เมื่อ action มีโอกาสเปลี่ยน state/effect  
**Test:** ordinary “แก้ bug นี้และ commit” ต้อง Auto-Boot โดยไม่มี UAAC reminder

## W-13 — Prompt/URL ไม่พิสูจน์ connector access

**Severity:** HIGH  
**Root cause:** ChatGPT Project Instructions ชี้ URL แต่ connector อาจไม่มี permission หรืออ่าน private repo ไม่ได้  
**Impact:** modelตอบจาก memory โดยแกล้งว่า Boot แล้ว  
**Resolution:** installation validation ต้องมี actual access/readback receipt ต่อ intended Agent/platform พร้อม observed identity/time  
**Failure token:** `GOVERNANCE_BOOTSTRAP_UNAVAILABLE`  
**Test:** `S-INSTALL-20`

## W-14 — Skill file exists แต่ platform ไม่ได้ invoke จริง

**Severity:** HIGH  
**Root cause:** Codex, Claude, Hermes และ ChatGPT มี Skill mechanism ต่างกัน  
**Impact:** `SKILLS_MATERIALIZED` เป็น file-presence theater  
**Resolution:** Procedure Registry เพิ่ม:

```yaml
implementation_type: NATIVE_SKILL | REPO_DIRECTIVE | PROMPT_ADAPTER | ROUTER
platform_bindings:
  - platform:
    launcher:
    invocation_test:
    status:
```

Installation ต้อง run ordinary-task behavioral probe ต่อ platform  
**Test:** `S-INSTALL-21`

## W-15 — Read-only Agent ไม่มี canonical write path

**Severity:** MEDIUM/HIGH  
**Root cause:** ChatGPT บาง Project อ่าน GitHub ได้แต่เขียน continuation ไม่ได้  
**Impact:** state ใน chat ไม่ถูก publish; Agent ตัวถัดไปไม่เห็น  
**Resolution:** State Authority Map ระบุ writer path ต่อ Agent:

```text
DIRECT_CANONICAL_WRITE
AUTHORIZED_WRITER_HANDOFF
READ_ONLY
```

read-only Agent ต้องสร้าง handoff/checkpoint proposal และสถานะ `PENDING_CANONICAL_PUBLICATION`; ห้ามอ้าง canonical update จน writer publish/readback  
**Test:** receiver sees only published state

## W-16 — Windows junction/symlink/nested repository escape

**Severity:** HIGH  
**Root cause:** lexical path check อย่างเดียวไม่พอ  
**Impact:** installer เขียนนอก Project ผ่าน junction/reparse point/submodule  
**Resolution:** canonicalize real path, inspect reparse points/symlinks, nested `.git`, submodule/worktree boundary; default block unless explicitly authorized  
**Test:** Windows junction and nested repo escape tests

## W-17 — Human commands อาจสร้าง repo ผิดหรือเปิดเผยข้อมูล

**Severity:** MEDIUM  
**Root cause:** walkthrough มี `gh repo create` ที่ดูเหมือน command default  
**Impact:** wrong owner/name/privacy/remote  
**Resolution:** เป็น `HUMAN ACTION`; Agentต้อง preview owner/name/visibility/remote และขอ explicit approval ก่อน create; secrets/credentialsไม่บันทึกลง docs  
**Test:** Human guide lint ตรวจ command classification

## W-18 — Claim contracts ยังไม่ครอบคลุมสถานะใหม่

**Severity:** HIGH  
**Resolution:** เพิ่ม contracts/fallbacks:

```text
PROJECT_BINDING_MATCH / PROJECT_BINDING_MISMATCH
BOOTSTRAP_KERNEL_RESOLVED / BOOTSTRAP_KERNEL_RESOLUTION_FAILED
AUTO_BOOT_VERIFIED / AUTO_BOOT_UNVERIFIED
TASK_CONTEXT_CURRENT / TASK_CONTEXT_STALE
CANONICAL_SURFACE_VISIBLE / CANONICAL_SURFACE_NOT_VISIBLE
RECEIVER_ACCESS_VERIFIED / RECEIVER_ACCESS_UNVERIFIED
```

fallback ต้องเป็น UNKNOWN/UNVERIFIED ไม่ invert เป็น positive  
**Test:** token without receipt cannot advance work

## W-19 — Test coverage ยังไม่พิสูจน์ latest architecture

**Severity:** BLOCKER ก่อน release  
**Resolution:** เพิ่ม scenarios/tests 14–23 ด้านล่าง และรัน full suite ใน fresh clone/extraction, per-subprocess timeout, duration report, no cache artifacts  
**Additional gate:** current full installation test runใน environment นี้ยังไม่จบครบ จึงต้องจัดเป็น `TEST_EXECUTION_UNVERIFIED` จนมี clean evidence

## W-20 — Broken-link/atomic publication ไม่มี gate

**Severity:** BLOCKER  
**Resolution:** pre-publication validator ต้องสร้าง final tree ก่อน ref updateและตรวจ:

- `UAAC.md` links resolveใน final tree
- `INSTALL-UAAC.md`, README, Constitution, release receipt อยู่ใน commit เดียวกัน
- no staging artifacts
- exact file count/hashes
- expected old branch SHA
- current main base SHA/freshness

**Test:** `S-INSTALL-22` / publication failure leaves branch unchanged

---

# 8. Human Walkthrough ที่ควรเพิ่ม

ชื่อที่แนะนำ:

```text
HUMAN-INSTALL-WALKTHROUGH-TH.md
```

README แยก route:

```text
สำหรับมนุษย์ → HUMAN-INSTALL-WALKTHROUGH-TH.md
สำหรับ Agent/Installer → INSTALL-UAAC.md
```

## โครงเนื้อหา

1. **FOR HUMAN READING ONLY** และ metadata
2. Mental model: Windows Codex ↔ GitHub Project ↔ ChatGPT Project
3. Step 0: สิ่งที่มีตอนเริ่ม — folder ว่าง + ChatGPT Project ว่าง
4. Prerequisites: Git/GitHub/connector/permissions
5. `HUMAN ACTION`: เลือก folder และ Project identity
6. `HUMAN ACTION`: สร้าง/อนุมัติ GitHub repo
7. `COPY/PASTE PROMPT`: สั่ง Codex ติดตั้งจาก `INSTALL-UAAC.md`
8. `AGENT ACTION — DESCRIPTIVE ONLY`: สิ่งที่ installer จะสร้าง
9. Project purpose/PRD ขั้นต่ำที่ Human ต้องตัดสินใจ
10. Commit/push canonical state
11. เชื่อม ChatGPT Project กับ GitHub และทดสอบ read accessจริง
12. ใส่ ChatGPT Project Instructions แบบ ultra-short
13. Cross-Agent convergence test
14. Interrupted-work recovery test
15. หลังติดตั้ง: ผู้ใช้สั่งงานปกติ ไม่ต้องย้ำ UAAC/Skill
16. Troubleshooting: no connector, wrong project, local-only, stale state, monorepo

## รูปแบบกล่อง

```text
🧑 HUMAN ACTION
🤖 AGENT ACTION — DESCRIPTIVE ONLY
📋 COPY/PASTE PROMPT
✅ EXPECTED EVIDENCE
⛔ STOP CONDITION
```

Agent ที่อ่านเอกสารนี้ต้อง route ไป `INSTALL-UAAC.md` และ resolve Project จริง ไม่ใช้ค่า example

---

# 9. Bootstrap Kernel และ Auto-Boot Specification

## 9.1 Minimal Kernel contract

Platform wrapper ควรสั้นและคงที่:

```text
This Project operates under UAAC.
Resolve the active Project binding and canonical governance/UAAC-BOOT.md.
Use the front door only as a router to adoption, Project Law, state/document authorities,
continuation, and Procedure Registry.
Invoke the registered UAAC-BOOT procedure before material work.
Do not treat memory, retrieval, tutorial examples, or Skill names as Current Truth/authority.
If binding/access/identity cannot be verified, stop affected work and report.
```

## 9.2 ChatGPT Project Instructions ultra-short

```text
Project นี้ใช้ UAAC: <PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

Prompt นี้เป็น launcher ไม่ใช่ proof ว่า Auto-Boot ทำงาน ต้องมี behavioral receipt

## 9.3 Full UAAC-BOOT procedure

1. Verify Project binding
2. Determine boot mode/freshness
3. Resolve pinned Constitution and Project Law
4. Resolve State Authority Map
5. Resolve Project Document Registry/PRD/current state
6. Resolve Capability Pack and Procedure Registry
7. Resolve continuation index/lineage
8. Classify materiality/risk/authority
9. Load bounded applicable scope
10. Invoke applicable procedures automatically
11. Create/refresh attempt preconditions
12. Continue only if canonical state coherent

---

# 10. Tests ที่ต้องเพิ่ม

```text
S-INSTALL-14 — Human Walkthrough Is Not Agent Protocol
S-INSTALL-15 — Project Binding Mismatch
S-INSTALL-16 — Stale Task Context Before Write
S-INSTALL-17 — Canonical Surface Not Visible To Receiver
S-INSTALL-18 — Auto-Boot Freshness Reuse and Invalidation
S-INSTALL-19 — Monorepo/Nested Project Boundary Resolution
S-INSTALL-20 — ChatGPT/Remote Agent Cannot Read Canonical Bootstrap
S-INSTALL-21 — Platform Skill Adapter Invocation
S-INSTALL-22 — Atomic Publication / Broken Link Prevention
S-INSTALL-23 — Base Freshness Recheck Before Publication
```

## Required negative tests

- Human guide value `C:\Projects\Project-A` must never become actual project root automatically
- local git remote differs from boot/adoption repository
- parent and nested Project both have front doors
- continuation changes after work starts but before commit
- Codex state is LOCAL_ONLY while ChatGPT reads old GitHub state
- ChatGPT connector denied access
- Skill file exists but adapter does not invoke it
- mutable upstream branch is used as effective law
- publication build fails; `hz-framework` ref remains unchanged
- main advances after build; publication refuses stale base

## Required positive tests

- ordinary user prompt without UAAC words triggers Auto-Boot
- unchanged identities permit DELTA/LIGHT reuse without rereading all laws
- changed Project Law/PRD/continuation invalidates boot receipt
- Codex and ChatGPT resolve same identities through different access surfaces
- terminal work remains reconstructible
- read-only Agent produces `PENDING_CANONICAL_PUBLICATION`, not false canonical update

---

# 11. File Change Map สำหรับ implementation รอบถัดไป

## Add

```text
HUMAN-INSTALL-WALKTHROUGH-TH.md
templates/BOOTSTRAP-KERNEL.md
templates/PROJECT-BINDING.example.yaml   # only if separate artifact is chosen
schemas/boot-receipt.schema.json         # stored only when evidence is required
```

## Update

```text
README.md
INSTALL-UAAC.md
INSTALLATION-THREAT-MODEL.md
SYSTEMS-THINKING-ANALYSIS-TH.md
ADOPTION-GUIDE.md
CHANGELOG.md
V4.1-TO-V4.2-TRACEABILITY.md
UAAC-v4.2-CONSTITUTION.md
laws/CONST-002.md
laws/CONST-014.md
laws/CONST-015.md
laws/CONST-016.md
laws/CONST-021.md
laws/CONST-023.md
laws/CONST-025.md
templates/PROJECT-UAAC-BOOT.template.md
templates/AGENTS-UAAC-BOOTSTRAP.md
templates/CHATGPT-PROJECT-INSTRUCTIONS-SHORT.md
templates/PROJECT-CAPABILITY-PACK.template.yaml
templates/SKILL-REGISTRY.template.yaml
templates/CONTINUATION-POINTER.template.yaml
templates/CHECKPOINT.template.yaml
templates/HANDOFF.template.yaml
templates/INSTALLATION-VALIDATION.template.yaml
schemas/project-capability-pack.schema.json
schemas/skill-registry.schema.json
schemas/continuation-pointer.schema.json
schemas/checkpoint.schema.json
schemas/handoff.schema.json
schemas/installation-validation.schema.json
skills/uaac-boot/SKILL.md
tools/validate_installation.py
tools/validate_package.py
tests/conformance-scenarios.md
tests/scenarios/030-standard-project-installation-profile.md
tests/test_installation_protocol.py
tests/test_validate_package.py
LAW-MANIFEST.yaml
CONSTITUTION-RELEASE.yaml
```

## Remove from final branch

```text
.uaac-upload/
.github/workflows/assemble-uaac.yml
all temporary payload chunks
all local-path probes/cache artifacts
```

---

# 12. Recommended Publication Strategy

## เลือก: Clean lease-guarded replacement บน `hz-framework`

หลัง Owner อนุมัติ design:

1. Record old `hz-framework` tip `34f2d8ee...` ใน release/migration receipt
2. Create clean worktree from current `main` (`a9b2bb0e...` หรือ fresher verified head)
3. Build UAAC 4.2.0 final tree locally/isolated
4. Run all validation/tests
5. Recheck `main` and `hz-framework` expected old SHAs
6. Create final commit(s) with no staging state
7. Update **only** `refs/heads/hz-framework` using force-with-lease/expected-old-SHA
8. Fresh clone/readback and rerun validators

เหตุผลที่ไม่เลือก merge ต่อจาก branch ปัจจุบัน:

- เก็บ 40 temporary/assembly commits เป็น effective history
- branch behind main 4 commits
- partial publication artifactsยังอยู่
- audit trailอ่านยากและสร้าง false confidence

ข้อควรระวัง: force-with-lease เป็น history rewrite จึงต้องได้รับ owner approval ชัดเจนในรอบ implementation แม้ target branch จะเป็น branch ที่อนุมัติแล้ว

ไม่สร้าง tag/release/branch อื่นโดยอัตโนมัติ เพราะขอบเขตอนุมัติปัจจุบันคือ `hz-framework` เท่านั้น

---

# 13. Pre-Commit Gates

ห้าม commit/publish จนทุกข้อ PASS:

```text
[ ] Owner approves this design/review record
[ ] release target accepted as 4.2.0
[ ] clean base is current main 1.2.2 or fresher
[ ] current hz-framework old SHA recorded
[ ] no staging transport on final tree
[ ] README Human/Agent routes separated
[ ] Human Walkthrough classified non-normative / DO_NOT_EXECUTE
[ ] Bootstrap Kernel and full BOOT separated
[ ] Project Binding and monorepo rules implemented
[ ] material task and boot freshness semantics implemented
[ ] attempt precondition/TOCTOU check implemented
[ ] visibility/receiver access semantics implemented
[ ] platform Skill adapters modeled and tested
[ ] all new claim contracts registered
[ ] S-INSTALL-14..23 specified
[ ] package validator PASS in fresh clone
[ ] complete test suite PASS with per-process timeout and durations
[ ] Windows folder/junction/nested-repo smoke tests PASS
[ ] ChatGPT connector actual read-access test PASS
[ ] Codex ↔ ChatGPT convergence PASS
[ ] interrupted-work recovery PASS
[ ] link audit PASS
[ ] release receipt hashes PASS
[ ] final remote readback PASS
```

---

# 14. สิ่งที่ไม่ควรทำ

```text
- ไม่ commit Human Walkthrough บน temporary branch แล้วค่อยแก้ทีหลัง
- ไม่แก้ normative behavior แต่คง version 4.1.0
- ไม่ใช้ README/Human guide เป็น Agent protocol
- ไม่ให้ Skill file existence เท่ากับ Skill invocation
- ไม่ให้ ChatGPT URL เท่ากับ connector access proof
- ไม่ให้ local Codex state เท่ากับ remote canonical state
- ไม่ใช้ last-write-wins เมื่อ context/continuation เปลี่ยน
- ไม่ assume one Project per repository
- ไม่ให้ Auto-Boot อ่านทุกไฟล์ทุก prompt อย่างไร้ขอบเขต
- ไม่อ้าง tests PASS จน full suite จบพร้อม evidence
- ไม่ใช้ staging workflow ที่เปลี่ยน effective branch ทีละส่วน
```

---

# 15. Final Recommendation

**ข้อสรุปที่แนะนำให้ยึดเป็นแบบ final ก่อน implementation:**

```text
1. Human Guide อธิบาย; Agent Protocol ปฏิบัติ
2. Bootstrap Kernel หา Project/front door ก่อน Skill system
3. Full UAAC-BOOT เลือก applicable Skills อัตโนมัติ
4. Auto-Boot ใช้ freshness/identity check ไม่ใช่อ่านทุกอย่างซ้ำ
5. Material task มี constitutional floor; unknown with state effect = material
6. Project binding ต้องพิสูจน์ repo/root/boundary/project_id ตรงกัน
7. Work attempt ต้อง recheck context ก่อน material write
8. Cross-Agent handoff ต้องใช้ receiver-visible canonical surface
9. One front door applies per Project boundary, not per repository
10. Platform adapter/invocation test สำคัญกว่า Skill file existence
11. Publication ต้อง atomic, clean-base, lease-guarded และ remote-verified
12. การเปลี่ยนแปลงชุดนี้ออกเป็น UAAC 4.2.0
```

สถานะเอกสารนี้:

```yaml
analysis_complete: true
implementation_performed: false
github_modified: false
commit_created: false
ready_for_owner_review: true
```

<!-- END_OF_DOCUMENT: UAAC-PRECOMMIT-20260821-001 -->
