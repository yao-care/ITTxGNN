---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab (DB12159): No TxGNN Repurposing Predictions Available

## One-Sentence Summary

Dupilumab (Dupixent) is a biologic monoclonal antibody targeting the IL-4Rα receptor, used to treat type 2 inflammatory conditions including atopic dermatitis and asthma. The current Evidence Pack contains **no TxGNN repurposing predictions**, as critical input data — including mechanism of action, original indications, and safety information — were not successfully loaded. A meaningful repurposing evaluation cannot proceed until these data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Data not loaded (atopic dermatitis / type 2 inflammatory disease per public sources) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — model produced no output |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Data Gap Summary

The Evidence Pack was generated with only one confirmed input (`drugbank`), and two blocking gaps were flagged at creation time:

| Gap ID | Category | Missing Item | Severity | Impact |
|--------|----------|-------------|----------|--------|
| DG001 | Drug Level | Package insert warnings / contraindications | **Blocking** | Cannot proceed to safety pre-screening (S1) |
| DG002 | Drug Level | Mechanism of action (MOA) | High | Mechanistic relevance analysis unavailable |

Because `predicted_indications` is empty, all downstream sections (clinical trial evidence, literature evidence, mechanism analysis) cannot be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.
No drug-drug interaction data was found for Dupilumab in the queried sources.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned zero repurposing candidates for Dupilumab, most likely because the model's required inputs — including MOA graph embeddings and original indication labels — were absent from the Evidence Pack. No evidence review is possible without a valid prediction set.

**To proceed, the following is needed:**

- [ ] Re-run TxGNN prediction with complete drug node data (MOA, DrugBank categories, known indication labels)
- [ ] Load package insert (TFDA/EMA/FDA) to extract approved indications, warnings, and contraindications
- [ ] Confirm DrugBank MOA: Dupilumab is an IL-4Rα antagonist (blocks IL-4 and IL-13 signaling); this should be retrievable via DrugBank API (DB12159)
- [ ] Verify Italy (AIFA) / Taiwan (TFDA) marketing authorisation status — both currently show 0 licences, which may be a data retrieval issue rather than true non-approval
- [ ] Once predictions are available, re-generate Evidence Pack v5 and re-run this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

