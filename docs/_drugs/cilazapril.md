---
layout: default
title: Cilazapril
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cilazapril: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Cilazapril is an angiotensin-converting enzyme inhibitor (ACEI) belonging to the RAAS-blocking drug class, primarily established for the treatment of hypertension.
The TxGNN model predicts it may have potential in **Pulmonary Hypertension with Unclear Multifactorial Mechanism (Group 5 PH)**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction — placing it at the model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (ACEI class; no Italy market authorization on record) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism (Group 5 PH) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved for this Evidence Pack. Based on established pharmacological knowledge, cilazapril is a prodrug ACE inhibitor that is hydrolysed in vivo to its active form, cilazaprilat. It blocks the conversion of angiotensin I to angiotensin II, thereby reducing RAAS-mediated vasoconstriction, aldosterone secretion, and vascular remodelling. The broader ACEI class (captopril, ramipril, lisinopril) holds strong Phase 3 RCT support across hypertension, heart failure, and hypertensive nephropathy — providing a solid mechanistic foundation from which TxGNN can draw its prediction.

The model's reasoning for Group 5 PH is theoretically plausible: angiotensin II promotes endothelin-1 (ET-1) upregulation and direct pulmonary vasoconstriction, while ACEI-related bradykinin accumulation can facilitate nitric oxide (NO) release — both pathways are known to influence pulmonary vascular tone. Additionally, RAAS overactivation has been documented in certain systemic conditions that underlie Group 5 PH (e.g., chronic kidney disease, haematological disorders), offering a secondary mechanistic link.

However, the clinical case remains weak. Group 5 PH is defined by its heterogeneous and multifactorial aetiology — encompassing haematological, metabolic, and systemic disorders — making it highly unlikely that RAAS blockade alone can address the core pathology. Current **ESC/ERS 2022 pulmonary hypertension guidelines explicitly do not recommend ACEIs as targeted PAH therapy for Group 5 PH**, and no clinical evidence specific to cilazapril in this setting has been identified. This prediction should therefore be treated as a hypothesis-generating signal only, not a clinical candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported exclusively by TxGNN model scoring (L5 — no clinical trials, no publications), and the mechanistic rationale for ACEI use in this aetiologically heterogeneous PH subtype is not endorsed by current clinical guidelines. No Italy market authorization exists to provide a regulatory foundation for further development.

**To proceed, the following is needed:**

- Retrieve full MOA data from DrugBank (DB01340) to enable formal mechanistic analysis
- Conduct a systematic literature search for ACEI class-effect signals in Group 5 PH specifically (distinct from other PH groups)
- Review ESC/ERS 2022 PH guidelines for any RAAS-targeted signals in relevant Group 5 sub-conditions (e.g., CKD-associated PH, haematological PH)
- Obtain and review the full prescribing information / package insert for cilazapril to assess key warnings and contraindications
- Evaluate whether a lower-ranked indication with stronger mechanistic grounding (e.g., **malignant hypertensive renal disease**, Rank 3, L4) represents a more actionable repurposing candidate for prioritisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

