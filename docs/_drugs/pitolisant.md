---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 3
---

# Pitolisant
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

The skill confirms this is a TxGNN multi-country pipeline context. The system prompt already defines the full report format. Proceeding to generate the report now.

---

# Pitolisant: From Narcolepsy to Insomnia

## One-Sentence Summary

Pitolisant is a first-in-class selective histamine H3 receptor inverse agonist, approved internationally (Europe and USA) for the treatment of narcolepsy with or without cataplexy. The TxGNN model predicts it may be effective for **Insomnia**, with **1 clinical trial** (withdrawn, zero enrollment, and not even targeting insomnia) and **8 publications** retrieved — however, virtually all literature addresses narcolepsy or excessive daytime sleepiness. Pitolisant's established wake-promoting mechanism is fundamentally opposite to what insomnia treatment requires, making this a likely **false-positive** prediction driven by disease graph proximity rather than genuine pharmacological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not locally registered; approved internationally for narcolepsy with or without cataplexy |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the retrieved literature, Pitolisant is a selective histamine H3 receptor inverse agonist. By blocking H3 autoreceptors on histaminergic neurons in the posterior hypothalamus, Pitolisant prevents tonic autoinhibition of histamine release, thereby increasing histaminergic neurotransmission throughout the brain. Downstream activation of postsynaptic H1 receptors promotes arousal and wakefulness. This is precisely why Pitolisant is efficacious in narcolepsy — a disorder defined by pathological inability to maintain wakefulness.

This mechanism is, however, **pharmacologically opposite** to what is required for insomnia treatment. Insomnia calls for sleep promotion, not wake promotion. It is no coincidence that the well-established sedative-hypnotics in clinical use — including doxepin, diphenhydramine, and the antihistamine class broadly — work as **H1 receptor antagonists**, dampening histaminergic activity to facilitate sleep. Pitolisant amplifies that same system in the exact opposite direction. A review in *Current Neuropharmacology* (PMID 34521328) explicitly contrasts H3R inverse agonist pitolisant (wakefulness) against H1R antagonist doxepin (insomnia treatment), underscoring this mechanistic dichotomy.

The TxGNN model assigned an exceptionally high score (99.71%) to this prediction, which most likely reflects the topological proximity of narcolepsy and insomnia nodes within the biomedical knowledge graph — both are classified as sleep disorders and share overlapping phenotypic descriptors. This is a recognized limitation of graph-based repurposing models: they can identify structural closeness without capturing the directional nature of a drug's pharmacodynamic action. This prediction is assessed as a **probable false positive** and does not warrant clinical development without a compelling mechanistic reframe.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Targeted **alcohol use disorder**, not insomnia — primary endpoint was reduction of monthly heavy drinking days. Trial was withdrawn before enrolling any participants, generating no clinical data. Represents a negative signal both for feasibility and for relevance to the insomnia indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet Neurology | Phase 3 RCT in children ≥6 years with narcolepsy; pitolisant demonstrated safety and efficacy for excessive daytime sleepiness and cataplexy. Entirely narcolepsy-focused — not insomnia. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant reduced residual excessive daytime sleepiness in OSA patients adherent to CPAP. Demonstrates a **wake-promoting** effect — the opposite of insomnia treatment. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | International RCT of pitolisant for daytime sleepiness in moderate-to-severe OSA patients refusing CPAP; confirmed wake-promoting efficacy. No insomnia data. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort (Real-world) | Revista de neurologia | Real-world study in type 1 narcolepsy patients unresponsive to prior standard treatments; pitolisant showed effectiveness and tolerability in this refractory population. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Reviews histaminergic system changes in neuropsychiatric disorders; explicitly contrasts pitolisant (H3R inverse agonist → wakefulness) with doxepin (H1R antagonist → insomnia treatment) — highlights the mechanistic incompatibility with the predicted indication. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | Comprehensive overview of all four histamine receptor subtypes and their drug targets; provides mechanistic foundation for H3R pharmacology in the brain. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Profile of pitolisant for narcolepsy management; confirms European authorization and characterises H3 inverse agonism as the drug's defining mechanism. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review/Mechanism | Clinical Neuropharmacology | Pitolisant as an alternative stimulant for adolescents with narcolepsy refractory to conventional therapy; underscores the wakefulness-enhancement mechanism via H3 autoreceptor blockade. |

---

## Italy Market Information

Pitolisant currently has no registered authorizations in Italy (0 licenses). The drug is not marketed locally.

> **Note:** Pitolisant (brand name **Wakix**) has received EMA approval for narcolepsy with or without cataplexy in adults, and subsequently for children aged 6 and above (EMA/CHMP). It has also been approved by the FDA (2019) for excessive daytime sleepiness in adult narcolepsy. These international approvals are not reflected in the local authorization database queried for this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pitolisant's core pharmacological action — promoting wakefulness through histamine H3 receptor inverse agonism — is directionally incompatible with insomnia treatment, which requires facilitation of sleep rather than arousal. The sole retrieved clinical trial was withdrawn with zero enrollment and was targeting a completely different indication (alcohol use disorder), and all eight publications in the literature corpus address narcolepsy or excessive daytime sleepiness. The TxGNN high score almost certainly reflects false-positive graph topology between sleep disorders rather than genuine repurposing potential.

**To proceed, the following is needed:**

- A credible mechanistic hypothesis explaining how a wake-promoting agent could paradoxically benefit insomnia patients (e.g., circadian resetting, rebound sleep induction, or a specific insomnia subtype such as hyperarousal-related insomnia — none of which are currently supported by evidence)
- De novo clinical trial data specifically in insomnia populations; no such trials exist
- Safety profiling for insomnia patients, who differ substantially from the narcolepsy population in sleep architecture, comorbidities, and concomitant medication use
- Reassessment of TxGNN model performance on the sleep disorder subgraph to quantify the systematic false-positive rate for pharmacodynamically opposing indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

