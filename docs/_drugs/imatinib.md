---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Imatinib
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

The skill confirms this is a TxGNN pipeline task. I'll now generate the evaluation report following the v5 format, based on the Evidence Pack data for Imatinib (DB00619).

---

# Imatinib: From CML & GIST to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib (Gleevec/Glivec) is a tyrosine kinase inhibitor originally developed for Chronic Myeloid Leukaemia (CML) and Gastrointestinal Stromal Tumours (GIST), targeting the BCR-ABL, c-KIT, and PDGFR kinases.
The TxGNN model predicts it may be effective for **Heart Fibrosarcoma**,
with **0 clinical trials** and **1 publication** currently identified for this indication — representing a model-only prediction with minimal direct evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukaemia (CML) and Gastrointestinal Stromal Tumours (GIST) |
| Predicted New Indication | Heart Fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided dataset. Based on well-established published literature, imatinib is a small-molecule tyrosine kinase inhibitor that competitively blocks three key oncogenic kinases: BCR-ABL (the driving fusion protein in CML), c-KIT (constitutively mutated in GIST and other sarcomas), and PDGFR-α/β (overactivated in fibroblastic tumours such as dermatofibrosarcoma protuberans). Its landmark success in CML and GIST established the paradigm of molecularly targeted therapy, and its PDGFR-blocking activity has since been applied across multiple fibroblastic and mesenchymal tumour types.

Cardiac fibrosarcoma is an exceptionally rare primary malignancy of the heart, with fewer than 100 documented cases in the entire published literature. For imatinib to be mechanistically relevant here, tumour cells would need to harbour activating mutations or overexpression of BCR-ABL, c-KIT, or PDGFR — none of which has been reported in heart fibrosarcoma to date. The theoretical rationale remains plausible in principle, given imatinib's known activity against fibroblastic tumours driven by the PDGF pathway, but is entirely unsupported by direct clinical or preclinical data for this specific tumour site.

The TxGNN prediction score of 99.94% reflects graph-network similarity across the drug-disease knowledge graph, not clinical efficacy. Because cardiac fibrosarcoma is so rare that it generates almost no literature signal, the model prediction cannot be independently validated at this stage. This is a hypothesis-generating output, not an evidence-based recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Editorial / Commentary | Prescrire International | Narrative review of imatinib's expanding indications beyond CML, including Ph+ ALL and other haematological/solid tumours; discusses lack of robust evidence for many new uses. Does not address heart fibrosarcoma — retrieved due to broad imatinib indication review. |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Tyrosine Kinase Inhibitor — BCR-ABL / c-KIT / PDGFR-α/β inhibitor) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia are frequently reported; severity is generally lower than conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low to moderate (oral administration; nausea is common but usually manageable) |
| Monitoring Items | Complete blood count (CBC with differential), liver function tests (ALT, AST, bilirubin), renal function (serum creatinine), fluid retention / peripheral oedema assessment, body weight |
| Handling Protection | Standard cytotoxic drug handling precautions apply; no special biocontainment beyond routine oral TKI protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Heart fibrosarcoma is an extremely rare tumour with no documented BCR-ABL, c-KIT, or PDGFR alterations, and the single identified publication is a general editorial that does not address this indication. No clinical trials exist and the biological plausibility remains unverified. Proceeding would be premature without foundational molecular data.

**To proceed, the following is needed:**
- Molecular pathology of cardiac fibrosarcoma tissue: IHC or NGS profiling for PDGFR-α/β expression, c-KIT mutation, or other imatinib-sensitive kinase alterations
- Establishment of preclinical models (cell lines or patient-derived xenografts) specific to cardiac fibrosarcoma
- Mechanism of action data retrieval from DrugBank (data gap DG002) to formally document biological plausibility
- Taiwan package insert (TFDA) and safety data (data gap DG001) to enable full S1 safety evaluation before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

