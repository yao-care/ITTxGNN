---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a catechol-O-methyltransferase (COMT) inhibitor, clinically established as an adjunct to levodopa/carbidopa therapy in adults with Parkinson's disease experiencing "off" episodes.
The TxGNN model predicts it may be effective for **PLA2G6-Associated Neurodegeneration (PLAN)**, a rare iron-accumulation neurodegenerative disorder presenting with Parkinson-like features.
Currently, **no clinical trials** and **no published literature** support this specific repurposing direction — this remains a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's Disease (adjunct to levodopa, for "off" period management) |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration (PLAN) |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, entacapone is a selective, reversible peripheral COMT inhibitor. By blocking the enzymatic breakdown of levodopa in the bloodstream, it increases the fraction of each levodopa dose that crosses the blood-brain barrier and is converted to dopamine in the nigrostriatal pathway. In Parkinson's disease, this extends the duration of levodopa's therapeutic effect and reduces motor fluctuations ("wearing-off").

PLA2G6-Associated Neurodegeneration (PLAN) is caused by loss-of-function mutations in the *PLA2G6* gene encoding phospholipase A2, a subtype of Neurodegeneration with Brain Iron Accumulation (NBIA). A clinically significant subset of PLAN patients — particularly those with the adult-onset atypical Parkinson phenotype — exhibit nigrostriatal dopaminergic degeneration that is phenotypically indistinguishable from idiopathic Parkinson's disease. This shared neuroanatomical vulnerability is the most plausible basis for the TxGNN prediction.

However, phenotypic similarity does not equal therapeutic equivalence. The dopaminergic deficit in PLAN arises from a fundamentally different upstream cause (phospholipid membrane dysregulation and iron toxicity) rather than aggregated α-synuclein pathology. Whether PLAN patients' motor symptoms are levodopa-responsive — a prerequisite for COMT inhibition to add any benefit — is inconsistent in published case reports. The TxGNN score most likely reflects graph-proximity clustering between PLAN and classic Parkinson nodes, not direct mechanistic evidence. At present, this connection is purely hypothetical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for entacapone in PLA2G6-associated neurodegeneration.

---

## Literature Evidence

Currently no related literature available for entacapone in PLA2G6-associated neurodegeneration.

---

## Italy Market Information

Entacapone has no approved marketing authorizations in Italy and is not currently available on the Italian market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.76%), this score reflects phenotypic overlap in the knowledge graph between PLAN and Parkinson's disease — not actual therapeutic evidence. There is zero clinical, observational, or preclinical data specifically evaluating entacapone in PLAN, and the mechanistic link is indirect at best.

**To proceed, the following is needed:**

- **MOA data**: Retrieve complete mechanism of action from DrugBank API (currently missing; blocks mechanistic plausibility analysis)
- **Safety data**: Obtain EMA/AIFA-approved package insert to assess contraindications and key warnings before any further evaluation
- **Levodopa responsiveness data in PLAN**: Systematic review of published PLAN case reports to determine what proportion of adult-onset phenotype patients respond to levodopa — this is the prerequisite gate for COMT inhibition to be clinically relevant
- **Preclinical signal**: Identify any in vitro or animal model studies using COMT inhibition in NBIA/PLA2G6 knockout models
- **Expert consultation**: Neurologist specializing in rare movement disorders to assess clinical plausibility before resource investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

