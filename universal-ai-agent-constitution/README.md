# Universal AI Agent Constitution (UAAC) v4.2.0

```yaml
constitution_id: UAAC-001
status: STABLE_CORE_READY_FOR_PROJECT_INSTALLATION_AND_ADOPTION
canonical_laws: laws/CONST-001.md ... laws/CONST-025.md
canonical_agent_install_protocol: INSTALL-UAAC.md
standard_project_front_door: governance/UAAC-BOOT.md
agent_behavioral_certification: PROJECT_SPECIFIC_NOT_IMPLIED
```

UAAC คือรัฐธรรมนูญกลางสำหรับ Project ที่มนุษย์, ChatGPT, Codex, Claude, Hermes, CLI Agent และ runtime อื่นทำงานร่วมกัน เป้าหมายไม่ใช่ทำให้ Agent ทุกตัวมีความจำเดียวกัน แต่ทำให้ทุกตัวกลับมา resolve **Project เดียวกัน กฎหมายเดียวกัน เอกสาร/PRD เดียวกัน state/artifact เดียวกัน และ continuation เดียวกัน** จากแหล่ง canonical ที่ตรวจสอบได้

> **หลักการจำง่าย:** ผู้ใช้สั่ง “งาน” ไม่ต้องสั่ง “กฎหมาย” ซ้ำ เมื่อ Project ผ่านการติดตั้งแล้ว Agent ต้อง Auto-Boot และเลือก applicable Skills เอง

## เริ่มตรงไหน

### 🧑 สำหรับมนุษย์ที่อยากเห็นตัวอย่างตั้งแต่ Windows folder ว่าง

อ่าน [`HUMAN-INSTALL-WALKTHROUGH-TH.md`](HUMAN-INSTALL-WALKTHROUGH-TH.md)

เอกสารนี้เป็นคำอธิบาย/ตัวอย่างสำหรับคนเท่านั้น มีสถานะ `DO_NOT_EXECUTE` และไม่ใช่ Agent protocol, authority หรือ Current Truth

### 🤖 สำหรับ Agent/Installer ที่กำลังติดตั้งจริง

อ่านและปฏิบัติตาม [`INSTALL-UAAC.md`](INSTALL-UAAC.md)

```text
Human guide = explanation/example
INSTALL-UAAC.md = canonical Agent protocol
```

### ✅ Project ติดตั้งแล้ว

ทุก Human/Agent/CLI เริ่มจาก front door ของ Project:

```text
governance/UAAC-BOOT.md
```

สำหรับ remote Agent ใช้ canonical URL ของไฟล์เดียวกัน

## Prompt ติดตั้งแบบสั้น

```text
ติดตั้งรัฐธรรมนูญ Project ตาม UAAC จาก:
<UAAC_INSTALL_URL>

ให้กับ Project:
<PROJECT_REPO_URL_OR_LOCAL_ROOT>

ทำตาม INSTALL-UAAC.md จนมีหลักฐานรองรับ INSTALLATION_VALIDATED
ตั้ง governance/UAAC-BOOT.md เป็น front door ของ Project
และพิสูจน์ Auto-Boot + cross-agent convergence ก่อนรายงานผล
```

`<UAAC_INSTALL_URL>` อาจเป็น discovery URL ของ repository นี้ แต่ Installer ต้อง resolve exact release/commit/hash ก่อน vendoring ห้ามใช้ mutable branch เป็น effective law ของ Project ปลายทาง

## ChatGPT Project Instructions แบบสั้นจริง

```text
Project นี้ใช้ UAAC: <PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

ข้อความนี้เป็นเพียง **launcher** ไปยัง Project front door ไม่ใช่ Constitution copy และไม่ใช่หลักฐานว่า connector เข้าถึง Project ได้ การติดตั้งต้องทดสอบ read access/identity จริง

## หลังติดตั้ง ผู้ใช้สั่งงานปกติ

```text
แก้ bug login นี้และรัน tests
```

Agent ต้องทำภายในเอง:

```text
Minimal Bootstrap Kernel
→ Project Binding check
→ governance/UAAC-BOOT.md
→ UAAC-BOOT freshness/applicability check
→ canonical Project Law / PRD / state / authority
→ applicable registered Skills
→ work
→ pre-write context recheck
→ checkpoint / handoff / report ตาม applicability
```

## ปัญหาที่ v4.2 ปิด

- Human tutorial ถูก Agent เข้าใจเป็น runbook
- ต้องหา BOOT Skill ก่อนอ่าน Skill Registry (bootstrap paradox)
- Codex/ChatGPT ชี้คนละ Project, repository, branch หรือ worktree
- monorepo มีหลาย Project แล้วจับ front door ของ parent/child ผิด
- state เปลี่ยนหลัง Agent เริ่มงานแต่ก่อน commit/push (`TOCTOU`)
- Codex มี local work ที่ remote ChatGPT มองไม่เห็น
- URL อยู่ใน prompt แต่ connector อ่าน canonical source ไม่ได้
- มี Skill file แต่ platform ไม่เคย invoke จริง
- Auto-Boot อ่านทุกไฟล์ใหม่ทุก prompt หรือ reuse stale context เกินไป
- staging/payload/workflow ถูกวางบน effective branch จนเกิด partial release

## Architecture

```text
HUMAN
  ├─ Human walkthrough (explanation only)
  └─ copy install prompt
               ↓
        Installer Agent
               ↓
        INSTALL-UAAC.md
               ↓
              Project
               ↓
    Minimal Bootstrap Kernel
               ↓
       Project Binding artifact
               ↓
     governance/UAAC-BOOT.md
               ↓
         registered UAAC-BOOT
               ↓
 ┌─────────────┼──────────────────┐
 ▼             ▼                  ▼
Law/Authority  Project docs/PRD   Continuation/artifacts
               ↓
        applicable Skills
               ↓
      ChatGPT / Codex / Claude / Hermes / CLI
```

## Auto-Boot ไม่ได้แปลว่าอ่านทุกอย่างใหม่หมด

Auto-Boot มีโหมด `FULL`, `DELTA`, `LIGHT` และใช้ identity/trigger-based freshness:

- `FULL`: session ใหม่, binding/governance/PRD/authority เปลี่ยน, handoff, publish/deploy หรือ uncertainty สูง
- `DELTA`: prior scope ยัง valid แต่มี identity บางส่วนต้อง fresh-read
- `LIGHT`: non-material/low-risk routing ที่ checked identities ไม่เปลี่ยน

ห้าม reuse เมื่อ Project binding, governance, Project Law, requirements/PRD, authority, continuation, adapter, artifact base หรือ publication state เปลี่ยน

## Material-task floor

อย่างน้อยงานต่อไปนี้เป็น material:

```text
source/artifact mutation
commit/push/merge
Project state/governance/requirements change
material decision or status claim
checkpoint/handoff
external effect
publish/deploy
secret/authority/cost/risk-tier use or change
```

ถ้าไม่แน่ใจและการจัดผิดอาจเปลี่ยน state/authority/effect/cost/risk ให้ถือเป็น material จนกว่าจะ resolve

## Shared state ต้องมองเห็นผู้รับ

```text
LOCAL_ONLY
→ PENDING_CANONICAL_PUBLICATION
→ CANONICAL_VISIBLE
```

Local checkpoint ช่วยกู้ session เดิมได้ แต่ยังไม่ใช่ shared state จนผู้รับอ่าน canonical surface และ exact identity ได้จริง

## โครงสร้างมาตรฐานของ Project ที่ติดตั้งแล้ว

```text
Project-A/
├── AGENTS.md / platform launchers
├── governance/
│   ├── BOOTSTRAP-KERNEL.md
│   ├── PROJECT-BINDING.yaml
│   ├── UAAC-BOOT.md
│   ├── CONSTITUTION-ADOPTION.yaml
│   ├── PROJECT-LAWS/PROJECT_RULES.md
│   ├── STATE-AUTHORITY-MAP.yaml
│   ├── PROJECT-DOCUMENT-REGISTRY.yaml
│   ├── PROJECT-CAPABILITY-PACK.yaml
│   ├── AGENT-ADAPTER-REGISTRY.yaml
│   ├── SKILL-REGISTRY.yaml
│   ├── CLAIM-CONTRACT-REGISTRY.yaml
│   ├── BOOT-RECEIPT.yaml
│   ├── CURRENT-CONTINUATION.yaml
│   ├── continuation/<LINEAGE>/CURRENT.yaml
│   ├── INSTALLATION-VALIDATION.yaml
│   └── LLM-WIKI/index.md
├── project-docs/
└── vendor/uaac/v4.2.0/
```

หนึ่ง effective front door ใช้ต่อ **หนึ่ง declared Project boundary** ไม่จำเป็นต้องหนึ่งต่อ repository; monorepo อาจมี child Projects ที่ประกาศ boundary/binding ของตนเอง

## Result states ไม่ถูกรวมเป็น “DONE”

```text
EXECUTED ≠ VERIFIED ≠ ACCEPTED ≠ PUBLISHED ≠ DEPLOYED ≠ CLOSED
```

งาน `BLOCKED`, `INTERRUPTED`, `FAILED`, `CANCELLED`, `ABANDONED`, `SUPERSEDED` และ `CLOSED` ต้องยัง reconstruct ได้จาก lineage pointer/receipt และ exact artifact

## สิ่งที่ไม่เป็น Current Truth/Authority โดยอัตโนมัติ

```text
Conversation/Agent Memory != Current Truth
Retrieval/Wiki/Summary      != Complete Reading
Skill/File Presence         != Invocation or Authority
Tool Access/Role            != Authority
Process Exit                != Verified Completion
Local Worktree              != Receiver-visible Shared State
```

## Greenfield / Brownfield / Monorepo

- **GREENFIELD:** สร้าง Project definition, requirements, governance และ continuity ตั้งแต่ต้น
- **BROWNFIELD:** inventory/map source เดิมก่อน ห้ามสร้าง PRD/Project Law/Current State แข่งกัน
- **MONOREPO:** resolve nearest declared Project binding; parent scan ต้อง exclude declared child Project roots

## อ่านต่อ

- Human walkthrough: [`HUMAN-INSTALL-WALKTHROUGH-TH.md`](HUMAN-INSTALL-WALKTHROUGH-TH.md)
- Agent install protocol: [`INSTALL-UAAC.md`](INSTALL-UAAC.md)
- Adoption concepts: [`ADOPTION-GUIDE.md`](ADOPTION-GUIDE.md)
- Deterministic runbook: [`ADOPTION-RUNBOOK.md`](ADOPTION-RUNBOOK.md)
- Threat model: [`INSTALLATION-THREAT-MODEL.md`](INSTALLATION-THREAT-MODEL.md)
- Systems Thinking: [`SYSTEMS-THINKING-ANALYSIS-TH.md`](SYSTEMS-THINKING-ANALYSIS-TH.md)
- Constitution entrypoint: [`UAAC-v4.2-CONSTITUTION.md`](UAAC-v4.2-CONSTITUTION.md)
- Traceability: [`V4.1-TO-V4.2-TRACEABILITY.md`](V4.1-TO-V4.2-TRACEABILITY.md)
- Conformance scenarios: [`tests/conformance-scenarios.md`](tests/conformance-scenarios.md)

Core/package validation ไม่ได้ certify Agent ทุกตัวอัตโนมัติ Project ปลายทางต้องรัน profile-required behavioral tests และบันทึก `INSTALLATION_VALIDATED`/`EFFECTIVE` แยกกันก่อน material effects
