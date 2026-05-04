---
layout: default
title: Clorpromazina
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
---

# Clorpromazina
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

# Clorpromazina: Repurposing Evaluation Incomplete — TxGNN Predictions Not Available

## One-Sentence Summary

Clorpromazina (chlorpromazine) is a first-generation phenothiazine antipsychotic with established use in psychiatric conditions.
However, this Evidence Pack contains **no TxGNN-predicted new indications** and is missing critical fields — original indications, mechanism of action, and safety data — making a full repurposing evaluation impossible at this time.
The data pipeline has confirmed that DrugBank and package insert sources each returned one result, but their content was not yet integrated into the Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | None — TxGNN predictions not populated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Clorpromazina is critically incomplete — without TxGNN predictions, original indications, mechanism of action, or safety data, no repurposing hypothesis can be formed or evaluated.

**To proceed, the following is needed:**

- **TxGNN model output** — `predicted_indications` array is empty; the model must be run or results loaded for this drug before any evaluation can begin
- **Original approved indications** — `original_indications` is empty; retrieve from AIFA database or package insert
- **Mechanism of action** — DrugBank query returned 1 result on 2026-03-29 but the data was not integrated into `drug.original_moa`; extract and populate
- **Safety information** — Package insert query returned 1 result on 2026-03-29 but `key_warnings` and `contraindications` remain unpopulated; parse and integrate
- **Drug interaction data** — DDI query returned no results; consider querying an alternative DDI database (e.g., DrugBank interactions, Drugs.com)
- **Italy market verification** — Confirm whether Clorpromazina holds any AIFA authorizations; 0 licenses is unexpected for a compound in this class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

