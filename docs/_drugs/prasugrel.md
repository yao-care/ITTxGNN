---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

Using the `txgnn-pipeline` skill to guide report generation context. Now proceeding to produce the full report from the Evidence Pack.

---

# Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine P2Y12 inhibitor used for prevention of thrombotic cardiovascular events in patients with acute coronary syndrome (ACS) undergoing percutaneous coronary intervention (PCI).
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of 99.88%.
However, **no directly relevant clinical trials or publications** supporting this specific indication were identified — all retrieved studies were evaluated as non-contributory due to keyword mismatch, placing this at an **L5 evidence level (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (ACS) / Percutaneous coronary intervention (PCI) — thrombotic event prevention |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Prasugrel is a third-generation thienopyridine that irreversibly inhibits the platelet P2Y12 ADP receptor, blocking platelet activation and aggregation. It is a prodrug that achieves faster and more consistent antiplatelet effects than clopidogrel, due to more efficient hepatic conversion to its active metabolite. Its established role is in preventing arterial thrombosis after coronary stent placement.

The mechanistic bridge to pulmonary arterial hypertension (PAH) rests on the observation that activated platelets are prominent contributors to PAH pathophysiology. In PAH, platelets release thromboxane A2 (TXA2), serotonin, and platelet-derived growth factor (PDGF) into the pulmonary circulation — all of which drive vasoconstriction and pulmonary vascular remodeling. Inhibiting P2Y12 could theoretically reduce these platelet-derived signals and attenuate progressive vascular damage.

However, this remains **indirect mechanistic inference only**. Prasugrel's known pharmacology concerns arterial thrombosis, not pulmonary vascular remodeling, and no preclinical or clinical study was identified that directly tests this hypothesis. The high TxGNN score likely reflects shared network neighborhoods in the knowledge graph (e.g., thrombosis, platelet biology) rather than empirically validated efficacy in PAH. This prediction is best treated as a hypothesis-generating signal, not actionable clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> **Data quality note:** Two trials were retrieved during the evidence search but were assessed as non-contributory (Relevance Grade C):
> - **[NCT03993119](https://clinicaltrials.gov/study/NCT03993119)**: A Spanish observational study of NOAC use in elderly patients with non-valvular atrial fibrillation — evaluates rivaroxaban/apixaban, not prasugrel, in a completely different disease.
> - **[NCT04846556](https://clinicaltrials.gov/study/NCT04846556)**: A retrospective study of apixaban in cancer-associated venous thromboembolism — no intersection with prasugrel or pulmonary hypertension.
>
> Both hits are the result of database keyword cross-matching artifacts and contribute nothing to this repurposing evaluation.

---

## Literature Evidence

Currently no related literature directly supporting prasugrel use in pulmonary hypertension.

> **Data quality note:** Two publications were retrieved but are not relevant to this indication:
> - **[PMID 34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/)** (Kardiologiia, 2021): COVID-19 comorbidity registry examining the impact of background cardiovascular therapy on COVID-19 outcomes — prasugrel is not specifically studied, and the focus is entirely unrelated to PAH.
> - **[PMID 21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/)** (Curr Med Res Opin, 2011): Retrospective cohort on clopidogrel adherence post-PCI in ACS — prasugrel is mentioned only as a treatment comparator in the ACS context, with no bearing on pulmonary hypertension.

---

## Italy Market Information

Prasugrel currently has no approved marketing authorizations in Italy. The drug is not marketed, and no product licenses are registered.

> **Context:** Prasugrel (brand name Efient®) is approved by EMA and marketed in multiple EU countries for ACS/PCI indications. The absence of Italian-specific registration data in this Evidence Pack may reflect a data gap rather than true unavailability. Independent verification via AIFA's official database is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (key warnings, contraindications, and drug-drug interactions) were not available from the current data sources. Based on prasugrel's pharmacological class (irreversible P2Y12 inhibitor), the following general cautions are well-established in the literature and should be verified against the full package insert:
> - **Bleeding risk** is the primary concern — prasugrel carries a boxed warning for serious and fatal bleeding in its FDA/EMA labelling.
> - **Contraindicated** in patients with prior stroke or TIA (net harm established in the TRITON-TIMI 38 trial).
> - **Not recommended** in patients ≥75 years or <60 kg without careful benefit-risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.88%), the mechanistic link between P2Y12 inhibition and pulmonary hypertension is speculative and indirect. No supporting clinical trials or literature were identified, resulting in an L5 evidence level that does not justify advancement without foundational preclinical data.

**To proceed, the following is needed:**
- **Preclinical studies**: In vitro or animal model experiments testing whether P2Y12 inhibition reduces pulmonary vascular remodeling or right ventricular pressure in PAH models (e.g., monocrotaline or hypoxia-induced PAH in rodents)
- **Mechanistic validation**: Evidence that platelet-derived TXA2, serotonin, or PDGF are meaningfully suppressed by P2Y12 inhibition in the pulmonary circulation context
- **Safety review**: Full package insert analysis for bleeding risk and contraindication profile — essential before any PAH population study design
- **Biomarker exploration**: Investigation of platelet activation markers in PAH cohorts to identify a patient subgroup most likely to benefit
- **Comparison with existing PAH therapies**: Position prasugrel's potential mechanism relative to approved PAH agents (PDE5 inhibitors, ERA, prostacyclin analogues) to assess whether antiplatelet therapy offers additive value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

