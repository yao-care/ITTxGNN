---
layout: default
title: Flunisolide
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Flunisolide
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

The txgnn-pipeline skill confirms this is TxGNN report work. Now I'll produce the Evaluation Report following the v5 format precisely.

---

# Flunisolide: From Asthma/Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Flunisolide is an inhaled corticosteroid (ICS) approved for the treatment of asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **Atopic Eczema**,
with **no clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / Allergic Rhinitis (ICS class, approved use) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Flunisolide is a synthetic fluorinated corticosteroid belonging to the inhaled corticosteroid (ICS) class. It exerts its effects by binding to glucocorticoid receptors, suppressing the transcription of pro-inflammatory cytokines, reducing eosinophil infiltration, and dampening mucosal immune activation. Its efficacy in asthma and allergic rhinitis has been well established through decades of clinical use.

Atopic eczema (atopic dermatitis) is driven by Th2-mediated immune dysregulation — the same inflammatory axis that corticosteroids broadly suppress. This mechanistic overlap explains why topical corticosteroids are the first-line standard of care for atopic dermatitis, and it is plausible that the TxGNN graph neural network identified this shared disease biology as a potential link to Flunisolide.

However, a critical limitation must be noted: Flunisolide is formulated exclusively as an inhaler and nasal spray. Atopic eczema requires topical application to skin, making direct repurposing of the existing formulation infeasible. Any translational effort would require dedicated pharmaceutical development of a topical Flunisolide preparation — a substantial additional step beyond standard repurposing. The model's prediction reflects class-level pharmacology, not formulation readiness.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18926054](https://pubmed.ncbi.nlm.nih.gov/18926054/) | 2008 | Observational/Biomarker | Allergy and Asthma Proceedings | Measured exhaled breath condensate (EBC) pH and Th1/Th2/Treg cytokines in children with asthma and atopic dermatitis; assessed whether inhaled corticosteroid treatment affects cytokine concentrations — provides mechanistic context linking ICS effects to AD immunology, but does not study Flunisolide as a treatment for AD |

---

## Italy Market Information

Flunisolide currently holds no marketing authorizations in Italy. No product is approved or commercially available on the Italian market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Flunisolide in atopic eczema is limited to a single observational biomarker study that does not directly evaluate Flunisolide as a treatment; additionally, the drug's inhaled/nasal spray formulation is fundamentally incompatible with the topical route required for atopic eczema, creating a pharmacological and regulatory barrier that standard repurposing cannot overcome without new formulation development.

**To proceed, the following is needed:**
- Clarification of the target route of administration: if topical delivery is intended, a dedicated topical formulation (cream/ointment) of Flunisolide must be developed and tested separately
- Retrieval of the full package insert (TFDA/EMA) to assess safety warnings, contraindications, and systemic absorption data relevant to any new route
- Mechanism of action data from DrugBank to formally validate the ICS–atopic dermatitis immunological link
- At minimum one controlled observational study or pilot clinical trial specifically evaluating Flunisolide (in any formulation) for atopic eczema before advancing to higher decision stages
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

