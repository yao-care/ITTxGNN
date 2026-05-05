---
layout: default
title: Verapamil
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Verapamil: From Cardiac Arrhythmia / Hypertension to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is a well-established L-type calcium channel blocker (CCB) used clinically for supraventricular tachycardia, angina pectoris, and hypertension; no formal Italy (AIFA) authorization records were found in this dataset.
The TxGNN model's top prediction links it to **Obsolete Bundle Branch Block** — a retired SNOMED/OMOP clinical concept — with **no clinical trials** and **no supporting publications** identified.
⚠️ This prediction warrants particular caution: the disease label is no longer in active clinical use, and Verapamil is pharmacologically regarded as contraindicated in bundle branch block due to the risk of inducing complete heart block.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cardiac arrhythmia, hypertension, angina pectoris (based on established pharmacological knowledge; no AIFA license records found in dataset) |
| Predicted New Indication | Obsolete Bundle Branch Block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed (no AIFA records found) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Verapamil belongs to the phenylalkylamine class of L-type voltage-gated calcium channel blockers. By blocking calcium entry into cardiac and smooth muscle cells, it slows conduction through the atrioventricular (AV) node, reduces heart rate and contractility, and dilates peripheral vasculature. These properties underpin its established clinical roles in supraventricular tachycardia (rate control), atrial fibrillation, stable angina, and hypertension. Detailed MOA data was not recoverable from the data pipeline for this report (flagged as data gap DG002), but Verapamil's cardiac electrophysiological profile is well characterised in the literature.

At surface level, the mechanistic link to bundle branch block (BBB) exists — Verapamil acts on cardiac conduction tissue, which is the anatomical substrate of BBB. However, this relationship is one of **pharmacological risk, not therapeutic benefit**: slowing AV nodal conduction in a patient with pre-existing BBB risks progression to complete (third-degree) heart block, a life-threatening condition. Clinical guidelines therefore list BBB — especially bifascicular or trifascicular block — as a contraindication or high-risk caution for Verapamil use.

A further critical issue undermines this prediction entirely: the disease label carries an "**obsolete**" prefix, indicating that this concept has been formally retired from the SNOMED CT / OMOP CDM ontology. The TxGNN knowledge graph likely retains this legacy node, which may explain the high model score. In practice, "obsolete bundle branch block" no longer corresponds to any active diagnostic category, and clinical translation of this prediction is not meaningful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

No AIFA authorizations for Verapamil were identified in this dataset. The drug is recorded as **not marketed** in Italy under the queried records (0 licenses, data as of 2026-03-29).

> **Note:** Verapamil (marketed globally as Isoptin®, Calan®, Veramil®, and generics) has regulatory approvals in many countries for arrhythmia, angina, and hypertension. A targeted AIFA database re-query is recommended to confirm the Italian market status before any formulary or licensing assessment is finalized.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical note derived from mechanistic analysis:** Across all 7 predicted indications in this Evidence Pack, the `repurposing_rationale` explicitly identifies mechanistic concerns for at least 4 predictions:
> - **Rank 1 (Obsolete Bundle Branch Block):** Verapamil is relatively contraindicated — risk of complete heart block.
> - **Rank 4 & 5 (Pulmonary Hypertension, Groups 3 & 5):** CCBs are not recommended in Group 3/5 PH; may worsen ventilation-perfusion mismatch in Group 3.
> - **Rank 2 (Malignant Renovascular Hypertension):** CCB monotherapy is less effective than RAAS inhibitors in the context of renal artery stenosis.
>
> Full warnings and contraindications should be verified against the package insert once obtained via TFDA/AIFA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction targets a retired ontology concept with no active clinical relevance; the mechanistic relationship between Verapamil and bundle branch block is one of contraindication rather than therapeutic opportunity. No clinical trials or supporting literature were identified for any of the 7 predicted indications, and all predictions carry the lowest evidence grade (L5) with unanimous "Hold" or equivalent recommendations.

**To proceed, the following is needed:**

- **Resolve Italy market status:** Conduct a direct AIFA database query to confirm whether Verapamil holds any Italian authorizations — the current dataset returned zero records, which may reflect a query limitation rather than a genuine absence from the Italian market.
- **Obtain full MOA data:** Query the DrugBank API to fill data gap DG002 and enable proper mechanistic analysis across indications.
- **Update disease ontology mapping:** Re-run TxGNN with a current SNOMED CT / OMOP CDM mapping to exclude retired ("obsolete") disease nodes from candidate outputs and improve prediction signal quality.
- **Explore rank 7 as a research hypothesis:** "Periodic paralysis with transient compartment-like syndrome" (rank 7) carries the only "Research Question" recommendation and the strongest plausible mechanistic hypothesis (VGCC mutations, Andersen-Tawil syndrome overlap). This is the only candidate in this report that merits a targeted literature deep-dive before formal hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

