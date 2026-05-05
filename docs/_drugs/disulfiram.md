---
layout: default
title: Disulfiram
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
---

# Disulfiram
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

# Disulfiram: Alcohol Use Disorder — Repurposing Evaluation (Incomplete Data)

## One-Sentence Summary

Disulfiram is an aldehyde dehydrogenase inhibitor historically used as an alcohol deterrent for alcohol use disorder (AUD). This Evidence Pack contains **no TxGNN repurposing predictions** — the `predicted_indications` array is empty — and key safety and mechanistic data are absent due to unresolved data gaps. **A full repurposing evaluation cannot be completed until the TxGNN pipeline output and package insert data are obtained.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alcohol Use Disorder (general knowledge; not populated in Evidence Pack) |
| Predicted New Indication | Not available — `predicted_indications` is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | Undetermined (no prediction output) |
| Italy Market Status | ✗ Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predictions are present in this Evidence Pack, so no evidence-based mechanistic rationale for a new indication can be provided at this stage.

Disulfiram is broadly known as an ALDH (aldehyde dehydrogenase) inhibitor that causes aversive acetaldehyde accumulation upon alcohol ingestion. Outside of AUD, exploratory research has examined its copper-chelating and proteasome-inhibiting properties in oncology contexts — but these directions are **not the subject of this report**, as no formal TxGNN prediction has been generated to guide the evaluation.

Detailed mechanism of action data is also flagged as a high-severity data gap (DG002) and must be retrieved from DrugBank before any repurposing mechanistic analysis can be conducted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — `predicted_indications` data is empty and no target indication has been identified.

---

## Literature Evidence

Currently no related literature available — `predicted_indications` data is empty and no target indication has been identified.

---

## Italy Market Information

Disulfiram has no approved product authorizations in Italy. The regulatory query returned 0 results — this drug is not currently marketed in Italy.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Although the TFDA package insert query (`tfda_package_insert`) returned a success status with 1 result, the structured safety fields (warnings, contraindications) were not parsed into the Evidence Pack. DDI query also returned no results. All three safety data categories require follow-up before any clinical safety assessment is possible.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is missing the three minimum inputs required for a repurposing evaluation: TxGNN prediction output, mechanism of action data, and structured safety information. Proceeding without these would produce an unsupported recommendation.

**To proceed, the following is needed:**

1. **Run TxGNN pipeline for Disulfiram** — generate `predicted_indications` with scores, trial links, and literature references; without this the report has no target indication to evaluate
2. **Parse TFDA package insert content** (DG001, Blocking) — the query returned a result but structured safety data was not extracted; warnings and contraindications must be populated before any safety screening
3. **Retrieve MOA from DrugBank API** (DG002, High) — the DrugBank query returned a result but MOA remains unpopulated; this is required for mechanistic plausibility analysis
4. **Supplement DDI data from an alternative source** — current DDI query returned `not_found`; consult DrugBank DDI database or MICROMEDEX to rule out interaction risks
5. **Check EMA / FDA databases for approved indications** — since Italy has 0 authorizations, international regulatory labels may provide the approved indication context needed for the report header
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

