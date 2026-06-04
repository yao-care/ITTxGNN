---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using `txgnn-pipeline` to check context — the skill confirms this is a standard TxGNN report generation task with no additional overrides. Proceeding to generate the report from the Evidence Pack.

---

# Temozolomide: From Glioblastoma to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide (TMZ) is an oral alkylating agent established as the backbone of the **Stupp protocol** — the global standard of care for newly diagnosed glioblastoma — where it is combined with radiotherapy to significantly extend survival.
The TxGNN model predicts it may be effective for the broader category of **Adult Astrocytic Tumour**, with **2 clinical trials** and **20 publications** currently supporting this direction, including multiple landmark Phase 3 RCTs.
Notably, glioblastoma is itself the highest-grade adult astrocytic tumour, meaning this prediction is strongly anchored in established clinical practice.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glioblastoma / Malignant Astrocytoma (established by landmark Phase 3 RCT evidence; no Taiwan TFDA registration found) |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide belongs to the **imidazotetrazine** class of alkylating agents. After oral administration, it spontaneously hydrolyses to its active metabolite **MTIC**, which methylates DNA at the O⁶-guanine and N7-guanine positions. The O⁶-methylguanine adduct is recognised by the mismatch repair (MMR) system, ultimately triggering apoptosis. A critical pharmacological advantage is its **excellent blood-brain barrier penetration** (CSF-to-plasma ratio ≈ 0.4), making it uniquely suited for central nervous system tumours.

Efficacy is strongly modulated by **MGMT promoter methylation status**: when the MGMT gene is silenced by methylation, the tumour cell cannot repair TMZ-induced DNA damage, yielding substantially better outcomes. This biomarker-driven response has been demonstrated across multiple Phase 3 trials and is now a routine predictive test before initiating TMZ-based therapy.

Adult astrocytic tumours encompass a histological spectrum — from WHO Grade 2 diffuse astrocytoma through Grade 3 anaplastic astrocytoma to Grade 4 glioblastoma (GBM). GBM is precisely the indication for which the Stupp protocol (concurrent TMZ + radiotherapy, followed by adjuvant TMZ) was validated and globally adopted. The TxGNN model's prediction therefore reflects mechanistic and clinical continuity: TMZ's alkylating action on neuroepithelial tumour cells, combined with its CNS penetration, makes it rationally applicable across the full adult astrocytic spectrum.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised trial comparing TMZ alone vs PCV (procarbazine + lomustine + vincristine) in recurrent WHO Grade III–IV astrocytic tumours. Direct head-to-head RCT evidence for TMZ in this exact disease category. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib) added to TMZ + radiotherapy as first-line treatment for glioblastoma. TMZ serves as the standard backbone, confirming its established safety and feasibility in this setting. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | Phase 3 RCT | N Engl J Med | **Landmark Stupp trial**: RT + concomitant/adjuvant TMZ vs RT alone in newly diagnosed GBM. Established TMZ as the standard of care (median OS 14.6 vs 12.1 months; 2-year survival 26.5% vs 10.4%). |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | Phase 3 RCT follow-up | Lancet Oncol | 5-year analysis of the EORTC-NCIC Stupp trial. Confirmed sustained OS benefit of TMZ + RT; MGMT methylation identified as key predictive biomarker (5-year OS 13.8% vs 1.9% for MGMT-methylated vs unmethylated). |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | Phase 3 RCT | Lancet Oncol | **NOA-08 trial**: TMZ alone vs radiotherapy alone in elderly patients with malignant astrocytoma (anaplastic astrocytoma or GBM). TMZ non-inferior to RT; MGMT methylation predicted benefit from TMZ. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | Phase 3 RCT | N Engl J Med | RTOG 0825: addition of bevacizumab to standard TMZ + RT in newly diagnosed GBM. TMZ-RT is the control arm reference; bevacizumab did not improve OS. |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | Phase 3 RCT | JAMA | **EF-14 trial**: Tumour Treating Fields (TTFields) + TMZ vs TMZ alone for maintenance therapy in GBM. TTFields + TMZ improved median OS (20.9 vs 16.0 months) and PFS. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | Phase 3 RCT | Lancet | **CeTeG/NOA-09 trial**: Lomustine-TMZ combination vs standard TMZ in newly diagnosed GBM with MGMT methylation. Combination arm showed improved OS (48.1 vs 31.4 months) in methylated patients. |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Phase 2/3 RCT subset | J Neuro-oncol | RT + TMZ in anaplastic astrocytoma (AA) and anaplastic oligo-astrocytoma (AOA). Exploratory cohort; supports TMZ + RT as active regimen across the broader astrocytic tumour spectrum. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | Phase 2/3 RCT | J Clin Oncol | **NRG BN007**: Dual checkpoint blockade (ipilimumab + nivolumab) added to standard TMZ chemoradiotherapy in MGMT-unmethylated GBM. TMZ backbone again used as standard comparator arm. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Systematic Review | JAMA | Comprehensive review of glioblastoma and other primary brain malignancies in adults. Confirms TMZ-based Stupp protocol as established standard; outlines unmet needs and emerging therapies. |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Early clinical review of TMZ in malignant gliomas (GBM and anaplastic astrocytoma). Documents early efficacy signals that led to Phase 3 trials and eventual approval. |

---

## Taiwan Market Information

Temozolomide currently has **no registered authorizations** in the Taiwan TFDA database based on the data retrieved for this report (query date: 2026-03-29, result count: 0). There are no licensed products, approved indications, or dosage forms on record.

> **Note:** This finding warrants independent verification against the current TFDA online drug licence database, as Temozolomide (Temodar®/Temodal®) holds regulatory approval in numerous major markets (USA, EU, Japan). The absence of TFDA records may reflect a data retrieval limitation or the drug being available under a different trade name or via special importation.

---

## Cytotoxicity

Temozolomide is classified as an antineoplastic agent (oral alkylating agent, imidazotetrazine class). The following table applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (Imidazotetrazine / Triazene class) |
| Myelosuppression Risk | **High** — Thrombocytopenia and neutropenia are the dose-limiting toxicities; typically nadir at days 21–28 of each 28-day cycle. Grade 3/4 thrombocytopenia occurs in ~14% of patients on the standard 5-day schedule. |
| Emetogenicity Classification | Moderate (standard antiemetic prophylaxis recommended prior to each dose) |
| Monitoring Items | CBC with differential and platelet count (on Day 22 and Day 29 of each cycle before next cycle); liver function tests (ALT, AST, bilirubin); renal function; MGMT promoter methylation status (baseline, for prognosis and treatment selection) |
| Handling Protection | Must be handled according to cytotoxic drug handling regulations — avoid crushing capsules, use appropriate PPE during preparation and disposal |

---

## Safety Considerations

Formal safety data (TFDA package insert warnings, contraindications, and drug interactions) were not retrievable from available sources at the time of this report.

> Please refer to the official package insert (Temodar®/Temodal® SmPC or FDA prescribing information) for complete safety information, including warnings regarding myelosuppression, opportunistic infections (e.g., *Pneumocystis jirovecii* pneumonia prophylaxis recommended during concurrent RT phase), hepatotoxicity, and use in pregnancy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Temozolomide in adult astrocytic tumours is among the strongest in neuro-oncology — the landmark Stupp Phase 3 RCT and its 5-year follow-up directly established TMZ + radiotherapy as the global standard of care for glioblastoma (WHO Grade 4 astrocytic tumour), and subsequent trials have extended evidence to anaplastic astrocytoma (Grade 3). The TxGNN prediction score of 99.36% is fully concordant with this established clinical evidence, with multiple completed Phase 3 RCTs qualifying this as Level L1 evidence.

**To proceed, the following is needed:**

- **Taiwan regulatory pathway clarification**: Verify whether Temozolomide is available in Taiwan under a trade name (Temodar®), via special importation, or under NHI reimbursement — TFDA query returned 0 results and needs manual confirmation.
- **Formal safety data**: Retrieve and document the complete package insert (warnings, contraindications, DDIs) — currently not available in the Evidence Pack due to the data gap flagged as DG001 (Blocking).
- **MGMT biomarker testing protocol**: Establish institutional workflow for MGMT promoter methylation testing to guide patient selection and expected response.
- **Opportunistic infection prophylaxis plan**: Confirm *P. jirovecii* prophylaxis protocol for patients receiving concurrent TMZ + radiotherapy.
- **Reimbursement review**: Assess NHI or institutional funding pathway for TMZ given its absence from TFDA records.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

