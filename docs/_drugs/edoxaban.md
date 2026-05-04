---
layout: default
title: Edoxaban
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 0
---

# Edoxaban
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

# EDOXABAN (DB09075): Drug Repurposing Evaluation — Insufficient Data to Proceed

## One-Sentence Summary

EDOXABAN is a small molecule drug (DrugBank: DB09075) that is currently not marketed in Taiwan, with no original indication data captured in this Evidence Pack.
The TxGNN model returned **no predicted indications** for this candidate, making a substantive repurposing evaluation impossible at this stage.
All critical data layers — mechanism of action, safety warnings, and model output — remain outstanding and must be resolved before this candidate can advance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Evaluation Is Possible at This Stage

The Evidence Pack for EDOXABAN is missing three foundational data layers required before any repurposing analysis can proceed:

**1. No TxGNN output.** The `predicted_indications` array is empty. Without a scored candidate indication from the graph neural network, there is no repurposing hypothesis to evaluate. This is the central input for the entire pipeline.

**2. No mechanism of action.** The `original_moa` field is flagged as a data gap (severity: High). Without understanding how EDOXABAN exerts its pharmacological effect, it is impossible to assess whether any mechanistic bridge to a new indication is plausible.

**3. No original indication confirmed.** The `original_indications` array is empty. While EDOXABAN is publicly known to be a direct Factor Xa inhibitor used for anticoagulation (atrial fibrillation, DVT/PE), this information has not been validated from a regulatory source (TFDA package insert) in the current pipeline run and therefore cannot be used as a formal input.

Until these three gaps are closed, the evaluation framework cannot advance beyond data collection.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: A TFDA package insert query was attempted on 2026-03-29 and returned a result (`result_status: success`), but the parsed content was not loaded into the safety fields of this Evidence Pack. The remediation step — parsing the downloaded PDF — appears incomplete.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
EDOXABAN has no TxGNN-predicted indications and no validated original indication or MOA data in the current Evidence Pack. There is no repurposing hypothesis to evaluate, assess mechanistically, or support with clinical evidence.

**To proceed, all of the following must be resolved:**

- **[Blocking]** Run the TxGNN prediction pipeline for EDOXABAN (DB09075) to generate scored candidate indications
- **[Blocking]** Parse the TFDA package insert PDF already retrieved (query log ID 4) to extract original indications, key warnings, and contraindications
- **[High]** Query DrugBank API for mechanism of action (MOA) — DrugBank record confirmed to exist (query log ID 3, 1 result found)
- **[High]** Re-run the Evidence Pack generation after the above inputs are available to produce a substantive L1–L5 evaluation

> The DrugBank record and TFDA package insert are already confirmed to exist. Resolving this candidate does not require new data sourcing — it requires completing the parsing and pipeline steps already initiated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

