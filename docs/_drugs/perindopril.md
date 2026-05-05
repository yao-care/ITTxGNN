---
layout: default
title: Perindopril
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 5
---

# Perindopril
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

---

# Perindopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Perindopril is a well-established ACE (Angiotensin-Converting Enzyme) inhibitor, widely used for the treatment of hypertension and chronic heart failure. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, a severe, RAAS-driven hypertensive emergency. Currently, **0 clinical trials** and **0 directly relevant publications** support this specific repurposing direction, placing the evidence at a model-prediction-only level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, chronic heart failure (ACE inhibitor class) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Perindopril belongs to the ACE inhibitor class, which exerts its primary effect by blocking the conversion of Angiotensin I to Angiotensin II within the Renin-Angiotensin-Aldosterone System (RAAS). The result is reduced vasoconstriction, lower aldosterone secretion, and decreased blood pressure. Detailed MOA data from DrugBank was not retrieved in this pipeline run, but the class-level mechanism is well established in clinical pharmacology.

Malignant renovascular hypertension is a hypertensive emergency most commonly caused by renal artery stenosis, which triggers a runaway activation of the RAAS — circulating Angiotensin II levels rise dramatically, driving the extreme blood pressure elevation that defines the condition. Because ACE inhibitors act directly upstream of this cascade by blocking Ang II production, the TxGNN model's high-scoring prediction is mechanistically coherent: targeting the primary driver of pathological vasoconstriction is a logical therapeutic approach.

However, a well-documented clinical paradox significantly complicates this prediction. In patients with bilateral renal artery stenosis — or stenosis of a functionally solitary kidney — ACE inhibitors can precipitate acute renal failure. This occurs because, when renal perfusion pressure is already critically reduced by the stenosis, glomerular filtration is maintained only by Angiotensin II-mediated constriction of the efferent arteriole. Removing that constriction with an ACE inhibitor collapses the filtration gradient. This is a class-level, mechanism-inherent safety concern directly relevant to the predicted indication, and must be addressed before any progression beyond Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Perindopril in malignant renovascular hypertension.

---

## Literature Evidence

Currently no related literature available directly evaluating Perindopril in malignant renovascular hypertension.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on the TxGNN model (L5), with zero supporting clinical trials or directly relevant publications for this indication; furthermore, the predicted disease context — renovascular hypertension associated with renal artery stenosis — represents a well-known high-risk setting for the ACE inhibitor class, where use can paradoxically precipitate acute renal failure, making clinical progression without additional safety data unjustifiable.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve complete DrugBank record for Perindopril to document RAAS pathway details and known class-level contraindications formally
- **Safety data gap resolution**: Obtain and parse the AIFA package insert (DG001 — currently Blocking severity) to confirm contraindication language regarding renal artery stenosis
- **Targeted literature search**: Commission a systematic review specifically on ACE inhibitor use in renovascular hypertension (including case series and observational cohort studies) to establish whether any subpopulation — e.g., unilateral stenosis with a contralateral normal kidney — may benefit safely
- **Patient stratification framework**: Define eligibility criteria to identify cases where the risk of renal function deterioration is manageable (e.g., functional imaging to exclude bilateral stenosis prior to any trial)
- **Preclinical bridging data**: If a viable patient subgroup is identified, a prospective pilot safety study with intensive renal function monitoring (serum creatinine, eGFR, potassium) should be designed before any Phase 2 consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

