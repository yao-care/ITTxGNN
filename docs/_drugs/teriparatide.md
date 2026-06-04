---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Postmenopausal Osteoporosis to Pregnancy-Associated Osteoporosis

## One-Sentence Summary

Teriparatide (PTH 1-34) is a recombinant parathyroid hormone analogue approved globally for the anabolic treatment of osteoporosis in postmenopausal women and men at high fracture risk.
The TxGNN model predicts it may be effective for **Pregnancy-Associated Osteoporosis (PLO)**, with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (postmenopausal women; men with primary or hypogonadal osteoporosis; glucocorticoid-induced osteoporosis) |
| Predicted New Indication | Pregnancy Associated Osteoporosis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Teriparatide is a synthetic 34-amino acid N-terminal fragment of human parathyroid hormone (PTH 1-34) that acts as a full agonist at the PTH1 receptor (PTH1R). Unlike conventional antiresorptive agents (bisphosphonates, denosumab), it works anabolically — directly stimulating osteoblast differentiation and activity, increasing bone mineral density (BMD), improving trabecular microarchitecture, and reducing vertebral and non-vertebral fracture risk. Detailed MOA data from DrugBank was not available in this evidence pack; the characterisation above is based on the published pharmacological literature.

Pregnancy- and lactation-associated osteoporosis (PLO) is a rare but severe condition in which the maternal skeleton cannot compensate for the calcium demands of fetal development and breastfeeding. During lactation, the mammary gland and placenta secrete large quantities of PTHrP (PTH-related protein), which signals through the same PTH1R receptor as teriparatide, driving accelerated osteoclastic bone resorption. The result is rapid BMD loss concentrated in the trabecular-rich spine, sometimes producing multiple vertebral compression fractures in otherwise healthy young women. The pathological driver of PLO and the therapeutic mechanism of teriparatide therefore converge on the same receptor axis.

Because teriparatide shares the PTH1R target with the endogenous instigator of PLO-related bone loss, its use as a therapeutic agent to shift receptor signalling from resorption toward formation is mechanistically coherent. This is further supported by a growing body of retrospective cohort studies, systematic reviews, and meta-analyses that have specifically evaluated teriparatide in PLO patients, consistently demonstrating BMD recovery at the lumbar spine and reduction in subsequent fracture risk. The TxGNN prediction reflects a biologically credible and clinically emerging extension of teriparatide's established bone-anabolic profile.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Renal osteodystrophy and CKD-associated osteoporosis; provides supportive safety and efficacy context for teriparatide in metabolic bone diseases characterised by disrupted mineral homeostasis — a pathophysiological domain overlapping with PLO |
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | PTH 1-34 (Forteo) combined with periodontal surgery for oral bone regeneration; confirms PTH1R-mediated osteogenic mechanism and the basic safety profile of subcutaneous teriparatide dosing |

> **Note:** No registered clinical trials directly studying teriparatide in PLO were identified. The two trials above provide indirect mechanistic and safety support. The main evidence base for this indication comes from observational literature.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic Review & Meta-analysis | *Osteoporosis International* | 35 studies, 943 patients; comprehensive analysis of presentation, risk factors, and treatment response in pregnancy-associated osteoporosis; vertebral fractures and back pain were the dominant features |
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic Review & Meta-analysis | *J Clin Endocrinol Metab* | Comparative effectiveness of therapeutic interventions in PLO; teriparatide evaluated alongside bisphosphonates and other anabolic agents as a key treatment modality |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Clinical Review | *Endocrine* | Focused review of teriparatide use in PLO; identifies it as a promising anabolic strategy for spine fractures occurring during late pregnancy or the postpartum lactation period |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Cohort Study | *Calcified Tissue International* | Multicenter retrospective cohort, 19 women treated with teriparatide 20 µg/day vs. conventional management in PLO; teriparatide group showed superior lumbar spine BMD and trabecular bone score (TBS) recovery |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Cohort Study | *Geburtshilfe und Frauenheilkunde* | 47 patients with PLO and postpartum vertebral fractures (mean 4 fractures/patient) treated with teriparatide; assessed impact on subsequent fracture incidence and BMD |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Cohort Study | *Calcified Tissue International* | Retrospective study of bone density trajectories after teriparatide discontinuation in PLO, with or without sequential antiresorptive therapy; addresses a key clinical management gap |
| [36764958](https://pubmed.ncbi.nlm.nih.gov/36764958/) | 2023 | Case Report | *Calcified Tissue International* | Severe PLO with multiple vertebral fractures treated with teriparatide followed by zoledronic acid; high-resolution imaging documented substantial improvements in bone microarchitecture and strength |
| [39976715](https://pubmed.ncbi.nlm.nih.gov/39976715/) | 2025 | Review | *Z Rheumatologie* | Risk factors, fracture patterns, and treatment strategies for PLO; teriparatide and bisphosphonates identified as best pharmacological options for severe cases |
| [33620518](https://pubmed.ncbi.nlm.nih.gov/33620518/) | 2022 | Review | *Calcified Tissue International* | Comprehensive review of PLO pathogenesis, skeletal fragility features, and treatment landscape including teriparatide and emerging biologics |
| [40837111](https://pubmed.ncbi.nlm.nih.gov/40837111/) | 2025 | Review | *J Endocrine Society* | Reviews calcium physiology during pregnancy and lactation, PTHrP-driven bone resorption mechanisms, and their relevance to PLO — directly supports the mechanistic rationale for teriparatide |

---

## Italy Market Information

Teriparatide is **not currently authorised in Italy**. No marketing authorizations were found in the regulatory database. Teriparatide is, however, authorised in the European Union under the brand names **Forsteo** (Eli Lilly) and generic formulations via EMA centralised procedure; Italy-specific AIFA registration should be verified independently.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings and contraindications (including the osteosarcoma black-box warning applicable in other markets) were not available in this evidence pack. These are critical to evaluate before any use in the PLO population, particularly given that PLO affects premenopausal women of childbearing age — a population that may not be covered by standard teriparatide prescribing guidelines.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple retrospective cohort studies and two independent systematic reviews with meta-analyses directly document teriparatide's efficacy in PLO — a condition driven by the same PTH1R receptor pathway that teriparatide targets. While no randomised controlled trials in PLO have been completed (largely due to the rarity of the condition), the mechanistic coherence and consistent observational evidence across international centres support an L3 evidence classification and justify conditional advancement.

**To proceed, the following is needed:**

- Obtain the full EMA/AIFA-authorised package insert for teriparatide (Forsteo) to review contraindications, particularly the osteosarcoma risk signal (Paget's disease, prior radiation, unexplained elevation of alkaline phosphatase) and its applicability to premenopausal PLO patients
- Retrieve MOA data from DrugBank (DB06285) to formally document the PTH1R agonist pharmacology and receptor binding kinetics
- Define the sequential therapy strategy: teriparatide in PLO is typically followed by antiresorptive consolidation (bisphosphonate or denosumab); a clinical protocol for this transition should be specified
- Confirm that Italian AIFA registration status for Forsteo (or biosimilars) is current and that the indication can be pursued as a labelled off-label use or through a dedicated expanded indication pathway
- Assess the feasibility of a prospective observational registry or adaptive trial in PLO given the rarity of the condition (estimated incidence < 1:10,000 pregnancies)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

