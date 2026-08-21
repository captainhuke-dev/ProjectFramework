# Universal AI Agent Constitution (UAAC)

จุดเริ่มต้นของรัฐธรรมนูญกลางสำหรับ Project ที่มีมนุษย์และ AI Agent ทำงานร่วมกัน

> **เป้าหมาย:** ผู้ใช้สั่ง “งาน” ไม่ต้องสั่ง “กฎหมาย” ซ้ำ เมื่อ Project ติดตั้ง UAAC แล้ว Agent ต้อง Auto-Boot จาก Project front door และเลือก applicable Skills เอง

---

# ⚡ Agent Quick Install

ถ้า Agent เช่น Codex / Claude / Hermes เปิดอยู่ใน Project เป้าหมายแล้ว ให้ผู้ใช้สั่งเพียง:

```text
ติดตั้งรัฐธรรมนูญ Project จาก
https://github.com/captainhuke-dev/ProjectFramework/tree/hz-framework
ลงใน Project ปัจจุบัน
```

Agent ต้องตีความว่า:

```text
SOURCE = ProjectFramework/hz-framework
TARGET = Project/workspace ที่ Agent กำลังเปิดอยู่
```

แล้วทำตามลำดับ:

```text
root README.md
→ UAAC.md
→ universal-ai-agent-constitution/INSTALL-UAAC.md
→ resolve immutable UAAC release
→ inventory TARGET Project
→ install/reconcile governance + Project docs + Skills
→ establish governance/UAAC-BOOT.md
→ validate
→ publish/readback ตาม authority
→ ส่ง ChatGPT Project Instructions ให้ Human
```

**ห้ามแก้ SOURCE เพียงเพราะ URL ของ SOURCE ถูกใช้ในคำสั่งติดตั้ง**

Canonical Agent installation protocol:

[`universal-ai-agent-constitution/INSTALL-UAAC.md`](universal-ai-agent-constitution/INSTALL-UAAC.md)

---

# 🤖 Mandatory completion output

เมื่อ Agent ติดตั้งจนมี canonical-visible Project front door แล้ว รายงานสุดท้ายต้องส่งข้อความนี้กลับให้ Human พร้อมแทน URL จริง:

```text
CHATGPT PROJECT INSTRUCTIONS — COPY THIS

Project นี้ใช้ UAAC: <ACTUAL_PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

ตัวอย่าง URL จริง:

```text
https://github.com/OWNER/PROJECT/blob/<CANONICAL_VISIBLE_REF>/governance/UAAC-BOOT.md
```

ถ้ายังไม่มี URL ที่ receiver อ่านได้จริง ให้รายงานตามจริงว่า `NOT_YET_CANONICAL_VISIBLE` และห้ามอ้างว่า cross-agent setup เสร็จ

---

# 🧑 Human walkthrough

สำหรับมนุษย์ที่ต้องการดูตัวอย่างตั้งแต่ Windows folder ว่าง → Codex → GitHub → ChatGPT:

[`HUMAN-INSTALL-WALKTHROUGH-TH.md`](HUMAN-INSTALL-WALKTHROUGH-TH.md)

เอกสารนี้เป็น **FOR HUMAN / NON-NORMATIVE / DO NOT EXECUTE** และไม่ใช่ Agent installation protocol

UAAC v4.2.0 verified package ยังคงเก็บ release copy ไว้ที่:

`universal-ai-agent-constitution/HUMAN-INSTALL-WALKTHROUGH-TH.md`

root file เป็น human convenience view เพื่อไม่แก้ package bytes ที่ผ่าน remote verification แล้ว

---

# ✅ Project ติดตั้งแล้ว

มนุษย์, ChatGPT, Codex, Claude, Hermes และ Agent/CLI ทุกตัวเริ่มจาก Project front door:

```text
governance/UAAC-BOOT.md
```

front door นี้เป็น router ไปยัง:

- Constitution ที่ Project pin ไว้
- Project Law
- State Authority Map
- Project Document Registry / PRD / Requirements
- Capability Pack / Skills
- Agent Adapter Registry
- Claim Contracts
- Current Continuation / lineage
- canonical artifact/state routes

หลังติดตั้ง ผู้ใช้ควรสั่งงานธรรมดา เช่น:

```text
แก้ bug login นี้และรัน tests
```

Agent ต้อง Auto-Boot และ resolve applicable governance/state/Skills เอง

---

# Release identity

Canonical UAAC v4.2.0 release ที่ผ่าน remote verification:

```text
Version: 4.2.0
Release commit: 5a309d8d38046bf3e8cd4beb2fc82a872f211cad
Canonical laws: 25
Conformance scenarios: 142
```

Mutable branch URL ใช้ discovery ได้ แต่ Project ปลายทางต้อง pin immutable release identity ก่อนถือเป็น effective Constitution

---

# เอกสารหลัก

- [Root README / Quick Install Contract](README.md)
- [Human install walkthrough](HUMAN-INSTALL-WALKTHROUGH-TH.md)
- [Canonical Agent installation protocol](universal-ai-agent-constitution/INSTALL-UAAC.md)
- [UAAC package README](universal-ai-agent-constitution/README.md)
- [Adoption runbook](universal-ai-agent-constitution/ADOPTION-RUNBOOK.md)
- [Adoption guide](universal-ai-agent-constitution/ADOPTION-GUIDE.md)
- [Constitution v4.2](universal-ai-agent-constitution/UAAC-v4.2-CONSTITUTION.md)
- [Systems Thinking analysis](universal-ai-agent-constitution/SYSTEMS-THINKING-ANALYSIS-TH.md)
- [Installation threat model](universal-ai-agent-constitution/INSTALLATION-THREAT-MODEL.md)
- [Release receipt](universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml)

---

# หลักสำคัญ

> เราไม่ได้ทำให้ AI ทุกตัวมีความจำเดียวกัน แต่ทำให้ AI ทุกตัวกลับมาอ่านรัฐธรรมนูญและทะเบียนความจริงของ Project ชุดเดียวกัน

```text
Memory != Current Truth
Retrieval != Verification
Skill != Authority
Prompt != Authority
Process Exit != Verified Completion
Local Work != Receiver-visible Shared State
```

`UAAC.md` เป็น upstream navigation page เท่านั้น ไม่ใช่ Project Law, Authority หรือ runtime Current Truth ของ Project ที่ติดตั้งแล้ว
