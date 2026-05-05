---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia / Stem Cell Mobilization to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF) widely used to treat chemotherapy-induced neutropenia and to mobilize hematopoietic stem cells (HSCs) for transplantation.
The TxGNN model predicts it may have potential relevance in **Primary Release Disorder of Platelets**, with a prediction score of **99.998%**.
However, supporting evidence is entirely indirect — consisting of **14 clinical trials** (all HSCT-related settings where filgrastim acts as a mobilization agent) and **1 publication** — placing this firmly at an early research-hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neutropenia management; hematopoietic stem cell mobilization for transplantation |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from the source database. Based on established pharmacology, filgrastim is a recombinant form of endogenous G-CSF that binds the G-CSF receptor (G-CSFR / CD114), driving proliferation, differentiation, and survival of neutrophil precursors in the bone marrow. Its well-established secondary effect — HSC mobilization from marrow into peripheral blood — is clinically exploited for donor and autologous stem cell collection prior to transplantation. This dual granulopoietic and mobilizing activity is the biological bridge underlying the TxGNN prediction.

The mechanistic rationale for primary release disorder of platelets is third-order and indirect. Filgrastim mobilises HSCs, which include megakaryocyte progenitors. In the context of allogeneic HSCT, engraftment of donor HSCs can repopulate the recipient's bone marrow de novo — theoretically correcting an underlying genetic defect in the platelet release machinery if one is present. The clinical trials retrieved all reflect this HSCT support role: filgrastim is used as a standard mobilization reagent, not as a direct treatment for any platelet disorder.

Importantly, no evidence exists that filgrastim independently modulates platelet dense granule secretion, the SNARE machinery, or downstream signalling cascades responsible for platelet release. The TxGNN prediction most likely arises from graph-level proximity in the biomedical knowledge graph between G-CSF pathway nodes and hematopoietic/platelet function nodes, rather than from a direct pharmacological action. Mechanistic plausibility is rated low-to-moderate at best, and the indication remains a research question requiring preclinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplantation for high-risk paediatric sarcomas; G-CSF used for donor mobilisation — provides indirect evidence that filgrastim-mobilised grafts can reconstitute full haematopoiesis including platelet lineage |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for patients with GATA2 mutations; filgrastim is an essential component of the donor mobilisation protocol; demonstrated feasibility of stem cell correction for genetic haematopoietic disorders |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | Randomised comparison of CD34+ selected vs. unselected autologous SCT in MCL/DLBCL; filgrastim serves as the standard mobilisation agent; relevant for understanding G-CSF's role in graft composition |
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for haematological malignancies; multi-arm study including donor lymphocyte infusion post-transplant; terminated early — limited conclusions available |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant with NK cells for myeloid leukaemia; filgrastim involved in recipient preparation; terminated with small sample (n=16) |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose optimisation of post-transplant cyclophosphamide combined with sirolimus/MMF for GVHD prophylaxis after reduced-intensity PBSC transplantation; G-CSF used for peripheral blood stem cell collection |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion followed by autologous HSCT for severe SLE; demonstrates filgrastim-mobilised autologous grafts can reset dysfunctional haematopoiesis in autoimmune contexts; very small cohort (n=9) |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform protocol testing PTCy-based GVHD prophylaxis in MMUD PBSC transplantation; G-CSF central to donor PBSC collection; ongoing, completion expected 2028 |

> **Important caveat:** None of the above trials were designed to evaluate filgrastim as a treatment for primary platelet release disorders. Filgrastim's role in all listed studies is as a mobilisation support agent within HSCT programmes. Relevance to the predicted indication is mechanistically indirect.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Clinical Study | Frontiers in Immunology | G-CSF administration in healthy donors preferentially mobilises specific lymphocyte subsets alongside HSCs; highlights that filgrastim reshapes the cellular composition of the mobilised graft beyond granulocytes, with implications for immune reconstitution post-HSCT |

---

## Italy Market Information

Filgrastim has **no registered product authorisations** in the Italy regulatory database reviewed for this analysis.

| Market Status | Authorizations | Data Source Date |
|---|---|---|
| Not Marketed | 0 | 2026-03-29 |

> This reflects data available in the source regulatory database at time of query. Current authorization status should be independently verified via official AIFA records, as filgrastim biosimilars are broadly available across the EU.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high prediction score (99.998%), the mechanistic connection between filgrastim and primary release disorder of platelets is a third-order inference (G-CSF → HSC mobilisation → HSCT → corrected megakaryocyte function), with no direct clinical trials or targeted publications. Evidence level L4 reflects mechanistic/indirect context only, and the evidence does not yet support a formal repurposing development path.

**To proceed, the following is needed:**

- **Preclinical mechanistic validation**: Determine whether any G-CSF signalling axis directly influences platelet dense granule biogenesis or the platelet release machinery (in vitro assays or patient-derived megakaryocyte models)
- **Complete MOA data**: Retrieve full mechanism of action from DrugBank (DB00099) to enable a proper mechanistic plausibility assessment
- **Targeted literature review**: Search for case reports or retrospective series documenting platelet function normalisation following G-CSF-mobilised HSCT in patients with documented platelet release disorders
- **Italy market verification**: Cross-check current AIFA authorisation database directly, as EU-approved filgrastim biosimilars may already carry relevant haematological indications
- **Safety profiling for target population**: Primary platelet release disorders often affect younger or paediatric patients; long-term G-CSF exposure risks (splenic rupture, bone pain, rare secondary AML in donors) must be assessed for this population specifically
- **Regulatory pathway scoping**: If preclinical data support the hypothesis, map the route to an orphan disease designation given the rarity of primary platelet release disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

