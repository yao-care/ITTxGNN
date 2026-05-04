---
layout: default
title: Desloratadina
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 0
---

# Desloratadina
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Desloratadina: Evidence Pack Incomplete — No Repurposing Prediction Available

## Summary

Desloratadina (Desloratadine) is a second-generation antihistamine widely used for allergic rhinitis and chronic urticaria.
This Evidence Pack contains **no TxGNN predicted indications**, which means a drug repurposing evaluation cannot be completed at this stage.
Additionally, the drug is **not currently marketed in Italy** under this INN, and key safety and MOA data are absent from the pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, chronic urticaria (general knowledge; not populated in Evidence Pack) |
| Predicted New Indication | Not available — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Report Cannot Be Completed

The Evidence Pack for Desloratadina is missing three critical components:

**1. No TxGNN predictions were returned.**
The `predicted_indications` array is empty. Without at least one predicted indication, there is no repurposing candidate to evaluate. This may indicate the drug was not found in the TxGNN knowledge graph, or the prediction pipeline did not run to completion.

**2. Mechanism of action data is absent.**
The `original_moa` field is marked as a data gap (severity: High). Desloratadine is known to be a selective peripheral histamine H₁-receptor antagonist — but this was not retrieved into the Evidence Pack. The DrugBank query returned one result (`result_count: 1`), yet the data was not populated, suggesting a pipeline extraction error.

**3. Safety data is unavailable.**
Both key warnings and contraindications returned `[Data Gap]`. The TFDA package insert query also returned one result (`result_count: 1`) but was not parsed into the pack.

---

## Italy Market Information

No Italian authorizations were found for **DESLORATADINA** under this exact INN.

> **Note:** Desloratadine-containing products may be marketed under brand names (e.g., Aerius, Neoclarityn) with different INN spellings or combination formulations. A search under "desloratadine" (English spelling) is recommended.

---

## Safety Considerations

Safety data was not successfully extracted into this Evidence Pack. Please refer to the EMA product information and the package insert for Desloratadine for current warnings, contraindications, and drug interactions.

The DDI query returned no interactions (`query_status: not_found`), which may reflect a search term mismatch rather than a true absence of known interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no predicted indications exist and critical drug-level data (MOA, safety) was not extracted despite successful upstream queries. A repurposing evaluation cannot be responsibly written without at least one TxGNN prediction to anchor the analysis.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** using the correct DrugBank identifier for Desloratadine (DB00967) to generate predicted indications
- **Extract DrugBank data** — the DrugBank query returned 1 result; confirm the extraction step did not silently fail, and populate `original_moa`, `drugbank_id`, and `categories`
- **Parse TFDA / EMA package insert** — the insert query returned 1 result; extract warnings, contraindications, and approved indications into the Evidence Pack
- **Verify INN spelling** — queries used `DESLORATADINA` (Italian/Spanish INN); confirm the TxGNN knowledge graph uses the same identifier, or remap to `desloratadine` (English INN / DrugBank standard)
- **Re-query Italy authorizations** under alternate spellings or brand names to confirm true market absence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

