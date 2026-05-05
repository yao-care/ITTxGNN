---
layout: default
title: Fosinopril
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

Using the `txgnn-pipeline` skill to guide report generation. Now producing the evaluation report based on the Evidence Pack.

---

# Fosinopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Fosinopril is an ACE inhibitor (angiotensin-converting enzyme inhibitor) classically used in the management of hypertension and heart failure. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **no clinical trials** and **no direct supporting publications** currently found for this specific indication. The entire evidence base rests at Level L5 — model prediction only — and a critical safety concern with this mechanism in renovascular disease warrants a Hold decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Heart failure (ACE inhibitor class; no Italy regulatory records on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacology, Fosinopril is a phosphinic acid-class ACE inhibitor. It blocks the conversion of Angiotensin I to Angiotensin II, reducing systemic vascular resistance and lowering blood pressure. Its efficacy in treating essential hypertension and reducing cardiovascular risk in heart failure patients is well established across multiple therapeutic guidelines.

Malignant renovascular hypertension is a severe, potentially life-threatening form of secondary hypertension driven by critical renal artery stenosis. The renin-angiotensin-aldosterone system (RAAS) is pathologically overactivated in this condition, which is precisely the pathway fosinopril targets — making the TxGNN prediction mechanistically plausible on its surface. The model likely identified this RAAS overlap as a strong signal.

However, a well-recognised danger exists: in renovascular disease, Angiotensin II-driven efferent arteriolar vasoconstriction is the *compensatory mechanism* the ischemic kidney depends upon to maintain glomerular filtration pressure. ACE inhibition removes this compensatory support, potentially precipitating acute kidney injury or complete loss of renal function in the affected kidney. This bidirectional mechanistic profile — antihypertensive benefit on one hand, risk of precipitating renal failure on the other — is a known clinical caution for ACE inhibitors as a class in this specific disease context, and significantly limits the repurposing potential of this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note:** A PubMed search for Fosinopril in this indication returned 0 results. A separate search for the rank-3 indication (pulmonary hypertension owing to lung disease/hypoxia) retrieved 20 publications, but these address general hypoxia biology and are not specific to fosinopril's role in this disease — their relevance is unconfirmed and they are not presented here.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, drug interactions) was not retrievable from the current data sources. For clinical use evaluation, the package insert and a drug interaction database query with a complete patient medication list are essential prerequisites.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.87%), the supporting evidence is entirely at Level L5 with no clinical trials or direct literature — and more critically, Fosinopril's ACE inhibitor mechanism is a well-recognised class-level hazard in renovascular disease, where inhibiting Angiotensin II can precipitate acute kidney failure rather than providing benefit.

**To proceed, the following is needed:**

- **MOA data from DrugBank** (DG002 remediation) to formally document the mechanistic link and contraindication profile
- **Package insert review** (DG001 remediation): formal contraindication text for bilateral renal artery stenosis / renovascular disease must be confirmed before any further evaluation
- **Renal function risk stratification**: a safety framework distinguishing unilateral vs. bilateral renovascular disease, where the risk-benefit profile differs substantially
- **Literature search broadening**: expand search to ACE inhibitors as a class (not fosinopril-specific) in malignant hypertension with renovascular etiology
- **Clinical expert consultation**: nephrology or hypertension specialist review of whether this TxGNN prediction represents a genuine repurposing opportunity or a contraindicated use being surfaced by the model's RAAS-pathway signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

