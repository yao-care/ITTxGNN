---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

The txgnn-pipeline skill confirms the reporting context. Now I'll generate the full evaluation report based on the Evidence Pack.

---

# Paliperidone: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Paliperidone is a second-generation (atypical) antipsychotic — the active metabolite of risperidone — with globally established use in schizophrenia and schizoaffective disorder.
The TxGNN model's highest-ranked prediction is **Retinal Dystrophy with or without Extraocular Anomalies** (score: **99.92%**),
however **no clinical trials** exist and all 15 retrieved publications address the ophthalmological disease area in general rather than paliperidone efficacy, placing this at evidence level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Schizoaffective Disorder (globally established; not registered in Italy) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Paliperidone is a D2/5-HT2A/α1-adrenergic/H1 multi-receptor antagonist. It modulates central dopamine and serotonin neurotransmission, which underpins its established efficacy in schizophrenia and schizoaffective disorder. Its pharmacological profile is closely related to risperidone, of which it is the primary active metabolite.

Retinal dystrophy with or without extraocular anomalies is a fundamentally different class of disease — a hereditary degenerative condition in which mutations in genes such as *RPGR* or *CRB1* cause progressive photoreceptor cell death and structural breakdown of the retina. The pathological mechanism is genetic and structural, with no established dopaminergic or serotonergic component driving disease progression.

The mechanistic rationale for this TxGNN prediction is not considered credible. Although dopamine receptors exist in trace amounts within retinal tissue, there is no published evidence that D2/5-HT2A antagonism can halt or reverse genetically-determined photoreceptor degeneration. The high prediction score most likely reflects a **graph-embedding false positive** — an artifact of disease-node proximity in the knowledge graph rather than a genuine biological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Fifteen publications were retrieved for the search combining paliperidone and retinal dystrophy with or without extraocular anomalies. However, upon inspection, **none of these papers document paliperidone use in this indication**. The publications address general ophthalmological topics — orbital infections, congenital lens and eyelid anomalies, extraocular muscle fibrosis disorders, optic disc pathology, and cranial dysinnervation syndromes. They appear to have been retrieved via disease-keyword matching on "extraocular anomalies" rather than any drug-disease co-occurrence. Listing them as supporting evidence would misrepresent the actual state of knowledge.

Currently no literature supporting paliperidone use in retinal dystrophy is available.

---

## Italy Market Information

Paliperidone holds **no marketing authorizations in Italy**. The drug is not currently registered or marketed in this jurisdiction. No authorization records are available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no credible mechanistic link between paliperidone's dopaminergic/serotonergic receptor antagonism and hereditary retinal dystrophy, and zero drug-specific clinical or literature evidence supports this indication. This TxGNN prediction is consistent with a graph-embedding false positive and should not progress to further evaluation without substantial new mechanistic evidence.

**To proceed, the following is needed:**
- A peer-reviewed mechanistic hypothesis connecting D2/5-HT2A modulation to photoreceptor survival or retinal degeneration pathways
- At least one preclinical study (in vitro or animal model) demonstrating paliperidone activity in a retinal dystrophy context
- Retrieval of complete MOA data from DrugBank (pending data gap DG002) before any mechanistic re-evaluation
- AIFA package insert data (pending data gap DG001) to enable full safety screening before any clinical feasibility assessment

---

> ### ⚠️ Supplementary Note: Most Actionable TxGNN Prediction
>
> Among all 10 ranked predictions in this Evidence Pack, **Rank 10 — Treatment-Refractory Schizophrenia** (TxGNN score: **99.80%**) is by far the most clinically meaningful and actionable finding. Key indicators:
>
> | Item | Detail |
> |------|--------|
> | Evidence Level | **L3** (observational studies + expert reviews) |
> | Clinical Trials | 4 identified (including 1 completed Phase 4) |
> | Literature | 2 supporting publications |
> | Mechanistic Link | Direct and well-understood — D2/5-HT2A antagonism targets the core neurotransmitter imbalances of schizophrenia |
> | Decision Stage | **Research Question** — warrants further investigation |
>
> Paliperidone in treatment-refractory schizophrenia (TRS) occupies a defined clinical niche: as a second-line option after failure of ≥2 standard D2 antagonists, prior to or alongside clozapine escalation. A **dedicated evaluation report for this indication is recommended** as the priority output from this pipeline run.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

