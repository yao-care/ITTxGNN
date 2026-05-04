---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: Repurposing Evaluation Cannot Proceed — Evidence Pack Incomplete

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor (5-ARI), broadly approved internationally for benign prostatic hyperplasia (BPH) and androgenetic alopecia, but currently not marketed in Taiwan.
This Evidence Pack contains **no TxGNN-predicted new indications**, and critical data including mechanism of action and safety warnings are missing.
A complete repurposing evaluation cannot be conducted until the identified data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign prostatic hyperplasia (BPH) *(from general pharmaceutical knowledge; not supplied in Evidence Pack)* |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no supporting studies provided in this pack |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indication is included in this Evidence Pack, so a mechanistic bridge between original and new indication cannot be drawn at this time.

Mechanism of action data is also absent from the Evidence Pack. Based on general pharmacological knowledge, dutasteride irreversibly inhibits both Type 1 and Type 2 isoforms of 5α-reductase, blocking the peripheral conversion of testosterone to dihydrotestosterone (DHT). This androgenic suppression underpins its efficacy in BPH and hair-loss indications and has motivated investigational use in prostate cancer prevention (e.g., the REDUCE trial). However, without a specific predicted indication to evaluate, the relevance of this mechanism to any new target cannot be formally assessed here.

This section will be completed once TxGNN prediction output (candidate_id: `TW-DB01126-multi`) is retrieved and appended to the Evidence Pack.

---

## Clinical Trial Evidence

Currently no predicted indication is available in this Evidence Pack; clinical trial evidence cannot be scoped or listed.

---

## Literature Evidence

Currently no predicted indication is available in this Evidence Pack; literature evidence cannot be scoped or listed.

---

## Taiwan Market Information

Dutasteride is **not currently marketed in Taiwan**. No TFDA licenses are on record (TFDA query returned 0 results on 2026-03-29).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not retrieved in this Evidence Pack.

> **Data Gap Notice:** TFDA package insert warnings/contraindications (DG001, severity: Blocking) and DrugBank MOA/safety data (DG002, severity: High) are both outstanding. Until DG001 is resolved, the candidate cannot advance past the S1 safety screening gate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for dutasteride is structurally incomplete — there are no TxGNN predictions to evaluate and two blocking-level data gaps remain unresolved, preventing any meaningful safety or mechanistic analysis.

**To proceed, the following is needed:**

1. **[Blocking] Retrieve TxGNN prediction results** — candidate_id `TW-DB01126-multi` should include at least one predicted indication; confirm whether the prediction pipeline was executed and why output is absent
2. **[Blocking] Download and parse the TFDA package insert PDF** (DG001) — extract key warnings, contraindications, and dosing restrictions to enable S1 safety screening
3. **[High] Retrieve MOA and DrugBank structured data** (DG002) — DrugBank query returned 1 result on 2026-03-29 but MOA was not populated; re-fetch and parse the pharmacodynamics field
4. **[Medium] Confirm original approved indications** — `original_indications` array is empty; cross-reference TFDA, EMA, or FDA labeling to populate this field before proceeding to indication-mapping analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

