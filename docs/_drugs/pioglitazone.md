---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 9
---

# Pioglitazone
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

Using `txgnn-pipeline` to confirm context. The skill confirms this is a TxGNN multi-country drug repurposing report task. Now generating the evaluation report from the provided Evidence Pack.

---

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (TZD) class PPARγ agonist widely used for treating Type 2 Diabetes Mellitus by improving peripheral insulin sensitivity.
The TxGNN model's top-ranked prediction places it as a potential candidate for **Opsismodysplasia**, a rare and severe skeletal dysplasia caused by *INPPL1* (SHIP2) gene mutations.
This prediction is currently supported by **0 clinical trials** and **0 publications**, and the mechanistic rationale raises significant concerns about biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrieved from the regulatory package insert for this report. Based on established pharmacology, pioglitazone is a selective **PPARγ (Peroxisome Proliferator-Activated Receptor gamma) agonist** in the thiazolidinedione class. PPARγ activation reshapes gene transcription programs in adipose tissue, skeletal muscle, and the liver, ultimately reducing insulin resistance. This is also the basis of all nine literature records identified for pioglitazone in the system — all address Type 2 Diabetes and related metabolic conditions, with no direct connection to skeletal disease.

Opsismodysplasia is caused by loss-of-function mutations in *INPPL1*, encoding the phosphatase SHIP2. SHIP2 modulates the PI3K/Akt signalling axis, which is essential for normal chondrocyte differentiation and endochondral ossification. While pioglitazone does interact indirectly with PI3K/Akt downstream targets through PPARγ, the connection is mechanistically problematic rather than supportive: PPARγ activation is well-documented to **suppress** osteoblast differentiation by antagonising the RUNX2 and Wnt/β-catenin pathways — the very transcription programs required for proper bone formation.

In a condition already characterised by severely impaired skeletal mineralisation, PPARγ agonism could plausibly worsen rather than improve the pathophysiology. The TxGNN model's high confidence score (99.59%) most likely reflects shared network topology with metabolic or signalling neighbours in the knowledge graph, rather than validated mechanistic relevance for this rare skeletal indication. Overall biological plausibility is assessed as **low to negative**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Pioglitazone holds no marketing authorizations in Italy. No approved products or indication records are available from the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on a model prediction (Evidence Level L5) with zero supporting clinical trials or published literature. More critically, current mechanistic analysis suggests PPARγ agonism may be counterproductive in opsismodysplasia — a skeletal disorder where osteoblast and chondrocyte function is already impaired — making this a low-plausibility repurposing hypothesis regardless of the high TxGNN score.

**To proceed, the following is needed:**
- Preclinical studies (in vitro/in vivo) examining the effect of PPARγ modulation in *INPPL1*/*SHIP2*-deficient chondrocyte or skeletal tissue models
- Mechanistic clarification of whether any PPARγ-independent actions of pioglitazone (e.g., anti-inflammatory, mitochondrial effects) could offer any partial benefit in this disease context
- Formal MOA and safety data retrieval: DrugBank API query for full pharmacology, and AIFA/package insert review for warnings, contraindications, and known drug interactions
- Reassessment of lower-ranked TxGNN predictions (e.g., Ranks 5–8: lipodystrophy subtypes) which carry stronger mechanistic rationale via PPARγ's role as the master regulator of adipogenesis, and may represent more viable repurposing candidates for priority follow-up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

