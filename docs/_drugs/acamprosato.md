---
layout: default
title: Acamprosato
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# Acamprosato
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

# Acamprosato: Drug Repurposing Evaluation Report

## One-Sentence Summary

Acamprosato (Acamprosate) is a medication historically used for the maintenance of abstinence in alcohol-dependent patients, though no original indications are recorded in the current evidence pack. No new indications have been predicted by the TxGNN model at this time, and no clinical trial or literature evidence is available to support repurposing. **This candidate cannot proceed to evaluation until critical data gaps are resolved.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications recorded) |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No model prediction or supporting studies available) |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN prediction has been generated for Acamprosato, so a mechanistic plausibility assessment cannot be performed.

Detailed mechanism of action (MOA) data is not available in the evidence pack. Based on publicly known information, Acamprosate is believed to modulate glutamatergic neurotransmission, primarily acting on NMDA receptors and potentially restoring the balance between excitatory and inhibitory neurotransmission disrupted by chronic alcohol exposure. Its established clinical use is in supporting abstinence from alcohol in alcohol-dependent patients who have already undergone detoxification.

Without a predicted new indication from TxGNN, it is not possible to evaluate the mechanistic relationship between the original use and any potential repurposed indication. This report should be revisited once TxGNN predictions become available and the MOA data gap (DG002) is resolved via DrugBank.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any predicted new indication — no TxGNN prediction has been generated for this drug.

---

## Literature Evidence

Currently no related literature available — no TxGNN prediction has been generated for this drug.

---

## Italy Market Information

Acamprosato is currently **not marketed** in Italy. No AIFA authorizations were found in the regulatory database (0 licenses on record).

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** The following critical data gaps were identified:
> - **TFDA package insert warnings/contraindications** (Severity: Blocking) — cannot complete Stage 1 safety assessment without this data. Remediation: download and parse the package insert PDF from the TFDA website.
> - **Drug-drug interactions**: No interactions found in the database query (query date: 2026-03-29).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications have been generated for Acamprosato, and the drug is not marketed in Italy. Multiple blocking data gaps — including mechanism of action and package insert safety data — prevent any meaningful repurposing evaluation at this time.

**To proceed, the following is needed:**
- Run TxGNN prediction pipeline for Acamprosato to generate candidate new indications
- Resolve **DG002**: Obtain detailed mechanism of action data via DrugBank API query
- Resolve **DG001**: Download and parse the official package insert PDF from the TFDA website to extract warnings, contraindications, and safety information
- Clarify the DrugBank ID (currently `null`) to enable cross-referencing with drug databases
- Confirm original approved indications from authoritative regulatory sources (AIFA, EMA, or equivalent)
- Re-evaluate once the above data is available and TxGNN predictions are generated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

