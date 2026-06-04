---
layout: default
title: Propafenone
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 8
---

# Propafenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

The txgnn-pipeline skill is noted. This task is report generation from an Evidence Pack, so I'll proceed directly to produce the structured Markdown evaluation report.

---

# Propafenone: From Cardiac Arrhythmia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Propafenone is a Class IC antiarrhythmic agent used clinically to manage cardiac arrhythmias including atrial fibrillation and ventricular tachycardia.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **0 clinical trials** and **3 publications** in the dataset — however, these publications describe adverse events and drug interactions rather than any therapeutic use.
At this stage, this prediction is considered mechanistically implausible and the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cardiac Arrhythmia (Class IC Antiarrhythmic; no Italy regulatory record available) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, propafenone is a Class IC antiarrhythmic agent that primarily blocks cardiac sodium channels (Nav1.5). It also possesses mild beta-adrenergic blocking and weak calcium channel antagonist properties. Crucially, its CNS penetration is very low due to insufficient lipophilicity — and no known mood-stabilizing or anti-manic mechanism has been identified for this drug.

Cardiac arrhythmia and manic bipolar affective disorder are mechanistically unrelated conditions. The TxGNN model appears to have misidentified a co-occurrence signal in its knowledge graph: the available "supporting" literature describes propafenone *causing* mania as an adverse effect (PMID 2579063) and documents harmful interactions between cardiovascular drugs and antipsychotics (PMID 32124390) — not evidence of therapeutic benefit in bipolar disorder. This is a known failure mode in graph-based models, where causal direction between a drug node and disease node is not properly resolved.

In summary, this rank-1 prediction does not have a biologically plausible rationale. The model has conflated an adverse event relationship (propafenone → mania) with a therapeutic one. No additional investigation for this indication is recommended.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ **Important caveat**: The publications below do **not** support propafenone as a treatment for bipolar disorder. They document adverse events and drug interactions. They appear in this dataset because propafenone and bipolar disorder co-occur in a safety context, not a therapeutic one.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacological Reports | Evaluates harmful interactions between antipsychotics and cardiovascular medications; does not support propafenone as a treatment for bipolar disorder |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case Report | Int J Psychiatry in Medicine | Reports a case of organic psychosis resulting from a venlafaxine–propafenone drug interaction in a bipolar patient — this is an adverse event, not a therapeutic application |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case Report | J Clin Psychiatry | Describes mania induced by propafenone administration; notes chemical similarity to bupropion (antidepressant) as a possible mechanism of psychiatric side effects |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Summary of All Predicted Indications

For context, the following table summarises all 8 TxGNN-predicted indications and their evidence status:

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Manic Bipolar Affective Disorder | 99.80% | L5 | **Hold** — adverse event misread as therapeutic |
| 2 | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) | 99.79% | L3 | **Proceed with Guardrails** — direct RyR2 inhibition mechanism; 9 publications |
| 3 | Periodic Paralysis with Transient Compartment-like Syndrome | 99.67% | L5 | **Hold** — channel selectivity mismatch (Nav1.5 vs Nav1.4) |
| 4 | Prinzmetal Angina | 99.45% | L5 | **Hold** — Class IC agents may worsen ischaemia-related arrhythmia |
| 5 | Incessant Infant Ventricular Tachycardia | 99.44% | L3 | **Proceed with Guardrails** — paediatric use on record since 1987; 5 publications |
| 6 | Arrhythmogenic Right Ventricular Cardiomyopathy (ARVC) | 99.42% | L3 | **Research Question** — proarrhythmia risk in structural heart disease; 12 publications |
| 7 | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) | 99.23% | L5 | **Hold** — no mechanistic intersection |
| 8 | Trichotillomania | 99.17% | L5 | **Hold** — peripheral cardiac drug; negligible CNS penetration |

The **most scientifically compelling** repurposing candidate is **CPVT (Rank 2)**: propafenone directly inhibits RyR2 calcium release channels — the primary pathological driver in CPVT — while its Nav1.5 blockade and mild beta-blocking properties provide complementary suppression of triggered arrhythmias.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Rank 1: Manic Bipolar Affective Disorder)*

**Rationale:**
The TxGNN rank-1 prediction is mechanistically implausible. Propafenone's very low CNS penetration, absence of any mood-stabilizing pathway, and the fact that the only available literature documents propafenone *causing* psychiatric adverse effects collectively make this a clear false positive. The model appears to have reversed the causal direction of a known adverse drug reaction.

**To proceed with further evaluation:**
- **Do not pursue** manic bipolar affective disorder as a repurposing target for propafenone
- **Recommended pivot**: Initiate a full evidence synthesis for **CPVT (Rank 2)**, which has mechanistic grounding (RyR2 inhibition, PMID 21270101, 26121139), observational cohort support, and a long-term case report of 35-year successful treatment (PMID 30820400)
- **Obtain package insert / regulatory data**: Retrieve Italy (AIFA) and Taiwan (TFDA) prescribing information to fill the safety data gap before any clinical planning
- **Obtain formal MOA documentation**: Query DrugBank API for DB01182 to complete mechanism-of-action analysis
- **For ARVC (Rank 6)**: Commission a systematic safety review specifically examining Class IC proarrhythmia risk in structural heart disease before proceeding further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

