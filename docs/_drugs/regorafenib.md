---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 8
---

# Regorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

The txgnn-pipeline skill covers pipeline operations and deployment rather than report generation — the detailed report format instructions in this session's system prompt take full precedence. Proceeding with the report now.

---

# Regorafenib: From Colorectal Cancer / GIST to Liposarcoma

## One-Sentence Summary

Regorafenib (Stivarga®) is an oral multikinase inhibitor approved in multiple major markets (FDA, EMA) for metastatic colorectal cancer, refractory gastrointestinal stromal tumour (GIST), and hepatocellular carcinoma, though it is not currently registered in Italy.
The TxGNN model predicts it may be effective for **Liposarcoma**, a subtype of soft tissue sarcoma, with a prediction score of **99.76%**.
This direction is supported by **2 completed Phase 2 clinical trials** specifically including liposarcoma cohorts and **9 publications**, placing the overall evidence at Level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Italy; globally approved for metastatic colorectal cancer, refractory GIST, and hepatocellular carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Regorafenib is an oral multikinase inhibitor that broadly targets angiogenic kinases (VEGFR1–3, TIE2), stromal kinases (PDGFR-β, FGFR), and oncogenic kinases (KIT, RET, RAF). Its established efficacy in colorectal cancer, GIST, and HCC all rely on blocking tumour vascular dependence — a mechanism shared across many solid tumour types. Detailed mechanistic data was not available from the regulatory database for this report; however, the target profile is extensively described in published literature (e.g., PMID 30069758, 24756792).

Liposarcoma belongs to the soft tissue sarcoma (STS) family and its tumour microenvironment is heavily driven by VEGFR/PDGFR-mediated angiogenesis, particularly in the dedifferentiated subtype where MDM2/CDK4 amplification co-exists with active angiogenic signalling. Regorafenib's simultaneous blockade of VEGFR1–3 and PDGFR-β provides a biologically plausible mechanism for anti-tumour activity, especially in dedifferentiated liposarcoma with high angiogenic burden.

The most critical context, however, is that two randomized Phase 2 trials — REGOSARC (NCT01900743) and SARC024 (NCT02048371) — directly tested regorafenib in liposarcoma-specific cohorts. Both confirmed limited activity in the *broad* liposarcoma population: the REGOSARC trial demonstrated significant PFS improvement in non-adipocytic STS subtypes (leiomyosarcoma, synovial sarcoma) but not in the liposarcoma cohort; SARC024 similarly did not support routine use in liposarcoma overall. These findings suggest that while a biologically rational subpopulation may exist, patient selection criteria or combination strategies will be essential to realising clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC: International, randomised, double-blind, placebo-controlled trial of regorafenib vs placebo in metastatic/unresectable STS after anthracycline failure. Includes a dedicated Liposarcoma cohort (Cohort A). Significant PFS improvement confirmed in non-adipocytic subtypes; liposarcoma cohort showed a trend but did not reach statistical significance (primary results: PMID 27751846). |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: Umbrella Phase 2 study of oral regorafenib across multiple sarcoma subtypes, each analysed independently. The liposarcoma cohort results (PMID 32701199) did not support routine use of regorafenib in this population; the authors conclude that novel therapies or combination approaches are warranted given limited treatment options. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | Randomized Phase 2 RCT | *The Lancet Oncology* | REGOSARC primary results: Regorafenib significantly improved PFS over placebo in non-adipocytic STS (leiomyosarcoma, synovial sarcoma, other subtypes); liposarcoma cohort did not meet the primary endpoint. Establishes differential activity by histological subtype. |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | Randomized Phase 2 RCT | *The Oncologist* | SARC024 liposarcoma cohort: Confirms REGOSARC findings — regorafenib does not support routine use in the broad liposarcoma population. Emphasises need for novel therapies and combination approaches. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | Phase 2 Cross-over Analysis | *European Journal of Cancer* | Updated REGOSARC analysis including post-cross-over regorafenib activity: confirmed efficacy in non-adipocytic STS; liposarcoma (adipocytic) remains a subgroup without significant benefit. Provides long-term follow-up data. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective Study | *Anti-Cancer Drugs* | Anlotinib in unresectable/metastatic well-differentiated/dedifferentiated liposarcoma. References that TKIs including regorafenib are approved in non-adipocytic STS, contextualising the class of agents in this disease and the unmet need in the adipocytic subtypes. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Systematic Review | *Critical Reviews in Oncology/Hematology* | Systematic review of maintenance therapy strategies in advanced STS. Reviews eight randomized trials including regorafenib-based approaches, contextualising its role within the overall STS treatment landscape post-first-line doxorubicin. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Phase 2 Secondary Analysis | *Cancer* | Q-TWiST analysis of REGOSARC: Integrated measure of clinical benefit (progression-free time + quality of life − toxicity time) in non-adipocytic sarcoma. Supports net clinical benefit of regorafenib when QoL and toxicity are factored in alongside PFS. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Narrative Review | *Targeted Oncology* | Comprehensive review of regorafenib's growing role across STS subtypes (liposarcoma, leiomyosarcoma, GIST). Summarises Phase 2/3 trial data and discusses the varying activity by histological subtype. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial Protocol | *BMC Cancer* | REGOSARC protocol paper: describes scientific rationale (angiogenesis as a key target in sarcoma biology), study design, stratification by histological subtype, and primary/secondary endpoints. Useful for understanding the trial's a priori hypotheses. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case Series (Indirect) | *Rare Tumors* | Pazopanib activity in metastatic Ewing sarcoma; provided the clinical rationale for expanding the SARC024 umbrella to include Ewing sarcoma alongside liposarcoma and osteosarcoma. Indirect reference supporting TKI class rationale in sarcoma. |

---

## Italy Market Information

Regorafenib is **not currently registered in Italy (AIFA)**. No marketing authorizations were identified in the regulatory search conducted on 2026-03-29.

> **Note:** Regorafenib (Stivarga®) holds marketing authorizations in other major regulatory jurisdictions, including the US (FDA, approved 2012 for mCRC; 2013 for GIST; 2017 for HCC) and the EU (EMA). Any compassionate use or named-patient access in Italy would need to follow AIFA's relevant provisions (e.g., Law 648/1996 or Article 3 of Law 79/2014).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Multikinase Inhibitor (VEGFR/PDGFR/RAF/KIT/RET/FGFR inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate — thrombocytopenia and neutropenia are reported adverse events, but myelosuppression is generally less severe than with conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low — oral targeted therapy; nausea occurs but high-grade emesis is uncommon |
| Monitoring Items | Complete blood count (with differential and platelets), liver function tests (ALT, AST, bilirubin, alkaline phosphatase), serum creatinine, blood pressure, thyroid function, urinalysis for protein |
| Handling Protection | Follow institutional protocols for oral cytotoxic/targeted agent handling; standard precautions for preparation and disposal apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed, randomised Phase 2 trials (REGOSARC and SARC024) have directly investigated regorafenib in liposarcoma-specific cohorts, establishing an L2 evidence base. However, both trials showed that regorafenib does not provide significant benefit in the *broad* liposarcoma population — the effect is concentrated in non-adipocytic STS subtypes. Biological plausibility is genuine (VEGFR/PDGFR pathway dependence in dedifferentiated liposarcoma), but clinical development should target molecularly enriched subgroups rather than unselected patients.

**To proceed, the following is needed:**
- **Mechanistic data (MOA):** Obtain from DrugBank API or Italy package insert to confirm kinase target profile relevant to liposarcoma biology
- **Safety documentation:** Retrieve Italy/EMA package insert for complete warnings, contraindications, and drug interaction data; AIFA access pathway assessment
- **Patient selection criteria:** Identify biomarker-defined subgroups in dedifferentiated liposarcoma (e.g., high angiogenic gene signature, VEGFR/PDGFR expression) most likely to respond to multikinase inhibition
- **Combination strategy exploration:** Evaluate regorafenib + immunotherapy (PD-1/L1) or CDK4/6 inhibition combinations in dedifferentiated liposarcoma, where single-agent VEGFR targeting showed insufficient activity
- **Regulatory pathway:** Define a compassionate use or named-patient access strategy under AIFA provisions given absence of Italian registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

