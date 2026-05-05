---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

The txgnn-pipeline skill confirms this is standard TxGNN repurposing output processing. Now generating the report from the Evidence Pack.

---

# Celecoxib: From Arthritis to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor globally approved for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis, though it currently holds no marketing authorization in Italy.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (encompassing ankylosing spondylitis and axial spondyloarthritis),
with **19 clinical trials** and **20 publications** currently supporting this direction — including multiple completed Phase 3 randomized controlled trials establishing **Level 1 evidence**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Globally approved for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis; no Italian authorization on record |
| Predicted New Indication | Inflammatory Spondylopathy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the primary data source. Based on published evidence, Celecoxib is the first selective cyclooxygenase-2 (COX-2) inhibitor introduced into clinical practice. It was specifically designed to provide anti-inflammatory and analgesic efficacy comparable to non-selective NSAIDs, while sparing COX-1 to reduce upper gastrointestinal toxicity. By selectively blocking COX-2, celecoxib suppresses the synthesis of pro-inflammatory prostaglandins — particularly PGE₂ — which are central mediators of pain, joint swelling, entheseal inflammation, and tissue destruction in inflammatory musculoskeletal diseases.

Inflammatory spondylopathy (ankylosing spondylitis / axial spondyloarthritis) is a chronic inflammatory disease in which the COX-2-mediated prostaglandin cascade plays a particularly prominent pathological role. Celecoxib's predicted benefit operates through at least three converging mechanisms: **(1)** reducing synovial and entheseal inflammation; **(2)** inhibiting osteoclast activation to slow erosive bone damage; and **(3)** — most notably, a 2025 meta-analysis demonstrated that celecoxib is the **only NSAID** shown to inhibit radiographic syndesmophyte (spinal bridging bone) formation, implying a direct bone-modifying effect beyond classical anti-inflammation, with the precise mechanism still under active investigation.

The biological and clinical logic connecting celecoxib to inflammatory spondylopathy is exceptionally strong. Published EU regulatory reviews confirm that celecoxib (Celebrex®) is already indicated in the European Union for symptomatic treatment of ankylosing spondylitis in adults. The TxGNN prediction therefore reflects an existing global evidence base that has not yet been formalised into an Italian marketing authorisation — making this a market access opportunity rather than a purely exploratory repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week double-blind RCT: Celecoxib 200mg QD vs 200mg BID vs Diclofenac 75mg SR BID in AS — compared safety and efficacy across dose regimens |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | 6-week double-blind RCT with 6-week extension in Chinese AS patients: Celecoxib 200mg QD vs Diclofenac 75mg SR — assessed symptom relief and safety |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week double-blind dose-confirmation trial: Celecoxib 200mg QD vs 400mg QD vs Diclofenac TID in AS — confirmed post-marketing efficacy and safety data |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | 54-week open-label RCT: Etanercept + Celecoxib vs Etanercept alone vs Celecoxib alone in active AS — primary endpoint MRI SPARCC score of sacroiliac joint |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: Celecoxib + Golimumab vs Golimumab monotherapy in AS — evaluated impact on radiographic structural damage progression over 2 years |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | MRI pilot study: NSAID effect on inflammatory lesion resolution in axial spondyloarthritis — assessed change from baseline in bone marrow oedema |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing selective COX-2 vs non-selective COX inhibitors in axSpA — examined disease activity improvement and proteomic biomarkers |
| [NCT01572675](https://clinicaltrials.gov/study/NCT01572675) | N/A | Completed | 547 | French pharmacoepidemiology study on etoricoxib and celecoxib (Celebrex®) in routine clinical practice — real-world utilisation patterns |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | 6-week double-blind RCT comparing 4 NSAIDs in axial spondyloarthritis — assessed pain score change at week 4 vs week 6 |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Phase 2 | Unknown | 300 | Registry project: Adalimumab + NSAIDs vs Adalimumab alone in ankylosing spondylitis — assessed safety and efficacy of combination strategy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic Review / Meta-analysis | BMB Reports | Celecoxib is the **only NSAID** demonstrated to inhibit radiographic bone progression in spondyloarthritis — proposed mechanism distinct from pure COX inhibition |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella Review | Drugs | Systematic synthesis of meta-analyses on celecoxib safety in chronic musculoskeletal conditions — comprehensive evaluation of cardiovascular, GI, and renal safety signals |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Iguratimod + celecoxib vs celecoxib alone in active axSpA — randomised double-blind placebo-controlled trial assessing add-on efficacy and safety |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Annals of the Rheumatic Diseases | CONSUL trial results: adding celecoxib to golimumab did not significantly reduce radiographic spinal progression over 2 years vs TNFi monotherapy |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT / Clinical Study | Clinical Rheumatology | Imrecoxib and celecoxib both modulate sacroiliac joint inflammation in axSpA via changes in bone metabolism markers and angiogenesis indices |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Celecoxib 200mg BID vs imrecoxib 100mg BID in axSpA over 12 weeks — equivalent efficacy; both influenced serum DKK-1 levels correlated with imaging improvement |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Comparative Cohort | Scandinavian Journal of Rheumatology | Nationwide retrospective cohort in AS: cardiovascular disease and GI bleeding risk comparable between celecoxib and non-selective NSAIDs |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | The Journal of Rheumatology | Celecoxib is efficacious and well tolerated in treating signs and symptoms of ankylosing spondylitis — foundational Phase 3 efficacy data |
| [27603385](https://pubmed.ncbi.nlm.nih.gov/27603385/) | 2016 | Population-based Cohort | Medicine | Taiwan NHI database (n=4,829 AS patients): celecoxib and sulfasalazine use negatively associated with coronary artery disease risk in AS |
| [17983259](https://pubmed.ncbi.nlm.nih.gov/17983259/) | 2007 | Comprehensive Drug Review | Drugs | Celecoxib approved in multiple countries for OA, RA, JRA (≥2 years), and AS — decade of clinical practice review confirming broad musculoskeletal indication profile |

---

## Italy Market Information

Celecoxib currently holds no marketing authorization in Italy. There are no approved products, dosage forms, or licensed indications on record in the Italian regulatory database.

> Note: Celecoxib (Celebrex®) is authorized in the European Union for the symptomatic treatment of osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis in adults, per published EU regulatory reviews. An Italian market entry would require submission to AIFA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (key warnings, contraindications, drug-drug interactions) were not retrievable from the Italian regulatory database for this drug. Clinical evidence in the literature does document cardiovascular and gastrointestinal risk profiles (see PMID [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) and [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/)), which should be reviewed as part of any regulatory submission or clinical protocol.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs and multiple Phase 4 trials directly evaluating celecoxib in ankylosing spondylitis / inflammatory spondylopathy establish L1 evidence. Celecoxib is already EU-approved for this indication in principle, and a 2025 meta-analysis suggests it may be the only NSAID with disease-modifying potential in spondyloarthritis — a clinically significant differentiator.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate AIFA marketing authorisation application for the ankylosing spondylitis / inflammatory spondylopathy indication, leveraging existing EMA evidence package
- **MOA documentation**: Obtain complete mechanism of action data from DrugBank (DB00482) to support regulatory dossier and mechanistic rationale
- **Safety dossier**: Retrieve AIFA SmPC / package insert for full Italian-compliant contraindications, warnings, and special population guidance
- **Drug interaction assessment**: Formal DDI review for co-prescribing with TNF inhibitors (etanercept, golimumab, adalimumab), DMARDs, and corticosteroids — common in the target spondyloarthritis population
- **Cardiovascular risk plan**: Define cardiovascular risk stratification and monitoring protocol for the target patient population, accounting for the known class-level COX-2 selective inhibitor cardiovascular signal
- **Paediatric consideration**: Clarify whether the Italian submission will include the JIA/RF+ pJIA indication, given FDA approval for celecoxib in JIA patients ≥2 years (evidence: PMID [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/))
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

