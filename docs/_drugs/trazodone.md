---
layout: default
title: Trazodone
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Trazodone
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

The `txgnn-pipeline` skill focuses on pipeline operations (training, validation, deployment), not report writing — my current task is governed by the system prompt's report format. I'll proceed directly to generating the evaluation report.

---

# Trazodone: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Trazodone is an atypical antidepressant that has been FDA-approved for the treatment of Major Depressive Disorder, working primarily through serotonergic mechanisms.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **0 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (FDA-approved; not registered in Italy) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available from DrugBank. However, based on the published literature, trazodone is an atypical antidepressant with two key pharmacological actions: (1) inhibition of serotonin (5-HT) reuptake, and (2) antagonism at 5-HT2A/2C receptors. These dual serotonergic effects form the theoretical foundation for its potential use in OCD.

OCD is understood to involve dysregulation of serotonin neurotransmission, and the current first-line pharmacotherapy — SSRIs and clomipramine — work precisely through the serotonin system. Trazodone shares this serotonergic profile, though its affinity for the 5-HT transporter is lower than that of typical SSRIs, which may limit its potency relative to standard OCD treatments. Notably, a 1987 neuroimaging study (PMID 3501130) found that trazodone's treatment response in OCD patients correlated with measurable shifts in caudate nucleus glucose metabolism measured by PET — providing rare neurobiological evidence for a mechanistic link.

The mechanistic overlap is therefore genuine, if partial. Trazodone may be particularly useful in OCD patients who are clomipramine-resistant, in those with comorbid depression and insomnia (where trazodone's H1-antagonist sedating properties provide additional benefit), or as an augmentation strategy. The evidence is modest and dates primarily from the late 1980s–1990s, which means modern controlled trials are lacking — but the biological rationale is well-grounded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | Journal of Clinical Psychopharmacology | Double-blind, placebo-controlled study of trazodone in OCD patients; investigated antiobsessive efficacy in a controlled setting |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacology Bulletin | Reviews mono- and polypharmacotherapy of OCD; OCD responds exclusively to SRIs; trazodone discussed in augmentation context |
| [8134850](https://pubmed.ncbi.nlm.nih.gov/8134850/) | 1994 | Review | Southern Medical Journal | Pharmacologic management of OCD; serotonin/dopamine dysregulation hypothesis; serotonergic agents including trazodone reviewed |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgraduate Medicine | Comprehensive review of trazodone's mechanism, formulations, and off-label uses including OCD, insomnia, and anxiety disorders |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Review | The Journal of Clinical Psychiatry | Biological approaches to treatment-resistant OCD; serotonin-augmentation strategies reviewed; trazodone referenced in open-label reports |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Open-label study | Clinical Neuropharmacology | Trazodone in 9 clomipramine-resistant OCD patients; whole-group showed significant mild improvement; 3 patients responded very favorably with relapse on withdrawal |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Neuroimaging study | Psychopathology | Treatment response to trazodone (±MAOI) correlated with shifts in caudate nucleus glucose metabolism by PET; neurobiological mechanism support |
| [29343875](https://pubmed.ncbi.nlm.nih.gov/29343875/) | 2017 | Case report | Rivista di Psichiatria | Trazodone prolonged-release in bipolar II/OCD comorbidity; simultaneously managed depressive and obsessive-compulsive symptoms |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case report | The Journal of Nervous and Mental Disease | Two severe OCD + depression patients unresponsive to multiple antidepressants achieved rapid and impressive improvement with trazodone |
| [6703152](https://pubmed.ncbi.nlm.nih.gov/6703152/) | 1984 | Case series | The American Journal of Psychiatry | Early clinical observation documenting trazodone use in OCD patients |

---

## Italy Market Information

Trazodone is not currently marketed in Italy. No marketing authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN assigns a near-perfect prediction score (99.95%), and the serotonergic mechanism of trazodone provides a credible biological basis for OCD treatment. A double-blind, placebo-controlled RCT (PMID 1629380) and an open-label study in clomipramine-resistant patients (PMID 2119885) provide Level 2 evidence, though the trials are small and dated (1990s). The absence of any registered modern clinical trial and Italy's zero-authorization status mean this should be treated as a research-stage hypothesis, not a clinical recommendation.

**To proceed, the following is needed:**
- Retrieve full text and results of the 1992 RCT (PMID 1629380) to assess effect size, sample size, and outcome measures
- Obtain trazodone's full mechanism of action data from DrugBank to strengthen the mechanistic rationale
- Obtain Italy package insert warnings and contraindications (currently a blocking data gap)
- Clarify the drug interaction profile, particularly with other serotonergic agents used in OCD (clomipramine, fluoxetine, fluvoxamine)
- Consider designing or identifying an ongoing Phase 2/3 trial in treatment-resistant OCD as the most efficient path to upgrade evidence from L2 to L1
- Evaluate whether the prolonged-release formulation (referenced in PMID 29343875) offers a more favorable tolerability profile for OCD patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

