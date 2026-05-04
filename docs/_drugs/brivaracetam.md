---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

The txgnn-pipeline skill confirms this is a standard TxGNN pipeline report task for the Italy deployment. Proceeding to generate the report from the Evidence Pack.

---

# Brivaracetam: From Focal-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Brivaracetam (BRV) is a third-generation antiseizure medication approved internationally for the adjunctive and monotherapy treatment of focal-onset (partial) seizures, acting as a high-affinity synaptic vesicle protein 2A (SV2A) ligand with 15–30× greater potency than levetiracetam.
The TxGNN model predicts it may be effective for **Visual Epilepsy**, with a prediction score of **99.51%**.
Currently **no dedicated clinical trials** have been registered for this specific indication, and while **19 publications** are available, the literature covers general BRV pharmacology and broad epilepsy management rather than visual epilepsy as a distinct clinical entity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Focal-onset seizures (adjunctive/monotherapy; approved internationally, not licensed in Italy) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on the published literature, brivaracetam is a selective, high-affinity ligand of synaptic vesicle protein 2A (SV2A) — the same target as levetiracetam, but with 15–30-fold greater binding affinity and markedly superior blood–brain barrier penetration. By occupying SV2A, BRV dampens excessive synaptic vesicle cycling and neurotransmitter release, raising the threshold for seizure initiation and propagation throughout cortical networks.

Visual epilepsy is a form of reflex epilepsy in which seizures are triggered by visual stimuli such as flickering lights or geometric patterns. The underlying mechanism involves abnormal hyperexcitability within the visual cortex and its downstream networks. Because SV2A is expressed throughout the cortex — including occipital/visual regions — BRV's suppression of synaptic vesicle release provides a plausible mechanistic connection. Critically, the photosensitivity model (photoparoxysmal EEG response, or PPR, to intermittent photic stimulation) has been used as a clinical proof-of-concept paradigm for SV2A ligands: early studies demonstrated that BRV can suppress visually-triggered cortical epileptiform discharges faster and more completely than levetiracetam, consistent with its higher brain penetration rate.

However, the 19 publications retrieved for this indication are predominantly general reviews of BRV pharmacology, focal epilepsy trial summaries, and broad epilepsy management guidelines — none specifically address visual epilepsy as a distinct clinical indication. The TxGNN prediction is mechanistically sound but remains at the preclinical/mechanistic evidence level (L4). The most directly relevant photosensitivity model evidence (PMID 17785672, 32949370) is catalogued under a related reflex epilepsy indication stream rather than visual epilepsy per se, and dedicated clinical trials are absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Visual Epilepsy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | Phase III RCT | Epilepsia open | Adjunctive BRV significantly reduced focal-onset seizure frequency vs. placebo in adult Asian patients (double-blind, placebo-controlled); confirms cross-population efficacy and tolerability |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic Review/Meta-analysis | Frontiers in neurology | BRV is safe and effective for childhood epilepsy; pooled analysis confirms meaningful seizure reduction across age groups with acceptable adverse-event profile |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Review/Meta-analysis | Expert review of neurotherapeutics | Comprehensive synthesis of BRV efficacy in focal epilepsy; highlights 15–30× greater SV2A affinity vs. levetiracetam and superior brain permeability as key differentiators |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Narrative Review | Advances in therapy | BRV preclinical and clinical profile: selective SV2A binding, favorable pharmacokinetics, and evidence for use in treatment-resistant epilepsy populations |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Narrative Review | Journal of epilepsy research | Synthesis of BRV trial and real-world data; confirms broad anti-seizure efficacy, faster CNS onset, and lower behavioral adverse-event burden vs. levetiracetam |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic Review/Meta-analysis | Frontiers in neurology | BRV safe and effective in children with epilepsy; favorable seizure-reduction and tolerability data across paediatric subgroups |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled Safety Analysis | Epilepsy & behavior | In-depth pooled safety analysis of adjunctive BRV in focal seizures across multiple RCTs; overall well-tolerated with low rates of behavioral adverse events |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Comprehensive review of antiseizure drug mechanisms; SV2A modulation confirmed as primary mechanism of the racetam class including BRV |
| [26664121](https://pubmed.ncbi.nlm.nih.gov/26664121/) | 2015 | Review | Neuropsychiatric disease and treatment | Early BRV profile: 10–30× more potent than levetiracetam, does not share LEV's Ca²⁺ channel or AMPA receptor activity, strong preclinical anti-seizure data across multiple models |
| [40069539](https://pubmed.ncbi.nlm.nih.gov/40069539/) | 2025 | Real-world Study | Neurology and therapy | Adjunctive BRV effective in epilepsy patients with intellectual disability (BRIVAFIRST Italy network); confirms real-world efficacy in populations typically excluded from RCTs |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for visual epilepsy is mechanistically plausible — BRV's SV2A-mediated dampening of cortical excitability can in principle suppress visually-triggered seizures — but no dedicated clinical trials exist and the retrieved literature does not include studies specifically targeting visual epilepsy as a clinical endpoint. With evidence remaining at L4 (preclinical/mechanistic inference), the data are insufficient to support a clinical repurposing decision at this stage.

**To proceed, the following is needed:**

- **Photosensitivity model proof-of-concept:** Commission or identify a dedicated PPR study in photosensitive epilepsy patients specifically evaluating BRV for visual-stimulus-triggered seizures; existing data (PMID 17785672, 32949370) on BRV in the photoparoxysmal response model should be formally incorporated
- **Targeted literature review:** Systematic search explicitly covering photosensitive epilepsy, pattern-sensitive epilepsy, and other visual reflex epilepsy subtypes with BRV
- **MOA documentation:** Complete the DrugBank API query (Data Gap DG002) to formally confirm SV2A mechanism and identify any secondary targets relevant to visual cortex excitability
- **Safety data retrieval:** Obtain the package insert (Data Gap DG001) to complete warnings, contraindications, and DDI profiling before any clinical pathway is opened
- **Prioritization note:** Consider advancing **Status Epilepticus** (Rank 2, L2 evidence, "Proceed with Guardrails") as the higher-priority repurposing candidate in parallel — a completed head-to-head IV BRV vs. IV levetiracetam trial in pediatric status epilepticus (NCT07163572, n=152) and a systematic review (PMID 32278203) provide substantially stronger evidence for that indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

