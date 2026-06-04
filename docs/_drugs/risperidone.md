---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 6
---

# Risperidone
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

Using the `txgnn-pipeline` skill to confirm context — this is a multi-indication drug repurposing evaluation for the Italy (AIFA) TxGNN deployment. I'll now generate the report.

The Evidence Pack is rank-ordered by TxGNN score, but **rank 1 (gaze palsy) has L5 evidence / Hold status** while **rank 6 (major affective disorder) has L1 evidence / Proceed with Guardrails** — the highest actionable signal. The report focuses on the most clinically meaningful prediction per the spirit of the format.

---

# Risperidone: From Schizophrenia to Major Affective Disorder

## One-Sentence Summary

Risperidone is a second-generation atypical antipsychotic established in the treatment of schizophrenia and acute bipolar mania.
The TxGNN model — evaluated across 6 predicted indications in this multi-indication pack — identifies **Major Affective Disorder** (encompassing major depressive disorder and bipolar spectrum conditions) as the highest-evidence repurposing target,
supported by **37 clinical trials** and **20 publications**, including 5 systematic reviews and meta-analyses.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Bipolar Mania (established drug profile; no Italy authorizations on record) |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data from DrugBank was not captured in this evidence pack. However, Risperidone's pharmacology is extensively characterised in the published literature: it acts as a combined **D2 dopamine receptor** and **5-HT2A serotonin receptor antagonist**. D2 blockade provides antimanic and antipsychotic effects by dampening excess dopaminergic tone, while 5-HT2A antagonism disinhibits prefrontal serotonin transmission — a pathway directly linked to antidepressant augmentation. This dual receptor profile maps precisely onto the neurobiological substrate of major affective disorder.

Major affective disorder is pathophysiologically characterised by dysregulation of both dopaminergic and serotonergic circuits. Bipolar mania involves dopaminergic hyperactivity amenable to D2 antagonism, while treatment-resistant depression (TRD) often reflects insufficient serotonergic signalling that benefits from 5-HT2A-mediated disinhibition when Risperidone is added to an antidepressant. This mechanistic duality makes Risperidone uniquely positioned across the affective spectrum, as confirmed by the breadth of Phase 3 RCT evidence in this pack.

One important regulatory caveat must be flagged: Risperidone already holds FDA approval for acute bipolar mania and ASD-related irritability. The `original_indications: []` field in this evidence pack almost certainly reflects a data extraction gap rather than the absence of prior approvals. The TxGNN prediction therefore likely represents a mix of **existing indication confirmation** (bipolar mania) and **genuine repurposing** (TRD augmentation) — the boundary must be clarified with AIFA before this is classified as a novel repurposing application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Double-blind, placebo- and active-controlled RCT of Risperidone LAI monotherapy vs placebo (+ olanzapine comparator) for prevention of mood episode recurrence in Bipolar I disorder; largest and highest-powered trial in this dataset |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | TEAM Study — head-to-head comparison of lithium, valproate, and risperidone in children/adolescents with early-onset mania; landmark paediatric Phase 3 RCT |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Adjunctive risperidone vs placebo in MDD patients with sub-optimal antidepressant response; among the largest Phase 3 augmentation RCTs for treatment-resistant MDD |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Risperidone augmentation of SSRI monotherapy in TRD — includes long-term maintenance phase comparing risperidone vs placebo add-on to demonstrate durability of response |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Risperidone monotherapy vs placebo in ambulatory bipolar disorder with comorbid panic or generalised anxiety disorder; double-blind RCT evaluating single-agent efficacy |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Risperidone vs divalproex sodium in paediatric bipolar disorder with neuroimaging circuit assessment; tests equivalence hypothesis in children |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Risperidone augmentation in patients who failed or only partially responded to an adequate antidepressant trial; evaluates safety and efficacy in the partial-responder population |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Phase 4 | Completed | 60 | Risperidone monotherapy in ambulatory bipolar disorder with moderately severe anxiety; double-blind, placebo-controlled real-world efficacy data |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Phase 4 | Terminated | 45 | ECT combined with risperidone vs ECT alone for treatment-resistant depression; early termination limits conclusions, but provides preliminary MDD-specific augmentation signal |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Double-blind pilot comparing risperidone vs olanzapine as add-on to a failed SSRI in TRD; first direct head-to-head comparison of atypical antipsychotics in treatment-resistant depression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review & Network Meta-analysis | J Affect Disorders | Compared efficacy and discontinuation rates across augmentation agents for adult TRD using network meta-analysis; risperidone included as an active comparator |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review & Meta-analysis | J Psychopharmacology | Evaluated adjunctive and combination treatments for early-stage TRD; SGAs including risperidone assessed for response and remission benefit over antidepressant monotherapy |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Systematic Review & Meta-analysis | J Psychopharmacology | Compared antidepressants + SGAs vs esketamine vs lithium for MDD treatment; provides head-to-head tolerability and efficacy context for risperidone augmentation |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review & Meta-analysis | Psychological Medicine | Comprehensive meta-analysis of antipsychotics as both monotherapy and adjunctive therapy in MDD; risperidone efficacy and tolerability data pooled across multiple RCTs |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Systematic Review | Cochrane Database Syst Rev | Cochrane review of second-generation antipsychotics for MDD and dysthymia; foundational evidence synthesis showing risperidone as an effective antidepressant-augmenting agent |
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Ann Intern Med | Randomised trial of risperidone augmentation for treatment-refractory MDD published in Annals of Internal Medicine; demonstrated significant response benefit vs placebo add-on |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Population-based Study | J Clin Psychiatry | Nationwide population-based study evaluating real-world effectiveness of aripiprazole, olanzapine, quetiapine, and risperidone augmentation for MDD using national health insurance data |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Clinical Review | Ann Pharmacother | Reviewed efficacy and safety of risperidone augmentation in MDD patients failing antidepressant monotherapy; synthesises trial-level evidence to support clinical practice guidance |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Practice Review | Acta Psychiatr Scand | Evidence-based treatment algorithms for bipolar mania; reviews risperidone positioning alongside mood stabilisers with clinical management recommendations |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | Clinical Review | Expert Opin Pharmacother | Risperidone LAI as monotherapy and adjunctive therapy in Bipolar I maintenance; addresses long-term prophylaxis and treatment nonadherence with injectable formulation |

---

## Italy Market Information

Risperidone currently has **no registered authorizations on record in Italy (AIFA)**. No product names, dosage forms, or approved indications were returned in this evidence pack.

> ⚠️ **This result is anomalous.** Risperidone is a widely-used antipsychotic with regulatory approvals across the US, EU, Japan, and most major markets. A zero-authorization result almost certainly reflects a data extraction limitation rather than actual absence from the Italian market. **Direct verification via the AIFA online registry (farmaci.agenziafarmaco.gov.it) is mandatory before drawing any regulatory conclusions.**

---

## Safety Considerations

Please refer to the package insert for safety information.

> The drug interaction (DDI) database returned no results, and Italy-specific package insert warnings were not captured in this evidence pack. Based on Risperidone's established pharmacological profile, the following areas should be proactively addressed in any clinical protocol:
> - **Metabolic monitoring**: weight, fasting glucose, HbA1c, lipid panel (metabolic syndrome risk with long-term use)
> - **Neurological monitoring**: extrapyramidal symptoms (EPS), tardive dyskinesia (AIMS scale), akathisia
> - **Cardiovascular**: QTc prolongation baseline ECG and follow-up
> - **Endocrine**: hyperprolactinaemia (especially in women of reproductive age)
>
> Formal safety data retrieval from the EMA SmPC or AIFA-approved package insert is required before any clinical application proceeds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — including a 585-patient double-blind Bipolar I maintenance trial (NCT00391222), the TEAM Study in paediatric mania (NCT00057681, N=379), and a 630-patient TRD augmentation trial (NCT00095134) — combined with five systematic reviews/meta-analyses, constitute L1-grade evidence. Risperidone's D2/5-HT2A dual mechanism is directly aligned with the dopaminergic and serotonergic pathophysiology of major affective disorder, and the evidence base is sufficient to support moving to a formal feasibility and regulatory review stage.

**To proceed, the following is needed:**

- **Regulatory boundary clarification**: Confirm whether "Major Affective Disorder" partially overlaps with Risperidone's existing approved indications (bipolar mania, schizophrenia). Resolve the `original_indications: []` data gap before classifying this as a true repurposing vs. an indication-extension application — this distinction has significant regulatory and commercial implications
- **Italy AIFA market status verification**: The 0-authorization finding must be confirmed directly via the AIFA registry; existing EU approvals (EMA) may already cover the target indication
- **Safety data retrieval**: Obtain the EMA SmPC or AIFA-registered package insert to populate formal warnings, contraindications, and DDI profiles
- **Indication subgroup stratification**: The evidence quality differs by affective subtype — design separate analysis pathways for (a) Bipolar I maintenance, (b) MDD adjunctive/augmentation, and (c) TRD; do not pool these as a single development track
- **Monitoring protocol definition**: Establish baseline and follow-up monitoring schedule for metabolic parameters, EPS/tardive dyskinesia, QTc, and prolactin before any investigator-initiated trial submission
- **Secondary indication triage**: This multi-indication pack also flags **Trichotillomania** (L3, 10 publications, Research Question) and **Phelan-McDermid syndrome** (L4, preclinical zebrafish data + case reports) as candidates for future exploratory research after the major affective disorder track is resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

