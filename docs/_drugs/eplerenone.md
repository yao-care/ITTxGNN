---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Eplerenone: From Hypertension / Post-MI Heart Failure to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor antagonist (sMRA), pharmacologically established for hypertension and post-myocardial infarction heart failure, though its original indication data is not available from the Italian regulatory record.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, with a prediction score of **99.50%**.
Currently, there are **no clinical trials** and **no directly relevant publications** supporting this new indication, placing this prediction at evidence level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Italy regulatory data (established pharmacological uses: hypertension, post-MI heart failure) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on established pharmacology, Eplerenone is a selective mineralocorticoid receptor (MR) antagonist — it competitively blocks aldosterone at the MR, thereby reducing sodium retention, lowering systemic blood pressure, and attenuating aldosterone-driven tissue fibrosis and vascular inflammation. Its efficacy in hypertension and post-MI left ventricular dysfunction has been validated in landmark trials (e.g., EPHESUS, EMPHASIS-HF for the MRA class).

The biological rationale connecting Eplerenone to pulmonary hypertension is grounded in the renin-angiotensin-aldosterone system (RAAS). RAAS over-activation is recognized as a contributor to pulmonary arterial hypertension (PAH) pathophysiology: aldosterone promotes pulmonary arterial smooth muscle cell proliferation, extracellular matrix deposition, and vasoconstriction. Animal model data for MR antagonism in pulmonary hypertension have generated early positive signals. Blocking the terminal MR effector could theoretically interrupt this aldosterone-mediated pulmonary vascular remodeling cycle.

However, the "unclear multifactorial mechanism" classification reflects a highly heterogeneous PH subgroup — multiple overlapping etiologies with varying degrees of RAAS involvement. The degree to which aldosterone is the dominant driver in any given patient within this category is unknown. While mechanistic plausibility exists, there is currently no clinical trial and no directly relevant literature to validate this hypothesis in humans. The prediction should therefore be treated as a research signal rather than a therapeutic lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature directly linking Eplerenone to pulmonary hypertension with unclear multifactorial mechanism is available.

> **Note:** The evidence search retrieved 20 publications for the related indication "pulmonary hypertension owing to lung disease and/or hypoxia" (rank 2), but all retrieved papers address the general biology of hypoxia (HIF-1α signaling, neurological hypoxia, oncological hypoxia) and contain no data on Eplerenone or MR antagonism in pulmonary hypertension. They are not presented as supporting evidence.

---

## Italy Market Information

Eplerenone currently holds **no marketing authorizations** in Italy and is not available on the Italian market. No product license data is on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in the current evidence pack. Package insert retrieval from official regulatory sources is a prerequisite before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN model output (evidence level L5), with zero supporting clinical trials and no directly relevant literature. The mechanistic hypothesis (aldosterone-driven pulmonary vascular remodeling blocked by Eplerenone) is biologically coherent but entirely unvalidated in humans. The heterogeneous and poorly defined nature of the "unclear multifactorial mechanism" PH subtype further reduces the probability that a single RAAS-directed agent would be broadly effective.

**To proceed, the following is needed:**

- **Safety prerequisites:** Retrieve and parse the full package insert from regulatory sources (TFDA/EMA/AIFA) to obtain contraindications, key warnings, and drug interactions — currently a blocking data gap
- **MOA confirmation:** Query DrugBank API to formally document the mechanism of action for mechanistic linkage analysis
- **Class-effect evidence sweep:** Conduct a systematic literature review for the broader MRA class (spironolactone, finerenone) in pulmonary hypertension, to assess whether a class-level signal exists before committing to Eplerenone specifically
- **PH subtype refinement:** Stratify "multifactorial" PH patients by RAAS biomarkers (plasma aldosterone, renin activity) to identify a subpopulation most likely to respond
- **Preclinical data:** Identify any animal or in vitro studies of Eplerenone or selective MR antagonism in models of pulmonary hypertension
- **Expert validation:** Convene pulmonary hypertension specialists and clinical pharmacologists to assess feasibility of a pilot investigator-initiated trial before committing to formal development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

