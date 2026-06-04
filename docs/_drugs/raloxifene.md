---
layout: default
title: Raloxifene
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 4
---

# Raloxifene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

The `txgnn-pipeline` skill confirms this is a TxGNN drug repurposing context. The report generation instructions are fully specified in the system prompt. I'll now produce the report from the Evidence Pack.

---

# Raloxifene: From Postmenopausal Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Raloxifene is a Selective Estrogen Receptor Modulator (SERM) widely established for the prevention and treatment of postmenopausal osteoporosis and reduction of invasive breast cancer risk in postmenopausal women.
The TxGNN model predicts it may be effective for **Duodenal Ulcer (disease)**, with **0 clinical trials** and **0 publications** currently supporting this direction — placing this prediction at Evidence Level L5 and making it a hypothesis-only signal requiring foundational investigation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postmenopausal osteoporosis; invasive breast cancer risk reduction |
| Predicted New Indication | Duodenal Ulcer (disease) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmaceutical knowledge, Raloxifene is a SERM that selectively modulates estrogen receptors in a tissue-specific manner: it acts as an estrogen agonist in bone (preserving bone mineral density) and in hepatic lipid metabolism, while acting as an antagonist in breast and uterine tissue — thereby avoiding stimulation of endometrial proliferation.

The mechanistic bridge to duodenal ulcer is built on the biology of ER-β (estrogen receptor beta), which is the dominant estrogen receptor subtype expressed in the gastrointestinal tract. Activation of ER-β has been proposed to promote mucus secretion, upregulate prostaglandin synthesis, and suppress NF-κB-driven mucosal inflammation — all of which are recognized gastroprotective mechanisms relevant to ulcer prevention and healing. In theory, if Raloxifene exerts meaningful ER-β agonist activity in the duodenal mucosa, it could confer a degree of mucosal protection.

However, this remains a class-effect inference rather than a Raloxifene-specific finding. Raloxifene's tissue selectivity for ER-β in the duodenum has not been specifically studied, and the repurposing rationale embedded in this Evidence Pack rates mechanistic credibility as **low to moderate**. There are no preclinical, observational, or clinical data to substantiate this prediction at present. The high TxGNN score reflects a graph-structural signal in the knowledge graph and should not be interpreted as clinical confidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Raloxifene has no approved product authorizations in Taiwan. Taiwan TFDA records return zero licenses, and no approved indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both TFDA package insert warnings/contraindications and drug-drug interaction data are currently unavailable for this Evidence Pack (identified as data gaps DG001 and DG002). These must be retrieved from the TFDA official website and DrugBank before any clinical or regulatory evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported exclusively by a TxGNN model score with no corroborating clinical trials, literature, or preclinical data (Evidence Level L5). The proposed ER-β mucosal protection mechanism is biologically speculative, the drug is not marketed in Taiwan, and two blocking data gaps — safety warnings and MOA — remain unresolved, making meaningful risk–benefit assessment impossible at this stage.

**To proceed, the following is needed:**

- **MOA data**: Retrieve Raloxifene mechanism of action from DrugBank API to confirm whether ER-β agonist activity in gastrointestinal tissue is documented
- **Safety data**: Download and parse the TFDA package insert to obtain warnings, contraindications, and drug interactions (currently blocking; severity: High/Blocking)
- **Preclinical signal check**: Search for animal model or cell-line studies examining estrogen receptor modulation and duodenal mucosal integrity
- **Epidemiological signal check**: Assess whether postmenopausal women on Raloxifene in real-world databases (e.g., CPRD, TriNetX) show lower rates of peptic or duodenal ulcer
- **Expert review**: Obtain gastroenterology expert opinion on the ER-β gastroprotection hypothesis before allocating research resources
- If a preclinical signal is confirmed, design a proof-of-concept Phase 2 trial or mechanistic study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

