---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog Alfa: Preliminary Assessment — No New Indications Predicted

## One-Sentence Summary

Albutrepenonacog alfa (DB13884) is a recombinant coagulation factor IX–albumin fusion protein, known internationally under the brand name Idelvion, used for the treatment and prophylaxis of **Hemophilia B**.
The TxGNN model has **not generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps that prevent a full evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (known: Hemophilia B) |
| Predicted New Indication | None — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

There are currently no TxGNN predictions for albutrepenonacog alfa, so no mechanistic plausibility assessment can be performed.

Based on publicly available information, albutrepenonacog alfa is a recombinant fusion protein that links human coagulation factor IX (FIX) with recombinant human albumin. The albumin moiety extends the half-life of FIX, allowing less frequent dosing. It restores the missing clotting factor in patients with Hemophilia B (congenital factor IX deficiency), enabling normal haemostasis.

Detailed mechanism of action data was not available in the evidence pack (flagged as Data Gap DG002). Without a TxGNN prediction or MOA data in the pack, no drug repurposing hypothesis can be evaluated at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered for any predicted new indication (no new indication was predicted by TxGNN).

## Literature Evidence

Currently no related literature available for any predicted new indication.

## Taiwan Market Information

Albutrepenonacog alfa has **no marketing authorizations** recorded with TFDA. The drug is classified as **not marketed** in Taiwan.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields (key warnings, contraindications, drug–drug interactions) returned as data gaps. The TFDA package insert query returned 1 result — this document should be retrieved and parsed to complete the safety profile (see Data Gap DG001).

## Data Gaps Requiring Resolution

The following critical data gaps were identified and must be addressed before any repurposing evaluation can proceed:

| Gap ID | Item | Severity | Impact | Recommended Remediation |
|--------|------|----------|--------|------------------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | **High** | Affects mechanistic relevance analysis | Query DrugBank API for full MOA data |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No new indications have been predicted by TxGNN for albutrepenonacog alfa. Additionally, the evidence pack contains blocking data gaps (TFDA package insert warnings) and high-severity gaps (MOA data) that preclude any meaningful repurposing assessment. The drug is not marketed in Taiwan, further limiting immediate applicability.

**To proceed, the following is needed:**
- TxGNN model predictions for this drug (currently the `predicted_indications` array is empty)
- Resolution of DG001: Retrieve and parse the TFDA package insert to extract warnings and contraindications
- Resolution of DG002: Query DrugBank API for detailed mechanism of action
- Confirmation of original approved indication(s) from regulatory source documents
- If the drug is not in the TxGNN knowledge graph, assess whether the molecular entity (recombinant FIX–albumin fusion) has sufficient representation in the training data to generate reliable predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

