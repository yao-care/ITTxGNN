---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: Drug Repurposing Evaluation — Pending Indication Data

## One-Sentence Summary

Dronedarone (DrugBank ID: DB04855) is a candidate drug entered into the TxGNN repurposing pipeline.
The current Evidence Pack contains **no TxGNN-predicted new indications** and no recorded original indications,
meaning a substantive repurposing assessment cannot be completed at this stage.
The two blocking data gaps — mechanism of action and package insert safety data — must be resolved before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model output pending |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline has not produced any predicted indications for Dronedarone in this Evidence Pack version (v4, data cutoff 2026-04-20), and the two data gaps flagged as High/Blocking severity prevent both mechanistic analysis and safety pre-screening. There is no basis on which to evaluate repurposing potential at this time.

**To proceed, the following is needed:**

- **\[DG001 — Blocking\]** Retrieve and parse the official package insert (PDF) to extract warnings and contraindications — required for safety pre-screening (S1 gate)
- **\[DG002 — High\]** Query DrugBank API for mechanism of action (MOA) — required for mechanistic plausibility analysis
- **Run TxGNN prediction** for Dronedarone (DB04855) to generate at least one ranked indication candidate before this report template can be meaningfully populated
- **Confirm original approved indication(s)** from TFDA or equivalent regulatory source (the `original_indications` field is currently empty)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

