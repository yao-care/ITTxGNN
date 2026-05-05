---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 1
---

# Modafinil
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

Looking at the Evidence Pack, I'll now generate the Modafinil repurposing evaluation report.

---

# Modafinil: From Narcolepsy / Excessive Daytime Sleepiness to Insomnia

## One-Sentence Summary

Modafinil is a wakefulness-promoting agent approved globally for narcolepsy, obstructive sleep apnea-associated excessive sleepiness, and shift work sleep disorder — but currently carries no marketing authorization in Italy.
The TxGNN model predicts it may have relevance for **Insomnia**, with **29 clinical trials** and **19 publications** identified in the evidence search.
However, the vast majority address daytime sleepiness rather than insomnia directly, and a fundamental mechanistic paradox significantly undermines the plausibility of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Narcolepsy, OSA-associated excessive sleepiness, shift work sleep disorder (globally approved; no Italy marketing authorization) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published literature, modafinil is a wakefulness-promoting agent that inhibits the dopamine transporter (DAT), thereby increasing synaptic dopamine availability in wake-promoting circuits. It also enhances norepinephrine (NE) and orexin/hypocretin signaling — effects that collectively sustain alertness and counteract pathological sleepiness. These properties underpin its approved uses across narcolepsy, obstructive sleep apnea (residual excessive sleepiness), and shift work sleep disorder.

Because modafinil carries approved indications across multiple sleep disorder subtypes, all of which cluster together in the TxGNN knowledge graph, the model likely generated a high prediction score (99.85%) based on topological proximity to insomnia rather than a directional therapeutic signal. One Phase 4 trial (NCT00124384) did specifically enroll primary insomnia patients, though the study aim was to improve *daytime functioning* when modafinil was added to cognitive behavioral therapy — not to treat nighttime sleep difficulties directly.

**Critical mechanistic concern:** There is a fundamental paradox at the core of this prediction. Insomnia is characterised by unwanted wakefulness and difficulty maintaining sleep, and effective treatment requires agents that facilitate sleep onset or maintenance. Modafinil, however, *promotes* wakefulness — and is itself classified as a drug that can *cause* insomnia as an adverse effect. This prediction almost certainly reflects a knowledge-graph false positive: graph proximity to sleep disorder nodes does not capture the directionality of pharmacological action. This prediction should be interpreted with extreme caution and does not constitute a credible repurposing candidate without additional mechanistic justification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | **Modafinil** alone or combined with CBT-I in primary insomnia; primary goal was improving daytime functioning, with secondary assessment of insomnia severity — does not constitute an insomnia treatment trial |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | CBT-I ± armodafinil for insomnia and fatigue in breast cancer survivors post-chemotherapy; four-arm design; armodafinil intended to counter cancer-related fatigue, not as a direct sleep aid |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | CBT-I ± armodafinil in cancer survivors with insomnia and fatigue after chemotherapy; same rationale as NCT01091974 — larger companion study |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot study of BBT-I ± armodafinil 150 mg/day in breast cancer patients with insomnia; preliminary design, limited power |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Armodafinil and/or CBT-I for insomnia comorbid with obstructive sleep apnea; assessed sleep continuity and CPAP adherence — small sample, no Phase designation |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Phase 2 | Completed | 830 | RECOVER-SLEEP platform: multi-intervention evaluation for sleep disturbances in Long COVID (PASC); specific interventions per appendix, modafinil role unclear from summary |
| [NCT06404099](https://clinicaltrials.gov/study/NCT06404099) | Phase 2 | Active, not recruiting | 361 | RECOVER-SLEEP platform: ongoing evaluation of interventions for PASC sleep disturbances; results pending |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Completed | 18 | **Modafinil** for circadian and cognitive dysfunction in stable bipolar disorder; sleep measured as secondary endpoint — very small sample (n=18) |
| [NCT00233090](https://clinicaltrials.gov/study/NCT00233090) | Phase 2 | Terminated | 21 | **Modafinil** vs. placebo for post-TBI fatigue; terminated early — insufficient evidence |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | **Modafinil** for sleep/wake disturbances in older adults; terminated after enrolling only 2 participants — no conclusions possible |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-based review | *Drugs* | Comprehensive RCT-based review of approved and investigational modafinil uses; confirms wake-promoting profile across narcolepsy, OSA, SWSD, and fatigue states — no support for primary insomnia treatment |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic review / Meta-analysis | *PLoS One* | Modafinil significantly reduces fatigue and excessive daytime sleepiness in multiple neurological disorders; confirms unidirectional wake-promoting effect |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Cochrane-style systematic review | *Parkinsonism & Related Disorders* | Modafinil improves daytime sleepiness in Parkinson's disease; does not address insomnia as a treatment target |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | EBM guideline review | *Movement Disorders* | MDS evidence-based review of non-motor Parkinson's treatments; modafinil recommended for excessive daytime sleepiness — not for insomnia |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Narrative review | *Expert Opinion on Pharmacotherapy* | Pharmacological and non-pharmacological management of sleep disturbances in Parkinson's disease; modafinil discussed for sleepiness, not insomnia |
| [15824337](https://pubmed.ncbi.nlm.nih.gov/15824337/) | 2005 | RCT | *Neurology* | Modafinil for fatigue in multiple sclerosis; confirms wake-promoting effect — insomnia not an endpoint |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | RCT | *J Head Trauma Rehabilitation* | Modafinil for fatigue and excessive daytime sleepiness in chronic TBI; no insomnia-specific endpoint |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | *Drugs* | Shift work sleep disorder: burden and management; modafinil reduces EDS in SWSD — directionality opposite to insomnia therapy |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | *Revue Neurologique* | Narcolepsy with cataplexy; sleep maintenance insomnia noted as a narcolepsy symptom, but modafinil's role targets daytime sleepiness, not nocturnal sleep |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | *Expert Opinion on Emerging Drugs* | Emerging treatments for narcolepsy; modafinil reviewed as the primary daytime EDS pharmacotherapy — not applicable to insomnia |

---

## Italy Market Information

Modafinil has **no marketing authorizations** currently registered in Italy. No license or approved indication data is available for this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction presents a fundamental mechanistic paradox — modafinil is a wake-promoting agent whose core pharmacology runs directly counter to the goal of insomnia therapy, and no completed RCT has demonstrated modafinil efficacy as a primary insomnia treatment. The high prediction score (99.85%) most likely reflects a knowledge-graph false positive arising from modafinil's broad presence in the sleep disorder disease space, not a genuine therapeutic signal.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis explaining how a wake-promoting agent could benefit insomnia (e.g., daytime wake consolidation improving nocturnal sleep architecture via homeostatic sleep pressure)
- Retrieval of full EMA/AIFA package insert data (warnings, contraindications, drug interactions) before any further regulatory or clinical planning
- Targeted mechanistic or preclinical study examining bidirectional sleep-wake effects of modafinil, particularly effects on nighttime sleep architecture (polysomnography)
- If a plausible hypothesis emerges, a small Phase 2 proof-of-concept trial in primary insomnia with objective PSG-based endpoints would be required before any repurposing pathway can be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

