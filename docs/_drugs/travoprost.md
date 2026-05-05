---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Travoprost
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

---

# Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a synthetic prostaglandin F2α analog (FP receptor agonist) administered as an ophthalmic solution, primarily used to lower intraocular pressure in patients with open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Visceral Calciphylaxis** with a near-perfect model confidence score,
however there are currently **0 clinical trials** and **0 publications** specifically addressing this indication — making this a purely model-driven prediction with no empirical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (inferred from clinical evidence; no Italy registration) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Travoprost is a selective FP prostanoid receptor agonist. Its proven efficacy in glaucoma derives from enhancing aqueous humor outflow through the uveoscleral pathway via relaxation of the ciliary muscle smooth muscle — an effect mediated by PGF2α receptor stimulation. This mechanism is well-documented across the 15 clinical trials retrieved in this evidence pack, all of which confirm Travoprost's role as an ocular hypotensive agent.

Visceral calciphylaxis is a rare and life-threatening syndrome seen predominantly in end-stage renal disease patients, characterised by progressive calcification and thrombosis of small dermal and subcutaneous blood vessels leading to ischemic necrosis. The theoretical mechanistic link proposed by TxGNN rests on two pillars: (1) prostaglandins generally possess vasodilatory properties that could theoretically improve microvascular perfusion in ischemic tissue, and (2) PGF2α has been shown to modulate vascular smooth muscle cell behaviour. One clinical study in the evidence pack (NCT00308945) directly measured Travoprost's effect on retinal vascular diameter and choroidal blood flow in glaucoma patients, confirming that the drug does exert measurable vascular effects — at least at the ocular level.

However, the leap from ocular vasodilation to systemic treatment of visceral calciphylaxis remains speculative and mechanistically weak. Calciphylaxis pathophysiology is dominated by calcium-phosphate deposition, pro-inflammatory cytokines, and coagulation dysregulation — none of which are known targets of the FP receptor pathway. Additionally, Travoprost exists only as a topical ophthalmic formulation; systemic bioavailability is negligible. The very high TxGNN score most likely reflects graph-level proximity within the vascular disease node network rather than a validated biological connection specific to calciphylaxis.

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
This prediction is entirely model-driven (L5) with zero clinical trials, observational studies, or preclinical literature supporting Travoprost's use in visceral calciphylaxis; the mechanistic connection between FP receptor agonism and calciphylaxis pathobiology is highly speculative, and no viable systemic route of administration currently exists.

**To proceed, the following is needed:**
- **Preclinical evidence**: In vitro or animal studies examining FP receptor expression and function in calcified vasculature or established calciphylaxis models
- **MOA data**: Retrieval of full mechanism of action from DrugBank (DG002) to assess any secondary target activity relevant to vascular calcification
- **Safety data**: Download and parse the package insert (DG001) to evaluate systemic absorption, cardiovascular warnings, and contraindications before any repurposing discussion
- **Formulation feasibility**: Assessment of whether a systemic (intravenous or subcutaneous) Travoprost formulation could be developed at pharmacologically active doses, given that the current ophthalmic route delivers negligible systemic exposure
- **Differential diagnosis of TxGNN signal**: Evaluate whether the high score reflects true calciphylaxis biology or is an artefact of knowledge-graph proximity to the broader vascular disease cluster (ranks 2–9 all predict vascular sub-conditions with similar scores, suggesting a class-level graph effect)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

