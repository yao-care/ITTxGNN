---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Eftrenonacog Alfa: From Haemophilia B — No TxGNN Prediction Available

## One-Sentence Summary

Eftrenonacog alfa (brand name: Alprolix) is a recombinant coagulation Factor IX Fc fusion protein indicated for the prevention and treatment of bleeding episodes in Haemophilia B (congenital Factor IX deficiency).
The current Evidence Pack contains **no TxGNN-predicted new indications** for this drug, and no original indication data was retrieved from the regulatory source.
Without a predicted target indication, this candidate **cannot proceed to standard repurposing evaluation** at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia B (congenital Factor IX deficiency) — from background knowledge; not retrieved in this Evidence Pack |
| Predicted New Indication | — (No prediction returned by TxGNN) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (Model prediction only — and none available) |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No warning, contraindication, or drug interaction data was returned in this Evidence Pack. The TFDA package insert query returned a result (`result_count: 1`), but its contents were not parsed into the structured fields. DrugBank was queried successfully, however MOA and safety fields remain unpopulated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Eftrenonacog Alfa is critically incomplete — the `predicted_indications` array is empty, meaning TxGNN returned no candidate repurposing targets, and key structured fields (original indications, MOA, safety warnings, contraindications) are all absent. There is no basis on which to evaluate mechanistic plausibility, evidence strength, or safety for any new indication.

**To proceed, the following is needed:**

- **Re-run TxGNN inference** for DB11608 and confirm whether an empty prediction list reflects a genuine null result or a pipeline failure
- **Resolve DG001 (Blocking):** Parse the TFDA/AIFA package insert PDF to extract warnings and contraindications — this data is available (`result_count: 1`) but was not ingested into the structured pack
- **Resolve DG002 (High):** Query DrugBank API for MOA, pharmacodynamics, and drug categories to enable mechanistic analysis
- **Populate `original_indications`:** Confirm regulatory indication text from AIFA/TFDA label (known clinically as Haemophilia B prophylaxis and on-demand treatment)
- **Re-generate Evidence Pack v5** after all blocking data gaps are resolved before re-evaluating this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

