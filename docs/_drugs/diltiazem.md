---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diltiazem: Repurposing Evaluation — Insufficient Data to Complete Assessment

## One-Sentence Summary

Diltiazem (DrugBank: DB00343) is a cardiovascular calcium channel blocker with established clinical use globally.
This Evidence Pack contains **no TxGNN predicted indications**, making a standard drug repurposing evaluation impossible at this stage.
Two data gaps of **Blocking / High severity** must be resolved before the evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | — |
| Evidence Level | Not evaluable (prediction not yet generated) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

This Evidence Pack is missing three critical elements that are prerequisites for a drug repurposing evaluation:

**1. No TxGNN predictions (`predicted_indications` is empty)**
The core output of the repurposing pipeline — the disease prediction list — is absent from this pack. Without a predicted indication target, there is no basis for clinical, mechanistic, or evidence review. This is the most fundamental gap.

**2. Mechanism of action (MOA) unavailable**
The DrugBank query returned a record (query log ID 3, status: success), but MOA data was not populated in the pack. Mechanistic plausibility analysis — the primary justification for repurposing — cannot be performed without this.

**3. Original indication data not extracted**
The `original_indications` field is empty. While the TFDA package insert query returned a result (query log ID 4, status: success), its contents were not parsed into the pack. Baseline disease characterization is therefore incomplete.

Until these gaps are resolved, the following report sections cannot be generated:
- Clinical Trial Evidence
- Literature Evidence
- Mechanism Rationale
- Cytotoxicity Assessment

---

## Taiwan Market Information

Diltiazem has **0 approved authorizations** in the TFDA database and is classified as **not marketed** in Taiwan. No product listing is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Diltiazem (DB00343) is structurally incomplete — the TxGNN prediction output is absent and two upstream data gaps (Blocking + High severity) have not been remediated. No repurposing evaluation can be generated under these conditions.

**To proceed, the following is needed:**

- **[Blocking]** Run TxGNN prediction pipeline for Diltiazem to generate `predicted_indications` — this is the prerequisite for the entire evaluation
- **[Blocking]** Parse the TFDA package insert PDF already retrieved (query log ID 4) to populate `original_indications`, `key_warnings`, and `contraindications`
- **[High]** Query DrugBank API (DB00343) to retrieve MOA, drug categories, and toxicity data
- **[Medium]** Re-run evidence collection (ClinicalTrials.gov + PubMed) for the predicted indication once TxGNN output is available
- **[Low]** Confirm whether DDI data should be sourced from an alternative database, as the current DDI query returned `not_found`
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

