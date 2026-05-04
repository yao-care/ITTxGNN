---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Donepezil: Evidence Pack Incomplete — TxGNN Repurposing Analysis Pending

## One-Sentence Summary

Donepezil (DrugBank: DB00843) has been retrieved from DrugBank, but this Evidence Pack contains **no TxGNN predicted indications**, no original indication records, and no safety data.
A repurposing evaluation cannot be completed at this stage; the recommended action is to resolve the identified data gaps before proceeding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No TxGNN predictions returned |
| TxGNN Prediction Score | — |
| Evidence Level | Not assessable |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The TFDA package insert query returned a result (query log ID 4, status: success), but the safety fields in this Evidence Pack have not yet been populated. A follow-up extraction step is needed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Donepezil is missing three critical components — TxGNN predicted indications, original indication records, and safety data — making it impossible to assess repurposing potential or risk profile at this time.

**To proceed, the following is needed:**

- **[Blocking] Resolve DG001 — TFDA Package Insert Safety Data**
  The TFDA package insert query succeeded but safety fields remain empty. Parse the retrieved PDF to populate key warnings, contraindications, and dosing precautions.

- **[High] Resolve DG002 — Mechanism of Action (MOA)**
  Query DrugBank API for DB00843 to retrieve pharmacological action, target proteins, and therapeutic category. This is essential for mechanistic plausibility analysis of any predicted indication.

- **[Critical] Re-run TxGNN Prediction Pipeline**
  `predicted_indications` is empty. Verify whether the model run completed successfully for DB00843, check for mapping errors between DrugBank ID and the KG node, and re-execute if necessary.

- **[Required] Populate Original Indications**
  `original_indications` is empty despite a successful DrugBank query. Confirm whether the extraction step parsed approved indications correctly and re-populate this field.

- Once the above data gaps are resolved, resubmit this Evidence Pack for a full v5 evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

