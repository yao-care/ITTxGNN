---
layout: default
title: Amisulpride
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 0
---

# Amisulpride
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

# AMISULPRIDE: Drug Repurposing Evaluation — Awaiting Prediction Data

## One-Sentence Summary

Amisulpride (DrugBank: DB06288) is a benzamide derivative known internationally as an atypical antipsychotic.
The current Evidence Pack contains **no TxGNN predicted indications**, and critical data gaps remain in mechanism of action and regulatory safety information.
This report documents the current status and outlines the steps needed before a repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Amisulpride |
| DrugBank ID | DB06288 |
| Original Indication | Not available in current data |
| Predicted New Indication | **None** — TxGNN predictions not yet generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions or supporting studies available) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations (TFDA) | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

> **No TxGNN predicted indication is available for evaluation at this time.**

Currently, detailed mechanism of action (MOA) data has not been retrieved for Amisulpride in this Evidence Pack. Based on publicly known information, Amisulpride is a selective dopamine D₂/D₃ receptor antagonist belonging to the benzamide class of atypical antipsychotics. It is widely used internationally for the treatment of schizophrenia (both positive and negative symptoms) and has also been investigated for other psychiatric conditions.

However, since the `predicted_indications` array is empty, no mechanistic bridging analysis between an original indication and a new predicted indication can be performed. The MOA data gap (DG002) further limits the ability to assess any future predictions in the context of target–disease relationships.

---

## Clinical Trial Evidence

Currently no related clinical trials are available — TxGNN has not yet generated predicted indications for this drug.

---

## Literature Evidence

Currently no related literature is available — without a predicted indication, no targeted literature search has been conducted.

---

## Taiwan Market Information

Amisulpride currently holds **no TFDA marketing authorizations** in Taiwan (market status: 未上市). No license records are available.

---

## Safety Considerations

> Please refer to the package insert for safety information.

All safety fields (key warnings, contraindications, and drug–drug interactions) returned as data gaps or not found in the current Evidence Pack. The following blocking data gaps have been identified:

- **DG001 (Blocking):** TFDA package insert warnings and contraindications have not been retrieved. This must be resolved before any Stage 1 safety assessment can proceed.
- **DG002 (High):** Mechanism of action data is missing from DrugBank, impacting mechanistic relevance analysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications exist for Amisulpride in this Evidence Pack, and critical data gaps (MOA, TFDA safety labelling) prevent meaningful evaluation. The drug is also not currently marketed in Taiwan, adding regulatory complexity to any repurposing pathway.

**To proceed, the following is needed:**

1. **Generate TxGNN predictions** — Run the TxGNN model for Amisulpride (DB06288) to obtain candidate repurposing indications with confidence scores
2. **Resolve DG001 (Blocking)** — Retrieve TFDA package insert warnings and contraindications (source: TFDA website, method: download and parse package insert PDF)
3. **Resolve DG002 (High)** — Retrieve detailed MOA data from DrugBank API to enable mechanistic bridging analysis
4. **Conduct evidence search** — Once a predicted indication is available, perform clinical trial (ClinicalTrials.gov) and literature (PubMed) searches for the drug–indication pair
5. **Re-evaluate market pathway** — Since Amisulpride is not marketed in Taiwan, assess whether an import/special access pathway or new drug application would be required for any repurposed indication

---

*This report was generated on 2026-04-03. Data cutoff: 2026-04-03. Results are for research purposes only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

