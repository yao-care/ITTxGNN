---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

---

# Bimatoprost: From Glaucoma to Alopecia

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analogue originally approved for open-angle glaucoma and ocular hypertension (Lumigan), with a subsequent FDA approval for eyelash hypotrichosis (Latisse), based on the serendipitous observation of eyelash growth in glaucoma patients.
The TxGNN model predicts it may be effective for **Alopecia** — including androgenetic alopecia (AGA) and alopecia areata (AA) — extending the established eyelash mechanism to the scalp.
This direction is currently supported by **11 registered clinical trials** (including three large completed Phase 2 RCTs) and **20 publications**, yielding one of the strongest evidence profiles in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma; ocular hypertension; eyelash hypotrichosis |
| Predicted New Indication | Alopecia (androgenetic alopecia and alopecia areata) |
| TxGNN Prediction Score | 99.993% (Rank #8 overall) |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Editorial note:** The highest TxGNN-scored indication (Rank #1, 99.997%) is *"malformation syndrome with odontal and/or periodontal component."* No clinical trial or direct literature evidence links bimatoprost to this condition — the 20 retrieved publications are general periodontology references. That prediction is assessed as L5 / Hold and is not the focus of this report. **Alopecia (Rank #8)** is presented as the primary target because it holds the strongest clinical evidence and the only actionable recommendation in this Evidence Pack.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded in this Evidence Pack. Based on the available literature, bimatoprost activates the FP (prostaglandin F) receptor on hair follicles, upregulating the Wnt/β-catenin signalling pathway. This extends the anagen (active growth) phase of the hair cycle, increases follicular density, and enlarges hair shaft diameter. The mechanism has already been clinically validated at the eyelid margin — the basis for the FDA-approved Latisse indication — establishing that bimatoprost genuinely interacts with follicular biology and not merely as an off-target effect.

The step from eyelash hypotrichosis to scalp alopecia is therefore a mechanistic extension, not a speculative leap. FP receptors are present in all hair follicles, and the hair cycle regulation machinery is conserved across the scalp and eyelid. In androgenetic alopecia, androgens progressively miniaturise scalp follicles by shortening the anagen phase; bimatoprost's ability to counteract exactly this shortening provides clear biological rationale. In alopecia areata, bimatoprost may rescue anagen entry in follicles suppressed by immune attack, even if it does not address the underlying autoimmune mechanism directly.

Importantly, the FP receptor approach is orthogonal to the two established AGA treatments (minoxidil and finasteride), offering a potential combination partner or alternative for patients who do not respond to or tolerate standard therapy. The Phase 2 programme directly compared bimatoprost to minoxidil in head-to-head arms, confirming the mechanism is being rigorously tested against the current standard of care.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Safety and efficacy of 3 bimatoprost doses vs. vehicle and OTC minoxidil 5% in men with AGA; double-blind RCT — largest male scalp trial |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Parallel female-pattern hair loss (FPHL) trial: 3 bimatoprost doses vs. vehicle and minoxidil 2%; double-blind RCT — largest female scalp trial |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Independent replication study of bimatoprost in male AGA; adds confidence to the male AGA evidence base |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Mechanistic validation: bimatoprost solution applied to androgen-dependent scalp follicles; demonstrates FP receptor activity in scalp tissue |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | CO₂ fractional laser combined with bimatoprost 0.03% for alopecia areata; novel combination strategy extending bimatoprost to AA subtype |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Bimatoprost 0.03% once daily for eyelash loss/hypotrichosis in children; provides paediatric safety data relevant to the broader programme |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability, and PK of two new bimatoprost formulations for alopecia; supports topical formulation development pathway |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Local PK and tolerability of bimatoprost applied daily to male AGA scalp for 14 days; confirms scalp absorption characteristics |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose escalation safety/PK study in male AGA; **terminated early** — termination reason must be reviewed before proceeding |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Latanoprost vs. bimatoprost ophthalmic solutions for eyelash growth in alopecia areata patients; early proof-of-concept in AA eyelash subtype |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Systematic Review + Network Meta-Analysis | J Dermatol Treatment | Compared relative efficacies of non-surgical AGA monotherapies in men and women; bimatoprost included in the network; highest-grade evidence for AGA pharmacotherapy |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Clinical Practice Guideline | J Dermatology | Japanese evidence-based guidelines for male- and female-pattern hair loss; bimatoprost reviewed as an emerging therapy with supporting trial data |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | Clinical Study | Arch Dermatol Res | Prospective study of CO₂ fractional laser + bimatoprost in alopecia areata; reports superior hair regrowth vs. laser alone, supports combination strategy |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective Study | Dermatol Therapy | Open-label prospective study of topical bimatoprost for eyelash loss in alopecia totalis and universalis; 16 of enrolled patients showed clinically meaningful response |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Non-randomised Clinical Trial | Indian Dermatol Online J | Head-to-head comparison of bimatoprost vs. clobetasol propionate in scalp alopecia areata; bimatoprost evaluated as a novel non-corticosteroid option for AA |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | Comprehensive review of bimatoprost for eyelash, eyebrow, and scalp alopecia; synthesises mechanism, clinical trial results, and safety profile |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatol Online J | Review of bimatoprost dermatology applications; traces the discovery path from glaucoma side-effects to alopecia treatment development |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | Mechanistic / Early Clinical Report | FASEB J | Foundational FASEB study: first formal demonstration that prostamide-related glaucoma therapy may address scalp alopecias; proposes and tests the FP receptor hypothesis in scalp tissue |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Formulation / Preclinical | Drug Delivery | Optimised topical bimatoprost formulation achieving 4.6× higher skin flux and 529% more dermal drug deposition; demonstrated improved AGA hair regrowth in vivo |
| [38577618](https://pubmed.ncbi.nlm.nih.gov/38577618/) | 2024 | Formulation Research | Int J Pharm X | Spanlastic nanogel delivery system for bimatoprost; superior cutaneous deposition and hair regrowth efficacy in androgenic alopecia model |

---

## Taiwan Market Information

Bimatoprost currently holds **no approved authorizations in Taiwan**. No dosage forms, product names, or approved indications are registered with Taiwan's regulatory authority.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, key warnings, or contraindication data were retrievable for this Evidence Pack.

> **Action required:** The TFDA package insert was queried but warning/contraindication fields were not populated in this Evidence Pack. A manual review of the official Taiwan package insert (or the FDA/EMA Lumigan and Latisse labelling) is recommended before any clinical use evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The FP receptor → Wnt/β-catenin → anagen extension mechanism is already clinically validated at the eyelid margin (FDA-approved Latisse), providing a strong biological anchor for the scalp extension. Three large completed Phase 2 RCTs (aggregate n > 850), a systematic review with network meta-analysis, and an active clinical study in alopecia areata collectively meet the L2 evidence threshold. While no Phase 3 data yet exist for scalp AGA, the overall body of evidence is sufficient to justify a structured development or licensing evaluation — under appropriate monitoring conditions.

**To proceed, the following is needed:**

- **Phase 3 trial initiation or identification:** No completed Phase 3 data exist for scalp AGA. This is the primary gap separating L2 from L1. A Phase 3 programme or access to a completed but unpublished dataset must be confirmed.
- **Termination reason for NCT02676310:** This Phase 1 dose-escalation trial was terminated early (n=53). The termination reason must be reviewed to rule out a safety signal that would affect the risk profile.
- **Full safety and contraindication data:** TFDA/FDA/EMA package insert review for key warnings, contraindications, and drug interactions — currently all flagged as data gaps.
- **Mechanism of action (MOA) data from DrugBank:** Formal MOA documentation needed to complete the mechanistic justification section and regulatory dossier.
- **Taiwan regulatory pathway assessment:** With 0 current authorizations, a full market entry strategy (NDA filing, reference country recognition, or other pathway) must be planned before any clinical development in Taiwan begins.
- **Formulation strategy decision:** Multiple topical formulations have been investigated (at least three in NCT01189279 alone); selecting the optimal formulation with sufficient scalp penetration is prerequisite for any Phase 3 design.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

