---
layout: default
title: Dulaglutide
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 0
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes — Repurposing Pipeline Data Insufficient

---

## One-Sentence Summary

Dulaglutide is a long-acting GLP-1 (glucagon-like peptide-1) receptor agonist, best known under the brand name Trulicity, originally developed and approved for the treatment of type 2 diabetes mellitus.
The current TxGNN pipeline run returned **no predicted new indications** for this drug — likely due to incomplete upstream data inputs rather than an absence of repurposing potential.
This report documents the state of available evidence and recommends targeted data remediation before proceeding with any repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus *(inferred from drug class; not captured in evidence pack)* |
| Predicted New Indication | Not available — pipeline returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Italy Market Status | Not found in regulatory query (0 licenses returned) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing candidates were generated in this pipeline run, so there is no model-driven indication to evaluate. However, it is worth documenting why dulaglutide is a pharmacologically compelling repurposing candidate in general, and why the empty result is most likely a pipeline artifact rather than a meaningful negative finding.

Dulaglutide is a long-acting GLP-1 receptor agonist. It mimics endogenous incretin signalling by stimulating insulin secretion in a glucose-dependent manner, suppressing glucagon release, slowing gastric emptying, and acting on hypothalamic satiety centres. Because GLP-1 receptors are widely expressed beyond the pancreas — in the cardiovascular system, liver, kidney, brain, and gut — the mechanistic basis for pleiotropic effects is well-established. The REWIND cardiovascular outcomes trial demonstrated a significant reduction in major adverse cardiovascular events (MACE), and emerging evidence supports investigation in obesity, non-alcoholic steatohepatitis (NASH/MASLD), chronic kidney disease, and neurodegenerative diseases such as Parkinson's.

The evidence pack is missing two critical inputs: the mechanism of action (MOA) field is marked as a data gap, and no Italian AIFA license data was retrieved. TxGNN relies on knowledge graph embeddings that incorporate drug targets and approved indication nodes. Without these anchor points, the model likely could not generate confident predictions — producing an empty result set by default rather than indicating dulaglutide has no repurposing value.

---

## Italy Market Information

The regulatory query returned **0 authorizations** and a "not marketed" status for dulaglutide in Italy. This result is almost certainly a data retrieval error. Dulaglutide (Trulicity®) received EMA marketing authorization in 2014 and is widely listed in the Italian Pharmaceutical Formulary (Lista di Trasparenza, AIFA). Likely causes of the null result include:

- Query used the INN "DULAGLUTIDE" while the AIFA database may index under the brand name "TRULICITY"
- Encoding or transliteration mismatch in the automated query

**Recommended action:** Re-run the AIFA query using "TRULICITY" as the search term and cross-reference the EPAR (European Public Assessment Report) via the EMA portal.

---

## Safety Considerations

Safety data was not retrieved in this pipeline run. Please refer to the package insert for complete safety information.

Based on the GLP-1 receptor agonist class profile, the following areas require investigation when completing the evidence pack:

- **Thyroid C-cell tumour risk**: Class-level warning based on rodent carcinogenicity data; contraindicated in patients with personal or family history of medullary thyroid carcinoma or MEN 2
- **Pancreatitis**: Cases of acute pancreatitis have been reported; discontinue if suspected
- **Hypoglycaemia**: Risk increases when combined with insulin secretagogues or insulin
- **Gastrointestinal effects**: Nausea, vomiting, diarrhoea — most common reasons for discontinuation
- **Heart rate**: Modest increase in resting heart rate observed across the class

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predicted indications because the evidence pack is missing critical drug-level inputs (MOA, drug targets, AIFA regulatory data, safety profile). The data gaps preclude both model inference and safety evaluation — this is a pipeline completeness issue, not a reflection of dulaglutide's actual repurposing potential.

**To proceed, the following is needed:**

- **Re-query DrugBank (DB09045)** to retrieve mechanism of action, protein targets (GLP-1R, etc.), and drug-drug interactions — the `DG002` gap must be resolved before TxGNN re-run
- **Re-query AIFA** using brand name "TRULICITY" to retrieve Italian marketing authorisation data and approved indications
- **Download and parse the EMA/AIFA package insert** (SmPC) to populate `key_warnings` and `contraindications` — required for the `DG001` blocking gap
- **Re-run TxGNN pipeline** with complete drug feature inputs; given dulaglutide's broad receptor expression profile, meaningful predicted indications are expected
- **Scope cardiovascular, metabolic, and neurological indication clusters** as priority review areas based on known GLP-1 receptor biology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

