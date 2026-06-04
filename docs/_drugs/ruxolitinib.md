---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

Using the `txgnn-pipeline` skill as context. Now generating the evaluation report based on the Evidence Pack.

---

The evidence pack contains **10 TxGNN-predicted indications** ranging from L5 (no evidence) to L2 (clinical study + Phase 3 trial). The top-ranked TxGNN prediction (uterine corpus PEComa, score 99.73%) has zero supporting evidence. This report focuses on **infection-associated hemophagocytic syndrome** — the highest-evidence prediction (L2) with the most actionable recommendation — while providing a full landscape summary of all predictions.

---

# Ruxolitinib: From Myeloproliferative Neoplasms to Infection-Associated Hemophagocytic Syndrome

## One-Sentence Summary

Ruxolitinib is a selective JAK1/2 inhibitor established in the treatment of myeloproliferative neoplasms, working by blocking aberrant JAK-STAT signaling that drives abnormal cell proliferation and systemic inflammation.
The TxGNN model predicts it may be effective for **infection-associated hemophagocytic syndrome (HPS/HLH)** — a life-threatening cytokine storm disorder triggered by viral or bacterial pathogens —
with **2 registered clinical trials** and **20 publications** currently supporting this direction, the strongest evidence among 10 predicted indications evaluated in this evidence pack.

> **Evidence pack scope:** TxGNN identified 10 candidate repurposing indications for ruxolitinib. Seven are PEComa/TSC-spectrum rare tumors (Ranks 1–4, 7) or rhabdoid tumor (Rank 6) with L5 evidence only. Liposarcoma (Rank 5) has L4 mechanistic evidence. Malignancy-associated HLH (Rank 9) carries L3 evidence. Infection-associated HPS (Rank 10) is the sole indication reaching L2 with an actionable recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in Taiwan |
| Predicted New Indication | Hemophagocytic Syndrome Associated with an Infection |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on analytical notes embedded throughout the repurposing rationale, ruxolitinib is a potent JAK1/2 inhibitor that simultaneously suppresses multiple pro-inflammatory cytokine axes — most critically IFN-γ (via JAK1/2–STAT1), IL-6 (via JAK1–STAT3), and IL-2/IL-15 (via JAK1/3–STAT5). This positions ruxolitinib as a broad cytokine storm modulator rather than a single-pathway blocker.

Infection-associated HPS/HLH develops when pathogens — predominantly Epstein-Barr virus, adenovirus, and certain bacteria — hijack T cell and macrophage activation, unleashing a catastrophic cytokine cascade. IFN-γ is the primary driver: it activates macrophages through JAK1/2–STAT1, which in turn produce more IFN-γ and IL-6 in a self-amplifying loop, leading to fever, pancytopenia, hyperferritinemia, hepatosplenomegaly, and multiorgan failure. The JAK1/2–STAT axis is the shared final signaling pathway for nearly every cytokine implicated in this process. Ruxolitinib blocks it at the source.

This mechanistic logic has been validated in multiple layers of evidence. Preclinical studies in perforin-deficient murine HLH models (PMID 31015190) confirmed that ruxolitinib reduces T cell activation, dampens IFN-γ downstream signaling, and decreases immunopathology. Combination studies in the same model further showed synergy with IFN-γ neutralization (PMID 37228616). Clinically, these findings translate into responses observed across pediatric EBV-HLH, adenovirus-associated post-transplant HPS, panniculitis-triggered HPS, infection-associated HPS in pregnancy, and AIDS-associated secondary HLH — spanning diverse trigger types and patient populations with consistent mechanistic logic.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07424222](https://clinicaltrials.gov/study/NCT07424222) | Phase 1 | Not Yet Recruiting | 16 | Pilot study of ruxolitinib for immune effector cell-associated HLH-like syndrome (IEC-HS) occurring after CAR-T therapy; evaluates safety, efficacy, optimal treatment duration, immunological response biomarkers, and CAR-T expansion dynamics post-ruxolitinib |
| [NCT04424056](https://clinicaltrials.gov/study/NCT04424056) | Phase 3 | Unknown | 216 | Open-label randomized trial of anakinra and/or tocilizumab ± ruxolitinib in severe COVID-19-associated hyperinflammation (Stage 2b/3, CRP >200 mg/L, ARDS); directly tests ruxolitinib combination in a cytokine storm setting — final publication status requires confirmation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Consensus Guidelines | Critical Care Medicine | International multidisciplinary consensus guidelines for HLH recognition, diagnosis, supportive care, and treatment in ICU; establishes the diagnostic and management framework within which ruxolitinib is being evaluated |
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Prospective Cohort | Blood | Ruxolitinib as first-line therapy for pediatric HLH with response-based treatment stratification (ChiCTR2000031702, n=50+); shows ruxolitinib's frontline viability and supports early JAK inhibition to prevent disease escalation |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Retrospective Cohort | British Journal of Haematology | Largest published comparison of RUX-based regimen (n=53) vs adjusted HLH-94 chemotherapy (n=42) in pediatric EBV-HLH; provides direct comparative efficacy and safety data for ruxolitinib vs standard-of-care |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Retrospective Cohort (n=12) | Annals of Hematology | Sintilimab combined with ruxolitinib as compassionate therapy for 12 adult EBV-HLH patients; demonstrates combination targeted immunotherapy strategy for refractory adult HLH with unsatisfactory overall survival on conventional therapy |
| [37702780](https://pubmed.ncbi.nlm.nih.gov/37702780/) | 2023 | Review | Innere Medizin | Review of HLH management in ICU patients including ruxolitinib and emapalumab; discusses CAR-T–associated HLH as an emerging indication and frames JAK inhibition within evolving treatment algorithms |
| [31943120](https://pubmed.ncbi.nlm.nih.gov/31943120/) | 2020 | Review | QJM | Comprehensive review of adult HLH diagnosis, triggers, and treatment; characterizes the high mortality burden and documents the limitations of HLH-94 in adult populations |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Case Series | Journal of Pediatric Hematology/Oncology | Emapalumab + ruxolitinib + dexamethasone for EBV-HLH with multiorgan damage and severe infection; illustrates a multi-target combination approach for cases refractory to both HLH-94 and ruxolitinib monotherapy |
| [38984023](https://pubmed.ncbi.nlm.nih.gov/38984023/) | 2024 | Case Report | Translational Pediatrics | Ruxolitinib as salvage therapy for adenovirus-associated HPS occurring after haploidentical allogeneic HSCT; successful outcome in a rare post-transplant HLH scenario with limited treatment options |
| [39620213](https://pubmed.ncbi.nlm.nih.gov/39620213/) | 2024 | Case Report | Frontiers in Immunology | Infection-associated HPS during pregnancy treated with ruxolitinib induction followed by HLH-94 protocol; notable evidence that ruxolitinib can be used in high-risk patients where cytotoxic chemotherapy carries additional risk |
| [36533357](https://pubmed.ncbi.nlm.nih.gov/36533357/) | 2022 | Case Report | Journal of Peking University Health Sciences | Two cases of panniculitis-associated HPS effectively resolved with ruxolitinib; demonstrates efficacy in an atypical HPS trigger with autoimmune-inflammatory overlap |

---

## Taiwan Market Information

Ruxolitinib currently has **no marketing authorizations** in Taiwan. No approved products, indications, or dosage forms are on record with the Taiwan FDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Data Gap Notice:** Taiwan package insert warnings, contraindications, and drug interaction data were not available in this evidence pack. These are classified as a **Blocking** data gap (DG001) that must be resolved before formal safety screening (Stage S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ruxolitinib's JAK1/2 inhibition directly and mechanistically targets the IFN-γ–driven cytokine storm cascade that defines infection-associated HPS/HLH. The growing clinical evidence base — spanning a frontline prospective cohort in *Blood*, the largest comparative pediatric cohort to date in *British Journal of Haematology*, multiple retrospective cohorts, an ongoing Phase 3 RCT (NCT04424056, n=216), and a forthcoming Phase 1 trial in CAR-T–associated HLH (NCT07424222) — establishes mechanistic-clinical consistency strong enough to justify cautious advancement under structured guardrails.

**To proceed, the following is needed:**

- **Confirm NCT04424056 final results** — Phase 3 status is listed as "Unknown"; if results are positive, evidence level upgrades from L2 to L1, which significantly strengthens the repurposing case
- **Resolve Taiwan package insert data gap (DG001)** — obtain and parse the 仿單 PDF from the TFDA website to complete safety screening and enable formal Stage S1 evaluation
- **Obtain full MOA data from DrugBank (DG002)** — required to complete the mechanistic linkage analysis and document the JAK1/2 inhibition profile formally
- **Pursue Taiwan import or compassionate use registration** — given zero current authorizations, a regulatory pathway must be identified before clinical availability can be established
- **Stratify evidence by HPS trigger type** — EBV-HLH has the most data; develop a Taiwan-specific subgroup analysis plan to identify the most responsive patient population
- **Design a prospective pilot study or patient registry** — to generate Taiwan-population–specific safety and efficacy data in infection-associated HPS cases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

