---
layout: default
title: Clomifene
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Clomifene
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

# Clomifene: From Ovulation Induction to Anovulation

## One-Sentence Summary

Clomifene (clomiphene citrate) is a selective estrogen receptor modulator (SERM) with over 60 years of global clinical use as a first-line ovulation induction agent for anovulatory infertility, though it is not currently registered in Italy.
The TxGNN model generated 10 predicted indications; **anovulation** (rank #10, score 99.52%) is the sole prediction with robust clinical support, backed by **50 clinical trials** and **20 publications** — the only L1-level finding in the entire prediction set.
The top-ranked predictions (ranks 1–9) were assessed as Hold or Research Question due to absent mechanistic links or lack of any clinical evidence, making anovulation the single actionable candidate from this TxGNN run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Italy; globally established for ovulation induction in anovulatory infertility (incl. PCOS) |
| Predicted New Indication | Anovulation (WHO Group II) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| Italy Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism of action data for Clomifene was not retrieved in this evidence pack. Based on the well-established clinical literature, Clomifene is a SERM of the triphenylethylene class. It competitively occupies estrogen receptors (ERα/ERβ) in the hypothalamic arcuate nucleus, blocking the normal estrogen negative-feedback signal. This disruption increases Kisspeptin/GnRH pulse frequency and amplitude, driving a synchronized rise in pituitary FSH and LH. The resulting gonadotropin surge stimulates follicle recruitment, dominant follicle maturation, and ultimately ovulation.

This mechanism directly addresses the root pathophysiology of WHO Group II anovulatory disorders — including polycystic ovary syndrome (PCOS) — where the hypothalamic-pituitary-ovarian (HPO) axis is functionally dysregulated but the ovarian machinery itself remains capable of responding. For these patients, removing the hypothalamic estrogen-feedback block is sufficient to restore the endogenous hormonal cascade needed for ovulation. This is why Clomifene has remained the backbone of first-line ovulation induction therapy for more than six decades, with multiple Phase 3/4 RCTs and several Cochrane systematic reviews confirming its efficacy.

> **TxGNN Prediction Context — Ranks 1–9:** The nine higher-ranked predictions include chromosomal copy-number disorders (partial trisomy/tetrasomy of chr5, chr12, chr18), anatomical structural defects (transverse and longitudinal vaginal septa), and rare genetic syndromes (46,XY testicular steroidogenesis defect, fragile X female carrier, BPES and its 3q23 variant). Each was assessed as **Hold** or **Research Question**: chromosomal dosage anomalies are inaccessible to any SERM mechanism; structural anatomical defects require surgical correction; and while BPES/fragile X–associated POI share a theoretical estrogen-axis intersection, no clinical evidence exists. Near-identical TxGNN scores across multiple chromosomal entries (0.99537–0.99538) strongly suggest knowledge-graph clustering artefacts in the reproductive-system node neighbourhood rather than genuine biological signal. Anovulation remains the only prediction supported by direct mechanistic and clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00478504](https://clinicaltrials.gov/study/NCT00478504) | Phase 4 | Completed | 159 | Double-blind crossover RCT: letrozole vs Clomifene for ovulation induction in PCOS; assessed pregnancy rate, multiple pregnancy rate, and live birth rate — primary Phase 4 head-to-head comparison |
| [NCT00610077](https://clinicaltrials.gov/study/NCT00610077) | Phase 3 | Completed | 55 | Open randomized multicenter trial: letrozole vs Clomifene in anovulatory infertility; cycle-by-cycle follicular response and pregnancy outcomes compared across 59 vs 68 cycles |
| [NCT00296465](https://clinicaltrials.gov/study/NCT00296465) | Phase 2/3 | Completed | 132 | Multicenter double-blind placebo-controlled RCT: pulsatile GnRH (IV/SC) vs Clomifene in anovulatory/oligoovulatory infertility; directly evaluated Clomifene ovulation induction efficacy and safety |
| [NCT00213148](https://clinicaltrials.gov/study/NCT00213148) | Phase 2 | Completed | 271 | Multicenter double-blind dose-finding study: anastrozole vs Clomifene in ovulatory dysfunction; large sample providing dose-response data for follicular growth and ovulation induction |
| [NCT00795808](https://clinicaltrials.gov/study/NCT00795808) | Phase 4 | Completed | 171 | Multicenter RCT: Metformin + Clomifene vs Clomifene alone vs Metformin alone in anovulatory PCOS; stratified by BMI (≤32 vs >32) to evaluate additive insulin-sensitising benefit |
| [NCT01573858](https://clinicaltrials.gov/study/NCT01573858) | N/A | Completed | 1,000 | PCOSAct trial — four-arm large RCT: two acupuncture protocols combined with Clomifene vs placebo in anovulatory PCOS women; primary endpoint live birth rate; large-scale real-world evidence |
| [NCT01896492](https://clinicaltrials.gov/study/NCT01896492) | Phase 4 | Completed | 200 | Double-blind RCT: Clomifene + N-acetyl cysteine (antioxidant adjuvant) vs Clomifene alone in newly diagnosed PCOS; assessed impact on ovulation and pregnancy rates |
| [NCT00558077](https://clinicaltrials.gov/study/NCT00558077) | Phase 4 | Completed | 50 | RCT: laparoscopic ovarian diathermy vs Metformin + Clomifene as second-line treatment after Clomifene monotherapy failure in anovulatory PCOS |
| [NCT02381184](https://clinicaltrials.gov/study/NCT02381184) | Phase 2/3 | Completed | 160 | RCT: extended Clomifene regimen (10-day) vs laparoscopic ovarian drilling in Clomifene-resistant PCOS; ovulation rate, endometrial thickness, and pregnancy rate as co-primary outcomes |
| [NCT06486870](https://clinicaltrials.gov/study/NCT06486870) | Phase 3 | Completed | 183 | Three-arm RCT comparing two ovulation induction therapies vs laparoscopic ovarian drilling in Clomifene-resistant PCOS women; completed January 2024 — most recent Phase 3 evidence in this indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [36165742](https://pubmed.ncbi.nlm.nih.gov/36165742/) | 2022 | Cochrane SR / Meta-analysis | Cochrane Database Syst Rev | Letrozole vs Clomifene for ovulation induction in PCOS: letrozole yields higher live birth and ovulation rates; Clomifene confirmed as the historical first-line standard against which all alternatives are benchmarked |
| [29273245](https://pubmed.ncbi.nlm.nih.gov/29273245/) | 2018 | 2×2 Factorial RCT | Lancet | M-OVIN trial: gonadotrophins vs Clomifene ± IUI in normogonadotropic anovulation with Clomifene failure; defines when to escalate from Clomifene to second-line therapy |
| [29183107](https://pubmed.ncbi.nlm.nih.gov/29183107/) | 2017 | Cochrane SR | Cochrane Database Syst Rev | Insulin-sensitising drugs (metformin, TZDs) vs Clomifene for PCOS subfertility; supports Clomifene's central role in standard treatment algorithms for anovulatory PCOS |
| [28143834](https://pubmed.ncbi.nlm.nih.gov/28143834/) | 2017 | Network Meta-analysis | BMJ | Systematic review + network meta-analysis comparing all first-line treatments for WHO Group II anovulation; provides ranked comparative effectiveness including Clomifene |
| [15674894](https://pubmed.ncbi.nlm.nih.gov/15674894/) | 2005 | Cochrane SR | Cochrane Database Syst Rev | Oral anti-oestrogens and adjuncts for anovulation-related subfertility; foundational review establishing Clomifene's first-line status and evaluating tamoxifen, dexamethasone, bromocriptine, and aromatase inhibitors for resistance |
| [36622200](https://pubmed.ncbi.nlm.nih.gov/36622200/) | 2023 | Follow-up RCT Analysis | Hum Reprod | Long-term outcomes after switching to gonadotrophins vs continuing Clomifene ± IUI in normogonadotropic anovulation; critical evidence for treatment-sequencing decisions post-Clomifene failure |
| [41863134](https://pubmed.ncbi.nlm.nih.gov/41863134/) | 2026 | Review | Gynecol Endocrinol | Most recent comprehensive review of Clomiphene citrate in anovulation: MOA, epidemiology, clinical efficacy, predictors of treatment outcome, and current limitations |
| [25681838](https://pubmed.ncbi.nlm.nih.gov/25681838/) | 2015 | Clinical Review | Obstet Gynecol Clin North Am | Ovulation induction review: pharmacology, indications, dosing regimens, efficacy, adjuvant therapies, and monitoring — standard clinical reference for Clomifene use |
| [21406133](https://pubmed.ncbi.nlm.nih.gov/21406133/) | 2010 | Clinical Review | BMJ Clin Evid | Evidence-based review of female infertility treatments, including Clomifene for ovulatory failure; contextualises Clomifene within the broader infertility management pathway |
| [2282740](https://pubmed.ncbi.nlm.nih.gov/2282740/) | 1990 | Pharmacological Review | Baillières Clin Obstet Gynaecol | Seminal pharmacological review of Clomiphene citrate: mechanism, clinical use, dosing principles, and side-effect profile — the foundational reference establishing its role in anovulation treatment |

---

## Italy Market Information

Clomifene is currently **not registered with AIFA** in Italy. No marketing authorizations are on record (0 licenses). Any clinical use in Italy at this time would require either a formal marketing authorization application or access through a compassionate use / off-label prescribing pathway under applicable Italian regulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Based on the established clinical literature, the following safety aspects are recognized for Clomifene in ovulation induction:
> - **Multiple pregnancy**: Twin rate approximately 5–10%; higher-order multiples are possible, particularly at higher doses
> - **Ovarian hyperstimulation syndrome (OHSS)**: Lower risk than FSH-based gonadotropin protocols, but ultrasound monitoring during stimulation cycles is recommended
> - **Anti-estrogenic peripheral effects**: May reduce endometrial thickness and cervical mucus quality, potentially lowering implantation rates despite successful ovulation — a recognized gap between ovulation rate (~80%) and pregnancy rate (~40%) per cycle

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clomifene has the highest possible evidence level (L1) for anovulation, supported by multiple completed Phase 3/4 RCTs, Cochrane systematic reviews, and six decades of clinical practice globally. The TxGNN model assigns a 99.52% prediction score, and the drug's SERM mechanism directly and specifically addresses the HPO-axis dysregulation underlying WHO Group II anovulatory infertility. The primary barrier to use in Italy is the current absence of AIFA registration rather than any gap in clinical efficacy evidence.

**To proceed, the following is needed:**
- Obtain formal package insert for Clomifene (contraindications, warnings, full safety profile) to complete the S1 safety screen currently blocked by the data gap
- Retrieve complete DrugBank MOA documentation (currently flagged as data gap DG002)
- Evaluate the AIFA regulatory pathway: marketing authorization application vs. off-label/compassionate use framework
- Develop a clinical safety monitoring protocol covering: ultrasound surveillance per stimulation cycle, multiple pregnancy counseling, OHSS risk stratification, and a maximum treatment duration policy (standard practice: ≤6 consecutive cycles)
- Review current first-line positioning of Clomifene relative to letrozole in the Italian clinical context, given that recent Cochrane evidence (2022) and the PCOS international guidelines increasingly favour letrozole as preferred first-line for PCOS-related anovulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

