---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

Using `txgnn-pipeline` skill context confirmed. Now generating the Irbesartan repurposing evaluation report based on the Evidence Pack.

---

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II type-1 (AT1) receptor blocker (ARB), globally established for essential hypertension and renal protection in type 2 diabetic nephropathy.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** with a prediction score of 99.31%; however, **no dedicated clinical trials or publications** have been identified for this specific indication.
Critically, a well-known ARB class contraindication — acute renal failure risk in bilateral renal artery stenosis — directly overlaps with the most common aetiology of this predicted indication and substantially constrains the clinical hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Essential hypertension / Diabetic nephropathy (established ARB; no Italy authorization on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (DrugBank query pending). Based on established pharmacology, Irbesartan is a selective angiotensin II type-1 (AT1) receptor antagonist. By blocking AT1 receptors, it interrupts the renin-angiotensin-aldosterone system (RAAS): reducing vasoconstriction, lowering aldosterone-driven sodium retention, and — critically for the kidney — decreasing efferent arteriolar resistance and intraglomerular pressure, resulting in reduced proteinuria and slower nephrosclerosis.

The mechanistic fit with malignant renovascular hypertension is immediately apparent: the core pathophysiology follows the sequence renal artery stenosis → renal ischaemia → massive renin release → angiotensin II surge → AT1 receptor overactivation → runaway blood pressure with end-organ damage. Since Irbesartan sits precisely at the AT1 effector step, it targets the apex of this cascade. The TxGNN score of 99.31% most likely reflects the strong knowledge-graph connectivity between this disease and the hypertension/RAAS node cluster. An analogous, closely related indication — **malignant hypertensive renal disease (rank 2, same score)** — is supported by indirect Phase 3 evidence: the IDNT trial (Lewis EJ et al., *NEJM* 2001) demonstrated that Irbesartan significantly delays renal composite endpoints (HR 0.80, p = 0.02) in diabetic nephropathy, a condition sharing the same RAAS-driven nephrosclerosis and glomerular hypertension mechanism.

However, a **well-established class-level contraindication** must be foregrounded: patients with bilateral renal artery stenosis (or unilateral stenosis in a solitary kidney) depend on angiotensin II–maintained efferent arteriolar tone to preserve glomerular filtration pressure. ARB or ACE inhibitor use in this anatomical context can precipitate acute renal failure. Because bilateral renal artery stenosis is a leading cause of renovascular hypertension, this contraindication applies to a significant — possibly majority — subpopulation of patients in the predicted indication. The TxGNN model captures pharmacological plausibility at the pathway level but does not appear to have encoded this anatomical exception, which is the central caveat for this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Irbesartan holds **no marketing authorizations** in Italy according to the current regulatory dataset (AIFA query: 0 records). No approved product entries or indication texts are available for review. Irbesartan is, however, widely authorized in other jurisdictions (EU, US, Japan) as an ARB for hypertension and diabetic nephropathy — a discrepancy that may warrant a regulatory data refresh before drawing country-specific conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinician Alert (derived from repurposing rationale, not from safety data fields):** A critical class-level risk is documented for all ARBs: in bilateral renal artery stenosis or solitary kidney, AT1 blockade removes the angiotensin II–dependent support of glomerular filtration pressure and may precipitate **acute renal failure**. This risk is directly and specifically relevant to the primary predicted indication (malignant renovascular hypertension) and constitutes a prerequisite safety assessment before any clinical investigation is designed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No dedicated clinical trials or publications support Irbesartan specifically in malignant renovascular hypertension, and the single most important anatomical subtype of this disease (bilateral renal artery stenosis) represents a known ARB contraindication — meaning the prediction, while mechanistically logical at the pathway level, is clinically high-risk without patient stratification. The closely related rank-2 indication (malignant hypertensive renal disease) carries a stronger evidence base (L3; IDNT trial indirect support; recommendation: Proceed with Guardrails) and may be a more viable near-term repurposing target.

**To proceed, the following is needed:**

- **Patient stratification data**: proportion of malignant renovascular hypertension cases with unilateral vs. bilateral renal artery stenosis, to define the subset where ARB use is safe and potentially beneficial
- **Formal MOA documentation**: DrugBank API query (DG002 pending) to confirm receptor binding profile, selectivity, and pharmacokinetics
- **Italy SPC (Summary of Product Characteristics) review**: AIFA package insert warnings and contraindications (DG001 Blocking gap) required before any safety-level assessment can be completed
- **Retrospective cohort evidence**: a search for real-world or registry data on ARB use outcomes specifically in unilateral renovascular hypertension as proof-of-concept before trial design
- **Reconsideration of rank-2 indication** (malignant hypertensive renal disease) as the primary repurposing target, given its mechanistic overlap with the IDNT trial and a more actionable evidence-to-risk profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

