---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# ALISKIREN: Drug Repurposing Candidate — Awaiting Prediction Data

## One-Sentence Summary

Aliskiren is a direct renin inhibitor originally developed for the treatment of hypertension. The TxGNN model has **not yet generated any predicted new indications** for this compound, and there are **no clinical trials or publications** linked to a repurposing hypothesis at this time. Significant data gaps remain in the evidence pack, preventing a meaningful repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (per known pharmacology; not listed in evidence pack) |
| Predicted New Indication | — None predicted |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction not yet available |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN prediction has been generated for Aliskiren, so there is no repurposing hypothesis to evaluate for mechanistic plausibility.

From general pharmacological knowledge, Aliskiren is the first-in-class direct renin inhibitor. It blocks the renin–angiotensin–aldosterone system (RAAS) at its most upstream point by binding to the active site of renin, thereby reducing the conversion of angiotensinogen to angiotensin I. This mechanism is well-established for blood pressure reduction and has been explored in cardiorenal protection contexts.

> **Note:** The evidence pack lists the mechanism of action as unavailable. The above description is based on published pharmacological literature. Once the DrugBank API query for MOA is completed (remediation item DG002), this section should be updated with the authoritative source data.

---

## Clinical Trial Evidence

Currently no predicted indication exists, therefore no related clinical trials can be mapped.

---

## Literature Evidence

Currently no predicted indication exists, therefore no related literature can be mapped.

---

## Taiwan Market Information

Aliskiren is **not marketed in Taiwan**. No TFDA licenses were found for this compound (query date: 2026-03-29). There are no locally approved products, dosage forms, or indications on record.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** TFDA package insert warnings and contraindications have not yet been parsed (data gap DG001, severity: Blocking). Drug–drug interaction data was also not found in the queried database. These gaps must be resolved before any safety assessment can proceed.

---

## Data Gaps Summary

The following critical data gaps were identified and must be resolved before this candidate can advance:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanism–indication relevance analysis | Query DrugBank API |
| — | TxGNN Predicted Indications | **Blocking** | No repurposing hypothesis to evaluate | Run TxGNN prediction pipeline for DB09026 |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN prediction has been generated for Aliskiren, meaning there is no drug repurposing hypothesis to evaluate. Additionally, the evidence pack contains blocking data gaps (TFDA safety data and MOA) that would prevent safety screening even if a prediction were available.

**To proceed, the following is needed:**
- Run the TxGNN prediction model for Aliskiren (DB09026) to generate candidate new indications
- Resolve DG001: Download and parse the TFDA package insert PDF to extract warnings and contraindications
- Resolve DG002: Query the DrugBank API to retrieve the detailed mechanism of action
- Re-assess Taiwan market status — confirm whether Aliskiren has ever been approved or if applications are pending
- Once predictions and safety data are available, re-generate the evidence pack and repeat this evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

