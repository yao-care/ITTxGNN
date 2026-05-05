---
layout: default
title: Cortisone
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 9
---

# Cortisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cortisone: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Cortisone (DB14681) is a steroid compound with no original indications recorded in the current Evidence Pack.
The TxGNN pipeline returned **no predicted new indications** for this candidate, and the drug is **not marketed in Italy**.
Without prediction output or regulatory history, a full repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions to evaluate |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological class, Cortisone belongs to the glucocorticoid (corticosteroid) family, but neither original indications nor MOA have been populated in the structured data fields.

No original indication is recorded in the `original_indications` field, and the TxGNN model returned an empty `predicted_indications` array. This may indicate that the candidate was filtered out prior to scoring, or that the knowledge graph lacked sufficient edges to generate a confident prediction.

Without mechanism data or model output, no mechanistic bridge between an original and a candidate new indication can be constructed at this stage.

---

## Italy Market Information

Cortisone has **no marketing authorizations** in Italy. No license records were returned from the regulatory query.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced no predicted indications for Cortisone, and critical data inputs — including mechanism of action and original indication text — are missing. Without a prediction target, repurposing evaluation cannot proceed.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain the package insert PDF from the official regulatory authority and parse key warnings and contraindications. This is a blocking gap that prevents safety pre-screening.
- **Resolve DG002 (High):** Query the DrugBank API to retrieve the structured mechanism of action (MOA) for DB14681. This is required for mechanistic plausibility analysis.
- **Investigate empty `predicted_indications`:** Confirm whether Cortisone was excluded from TxGNN scoring due to missing knowledge graph edges, or whether the model ran but produced no high-confidence predictions. If the former, supplement the KG with curated pharmacological data and re-run.
- **Populate `original_indications`:** Source original approved indications from DrugBank or WHO INN records and add to the Evidence Pack before re-evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

