---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Dorzolamide
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

# Dorzolamide: Evaluation Incomplete — No TxGNN Predictions Available

## One-Sentence Summary

Dorzolamide (DrugBank: DB00869) is a carbonic anhydrase inhibitor with established ophthalmic use (glaucoma / ocular hypertension); however, the current Evidence Pack contains **no TxGNN-predicted new indications**, no Taiwan regulatory approvals, and multiple blocking data gaps — a full repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not provided in Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no predictions or supporting studies in pack |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Evaluation Cannot Proceed

The Evidence Pack for Dorzolamide was built from a single data source (`drugbank`) and is missing two critical inputs:

**No TxGNN output.** The `predicted_indications` array is empty. Without at least one predicted indication, there is no repurposing hypothesis to evaluate — the entire downstream analysis (mechanism rationale, clinical trial search, literature review) has no anchor.

**Mechanism of action unavailable.** The `original_moa` field is flagged as a data gap (`DG002`, severity: High). Dorzolamide is known from the literature to be a topical carbonic anhydrase inhibitor that reduces aqueous humor production, but this has not been captured in the Evidence Pack and therefore cannot be formally cited for mechanistic reasoning.

**Safety data unavailable.** Both `key_warnings` and `contraindications` returned `[Data Gap]` (`DG001`, severity: Blocking). Per the evaluation protocol this blocks entry into the safety screening stage (S1).

---

## Data Gap Summary

| Gap ID | Item | Severity | Remediation |
|--------|------|----------|-------------|
| DG001 | TFDA package insert warnings / contraindications | Blocking | Download package insert PDF from TFDA website and parse |
| DG002 | Mechanism of action (MOA) | High | Query DrugBank API for DB00869 |
| — | TxGNN predicted indications | Blocking | Re-run TxGNN inference pipeline for Dorzolamide |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing the TxGNN prediction output that defines the repurposing hypothesis, and blocking safety data gaps prevent entry into the initial safety screening stage. There is currently no evaluable candidate to assess.

**To proceed, the following is needed:**

- **Re-run TxGNN inference** for Dorzolamide (DB00869) and populate `predicted_indications` with at least one ranked candidate disease
- **Resolve DG001** — retrieve and parse the TFDA (or AIFA) package insert to extract key warnings, contraindications, and special population precautions
- **Resolve DG002** — query DrugBank API to retrieve the full mechanism of action entry for DB00869
- **Confirm market status** — verify whether Dorzolamide (e.g., Trusopt®) holds any active authorizations in the target market, as zero licences currently listed may reflect a query gap rather than true absence
- **Re-generate Evidence Pack (v5)** once the above inputs are available and resubmit for full evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

