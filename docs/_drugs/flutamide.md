---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Flutamide
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

Using the **txgnn-pipeline** skill as context, and the Drug Repurposing Evaluation Report Prompt (v5) in the system prompt, I'll now generate the report.

The Evidence Pack for FLUTAMIDE contains 10 predicted indications. Rank 1 (highest TxGNN score) has no clinical evidence (L5 / Hold), while **Rank 6 — "male reproductive organ cancer"** carries the strongest evidence (L2, 50 clinical trials, 20 publications, "Proceed with Guardrails"). I'll build the report around Rank 6 as the primary actionable finding.

---

# Flutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Flutamide is a non-steroidal antiandrogen established globally for prostate cancer hormone therapy, though it currently holds no Italian marketing authorization.
The TxGNN model predicts it may be effective for **Male Reproductive Organ Cancer** as a broad indication category,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Italian authorization on record; globally established for prostate cancer hormone therapy |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on well-established pharmacological knowledge, Flutamide is a non-steroidal antiandrogen that competitively and reversibly blocks the androgen receptor (AR), preventing testosterone and dihydrotestosterone (DHT) from binding and activating downstream gene programs that drive cellular proliferation and survival. Unlike steroidal antiandrogens, Flutamide has no intrinsic hormonal activity, giving it high receptor selectivity and a relatively clean off-target profile.

Male reproductive organ cancer — with prostate cancer as the dominant entity — is fundamentally dependent on AR signaling. DHT binding to nuclear AR activates transcription of pro-survival and growth genes, making AR blockade the central therapeutic strategy. Flutamide disrupts this pathway directly and has historically been used either as monotherapy or in combination with LHRH agonists (total androgen blockade, TAB) to achieve PSA suppression and tumor volume reduction. This precise mechanistic alignment with the disease's core driver explains the TxGNN model's 99.98% confidence score.

Beyond prostate cancer, the broader category of male reproductive organ cancers includes other androgen-sensitive tumors where AR expression has been reported. The extensive clinical trial activity surrounding Flutamide — including a Phase 4 head-to-head comparison against enzalutamide in castration-resistant prostate cancer, a dedicated pre-surgical window-of-opportunity trial, and multiple large Phase 3 studies incorporating flutamide-containing androgen deprivation regimens alongside radiotherapy — firmly establishes both the biological plausibility and the clinical foundation for this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00003734](https://clinicaltrials.gov/study/NCT00003734) | Phase 3 | Unknown | 276 | Randomized comparison of 4 vs. 8 months of neoadjuvant triptorelin + flutamide prior to radiotherapy for high-risk localized prostate cancer; directly evaluates optimal duration of flutamide-containing AR blockade before RT |
| [NCT00567580](https://clinicaltrials.gov/study/NCT00567580) | Phase 3 | Active, Not Recruiting | 1,792 | SPPORT trial: short-term androgen deprivation (including antiandrogens such as flutamide and bicalutamide) combined with pelvic lymph node or prostate bed radiotherapy for PSA-rising post-prostatectomy prostate cancer |
| [NCT00769548](https://clinicaltrials.gov/study/NCT00769548) | Phase 3 | Completed | 1,322 | Whole pelvic irradiation + total androgen suppression vs. boost irradiation only; compares neoadjuvant vs. adjuvant timing of androgen suppression in prostate cancer; results published |
| [NCT00003653](https://clinicaltrials.gov/study/NCT00003653) | Phase 3 | Completed | 1,386 | Intermittent vs. continuous androgen suppression (antiandrogen-inclusive regimens) for PSA progression after radiotherapy; long-term overall survival outcomes published |
| [NCT00936390](https://clinicaltrials.gov/study/NCT00936390) | Phase 3 | Completed | 1,538 | Dose-escalated radiotherapy with or without short-term androgen deprivation in intermediate-risk prostate cancer; evaluates additive clinical benefit of AR blockade with modern RT |
| [NCT02918968](https://clinicaltrials.gov/study/NCT02918968) | Phase 4 | Completed | 206 | Direct randomized comparison of enzalutamide vs. flutamide + ADT in CRPC patients who failed bicalutamide-based combined androgen blockade; provides head-to-head flutamide efficacy data in the modern treatment era |
| [NCT06601205](https://clinicaltrials.gov/study/NCT06601205) | Phase 2/3 | Completed | 125 | Pre-surgical window-of-opportunity trial directly comparing low-dose flutamide (125 mg/day × 6 weeks) vs. finasteride vs. placebo in prostate cancer; tissue biomarkers as surrogate endpoints |
| [NCT01786265](https://clinicaltrials.gov/study/NCT01786265) | Phase 2 | Active, Not Recruiting | 310 | Finite androgen ablation (flutamide-inclusive) with or without abiraterone acetate + prednisone for PSA-progressing prostate cancer after surgery or radiotherapy |
| [NCT02090114](https://clinicaltrials.gov/study/NCT02090114) | Phase 2 | Completed | 112 | Bipolar androgen therapy (BAT) followed by enzalutamide or abiraterone in metastatic CRPC; evaluates sequential AR-pathway manipulation strategies and resistance mechanisms relevant to antiandrogen sequencing |
| [NCT00288080](https://clinicaltrials.gov/study/NCT00288080) | Phase 3 | Completed | 612 | Androgen suppression (leuprolide/goserelin + flutamide/bicalutamide) + 3DCRT/IMRT vs. same + docetaxel/prednisone for localized high-risk prostate cancer; results published |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [21751904](https://pubmed.ncbi.nlm.nih.gov/21751904/) | 2011 | RCT | N Engl J Med | Short-term ADT before and during radiotherapy significantly improves disease-specific and overall survival in localized prostate adenocarcinoma; landmark RCT (RTOG 94-08) establishing the combined hormone-RT standard of care |
| [8252497](https://pubmed.ncbi.nlm.nih.gov/8252497/) | 1993 | Review/Mechanistic | Cancer | Demonstrates flutamide as a pure antiandrogen with no intrinsic activity; maximal prostate weight inhibition achieved with flutamide + LHRH agonist combination; foundational mechanistic justification for total androgen blockade |
| [3157927](https://pubmed.ncbi.nlm.nih.gov/3157927/) | 1985 | Clinical Trial | The Prostate | Long-acting LH-RH agonist microcapsules combined with flutamide in Dunning R-3327H prostate cancer model; establishes preclinical and early clinical basis for combined androgen blockade strategy |
| [8650871](https://pubmed.ncbi.nlm.nih.gov/8650871/) | 1996 | Clinical Study | Urology | TRUS-measured prostate volume reduction with flutamide and flutamide + castration in previously untreated prostate cancer; objective morphological response assessment demonstrating AR blockade efficacy |
| [24950779](https://pubmed.ncbi.nlm.nih.gov/24950779/) | 2014 | Clinical Study | Cancer Prev Res | Phase II study of preoperative flutamide (125 mg/day × 6 weeks) in women at high ovarian cancer risk; demonstrates anti-androgenic tissue biomarker activity and supports androgen's role across reproductive cancers |
| [3287388](https://pubmed.ncbi.nlm.nih.gov/3287388/) | 1988 | Clinical Study | Prog Clin Biol Res | 5-year clinical experience with flutamide + LHRH agonist combination therapy for Stage C and D prostate cancer; documents long-term efficacy, PSA response, and tolerability profile |
| [3071951](https://pubmed.ncbi.nlm.nih.gov/3071951/) | 1988 | Clinical Study | Am J Clin Oncol | Rationale and evidence for combining non-steroidal antiandrogens with LH-RH analogues in prostate cancer; describes total androgen blockade advantages over surgical or medical castration alone |
| [65117](https://pubmed.ncbi.nlm.nih.gov/65117/) | 1976 | Review | Adv Sex Horm Res | Foundational review on steroidal and non-steroidal antiandrogens including flutamide; mechanisms of androgen action blockade at receptor and biosynthesis levels; defines the drug class |
| [37919464](https://pubmed.ncbi.nlm.nih.gov/37919464/) | 2023 | Preclinical | Sci Rep | Ganoderma lucidum polysaccharide sensitizes prostate cancer cells to flutamide and docetaxel in vitro; MTT cytotoxicity assays demonstrate synergistic anti-proliferative effects; supports combination strategies |
| [30400755](https://pubmed.ncbi.nlm.nih.gov/30400755/) | 2018 | In vitro | Tumour Biol | miRNA-23b and miRNA-27b combined with flutamide increases apoptosis rate and decreases CCNG1 expression in castration-resistant prostate cancer (PC-3 cell line); mechanistic insight into overcoming AR-independent resistance |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormone therapy — Non-steroidal antiandrogen (not a conventional cytotoxic agent; androgen receptor antagonist class) |
| Myelosuppression Risk | Low — Flutamide does not suppress bone marrow; myelotoxicity is not a class effect of antiandrogens |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT, AST, bilirubin) — hepatotoxicity is the primary and serious safety concern; PSA and serum testosterone for treatment response monitoring |
| Handling Protection | Standard pharmaceutical handling procedures apply; cytotoxic chemotherapy handling regulations are not required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2–4 randomized controlled trials — including a direct Phase 4 head-to-head comparison of Flutamide vs. enzalutamide in CRPC (NCT02918968, N=206) and several large Phase 3 studies where Flutamide-based total androgen blockade is a standard treatment arm — demonstrate meaningful evidence of efficacy in male reproductive organ cancer. The AR-blockade mechanism is scientifically robust and directly maps to the target disease's oncogenic driver. The primary barrier to proceeding is the complete absence of Italian (AIFA) marketing authorization and the unavailability of formal safety documentation in the current Evidence Pack.

**To proceed, the following is needed:**
- **Italian regulatory pathway**: Determine whether an AIFA Marketing Authorization Application (MAA) or an EU mutual recognition/decentralized procedure is applicable, and identify the appropriate indication label scope
- **Full Italian package insert**: Obtain and formally review warnings, contraindications (particularly severe hepatic impairment), and drug-drug interactions — Flutamide carries a known risk of serious, sometimes fatal hepatotoxicity
- **Hepatotoxicity risk management plan**: Establish a liver function monitoring schedule (baseline LFTs, monthly for first 4 months, then periodically), patient exclusion criteria, and patient/prescriber education materials
- **Comparative positioning analysis**: Evaluate Flutamide's clinical place relative to newer-generation antiandrogens (enzalutamide, apalutamide, darolutamide) that are already AIFA-authorized, particularly for CRPC and non-metastatic CRPC settings
- **Mechanism of action documentation**: Retrieve complete DrugBank MOA data (DG002) to support the regulatory submission narrative
- **Target population definition**: Define the specific patient subgroup offering the clearest benefit-risk advantage (e.g., CRPC following bicalutamide failure, neoadjuvant setting, or cost-sensitive markets where newer agents are inaccessible)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

