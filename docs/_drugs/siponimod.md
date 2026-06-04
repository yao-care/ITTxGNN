---
layout: default
title: Siponimod
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 8
---

# Siponimod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Siponimod: From Secondary Progressive Multiple Sclerosis to Pulmonary Hypertension

## One-Sentence Summary

Siponimod (Mayzent) is a selective sphingosine-1-phosphate (S1P) receptor modulator approved for secondary progressive multiple sclerosis (SPMS), where it reduces CNS lymphocyte infiltration and slows disease progression.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Secondary Progressive Multiple Sclerosis (SPMS) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, siponimod is a selective S1P1/S1P5 receptor modulator approved for secondary progressive multiple sclerosis. It acts by retaining lymphocytes in lymph nodes, reducing their infiltration into the CNS, and additionally exerts neuroprotective effects via S1P5 receptors in the brain and spinal cord.

The theoretical connection to pulmonary hypertension lies in the vascular biology of S1P signaling. S1P1 receptors are expressed on pulmonary vascular endothelial cells, and the S1P axis regulates vascular tone, endothelial barrier integrity, and smooth muscle cell proliferation — all processes that are dysregulated in pulmonary arterial hypertension (PAH). An S1P1 modulator could, in principle, influence pathological pulmonary vascular remodeling.

However, this mechanistic link operates in both directions. Siponimod carries established cardiac safety warnings — including first-dose bradycardia and AV conduction block — which represent a specific concern in pulmonary hypertension patients who commonly have compromised right ventricular function. This safety profile may constitute a relative or absolute contraindication in this population. Pre-clinical validation in pulmonary vascular disease models would be essential before any further development in this direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Siponimod is not currently marketed in Italy. No AIFA authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert warnings and contraindications data were not retrievable in this evidence pack. Based on the drug's pharmacological class (S1P receptor modulator), clinically relevant safety considerations include: first-dose bradycardia, AV conduction block, macular oedema, risk of infections due to lymphopenia, and CYP2C9 genotype-dependent dosing requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.68%) based on knowledge graph connectivity between S1P1 receptor biology and pulmonary vascular disease, but there is currently zero clinical or published literature evidence specifically supporting siponimod in pulmonary hypertension. Furthermore, the drug's known cardiac safety profile raises specific concerns in this patient population.

**To proceed, the following is needed:**

- **Pre-clinical validation:** Pulmonary arterial hypertension animal model studies (e.g., monocrotaline or Sugen/hypoxia rat model) examining the effect of S1P1 modulation on pulmonary vascular remodeling
- **Cardiac safety assessment:** Right ventricular hemodynamic evaluation in a PH-specific context, given known bradycardia and AV block risks
- **Full MOA data retrieval:** DrugBank API query to confirm receptor selectivity profile (S1P1 vs. S1P5 vs. other subtypes) and downstream signaling
- **Regulatory safety review:** Download and parse the full EMA/AIFA package insert to identify whether pulmonary hypertension or cardiac conduction abnormalities are listed as contraindications
- **Comparator landscape review:** Survey other S1P modulators (fingolimod, ozanimod) for any available PAH preclinical or clinical data to assess class-level plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

