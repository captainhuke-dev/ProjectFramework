# Universal AI Agent Constitution (UAAC) 5.0

หน้านี้เป็น repository navigation สำหรับ UAAC เท่านั้น ไม่ใช่ Project Law, runtime state หรือ Current Truth ของ Project ที่ติดตั้งแล้ว

## ติดตั้ง UAAC

เริ่มจาก:

1. [`universal-ai-agent-constitution/README.md`](universal-ai-agent-constitution/README.md)
2. [`universal-ai-agent-constitution/INSTALL-UAAC.md`](universal-ai-agent-constitution/INSTALL-UAAC.md)
3. [`universal-ai-agent-constitution/UAAC-v5.0-CONSTITUTION.md`](universal-ai-agent-constitution/UAAC-v5.0-CONSTITUTION.md)

เส้นทางปกติใน Project คือ:

```text
persistent launcher
→ governance/UAAC.md
→ governance/UAAC-ADOPTION.yaml
→ local pinned Constitution
→ bounded materially required Project sources
→ work
```

Project rules เป็น conditional: ใช้ source จริงที่มีอยู่แล้ว หรือสร้างเมื่อมี rule จริงเท่านั้น ห้ามสร้างไฟล์เปล่าเพื่อให้ครบโครงสร้าง

```text
Install UAAC != install or upgrade ProjectFramework
```

## Production และกฎหมาย

- Package: [`universal-ai-agent-constitution/`](universal-ai-agent-constitution/)
- Constitution: [`universal-ai-agent-constitution/UAAC-v5.0-CONSTITUTION.md`](universal-ai-agent-constitution/UAAC-v5.0-CONSTITUTION.md)
- Laws: [`universal-ai-agent-constitution/laws/`](universal-ai-agent-constitution/laws/)
- Release metadata: [`universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml`](universal-ai-agent-constitution/CONSTITUTION-RELEASE.yaml)

Operational constitutional law อยู่ใน `laws/CONST-001.md` ถึง `CONST-025.md` เท่านั้น

## Adoption และ migration

- Adoption guide: [`universal-ai-agent-constitution/ADOPTION-GUIDE.md`](universal-ai-agent-constitution/ADOPTION-GUIDE.md)
- Templates: [`universal-ai-agent-constitution/templates/`](universal-ai-agent-constitution/templates/)
- Migration/rollback: [`universal-ai-agent-constitution/MIGRATION-v4.2-TO-v5.0.md`](universal-ai-agent-constitution/MIGRATION-v4.2-TO-v5.0.md)
- Human walkthrough: [`HUMAN-INSTALL-WALKTHROUGH-TH.md`](HUMAN-INSTALL-WALKTHROUGH-TH.md)

## Optional profiles

[`universal-ai-agent-constitution/profiles/`](universal-ai-agent-constitution/profiles/) เป็น non-normative และต้อง opt in ผ่าน adoption อย่างชัดเจน การมีไฟล์อยู่ไม่ถือว่า activate และไม่สร้าง authority

## Developer conformance

[`uaac-conformance/`](uaac-conformance/) เป็น developer-only, non-normative และไม่ใช่ dependency ของการใช้งาน UAAC Core

## Historical UAAC 4.2

- Reconstruction: [`docs/uaac-history/v4.2/`](docs/uaac-history/v4.2/)
- Reference fixture: [`uaac-v4.2-reference-project/`](uaac-v4.2-reference-project/)

ใช้ immutable commit/tree ที่บันทึกไว้ใน historical inventory ห้ามใช้ current v5 package แทน bytes ของ v4.2
