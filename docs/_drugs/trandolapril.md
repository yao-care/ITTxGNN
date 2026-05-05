---
layout: default
title: Trandolapril
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 6
---

# Trandolapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

---

# Trandolapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Trandolapril is an ACE (angiotensin-converting enzyme) inhibitor established for the treatment of hypertension and left ventricular dysfunction following myocardial infarction. The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, with **0 clinical trials** and **0 publications** directly supporting this direction. Critically, the drug's core mechanism raises a fundamental safety paradox for this indication — ACE inhibitors are contraindicated in bilateral renal artery stenosis, the most common etiology of renovascular hypertension, making immediate clinical advancement inappropriate without further safety profiling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and post-MI left ventricular dysfunction (no Italy authorization record in this dataset) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Trandolapril belongs to the ACE inhibitor class — it works by blocking the enzyme that converts angiotensin I to angiotensin II, thereby reducing vasoconstriction, lowering aldosterone secretion, and decreasing both systemic vascular resistance and blood pressure. These properties underpin its proven efficacy in essential hypertension and post-MI cardiac remodeling.

The biological logic connecting Trandolapril to **malignant renovascular hypertension** runs directly through the renin-angiotensin-aldosterone system (RAAS). In renovascular disease, renal artery stenosis triggers excessive renin release, driving angiotensin II–mediated vasoconstriction and severe, often refractory hypertension. ACE inhibition can, in principle, interrupt this pathological cascade at the source — which explains why the TxGNN knowledge-graph model assigns an extremely high prediction score (99.92%).

However, the same mechanism creates a critical clinical paradox. In **bilateral** renal artery stenosis — the most common cause of renovascular hypertension — glomerular filtration pressure is maintained almost entirely by angiotensin II–mediated efferent arteriolar constriction. Removing that compensatory support with an ACE inhibitor risks precipitous loss of renal perfusion and acute kidney failure. This is a well-recognized clinical contraindication. TxGNN's high score likely reflects network-level proximity between RAAS modulation and renovascular pathology, but the model does not encode this contraindication. Any clinical exploration of this prediction must be restricted to a carefully defined subpopulation — for example, unilateral RAS with a confirmed normal contralateral kidney — and requires mandatory nephrology review before proceeding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Trandolapril in malignant renovascular hypertension.

---

## Literature Evidence

Currently no related literature available for Trandolapril in malignant renovascular hypertension.

---

## Italy Market Information

Trandolapril currently holds **no marketing authorizations** in Italy. No licensed products or approved indications are recorded in this dataset.

> **Note:** The query log confirms a successful AIFA database lookup was performed (2026-03-29) with zero results. Trandolapril is available under brand names such as Gopten in other European markets; the lack of Italy authorization should be independently verified via the official AIFA registry before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important mechanistic warning:** Although formal safety records were not retrievable for this dataset, the repurposing rationale analysis identifies a clinically significant concern independent of the package insert: ACE inhibitors as a class — including Trandolapril — can precipitate acute renal failure in patients with bilateral renal artery stenosis or stenosis of a solitary functioning kidney. Since this anatomy is the predominant driver of renovascular hypertension, any prescribing decision in this indication requires prior renal vascular imaging and specialist assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (malignant renovascular hypertension, 99.92%) carries zero supporting clinical trials and zero published literature, and the mechanistic analysis reveals a probable contraindication in the most common clinical presentation of the disease — not a repurposing opportunity. Proceeding to clinical evaluation without first resolving this safety paradox and defining a safe patient subgroup would be inappropriate.

**To proceed, the following is needed:**

- **Retrieve the full EMA/AIFA SmPC** for Trandolapril to formally document contraindications, warnings, and renal monitoring requirements
- **Define the eligible patient subpopulation:** unilateral RAS with confirmed normal contralateral kidney function, where ACE inhibition is mechanistically safer
- **Broaden the literature search** from Trandolapril-specific queries to ACE inhibitors as a class in renovascular hypertension, to establish the existing evidence base
- **Evaluate alternative predicted indications** with more favorable benefit-risk profiles as potential earlier development priorities:
  - **Chronic pulmonary heart disease** (Rank 6, Evidence Level L4) — supported by an animal study ([PMID 8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/)) showing long-term Trandolapril treatment attenuates augmented vasoconstriction in rats with chronic heart failure; mechanistic rationale via RAAS-mediated right ventricular remodeling is plausible
  - **Pulmonary hypertension owing to lung disease/hypoxia** (Rank 4, Evidence Level L5) — Group 3 pulmonary hypertension presents lower systemic blood pressure concerns than Group 1 PAH, making ACE inhibition mechanistically safer to explore; elevated angiotensin II under hypoxia provides a biological entry point
- **Confirm Italy market status** via direct AIFA registry lookup, as commercial availability in neighboring EU markets (e.g., Gopten in Germany/UK) may affect regulatory pathway planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

