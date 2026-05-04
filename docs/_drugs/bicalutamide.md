---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

Using `txgnn-pipeline` to confirm context — the skill confirms this is a standard TxGNN Evidence Pack → pharmacist report generation task. Proceeding directly with the report.

---

Based on the Evidence Pack, I'm writing the report focused on **Female Breast Carcinoma** (rank 9) as the primary predicted indication, because it holds the strongest clinical evidence (L2, Phase 2 trial active, 20 publications) and the only actionable "Proceed with Guardrails" recommendation. Rankings 1–8 and 10 all scored "Hold" with weak or no mechanistic linkage.

---

# Bicalutamide: From Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Bicalutamide is a non-steroidal androgen receptor (AR) antagonist with global regulatory approval for prostate cancer, currently not registered in Italy.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** — particularly the AR-positive triple-negative breast cancer (LAR-TNBC) subtype —
with **1 Phase 2 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate Cancer (globally approved; not currently registered in Italy) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L2 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bicalutamide is a non-steroidal androgen receptor (AR) antagonist: it competitively binds the AR ligand-binding domain, blocking androgens from activating AR-mediated gene transcription. This mechanism is the backbone of prostate cancer hormonal therapy, where AR signaling is the primary growth driver. Detailed MOA data from the Italian package insert was not retrievable in this data pull; the above description is based on well-established pharmacological literature.

The androgen receptor is expressed in approximately 70–90% of all breast cancers. Within triple-negative breast cancer (TNBC) — a subtype lacking estrogen receptor, progesterone receptor, and HER2 amplification — roughly 10–35% of cases belong to the **luminal androgen receptor (LAR)** subtype, where AR is the dominant oncogenic signal. In LAR-TNBC tumors, AR drives proliferation and invasion through β-catenin transcription activation, ERK phosphorylation cascades, and FOXC2-mediated suppression of ferroptosis. Multiple in vitro studies confirm that bicalutamide suppresses LAR-TNBC cell growth by directly interrupting these AR-dependent pathways.

The mechanistic parallel to prostate cancer is therefore direct and biologically coherent: the same AR blockade that controls castration-naïve prostate cancer applies to AR-driven breast cancer subtypes. The existence of an ongoing Phase 2 trial combining bicalutamide with dual immune checkpoint blockade (NCT03650894), alongside a documented complete clinical response case and publications as recent as 2026, confirms that this is an active and scientifically credible research direction — not a speculative extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, Not Recruiting | 30 | Evaluates the safety and efficacy of bicalutamide combined with nivolumab and ipilimumab in metastatic HER2-negative breast cancer; designed to integrate AR blockade with dual immune checkpoint inhibition as a chemotherapy-sparing strategy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | Comprehensive review of anti-androgen agents (bicalutamide, enzalutamide, enobosarm) for AR+ TNBC; covers combination approaches with chemotherapy and immunotherapy |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Science China. Life Sciences | AR + ERK co-inhibition triggers ferroptosis via FOXC2 in TNBC; bicalutamide + GDC-0994 show significant synergistic anti-tumor effect in vitro and in vivo |
| [33341447](https://pubmed.ncbi.nlm.nih.gov/33341447/) | 2021 | Translational | European Journal of Cancer | Serial [¹⁸F]-FDHT-PET demonstrates AR occupancy kinetics during bicalutamide treatment in AR+ metastatic breast cancer; proposes AR imaging as a predictive biomarker for response |
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase II | The Oncologist | Bicalutamide + aromatase inhibitor in ER+/AR+ AI-resistant advanced breast cancer; Phase II single-arm study terminated early due to limited efficacy (CBR 16.7% at 6 months, ORR 0%) — highlights patient selection importance |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | In vitro | Medicine | Bicalutamide inhibits proliferation and invasion of MDA-MB-231 TNBC cells; mechanistically linked to AR signaling pathway suppression |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | In vitro | Anti-Cancer Drugs | Bicalutamide + curcumin combination shows strong therapeutic effect on AR+ TNBC cells; synergism via dual pathway disruption |
| [29069648](https://pubmed.ncbi.nlm.nih.gov/29069648/) | 2017 | Mechanistic | Cellular Physiology and Biochemistry | Bicalutamide antagonizes AR and inhibits the AR–β-catenin transcription complex in ER-negative breast cancer; provides mechanistic rationale for ongoing Phase II trials |
| [24888812](https://pubmed.ncbi.nlm.nih.gov/24888812/) | 2016 | Case Report | Journal of Clinical Oncology | Complete response of metastatic AR-positive breast cancer to bicalutamide monotherapy — first published clinical proof-of-concept for single-agent activity |
| [21633166](https://pubmed.ncbi.nlm.nih.gov/21633166/) | 2011 | Translational | Journal of Clinical Investigation | Landmark paper identifying 6 TNBC molecular subtypes including LAR (luminal androgen receptor); establishes AR as a primary therapeutic target and rationale for anti-androgen therapy in TNBC |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treatment Reviews | Detailed characterization of the LAR-TNBC subtype: genomic features (PIK3CA enrichment), AR expression prevalence (~10–35% of TNBC), and clinical rationale for AR-targeted therapy |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen Receptor Antagonist (Non-steroidal antiandrogen; hormonal/endocrine therapy) |
| Myelosuppression Risk | Low (bicalutamide lacks direct cytotoxic activity on hematopoietic progenitor cells; myelosuppression is not a recognized class effect) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT, AST, total bilirubin — drug-induced liver injury is a known risk), CBC at baseline, renal function |
| Handling Protection | Standard pharmaceutical handling procedures; special cytotoxic containment measures (closed-system transfer devices, etc.) are generally not required for this drug class |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Full safety data (AIFA-approved warnings, contraindications, and drug interactions) were not available in this Evidence Pack. Retrieval of the official Italian SmPC is required before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bicalutamide possesses a direct, biologically coherent mechanism (AR blockade) for treating AR-positive breast cancer, validated by an active Phase 2 trial, multiple in vitro studies, a documented complete clinical response case, and publications as recent as 2026. Evidence is sufficient to advance this hypothesis — but it must be applied strictly to biomarker-selected patients (AR+ tumors, particularly LAR-TNBC) to avoid the efficacy failure seen in unselected populations.

**To proceed, the following is needed:**
- **Safety review**: Retrieve and analyze the full AIFA SmPC (or EMA product information) to document hepatotoxicity warnings, contraindications, and drug interactions before any clinical application
- **Biomarker prerequisite**: Establish AR expression testing (IHC ≥10% threshold or molecular LAR subtype confirmation) as a mandatory patient selection criterion — bicalutamide is not expected to benefit AR-negative tumors
- **Await Phase 2 results**: Monitor NCT03650894 (completion expected December 2026) for safety and efficacy readout before expanding to combination immunotherapy protocols
- **Regulatory pathway analysis**: Conduct AIFA authorization feasibility assessment for Italy, including off-label use framework or formal repurposing application, given zero current registrations in the country
- **Combination strategy planning**: For the emerging AR + ERK co-targeting approach (bicalutamide + ERK inhibitor; 2026 FOXC2/ferroptosis data), a dedicated preclinical package should be completed before initiating Phase 1 dose-escalation in humans
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

