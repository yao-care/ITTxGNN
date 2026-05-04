---
layout: default
title: Alizapride
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 0
---

# Alizapride
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

# Alizapride: Drug Repurposing Evaluation Report

## One-Sentence Summary

Alizapride is a benzamide-derivative dopamine antagonist antiemetic (DrugBank ID: DB01425), not currently marketed in Taiwan.
The TxGNN model has **no predicted new indications** for this drug at present,
and the evidence pack contains **0 clinical trials** and **0 publications** to support any repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no TFDA-approved indications on record) |
| Predicted New Indication | None — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack. Based on known pharmacological information, Alizapride is a substituted benzamide that acts as a dopamine D₂ receptor antagonist. It is used in some countries (primarily in Europe) as an antiemetic for the management of nausea and vomiting, including chemotherapy-induced and postoperative nausea.

However, **no TxGNN-predicted new indications were generated** for Alizapride. The `predicted_indications` array is empty, meaning the graph neural network model did not identify any high-confidence repurposing candidates for this compound at the current data cutoff (2026-04-03).

Without a predicted indication, a mechanistic plausibility analysis cannot be performed. Further data enrichment — particularly the drug's MOA details from DrugBank and regulatory label information — may enable future prediction runs to yield actionable results.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Alizapride has **no TFDA marketing authorizations** in Taiwan. There are no registered licenses, product names, or approved dosage forms on record.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: TFDA package insert data, key warnings, contraindications, and drug–drug interaction data were all queried but returned no results for Alizapride. This is consistent with the drug not being marketed in Taiwan.

---

## Data Gaps Summary

The following critical data gaps were identified in this evidence pack:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot proceed to S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications exist for Alizapride, the drug is not marketed in Taiwan (0 authorizations), and critical safety data (warnings, contraindications) is entirely missing. There is insufficient evidence to support any repurposing evaluation at this time.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: Obtain TFDA package insert warnings and contraindications, or source equivalent safety data from EMA/FDA databases since the drug is marketed in Europe
- Resolve **DG002 (High)**: Retrieve detailed MOA data from DrugBank API to enable mechanistic analysis
- Re-run TxGNN prediction pipeline after enriching the drug's knowledge graph representation with MOA, target, and pathway data
- Evaluate whether Alizapride's dopamine D₂ antagonist profile yields viable repurposing candidates in a subsequent prediction cycle
- Consider sourcing regulatory and clinical data from EMA (European Medicines Agency), as Alizapride has market presence in select European countries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

