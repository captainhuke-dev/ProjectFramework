# ProjectFramework — HZ Framework + UAAC

> Repository: `captainhuke-dev/ProjectFramework`  
> Distribution branch: **`hz-framework`**  
> Project Source Framework: **1.2.2**  
> Universal AI Agent Constitution (UAAC): **4.2.0**

สาขา `hz-framework` คือชุดที่เราใช้รวม **ProjectFramework + UAAC** สำหรับสร้างและควบคุม Project ที่มี Human และ AI Agent หลายตัวทำงานร่วมกัน เช่น ChatGPT, Codex, Claude, Hermes และ CLI Agent

เป้าหมายหลักคือให้ Agent ทุกตัวกลับมาอ่าน **Project เดียวกัน กฎหมายเดียวกัน เอกสาร/PRD เดียวกัน Current State เดียวกัน และ Continuation เดียวกัน** แทนการพึ่งความจำของแต่ละแชตหรือแต่ละ Agent

> **หลักการจำง่าย:** ผู้ใช้สั่ง “งาน” ไม่ต้องสั่ง “กฎหมาย” ซ้ำ เมื่อ Project ติดตั้ง UAAC แล้ว Agent ต้อง Auto-Boot และเลือก applicable Skills เอง

---

# ⚡ ใช้งานแบบสั้นที่สุด

## Project ยังไม่ได้ติดตั้ง UAAC

ถ้า Agent เช่น Codex / Claude / Hermes เปิดอยู่ใน **Project เป้าหมาย** แล้ว ให้สั่งเพียง:

```text
ติดตั้งรัฐธรรมนูญ Project จาก
https://github.com/captainhuke-dev/ProjectFramework/tree/hz-framework
ลงใน Project ปัจจุบัน
```

นี่คือ **Canonical Quick Install Command** ของเรา

### Agent ต้องตีความคำสั่งนี้อย่างไร

```text
SOURCE
https://github.com/captainhuke-dev/ProjectFramework/tree/hz-framework
= แหล่งค้นหา Framework + UAAC installation protocol

TARGET
Project/workspace ที่ Agent กำลังเปิดอยู่
= Project ที่ต้องติดตั้ง
```

**ห้ามสลับ SOURCE กับ TARGET** และห้ามแก้ `captainhuke-dev/ProjectFramework` เพียงเพราะ URL ของมันถูกส่งมาในคำสั่งติดตั้ง

เมื่อได้รับคำสั่งข้างต้น Agent ต้องทำเองตามลำดับ:

```text
1. เปิด root README.md ของ SOURCE นี้
2. ระบุว่าตนกำลังทำงานในบทบาท Agent/Installer
3. อ่าน UAAC.md เพื่อ resolve release/navigation context
4. fresh-read canonical installer:
   universal-ai-agent-constitution/INSTALL-UAAC.md
5. resolve และ pin exact immutable UAAC release identity
6. inventory TARGET Project ก่อน mutation
7. classify GREENFIELD / BROWNFIELD / MONOREPO-NESTED
8. ใช้ isolated adoption branch/worktree หรือ transaction boundary
9. install/reconcile Project Governance
10. map Project Definition / PRD / Requirements / Current State เดิม
11. materialize applicable Skills + platform adapters
12. establish governance/UAAC-BOOT.md เป็น Project front door
13. establish continuation / artifact / state routing
14. validate installation + Auto-Boot + applicable convergence checks
15. publish/readback ตาม authority และ visibility ที่ Project อนุญาต
16. ส่งผลลัพธ์พร้อม ChatGPT Project Instructions แบบสั้นที่สุดให้ Human
```

Agent ต้องปฏิบัติตาม `INSTALL-UAAC.md` เป็น canonical protocol; README นี้เป็น discovery/navigation contract ไม่แทนตัว installer

---

# 🤖 Mandatory Agent Completion Output

เมื่อ Agent ติดตั้งจนถึงสถานะที่มีหลักฐานรองรับตาม authority ที่ได้รับแล้ว **รายงานสุดท้ายต้องมีส่วนนี้เสมอ**:

```text
CHATGPT PROJECT INSTRUCTIONS — COPY THIS

Project นี้ใช้ UAAC: <ACTUAL_PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

`<ACTUAL_PROJECT_UAAC_BOOT_URL>` ต้องเป็น URL จริงของ Project ที่ติดตั้งแล้ว เช่น:

```text
https://github.com/OWNER/PROJECT/blob/<CANONICAL_VISIBLE_REF>/governance/UAAC-BOOT.md
```

ห้ามคืน placeholder ถ้า Agent อ้างว่าพร้อมให้ ChatGPT ใช้งานแล้ว

ถ้ายังไม่มี canonical-visible URL ให้รายงานสถานะตามจริง เช่น:

```text
CHATGPT_PROJECT_BOOT_URL: NOT_YET_CANONICAL_VISIBLE
```

และห้ามอ้างว่า cross-agent setup เสร็จสมบูรณ์

### ทำไมต้องส่งข้อความนี้

Human จะเอาข้อความสั้นนี้ไปใส่ใน **ChatGPT Project → Instructions** เพียงครั้งเดียว หลังจากนั้นผู้ใช้สั่งแต่งานตามปกติ ไม่ต้อง prompt กฎหมาย, PRD, continuation หรือชื่อ Skill ซ้ำอีก

---

# ✅ Project ติดตั้งแล้ว

ทุก Human / ChatGPT / Codex / Claude / Hermes / CLI เริ่มจาก front door ของ Project:

```text
governance/UAAC-BOOT.md
```

สำหรับ remote Agent ให้ใช้ canonical URL ของไฟล์เดียวกัน

หลังจากนั้นผู้ใช้สั่งงานปกติ เช่น:

```text
แก้ bug login นี้และรัน tests
```

Agent ต้องทำภายในเอง:

```text
Minimal Bootstrap Kernel
→ Project Binding check
→ governance/UAAC-BOOT.md
→ freshness/applicability check
→ Project Law / PRD / Current State / Authority
→ applicable Skills
→ work
→ pre-write context recheck
→ checkpoint / handoff / report ตาม applicability
```

---

# 🧑 สำหรับมนุษย์ — ดูตัวอย่างตั้งแต่ศูนย์

ถ้าต้องการดู flow ตั้งแต่ Windows folder ว่าง → Codex → GitHub → ChatGPT ให้เปิด:

➡️ **[HUMAN-INSTALL-WALKTHROUGH-TH.md](HUMAN-INSTALL-WALKTHROUGH-TH.md)**

ตัวอย่างครอบคลุม:

```text
Windows folder ว่าง
→ เปิด Codex ใน folder
→ สร้าง Git/GitHub Project
→ ติดตั้ง UAAC
→ push canonical Project state
→ สร้าง ChatGPT Project
→ ใส่ ChatGPT Project Instructions
→ ทดสอบ Codex ↔ ChatGPT convergence
→ เริ่มสั่งงานปกติ
```

ไฟล์ Human Walkthrough เป็น **FOR HUMAN / NON-NORMATIVE / DO NOT EXECUTE** เท่านั้น

Agent ห้ามเอา path, repository, branch หรือ command ตัวอย่างจาก Human Guide ไปใช้เป็น Current Truth

---

# 🤖 สำหรับ Agent / Installer — canonical protocol

Agent ที่ได้รับคำสั่งให้ “ติดตั้งรัฐธรรมนูญ Project” ต้องใช้:

➡️ **[universal-ai-agent-constitution/INSTALL-UAAC.md](universal-ai-agent-constitution/INSTALL-UAAC.md)**

```text
Human Guide = explanation/example
Root README = discovery + quick-install contract
INSTALL-UAAC.md = canonical Agent installation protocol
```

ตัว installer ครอบคลุม:

- authority / target / immutable source resolution
- inventory before mutation
- GREENFIELD / BROWNFIELD / MONOREPO handling
- isolated staging
- Minimal Bootstrap Kernel
- Project Binding
- Project Law
- State Authority Map
- Project Document Registry / PRD routing
- Capability Pack / Skills
- Agent Adapter Registry
- Auto-Boot
- Current Continuation / lineage
- visibility / receiver access
- pre-write TOCTOU recheck
- claim contracts
- installation validation
- atomic commit/publication
- remote readback
- EFFECTIVE adoption separation

---

# 📜 UAAC Front Door

➡️ **[UAAC.md](UAAC.md)**

`UAAC.md` เป็น navigation page ของ UAAC ไม่ใช่ Project Law หรือ Current Truth

Canonical UAAC v4.2.0 release ที่ผ่าน remote verification:

```text
Version: 4.2.0
Release commit: 5a309d8d38046bf3e8cd4beb2fc82a872f211cad
Canonical laws: 25
Conformance scenarios: 142
```

Package:

➡️ **[universal-ai-agent-constitution/](universal-ai-agent-constitution/)**

เอกสารสำคัญ:

- [Canonical Agent Installer](universal-ai-agent-constitution/INSTALL-UAAC.md)
- [UAAC README](universal-ai-agent-constitution/README.md)
- [Constitution v4.2](universal-ai-agent-constitution/UAAC-v4.2-CONSTITUTION.md)
- [Adoption Guide](universal-ai-agent-constitution/ADOPTION-GUIDE.md)
- [Adoption Runbook](universal-ai-agent-constitution/ADOPTION-RUNBOOK.md)
- [Installation Threat Model](universal-ai-agent-constitution/INSTALLATION-THREAT-MODEL.md)
- [Systems Thinking Analysis](universal-ai-agent-constitution/SYSTEMS-THINKING-ANALYSIS-TH.md)
- [Release Receipt](universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml)

> `universal-ai-agent-constitution/` v4.2.0 เป็น verified release package การปรับ UX/navigation ที่ root ไม่เปลี่ยน package identity และไม่ควรแก้ package bytes เดิมโดยไม่ออก release/version ใหม่

---

# ProjectFramework 1.2.2

ProjectFramework เป็น framework สำหรับทำให้ Project มีโครงสร้าง Current Truth, Authority, Requirements, Decisions, Evidence, Risks, Assumptions, Milestones, Outcomes, Dependencies, Change Control, Handoff, Migration, Technical Design, Deployment knowledge และ Continuation ที่ reconstruct ได้

Package หลัก:

➡️ **[managing-project-source/](managing-project-source/)**

เอกสารหลัก:

- [Framework Release](managing-project-source/FRAMEWORK-RELEASE.yaml)
- [Managing Project Source Skill](managing-project-source/SKILL.md)
- [Core Governance Rules](managing-project-source/references/core-governance-rules.md)
- [Project Source templates](managing-project-source/templates/)

ProjectFramework pin ของแต่ละ Project และ UAAC release identity เป็นคนละ dependency; การติดตั้ง UAAC ไม่ได้อนุมัติการ upgrade ProjectFramework pin โดยอัตโนมัติ

---

# Architecture หลัก

```text
                         HUMAN
                           │
          ┌────────────────┴─────────────────┐
          ▼                                  ▼
 Human Walkthrough                   one-line install command
   explanation only                          │
                                              ▼
                                       Installer Agent
                                              │
                                  root README discovery
                                              │
                                              ▼
                                       INSTALL-UAAC.md
                                              │
                                              ▼
                                           Project
                                              │
                                      Minimal Boot Kernel
                                              │
                                              ▼
                                   governance/UAAC-BOOT.md
                                              │
              ┌───────────────────────────────┼───────────────────────────────┐
              ▼                               ▼                               ▼
       Constitution/Law              Project docs / PRD             State / Continuation
              │                               │                               │
              └───────────────────────────────┼───────────────────────────────┘
                                              ▼
                                      Applicable Skills
                                              │
                        ┌─────────────────────┼─────────────────────┐
                        ▼                     ▼                     ▼
                     ChatGPT                Codex             Claude/Hermes/CLI
```

เราไม่ได้ทำให้ AI ทุกตัวมี memory เดียวกัน แต่ทำให้ทุกตัวกลับมา resolve canonical Project state ชุดเดียวกัน

---

# โครงสร้าง Repository บน `hz-framework`

```text
ProjectFramework/
├── README.md                              ← Agent/Human discovery front page
├── HUMAN-INSTALL-WALKTHROUGH-TH.md       ← Human example
├── UAAC.md                                ← UAAC navigation front door
├── .gitattributes
├── managing-project-source/               ← ProjectFramework package
├── universal-ai-agent-constitution/       ← UAAC v4.2.0 verified package
├── uaac-v4.2-reference-project/           ← reference/convergence evidence project
├── examples/
└── docs/
```

หลังติดตั้ง Project ปลายทางจะประมาณ:

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
│   ├── CURRENT-CONTINUATION.yaml
│   └── continuation/<LINEAGE>/CURRENT.yaml
├── project-docs/
└── vendor/uaac/v4.2.0/
```

---

# Result-state discipline

```text
COPIED ≠ CORE_INSTALLED ≠ INSTALLATION_VALIDATED ≠ EFFECTIVE
EXECUTED ≠ VERIFIED ≠ ACCEPTED ≠ PUBLISHED ≠ DEPLOYED ≠ CLOSED
```

Agent ต้องรายงานสถานะแยกตามหลักฐาน ห้ามใช้ `DONE` หรือ `COMPLETE` ครอบสถานะที่ยังไม่ได้พิสูจน์

---

# สิ่งที่ไม่ใช่ Current Truth โดยอัตโนมัติ

```text
Conversation / Chat memory      != Current Truth
Agent memory / OpenViking       != Current Truth
Wiki / Retrieval / Summary      != Verification
Skill file presence             != Invocation / Authority
Local worktree                  != Receiver-visible shared state
Prompt                          != Authority
Process exit                    != Verified completion
```

เมื่อ source ขัดกัน ให้ resolve ตาม Project Law + State Authority Map + canonical artifact identity ไม่ใช่เลือกจากความจำ

---

# Branch และ Release Policy

- `main` คือ upstream ProjectFramework baseline
- `hz-framework` คือ distribution branch ที่เราใช้สำหรับ Framework + UAAC
- Project ปลายทางต้อง vendor/pin UAAC identity แบบ immutable
- Project ที่ติดตั้งแล้วไม่ auto-follow `hz-framework` HEAD
- root navigation/docs อาจปรับปรุงได้โดยไม่เปลี่ยน UAAC v4.2 verified package bytes
- การ upgrade UAAC หรือ ProjectFramework ใน Project ปลายทางต้องประเมินผลกระทบ, validate และ promote ตาม governance ของ Project นั้น

---

# TL;DR

### ติดตั้งครั้งแรก

```text
ติดตั้งรัฐธรรมนูญ Project จาก
https://github.com/captainhuke-dev/ProjectFramework/tree/hz-framework
ลงใน Project ปัจจุบัน
```

### Agent ทำเอง

```text
README
→ UAAC.md
→ INSTALL-UAAC.md
→ inventory
→ pin immutable release
→ install/reconcile governance + docs + Skills
→ UAAC-BOOT
→ validate
→ canonical visibility/readback
```

### Agent ต้องส่งกลับให้ Human

```text
CHATGPT PROJECT INSTRUCTIONS — COPY THIS

Project นี้ใช้ UAAC: <ACTUAL_PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

### หลังจากนั้น

ผู้ใช้สั่งแต่งาน ส่วนการอ่านกฎหมาย, Project state และเลือก Skill เป็นหน้าที่ของ Agent
