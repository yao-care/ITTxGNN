---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 5
---

# Montelukast
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

Using `txgnn-pipeline` to check for report generation guidance — not applicable here since the task is report writing from a completed Evidence Pack, not pipeline execution. Proceeding directly with the Drug Repurposing Evaluation Report per the v5 format.

---

# Montelukast: From Asthma to Bronchitis

## One-Sentence Summary

Montelukast (brand name Singulair) is a selective cysteinyl leukotriene receptor 1 (CysLT1) antagonist approved worldwide for the treatment of asthma and allergic rhinitis, though no AIFA registration is recorded in the current Italian dataset.
The TxGNN model predicts it may be effective for **Bronchitis**, with **23 clinical trials** and **20 publications** currently supporting this direction — including Phase 3 trials in RSV-induced bronchiolitis and Phase 2 trials in bronchiolitis obliterans syndrome after stem cell transplantation.
Evidence is rated L2, anchored by completed Phase 2–4 trials and a 2024 ERS/EBMT clinical practice guideline that explicitly recommends montelukast-containing regimens for pulmonary bronchiolitis obliterans.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma, Allergic Rhinitis (globally approved; no AIFA registration found in current dataset) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Italy Market Status | Not marketed (no AIFA license found) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, montelukast is a selective, orally active CysLT1 receptor antagonist. Cysteinyl leukotrienes — LTC4, LTD4, and LTE4 — are potent lipid mediators produced by mast cells and eosinophils during airway inflammation. By competitively blocking CysLT1, montelukast reduces bronchial smooth muscle contraction, vascular permeability, eosinophil recruitment, and mucus hypersecretion, all of which are core pathological features of bronchitis.

The mechanistic bridge from asthma to bronchitis is well-supported. During acute bronchitis and recurrent obstructive bronchitis episodes, LTD4 and LTE4 concentrations in bronchial lavage fluid are significantly elevated — the same mediators that montelukast was designed to block. Non-asthmatic eosinophilic bronchitis (NAEB), a distinct subtype, has direct RCT-level evidence showing that add-on montelukast to inhaled budesonide significantly reduces airway eosinophilia and cough severity (PMID 25563311). Separately, in bronchiolitis obliterans syndrome (BOS) — a severe fibrotic complication of lung or hematopoietic stem cell transplantation — the leukotriene pathway plays a documented pathogenic role supported by animal models (PMID 28545478) and prospective Phase 2 trials (PMID 35114411, PMID 26475726).

In 2024, the European Respiratory Society (ERS) and European Bone Marrow Transplantation Society (EBMT) jointly published clinical practice guidelines that formally recommend the FAM regimen (fluticasone + azithromycin + montelukast) for pulmonary chronic graft-versus-host disease/BOS (PMID 38485149). This guideline endorsement, combined with the leukotriene-driven pathobiology shared across bronchitis subtypes, makes the TxGNN prediction mechanistically coherent and clinically credible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Directly evaluated montelukast sodium for treatment and prevention of recurrent obstructive bronchitis in children aged 1–7 years; 80 children randomized into two groups |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Evaluated montelukast for acute bronchiolitis and post-bronchiolitis viral-induced wheezing in infants aged 3–12 months; most directly relevant completed trial |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1,125 | Large Phase 3 RCT comparing two doses of montelukast vs placebo for respiratory symptoms of RSV-induced bronchiolitis in children aged 3–24 months |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | Compared montelukast vs prednisolone in chronic cough including eosinophilic bronchitis patients (FeNO ≥30 ppb); measured 24-hour cough count after 2 weeks |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Phase 4 | Completed | 100 | Assessed add-on oral montelukast to standard treatment in preschool children hospitalized for acute respiratory illness with overlapping bronchitis/asthma presentation |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | Double-blind placebo-controlled RCT testing montelukast to slow progression of bronchiolitis obliterans syndrome (BOS) after lung transplantation |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | Evaluated once-daily montelukast effect on duration of acute illness in infants with first-time viral bronchiolitis |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | RCT of add-on montelukast to inhaled budesonide in non-asthmatic eosinophilic bronchitis; primary endpoint was cough visual analogue score |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Multi-institutional prospective Phase 2 study of montelukast for bronchiolitis obliterans following allogeneic or autologous stem cell transplantation; evaluated lung function decline |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Phase 2 trial of fluticasone + azithromycin + montelukast (FAM) for bronchiolitis obliterans after stem cell transplant; treatment failure rate (≥10% FEV1 decline) as primary endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Clinical Practice Guideline | European Respiratory Journal | ERS/EBMT guidelines on treatment of pulmonary chronic graft-versus-host disease; FAM regimen (including montelukast) formally recommended for BOS management |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Therapeutic Advances in Respiratory Disease | Comprehensive review of montelukast's therapeutic potential in BOS following lung and hematopoietic stem cell transplantation; TH-1/TH-2, NF-κB, and TGF-β mechanisms reviewed |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Phase 2 Trial | Transplantation and Cellular Therapy | Prospective Phase 2 multi-institutional trial of montelukast for BOS after HCT; examined whether CysLT blockade altered lung function decline over time |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Phase 2 Trial | Biology of Blood and Marrow Transplantation | FAM (fluticasone + azithromycin + montelukast) with steroid pulse for new-onset BOS after HCT; n=36, ~50% of patients avoided treatment failure at 6 months |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Add-on montelukast to budesonide vs budesonide alone in non-asthmatic eosinophilic bronchitis; significant improvement in cough VAS score, quality of life, and airway eosinophilia |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Clinical Study | Respiratory Research | Combination of budesonide/formoterol + montelukast + N-acetylcysteine for BOS after HSCT; compared against corticosteroid standard of care |
| [30038355](https://pubmed.ncbi.nlm.nih.gov/30038355/) | 2019 | Review | Bone Marrow Transplantation | Global review of BOS diagnostic and therapeutic challenges post-HCT; montelukast positioned as key treatment component with mechanistic rationale |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal Study | Journal of Cardiothoracic Surgery | Rat transplantation model of bronchiolitis obliterans; LTB4 significantly elevated in chronic rejection; montelukast attenuated fibrotic progression |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Systematic Review | Pediatric Allergy and Immunology | Systematic review on montelukast efficacy for preventing post-RSV-bronchiolitis wheezing; CysLT pathway linked to long-term reactive airway disease after bronchiolitis |
| [20442434](https://pubmed.ncbi.nlm.nih.gov/20442434/) | 2010 | Animal Study | American Journal of Respiratory and Critical Care Medicine | Neonatal mouse RSV model; montelukast during primary infection prevented airway hyperresponsiveness, eosinophilic inflammation, and mucus hyperproduction upon reinfection |

---

## Italy Market Information

Montelukast currently has **no AIFA-registered authorizations** in the current dataset (0 licenses found).

> **Important note:** This likely reflects a data collection gap rather than actual market absence. Montelukast (Singulair® and multiple generics) has EMA approval and is broadly marketed across EU member states. Direct verification against the AIFA public medicines database is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

The safety data fields in the current Evidence Pack are not populated. Please refer to the package insert for complete information on warnings, contraindications, and drug interactions.

From the clinical literature retrieved as part of this evaluation, one critical safety signal is consistently documented and warrants explicit attention:

- **Neuropsychiatric adverse events (FDA Black Box Warning):** In 2020, the US FDA issued a black box warning for montelukast citing risks including agitation, aggression, anxiety, depression, hallucinations, sleep disturbances, and suicidal ideation/behavior. Multiple large cohort studies and systematic reviews confirm this signal (PMID 37758273, PMID 35608857, PMID 36948487, PMID 39836401, PMID 39578088). Risk appears present across age groups but is particularly relevant in pediatric populations — especially pertinent given that many bronchitis trials enroll children.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The 2024 ERS/EBMT clinical practice guideline formally endorsing FAM therapy (which includes montelukast) for bronchiolitis obliterans, combined with Phase 2–4 trial evidence across multiple bronchitis subtypes and an RCT demonstrating efficacy in eosinophilic bronchitis, provides sufficient mechanistic and clinical basis to proceed — provided the target bronchitis subtype is clearly defined and the neuropsychiatric safety signal is prospectively monitored.

**To proceed, the following is needed:**
- Verify AIFA registration status directly in the official AIFA public medicines database — the current dataset (0 licenses) almost certainly reflects a data gap
- Obtain the EMA Summary of Product Characteristics (SmPC) for complete contraindications, DDI profile, and population-specific warnings
- Define the target bronchitis subtype: acute infectious bronchiolitis (infants), non-asthmatic eosinophilic bronchitis (adults), or bronchiolitis obliterans syndrome (post-transplant), as evidence strength and regulatory pathways differ substantially across these
- Resolve the status of NCT04613180 (recurrent obstructive bronchitis, UNKNOWN status) and extract results if the trial has completed
- Design a structured safety monitoring plan addressing the FDA black box warning on neuropsychiatric events, with mandatory patient/caregiver counselling prior to initiation — particularly for pediatric target populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

