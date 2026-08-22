---
document_type: UAAC_HUMAN_INSTALL_WALKTHROUGH
audience: HUMAN
normative: false
authority_effect: NONE
truth_authority: NONE
agent_execution: DO_NOT_EXECUTE
canonical_agent_install_protocol: INSTALL-UAAC.md
example_values_are_current_truth: false
---

# FOR HUMAN READING ONLY — ตัวอย่างติดตั้ง UAAC จากศูนย์บน Windows

> เอกสารนี้เป็น **คำอธิบายและตัวอย่างสำหรับมนุษย์** ไม่ใช่ Agent protocol, ไม่ใช่ Project Law, ไม่ใช่ Current Truth และห้าม Agent นำ path, repository, branch, command หรือตัวอย่างในเอกสารนี้ไป execute โดยอัตโนมัติ
>
> Agent/Installer ต้อง fresh-read และปฏิบัติตาม [`INSTALL-UAAC.md`](INSTALL-UAAC.md) จาก release ที่ pin แล้ว พร้อม resolve Project จริงก่อนทำงานเสมอ

## เป้าหมายของตัวอย่าง

เริ่มจาก:

```text
Windows folder ว่าง: C:\Projects\Project-A
Codex: ชี้ working directory มาที่ folder นี้
ChatGPT: เพิ่งสร้าง Project ใหม่และยังไม่มี instruction
GitHub: ยังไม่มี repository ของ Project-A
```

จบที่:

```text
Windows Codex ─┐
               ├─► GitHub Project-A ─► governance/UAAC-BOOT.md
ChatGPT Project┘
```

Codex และ ChatGPT ไม่จำเป็นต้องแชร์ conversation หรือ memory แต่ต้องอ่าน Project identity, governance, documents, artifacts และ continuation state จาก canonical surface เดียวกัน

## สัญลักษณ์ในเอกสาร

- **🧑 HUMAN ACTION** — คนต้องตัดสินใจหรือกดทำเอง
- **🤖 AGENT ACTION (DESCRIPTIVE ONLY)** — อธิบายว่า Agent ที่ถูกสั่งผ่าน canonical protocol จะทำอะไร ไม่ใช่คำสั่งให้ execute จากเอกสารนี้
- **📋 COPY/PASTE PROMPT** — ข้อความที่มนุษย์ตั้งใจ copy ไปสั่ง Agent
- **✅ VERIFY** — สิ่งที่ต้องตรวจให้เห็นจริง

---

## Step 0 — เริ่มจาก folder เปล่า

### 🧑 HUMAN ACTION

สร้างหรือเลือก folder เช่น:

```text
C:\Projects\Project-A
```

เปิด Codex และชี้ Working Directory มาที่ folder นี้ ห้ามถือว่า `Project-A` ในตัวอย่างเป็นชื่อจริงของ Project อื่น

### ✅ VERIFY

- Codex เห็น path ที่มนุษย์เลือกจริง
- ยังไม่มี `governance/UAAC-BOOT.md`
- ยังไม่มี Project Law/PRD/Current Continuation
- Project ถูกจัดเป็น `GREENFIELD` เว้นแต่พบ source เดิมภายใน boundary

## Step 1 — เริ่ม Git และสร้าง canonical repository

### 🧑 HUMAN ACTION

มนุษย์เลือก visibility (`private`/`public`), owner, repository name และ canonical branch ตามนโยบายจริง

ตัวอย่าง PowerShell เพื่ออธิบายแนวคิดเท่านั้น:

```powershell
cd C:\Projects\Project-A
git init -b main
gh repo create OWNER/PROJECT-A --private --source . --remote origin
```

### ✅ VERIFY

- `git rev-parse --show-toplevel` ตรงกับ Project boundary
- `git remote get-url origin` ตรงกับ repository ที่มนุษย์เลือก
- nested repo, junction หรือ symlink ไม่พาออกนอก boundary

## Step 2 — สั่ง Codex ติดตั้ง UAAC

### 📋 COPY/PASTE PROMPT

```text
ติดตั้งรัฐธรรมนูญ Project ตาม UAAC จาก:
<UAAC_INSTALL_URL_PINNED_OR_DISCOVERY_URL>

ให้กับ Project ปัจจุบัน:
<ACTUAL_PROJECT_ROOT>

Canonical repository:
<ACTUAL_PROJECT_REPO_URL>

Canonical branch/ref policy:
<ACTUAL_CANONICAL_REF_POLICY>

Project นี้คาดว่าเป็น GREENFIELD แต่ให้ inventory และยืนยันก่อนแก้
ทำตาม INSTALL-UAAC.md จนถึงสถานะที่มีหลักฐานรองรับ
ห้ามแก้ UAAC upstream และห้ามใช้ตัวอย่างจาก Human walkthrough เป็น Project truth
```

### 🤖 AGENT ACTION (DESCRIPTIVE ONLY)

Installer Agent จะ resolve release identity ที่ immutable, inventory Project, สร้าง/reconcile governance, Project documents, Skills/adapters, continuation และ validation artifacts ตาม canonical Agent protocol

## Step 3 — ให้ข้อมูล Project ขั้นต่ำ

### 🧑 HUMAN ACTION

ถ้า Project ยังไม่มี definition/requirements ให้มนุษย์ระบุอย่างน้อย:

```text
ชื่อ Project:
เป้าหมาย:
ผู้ใช้งานหลัก:
ขอบเขตรอบแรก:
สิ่งที่ไม่อยู่ในขอบเขต:
ความเสี่ยง/ข้อจำกัดสำคัญ:
```

Agent ห้ามแต่งข้อมูลเพื่อเปลี่ยน `BLOCKED` เป็น `RESOLVED`

## Step 4 — ตรวจโครงสร้างหลัง install

### ✅ VERIFY

อย่างน้อยควร resolve ได้:

```text
governance/PROJECT-BINDING.yaml
governance/UAAC-BOOT.md
governance/CONSTITUTION-ADOPTION.yaml
governance/PROJECT-LAWS/PROJECT_RULES.md
governance/STATE-AUTHORITY-MAP.yaml
governance/PROJECT-DOCUMENT-REGISTRY.yaml
governance/PROJECT-CAPABILITY-PACK.yaml
governance/SKILL-REGISTRY.yaml
governance/AGENT-ADAPTER-REGISTRY.yaml
governance/CURRENT-CONTINUATION.yaml
governance/INSTALLATION-VALIDATION.yaml
```

`UAAC-BOOT.md` ต้องเป็น router เท่านั้น:

```yaml
authority_effect: NONE
truth_authority: NONE
```

## Step 5 — Commit/push canonical-visible state

### 🤖 AGENT ACTION (DESCRIPTIVE ONLY)

ก่อน write/commit Agent recheck Project binding, governance identity, continuation predecessor และ artifact base จาก attempt/boot receipt หากเปลี่ยนต้องรายงาน `TASK_CONTEXT_STALE`

### ✅ VERIFY

- local-only work ถูกระบุว่า `LOCAL_ONLY` หรือ `PENDING_CANONICAL_PUBLICATION`
- ก่อน handoff ต้อง publish/share state ที่ผู้รับเข้าถึงได้
- remote readback แสดง bytes/identity ที่ตั้งใจ

## Step 6 — สร้าง ChatGPT Project และเชื่อม GitHub

### 🧑 HUMAN ACTION

1. สร้าง ChatGPT Project ใหม่
2. เชื่อม GitHub connector ให้มีสิทธิ์อ่าน Project repository
3. ทดลองเปิด canonical `governance/UAAC-BOOT.md` จริง
4. ถ้าอ่านไม่ได้ ห้ามถือว่าเชื่อมสำเร็จ

## Step 7 — ใส่ ChatGPT Project Instructions แบบสั้น

### 📋 COPY/PASTE PROMPT

```text
Project นี้ใช้ UAAC: <PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

ข้อความนี้เป็น launcher ไม่ใช่กฎหมายและไม่ใช่หลักฐานว่า connector อ่านได้

## Step 8 — ทดสอบ Codex ↔ ChatGPT convergence

### 🧑 HUMAN ACTION

ถามทั้งสองตัวแยกกันว่า:

```text
รายงาน Project ID, Constitution identity, Project Law identity,
State Authority Map, Project documents/PRD, Skill/Adapter registries,
Current Continuation/lineage, artifact ล่าสุด และ exact next action
```

### ✅ VERIFY

ผลต้องตรงกันใน identity ที่ material และแต่ละ Agent ต้องมี canonical-access receipt ของตัวเอง

## Step 9 — เริ่มสั่งงานปกติ

หลัง Project ผ่าน validation ผู้ใช้ควรสั่งเพียงงาน เช่น:

```text
แก้ bug login นี้และรัน tests
```

Agent ต้อง Auto-Boot และเลือก applicable procedures เอง ผู้ใช้ไม่ต้องใส่กฎหมายหรือชื่อ Skill ซ้ำ

## Step 10 — วันถัดไปหรือ session ใหม่

Codex อาจหยุดหลัง checkpoint แล้ว ChatGPT session ใหม่ต้อง reconstruct completed, pending, blocker, artifact และ exact next action จาก canonical continuation โดยไม่ต้องอ่านข้อความแชตเดิม

---

## สิ่งที่ตัวอย่างนี้ไม่รับรอง

- path/ชื่อ repository/branch ในตัวอย่างไม่ใช่ Current Truth
- การมีไฟล์ Skill ไม่พิสูจน์ว่า platform invoke Skill
- URL ใน instruction ไม่พิสูจน์ connector access
- local Codex state ไม่เท่ากับ remote-visible state จน publish/readback
- การ copy Constitution ไม่เท่ากับ `INSTALLATION_VALIDATED` หรือ `EFFECTIVE`

## เส้นทางที่ถูกต้อง

```text
Human ต้องการเข้าใจ → เอกสารนี้
Agent ต้องติดตั้ง       → INSTALL-UAAC.md
Agent ทำงานใน Project   → Minimal Bootstrap Kernel → governance/UAAC-BOOT.md → registered UAAC-BOOT
```
