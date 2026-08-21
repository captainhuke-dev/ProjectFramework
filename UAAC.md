# Universal AI Agent Constitution (UAAC)

จุดเริ่มต้นของรัฐธรรมนูญกลางสำหรับ Project ที่มีมนุษย์และ AI Agent ทำงานร่วมกัน

## ถ้าจำได้แค่ 2 อย่าง

### Project ยังไม่ได้ติดตั้ง UAAC

สำหรับมนุษย์ที่ต้องการ walkthrough แบบกดอ่านง่ายจากหน้าแรก:

[`HUMAN-INSTALL-WALKTHROUGH-TH.md`](HUMAN-INSTALL-WALKTHROUGH-TH.md)

เอกสารข้างต้นมีสถานะ **FOR HUMAN / NON-NORMATIVE / DO NOT EXECUTE** และไม่ใช่ Agent installation protocol

> UAAC v4.2.0 verified package ยังคงเก็บ release copy ไว้ที่ `universal-ai-agent-constitution/HUMAN-INSTALL-WALKTHROUGH-TH.md`; root file เป็น human convenience view เพื่อไม่แก้ package bytes ที่ผ่าน remote verification แล้ว

สำหรับ Agent/Installer ให้เริ่มจาก canonical protocol:

[`universal-ai-agent-constitution/INSTALL-UAAC.md`](universal-ai-agent-constitution/INSTALL-UAAC.md)

Prompt มาตรฐาน:

```text
ติดตั้งรัฐธรรมนูญ Project ตาม UAAC จาก

https://github.com/captainhuke-dev/ProjectFramework/blob/hz-framework/universal-ai-agent-constitution/INSTALL-UAAC.md

ให้กับ Project:

<PROJECT_REPO_URL>

ทำตาม INSTALL-UAAC.md จนมีหลักฐานรองรับ INSTALLATION_VALIDATED
ตั้ง governance/UAAC-BOOT.md เป็น front door ของ Project
และพิสูจน์ Auto-Boot + cross-agent convergence ก่อนรายงานผล
```

ลิงก์ branch ด้านบนใช้เพื่อค้นหา installation protocol เท่านั้น ผู้ติดตั้งต้อง resolve และ pin release/commit identity ที่แน่นอนก่อนนำไปเป็นกฎหมายที่มีผลของ Project

### Project ติดตั้ง UAAC แล้ว

มนุษย์, ChatGPT, Codex และ Agent/CLI ทุกตัวเริ่มจาก:

```text
governance/UAAC-BOOT.md
```

front door นี้เป็น router ไปยัง Constitution ที่ Project pin ไว้, Project Law, State Authority Map, Project Document Registry/PRD, Capability Pack/Skills, Claim Contracts และ Current Continuation ของ Project นั้น

## เอกสารหลัก

- [Human install walkthrough — root](HUMAN-INSTALL-WALKTHROUGH-TH.md)
- [README ภาษาไทยและภาพรวมระบบ](universal-ai-agent-constitution/README.md)
- [Canonical Agent installation protocol](universal-ai-agent-constitution/INSTALL-UAAC.md)
- [Adoption runbook](universal-ai-agent-constitution/ADOPTION-RUNBOOK.md)
- [เหตุผลและรูปแบบ adoption](universal-ai-agent-constitution/ADOPTION-GUIDE.md)
- [ตัวรัฐธรรมนูญ v4.2](universal-ai-agent-constitution/UAAC-v4.2-CONSTITUTION.md)
- [Systems Thinking analysis](universal-ai-agent-constitution/SYSTEMS-THINKING-ANALYSIS-TH.md)
- [Installation threat model](universal-ai-agent-constitution/INSTALLATION-THREAT-MODEL.md)
- [Release receipt](universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml)

## หลักสำคัญ

> เราไม่ได้ทำให้ AI ทุกตัวมีความจำเดียวกัน แต่ทำให้ AI ทุกตัวกลับมาอ่านรัฐธรรมนูญและทะเบียนความจริงของ Project ชุดเดียวกัน

`UAAC.md` เป็น upstream navigation page เท่านั้น ไม่ใช่ Project Law, Authority หรือ runtime Current Truth ของ Project ที่ติดตั้งแล้ว
