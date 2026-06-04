---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
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

Using `txgnn-pipeline` to guide report generation for this Italy TxGNN repurposing evaluation.

Now generating the Rivaroxaban evaluation report based on the Evidence Pack:

---

# Rivaroxaban: From Thromboembolism to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct oral Factor Xa inhibitor clinically established for the prevention and treatment of venous thromboembolism (VTE) and stroke prevention in atrial fibrillation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **4 publications** currently supporting this direction — none of which directly test rivaroxaban as a treatment for RA.
Given the speculative mechanistic link and absence of direct clinical evidence, this prediction warrants significant caution before any further investment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Italy authorization data available |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on clinical trial references and known pharmacology, rivaroxaban is a direct Factor Xa inhibitor — it blocks the conversion of prothrombin to thrombin in the coagulation cascade, thereby preventing fibrin clot formation. It is widely used for DVT, pulmonary embolism, and stroke prevention in non-valvular atrial fibrillation.

The proposed connection to rheumatoid arthritis rests on an indirect biological pathway: systemic inflammation in RA chronically activates the coagulation cascade, leading to elevated thrombin generation. Factor Xa inhibition may theoretically modulate downstream inflammation via the PAR-2 (Protease-Activated Receptor-2) signalling pathway, and RA patients carry a substantially elevated VTE and cardiovascular thromboembolic risk compared to the general population. From this angle, the TxGNN model may have captured a real comorbidity pattern — RA patients frequently require anticoagulation — and translated it into a repurposing signal.

However, this mechanistic link is indirect and speculative. The available literature does not contain any study designed to test whether rivaroxaban modifies RA disease activity or outcomes. The TxGNN score reflects a knowledge-graph association rather than a validated disease-modifying hypothesis. This distinction is critical: anticoagulation *management in RA patients* is a legitimate clinical consideration, but it is not the same as rivaroxaban *treating RA*.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Rivaroxaban × Rheumatoid Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Thrombin generation assay (TGA) evaluated as a tool to screen hypercoagulable states in autoimmune diseases, including antiphospholipid syndrome; cardiovascular risk is regularly associated with autoimmune disease — provides indirect mechanistic background |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case Report | Cureus | 88-year-old patient with RA on oral steroids experienced recurrent embolic events in lower extremities and cerebral circulation despite ongoing anticoagulant therapy for AF — illustrates anticoagulation complexity in RA comorbidity, not RA disease modification |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Comprehensive review of lower extremity VTE diagnosis and treatment; DVT incidence 88–112/100,000 person-years, 10-year recurrence rate 20–36% — background context for anticoagulation need |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Observational | PLoS One | Adherence comparison of rivaroxaban vs apixaban in non-valvular AF; non-adherence associated with poor health outcomes — no RA relevance, background pharmacoepidemiology only |

> ⚠️ **Note:** None of the above publications directly investigates rivaroxaban as a treatment for rheumatoid arthritis. All are indirect background or comorbidity evidence.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data gaps identified in this Evidence Pack (DG001: Italy/AIFA package insert warnings and contraindications; DG002: full MOA characterisation) must be resolved before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score to this prediction, but the underlying evidence is entirely L5 — model-derived only — with no clinical trials and no publications directly testing rivaroxaban in RA. The proposed mechanistic link via PAR-2 signalling is biologically plausible but unvalidated, and the literature retrieved reflects RA as a VTE risk context rather than a therapeutic target for Factor Xa inhibition.

**To proceed, the following is needed:**

- **Fill DG001**: Retrieve Italy (AIFA) package insert warnings and contraindications to enable S1 safety screening
- **Fill DG002**: Query DrugBank API for full MOA characterisation and any preclinical inflammation data
- **Preclinical validation**: Identify or commission in vitro / in vivo studies testing Factor Xa inhibition in RA synovial models (PAR-2 pathway)
- **Reassess prediction ranking**: Consider redirecting investigation resources toward **Rank 3 (HIV infectious disease, L3 evidence)**, which has one completed Phase 2 trial (NCT00786422) and a clinically grounded hypothesis around DOAC use in HIV patients on ART — a more tractable and evidence-supported repurposing question
- **Italy regulatory clarification**: The Evidence Pack shows 0 Italy authorizations; verify whether Rivaroxaban (Xarelto®) is marketed in Italy under a different data source, as this may affect feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

