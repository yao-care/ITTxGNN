---
layout: default
title: Apomorfina
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 0
---

# Apomorfina
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

# APOMORFINA: Initial Drug Repurposing Assessment

## One-Sentence Summary

Apomorfina (Apomorphine) is a dopamine agonist known internationally for the treatment of Parkinson's disease motor fluctuations. The TxGNN model has **no predicted new indications** for this drug at present, and the evidence pack contains significant data gaps that prevent a full evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset |
| Predicted New Indication | None (no TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only, insufficient data |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Apomorfina (Apomorphine) is a non-selective dopamine agonist acting on both D1 and D2 receptor subtypes. It is used internationally as a rescue therapy for acute "off" episodes in advanced Parkinson's disease, typically administered via subcutaneous injection or sublingual film.

However, the TxGNN model has not generated any predicted new indications for this compound. This may be due to incomplete knowledge-graph mapping, the absence of a DrugBank ID linkage, or insufficient network connectivity in the prediction model. Without a predicted indication, no mechanistic plausibility analysis can be performed at this time.

## Clinical Trial Evidence

No TxGNN-predicted indications are available; therefore, no targeted clinical trial search was conducted for repurposing candidates.

## Literature Evidence

No TxGNN-predicted indications are available; therefore, no targeted literature search was conducted for repurposing candidates.

## Taiwan Market Information

Apomorfina currently holds **no valid marketing authorizations** from the TFDA. The drug is classified as **not marketed (未上市)** in Taiwan.

## Safety Considerations

> Please refer to the package insert for safety information. No TFDA label warnings, contraindications, or drug-drug interaction data were available for this compound in the current dataset.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for Apomorfina contains critical data gaps — no DrugBank ID linkage, no original indication data, no mechanism of action, no TFDA authorization, and most importantly, **no TxGNN-predicted new indications**. Without a candidate repurposing indication, no evaluation can proceed.

**To proceed, the following is needed:**
- **Resolve DrugBank linkage** — Confirm the DrugBank ID for Apomorphine (likely DB00714) and re-run the knowledge graph mapping
- **Re-run TxGNN prediction** — With correct DrugBank linkage, regenerate predicted indications
- **Obtain MOA data** — Query DrugBank API for detailed mechanism of action (dopamine D1/D2 agonism)
- **Clarify regulatory scope** — If Taiwan marketing is not planned, consider whether another country's regulatory dataset (e.g., EMA, FDA) should be used as reference
- **TFDA package insert analysis** — The query log indicates a successful package insert retrieval (query #4, result_count=1); this data should be parsed and integrated into the next version of the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

