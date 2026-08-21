# ProjectFramework — HZ Framework + UAAC

> Repository: `captainhuke-dev/ProjectFramework`  
> Distribution branch: **`hz-framework`**  
> Project Source Framework: **1.2.2**  
> Universal AI Agent Constitution (UAAC): **4.2.0**

สาขา `hz-framework` คือชุดที่เราใช้รวม **ProjectFramework + UAAC** สำหรับสร้างและควบคุม Project ที่มี Human และ AI Agent หลายตัวทำงานร่วมกัน เช่น ChatGPT, Codex, Claude, Hermes และ CLI Agent

เป้าหมายหลักคือทำให้ Agent ทุกตัวกลับมาอ่าน **Project เดียวกัน กฎหมายเดียวกัน เอกสาร/PRD เดียวกัน Current State เดียวกัน และ Continuation เดียวกัน** แทนการพึ่งความจำของแต่ละแชตหรือแต่ละ Agent

> **หลักการจำง่าย:** ผู้ใช้สั่ง “งาน” ไม่ต้องสั่ง “กฎหมาย” ซ้ำ เมื่อ Project ติดตั้ง UAAC แล้ว Agent ต้อง Auto-Boot และเลือก applicable Skills เอง

---

# 🚀 ถ้าคุณเพิ่งเข้ามา ให้เริ่มตรงนี้

## 🧑 สำหรับมนุษย์ — ดูตัวอย่างตั้งแต่ศูนย์

ถ้าต้องการเห็นภาพตั้งแต่:

```text
Windows folder ว่าง
→ เปิด Codex ใน folder
→ สร้าง Git/GitHub Project
→ ติดตั้ง UAAC
→ push canonical Project state
→ สร้าง ChatGPT Project
→ เชื่อม ChatGPT + Codex
→ ทดสอบว่าอ่าน Project state ตรงกัน
```

ให้เปิดไฟล์นี้ที่ root ได้เลย:

➡️ **[HUMAN-INSTALL-WALKTHROUGH-TH.md](HUMAN-INSTALL-WALKTHROUGH-TH.md)**

ไฟล์นี้เป็น **FOR HUMAN / NON-NORMATIVE / DO NOT EXECUTE** ใช้เพื่ออธิบายและยกตัวอย่างเท่านั้น

## 🤖 สำหรับ Agent / Installer — ติดตั้งจริง

Agent ที่ได้รับคำสั่งให้ “ติดตั้งรัฐธรรมนูญ Project” ต้องใช้ canonical installation protocol:

➡️ **[universal-ai-agent-constitution/INSTALL-UAAC.md](universal-ai-agent-constitution/INSTALL-UAAC.md)**

```text
Human Guide = อ่านเพื่อเข้าใจ
INSTALL-UAAC.md = Agent protocol สำหรับทำจริง
```

## 📜 จุดเริ่มต้น UAAC

➡️ **[UAAC.md](UAAC.md)**

ใช้เพื่อดูภาพรวม UAAC, จุดเริ่มต้นของ Human/Agent และเส้นทางไปยัง Constitution, Skills, tests และ release artifacts

---

# ถ้าจำได้แค่ 2 อย่าง

## 1. Project ยังไม่ได้ติดตั้ง UAAC

สั่ง Agent เช่น Codex ด้วย prompt แบบนี้:

```text
ติดตั้งรัฐธรรมนูญ Project ตาม UAAC จาก:
https://github.com/captainhuke-dev/ProjectFramework/blob/hz-framework/universal-ai-agent-constitution/INSTALL-UAAC.md

ให้กับ Project:
<PROJECT_REPO_URL_OR_LOCAL_ROOT>

ทำตาม INSTALL-UAAC.md จนมีหลักฐานรองรับ INSTALLATION_VALIDATED
ตั้ง governance/UAAC-BOOT.md เป็น front door ของ Project
และพิสูจน์ Auto-Boot + cross-agent convergence ก่อนรายงานผล
```

URL ของ branch ใช้เพื่อ **ค้นหา installation protocol** เท่านั้น Installer ต้อง resolve และ pin exact immutable UAAC identity ก่อนนำไปเป็น effective Constitution ของ Project

## 2. Project ติดตั้ง UAAC แล้ว

ทุก Human / ChatGPT / Codex / Claude / Hermes / CLI เริ่มจาก:

```text
governance/UAAC-BOOT.md
```

สำหรับ remote Agent ใช้ canonical URL ของไฟล์เดียวกัน

หลังจากนั้นผู้ใช้สั่งงานปกติ เช่น:

```text
แก้ bug login นี้และรัน tests
```

Agent ต้อง Auto-Boot, resolve canonical Project state และเลือก applicable Skills เอง

---

# Architecture หลัก

```text
                         HUMAN
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
HUMAN-INSTALL-WALKTHROUGH-TH.md       copy install prompt
        │                                     │
   explanation                               ▼
   only                                Installer Agent
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

# UAAC v4.2.0

UAAC คือรัฐธรรมนูญกลางของ AI Project

Canonical release ที่ผ่าน remote verification:

```text
Version: 4.2.0
Release commit: 5a309d8d38046bf3e8cd4beb2fc82a872f211cad
Canonical laws: 25
Conformance scenarios: 142
```

Package:

➡️ **[universal-ai-agent-constitution/](universal-ai-agent-constitution/)**

เอกสารสำคัญ:

- [Agent installation protocol](universal-ai-agent-constitution/INSTALL-UAAC.md)
- [UAAC README](universal-ai-agent-constitution/README.md)
- [Constitution v4.2](universal-ai-agent-constitution/UAAC-v4.2-CONSTITUTION.md)
- [Adoption Guide](universal-ai-agent-constitution/ADOPTION-GUIDE.md)
- [Adoption Runbook](universal-ai-agent-constitution/ADOPTION-RUNBOOK.md)
- [Installation Threat Model](universal-ai-agent-constitution/INSTALLATION-THREAT-MODEL.md)
- [Systems Thinking Analysis](universal-ai-agent-constitution/SYSTEMS-THINKING-ANALYSIS-TH.md)
- [Release Receipt](universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml)

> `universal-ai-agent-constitution/` v4.2.0 เป็น release package ที่ตรวจแล้ว เอกสาร navigation ที่ root อาจถูกปรับปรุงได้ แต่ไม่ควรแก้ package bytes เดิมโดยไม่ออก release/version ใหม่ตาม governance

---

# Human Walkthrough กับ Agent Protocol ต่างกันอย่างไร

| เอกสาร | ผู้ใช้หลัก | Execute ได้หรือไม่ | Authority / Truth |
|---|---|---:|---|
| `HUMAN-INSTALL-WALKTHROUGH-TH.md` | Human | ❌ ไม่ใช่ runbook | NONE |
| `universal-ai-agent-constitution/INSTALL-UAAC.md` | Installer Agent | ✅ ตาม protocol | Procedural contract ภายใต้ UAAC |
| `UAAC.md` | Human/Agent navigation | ❌ ไม่ใช่ Project Law | NONE |
| Project `governance/UAAC-BOOT.md` | ทุก Agent หลัง install | ✅ เป็น router | NONE; route ไป canonical sources |

ดังนั้น Agent ห้ามเอา path, repo, branch หรือ command ตัวอย่างจาก Human Guide ไปใช้เป็น Current Truth

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

### Framework 1.2.2 เพิ่มอะไร

Framework 1.2.2 เพิ่ม **Git Base Freshness and Forward-Port governance** สำหรับ branch/worktree:

```text
FRESH
STALE_NON_SEMANTIC
STALE_SEMANTIC
UNKNOWN
```

งานใหม่ต้องเริ่มจาก canonical integration target ที่ fresh หรือประกาศ `STACKED_WORK` อย่างชัดเจน ไม่ใช่เริ่มต่อจาก feature branch ที่บังเอิญ checkout อยู่

หลักสำคัญ:

```text
Mergeable != Acceptable
Responsibility != Authority
Memory != Current Truth
Process Exit != Verified Completion
```

Existing Project ไม่ auto-upgrade เมื่อ Framework upstream เปลี่ยน ต้องใช้ governed migration/forward-port ตาม Project Law

---

# โครงสร้าง Repository บน `hz-framework`

```text
ProjectFramework/
├── README.md                              ← หน้าแรกของเรา
├── HUMAN-INSTALL-WALKTHROUGH-TH.md       ← Human example อ่านง่ายจาก root
├── UAAC.md                                ← UAAC front door
├── .gitattributes
├── managing-project-source/               ← ProjectFramework package
├── universal-ai-agent-constitution/       ← UAAC v4.2.0 verified package
├── examples/
└── docs/
```

ภายใน Project ที่ติดตั้ง UAAC แล้ว โครงมาตรฐานจะประมาณ:

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

# ChatGPT Project Instructions แบบสั้น

หลังติดตั้ง Project แล้ว ให้ ChatGPT Project Instructions ชี้ Project front door เท่านั้น:

```text
Project นี้ใช้ UAAC: <PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

ไม่ต้อง copy Constitution, PRD หรือ Current State เข้า Project Instructions

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
- การแก้เอกสาร navigation ของ `hz-framework` ไม่ควรเปลี่ยน UAAC v4.2 package bytes
- Project ปลายทางต้อง vendor/pin UAAC identity แบบ immutable
- Project ที่ติดตั้งแล้วไม่ auto-follow `hz-framework` HEAD

ถ้าจะ upgrade UAAC หรือ ProjectFramework ใน Project ปลายทาง ต้องประเมินผลกระทบ, validate และ promote ตาม governance ของ Project นั้น

---

# สรุป

```text
อยากเข้าใจตั้งแต่ศูนย์
→ HUMAN-INSTALL-WALKTHROUGH-TH.md

ให้ Agent ติดตั้งจริง
→ universal-ai-agent-constitution/INSTALL-UAAC.md

อยากดู UAAC
→ UAAC.md

Project ติดตั้งแล้ว
→ governance/UAAC-BOOT.md

จากนั้นผู้ใช้สั่ง “งาน” ตามปกติ
→ Agent Auto-Boot + ใช้ applicable Skills เอง
```

**เป้าหมายสุดท้าย:** Human ไม่ต้องจำกฎทุกข้อ และ Agent ไม่ต้องแชร์ memory กัน แต่ทุกฝ่ายต้องกลับมาอ่าน canonical Project state ชุดเดียวกันเสมอ
