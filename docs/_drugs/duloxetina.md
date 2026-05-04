---
layout: default
title: Duloxetina
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Duloxetina
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

# DULOXETINA: Evaluation Suspended – Incomplete Evidence Pack

## One-Sentence Summary

Duloxetina (Duloxetine) is an internationally recognized serotonin-norepinephrine reuptake inhibitor (SNRI), approved in multiple countries for major depressive disorder, generalized anxiety disorder, and neuropathic pain.
However, this Evidence Pack contains **no TxGNN-predicted new indications**, **no Italy regulatory records**, and **no safety data**, making a standard drug repurposing evaluation impossible at this stage.
A corrected re-query with the proper DrugBank identifier is required before any evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Italy regulatory database |
| Predicted New Indication | None (TxGNN predictions absent) |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Are No Predictions Available?

Duloxetina returned zero results from the Italy (AIFA) regulatory database, and the Evidence Pack carries no DrugBank ID. Without a valid DrugBank node, the TxGNN knowledge graph pipeline cannot map the drug to any disease node and therefore produces no predicted indications.

This is almost certainly a **data linkage problem**, not a genuine absence of repurposing potential. Duloxetine is a well-characterized compound with an established mechanism (dual inhibition of the serotonin transporter SERT and the norepinephrine transporter NET) and an active research portfolio covering cancer-related neuropathic pain, stress urinary incontinence, fibromyalgia, and chemotherapy-induced peripheral neuropathy, among others.

The most likely root causes are: (1) the INN spelling "DULOXETINA" not matching the AIFA database entry (which may index under "duloxetina" with lower-case, or by brand names **Cymbalta** / **Xeristar**), and (2) the absence of a DrugBank ID preventing TxGNN from running. Correcting these two points should unlock both the MOA data and the full prediction set.

---

## Italy Market Information

No authorizations were found in the Italy regulatory database for the query term **"DULOXETINA"**.

> **Note:** Duloxetine is commercially available in Italy under the brand names **Cymbalta** and **Xeristar**. The zero-result query likely reflects a spelling mismatch or search-scope limitation in the automated pipeline rather than actual market absence. A manual AIFA search using the brand name or the lowercase INN "duloxetina" is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted indications, no AIFA regulatory records, and no safety warnings — none of the minimum data required for a Level-1 to Level-5 evidence assessment is present. Proceeding to evaluation would produce a structurally empty report with no actionable content.

**To proceed, the following is needed:**

- **Resolve DrugBank ID:** Duloxetine's likely identifier is **DB00476**; confirm and re-inject into the pipeline.
- **Re-query AIFA:** Use lowercase "duloxetina" and/or brand names "Cymbalta" / "Xeristar" to retrieve existing Italy market authorizations and approved indications.
- **Re-run TxGNN:** With a valid DrugBank ID, re-execute the knowledge-graph prediction step to generate ranked predicted indications.
- **Retrieve package insert:** Download the AIFA/TFDA package insert PDF to populate key warnings, contraindications, and DDI data.
- **Resubmit a complete Evidence Pack:** Once the above gaps are resolved, regenerate the Evidence Pack and return for a full evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

