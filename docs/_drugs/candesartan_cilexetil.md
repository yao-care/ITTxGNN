---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Candesartan Cilexetil: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker (ARB) established in the management of hypertension and heart failure, acting by selectively blocking AT1 receptors to reduce vasoconstriction driven by the renin-angiotensin-aldosterone system (RAAS).
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, a condition where intense RAAS activation plays a central pathophysiological role.
However, **no clinical trials and no directly relevant literature** are currently available for this specific drug–disease pair, placing this prediction at an early mechanistic inference stage (L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (ARB class; no Italy registration on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 (mechanistic inference only) |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Candesartan cilexetil is a prodrug that is hydrolyzed after oral absorption to its active form, candesartan — a selective, insurmountable antagonist of the angiotensin II type 1 (AT1) receptor. By blocking AT1, candesartan abolishes angiotensin II–mediated vasoconstriction, aldosterone secretion, and sympathetic activation, resulting in sustained blood pressure reduction and renal protection. Although detailed MOA data was not retrieved in this Evidence Pack, the drug's class mechanism is well-established in the pharmacological literature.

Malignant renovascular hypertension is a severe, rapidly progressive syndrome driven by renal artery stenosis triggering extreme RAAS activation. Angiotensin II concentrations surge, producing intense systemic and renal vasoconstriction, end-organ damage to the kidneys, retina, and brain. Because the ARB mechanism directly antagonizes the dominant pathophysiological driver of this condition, the TxGNN prediction has a mechanistically coherent rationale.

A critical safety concern, however, is intrinsic to this indication: **in patients with bilateral renal artery stenosis** — which is common in renovascular disease — ARB use can precipitate acute renal failure by removing the angiotensin II–dependent compensatory mechanism that maintains glomerular filtration pressure. This is not a reason to dismiss the prediction, but it is a mandatory screening prerequisite before any clinical evaluation. No candesartan-specific RCT or observational study exists for this indication; the mechanistic argument relies entirely on class-level ARB pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 3 literature:** The 20 PubMed records retrieved for the "pulmonary hypertension owing to lung disease and/or hypoxia" indication are general hypoxia physiology and pathology papers (covering neurodegenerative disease, cancer biology, and altitude medicine). None address candesartan or ARB class drugs in the context of pulmonary hypertension and do not constitute supportive clinical evidence for any predicted indication in this report.

---

## Italy Market Information

Candesartan cilexetil has **no registered marketing authorizations in Italy**. There is no approved product to reference for indication text, dosage form, or prescribing conditions.

---

## Safety Considerations

Please refer to the package insert for complete safety information.

Additionally, one mechanistic safety concern is directly relevant to the predicted indication and warrants explicit attention:

- **Bilateral renal artery stenosis (BAS)**: ARB use in patients with BAS can cause acute renal failure by abolishing angiotensin II–dependent efferent arteriolar tone, which is the compensatory mechanism maintaining GFR when afferent flow is compromised. BAS must be excluded before ARB therapy is considered in any renovascular hypertension setting.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically plausible — candesartan's AT1 blockade directly targets the RAAS hyperactivation that drives malignant renovascular hypertension — but there is a complete absence of supporting clinical trials or candesartan-specific literature, a mandatory safety screening requirement (ruling out bilateral renal artery stenosis), and no Italy market presence from which to leverage off-label use pathways.

**To proceed, the following is needed:**

- **Safety prerequisite**: Define a patient screening protocol to exclude bilateral renal artery stenosis before any clinical evaluation
- **Class-level evidence review**: Conduct a systematic review of ARB class data (losartan RENAAL, irbesartan IDNT, and other RCTs) in hypertensive nephropathy and renovascular disease to assess whether class-level extrapolation is defensible
- **Candesartan-specific data gap**: Search for any preclinical (animal model) studies of candesartan in renovascular or malignant hypertension models to determine whether there is species-level mechanistic evidence
- **MOA & safety data**: Retrieve full DrugBank entry and package insert to complete the pharmacokinetic, DDI, and contraindication profile
- **Regulatory pathway**: Given zero Italy authorizations, assess whether a Named Patient Program, compassionate use, or investigator-initiated trial would be the appropriate regulatory entry point
- **Secondary indications**: Rank 2 (malignant hypertensive renal disease, L4) shares the same ARB-RAAS mechanistic rationale and could be evaluated in parallel; Ranks 4–5 (multifactorial PH, Braddock syndrome) are assessed as Hold with insufficient mechanistic basis and should not be prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

