---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill to confirm context, then generating the evaluation report from the Evidence Pack.

---

# Roxadustat: From Renal Anemia to Dry Eye Syndrome

## One-Sentence Summary

Roxadustat (FG-4592) is a prolyl hydroxylase domain (PHD) inhibitor approved in China, the EU, and Japan for treating anemia in patients with chronic kidney disease (renal anemia), but not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Dry Eye Syndrome**, with **1 observational clinical study** providing only indirect epidemiological support.
Direct intervention trials are entirely absent, and the overall evidence base remains at preclinical/mechanistic level (L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anemia associated with chronic kidney disease (renal anemia) — approved in China, EU, and Japan; not marketed in Taiwan |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Roxadustat works by inhibiting HIF prolyl hydroxylase domain (PHD) enzymes, which under normal oxygen conditions continuously tag HIF-1α and HIF-2α for proteasomal degradation. By blocking PHD, Roxadustat allows HIF-1α/HIF-2α to accumulate even in normoxic conditions, driving transcription of erythropoietin (EPO) and stimulating red blood cell production — the mechanism underlying its approved use in renal anemia.

The proposed mechanistic bridge to dry eye syndrome hinges on HIF-1α's broader role beyond erythropoiesis. HIF-1α stabilization can upregulate VEGF and TGF-β3, cytokines relevant to lacrimal gland function, corneal epithelial regeneration, and goblet cell maintenance in the conjunctiva. In principle, this could improve tear film stability and reduce ocular surface inflammation — key dry eye pathology drivers. Supporting this hypothesis at an epidemiological level, patients with renal anemia have been observed to have elevated rates of meibomian gland dysfunction and dry eye symptoms, suggesting a shared ischemia-hypoxia axis in both conditions.

However, this mechanistic rationale remains entirely theoretical. No study has directly tested Roxadustat as a dry eye treatment. The one available clinical study (NCT06287879) is observational — it describes meibomian gland morphology in renal anemia patients receiving EPO or Roxadustat, not a therapeutic intervention for dry eye. The predictive signal from TxGNN is high (99.51%), but the biological plausibility is indirect and unconfirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|------------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | NA | Unknown | 50 | Observational study collecting meibomian gland function and morphology data from renal anemia patients who visited ophthalmology with dry eye complaints. Roxadustat is one of the drugs these patients receive (alongside EPO), but the study does not test Roxadustat as a dry eye intervention. Provides epidemiological evidence of renal anemia–dry eye comorbidity as a foundation for future trials. |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Roxadustat has not received approval from Taiwan's TFDA and is not marketed in Taiwan. No licenses or authorizations are on record. For reference, the drug is currently approved in China (NMPA, 2021), the European Union (EMA, 2021 for non-dialysis CKD anemia), and Japan (PMDA, 2020).

---

## Safety Considerations

> ⚠️ **Mechanistic Safety Alert — Oncological Risk:**
> While the primary predicted indication is dry eye syndrome, TxGNN also ranked **Squamous Cell Carcinoma (SCC)** as a predicted indication (score 99.02%). This combination warrants an explicit mechanistic safety warning: Roxadustat stabilizes HIF-1α/HIF-2α, and HIF pathway activation in tumor microenvironments is a well-established driver of tumor angiogenesis (via VEGF↑), epithelial-mesenchymal transition (EMT), and hypoxic survival adaptation. Using Roxadustat in any patient with active solid tumors — including SCC — would be mechanistically contraindicated and could accelerate disease progression. Notably, the FDA declined to approve Roxadustat in the US partly due to signals of increased major adverse cardiovascular events (MACE) and concerns about oncologic safety.

For complete warnings and contraindications applicable to the dry eye syndrome indication, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological hypothesis linking HIF-1α stabilization to dry eye improvement is conceptually interesting, but no direct clinical intervention trial, preclinical model, or published mechanistic study supports Roxadustat as a dry eye treatment. The only available evidence is a single observational study providing indirect epidemiological context. Combined with zero Taiwan regulatory presence, absent safety data, and an active mechanistic safety concern in oncology patients, the evidence does not yet justify advancement.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept:** In vitro or animal model studies specifically testing HIF-PHI on lacrimal gland function, tear secretion, and corneal epithelial repair endpoints
- **Route of administration assessment:** Roxadustat is an oral systemic drug — any dry eye application must address whether systemic dosing (at anemia-level doses) or a novel topical ophthalmic formulation is feasible and safe
- **Safety package review:** Full Taiwan TFDA package insert data for contraindications, warnings, and special population restrictions; independent cardiovascular and oncologic risk stratification for non-anemia populations
- **Mechanism of action documentation:** Complete MOA data from DrugBank to enable formal mechanistic-link scoring
- **Epidemiological clarification:** Prospective data on whether Roxadustat treatment in CKD patients correlates with reduced dry eye severity (could be collected within existing CKD nephrology cohorts at low cost)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

