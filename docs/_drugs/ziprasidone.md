---
layout: default
title: Ziprasidone
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Ziprasidone
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

# Ziprasidone: From Schizophrenia to Trichotillomania

## One-Sentence Summary

Ziprasidone is a second-generation (atypical) antipsychotic primarily used for schizophrenia and bipolar disorder, with dopamine D2 and serotonin 5-HT2A receptor antagonism as its core pharmacological profile.
The TxGNN model predicts it may be effective for **Trichotillomania** (hair-pulling disorder, an OCD-spectrum condition),
however **no clinical trials or published literature** currently support this specific repurposing direction — the evidence level is **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Bipolar disorder (known pharmacological use; no Italy license on record) |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on established pharmacological knowledge, ziprasidone is an atypical antipsychotic that acts primarily through dopamine D2 receptor antagonism and serotonin 5-HT2A antagonism, with additional partial agonism at 5-HT1A receptors and inhibition of norepinephrine/serotonin reuptake. Its efficacy in schizophrenia and bipolar mania has been confirmed through multiple Phase 3 randomised controlled trials.

Trichotillomania is classified within the obsessive-compulsive and related disorders (OCD spectrum) in DSM-5. Theoretically, D2 receptor antagonism may dampen compulsive repetitive behaviors by modulating dopaminergic reward and habit circuits — a pathway shared with other OCD-spectrum interventions. Additionally, the 5-HT2A antagonism component may contribute to impulse control through serotonergic modulation. Some antipsychotics have been explored as augmentation agents in OCD-spectrum disorders, providing indirect biological plausibility.

However, this mechanistic rationale is highly speculative for trichotillomania specifically. No ziprasidone-specific clinical trials or publications in this indication have been identified. The TxGNN prediction likely reflects graph-level structural proximity within the disease–drug knowledge network rather than direct clinical evidence. At this stage, the prediction should be treated as a hypothesis-generating signal only, not actionable clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Ziprasidone currently holds **no marketing authorizations in Italy**. No license records are available in this evidence pack.

> Note: Ziprasidone is marketed in other jurisdictions (e.g., as Geodon® in the United States, Zeldox® in Europe) for schizophrenia and acute bipolar mania. Italy-specific approval status should be verified directly with AIFA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key note: Ziprasidone carries a known class risk of **QTc interval prolongation**, which is a particular concern for use in populations not already monitored under a psychiatry framework. This should be a primary safety consideration in any future feasibility assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature support ziprasidone's use in trichotillomania. The mechanistic link is biologically plausible in principle but remains entirely speculative without preclinical or clinical validation. There is insufficient evidence to proceed beyond hypothesis generation at this time.

**To proceed, the following is needed:**
- Retrieve and review the full package insert (AIFA/EMA SmPC) to characterise key warnings, contraindications, and QTc-related risk
- Confirm detailed mechanism of action data via DrugBank API (DG002 remediation)
- Conduct a targeted literature search on antipsychotics and/or dopamine modulators in OCD-spectrum disorders, specifically trichotillomania
- Assess whether any exploratory or investigator-initiated trials exist in registries outside ClinicalTrials.gov (e.g., EU CTR, ISRCTN)
- If biological rationale is strengthened, consider preclinical proof-of-concept study planning before any clinical trial investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

