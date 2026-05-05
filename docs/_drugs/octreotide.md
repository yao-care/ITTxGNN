---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 2
---

# Octreotide
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

Using the `txgnn-pipeline` skill to set context, then proceeding with report generation per the v5 prompt specification.

---

# Octreotide: From Acromegaly/Neuroendocrine Tumors to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a synthetic somatostatin analogue with established clinical use in acromegaly, carcinoid syndrome, and neuroendocrine tumors.
The TxGNN model predicts it may be effective for **Vulvar Inverted Follicular Keratosis**,
but with **0 clinical trials** and **0 publications** currently supporting this direction, the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acromegaly, carcinoid syndrome, neuroendocrine tumors (no Italy authorization on file) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Octreotide is a synthetic octapeptide analogue of somatostatin that primarily agonizes SSTR2 and SSTR5 receptors, suppressing growth hormone (GH), IGF-1, and various gastrointestinal hormones. Its proven efficacy in acromegaly and neuroendocrine tumors is mediated entirely through this somatostatin receptor axis.

The proposed mechanistic link to **Vulvar Inverted Follicular Keratosis (IFK)** is highly indirect and requires at least four inferential steps: (1) SSTR2/5 receptors are expressed at low levels in epidermal keratinocytes; (2) Octreotide suppresses IGF-1 release, which could theoretically dampen IGF-1R–driven keratinocyte proliferation; (3) IFK is a rare benign tumor of hair follicle origin associated with HPV infection and acanthomatous differentiation — conditions with no established connection to the SSTR axis; (4) no study has directly explored SSTR agonism in IFK or related follicular keratoses.

The TxGNN graph-network model assigns a high numerical score (99.58%), but this reflects structural proximity in the knowledge graph, not clinical plausibility. The mechanistic inference here is among the weakest category of repurposing signals, and the extreme rarity of vulvar IFK makes prospective clinical validation highly impractical without at minimum preclinical in vitro confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Octreotide currently holds **no marketing authorizations in Italy**. The drug is not marketed and no AIFA-approved licenses are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model-prediction signal (Evidence Level L5) with zero supporting clinical trials or published literature. The mechanistic connection between Octreotide's somatostatin receptor agonism and vulvar inverted follicular keratosis spans ≥4 indirect graph hops with no experimental validation at any level — cell, animal, or human.

**To proceed, the following is needed:**

- **Preclinical mechanistic validation:** Confirm SSTR2/5 functional expression in IFK tumor cells and test Octreotide anti-proliferative activity in vitro before any further investment
- **Expanded literature review:** Broaden search to somatostatin analogues + skin keratosis, follicular tumors, and HPV-driven epithelial proliferation to identify any indirect supportive evidence
- **MOA documentation:** Retrieve full DrugBank pharmacology data to formally characterize the drug–disease graph path
- **Safety profile:** Obtain complete prescribing information (warnings, contraindications, DDI) — currently all safety fields are data gaps
- **Italy regulatory pathway:** Octreotide is not marketed in Italy; establishing regulatory status and formulation availability is a prerequisite for any clinical development program in this jurisdiction
- **Disease feasibility check:** Vulvar IFK is an extremely rare benign condition — conduct epidemiological scoping to assess whether a clinical trial population is even achievable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

