---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

The txgnn-pipeline skill is for pipeline management, not report generation. The system prompt already contains the complete report specification. Proceeding to generate the pharmacist evaluation report based on the Evidence Pack JSON.

---

# Sirolimus: From Organ Transplant Rejection to Liposarcoma

## One-Sentence Summary

Sirolimus (rapamycin) is an mTOR inhibitor globally established for prevention of organ rejection in renal transplant recipients, with no current Italy market authorization.
The TxGNN model predicts it may be effective for **Liposarcoma**, with a prediction score of **99.89%**.
This direction is currently supported by **5 clinical trials** and **12 publications**, including one completed Phase 2 trial directly using sirolimus in myxoid liposarcoma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention (no Italy regulatory data available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sirolimus (rapamycin) is a macrolide compound and the prototype mTOR inhibitor. It functions by binding intracellularly to FKBP12; the resulting complex then binds to and allosterically inhibits mTORC1, blocking downstream effectors S6K1 and 4EBP1. This arrests the cell cycle at G1 phase, suppresses cap-dependent protein translation, and inhibits tumor cell proliferation and angiogenesis. While detailed MOA documentation was not available in the regulatory database queried, sirolimus's mechanism as a direct mTOR inhibitor is extensively characterized in the scientific literature, and all mechanistic rationale below is drawn from published evidence.

Dedifferentiated liposarcoma (DDLPS) is characterized by high-frequency activation of the Akt-mTOR and MAPK signaling pathways, confirmed by immunohistochemical analysis across 99 DDLPS specimens (PMID 26518767). This aberrant pathway activation directly implicates mTORC1 as a therapeutic target. In patient-derived orthotopic xenograft (PDOX) animal models, rapamycin in combination with the autophagy inhibitor chloroquine demonstrated synergistic tumor growth arrest in both well-differentiated and dedifferentiated liposarcoma (PMID 37400145, PMID 36309387), mechanistically linking mTOR inhibition to tumor control in this specific histology.

Most importantly, the completed Phase 2 trial NCT02821507 directly evaluated the combination of sirolimus and cyclophosphamide in 70 patients with metastatic or unresectable myxoid liposarcoma and chondrosarcoma—the most direct available clinical evidence. Four additional trials tested mTOR inhibitor analogs (temsirolimus, ridaforolimus, everolimus) across broader sarcoma populations, consistently demonstrating class-level antiproliferative activity. The convergence of molecular, preclinical, and clinical evidence makes the TxGNN prediction mechanistically sound.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|------------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | **Direct sirolimus trial:** Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; mTOR inhibition shown to prevent tumor growth in in vivo mouse models; highest-grade direct evidence |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor) administered 5 days/2-week cycle in advanced sarcoma; largest Phase 2 cohort validating mTOR class efficacy across sarcoma subtypes |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab (anti-IGF-1R) + temsirolimus in pediatric recurrent/refractory sarcoma; dual-pathway mTOR + IGF-1R targeting; provides safety and preliminary efficacy reference |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus + liposomal doxorubicin in recurrent sarcoma; established safe dosing and early efficacy signals for mTOR inhibitor combination strategies |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma (DDL) and leiomyosarcoma (LMS); CDK4/6 + mTOR co-inhibition; DDL subtype precisely matches liposarcoma target population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 Trial Report | Clinical Cancer Research | SAR-096: Ribociclib + everolimus in advanced DDLPS and LMS; reports anti-tumor activity of mTOR + CDK4/6 dual inhibition in the exact liposarcoma subtype of interest |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical/Translational | Cancer Genomics & Proteomics | Rapamycin + chloroquine synergistically inhibits autophagy and induces apoptosis in well-differentiated liposarcoma; preclinical validation of sirolimus + autophagy inhibitor strategy |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | PDOX Animal Model | In Vivo | Rapamycin + chloroquine arrests tumor growth in a DDLPS patient-derived orthotopic xenograft (PDOX) model; demonstrates translational relevance of mTOR inhibition in DDLPS |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/Molecular | Tumour Biology | Akt-mTOR and MAPK pathway activation confirmed in 99 DDLPS specimens by immunohistochemistry; in vitro antitumor effect of mTOR inhibitor demonstrated; core mechanistic evidence |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Molecular Cancer Therapeutics | MLN0128 (ATP-competitive mTOR kinase inhibitor blocking both mTORC1/2) shows potent in vitro and in vivo antitumor activity in bone and soft-tissue sarcoma models; highlights limitations of first-generation rapalogs |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Comprehensive overview of novel therapeutics in soft tissue sarcoma, including FDA-approved TKIs and emerging mTOR inhibitor combination strategies |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Current Opinion in Oncology | Rationale and results of recent clinical trials with molecular-targeted agents for advanced sarcomas; contextualizes mTOR inhibition within the sarcoma treatment landscape |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Clinical Cohort | JASN | Sirolimus after cyclosporine withdrawal in renal transplant patients significantly reduces cancer incidence; demonstrates sirolimus's intrinsic antiproliferative/anti-cancer properties in a clinical population |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Clinical Review | Transplantation Proceedings | Immunosuppressive drug effects on malignancy in long-term transplant patients; sirolimus's differential cancer-protective profile vs. calcineurin inhibitors |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Molecular classification of rare connective tissue tumors and sarcomas with specific alterations; provides biological framework for mTOR inhibitor targeting in sarcoma subgroups |

---

## Italy Market Information

Sirolimus currently has **no marketing authorizations in Italy**. There are no approved products, dosage forms, or licensed indications on record with AIFA.

Any use in Italy would require either a compassionate use application (*uso compassionevole*) under AIFA regulations or enrollment in an authorized clinical trial.

---

## Cytotoxicity

Sirolimus belongs to the rapalog class of targeted antineoplastic agents. Although not a conventional cytotoxic drug, its analogs (temsirolimus, everolimus) are FDA- and EMA-approved antineoplastics, and sirolimus itself is used in oncological contexts (FDA-approved for LAM; nab-sirolimus approved for malignant PEComa). The following applies when used in a cancer treatment setting:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalog class); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate — anemia and thrombocytopenia reported; leucopenia less common; significantly less myelotoxic than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, serum creatinine and eGFR, liver function tests (AST/ALT/bilirubin), fasting lipid panel (triglycerides, total cholesterol), fasting glucose, sirolimus whole-blood trough levels |
| Handling Protection | Standard oncology handling precautions; cytotoxic drug handling protocols recommended in the cancer treatment setting |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The completed Phase 2 trial NCT02821507 directly testing sirolimus in myxoid liposarcoma (n=70), combined with a strong mechanistic basis (confirmed mTOR pathway activation in DDLPS), extensive mTOR inhibitor class-effect data across sarcoma subtypes, and a TxGNN score of 99.89% (L2 evidence), provides sufficient grounds to advance—but the absence of Italy regulatory authorization and the lack of published trial results from NCT02821507 require protective guardrails before any clinical deployment.

**To proceed, the following is needed:**
- Obtain and review published results from NCT02821507 (sirolimus + cyclophosphamide in myxoid liposarcoma) to confirm efficacy magnitude and safety profile
- Retrieve full mechanism of action data from DrugBank API (DG002 remediation) to formalize the MOA rationale section
- Assess AIFA pathway for sirolimus authorization in Italy — compassionate use (*uso compassionevole*, L. 648/96) or investigator-initiated trial (IIT) application
- Develop a patient selection protocol specifying liposarcoma histological subtype (myxoid vs. dedifferentiated vs. well-differentiated) and molecular profiling criteria (mTOR pathway activation status)
- Design a sirolimus therapeutic drug monitoring (TDM) plan with target trough blood levels and safety stopping rules
- Consult with a sarcoma specialist and clinical pharmacologist before initiating any off-label use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

