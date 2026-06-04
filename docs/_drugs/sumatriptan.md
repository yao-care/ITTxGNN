---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 1
---

# Sumatriptan
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

---

# Sumatriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is the prototypical triptan, widely used for the acute treatment of migraine attacks (with or without aura) and cluster headache.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly known as basilar-type migraine),
with **0 registered clinical trials** and **18 publications** currently informing this direction.
While the mechanistic rationale is scientifically plausible, historical prescribing cautions specific to this subtype and the absence of direct trial evidence require careful evaluation before proceeding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (with or without aura); cluster headache |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sumatriptan is a selective 5-HT1B/1D receptor agonist — the first and most studied member of the triptan class. It terminates migraine attacks through two complementary mechanisms: constricting dilated cranial blood vessels and inhibiting the release of vasoactive neuropeptides (CGRP, substance P) from perivascular trigeminal axons in the dura mater. This action directly interrupts trigeminovascular activation, the central pathway in migraine pain generation.

Migraine with brainstem aura (MBA) is a migraine subtype defined by aura symptoms of brainstem origin — including dysarthria, vertigo, tinnitus, diplopia, bilateral paraesthesia, or decreased level of consciousness — occurring before the headache phase. Its pathophysiology involves cortical spreading depression (CSD) extending into the brainstem and activation of the trigeminal cervical complex. Because sumatriptan's primary targets (5-HT1B/1D receptors, trigeminovascular pathways) overlap precisely with these MBA mechanisms, the TxGNN prediction has a credible mechanistic foundation.

That said, the International Headache Society (IHS) historically listed MBA (then "basilar-type migraine") as a relative contraindication to triptans, citing theoretical risk of basilar artery vasospasm. Post-2004 literature has increasingly questioned whether this caution is overly conservative given the lack of documented vasospasm events — but no dedicated RCT in MBA patients has yet been conducted. Compounding this, PMID 25841032 (Hansen et al., 2015, *Neurology*) documented that sumatriptan shows meaningfully reduced efficacy in migraine with aura compared to migraine without aura, suggesting that MBA — a more severe aura subtype — may respond less robustly than general migraine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sumatriptan specifically in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Comparative Clinical Study | *Neurology* | Sumatriptan demonstrates reduced efficacy in migraine with aura vs. without aura — directly relevant to the brainstem aura subtype and a key caution for this repurposing |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | *Cephalalgia* | Early sumatriptan administration prevents PACAP38-induced migraine attacks in a randomised controlled trial; confirms triptan efficacy in provoked migraine models |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | *Cephalalgia* | Double-blind, placebo-controlled parallel-group trial of oral sumatriptan 200 mg in acute migraine with aura; efficacy rates of 70–85% established in open-label studies |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | *Phytotherapy Research* | Double-blind RCT comparing ginger powder vs. sumatriptan in acute migraine without aura (n=100); comparable efficacy between arms |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review | *Headache* | American Headache Society updated evidence assessment of all acute migraine pharmacotherapies; sumatriptan receives highest evidence rating for acute treatment |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | *Cephalalgia* | Comprehensive review of sumatriptan clinical experience in migraine and cluster headache; details 5-HT1 receptor mechanism and vascular effects relevant to the MBA contraindication debate |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Review | *Neurology* | Addresses sumatriptan use during the migraine aura phase; discusses the pharmacological rationale and clinical implications |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Clinical Study | *JAMA Neurology* | PET imaging study showing sumatriptan's central 5-HT1B receptor binding during migraine attacks; clarifies CNS mechanism and extent of central penetration |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Drug Approval Review | *Expert Review of Neurotherapeutics* | Reviews sumatriptan needle-free subcutaneous approval for acute migraine with or without aura and cluster headache; highlights superiority of subcutaneous route in refractory attacks |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | *Handbook of Clinical Neurology* | Status migrainosus (migraine attack >72 h): complications, clinical course, and treatment burden; contextualises the severity end of the migraine spectrum where treatment gaps remain |

---

## Italy Market Information

Sumatriptan currently holds no marketing authorizations in Italy. No product data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Clinical Note**: The historical IHS contraindication of triptans in basilar-type migraine (now MBA) stems from a theoretical risk of basilar artery vasospasm. No confirmed vasospasm events attributable to sumatriptan in this subtype have been documented in the literature, but this risk profile must be formally re-evaluated against current evidence before clinical use. Sumatriptan is also known to be contraindicated in ischaemic heart disease, prior stroke/TIA, and uncontrolled hypertension — conditions that require active screening in MBA patients given their overlapping symptom profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Sumatriptan's mechanism of action maps directly onto the trigeminal and vascular pathways implicated in migraine with brainstem aura, and the TxGNN model assigns near-maximal confidence (99.74%). However, no dedicated clinical trials exist for this specific subtype, the evidence base (L3) relies on observational and review data for migraine in general, reduced aura-subtype efficacy has been documented, and the historical contraindication has not been formally resolved by prospective trial data.

**To proceed, the following is needed:**

- **Resolve the historical contraindication**: Commission a systematic review of post-2004 evidence specifically addressing triptan safety in MBA, with input from a headache neurologist specialist
- **Conduct a dedicated prospective study**: Design a phase 2 RCT in confirmed MBA patients (IHS ICHD-3 criteria) to establish efficacy and safety benchmarks
- **Fill regulatory data gaps**: Obtain the full package insert (complete contraindications, drug interactions, warnings) before any prescribing guidance is issued
- **Establish a safety monitoring plan**: Include cardiovascular and cerebrovascular monitoring, particularly for patients with vascular risk factors, given MBA's symptom overlap with TIA/stroke
- **Clarify MOA data**: Retrieve formal DrugBank pharmacodynamic data to strengthen mechanistic documentation in the evidence package
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

