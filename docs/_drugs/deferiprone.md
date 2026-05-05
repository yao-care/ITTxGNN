---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Deferiprone: Iron Overload Drug — Repurposing Evaluation (Insufficient Data)

## One-Sentence Summary

Deferiprone (DB08826) is a known iron chelator historically used to treat transfusional iron overload in patients with thalassemia syndromes.
However, the current Evidence Pack contains **no TxGNN-predicted new indications** and **no Taiwan market authorizations**, making a standard repurposing evaluation impossible at this stage.
Multiple critical data gaps — including missing MOA documentation, package insert warnings, and contraindications — must be resolved before any repurposing pathway can be assessed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron overload (thalassemia; not formally captured in this Evidence Pack) |
| Predicted New Indication | None — TxGNN predictions not available in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction unavailable; no supporting studies retrievable) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The Evidence Pack for Deferiprone was constructed from DrugBank data only (`inputs_received: ["drugbank"]`). Two blocking or high-severity data gaps directly prevent prediction and analysis:

1. **Missing Taiwan package insert warnings and contraindications (DG001 — Blocking):** Without this document, the safety pre-screening step (S1) cannot begin. The remediation path is to download the relevant package insert PDF from the TFDA official website and parse it.

2. **Missing mechanism of action data (DG002 — High):** Without a confirmed MOA, the mechanistic plausibility linking Deferiprone's pharmacology to any new target indication cannot be assessed. DrugBank API query should retrieve this.

Until both gaps are resolved, TxGNN scoring for this candidate cannot be trusted or interpreted.

---

## Taiwan Market Information

No product authorizations for Deferiprone were found in the Taiwan (TFDA) database as of the data cutoff (2026-04-20). The drug is currently **not marketed** in Taiwan.

> If marketing authorization data exists in other jurisdictions (e.g., EMA/FDA approval for Ferriprox), it should be retrieved separately and incorporated into a revised Evidence Pack.

---

## Safety Considerations

Safety data could not be retrieved for this evaluation. Please refer to the official package insert (obtainable from TFDA or EMA) for full warnings, contraindications, and drug interaction information before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is incomplete in two blocking dimensions — no TxGNN predictions were generated, and critical safety documentation (package insert) is absent — making it impossible to evaluate repurposing feasibility or patient safety at this time.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Download and parse the Deferiprone package insert from the TFDA website to extract approved warnings and contraindications; this unblocks the S1 safety pre-screening step
- **[DG002 — High]** Query the DrugBank API for Deferiprone's confirmed mechanism of action (iron chelation pathway, target proteins) to enable mechanistic plausibility analysis
- **Re-run the TxGNN pipeline** after data gaps are resolved so that a ranked list of predicted new indications is generated
- **Expand regulatory data inputs** to include EMA/FDA authorization records (Deferiprone/Ferriprox holds approvals outside Taiwan that may inform the repurposing context)
- Once predictions are available, **re-generate this report** using the full Evidence Pack (v5+)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

