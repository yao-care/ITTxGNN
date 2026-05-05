---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

以下是根據 Evidence Pack 生成的藥師評估報告。由於 TxGNN 排名第 1–8 的預測均為 L5/Hold 且無任何機轉關聯，本報告聚焦於證據最充分、最具臨床可行性的第 10 名預測：幼年型特發性關節炎（JIA）。

---

# Piroxicam: From Rheumatic & Musculoskeletal Pain to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is a non-selective COX-1/COX-2 inhibitor (NSAID) with decades of clinical use for inflammatory and musculoskeletal conditions, including rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **Juvenile Idiopathic Arthritis (JIA)**, with **0 registered clinical trials** and **13 publications**—including two direct piroxicam-vs.-naproxen controlled trials in pediatric patients—currently supporting this direction.
Note: TxGNN's highest-scoring predictions (ranks 1–8) are rare genetic skeletal dysplasia syndromes with no mechanistic link to COX inhibition and no supporting evidence (all L5/Hold); JIA (rank 10) is selected here as the most actionable and mechanistically coherent target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Taiwan regulatory data (not marketed in Taiwan); globally established for rheumatoid arthritis, osteoarthritis, and musculoskeletal pain |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal mechanism of action data is listed as a data gap in this evidence pack. However, piroxicam's pharmacology is extensively documented in the global literature: it non-selectively inhibits both COX-1 and COX-2 enzymes, blocking the conversion of arachidonic acid to prostaglandins and thereby reducing PGE2 synthesis—a central mediator of pain, fever, and joint inflammation.

The core pathology of JIA is chronic synovitis driven by T-cell activation and pro-inflammatory cytokines (IL-1, IL-6, TNF-α), with PGE2 playing a key role in perpetuating joint swelling and pain. Piroxicam directly targets this inflammatory cascade. NSAIDs are endorsed as first-line symptomatic treatment for JIA by both EULAR and ACR guidelines, making the mechanistic connection between piroxicam and JIA straightforward.

Crucially, the evidence here is not merely class-level: a 1986 multicentre double-blind crossover trial (PMID 3510686) directly compared piroxicam versus naproxen in 47 children with juvenile chronic arthritis (the predecessor disease category to JIA) and found comparable efficacy with good tolerability; a 1987 trial (PMID 2957205) similarly demonstrated significant reduction in painful and swollen joints. Piroxicam's long half-life (~32 hours in children, per PMID 1782984) enables once-daily dosing—a meaningful practical advantage in pediatric adherence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov search returned 0 results for piroxicam + juvenile idiopathic arthritis).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | Multicentre Controlled Trial | British Journal of Rheumatology | Piroxicam vs. naproxen in 47 children (age 5–16) with seronegative JCA; 8-week double-blind crossover; no significant efficacy difference, good tolerability in both arms |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Clinical Trial | European Journal of Rheumatology and Inflammation | Piroxicam vs. naproxen in 26 JRA patients (age 3–25); significant reduction in painful and swollen joints (p<0.05) |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic Review + Network Meta-analysis | World Journal of Clinical Cases | Network meta-analysis comparing multiple NSAIDs for JIA; evaluates comparative efficacy and optimal drug selection across the NSAID class |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic Review + Network Meta-analysis | Indian Pediatrics | Comparative efficacy and safety of 9 NSAIDs in JIA; piroxicam included; confirms class benefit with drug-level differentiation |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic Study | European Journal of Clinical Pharmacology | Steady-state PK of piroxicam in 10 children with RA (age 7–16, 20–63 kg); mean half-life 32.6 h; confirms once-daily dosing feasibility in pediatric population |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Long-term Safety Cohort | Clinical Rheumatology | 117 children followed mean 8.6 years in pediatric rheumatology clinic; 155 NSAID exposures documented; characterizes long-term NSAID toxicity profile in JIA |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort Study | International Ophthalmology | CI found in 56% of ANA-positive pauciarticular JCA patients; highlights importance of extra-articular monitoring alongside NSAID therapy |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderarztliche Praxis | Current pharmacologic therapy for juvenile chronic arthritis; piroxicam presented alongside sulfasalazine as newer therapeutic agent in this disease |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review (Drug Delivery) | Critical Reviews in Therapeutic Drug Carrier Systems | NSAID microencapsulation for arthritis types including JIA; discusses piroxicam delivery optimization for improved GI tolerability |
| [6753142](https://pubmed.ncbi.nlm.nih.gov/6753142/) | 1982 | Review | Schweizerische Medizinische Wochenschrift | NSAID prescribing guidelines with safety-first approach; piroxicam referenced among newer agents; covers special populations including pediatric and ulcer patients |

---

## Taiwan Market Information

Piroxicam is not currently marketed in Taiwan. No authorization records are on file with the TFDA. No product table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. Taiwan regulatory package insert data (warnings, contraindications) was not retrievable at the time of this report and constitutes a **Blocking data gap** (DG001) that must be resolved before proceeding to clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Piroxicam has direct head-to-head controlled trial evidence in pediatric patients with juvenile arthritis, demonstrating efficacy comparable to naproxen with acceptable tolerability; as NSAIDs are guideline-endorsed first-line therapy for JIA, the mechanistic and clinical basis for this repurposing direction is well-established across more than three decades of literature.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve Taiwan regulatory package insert (TFDA) to complete warnings and contraindications assessment—required before any S1 safety evaluation
- **[High]** Confirm formal MOA data via DrugBank API (DG002)—needed for complete mechanistic rationale documentation
- Review current pediatric dosing guidelines: most trial data originates from the 1980s–1990s; contemporary weight-based dosing protocols should be verified against current standards
- Drug interaction screening for common JIA co-medications (methotrexate, corticosteroids, biologics), particularly the known NSAID-MTX interaction risk
- Assess feasibility of Taiwan registration: piroxicam is not currently marketed in Taiwan; a regulatory pathway assessment is required before any clinical deployment
- Consider whether a dedicated prospective observational study or registry data collection could upgrade evidence from L2 to L1 (no Phase 3 RCT currently exists in the modern JIA diagnostic framework)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

