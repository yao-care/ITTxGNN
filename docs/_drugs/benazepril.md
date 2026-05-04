---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 5
---

# Benazepril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to confirm context, then generating the report based on the Evidence Pack.

---

# BENAZEPRIL: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE (angiotensin-converting enzyme) inhibitor, established in clinical practice for the treatment of hypertension and heart failure via RAAS pathway blockade.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** with a score of **99.65%**,
however **no clinical trials** and **no direct publications** specific to this combination are currently available — and a well-known serious contraindication applies in bilateral renal artery stenosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (no formal Italy registration record found) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank source queried. Based on established pharmacological knowledge, Benazepril is an ACE inhibitor — it competitively inhibits angiotensin-converting enzyme, blocking the conversion of angiotensin I to angiotensin II. This suppresses vasoconstriction and aldosterone secretion, resulting in systemic blood pressure reduction and decreased cardiac afterload.

Malignant renovascular hypertension shares the RAAS pathway as its core driver: renal artery stenosis triggers renin hypersecretion, leading to runaway angiotensin II production and severe, treatment-resistant hypertension. Because benazepril directly targets the central effector of this cascade, the mechanistic rationale is coherent — and explains why TxGNN assigned a 99.65% repurposing score. The disease and the drug mechanism point at the same biological axis.

However, this apparent mechanistic alignment collapses under a critical safety constraint. In **bilateral renal artery stenosis** — a common anatomical variant in malignant renovascular hypertension — ACE inhibitors remove the angiotensin II–mediated efferent arteriolar tone that maintains glomerular filtration pressure. The consequence is an abrupt, severe drop in GFR and potentially irreversible acute kidney injury (AKI). This is a well-recognised, serious contraindication that fundamentally limits the clinical applicability of benazepril in this indication. It is not a theoretical risk; it is a documented clinical hazard.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Although formal safety data could not be retrieved from this pipeline run, the mechanistic analysis identifies a clinically critical concern — ACE inhibitors are contraindicated in bilateral renal artery stenosis due to risk of acute kidney injury. This should be confirmed against the full AIFA-approved labelling before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the theoretically compelling RAAS mechanistic link, there is zero clinical trial or literature evidence specifically supporting Benazepril in malignant renovascular hypertension, and a known life-threatening contraindication (AKI in bilateral renal artery stenosis) creates a blocking safety concern that cannot be resolved without further data.

**To proceed, the following is needed:**

- **Formal MOA documentation** — retrieve full DrugBank record (DB00542) to complete mechanistic analysis and enable similarity scoring
- **Safety profile completion** — obtain AIFA (Italy) package insert to document contraindications and warnings formally; bilateral renal artery stenosis contraindication must be explicitly evaluated
- **Patient subgroup stratification** — distinguish unilateral from bilateral RAS: ACE inhibitors may carry a more manageable benefit-risk profile in unilateral stenosis, which warrants a separate sub-analysis
- **Class-effect literature review** — search evidence on related ACE inhibitors (e.g., Ramipril, Enalapril) in malignant renovascular hypertension; class-level evidence could indirectly inform a benazepril repurposing case
- **Consider escalating Rank 2** — Malignant Hypertensive Renal Disease (same TxGNN score, L4, recommendation: Research Question) may represent a more tractable repurposing opportunity given available mechanistic support from the REIN trial with Ramipril; consider making this the primary research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

