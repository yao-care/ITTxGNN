---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 9
---

# Iloprost
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

Now I have all the context needed. Let me generate the report based on the Evidence Pack.

---

# Iloprost: From Pulmonary Arterial Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Iloprost is a synthetic prostacyclin (PGI₂) analogue, recognized globally as a treatment for Pulmonary Arterial Hypertension (PAH); it is not currently registered or marketed in Taiwan.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, but this direction is supported by **zero clinical trials and zero publications**, suggesting the prediction most likely reflects knowledge graph topology rather than a genuine mechanistic connection.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally established for Pulmonary Arterial Hypertension (PAH) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Iloprost is a stable synthetic analogue of prostacyclin (PGI₂) that selectively activates IP receptors on vascular smooth muscle and platelets, producing pulmonary vasodilation, inhibition of platelet aggregation, and suppression of vascular remodeling. It is approved in multiple countries (EU, US, others) for PAH under brand names such as Ventavis (inhaled) and Ilomedin (IV/infusion).

Hypotrichosis Simplex of the Scalp is a rare autosomal dominant genodermatosis caused by loss-of-function mutations in the *CDSN* gene, which encodes corneodesmosin — a structural protein critical for corneodesmosomes (cell-adhesion junctions) in the scalp epidermis and the inner root sheath of hair follicles. The disease mechanism is entirely structural: keratinocyte adhesion fails, leading to progressive follicular miniaturization and hair loss. There is no known vascular, platelet, or IP-receptor component to its pathology.

Although prostaglandins broadly (particularly PGE₂ via EP2/EP4 receptors) have been shown to promote anagen-phase hair follicle cycling, Iloprost's specific pharmacological target — the IP receptor — is a distinct signaling pathway with no established role in CDSN-dependent structural integrity. The repurposing rationale therefore lacks a credible mechanistic foundation. The TxGNN high score (99.45%) is most plausibly attributed to topological proximity of "scalp/skin disease" nodes in the knowledge graph rather than true biological relatedness to PAH-type IP-receptor pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence for Iloprost in hypotrichosis simplex of the scalp, and the mechanistic link between IP-receptor agonism and CDSN-structural hair follicle defects is not biologically coherent. Proceeding at this stage would not be a productive use of research resources.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis connecting IP-receptor/prostacyclin signaling to CDSN protein expression, corneodesmosome stability, or hair follicle cycle regulation
- At minimum, in vitro evidence (e.g., keratinocyte or follicle organoid assays) demonstrating any biological response to IP-receptor activation in CDSN-deficient models
- Retrieval of the full Iloprost package insert (TFDA/EMA) to document MOA, warnings, and contraindications before any further safety assessment can proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

