---
layout: default
title: Dapagliflozin
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Dapagliflozin
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

# Dapagliflozin: Evidence Pack Incomplete — Repurposing Evaluation Pending

## One-Sentence Summary

Dapagliflozin (DrugBank DB06292) is an oral small-molecule drug with no original indications or TxGNN-predicted new indications recorded in the current Evidence Pack.
No repurposing candidates, clinical trial links, or mechanism of action data are available at this time, making a full evaluation impossible.
The recommended decision is **Hold** until critical data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction only (no actual predictions yet loaded) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed Yet

Three blocking conditions prevent a repurposing analysis from being written:

1. **No TxGNN predictions loaded.** The `predicted_indications` array is empty. Without at least one candidate indication, there is no disease target to analyze, no mechanistic bridge to draw, and no evidence table to populate.

2. **Mechanism of action (MOA) data is absent.** The `original_moa` field was not retrieved from DrugBank in this pipeline run. MOA is the foundation of any mechanistic justification — without it, any explanation of "why the prediction is reasonable" would be speculative.

3. **No original indications on record.** The `original_indications` array is empty, so the starting point of the repurposing story (what the drug was originally approved for) is also undefined in this pack.

These three gaps together mean the core narrative of the report — drug mechanism → original use → new use — cannot be constructed from available data.

---

## Taiwan Market Information

Dapagliflozin has **no approved licenses** in the Taiwan market as of the data cutoff (2026-04-20). No dosage forms, product names, or approved indications are on record in the TFDA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Dapagliflozin (DB06292) is structurally incomplete — no predicted indications, no MOA, and no safety data are present. Running an evaluation with fabricated or assumed content would misrepresent the drug's evidence status.

**To proceed, the following is needed:**

- **TxGNN predictions** — re-run the TxGNN pipeline for DB06292 and populate the `predicted_indications` array with at least one candidate indication, including score, clinical trials, and literature
- **Mechanism of action** — query DrugBank API for DB06292 and populate `original_moa` (classified as High-severity data gap DG002)
- **TFDA package insert** — parse the package insert PDF to extract key warnings and contraindications (classified as Blocking-severity data gap DG001)
- **Original indications** — populate `original_indications` from TFDA, DrugBank, or EMA/FDA public databases
- **Drug-drug interaction data** — the DDI query returned `not_found`; retry against an alternative DDI database or DrugBank interactions endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

