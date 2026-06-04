---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Teriflunomide: From Leflunomide Active Metabolite to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Teriflunomide is the pharmacologically active metabolite of leflunomide—an oral immunomodulatory agent originally developed from the rheumatoid arthritis drug family—functioning through selective inhibition of de novo pyrimidine synthesis to suppress autoreactive lymphocyte proliferation.
The TxGNN model predicts it may be highly effective for **relapsing-remitting multiple sclerosis (RRMS)**,
backed by **multiple completed Phase 3 pivotal trials** and **19 peer-reviewed publications**, including studies that have already formed the basis for FDA (2012) and EMA (2013) regulatory approvals—making this a TxGNN validation of an established global indication not yet registered in Taiwan.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally derived from leflunomide (rheumatoid arthritis) lineage |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis (RRMS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Teriflunomide is the active metabolite of leflunomide, selectively and reversibly inhibiting dihydroorotate dehydrogenase (DHODH)—the rate-limiting mitochondrial enzyme in the de novo pyrimidine synthesis pathway. The biological insight driving this mechanism is elegant: activated T cells and B cells uniquely depend on de novo pyrimidine synthesis (rather than the salvage pathway) to sustain rapid proliferation during an immune response. Resting lymphocytes, which rely on the salvage pathway, are largely spared. This selectivity means DHODH inhibition targets pathologically activated, autoreactive lymphocytes while preserving baseline immune surveillance—an ideal immunological profile for an autoimmune disease like RRMS.

In relapsing-remitting multiple sclerosis, self-reactive T and B cells orchestrate inflammatory attacks on the central nervous system, leading to demyelination, axonal damage, episodic relapses, and progressive disability accumulation. By blocking the proliferative expansion of these autoreactive lymphocytes in the periphery, teriflunomide directly interrupts the upstream immunological cascade before CNS invasion occurs. This mechanistic alignment—from autoimmune lymphocyte dysregulation to pyrimidine-dependent proliferative block—explains why the TxGNN model assigned a near-perfect prediction score of 99.24%.

Beyond the primary DHODH pathway, mechanistic Phase IV data (NCT03464448) have demonstrated that teriflunomide positively modulates regulatory B lymphocytes (Breg cells), providing an additional immunoregulatory dimension that may contribute to sustained long-term disease control. The convergence of DHODH inhibition, reduced T-cell and B-cell activation, and Breg upregulation creates a multi-layered immunomodulatory profile that is particularly well-suited to the chronic, relapsing nature of RRMS—a finding further reinforced by the 2024 Cochrane Network Meta-Analysis and teriflunomide's consistent role as the active comparator in recent high-efficacy DMT Phase 3 trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1,088 | Pivotal double-blind RCT in RRMS: both 7 mg and 14 mg doses significantly reduced annualized relapse rate (ARR) vs. placebo; also assessed disability progression (EDSS), MRI lesion burden, and patient-reported fatigue |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Head-to-head RCT vs. interferon β-1a (s.c.) over 108 weeks plus long-term extension: evaluated time to treatment failure, relapse frequency, fatigue, and patient treatment satisfaction |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term safety extension of EFC6049 pivotal trial: documented multi-year safety/tolerability profile and sustained efficacy on disability progression, relapse rate, and MRI endpoints |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension of the first-in-class Phase 2 RRMS study: provided foundational long-term safety and efficacy data that underpinned the Phase 3 programme design |
| [NCT02776072](https://clinicaltrials.gov/study/NCT02776072) | N/A (Observational) | Completed | 2,978 | Largest real-world comparative study in this dataset: assessed 12-month relapse rates for teriflunomide vs. dimethyl fumarate, glatiramer acetate, and fingolimod in RRMS clinical practice |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A (Observational) | Completed | 106 | Investigator-initiated real-world effectiveness study over ≥2 years at an MS clinic: complementary generalizability data outside RCT conditions |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A (Mechanistic) | Completed | 30 | Phase IV open-label mechanistic study: characterized teriflunomide's effect on B-cell activation markers, costimulatory molecules, cytokine secretion, and regulatory B lymphocytes (Breg) in RRMS patients |
| [NCT03768648](https://clinicaltrials.gov/study/NCT03768648) | N/A (Observational) | Completed | 75 | Evaluated everyday cognitive function using ecological assessments and non-conventional MRI markers in RRMS patients on teriflunomide; contributed quality-of-life and cognitive outcome data |
| [NCT05962177](https://clinicaltrials.gov/study/NCT05962177) | N/A (Prospective Cohort) | Recruiting | 400 | Ongoing prospective monocentric cohort (2023–2030) characterizing RRMS patients in current clinical routine, including teriflunomide as a first-line treatment arm alongside high-efficacy therapies |
| [NCT06843382](https://clinicaltrials.gov/study/NCT06843382) | N/A (Observational) | Not Yet Recruiting | 100 | ROOF-MS: multicenter prospective cohort comparing teriflunomide vs. dimethyl fumarate on physical and cognitive fatigability outcomes; expected to start November 2025 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-Analysis | Cochrane Database Syst Rev | Updated Cochrane NMA of all immunomodulators and immunosuppressants for RRMS; systematically quantifies the relative benefit of teriflunomide vs. placebo and active comparators across the full DMT landscape |
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT (Phase 3, ASCLEPIOS I/II) | N Engl J Med | Ofatumumab (anti-CD20) vs. teriflunomide in 1,882 RMS patients: ofatumumab superior on ARR and MRI endpoints; teriflunomide served as active comparator, confirming its established efficacy baseline in Phase 3 |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT (Phase 3) | N Engl J Med | Tolebrutinib (oral brain-penetrant BTK inhibitor) vs. teriflunomide in relapsing MS: evaluated CNS-penetrant modulation of microglia and B cells; teriflunomide as benchmark reference arm |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT (Phase 3, ULTIMATE I/II) | N Engl J Med | Ublituximab (glycoengineered anti-CD20) vs. teriflunomide: superior B-cell depletion and ARR reduction; further validates teriflunomide as the standard-of-care first-line comparator |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT (Phase 3, evolutionRMS 1 & 2) | Lancet Neurology | Evobrutinib (BTK inhibitor) vs. teriflunomide across two Phase 3 trials in relapsing MS: reinforces teriflunomide's unshakeable role as the reference arm for next-generation oral DMT development |
| [37691530](https://pubmed.ncbi.nlm.nih.gov/37691530/) | 2023 | RCT Extension (ALITHIOS) | Mult Scler | Four-year ofatumumab extension data vs. teriflunomide: sustained superiority of anti-CD20 therapy documented; also provides one of the longest available teriflunomide active-comparator safety datasets |
| [31898276](https://pubmed.ncbi.nlm.nih.gov/31898276/) | 2020 | Systematic Review | CNS Drugs | Systematic review comparing all five approved oral DMTs for RRMS (fingolimod, DMF, teriflunomide, cladribine, siponimod); summarizes head-to-head and indirect efficacy and safety comparisons |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | JAMA clinical review of MS diagnosis and treatment (estimated 900,000 US patients); positions teriflunomide as a standard first-line oral DMT within the modern treatment algorithm |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Dedicated teriflunomide monograph: mechanism (DHODH inhibition, lymphocyte selectivity), RCT efficacy summary, real-world effectiveness, and tolerability profile; key prescribing reference |
| [37382446](https://pubmed.ncbi.nlm.nih.gov/37382446/) | 2023 | Clinical Study (Pediatric) | Expert Rev Neurother | Teriflunomide as first-line DMT in children and adolescents with RRMS; summarizes the basis for EU pediatric approval and extends the evidence base beyond adult populations |

---

## Taiwan Market Information

Teriflunomide is currently **not registered or marketed in Taiwan**. The TFDA database contains no approved authorizations for this compound.

> For reference: Teriflunomide is approved as **Aubagio®** (Sanofi) in over 80 countries, including the United States (FDA, September 2012), European Union (EMA, August 2013), and Japan (PMDA). A pediatric RRMS indication was additionally approved in the EU in 2023.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The TFDA package insert (key warnings, contraindications) was not retrievable in the current evidence pack and is flagged as a blocking data gap (DG001). DDI database query returned no results. For immediate reference, the EMA Summary of Product Characteristics (SmPC) for Aubagio® should be consulted for hepatotoxicity monitoring requirements, teratogenicity risk, accelerated elimination procedures, and lymphocyte count thresholds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Teriflunomide carries one of the strongest evidence bases in the RRMS pharmacological landscape—multiple completed Phase 3 RCTs (including the 1,088-patient pivotal trial and a head-to-head comparison vs. IFN β-1a), a 2024 Cochrane Network Meta-Analysis, and consistent selection as the active comparator in no fewer than four recent Phase 3 trials for next-generation DMTs. The L1 evidence classification is unambiguous. The primary barrier to Taiwan deployment is not efficacy uncertainty but the absence of local regulatory data.

**To proceed, the following is needed:**
- **[Blocking – DG001]** Download and parse the TFDA package insert PDF to extract key warnings and contraindications, particularly hepatotoxicity monitoring (ALT/AST), teratogenicity (Category X equivalent), and lymphocyte count requirements
- **[High – DG002]** Query DrugBank API for full MOA data including known off-target effects and metabolic pathway details
- Retrieve DDI data from EMA SmPC or FDA label as interim substitute pending TFDA-specific DDI database results
- Establish a Taiwan-specific safety monitoring plan: liver function tests (baseline + monthly for 6 months), complete blood count, blood pressure, and a formal teratogenicity risk communication plan with accelerated elimination protocol documentation (cholestyramine/activated charcoal washout)
- Assess whether the pediatric RRMS data (EU approval 2023; PMID 37382446) is relevant for any Taiwan pediatric MS population
- Confirm Taiwan NHI formulary pathway and comparator landscape (interferon β, glatiramer acetate, fingolimod availability) to position teriflunomide within local treatment algorithms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

