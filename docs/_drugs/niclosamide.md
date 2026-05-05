---
layout: default
title: Niclosamide
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Niclosamide
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

Using the `txgnn-pipeline` skill to guide report generation. Now producing the evaluation report from the Evidence Pack.

---

# Niclosamide: From Tapeworm Infection to Heart Disease

## One-Sentence Summary

Niclosamide is an FDA-approved anthelmintic drug originally used to treat tapeworm (helminthic) infections, classified as an WHO Essential Medicine.
The TxGNN model predicts it may be effective for **Heart Disease**,
with **3 clinical trials** (all withdrawn or terminated) and **15 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anthelmintic — tapeworm/helminthic infections (cestodiasis) |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information from the supporting literature, niclosamide is a salicylanilide anthelmintic whose repurposing potential for heart disease rests on several distinct pharmacological pathways identified in recent mechanistic and preclinical research.

Four plausible biological links to cardiac pathology have emerged: **(1) STAT3 inhibition** — niclosamide suppresses STAT3 signaling, which reduces pathological cardiac hypertrophy and attenuates adverse structural remodeling under chronic pressure overload, directly demonstrated in a murine heart failure model (PMID 34736968); **(2) Wnt/β-catenin inhibition** — suppression of this pathway limits cardiac fibrosis and remodeling, a major driver of progressive heart failure; **(3) TMEM16A/F ion channel modulation** — niclosamide modulates calcium-activated chloride channels that regulate vascular tone and platelet procoagulant activity, with potential relevance to hypertension and thrombosis (PMID 38814250, 36684586); and **(4) anti-calcification in valve tissue** — niclosamide inhibits osteogenic transformation of human valvular interstitial cells via the AMPK/mTOR pathway, with possible application to calcific aortic valve disease (PMID 39515588).

Although helminthic infection and cardiac disease appear mechanistically unrelated, niclosamide's broad pleiotropic effects on STAT3, Wnt, mTOR, and mitochondrial uncoupling converge on pathways central to heart failure, valve calcification, and ischemic injury. One important caveat: TMEM16A potentiation has been associated with vasoconstriction (PMID 38814250, 40491382), which may represent an adverse cardiovascular effect that requires careful characterization before any clinical translation.

---

## Clinical Trial Evidence

> ⚠️ **Important:** None of the three identified trials were designed to evaluate niclosamide specifically for heart disease. All are withdrawn or terminated. Indirect relevance to cardiac outcomes comes through COVID-19–associated cardiac injury mechanisms. Dedicated heart disease trials are currently absent.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03521232](https://clinicaltrials.gov/study/NCT03521232) | Phase 1/2 | Terminated | 27 | Open-label study of niclosamide enemas (150 mg and 450 mg) in mild-to-moderate ulcerative proctitis/procto-sigmoiditis; the only trial with actual patient enrollment — provides preliminary safety and pharmacokinetic data. Termination reasons require clarification to assess safety signal risk. |
| [NCT04542434](https://clinicaltrials.gov/study/NCT04542434) | Phase 2 | Withdrawn | 0 | Randomized, double-blind, placebo-controlled study of oral niclosamide in adults with moderate COVID-19 with gastrointestinal symptoms; withdrawn before any enrollment. Study design confirms community recognition of niclosamide's Phase 2 potential but yields no efficacy or safety data. |
| [NCT04372082](https://clinicaltrials.gov/study/NCT04372082) | Phase 3 | Withdrawn | 0 | Combination of hydroxychloroquine + diltiazem + niclosamide for mild COVID-19 in patients with comorbidities including cardiovascular disease; withdrawn before enrollment. Indirect relevance to cardiac outcomes only through COVID-19 complication prevention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34736968](https://pubmed.ncbi.nlm.nih.gov/34736968/) | 2021 | Animal study (murine) | European Journal of Pharmacology | **Most direct evidence:** niclosamide attenuates pressure-overload induced heart failure in mice by enhancing mitochondrial respiration and ATP production in cardiomyocytes |
| [39515588](https://pubmed.ncbi.nlm.nih.gov/39515588/) | 2024 | In vitro (human cells) | Biochemical Pharmacology | Niclosamide inhibits calcification of human valvular interstitial cells via AMPK/mTOR suppression; supports application in calcific aortic valve disease |
| [38288981](https://pubmed.ncbi.nlm.nih.gov/38288981/) | 2024 | Nanoplatform study | ACS Applied Materials & Interfaces | Platelet-membrane-encapsulated niclosamide nanoparticles suppress ROS and activate STAT3/Bcl-2 pathway to protect against myocardial injury in mice |
| [38814250](https://pubmed.ncbi.nlm.nih.gov/38814250/) | 2024 | Mechanistic study | Journal of General Physiology | Niclosamide potentiates TMEM16A under physiological Ca²⁺ levels, inducing vasoconstriction — indicates complex vascular effects and a potential safety concern |
| [39102426](https://pubmed.ncbi.nlm.nih.gov/39102426/) | 2024 | Mechanistic/Translational | PLoS Pathogens | SARS-CoV-2 spike-induced senescent syncytia contribute to exacerbated heart failure; niclosamide's TMEM16 inhibition may limit syncytia-mediated cardiac injury in long COVID |
| [36684586](https://pubmed.ncbi.nlm.nih.gov/36684586/) | 2022 | In vitro mechanistic | Frontiers in Cardiovascular Medicine | SARS-CoV-2 spike activates TMEM16F-mediated platelet procoagulant activity (thrombosis); niclosamide identified as one of the most effective inhibitors in an FDA/EMA-approved drug screen of >3,000 compounds |
| [33827113](https://pubmed.ncbi.nlm.nih.gov/33827113/) | 2021 | In vitro mechanistic | Nature | Niclosamide (as TMEM16 inhibitor) blocks SARS-CoV-2 spike–induced multinucleated syncytia in pneumocytes; implicates TMEM16 axis in COVID-19–related pulmonary and cardiac pathology |
| [41453737](https://pubmed.ncbi.nlm.nih.gov/41453737/) | 2026 | Mechanistic | American Journal of Transplantation | TMEM16F-CLIC1 interaction mediates recipient dendritic cell cross-decoration following heart transplantation; niclosamide's TMEM16 modulation may have implications for transplant rejection |
| [40133574](https://pubmed.ncbi.nlm.nih.gov/40133574/) | 2025 | Bioinformatics/scRNA-seq | Scientific Reports | Identifies Hippo pathway biomarkers (NAMPT, CXCL1, CREM) in acute myocardial infarction subtypes; provides genomic context for niclosamide's Wnt/STAT3 inhibition as a cardioprotective target |
| [29736201](https://pubmed.ncbi.nlm.nih.gov/29736201/) | 2018 | Animal study | American Journal of Translational Research | Niclosamide ethanolamine salt improves type 1 diabetes and diabetic kidney disease in mice; metabolic benefits are indirectly relevant to diabetic cardiomyopathy prevention |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Additional note:** A vasoconstriction signal from TMEM16A potentiation (PMID 38814250) has been identified in the literature. This represents a potential cardiovascular adverse effect that should be specifically evaluated in any future cardiac indication development program, particularly in patients with hypertension or coronary artery disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite compelling mechanistic hypotheses and direct animal-model evidence for heart failure (PMID 34736968), there are currently no completed clinical trials evaluating niclosamide for any heart disease indication, package insert safety data is unavailable for review, and the drug is not marketed in Taiwan. The evidence base remains at the preclinical/mechanistic stage (L3), insufficient to justify advancing toward clinical development without additional foundational work.

**To proceed, the following is needed:**

- **Safety data retrieval:** Obtain and review the full niclosamide package insert (TFDA/FDA/EMA) for warnings, contraindications, and organ toxicity profile — currently a blocking data gap
- **Vascular safety clarification:** Characterize the TMEM16A potentiation–vasoconstriction interaction (PMID 38814250) in a cardiovascular safety study before exposing cardiac patients
- **MOA confirmation:** Query DrugBank (DB06803) for complete mechanism of action, target binding profile, and pharmacokinetic data
- **Drug-drug interaction assessment:** Screen for interactions relevant to cardiac co-medications (antihypertensives, anticoagulants, antiplatelets, statins)
- **Focused preclinical program:** Establish a dose-response and tolerability profile specifically in validated cardiac disease models (pressure-overload HF, calcific aortic valve disease)
- **Regulatory pathway scoping:** Assess feasibility of a new indication filing in Taiwan or other jurisdictions given current zero-license status
- **Phase 1 study design:** Upon satisfactory preclinical safety, design a dedicated Phase 1 cardiac trial (suggested target: heart failure with reduced ejection fraction or calcific aortic valve disease) with biomarker endpoints (STAT3 activity, echocardiographic parameters, valve calcification scores)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

