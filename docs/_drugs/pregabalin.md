---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill to establish context, then generating the report per the v5 format specification.

---

# Pregabalin: From Neuropathic Pain to Tendinitis

## One-Sentence Summary

Pregabalin is a gabapentinoid anticonvulsant and analgesic globally established for neuropathic pain, fibromyalgia, and epilepsy, but not yet registered in Taiwan.
The TxGNN model (rank #1) predicts it may be effective for **Tendinitis**, with **0 clinical trials** and **6 publications** currently supporting this direction — the majority representing indirect surgical-pain or preclinical evidence rather than direct tendinitis studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan regulatory record; globally approved for neuropathic pain, epilepsy, and fibromyalgia |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Pregabalin binds to the **α2δ subunit of voltage-gated calcium channels (VGCC)**, reducing presynaptic calcium influx and thereby decreasing the release of excitatory neurotransmitters — glutamate, norepinephrine, and substance P. This mechanism is the basis of its proven efficacy in neuropathic pain, epilepsy, and fibromyalgia.

The mechanistic connection to tendinitis is biologically plausible, but conditional. **Chronic tendinopathy** is now recognized to involve a neuropathic pain component and central sensitization: sensitized spinal dorsal horn neurons amplify pain signals from the tendon, even in the absence of ongoing tissue inflammation. In this chronic-phase context, Pregabalin's α2δ VGCC inhibition could reduce central pain amplification. Two identified RCTs provide indirect support, showing that perioperative Pregabalin reduces pain and opioid consumption after arthroscopic rotator cuff repair — a procedure involving direct tendon pathology.

However, **acute tendinitis is primarily driven by inflammatory mediators** (prostaglandins, cytokines), and Pregabalin has no known anti-inflammatory mechanism. Its potential clinical role is therefore restricted to the neuropathic/sensitization component of **chronic** tendon disease, not as a first-line or disease-modifying agent for acute tendinitis. This mechanistic mismatch explains the L4 evidence ceiling and the absence of registered clinical trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral Pregabalin achieved post-operative pain scores equivalent to interscalene brachial plexus block after arthroscopic rotator cuff repair; also assessed opioid consumption and patient satisfaction |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT | J Orthop Sci | Evaluated Pregabalin's analgesic efficacy and opioid-sparing effect after arthroscopic rotator cuff repair; supports its role in multimodal analgesia for tendon surgery |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case Report | Pain Practice | First reported case of posterior femoral cutaneous nerve neuropathy caused by hamstring tendonitis from marathon running; highlights neuropathic pain overlap with tendon injury |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Clinical Review | Praxis | Fluoroquinolone-associated disability including tendinopathy; documents the neuropathic and systemic pain dimension of tendon disorders — supports the central sensitization hypothesis |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Piriformis syndrome treated by sciatic neurolysis and piriformis tendon release; indirectly supports neuropathic pain involvement in tendon-adjacent pathology |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | Plant extract (Cissus quadrangularis, traditionally used for tendon healing) tested against vincristine-induced neuropathy in rats; indirect mechanistic context only, minimal direct relevance |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns the highest prediction score (99.71%) to this indication, the underlying evidence is purely observational/preclinical (L4), with no registered clinical trials specifically investigating Pregabalin in tendinitis. More critically, the mechanistic rationale applies only to the **chronic neuropathic phase** of tendon disease — not to acute tendinitis, which is the primary ICD entity in question.

**To proceed, the following is needed:**

- Formal MOA data from DrugBank to confirm α2δ VGCC binding relevance to tendon pain pathways
- Clarification of target population: **chronic tendinopathy with central sensitization** vs. acute inflammatory tendinitis (these require different study designs and endpoints)
- Safety and warning data from the Taiwan TFDA package insert or global prescribing information (currently a blocking data gap)
- A pilot prospective study or registry in patients with chronic tendinopathy screened for neuropathic pain features (e.g., S-LANSS or DN4 score ≥ threshold) before committing to an RCT
- Consideration of whether **migraine disorder** (predicted indication #5, Evidence Level L2, 3 trials, 19 publications) should be prioritized as a more evidence-supported repurposing candidate for Pregabalin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

