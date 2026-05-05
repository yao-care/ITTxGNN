---
layout: default
title: Mepolizumab
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

以下是根據 Evidence Pack 產生的藥師評估報告：

---

# Mepolizumab: From Hypereosinophilic Syndrome to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody used internationally for eosinophilic conditions including severe eosinophilic asthma and hypereosinophilic syndrome (HES); it is not currently approved in Taiwan.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, with **0 clinical trials** and **1 case report** currently supporting this direction.
The mechanistic link is indirect and context-dependent, applicable only in the narrow setting of HES-complicated thrombocytopenia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypereosinophilic syndrome / Eosinophilic conditions (international approval; not approved in Taiwan) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, mepolizumab is an anti-IL-5 monoclonal antibody that blocks interleukin-5 (IL-5), the cytokine primarily responsible for eosinophil proliferation, activation, and survival. By depleting circulating eosinophils, mepolizumab prevents eosinophil-mediated end-organ damage, including tissue infiltration and the release of toxic granule proteins.

The proposed mechanistic bridge to immune-mediated thrombocytopenia runs through HES: activated eosinophils in HES release cytotoxic granule proteins — eosinophil cationic protein (ECP) and major basic protein (MBP) — which can physically damage platelet membranes, drive platelet consumption, and trigger secondary immune-mediated platelet destruction. In this highly specific scenario, reducing the eosinophil burden with mepolizumab may indirectly improve platelet counts.

Critically, this pathway is indirect and context-dependent. Mepolizumab does not directly address the core mechanisms of primary immune thrombocytopenic purpura (ITP), such as anti-GPIIb/IIIa autoantibodies or T-cell-mediated platelet destruction. The TxGNN prediction is therefore plausible only when thrombocytopenia arises as a complication of active HES — not as a standalone therapy for primary ITP.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | Mepolizumab resolved steroid-resistant hypereosinophilic immune diathesis in a patient with atypical hemolytic uremic syndrome (aHUS), with concurrent amelioration of mixed thrombotic microangiopathy — suggesting that eosinophil-mediated platelet pathology may be partially reversible with IL-5 blockade. |

---

## Taiwan Market Information

Mepolizumab is currently not approved or marketed in Taiwan. No TFDA authorization records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole piece of supportive evidence is a single case report in a highly unusual, multi-system clinical context (aHUS + HES + thrombotic microangiopathy); there are no registered clinical trials and no systematic data linking mepolizumab to immune-mediated platelet destruction in a general patient population.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full mechanism of action from DrugBank (DG002) to strengthen the mechanistic rationale
- **Taiwan safety data**: Download and parse the TFDA package insert to complete warnings and contraindications assessment (DG001)
- **Patient subpopulation definition**: Clearly define the target cohort as "HES-associated immune thrombocytopenia" rather than primary ITP, to narrow the clinical hypothesis
- **Prospective case series or observational study**: At least a multi-centre case series is needed before advancing to a formal clinical trial design
- **International regulatory review**: Confirm whether any HES-complicated thrombocytopenia cases have been captured in the EMA or FDA post-marketing surveillance data for mepolizumab
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

