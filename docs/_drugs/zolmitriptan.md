---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 3
---

# Zolmitriptan
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

The `txgnn-pipeline` skill confirms the TxGNN reporting context. Now let me generate the report from the Evidence Pack.

---

# Zolmitriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a selective serotonin 5-HT1B/1D receptor agonist (triptan) widely used for the acute treatment of migraine attacks.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly known as basilar-type migraine),
with **0 registered clinical trials** and **19 publications** currently surrounding this direction—though the evidence is predominantly derived from general migraine or mixed-aura populations rather than dedicated brainstem aura trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (with or without aura) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Zolmitriptan acts as a selective 5-HT1B/1D receptor agonist — the same pharmacological class as all triptans. It constricts dilated cranial blood vessels and, critically, inhibits trigeminal nociceptive transmission at both peripheral and **central (brainstem) levels**. This dual peripheral-central action distinguishes zolmitriptan from earlier triptans such as sumatriptan, and is the primary mechanistic reason TxGNN flags it as relevant to a brainstem-originating migraine subtype.

Migraine with brainstem aura (MBA) is characterized by aura symptoms arising from brainstem structures — vertigo, diplopia, dysarthria, tinnitus, or decreased consciousness — followed by or concurrent with typical migraine headache. Because the 5-HT1D receptor is expressed in the brainstem's trigeminal nucleus caudalis and periaqueductal grey, zolmitriptan's central penetration offers a plausible mechanistic rationale for relieving MBA symptoms.

However, the historical context complicates this prediction significantly. All triptans were traditionally contraindicated in basilar-type migraine (now renamed MBA) due to theoretical concern about basilar artery vasospasm causing stroke. Emerging data (including PMID 11903526) suggest this restriction may be overly conservative, but no dedicated Phase 2/3 RCT has prospectively enrolled MBA patients. The TxGNN prediction is mechanistically coherent and directionally supported by evolving expert opinion, yet dedicated prospective evidence remains absent.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registering "migraine with brainstem aura" as an indication for zolmitriptan have been identified in ClinicalTrials.gov or the ICTRP registry.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical Case Series | Headache | Reports triptan use in basilar migraine and migraine with prolonged aura; suggests triptans may be used cautiously in these patients with prominent neurological symptoms |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | J Headache Pain | Compares frovatriptan vs. zolmitriptan (and others) in migraine with aura; establishes that triptans taken during the headache phase are effective in aura-type migraine |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT subgroup | Neurological Sciences | Head-to-head frovatriptan 2.5 mg vs. zolmitriptan 2.5 mg in migraine with aura; zolmitriptan showed comparable efficacy in this Italian multicenter crossover study |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review / Guideline | Headache | American Headache Society updated evidence assessment for acute migraine pharmacotherapy; zolmitriptan achieves high evidence rating for general migraine |
| [9399016](https://pubmed.ncbi.nlm.nih.gov/9399016/) | 1997 | Phase 3 Trial | Cephalalgia | Tolerability profile across >3,000 subjects; zolmitriptan 2.5–5 mg well tolerated with predictable adverse-event profile |
| [15581383](https://pubmed.ncbi.nlm.nih.gov/15581383/) | 2004 | RCT | CNS Drugs | Zolmitriptan 5 mg ODT demonstrates rapid headache response onset within 45 min and sustained efficacy at 2 hours |
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | RCT | Headache | TEENZ study: zolmitriptan nasal spray effective and well tolerated in adolescents aged 12–17; relevant for understanding use in non-standard migraine populations |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Frontiers in Neurology | Reviews treatment options for vestibular migraine (an overlapping brainstem-aura-related entity); notes scarcity of dedicated RCTs |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | RCT | Cephalalgia | Compares triptan efficacy in migraine with early cutaneous allodynia; zolmitriptan group showed significant pain reduction at 1 hour |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical Review | Cephalalgia | Documents zolmitriptan's central 5-HT1B/1D agonism and ability to inhibit trigeminovascular activation at the brainstem level — directly supports the mechanistic rationale |

---

## Taiwan Market Information

Zolmitriptan currently holds **no marketing authorizations** in Taiwan. There are no licensed products, approved indications, or regulated dosage forms on record with the TFDA as of the data cutoff (2026-05-05).

---

## Safety Considerations

Detailed TFDA package insert warnings and contraindications were not available in the current Evidence Pack, and no drug-drug interaction data were retrieved. The historical class-level concern — **triptan use in basilar-type / brainstem aura migraine** — represents the most clinically significant safety signal and must be reviewed against the current prescribing information before any use in this population.

> Please refer to the official prescribing information (package insert) for complete safety information, including contraindications, warnings, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic rationale for zolmitriptan in migraine with brainstem aura is scientifically plausible — its central 5-HT1D activity at the brainstem level directly addresses the pathophysiology — no prospective clinical trial has specifically enrolled this patient subtype, and the historically recognized class contraindication has not been formally overturned by a dedicated safety study. Evidence level L3 with zero registered trials is insufficient to proceed beyond hypothesis generation.

**To proceed, the following is needed:**

- **Prospective safety study**: A dedicated open-label or placebo-controlled trial enrolling patients meeting the ICHD-3 criteria for migraine with brainstem aura, with neurological monitoring for basilar artery events
- **Regulatory contraindication review**: Formal reassessment of whether the historical triptan contraindication in this subtype remains valid, citing the most recent ICHD and AHS guidance
- **MOA data retrieval**: Full DrugBank pharmacology entry to document receptor binding profiles and CNS penetrance data (currently listed as a data gap)
- **Taiwan market pathway**: TFDA new drug application strategy, given the drug is not currently marketed in Taiwan
- **TFDA package insert**: Obtain and parse the full prescribing information to complete the safety profile before any clinical protocol is designed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

