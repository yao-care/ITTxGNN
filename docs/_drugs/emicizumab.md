---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Emicizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Emicizumab: Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Emicizumab (DB13923) is a bispecific antibody recognized internationally for hemophilia A prophylaxis, but this Evidence Pack contains **no TxGNN-predicted indications** and critical data gaps across mechanism of action, safety warnings, and regulatory filings.
Without predicted indications, a standard repurposing pathway evaluation cannot be completed at this time.
The recommended decision is **Hold** pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (model pipeline produced no output) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Evaluation Cannot Proceed

The Evidence Pack for Emicizumab has three compounding data gaps that block standard evaluation:

**1. No TxGNN predicted indications.** The `predicted_indications` array is empty, meaning the knowledge-graph / deep-learning pipeline did not return any repurposing candidates for this drug. This may occur when the drug's node representation in the TxGNN knowledge graph is incomplete or when it was not included in the training entity set. Without at least one predicted indication, the core repurposing hypothesis does not exist.

**2. Mechanism of action unavailable.** The MOA field is missing, which prevents the mechanistic plausibility analysis that anchors every repurposing argument. Emicizumab is publicly known to be an anti-factor IXa/Xa bispecific antibody, but this must be confirmed from a structured data source (DrugBank API) before it can be cited in a formal evaluation.

**3. No regulatory filings in Taiwan.** With zero TFDA licenses and no package insert data retrieved, the local safety baseline (warnings, contraindications, dosing) is absent. The DDI query also returned no results.

---

## Taiwan Market Information

No TFDA authorizations found. Emicizumab has not been registered in Taiwan as of the data cut-off date (2026-04-20).

---

## Safety Considerations

Please refer to the package insert and internationally approved labeling (FDA/EMA) for safety information, as no Taiwan-specific safety data was available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline generated zero repurposing predictions for Emicizumab, and the two blocking data gaps (MOA and safety warnings) prevent even a preliminary feasibility assessment. There is no actionable repurposing hypothesis to evaluate at this stage.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve TFDA package insert PDF and extract warnings and contraindications, enabling S1 safety screening.
- **[DG002 — High]** Query DrugBank API for Emicizumab (DB13923) to obtain structured MOA, pharmacology, and toxicity data.
- **Re-run TxGNN pipeline** after confirming that Emicizumab's knowledge graph node (entities, edges, drug–gene–disease links) is fully populated; then re-generate `predicted_indications`.
- Once predictions are available, re-issue this Evidence Pack with `predicted_indications[0]` populated to trigger a full L1–L5 evidence review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

