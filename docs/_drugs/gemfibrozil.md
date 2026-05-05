---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

The txgnn-pipeline skill is noted. This task is report generation from an Evidence Pack — I'll apply the report format specification in the system prompt directly.

---

# Gemfibrozil: From Hypertriglyceridemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a fibrate-class lipid-lowering agent (PPARα agonist) classically used for the management of hypertriglyceridemia and mixed dyslipidemia.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** (RA), with **0 clinical trials** and **4 publications** currently supporting this direction — evidence is at an early, preclinical stage.
The biological rationale centres on PPARα-mediated suppression of inflammatory cytokines, but human-level validation is entirely absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertriglyceridemia / Dyslipidemia (fibrate class; no Italy registration on record) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on well-established pharmacology, gemfibrozil is a **PPARα (peroxisome proliferator-activated receptor alpha) agonist** of the fibrate class. Its classical role is to reduce serum triglycerides and raise HDL cholesterol by increasing lipoprotein lipase activity and reducing hepatic VLDL secretion.

The anti-inflammatory bridge to rheumatoid arthritis is mechanistically plausible. PPARα activation suppresses **NF-κB signalling**, which is the master transcription factor driving synovial inflammation in RA. Downstream consequences include downregulation of TNF-α, IL-6, and IL-1β — the very cytokines that biologics such as adalimumab and tocilizumab are designed to block. Additionally, fibrate-class compounds with partial PPARγ co-agonism can inhibit osteoclast differentiation, potentially limiting the bone erosion that defines progressive RA.

The most direct supporting evidence comes from a 2019 rat adjuvant-induced arthritis (AIA) model study (PMID 30074417), which found that gemfibrozil combined with reduced-dose prednisolone achieved arthritis control equivalent to full-dose prednisolone — suggesting a **steroid-sparing effect**. A 2026 collagen-induced arthritis (CIA) study of bezafibrate, another fibrate, further validates the fibrate class mechanism via PPAR-γ-dependent immune modulation (PMID 41207105). However, these are animal models, and extrapolation to human RA requires dedicated clinical investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal study (AIA model) | Modern Rheumatology | Gemfibrozil (30 mg/kg) combined with reduced-dose prednisolone achieved arthritis control comparable to full-dose prednisolone in a rat AIA model; supports steroid-sparing potential via PPARα |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Animal study (CIA model) | Int Immunopharmacology | Bezafibrate (pan-PPAR agonist) attenuated experimental RA via PPAR-γ-dependent modulation of inflammatory pathways; demonstrates fibrate class anti-arthritic mechanism |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Mechanistic study | J Immunology | Nitric oxide downregulates Foxp3 in regulatory T cells following MBP priming; provides mechanistic context for immune dysregulation in autoimmune disease relevant to RA pathophysiology |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review | Am J Clin Dermatology | Palmar erythema as a secondary marker of systemic pathology including RA; indirect relevance only — not a gemfibrozil study |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Two data gaps were identified in this Evidence Pack that directly affect safety evaluation: (1) Italy/TFDA package insert warnings and contraindications were not retrieved (DG001, Severity: Blocking); (2) Formal MOA data from DrugBank is absent (DG002, Severity: High). Both must be resolved before any clinical safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting gemfibrozil for rheumatoid arthritis is limited exclusively to animal models and mechanistic studies (L4), with no human clinical trials registered and no controlled human data. Although the PPARα → NF-κB → cytokine suppression pathway is biologically coherent, the gap between rodent AIA models and clinical RA is substantial and well-documented.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve Italy/TFDA package insert to establish contraindications and key warnings before any safety evaluation
- **Resolve DG002 (High):** Confirm full DrugBank MOA profile for gemfibrozil, including known pharmacodynamic interactions with RA co-medications (DMARDs, NSAIDs, biologics)
- **DDI risk assessment:** Gemfibrozil is a strong CYP2C8 inhibitor — evaluate interaction potential with methotrexate and other RA standard-of-care agents
- **Preclinical specificity:** Commission gemfibrozil-specific (not class-level) synovial cell line studies and dose-response characterisation in CIA model
- **Comparative positioning:** Justify gemfibrozil over bezafibrate or fenofibrate, both of which have stronger or more recent animal RA evidence
- **Regulatory feasibility:** Assess whether the Italy (AIFA) off-label or compassionate use pathway applies given zero domestic market authorisations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

