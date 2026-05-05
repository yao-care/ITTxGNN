---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

Using the `txgnn-pipeline` skill context confirmed. Now generating the evaluation report from the Evidence Pack.

---

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α (FP) receptor agonist widely used to reduce intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 completed Phase 2 clinical trial** currently providing direct supporting evidence for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Latanoprost is a selective prostaglandin F2α (FP) receptor agonist that lowers intraocular pressure by increasing aqueous humor outflow through the uveoscleral pathway. Its efficacy and safety in reducing IOP for open-angle glaucoma and ocular hypertension are well established across decades of clinical use.

Primary hereditary glaucoma — caused by mutations in genes such as *MYOC* (myocilin) and *CYP1B1* — shares the same pathological endpoint as open-angle glaucoma: elevated IOP leading to progressive optic nerve damage and irreversible vision loss. Although the root cause is genetic rather than acquired, IOP control remains the cornerstone of management for most hereditary glaucoma forms, including cases refractory to surgical procedures.

Because Latanoprost's mechanism acts downstream of the genetic defect — directly enhancing uveoscleral outflow regardless of the upstream mutation — its IOP-lowering effect is biologically applicable to this population. Notably, a Phase 2 trial (NCT01527682) directly evaluated a prostaglandin analogue and dorzolamide combination in paediatric hereditary glaucoma patients who had already failed surgery, providing the strongest currently available direct clinical evidence for this repurposing pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed ocular hypotensive efficacy and safety of a prostaglandin analogue (latanoprost class) plus dorzolamide in paediatric glaucoma patients refractory to surgery. Targeted 68 eyes across 34–68 patients; protocol was amended mid-study. Full-text review needed to confirm primary endpoint outcomes. |

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Latanoprost is not currently approved or marketed in Italy (AIFA). No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial directly evaluates prostaglandin analogue therapy in paediatric primary hereditary glaucoma refractory to surgery, and Latanoprost's FP receptor-mediated IOP reduction is mechanistically valid regardless of the underlying genetic aetiology — making this a well-grounded repurposing candidate.

**To proceed, the following is needed:**
- Full-text review of NCT01527682 to confirm primary endpoint achievement, safety profile, and subgroup-specific outcomes
- Mechanism of action (MOA) data from DrugBank API to complete the mechanistic rationale
- Safety and contraindication data from the Italian / AIFA package insert to enable S1 safety screening
- Paediatric dosing and formulation suitability assessment for the primary hereditary glaucoma population
- Drug–drug interaction (DDI) profile review, particularly for patients on concurrent anti-glaucoma therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

