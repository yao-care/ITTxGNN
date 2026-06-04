---
layout: default
title: Quinapril
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 5
---

# Quinapril
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

Using the `txgnn-pipeline` skill for context, and the **Drug Repurposing Evaluation Report v5** prompt, here is the full report for Quinapril:

---

# Quinapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Quinapril is an ACE inhibitor (ACEI) belonging to the renin-angiotensin-aldosterone system (RAAS) blocker class, classically used to treat hypertension and heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with a prediction score of 99.86%.
Currently, **no dedicated clinical trials** and **no direct publications** for this specific drug–disease pair were identified; the supporting rationale rests on mechanism-level class evidence for ACE inhibitors in hypertensive nephropathy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Heart Failure (ACE inhibitor class; no Italy authorization record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological class information, Quinapril is an ACE inhibitor that blocks the conversion of angiotensin I to angiotensin II — a potent vasoconstrictor that also stimulates aldosterone secretion and promotes renal fibrosis. By suppressing angiotensin II production, Quinapril dilates the efferent glomerular arteriole, reduces intraglomerular filtration pressure, and slows the progression of glomerulosclerosis and proteinuria. Bradykinin accumulation — a secondary consequence of ACE inhibition — further contributes to vasodilation via nitric oxide release.

Hypertensive renal disease and its malignant subtype both involve pronounced RAAS overactivation driving renal microangiopathy. For chronic hypertensive nephropathy, the ACEI class is supported by strong guideline-level class evidence. Malignant hypertensive renal disease is the acute, rapidly accelerating subtype characterized by severe blood pressure elevation, fibrinoid necrosis of renal arterioles, and acute kidney injury — a context where RAAS suppression is mechanistically well-motivated given the extreme renin-angiotensin activation seen in these patients.

However, an important clinical nuance must be flagged: malignant hypertensive renal disease frequently presents as a medical emergency. Quinapril, as a long-acting oral prodrug ACEI, has not been studied specifically in this acute-critical subtype via RCT. The TxGNN model plausibly captures the biological link between ACE inhibition and renal protection, but clinical applicability to the malignant subtype — including appropriate dosing, timing, and risk of acute blood pressure overcorrection — requires dedicated investigation before any repurposing recommendation can be made.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Quinapril holds no current marketing authorization in Italy and is not listed as a marketed product. No product license records are on file. A regulatory pathway assessment with AIFA would be required before any clinical application in Italy.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications data were not available in this evidence pack. Of particular clinical relevance for this indication, the known class-level contraindication of ACE inhibitors in bilateral renal artery stenosis must be evaluated before use in any renovascular hypertensive patient.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Quinapril in malignant hypertensive renal disease is conceptually coherent — RAAS suppression via ACE inhibition directly addresses the pathophysiology — but no quinapril-specific clinical trials or direct literature for this indication were identified, key safety data are missing, and the drug is not marketed in Italy, leaving the evidence base at L4 (mechanistic rationale only).

**To proceed, the following is needed:**

- **Literature search expansion**: Systematic review of ACEI use (as a class) in malignant hypertension with renal involvement — including observational cohort data, case series, and international nephrology guidelines
- **Package insert review**: Obtain and parse Quinapril's full prescribing information to document contraindications (especially bilateral renal artery stenosis, acute renal failure), warnings, and dosing guidance in renal impairment
- **MOA data**: Retrieve formal mechanism of action from DrugBank (DB00881) to support the mechanistic rationale section
- **Renovascular safety clarification**: Distinguish malignant hypertensive renal disease (primary RAAS overactivation — ACEI potentially appropriate) from malignant renovascular hypertension (stenosis-driven — ACEI potentially contraindicated, as flagged in predicted rank 2)
- **Nephrology expert consultation**: Validate clinical feasibility of an observational or prospective study design in this high-acuity patient population
- **AIFA regulatory pathway assessment**: Evaluate the route to authorization in Italy given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

