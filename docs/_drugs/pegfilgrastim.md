---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Pegfilgrastim: From Chemotherapy-Induced Neutropenia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a long-acting PEGylated form of G-CSF (granulocyte colony-stimulating factor), primarily used to reduce the risk of febrile neutropenia in patients receiving myelosuppressive chemotherapy.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (SNPDR)**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of febrile neutropenia following cytotoxic chemotherapy |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Pegfilgrastim is a PEGylated derivative of filgrastim that acts as a G-CSF receptor (CSF3R) agonist. By binding CSF3R on bone marrow progenitor cells, it stimulates the proliferation and differentiation of neutrophil precursors and mobilizes hematopoietic stem and progenitor cells (HSPCs) and endothelial progenitor cells (EPCs) into peripheral circulation. Its extended half-life relative to filgrastim allows for once-per-cycle dosing in the chemotherapy setting.

The proposed mechanistic bridge to diabetic retinopathy centers on the EPC mobilization hypothesis: EPCs mobilized by G-CSF signaling theoretically home to sites of microvascular injury in the retina and participate in vessel repair. In early-to-moderate non-proliferative diabetic retinopathy, where microvascular dropout is the dominant pathology, this vascular regeneration hypothesis provides at least a biological rationale for exploration.

However, the prediction carries a specific and serious risk at the SNPDR stage. G-CSF simultaneously upregulates VEGF secretion from mobilized cells — the same signal that drives pathological angiogenesis in proliferative diabetic retinopathy (PDR). At the SNPDR threshold, where the eye is already at high risk of converting to PDR, any stimulus that augments VEGF could accelerate progression to tractional retinal detachment and irreversible vision loss. The evidence pack itself flags this as a dual-directional risk where the safety concern likely outweighs the theoretical therapeutic benefit at this particular disease stage.

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
The TxGNN prediction is mechanistically traceable but rests entirely on computational inference (L5); there are no registered trials, no published literature, and no preclinical data to validate efficacy in SNPDR — and the same G-CSF mechanism that theoretically supports retinal vessel repair also carries a plausible risk of triggering VEGF-driven disease progression at this critical disease stage.

**To proceed, the following is needed:**
- **Preclinical safety data**: In vitro and in vivo studies in SNPDR models specifically evaluating whether G-CSF-mediated EPC mobilization is accompanied by net VEGF upregulation and angiogenic risk at the retinal level
- **Disease-stage stratification**: Determine whether a therapeutic window exists (e.g., early NPDR vs. SNPDR) where the vascular repair signal exceeds the pro-angiogenic risk
- **Full MOA documentation**: Retrieve complete mechanism of action data from DrugBank to enable formal mechanistic scoring
- **Package insert safety review**: Obtain full prescribing information to extract contraindications, key warnings, and drug interaction profile before any S1 safety evaluation
- **Ophthalmology expert consultation**: Validate the EPC mobilization hypothesis and assess clinical plausibility with a retinal specialist
- **Literature gap analysis**: Systematic search for G-CSF or filgrastim (non-PEGylated analog) studies in diabetic retinopathy models, which may provide indirect mechanistic evidence
- If preclinical data supports net benefit, a Phase 1/2 proof-of-concept trial with rigorous retinal imaging endpoints (OCTA, fluorescein angiography) would be the minimum threshold for advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

