---
layout: default
title: Amitriptilina
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 0
---

# Amitriptilina
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amitriptyline (AMITRIPTILINA): Drug Repurposing Evaluation Report

## One-Sentence Summary

Amitriptyline (AMITRIPTILINA) is a well-known tricyclic antidepressant widely used for depression, neuropathic pain, and migraine prophylaxis. The TxGNN model did **not generate any predicted new indications** for this compound in the current analysis cycle. Significant data gaps remain, including mechanism of action details, regulatory safety information, and market authorization data for Italy.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug (INN) | AMITRIPTILINA (Amitriptyline) |
| DrugBank ID | Not available |
| Original Indication | Not recorded in evidence pack (known: depression, neuropathic pain) |
| Predicted New Indication | **None** — no indications predicted by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — No predictions and no supporting studies in this pack |
| Italy Market Status | ❌ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There is **no TxGNN prediction to evaluate** for Amitriptyline in this analysis cycle. The predicted indications list is empty, meaning the model either did not process this drug or did not identify indications meeting the confidence threshold.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Amitriptyline is a tricyclic antidepressant (TCA) that primarily inhibits the reuptake of serotonin and norepinephrine. It also has anticholinergic, antihistaminic, and sodium channel–blocking properties, which account for its broad clinical utility in depression, neuropathic pain, migraine prophylaxis, and functional gastrointestinal disorders. However, none of this mechanistic rationale can be linked to a new predicted indication because no prediction was generated.

Before a meaningful evaluation can be performed, the TxGNN prediction pipeline should be re-run for Amitriptyline to determine if any repurposing candidates emerge. The drug's rich polypharmacology makes it a plausible candidate for multi-target repurposing once data gaps are resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack — no predicted indication was available to query against.

---

## Literature Evidence

Currently no related literature available in this evidence pack — no predicted indication was available to query against.

---

## Italy Market Information

No marketing authorizations recorded. Amitriptyline does not appear to hold current AIFA-approved licenses in the dataset reviewed (0 licenses found).

---

## Safety Considerations

> Please refer to the package insert for safety information.

All safety fields (key warnings, contraindications, drug-drug interactions) returned no data in the current evidence pack. The DDI query returned `not_found` with 0 interactions. This represents a **Blocking** data gap (DG001) that must be resolved before any Stage 1 safety assessment can proceed.

---

## Data Gaps Summary

The following critical gaps were identified and should be addressed before re-evaluation:

| Gap ID | Category | Item | Severity | Remediation |
|--------|----------|------|----------|-------------|
| DG001 | Drug Level | Package insert warnings / contraindications | **Blocking** | Download and parse package insert PDF from regulatory authority website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Query DrugBank API (note: DrugBank ID is currently missing) |
| — | Prediction | TxGNN predicted indications | **Blocking** | Re-run TxGNN prediction pipeline for Amitriptyline |
| — | Drug Level | DrugBank ID | High | Resolve DrugBank mapping (DB00321 is the known ID for Amitriptyline) |
| — | Regulatory | Italy market authorization data | Medium | Query AIFA database directly |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN prediction was generated for Amitriptyline, and multiple blocking data gaps (safety information, MOA, regulatory data) prevent any meaningful repurposing evaluation. The evidence pack is essentially empty across all key dimensions.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping** — Amitriptyline's known DrugBank ID is DB00321; linking this would unlock MOA, toxicity, and interaction data
- **Re-run TxGNN prediction pipeline** with corrected drug identifier to generate candidate indications
- **Obtain AIFA / regulatory safety data** — download and parse the package insert to fill the blocking DG001 gap
- **Re-query DDI databases** once DrugBank ID is properly linked
- **Re-generate evidence pack** after the above gaps are filled, then re-evaluate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

