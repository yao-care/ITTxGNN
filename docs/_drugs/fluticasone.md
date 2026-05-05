---
layout: default
title: Fluticasone
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 3
---

# Fluticasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the `txgnn-pipeline` skill noted. No additional pipeline-specific overrides apply to report generation. Proceeding to render the report from the Evidence Pack.

---

# Fluticasone: From Allergic Rhinitis to Migraine Disorder

## One-Sentence Summary

Fluticasone is a potent synthetic glucocorticoid widely used as an inhaled or intranasal corticosteroid for allergic rhinitis, asthma, and related inflammatory conditions, though it holds no current regulatory approval in Italy.
The TxGNN model predicts it may be effective for **Migraine Disorder**, however with **0 clinical trials** and only **1 peripherally related publication** available, the evidence base is minimal at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / Asthma (corticosteroid class; no Italy authorization on record) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack. Based on established pharmacology, Fluticasone is a potent synthetic glucocorticoid (GC) that acts via intracellular glucocorticoid receptors to broadly suppress inflammatory gene expression — including inhibition of NF-κB signalling, COX-2 activity, and pro-inflammatory cytokine release (e.g., IL-1β, TNF-α).

Neuroinflammation is a recognized component of migraine pathophysiology: trigeminal nerve activation triggers the release of inflammatory neuropeptides such as CGRP and substance P, which in turn promote dural vasodilation and central pain sensitization. Fluticasone's anti-inflammatory profile theoretically overlaps with these pathways. Furthermore, the intranasal route of administration may additionally influence the sphenopalatine ganglion (SPG) — a parasympathetic ganglion in close proximity to the nasal mucosa that is already an established interventional target for migraine treatment (SPG blockade).

That said, this mechanistic link remains indirect and theoretical. Systemic bioavailability of intranasal fluticasone is very low (< 2%), making meaningful CNS penetration uncertain. No direct pharmacological studies have demonstrated trigeminal anti-inflammatory activity at clinically achievable doses. The TxGNN model's high prediction score likely reflects shared biological network features between corticosteroid pathways and migraine-related nodes in the knowledge graph, rather than direct pharmacological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Pharmacovigilance Review | Ann Allergy Asthma Immunol | WHO Uppsala Monitoring Centre data revealed an unexpected cluster of neuropsychiatric adverse events during intranasal corticosteroid use — suggesting that despite assumed local action, CNS exposure and neurological effects do occur, lending indirect biological plausibility to CNS activity of intranasal fluticasone |

> **Note:** This publication is an adverse event signal analysis, not a therapeutic efficacy study for migraine. It provides indirect mechanistic context only.

---

## Italy Market Information

Fluticasone (DB13867) currently holds no marketing authorizations in Italy. There are no approved product registrations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.20%, the supporting evidence is at Level L5 — no clinical trials have tested fluticasone for migraine, the single identified publication is a pharmacovigilance adverse event review rather than a therapeutic study, and the proposed mechanistic pathway (neuroinflammation suppression via intranasal GC delivery) remains an indirect, unvalidated hypothesis.

**To proceed, the following is needed:**
- Retrieve full mechanism of action (MOA) data from DrugBank to confirm relevant GC receptor targets
- Obtain official package insert warnings and contraindications (AIFA / TFDA) to assess safety baseline
- Commission or identify preclinical studies evaluating fluticasone's effect on trigeminal neuroinflammation or CGRP release
- Assess CNS bioavailability: does any intranasal or systemic fluticasone formulation achieve sufficient exposure at the trigeminal nucleus or dural level?
- Search for at least one proof-of-concept clinical study or case series testing corticosteroids (class-level) in acute or prophylactic migraine management, to establish mechanistic class evidence
- Clarify route compatibility: identify whether an appropriate delivery route exists to achieve the required pharmacological target engagement for migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

