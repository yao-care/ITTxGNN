---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Inflammatory Conditions to Atopic Eczema

## One-Sentence Summary

Budesonide is a potent synthetic glucocorticoid used globally for asthma, COPD, allergic rhinitis, and inflammatory bowel conditions; however, no approved indication is currently recorded in the Italian AIFA database.
The TxGNN model predicts it may be effective for **Atopic Eczema**, based on its mechanism of suppressing Th2 cytokines that are central to this skin disease.
Current evidence consists of **2 retrieved clinical trials** (neither directly evaluating budesonide for eczema) and **20 publications** — with the strongest direct support being a 2024 preclinical nanoparticle formulation study — placing the overall evidence level at **L4**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication found in Italian AIFA database |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Budesonide is a potent synthetic glucocorticoid that exerts its anti-inflammatory effects by binding to intracellular glucocorticoid receptors (GR). Once bound, it suppresses the transcription of key Th2 cytokines — including IL-4, IL-5, and IL-13 — while simultaneously inhibiting eosinophil recruitment and reducing NF-κB-driven inflammatory cascades. Detailed MOA data from DrugBank was not available for this evaluation; the mechanism described here is based on established pharmacological knowledge and the repurposing rationale provided in the evidence pack.

Atopic eczema (ICD-10 L20) is primarily driven by a Th2-dominant inflammatory response, characterized by elevated IL-4/IL-13 signaling, impaired skin barrier function, and eosinophilic tissue infiltration. Budesonide's mechanism of directly suppressing these same cytokine pathways provides a mechanistically coherent rationale for its potential utility in this indication. In fact, topical corticosteroids broadly are already a first-line treatment for atopic dermatitis — the question for this repurposing candidate lies in whether budesonide specifically, particularly in novel delivery formats, offers meaningful advantages.

One additional note of caution: TxGNN ranked both "atopic eczema" (rank #1, score 99.96%) and "dermatitis, atopic" (rank #3, score 99.81%) as separate predictions. These are clinically the same entity (ICD-10 L20), suggesting the model is predicting the same indication from two different knowledge graph nodes. The most direct human evidence in the literature comes from PMID 38275852 (2024), which developed pH-sensitive budesonide nanoparticle hydrogels explicitly designed for pediatric atopic dermatitis, confirming the recognized pharmacological rationale. However, this remains a preclinical formulation study.

---

## Clinical Trial Evidence

Neither of the two retrieved trials directly evaluates budesonide as a treatment for atopic eczema. Both are Grade C — atopic disease appears as a background enrollment criterion or co-morbidity, not as the primary treatment target.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | NA | Unknown | 150 | Characterizes severe pediatric asthma endotypes using immune, metabolomics, and microbial analyses; atopy (including eczema) is a background phenotypic variable, not a treatment endpoint — not applicable as budesonide-for-eczema evidence |
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy (not budesonide) in atopic wheezing children at high risk for asthma; eczema is listed as an enrollment risk factor — not applicable as direct treatment evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical / Formulation | Gels (Basel) | Budesonide-loaded Eudragit L100 nanoparticles formulated into pH-sensitive hydrogels for local therapy of pediatric atopic dermatitis; exploits pH changes in atopic lesions for targeted release — strongest direct evidence available, but preclinical only |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | Veterinary RCT | J Vet Pharmacol Ther | Randomized, blinded, placebo-controlled crossover trial (n=29 dogs) of 0.025% budesonide leave-on conditioner (Barazone) for canine atopic dermatitis; significantly reduced skin lesions and pruritus — only controlled trial evidence, but in a non-human model |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Clinical Study | Pediatric Dermatology | Knemometry study in 14 children (5–12y) with atopic dermatitis treated with topical budesonide; detected measurable systemic glucocorticoid activity — confirms dermal absorption and systemic safety concern in children |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Clinical Study | Dermatology (Basel) | Topical glucocorticosteroids in children with atopic dermatitis assessed for effects on IGF axis, bone collagen turnover; percutaneous absorption confirmed — relevant safety baseline for pediatric topical use |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | Prospective Clinical | Allergologia et Immunopathologia | Differential budesonide response in atopic vs. non-atopic infants with recurrent wheezing; atopic status modulated therapeutic response — indirect evidence of pharmacological sensitivity in the atopic phenotype |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Cross-sectional | Contact Dermatitis | Italian SIDAPA baseline patch-test series (2018–2019): budesonide allergy frequency has declined over two decades; confirms budesonide remains the standard corticosteroid hypersensitivity marker in Italy |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | Contact Dermatitis | Contact sensitization patterns in Asian dermatology patients with and without atopic dermatitis; similar or higher patch-test positivity in AD patients — relevant safety signal for topical budesonide use |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Review | J Allergy Clin Immunol | Review of emerging EoE therapies; swallowed topical corticosteroids (including budesonide) are current standard off-label treatment — demonstrates established mucosal anti-inflammatory role with shared Th2 mechanistic basis |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid hypersensitivity in asthma patients; budesonide identified as causing delayed contact allergy — safety signal directly relevant to topical application in atopic patients |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids and HPA axis suppression; discusses systemic safety in patients with comorbid allergic rhinitis and atopic dermatitis — supports need for systemic monitoring in polytherapy contexts |

---

## Italy Market Information

Budesonide is not registered in the Italian AIFA database. No authorized product records are available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Important Safety Signal Identified in the Literature**: Multiple independent studies — including PMID 30053491, 24603519, 35184304, 19183418, and 37550231 — consistently report that budesonide is a recognized contact allergen in patients with atopic dermatitis, falling within the Group B corticosteroid cross-reactivity cluster. This creates a therapeutic paradox: the intended anti-inflammatory agent may itself act as a sensitizing hapten in the target patient population. This finding is specific to topical administration routes and must be addressed as a priority safety concern before any clinical investigation in atopic eczema proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for budesonide in atopic eczema is pharmacologically coherent (GR-mediated Th2 suppression), but current evidence is limited to preclinical formulation work and indirect clinical signals. Critically, a well-documented contact sensitization risk in the exact target population creates a safety concern that must be resolved before advancing this candidate.

**To proceed, the following is needed:**

- **Safety data gap resolution**: Obtain Italian AIFA package insert (Data Gap DG001 — Blocking) and DrugBank MOA data (Data Gap DG002 — High) before any further evaluation stages
- **Contact sensitization risk assessment**: Conduct formal patch-test screening protocol for budesonide hypersensitivity in prospective atopic dermatitis patients; consider Group B corticosteroid cross-reactivity profiling
- **Human clinical trial evidence**: No RCT or prospective human study directly evaluating budesonide for atopic eczema currently exists — a Phase 2 proof-of-concept trial is required to advance to L2 evidence
- **Novel delivery strategy**: If pursuing this indication, prioritize nanoparticle or encapsulated delivery systems (as explored in PMID 38275852) to reduce direct sensitizer exposure and improve local drug concentration
- **Knowledge graph deduplication**: "Atopic eczema" (rank #1) and "Dermatitis, atopic" (rank #3) are the same clinical entity (ICD-10 L20); these two TxGNN predictions should be merged in the pipeline to avoid double-counting evidence and recommendations
- **Evaluate rank #2 (Bronchitis) as higher-priority candidate**: The bronchitis indication carries L2 evidence with a meta-analysis and systematic review directly involving budesonide, and a "Proceed with Guardrails" recommendation — this may represent a more immediate repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

