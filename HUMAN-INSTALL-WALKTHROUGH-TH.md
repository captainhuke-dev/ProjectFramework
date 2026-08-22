---
document_type: UAAC_V5_HUMAN_INSTALL_WALKTHROUGH_ROOT_VIEW
audience: HUMAN
normative: false
authority_effect: NONE
truth_authority: NONE
agent_execution: DO_NOT_EXECUTE_AS_A_SCRIPT
canonical_agent_install_guide: universal-ai-agent-constitution/INSTALL-UAAC.md
---

# ตัวอย่างติดตั้ง UAAC 5.0 แบบ Constitution-First

เอกสารนี้อธิบายแนวทางสำหรับมนุษย์ ไม่ใช่กฎหมาย ไม่ใช่ runtime procedure และไม่ใช่คำสั่งให้ Agent execute path หรือตัวอย่างโดยอัตโนมัติ ให้ Agent อ่าน [`INSTALL-UAAC.md`](universal-ai-agent-constitution/INSTALL-UAAC.md) และ resolve Project จริงก่อนเสมอ

```text
Installing UAAC does not install or upgrade ProjectFramework.
```

## ผลลัพธ์ขั้นต่ำ

```text
persistent launcher
governance/UAAC.md
governance/UAAC-ADOPTION.yaml
vendor/uaac/v5.0.0/UAAC-v5.0-CONSTITUTION.md + linked laws
```

Project rules are conditional. ถ้า Project มี rules จริงอยู่แล้ว ให้ reuse source เดิม ถ้ายังไม่มี rules ห้ามสร้างไฟล์ rules เปล่าเพื่อให้โครงสร้างดูครบ

## Step 1 — เลือก Project boundary

มนุษย์เลือก folder หรือ repository ของ Project จริง จากนั้นให้ Agent inspect ไฟล์และ instruction ที่มีอยู่ก่อน ห้ามสมมติว่า folder ว่าง และห้ามแก้ repository ต้นทางเพียงเพราะใช้ URL ต้นทางเป็นแหล่งดาวน์โหลด UAAC

## Step 2 — เก็บ Constitution ไว้ใน Project

คัดลอก UAAC 5.0 production distribution ซึ่งมีเฉพาะ Markdown/YAML ไปไว้ใน Project เช่น `vendor/uaac/v5.0.0/` ต้องมี `UAAC-v5.0-CONSTITUTION.md` และ `laws/CONST-001.md` ถึง `CONST-025.md` ให้อ่านได้ในเครื่องแม้ network ใช้งานไม่ได้

Remote URL หรือ Git commit ใช้เป็น provenance และ remote route ได้ แต่ไม่ควรเป็น dependency เดียวของการทำงาน

## Step 3 — สร้าง adoption ขนาดเล็ก

สร้าง `governance/UAAC-ADOPTION.yaml` โดยเริ่มจาก [`UAAC-ADOPTION.yaml`](universal-ai-agent-constitution/templates/UAAC-ADOPTION.yaml) แล้วแทนค่า Project จริง

Required fields มีเพียง:

```text
project.id
project.boundary
constitution.id
constitution.version
constitution.local_locator
constitution.immutable_identity
```

เพิ่ม `project_rules`, `canonical_sources`, `continuation` หรือ `profiles` เฉพาะเมื่อมี route จริงหรือมีการ adopt profile อย่างชัดเจน ห้ามใส่ empty list, runtime status, receipt, epoch, boot mode หรือ registry

## Step 4 — สร้าง Project router

สร้าง `governance/UAAC.md` จาก [`PROJECT-UAAC.md`](universal-ai-agent-constitution/templates/PROJECT-UAAC.md) ไฟล์นี้เป็น router สั้น ๆ ไม่ใช่กฎหมายชุดที่สอง และไม่เก็บ current task/state

Router จะพา Agent ไปตามลำดับ:

```text
UAAC-ADOPTION.yaml
→ local pinned Constitution
→ bounded set ของ laws/rules/canonical sources ที่ materially required
→ sufficient complete coverage
→ work
```

Search, retrieval และ summary ช่วยหา source ได้ แต่ไม่ถือว่าอ่านครบ

## Step 5 — อัปเดต persistent launcher

เลือก template ให้ตรง platform จาก [`templates/platform/`](universal-ai-agent-constitution/templates/platform/) แล้ว merge instruction เข้ากับ launcher เดิมโดยไม่ลบคำสั่งอื่น

ข้อความหลักคือให้ Agent อ่าน `governance/UAAC.md` ก่อน material work โดยผู้ใช้ไม่ต้องพูดคำว่า UAAC, ไม่ต้องตั้งชื่อ Skill และไม่ต้องสั่งให้อ่าน Wiki ซ้ำ

Auto-Boot ใน v5 คือ persistent instruction behavior ไม่ใช่ daemon, boot engine หรือ background service

## Step 6 — ตรวจ Greenfield หรือ Brownfield

### Greenfield

- ไม่มี Project rules จริง → ไม่สร้าง rules file
- ไม่มี continuation ที่จำเป็น → ไม่สร้าง continuation placeholder
- adoption มีเพียง required fields และ route จริง

### Brownfield

- reuse Project rules, PRD, architecture และ current state ที่มีอยู่
- ไม่ copy truth ซ้ำเพียงเพื่อเติม template
- รักษา launcher และ source authority เดิมที่ไม่ขัดกัน
- ถ้าพบ conflict ที่ materially relevant ให้หยุดเฉพาะส่วนที่ได้รับผลและรายงาน

## Step 7 — อ่านกลับโดยไม่พึ่ง runtime

มนุษย์หรือ LLM อ่านเส้นทางนี้ตรง ๆ:

```text
launcher
→ governance/UAAC.md
→ governance/UAAC-ADOPTION.yaml
→ local UAAC-v5.0-CONSTITUTION.md
→ selected laws และ Project sources
```

ยืนยันว่า network ปิดได้, ไม่มี Python/validator requirement, ไม่ติดตั้ง ProjectFramework, Project rules เป็น conditional และ optional profiles ไม่ activate จากการมีไฟล์อยู่

## ส่ง instruction ให้ ChatGPT Project

เมื่อ Project มี local/canonical route ที่ receiver อ่านได้จริง มนุษย์สามารถใส่ข้อความสั้น ๆ เช่น:

```text
ก่อน material work ให้อ่าน governance/UAAC.md และ follow local UAAC routes โดยไม่ต้องให้ผู้ใช้ restate UAAC หรือระบุ Skill; memory != Current Truth
```

หาก receiver อ่าน route ไม่ได้ ให้รายงานตามจริงและอย่าอ้างว่าติดตั้ง cross-agent สำเร็จ

## Migration จาก v4.2

ใช้ [`MIGRATION-v4.2-TO-v5.0.md`](universal-ai-agent-constitution/MIGRATION-v4.2-TO-v5.0.md) แบบ side-by-side เก็บ old pin และ rollback source ไว้จน v5 route ผ่าน readback หลังมี material state change แล้ว rollback ต้องตรวจ compatibility และ remap state ที่ไม่เข้ากันก่อน
