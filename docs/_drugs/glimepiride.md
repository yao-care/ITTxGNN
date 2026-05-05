---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

Using `txgnn-pipeline` skill noted — it covers pipeline management. For report generation, the system prompt format governs. Proceeding to produce the report now.

---

# Glimepiride: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a third-generation sulfonylurea antidiabetic agent, widely used to treat Type 2 Diabetes Mellitus by stimulating pancreatic insulin secretion. The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, yet there are currently **0 clinical trials** and **0 publications** supporting this direction — leaving this prediction at the lowest possible evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (based on drug class; no Taiwan regulatory record available) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Glimepiride belongs to the third-generation sulfonylurea class and works primarily by binding to the ATP-sensitive potassium (K-ATP) channel on pancreatic β-cells, triggering insulin release. It also has a weak partial agonist effect on PPAR-γ, which is far less pronounced than that of thiazolidinediones.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder characterised by anti-GAD65 (glutamic acid decarboxylase 65) antibodies. GAD65 is also the key autoantigen targeted in Type 1 Diabetes Mellitus. Because both conditions share immune-mediated targeting of GAD65, TxGNN likely captured this biological overlap in its graph structure — creating an apparent mechanistic bridge. Additionally, neuronal cells express K-ATP channels, so a theoretical pathway exists through which Glimepiride could influence GABAergic interneuron excitability (since GAD65 catalyses GABA synthesis).

However, the mechanistic link is highly indirect and speculative. The hypothesis that Glimepiride could improve GABAergic interneuron function in SPS has no experimental support whatsoever. The high TxGNN score most likely reflects the shared GAD65 antigen topology in the knowledge graph, rather than any direct or clinically plausible pharmacological action. This is a classic case where a model captures disease proximity but not true drug-target suitability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Glimepiride has no approved authorisations on record in Taiwan (TFDA). No product licences, dosage forms, or approved indications are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction rests entirely on a highly indirect mechanistic hypothesis — the shared GAD65 autoantigen between Type 1 Diabetes Mellitus and Classic Stiff Person Syndrome — without a single supporting clinical trial or published study. Furthermore, the drug's primary mechanism (stimulating residual β-cell insulin secretion) is irrelevant to the neurological pathology of SPS, and no plausible therapeutic pathway has been experimentally demonstrated.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank (DG002 remediation) to confirm whether any neurological target engagement exists
- Obtain TFDA package insert warnings and contraindications (DG001 remediation) before any safety assessment can begin
- Commission preclinical studies exploring whether Glimepiride modulates GABAergic interneuron activity or anti-GAD65 immunity in animal models of SPS
- Expert consultation with neurologists or neuroimmunologists specialising in Stiff Person Syndrome to evaluate biological plausibility
- Clarify whether the TxGNN high score reflects genuine drug-disease relatedness or a graph topology artefact from the shared GAD65 node (model interpretability review recommended)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

