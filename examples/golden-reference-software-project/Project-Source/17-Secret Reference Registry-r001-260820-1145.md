---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "SECRETS-001"
document_type: "SECRET_REFERENCE_REGISTRY"
semantic_slot: "17"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
synthetic_reference: true
---

# 17 — Secret Reference Registry

## SECRET-001 — Database Credential Reference

- **Secret Type:** DATABASE_PASSWORD
- **System / Environment:** Synthetic HarborDesk reference / deployment blueprint
- **External Storage Reference:** `secret://golden-reference/db-password`
- **Required Authority:** AUTH-001 permits documentation of the reference only; it does not grant access to any real credential
- **Status:** SYNTHETIC_REFERENCE_ONLY

```yaml
secret_value_present: false
```

No actual secret value exists in this Golden Reference.
