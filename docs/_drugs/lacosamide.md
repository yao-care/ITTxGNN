---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

The `txgnn-pipeline` skill confirms the context. Now I'll generate the full evaluation report based on the Evidence Pack.

---

# Lacosamide: From Focal Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide (Vimpat®) is an antiseizure medication approved for the treatment of focal (partial onset) epilepsy.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
with **1 clinical trial** and **14 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Focal epilepsy (partial onset seizures) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this evidence pack. Based on published literature, lacosamide is a third-generation antiseizure medication that works primarily by selectively enhancing the slow inactivation of voltage-gated sodium channels (Nav1.x), stabilizing hyperexcitable neuronal membranes and reducing repetitive neuronal firing. A secondary mechanism involves binding to collapsin response mediator protein 2 (CRMP2), which modulates ion channel trafficking and synaptic connectivity in limbic circuits.

The mechanistic rationale is strong: lamotrigine and carbamazepine — both sodium channel modulators in the same pharmacological class — are established first-line treatments for bipolar disorder. Lacosamide shares the Nav1.x modulation mechanism, suggesting a plausible mood-stabilizing pathway. Moreover, CRMP2 modulation may independently influence synaptic plasticity in limbic regions implicated in mood regulation, providing a second mechanistic bridge to affective disorders.

Clinically, the progression of evidence follows a coherent arc: observational studies first noted incidental improvements in depressive and anxious symptoms in epilepsy patients receiving lacosamide; a retrospective 30-day comparison study (PMID 30251375) and a 12-week open-label pilot trial (PMID 33666402) then directly examined lacosamide in bipolar disorder patients without epilepsy, both reporting positive signals; a Phase 3 RCT (NCT07412132) is now actively recruiting. **An important caveat:** existing clinical evidence primarily addresses **bipolar depressive episodes**, not manic episodes specifically — the disease-phase distinction is clinically critical and represents a gap in the current evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Randomized, double-blind, parallel-group trial evaluating lacosamide as augmentation to first- or second-line treatments in moderate-to-severe bipolar depressive episodes (Types I & II). Note: n=40 is substantially below typical Phase 3 standards (≥200); statistical power is a concern. NCT ID format is atypical and requires verification. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label Pilot Trial | J Clin Psychopharmacol | 12-week pilot study demonstrating efficacy and tolerability of lacosamide for bipolar depression — earliest prospective clinical signal |
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective Comparison | Psychiatry Clin Neurosci | 30-day comparison of lacosamide vs other antiepileptics in hospitalized BD patients without epilepsy; positive findings in a real-world psychiatric setting |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective Multicenter | Epilepsy Behav | Lacosamide improved depression and anxiety scores in focal refractory epilepsy patients; effects appear partly independent of seizure control, suggesting intrinsic psychotropic activity |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case Report | Acta Bio-Medica | Clinical mood stabilization with lacosamide in a patient with mood disorder, PTSD, and fronto-temporal epilepsy; discusses Nav slow-inactivation as a membrane-stabilizing mechanism in psychiatry |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Adverse Event Report | Indian J Psychol Med | ⚠️ Safety signal: lacosamide precipitated neutropenia in a BD patient with comorbid epilepsy — haematological monitoring indicated |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chem Neurosci | CRMP2 as a druggable neurological target; explains lacosamide's CRMP2-binding and its relevance to ion channel trafficking and limbic synaptic plasticity |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case Report | Cureus | Complex management of a pregnant BD Type I patient with comorbid epilepsy and PNES; demonstrates real-world use of lacosamide in psychiatric–neurological overlap |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | TDM 2018 update noting lacosamide's expanding clinical use beyond epilepsy, including pain and bipolar disorder |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | Structural Study | PNAS | Cryo-EM structures of human Nav1.7 bound to antiseizure drugs (riluzole, lamotrigine); provides mechanistic framework for how Nav-targeting AEDs achieve their shared pharmacological effects |
| [40777679](https://pubmed.ncbi.nlm.nih.gov/40777679/) | 2025 | Case Report | Cureus | Xylazine withdrawal in a patient with comorbid bipolar disorder; lacosamide used as part of management — illustrates BD–epilepsy clinical overlap context |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Literature-derived safety signal:** PMID 30275630 documents a case of lacosamide-precipitated **neutropenia** in a patient with bipolar disorder and comorbid epilepsy. Baseline and periodic haematological monitoring (CBC with differential) is advisable if lacosamide is used in psychiatric populations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lacosamide shares a mechanistic drug class with lamotrigine and carbamazepine — both established first-line bipolar disorder treatments — and preliminary clinical data from a retrospective study and a 12-week open-label pilot trial have demonstrated positive signals. An active Phase 3 RCT confirms growing clinical commitment to this hypothesis. However, the existing evidence base predominantly addresses **bipolar depressive episodes**, whereas the TxGNN-predicted indication is the **manic phase**, leaving a direct evidence gap for manic episode management.

**To proceed, the following is needed:**

- Completion and full publication of NCT07412132 Phase 3 results (with enrollment size adequacy review)
- Direct clinical evidence specifically for **manic episode** (not only depressive episode) efficacy
- Full mechanism of action documentation from DrugBank (DG002 data gap)
- Safety monitoring protocol including CBC with differential (neutropenia risk)
- Assessment of Taiwan regulatory pathway (TFDA) for off-label use or new indication application, given current zero-authorization status
- Head-to-head comparison design vs. established BD treatments (lithium, valproate, lamotrigine) to define competitive clinical positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

