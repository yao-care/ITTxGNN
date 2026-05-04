---
layout: default
title: Aciclovir
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Aciclovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Aciclovir: Drug Repurposing Evaluation Report — Preliminary Assessment

## One-Sentence Summary

Aciclovir is a widely used antiviral agent, primarily indicated for the treatment of herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections. The TxGNN model has **not yet generated any predicted new indications** for this drug, and the current evidence pack contains significant data gaps that must be resolved before evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (known use: HSV and VZV infections) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction or supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Aciclovir is a synthetic nucleoside analogue that selectively targets herpes virus–infected cells. It is phosphorylated by viral thymidine kinase and subsequently by cellular kinases to its active triphosphate form, which inhibits viral DNA polymerase and terminates viral DNA chain elongation.

However, **no TxGNN-predicted new indications have been generated for Aciclovir at this time**. The absence of a prediction means there is no mechanistic bridge to evaluate between the original indication and a potential new therapeutic use. This may be due to insufficient input data, network connectivity limitations in the knowledge graph, or the drug not meeting the model's threshold for novel indication prediction.

Before any repurposing assessment can be conducted, the data gaps identified below must be addressed, and the TxGNN model must produce at least one candidate indication with a confidence score.

## Clinical Trial Evidence

Currently no related clinical trials registered for a new predicted indication.

## Literature Evidence

Currently no related literature available for a new predicted indication.

## Taiwan Market Information

No TFDA marketing authorizations were found for Aciclovir. The drug is currently classified as **not marketed (未上市)** in Taiwan based on the TFDA query conducted on 2026-03-29.

## Safety Considerations

> Please refer to the package insert for safety information. The current evidence pack contains no resolved safety data (warnings, contraindications, or drug–drug interactions were not retrieved from available sources).

## Data Gaps Requiring Resolution

The following critical data gaps were identified in this evidence pack and must be addressed before further evaluation:

| Gap ID | Category | Item | Severity | Remediation |
|--------|----------|------|----------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Download and parse package insert PDF from the TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Query DrugBank API for complete MOA data |

Additionally, the following items are absent:
- **DrugBank ID**: Not linked — limits cross-referencing with DrugBank safety, pharmacology, and interaction databases
- **Original Indications**: Not populated in the evidence pack — need to extract from regulatory or reference sources
- **TxGNN Predicted Indications**: Empty — the model has not produced candidate indications for this drug

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for Aciclovir is critically incomplete. There are **no TxGNN-predicted new indications**, no resolved safety data, no Taiwan marketing authorizations, and two identified data gaps (one of which is Blocking severity). Evaluation cannot proceed until fundamental input data is available.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): Obtain and parse TFDA package insert for warnings and contraindications
- Resolve **DG002** (High): Retrieve mechanism of action from DrugBank (DrugBank ID: [DB00787](https://go.drugbank.com/drugs/DB00787) for Aciclovir)
- Populate the `original_indications` field from regulatory or pharmacopoeia sources
- Re-run the TxGNN prediction pipeline to generate candidate new indications
- Once a predicted indication is available, collect clinical trial and literature evidence to support evaluation

---

*This report was generated on 2026-04-03. Results are for research reference only and do not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

