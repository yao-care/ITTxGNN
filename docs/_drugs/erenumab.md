---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 1
---

# Erenumab
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

Using the `txgnn-pipeline` skill to confirm context — this is a Taiwan TxGNN project. The skill confirms standard workflow; no additional pipeline steps override report generation. Proceeding to compose the report per the Evidence Pack.

---

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab is a fully human monoclonal antibody that blocks the CGRP (calcitonin gene-related peptide) receptor, established as a preventive treatment for episodic and chronic migraine.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura (MBaA)** — a rare, historically underserved migraine subtype — with **0 clinical trials** and **20 publications** currently supporting this direction, primarily covering migraine with aura broadly rather than the brainstem-specific subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention (episodic and chronic migraine) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Erenumab (brand name: Aimovig) is the first CGRP receptor monoclonal antibody specifically engineered to prevent migraine. CGRP is a potent vasodilatory neuropeptide released from trigeminal nerve terminals during migraine attacks; by occupying and blocking its receptor, erenumab interrupts the cycle of neurogenic inflammation and vasodilation that sustains migraine pain. This mechanism is well-validated in Phase 3 trials for both episodic and chronic migraine.

Migraine with Brainstem Aura (MBaA) — formerly called basilar-type migraine per ICHD-3 — is characterized by aura symptoms that originate from brainstem structures: vertigo, dysarthria, tinnitus, diplopia, and ataxia. Its pathophysiology involves cortical spreading depression (CSD) propagating into the posterior fossa and recruiting the basilar artery and posterior circulation. Critically, CGRP is highly expressed in posterior fossa structures, particularly the brainstem trigeminal nucleus. This anatomical overlap forms the core of TxGNN's mechanistic inference: if CGRP receptor blockade reduces trigeminovascular activation in cortical migraine, the same pathway in the posterior fossa could plausibly reduce the frequency and severity of brainstem aura events.

The prediction is not without caveats. MBaA was historically treated as a contraindication for triptans (vasoconstrictors) due to theoretical posterior circulation vasospasm risk. Although erenumab does not vasoconstrict and actually reduces vasodilation, its net vascular effect specifically in the posterior circulation of MBaA patients has never been formally studied. The 2024 experimental data (PMID 38850034) further shows that sildenafil — acting via the cGMP pathway — can still trigger migraine attacks even under erenumab pretreatment, suggesting CGRP-independent brainstem mechanisms exist. This means CGRP receptor blockade alone may provide only partial coverage in MBaA.

---

## Clinical Trial Evidence

Currently no clinical trials specifically studying erenumab in migraine with brainstem aura are registered in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | RCT Secondary Analysis | JAMA Neurology | Pooled analysis of erenumab RCTs; comparable safety and efficacy confirmed in migraine with aura vs. without aura; provides the most direct efficacy analogy for brainstem aura subtype |
| [35230406](https://pubmed.ncbi.nlm.nih.gov/35230406/) | 2022 | Review / Clinical Summary | JAMA | Erenumab determined safe and effective for migraine with aura based on aggregated RCT data; broad endorsement of the aura indication |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Observational (REFORM Study) | J Headache Pain | Longitudinal characterization of migraine aura frequency changes during and after erenumab treatment in adults with frequent, prospectively confirmed aura; most directly relevant to aura biology |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Cohort (Post-hoc) | Headache | Post-hoc cardiovascular safety analysis of long-term erenumab trials in patients stratified by CV risk degree, including those with aura (elevated baseline vascular risk) |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Biomarker Cohort (REFORM) | J Headache Pain | Elevated plasma suPAR (systemic inflammation marker, higher in migraine with aura) predicts erenumab response; supports CGRP–inflammation axis as a therapeutic target in aura patients |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3b RCT | Lancet | Foundational efficacy trial: erenumab effective in episodic migraine patients who failed 2–4 prior preventives; establishes the drug's role in refractory migraine, a population overlapping with MBaA |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | Int Immunopharmacology | Systematic review confirming erenumab prophylactic efficacy across episodic and chronic migraine subtypes |
| [38850034](https://pubmed.ncbi.nlm.nih.gov/38850034/) | 2024 | Experimental / Basic Science | Cephalalgia | Sildenafil (cGMP/PDE5 pathway) induces migraine attacks even with prior erenumab administration; demonstrates CGRP-independent brainstem mechanisms — key safety and mechanistic caveat for MBaA |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Real-World Cohort | Clin Neurol Neurosurg | Croatian real-world data: erenumab effective and safe in treatment-resistant chronic migraine at 6 months; includes patients with multiple prior prophylaxis failures |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Comprehensive review of CGRP's role in migraine pathophysiology, covering trigeminal system, posterior fossa involvement, and CNS dysfunction — mechanistic foundation for MBaA rationale |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although erenumab has a mechanistically plausible basis for benefit in MBaA — CGRP receptor blockade in posterior fossa structures where CGRP is abundantly expressed — no clinical trials exist for this specific subtype, the available literature covers migraine with aura broadly rather than MBaA specifically, and the historically elevated posterior circulation vascular risk in MBaA patients creates an unresolved safety signal that cannot be cleared from current evidence alone. The evidence level (L3) and decision stage (S1: Research Question) confirm this is still a hypothesis-generating finding.

**To proceed, the following is needed:**
- **Safety clarification first**: Post-hoc extraction of MBaA patients (identified by ICHD-3 criteria) from existing erenumab long-term open-label trials, with focused cerebrovascular safety analysis
- **Mechanistic data**: Confirmation of CGRP receptor density and distribution in posterior fossa / basilar artery territory in MBaA vs. other migraine subtypes
- **Prospective registry or observational study**: Real-world cohort of erenumab-treated MBaA patients with structured monitoring for posterior circulation events (stroke, TIA, vertebrobasilar vasospasm)
- **Headache specialist review**: Expert consensus on whether the historical vasospasm contraindication (from triptan era) translates — or does not — to a CGRP receptor antibody mechanism
- **Regulatory and MOA data**: Full Taiwan (TFDA) package insert and DrugBank MOA record to complete the formal S1 safety screen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

