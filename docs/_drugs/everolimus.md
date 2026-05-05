---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Everolimus
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

The txgnn-pipeline skill confirms this is a standard TxGNN output task. The system prompt's Report Prompt v5 provides the complete formatting specification. Proceeding to generate the report from the Evidence Pack.

---

# Everolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is a rapamycin analogue (rapalog) and mTOR inhibitor, globally established for renal cell carcinoma, hormone receptor-positive breast cancer, and neuroendocrine tumours, though no marketing authorisation was identified in the current regulatory dataset.
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **1 active Phase 2 clinical trial** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal cell carcinoma (globally established; no registration found in current dataset) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Everolimus is a well-characterised mTOR inhibitor, even though its formal DrugBank MOA record was not captured in this evidence pack. It acts by inhibiting mTORC1 (mechanistic target of rapamycin complex 1), suppressing downstream effectors S6K1 and 4EBP1, which are critical regulators of protein synthesis and G1→S cell cycle progression. This mechanism underpins its approved use in renal cell carcinoma and hormone receptor-positive breast cancer, where PI3K/Akt/mTOR pathway overactivation drives tumour growth.

Dedifferentiated liposarcoma (DDLS) — the primary subtype targeted in current clinical trials — is biologically relevant to this mechanism. A clinicopathological study of 99 DDLS specimens (PMID 26518767, 2016) provided immunohistochemical evidence of Akt/mTOR and MAPK pathway activation, together with in vitro demonstration of mTOR inhibitor antitumour effects. DDLS is further defined by CDK4 gene amplification, establishing a strong biological rationale for combining CDK4/6 inhibition with mTOR inhibition — a strategy already validated to produce synergistic growth inhibition across multiple tumour models.

The TxGNN prediction is directly reinforced by an ongoing Phase 2 trial (NCT03114527) evaluating Ribociclib (CDK4/6 inhibitor) plus Everolimus in advanced DDL and leiomyosarcoma, with published results already appearing in Clinical Cancer Research (PMID 37967116, 2024). Together, the mechanistic data, preclinical synergy evidence, and early-phase clinical data form a coherent and biologically plausible rationale for Everolimus in liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, Not Recruiting | 48 | Two-centre, two-arm study evaluating Ribociclib + Everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) in patients with ≥1 prior systemic therapy. Ribociclib 300 mg/day 3-weeks-on/1-week-off; Everolimus 2.5 mg daily. Completion expected December 2025. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 Results | Clinical Cancer Research | Published results of Ribociclib + Everolimus Phase 2 trial (NCT03114527) in advanced DDL and LMS; CDK4 and mTOR dual inhibition demonstrates synergistic antitumour activity across multiple tumour models |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational Study | Tumour Biology | Immunohistochemical analysis of 99 DDLS specimens demonstrating Akt/mTOR and MAPK pathway activation; in vitro data confirm antitumour effect of mTOR inhibitor, providing direct mechanistic rationale |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Comprehensive review of CDK inhibitors in sarcomas using patient-derived orthotopic xenograft (PDOX) models; identifies CDK4/6 + mTOR combination strategies as high-priority candidates for clinical translation |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Evaluation of eribulin in combination with mechanistically distinct anticancer agents across human tumour xenograft models including liposarcoma; supports exploration of multi-agent approaches |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Molecular Study | Oncogene | XPO1 inhibitor (Selinexor) disrupts core transcriptional regulatory circuitry of DDLPS by modulating translation; highlights translational regulation as a key oncogenic vulnerability and underscores ongoing unmet need for effective targeted therapies in DDLPS |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalog); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to Moderate — anaemia, thrombocytopenia, and lymphopenia have been reported, but severity is generally lower than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, fasting blood glucose, serum lipids (triglycerides and cholesterol), serum creatinine, liver function tests (ALT/AST), and pulmonary assessment (risk of non-infectious pneumonitis) |
| Handling Protection | Standard oral oncology handling precautions; consult institutional cytotoxic drug handling policy for oral targeted agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
An active Phase 2 trial (NCT03114527) with peer-reviewed published results directly evaluates Everolimus in dedifferentiated liposarcoma, backed by solid mechanistic data demonstrating mTOR pathway activation in this tumour type. However, the current evidence covers a combination regimen (Ribociclib + Everolimus) rather than Everolimus monotherapy, the trial is not yet formally completed, and the drug holds no marketing authorisation in this jurisdiction.

**To proceed, the following is needed:**
- Final results of NCT03114527 upon trial completion (expected December 2025)
- Clarification of treatment strategy: Everolimus monotherapy vs. combination with a CDK4/6 inhibitor for DDL
- Market authorisation evaluation or compassionate use pathway for Everolimus in this jurisdiction
- Formal DrugBank MOA data retrieval to complete mechanistic documentation
- Comprehensive safety monitoring plan covering pneumonitis, metabolic toxicities (hyperglycaemia, dyslipidaemia), myelosuppression, and relevant drug-drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

