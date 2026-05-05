---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 3
---

# Febuxostat
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

Using the `txgnn-pipeline` skill as context. Now generating the evaluation report based on the Evidence Pack.

---

# Febuxostat: From Hyperuricemia (Gout) to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is an established xanthine oxidase inhibitor approved globally for managing hyperuricemia in adult patients with gout.
The TxGNN model predicts it may be effective for **Renal Hypouricemia (hypouricemia, renal)**,
with **1 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperuricemia in adult patients with gout |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, febuxostat is a non-purine selective inhibitor of xanthine oxidase (XO) — the enzyme that converts hypoxanthine → xanthine → uric acid. By blocking XO, febuxostat reduces uric acid biosynthesis, which is the basis of its efficacy in gout. This mechanistic class is distinct from allopurinol (a purine analogue) because febuxostat binds a different site on XO with higher selectivity.

Renal hypouricemia (RHUC) is caused by loss-of-function mutations in uric acid transporters (primarily URAT1/SLC22A12), resulting in excessive renal uric acid excretion and abnormally low serum urate. Despite low serum uric acid, RHUC patients face a serious complication: exercise-induced acute kidney injury (EIAKI). The proposed mechanism is that during intense anaerobic exercise, XO produces a burst of reactive oxygen species (ROS) and xanthine within renal tubules, causing acute oxidative tubular damage — independent of serum uric acid levels.

This is where febuxostat's XO inhibition becomes relevant in a novel context: rather than lowering serum uric acid (already low in RHUC), febuxostat may prevent EIAKI by suppressing the renal tubular ROS surge triggered by exercise. PMID 36754409 describes precisely this case — a 16-year-old athlete with familial RHUC and recurrent EIAKI in whom febuxostat was used as prophylaxis after standard hydration failed. This mechanistic pivot (systemic urate-lowering → renal tubular oxidative protection) provides a plausible biological rationale for the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study examining effects of uric acid control on kidney stone recurrence and renal function in patients with hyperuricemia and urolithiasis (Shanghai Xu-hui Central Hospital, 2020–2022) |

> **Note:** This trial focuses on hyperuricemia with stone disease, not renal hypouricemia specifically. Its relevance to RHUC is indirect — it provides evidence on febuxostat's renal effects but does not target the RHUC population.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case Report | Internal Medicine (Tokyo) | Febuxostat used as prophylaxis for recurrent EIAKI in a 16-year-old football player with familial RHUC (URAT1 compound heterozygous mutation); standard hydration had failed — supports XO inhibition as a preventive mechanism in RHUC-associated EIAKI |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia for practicing rheumatologists; covers etiology (renal vs. non-renal), clinical presentations, and management; establishes disease context and clinical framework for RHUC |

---

## Taiwan Market Information

Febuxostat currently holds **no marketing authorizations** in Taiwan (0 licenses on record). There are no approved products, dosage forms, or local indications to display.

> Febuxostat is approved in other markets under brand names such as **Uloric** (USA) and **Adenuric** (EU/Japan) for gout-related hyperuricemia, but has not received TFDA approval to date.

---

## Safety Considerations

Safety data from the Taiwan package insert and drug interaction database were not retrievable for this evidence pack. Please refer to the package insert and current prescribing information for warnings, contraindications, and drug interactions.

> **Clinician note:** In international markets, febuxostat carries a regulatory warning regarding increased risk of cardiovascular mortality compared to allopurinol (based on the CARES trial). This should be considered when evaluating patient suitability, pending local safety data retrieval.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between XO inhibition and EIAKI prevention in RHUC patients is biologically plausible and supported by a published case report, but the overall evidence base remains limited to a single case and a narrative review — insufficient for clinical implementation without further prospective data.

**To proceed, the following is needed:**

- **MOA documentation**: Query DrugBank API (DB04854) to formally populate mechanism of action data
- **Taiwan safety data**: Retrieve TFDA package insert (warnings, contraindications, DDI profile) — currently flagged as Blocking gap
- **Prospective clinical evidence**: Pilot RCT or prospective cohort study evaluating febuxostat for EIAKI prevention specifically in RHUC patients
- **Cardiovascular risk assessment**: Review CARES trial data and confirm cardiovascular risk profile is acceptable for the RHUC population (typically young athletes)
- **Dose optimization**: Establish appropriate febuxostat dosing for EIAKI prophylaxis, which may differ from standard gout dosing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

