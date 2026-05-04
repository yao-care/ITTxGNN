---
layout: default
title: Eletriptan
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 4
---

# Eletriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Eletriptan: Drug Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Eletriptan is a selective serotonin 5-HT1B/1D receptor agonist belonging to the triptan class, used for the acute treatment of migraine with or without aura.
The current Evidence Pack contains **no TxGNN model predictions** for new indications, and the drug is **not marketed in Taiwan** with zero approved authorizations.
Evaluation cannot proceed until TxGNN prediction data and safety information are supplemented.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine — acute treatment (triptan class) |
| Predicted New Indication | N/A — No TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

No TxGNN predicted indications are present in this Evidence Pack, so mechanistic plausibility analysis for a new indication cannot be performed at this stage.

For context, Eletriptan belongs to the triptan class and acts as a selective agonist at serotonin 5-HT1B and 5-HT1D receptors. This dual-receptor mechanism produces selective cranial vasoconstriction and inhibits the presynaptic release of vasoactive neuropeptides — including CGRP and substance P — thereby interrupting the trigeminovascular cascade responsible for migraine pain. Detailed MOA data has been flagged as a data gap (DG002: High severity) and requires formal retrieval from DrugBank before any mechanistic bridge to a new indication can be assessed.

Once TxGNN model predictions are generated, the analysis should focus on whether 5-HT1 receptor signalling or CGRP-pathway modulation overlaps with the disease biology of any candidate indication. The serotonergic system has documented involvement in mood disorders, cluster headache, and certain pain syndromes, which may provide plausible mechanistic anchors — but this remains speculative until prediction data are available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted new indication is available to search against.

---

## Literature Evidence

Currently no related literature available — no predicted new indication is available to search against.

---

## Taiwan Market Information

Eletriptan has no approved authorizations in Taiwan. No license records are available for display.

> Note: Eletriptan (brand name Relpax, Pfizer) is approved in the EU, US, and several other markets for acute migraine treatment. A Taiwan regulatory filing has not been submitted or approved based on current TFDA data.

---

## Safety Considerations

Safety data including key warnings and contraindications are currently unavailable due to data gaps identified during the Evidence Pack build:

- **DG001 (Blocking):** TFDA package insert warnings and contraindications — required for S1 safety screening; must be retrieved from the TFDA website before evaluation can advance.
- **DG002 (High):** Mechanism of action detail — required for mechanistic plausibility analysis; must be retrieved from DrugBank.
- **DDI query:** Returned no results (query status: not found).

Please refer to the international package insert (SmPC / USPI) for interim safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Eletriptan is critically incomplete — the `predicted_indications` array is empty and two blocking/high-severity data gaps prevent safety screening and mechanistic analysis from proceeding. There is no actionable repurposing signal to evaluate at this time.

**To proceed, the following is needed:**

- **TxGNN model predictions** must be generated for Eletriptan (`predicted_indications` is currently empty — the pipeline may not have processed DB00216)
- **MOA data** from DrugBank (DG002 — High): needed for mechanistic plausibility analysis
- **Safety data** from TFDA package insert (DG001 — Blocking): key warnings and contraindications required before S1 safety screening
- **DDI database re-query**: the current not-found result may reflect a query issue; interaction data for a 5-HT1 agonist is clinically relevant (especially with MAOIs, SSRIs, and other triptans)
- **Regulatory pathway scoping**: if Taiwan market entry is a goal, a full new drug application (NDA) would be required given zero existing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

