---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 6
---

# Rimegepant
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

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rimegepant (Nurtec ODT / Vydura) is a CGRP receptor antagonist approved in the US and EU for the acute treatment of migraine with or without aura, and for the preventive treatment of episodic migraine in adults.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a specific subtype historically excluded from triptan use due to vascular safety concerns — with **no dedicated clinical trials** and **14 publications** (drawn primarily from general migraine populations) currently informing this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute treatment of migraine with or without aura; preventive treatment of episodic migraine (based on US/EU approvals — not yet registered in Italy) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Rimegepant belongs to the gepant class — small-molecule calcitonin gene-related peptide (CGRP) receptor antagonists. CGRP is a neuropeptide released from trigeminal nerve terminals during migraine attacks; by blocking its receptor, rimegepant interrupts the trigeminal-vascular pain cascade that underlies migraine regardless of aura subtype. This mechanism is not route-specific or cortex-specific: it operates across the entire trigeminal system, including brainstem projections.

Migraine with brainstem aura (historically called basilar-type migraine) produces aura symptoms originating in the brainstem — dysarthria, diplopia, tinnitus, hyperacusis, or impaired consciousness — before or during the headache phase. For decades, triptans were considered contraindicated in this population due to concerns about serotonin-mediated vasoconstriction in the posterior circulation. Rimegepant does not act via vasoconstriction; the 2026 longitudinal MRI angiography study (PMID 41574090) confirmed a non-vasoconstrictive vascular profile during real migraine attacks, making it theoretically safer than triptans for this subtype.

The principal limitation is that all existing Phase 3 RCTs enrolled adults with "migraine with or without aura" as a broad category, without stratifying for the brainstem aura variant. The prediction therefore rests on mechanistic extrapolation supported by indirect population-level data, not a dedicated trial. Given the unmet need in this patient group — who currently have few approved acute options — the extrapolation is scientifically defensible, though prospective confirmation remains necessary.

---

## Clinical Trial Evidence

Currently no clinical trials specifically studying rimegepant for migraine with brainstem aura are registered in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Narrative Review | CNS Drugs | Comprehensive review of rimegepant (Nurtec ODT / Vydura): Phase 3 pivotal trials demonstrated superiority over placebo for 2-hour pain freedom and sustained pain relief; dual approval for acute and preventive migraine |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Comprehensive Review | Handbook of Clinical Neurology | Full overview of the gepant class; traces CGRP receptor antagonist development from first-generation (hepatotoxicity issues) to approved gepants; contextualises rimegepant's safety profile |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Regulatory Review | Drugs | First-approval profile: clinical pharmacology, pivotal trial data, and regulatory milestones for rimegepant ODT; also notes investigation for refractory trigeminal neuralgia |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network Meta-Analysis | The Journal of Headache and Pain | Indirect comparison of lasmiditan vs. rimegepant and ubrogepant for acute oral migraine treatment; quantifies onset-of-efficacy differences across novel agents in the absence of head-to-head trials |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 Open-Label Trial | The Journal of Headache and Pain | 24-week study of once-daily rimegepant 75 mg for episodic migraine prevention; confirms long-term tolerability at a higher dosing frequency than currently approved |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 Open-Label | Cephalalgia | Long-term safety and effectiveness of rimegepant 75 mg ODT in Chinese adults with 6–18 monthly migraine attacks; first Phase 3 dataset from an Asian population, supporting cross-ethnic generalisability |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Longitudinal MRA Study | Brain Communications | First direct vascular imaging study during spontaneous migraine attacks; confirms rimegepant does not cause cerebral or extracerebral vasoconstriction — directly relevant to the safety argument in brainstem aura |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Contextual review of rimegepant within the landscape of novel acute migraine therapies; discusses patient selection, safety, and pharmacoeconomics |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospective Cohort | Headache | Off-label rimegepant use for acute migraine in adolescents; evaluates real-world tolerability and effectiveness outside approved age groups |
| [32993366](https://pubmed.ncbi.nlm.nih.gov/32993366/) | 2021 | Review | Annals of Pharmacotherapy | Comparative review of rimegepant, ubrogepant, and lasmiditan as novel acute migraine agents; summarises efficacy endpoints, adverse event profiles, and place-in-therapy considerations |

---

## Italy Market Information

Rimegepant currently holds no AIFA marketing authorizations in Italy. It is approved in the US as Nurtec ODT (Pfizer/Biohaven) and in the EU as Vydura; however, EU approval does not automatically confer Italian market availability — a separate AIFA procedure or mutual recognition process would be required. Italian patients currently have no licensed access to this drug.

---

## Safety Considerations

Please refer to the Vydura EU Summary of Product Characteristics (SmPC) for the full safety profile. No drug interaction data was available in this evidence pack for automated review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Rimegepant's non-vasoconstrictive CGRP receptor antagonism is mechanistically applicable across all migraine subtypes, and for migraine with brainstem aura specifically, the absence of vasoconstriction addresses the core reason triptans have been avoided in this population — creating a genuinely meaningful clinical opportunity. However, all supporting evidence is indirect extrapolation from broad migraine trials; no dedicated brainstem aura data exists.

**To proceed, the following is needed:**
- A prospective registry or sub-group analysis specifically capturing patients with migraine with brainstem aura to generate direct efficacy and safety data
- Full MOA documentation (DrugBank API query listed as pending) to support regulatory and payer submissions
- AIFA marketing authorization application or compassionate use framework — rimegepant is approved in the EU (Vydura) but not yet registered in Italy
- Review of the full Vydura SmPC for contraindications, hepatic warnings, and CYP3A4 interaction guidance before clinical use
- Pharmacovigilance design tailored to the brainstem aura population, who may carry elevated cerebrovascular risk compared to typical migraine patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

