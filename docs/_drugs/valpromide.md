---
layout: default
title: Valpromide
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 1
---

# Valpromide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

The txgnn-pipeline skill is about pipeline management and doesn't override this report-generation task. I'll proceed with generating the evaluation report directly from the Evidence Pack.

---

# Valpromide: From Anticonvulsant/Mood Disorders to Insomnia

## One-Sentence Summary

Valpromide is an amide prodrug of valproic acid, historically associated with anticonvulsant and mood-stabilizing applications — though no approved indication is formally registered in Italy.
The TxGNN model predicts it may be effective for **insomnia**, with **0 clinical trials** and **1 publication** currently supporting this direction.
The overall evidence base remains minimal, placing this candidate at the earliest stage of exploration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in Italy (drug not marketed) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Valpromide. Based on known pharmacological information, Valpromide is a structural amide prodrug of valproic acid — upon metabolism it is converted to valproic acid, which in turn enhances GABAergic neurotransmission in the central nervous system. This mechanism is broadly analogous to that of benzodiazepines, a major class of approved sleep aids, providing a theoretical basis for a sedative/hypnotic effect.

The conceptual link between anticonvulsant/mood-stabilizing drugs and insomnia is not unprecedented: valproate-class agents are sometimes observed to improve sleep architecture as a secondary effect in patients with epilepsy or bipolar disorder. Insomnia frequently co-occurs with agitation and anxiety disorders, and the GABAergic enhancement pathway that underlies Valpromide's anticonvulsant activity could plausibly reduce sleep-onset latency or improve sleep continuity.

However, it is important to emphasise that this mechanistic reasoning is derived **indirectly** from the valproate class. Valpromide itself has not been directly validated for GABA-mediated sleep promotion in controlled human studies. The TxGNN model prediction (score 99.79%) reflects graph-based biological plausibility, not clinical evidence — and must be interpreted accordingly until prospective data are available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10370890](https://pubmed.ncbi.nlm.nih.gov/10370890/) | 1999 | Case Series (n=8) | L'Encephale | Valpromide and carbamazepine used to manage aggressive agitation, anxiety, and insomnia in Alzheimer's dementia patients; both agents showed efficacy with a more favourable side-effect profile than neuroleptics |

---

## Italy Market Information

Valpromide currently holds no marketing authorizations in Italy and is not commercially available on the Italian market.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, contraindications, or key warnings could be retrieved for Valpromide at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting Valpromide for insomnia consists of a single 1999 case series (n=8) in which insomnia was a secondary symptom — not a primary endpoint — in a dementia population. There are no registered clinical trials, no regulatory approvals in Italy, and no verified MOA data. The TxGNN score reflects mechanistic plausibility through graph inference, not clinical validation.

**To proceed, the following is needed:**
- Retrieval and review of the Valpromide package insert (TFDA/EMA sources) to establish key warnings and contraindications before any safety assessment can be conducted
- Confirmation of mechanism of action via DrugBank API query (DG002)
- Prospective pharmacokinetic/pharmacodynamic studies characterising Valpromide's direct CNS sleep-promoting effects independently of valproic acid conversion
- At minimum one Phase 2 exploratory clinical trial in primary insomnia patients (general adult population, not solely dementia cohorts) before upgrading the evidence level
- Assessment of whether Italy/EU regulatory pathway is feasible given zero existing authorizations and no approved indication in any country
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

