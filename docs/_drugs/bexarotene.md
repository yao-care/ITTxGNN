---
layout: default
title: Bexarotene
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 3
---

# Bexarotene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Bexarotene: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Bexarotene (Targretin) is a selective retinoid X receptor (RXR) agonist globally approved for the treatment of cutaneous T-cell lymphoma (CTCL), including mycosis fungoides and Sézary syndrome.
The TxGNN model predicts it may be effective for **Primary Cutaneous B-Cell Lymphoma (PCBCL)**,
with **2 clinical trials** and **13 publications** currently available — though evidence directly addressing PCBCL remains sparse, and the mechanistic basis for this prediction is weaker than for its established CTCL indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cutaneous T-Cell Lymphoma (CTCL) / Mycosis Fungoides (globally approved; no Italy authorisation) |
| Predicted New Indication | Primary Cutaneous B-Cell Lymphoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable for this evidence pack. Based on published literature included in the evidence set, bexarotene is a selective retinoid X receptor (RXR) agonist that binds and activates RXR nuclear transcription factors, leading to modulation of cell growth, apoptosis, and differentiation. In CTCL, this mechanism primarily induces apoptosis and terminal differentiation of malignant T-lymphocytes, and bexarotene is an established systemic agent for both early- and advanced-stage CTCL with an overall response rate of approximately 45–54% in refractory disease.

The mechanistic bridge to PCBCL is theoretically conceivable: both CTCL and PCBCL originate in the skin, and some preclinical data suggest that RXR agonists can promote B-lymphocyte differentiation through RAR/RXR signalling pathways. The TxGNN model's high prediction score (0.9944) most likely reflects shared cutaneous lymphoma genomic network architecture rather than a direct mechanistic signal. Notably, bexarotene achieves strong TxGNN scores for two closely related conditions in this evidence pack — Sézary syndrome (rank 2, 99.29%) and the broader lymphosarcoma category (rank 3, 99.12%) — where clinical evidence is substantially stronger.

However, PCBCL biology differs fundamentally from CTCL. PCBCL is dominated by BCL-2 overexpression and B-cell receptor signalling dependence rather than the skin-trafficking and T-cell apoptotic pathways that bexarotene targets. All available clinical trial data is from T-cell subtypes and cannot be directly extrapolated. Until preclinical evidence specifically validates RXR agonism in PCBCL models, this prediction warrants caution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05106192](https://clinicaltrials.gov/study/NCT05106192) | N/A | Withdrawn | 0 | Compared MedJet needle-free delivery system vs standard of care for cutaneous lymphoma plaques (both T- and B-cell types); study was withdrawn before any enrollment began. Primary agent was triamcinolone acetonide, not bexarotene — no efficacy or safety data available |
| [NCT01134341](https://clinicaltrials.gov/study/NCT01134341) | Phase 1 | Completed | 34 | Dose-finding study of pralatrexate + bexarotene in relapsed/refractory CTCL; enrolled exclusively T-cell lymphoma patients. Provides indirect Phase 1 safety and pharmacokinetic data for bexarotene combination use, but cannot serve as PCBCL efficacy evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31466585](https://pubmed.ncbi.nlm.nih.gov/31466585/) | 2019 | Clinical Management Review | Dermatologic Clinics | Comprehensive PCBCL diagnosis and management review; emphasises limited treatment guideline data and institutional variability; localized therapies preferred for indolent subtypes |
| [34059248](https://pubmed.ncbi.nlm.nih.gov/34059248/) | 2021 | Review | Medical Clinics of North America | Broad review of cutaneous T- and B-cell lymphomas covering clinical presentation, differential diagnosis, and therapeutic options |
| [14616487](https://pubmed.ncbi.nlm.nih.gov/14616487/) | 2003 | Clinical Guideline Review | Australasian Journal of Dermatology | Management review covering the full spectrum of primary cutaneous lymphomas; mentions retinoids as therapeutic options |
| [29881891](https://pubmed.ncbi.nlm.nih.gov/29881891/) | 2018 | Retrospective Case Series | Der Hautarzt | 163-patient case series of primary cutaneous lymphomas from daily clinical practice; describes epidemiology and subtype distribution |
| [19786826](https://pubmed.ncbi.nlm.nih.gov/19786826/) | 2009 | Experimental Therapy Review | Skin Pharmacology and Physiology | Reviews novel and experimental skin-directed therapies for both cutaneous T- and B-cell lymphomas; discusses bexarotene in this broader context |
| [31932947](https://pubmed.ncbi.nlm.nih.gov/31932947/) | 2020 | Review | Der Pathologe | Clinical overview of cutaneous lymphoma subgroups; explicitly names bexarotene as a systemic treatment option for Sézary syndrome and advanced-stage CTCL |
| [20806174](https://pubmed.ncbi.nlm.nih.gov/20806174/) | 2010 | Review | Therapeutische Umschau | Covers WHO/EORTC classification of cutaneous T- and B-cell lymphomas; provides epidemiological and nosological context |
| [22031653](https://pubmed.ncbi.nlm.nih.gov/22031653/) | 2011 | Case Report | Dermatology Online Journal | Case of recurrent primary cutaneous marginal-zone B-cell lymphoma managed with localized treatment; illustrates clinical management challenges in indolent PCBCL |
| [23941646](https://pubmed.ncbi.nlm.nih.gov/23941646/) | 2013 | Case Series / Subtype Description | Journal of Cutaneous Pathology | Describes diagnostic pitfalls in cutaneous follicular helper T-cell lymphoma initially misdiagnosed as PCBCL; highlights the critical importance of accurate B-cell vs T-cell subtyping |
| [15861527](https://pubmed.ncbi.nlm.nih.gov/15861527/) | 2005 | Case Report | Croatian Medical Journal | Rare co-occurrence of mycosis fungoides (CTCL) and EBV-associated cutaneous B-cell lymphoproliferative disease in one patient; topical acyclovir led to full clinical recovery of the B-cell component |

---

## Italy Market Information

Bexarotene is currently **not approved or marketed in Italy**. No marketing authorisations are on record with AIFA.

For reference, bexarotene (Targretin) holds FDA approval in the United States for the treatment of cutaneous manifestations of CTCL in patients refractory to at least one prior systemic therapy, and has received approval in Japan (2016) and some European markets.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Rexinoid (selective Retinoid X Receptor agonist); distinct from conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low to medium — neutropenia is reported; not typically the primary dose-limiting toxicity |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (for neutropenia); lipid panel (hypertriglyceridemia is frequent and often dose-limiting, may require lipid-lowering therapy); thyroid function — TSH and free T4 (central hypothyroidism is a well-documented class effect, prophylactic levothyroxine is often co-prescribed); liver function tests |
| Handling Protection | Standard cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from evidence pack literature:** The following adverse effects are consistently reported across multiple publications in this evidence pack: hypertriglyceridemia (frequent, often dose-limiting), central hypothyroidism (well-documented class effect requiring thyroid monitoring and often prophylactic levothyroxine), and neutropenia. Formal safety data from AIFA-approved labelling was not available as bexarotene holds no Italy authorisation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high score for bexarotene in PCBCL (99.44%) most likely reflects shared cutaneous lymphoma network features rather than a direct mechanistic link. All available clinical evidence is confined to T-cell lymphoma subtypes — there are no completed trials and no direct literature showing bexarotene activity in PCBCL. The L4 evidence level and fundamental differences in B-cell lymphoma biology mean this cannot advance beyond a research question at this stage. It is worth noting, however, that bexarotene carries substantially stronger evidence for the rank-2 prediction (Sézary syndrome), where it holds regulatory approval in multiple jurisdictions.

**To proceed, the following is needed:**

- **Preclinical validation:** In vitro studies evaluating bexarotene or other RXR agonists in PCBCL cell lines (marginal-zone, follicle-centre, and diffuse large B-cell subtypes), followed by in vivo xenograft models
- **Mechanistic characterisation:** Confirm whether RXR pathway activity is present and functionally relevant in primary PCBCL tumour biopsies
- **MOA data retrieval:** Obtain formal DrugBank mechanism-of-action data (currently a data gap)
- **Safety data:** Retrieve AIFA/EMA-aligned package insert warnings and contraindications; Italy market entry would require a separate regulatory strategy
- **Off-label case review:** Systematic search for any published case reports of bexarotene use specifically in PCBCL
- **Regulatory pathway assessment:** If preclinical data is supportive, consider a Phase 1/2 pilot trial with PCBCL-specific eligibility criteria and tissue-level biomarker endpoints (RXR expression, BCL-2 status)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

