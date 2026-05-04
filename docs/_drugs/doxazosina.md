---
layout: default
title: Doxazosina
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Doxazosina
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

# Doxazosina: Drug Repurposing Evaluation — Insufficient Data to Complete Assessment

## One-Sentence Summary

Doxazosina (international INN: Doxazosin) is an alpha-1 adrenergic receptor blocker with established clinical use in hypertension and benign prostatic hyperplasia. The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, and no Italy market authorizations were found under the queried name. A full repurposing evaluation cannot be completed until prediction data, regulatory records, and safety information are retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack (general knowledge: hypertension, BPH) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — prediction data absent |
| Italy Market Status | Not found (0 authorizations under "DOXAZOSINA") |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacological knowledge, Doxazosina is a selective alpha-1 adrenergic receptor antagonist. Its efficacy in hypertension (via vascular smooth muscle relaxation) and benign prostatic hyperplasia (via relaxation of prostatic smooth muscle) has been well established clinically.

No TxGNN prediction output was present in the `predicted_indications` field of the Evidence Pack. As a result, it is not possible to evaluate whether the mechanism of action supports any specific new indication. This section will be fully populated once prediction data becomes available.

---

## Italy Market Information

No market authorization records were returned under the search term **"DOXAZOSINA"**. This is most likely a **name-matching issue**: the English INN is "Doxazosin" and the brand name widely used in Europe is **Cardura** (Pfizer). A re-query using the English INN or brand name against the AIFA database is expected to return active authorizations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | No records found | — | Re-query required with "Doxazosin" or "Cardura" |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack returned no TxGNN repurposing predictions, no Italy regulatory data, and no safety profile — the three core inputs required for a repurposing evaluation. Proceeding without these would result in an evidence-free recommendation.

**To proceed, the following is needed:**

- **Re-run TxGNN pipeline** using the correct English INN **"Doxazosin"** (expected DrugBank ID: DB00590) to obtain ranked repurposing candidate indications
- **Re-query AIFA / Italy regulatory database** using "Doxazosin" or brand name "Cardura" to retrieve active market authorization records and approved indications
- **Retrieve MOA from DrugBank** (DB00590) to populate mechanism-of-action analysis
- **Obtain AIFA package insert** for key warnings, contraindications, and special population precautions
- **Re-run DDI check** using standardized INN "Doxazosin" (current query returned no results under "DOXAZOSINA")
- **Confirm DrugBank ID** — the Evidence Pack lists `drugbank_id: null`; this must be resolved before any pipeline re-run
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

