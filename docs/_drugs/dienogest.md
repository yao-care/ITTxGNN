---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# DIENOGEST: Repurposing Candidate — Insufficient Data for Full Evaluation

## One-Sentence Summary

Dienogest (DrugBank DB09123) is a synthetic progestogen; however, the current Evidence Pack contains no original indication records from the regulatory database and **no TxGNN-predicted new indications**, making a standard repurposing evaluation impossible at this stage. Critical data gaps in mechanism of action, safety warnings, and regulatory history must be resolved before any evidence-based conclusion can be drawn.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Taiwan regulatory records found) |
| Predicted New Indication | Not available (TxGNN predictions not yet generated) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — Model prediction not yet run; no supporting studies retrievable |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indication is available in this Evidence Pack (`predicted_indications: []`). Without a target disease, a mechanistic rationale cannot be constructed.

Currently, detailed mechanism of action data is also not available. Based on DrugBank record DB09123, Dienogest is classified as a progestogen (fourth-generation synthetic progestin). Its pharmacological activity is mediated through progesterone receptor agonism, and it is widely used in European and Asian markets for endometriosis and hormonal contraception — though none of these indications appear in the Taiwan regulatory database queried.

**To proceed with this section**, the TxGNN prediction pipeline must first be run and a target disease must be confirmed before any mechanistic bridge can be evaluated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this Evidence Pack. This is because no predicted indication has been identified; once a target disease is confirmed, a ClinicalTrials.gov query can be executed.

---

## Literature Evidence

Currently no related literature available. Target indication must be specified before a PubMed query can yield meaningful results.

---

## Taiwan Market Information

No authorizations found. The TFDA query (2026-03-29) returned 0 records for DIENOGEST.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction data was found in the DDI database query (2026-03-29). TFDA package insert parsing was recorded as successful (query ID 4), but extracted warning and contraindication fields are unavailable in this Evidence Pack version.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Dienogest is missing all three elements required for a repurposing evaluation: a TxGNN-predicted target indication, mechanism of action data, and safety/regulatory content. There is no basis on which to assess efficacy plausibility, evidence strength, or risk profile at this time.

**To proceed, the following is needed:**

1. **Run TxGNN prediction pipeline** — Generate ranked candidate indications for DB09123 so a target disease can be selected
2. **Retrieve MOA from DrugBank API** — Populate `original_moa` to enable mechanistic rationale (Data Gap DG002, severity: High)
3. **Download and parse TFDA package insert PDF** — Extract warnings and contraindications to unblock the safety evaluation (Data Gap DG001, severity: Blocking)
4. **Confirm original indication** — Query DrugBank or WHO INN records to populate `original_indications` (currently empty)
5. **Re-run Evidence Pack generation** (target version: v5) — Once gaps above are resolved, resubmit for a complete L1–L5 evidence grading and Go/Hold/Proceed recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

