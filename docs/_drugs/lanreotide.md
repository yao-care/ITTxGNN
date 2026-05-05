---
layout: default
title: Lanreotide
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 5
---

# Lanreotide
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

Using the `txgnn-pipeline` skill for context on this TxGNN report. Now generating the evaluation report based on the Evidence Pack.

---

# Lanreotide: From Acromegaly to Hypertrichosis

## One-Sentence Summary

Lanreotide is a long-acting somatostatin analogue used internationally to treat acromegaly and gastroenteropancreatic neuroendocrine tumors by suppressing growth hormone (GH) and IGF-1 secretion — it is not currently marketed in Italy.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but **no clinical trials** and **no published literature** currently support this direction.
This prediction rests entirely on an indirect theoretical link between the GH/IGF-1 axis and hair follicle biology, and should be treated as a model-generated hypothesis only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Italy; internationally indicated for acromegaly and gastroenteropancreatic neuroendocrine tumors (GEP-NETs) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Lanreotide is a synthetic octapeptide that selectively binds to somatostatin receptors — primarily SSTR2 and SSTR5. This receptor activation suppresses pituitary GH secretion and reduces circulating IGF-1 levels. Its efficacy in acromegaly (GH excess) and in slowing tumor growth in GEP-NETs has been confirmed across multiple international markets and regulatory approvals.

The connection to hypertrichosis is built on one step of indirect reasoning: IGF-1 is a recognized promoter of hair follicle proliferation and cycling. By lowering IGF-1, Lanreotide could theoretically attenuate abnormal hair growth. This line of thinking is biologically plausible on paper, but it does not account for the actual pathogenesis of hypertrichosis, which is predominantly driven by genetic mutations (affecting TRPS1, keratin structural genes, or chromosomal loci such as 8q) or by drug-induced side effects — both of which are entirely independent of the GH/IGF-1 axis.

The somatostatin pathway has no established role in hypertrichosis pathogenesis. The TxGNN model most likely generated this prediction by traversing network-level associations between IGF-1 biology and hair follicle biology across its disease–drug knowledge graph. This is a hypothesis-generating signal that requires laboratory validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Lanreotide is not currently authorized or marketed in Italy. No regulatory licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure L5 prediction — no clinical trials, no published literature, and a mechanistic rationale that is speculative at best. The theoretical link between somatostatin receptor agonism and hypertrichosis is not supported by any established pathophysiological evidence, and the drug is not approved in Italy, adding further regulatory distance from any near-term application.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro hair follicle models or animal studies demonstrating that SSTR2/SSTR5 agonism measurably reduces pathological hair growth
- **Retrospective pharmacovigilance review**: Whether acromegaly patients treated with Lanreotide show any incidental reduction in hypertrichosis symptoms in published case reports or registries
- **Mechanistic studies**: Direct confirmation that IGF-1 suppression inhibits the specific hair follicle pathways involved in hypertrichosis subtypes (not just general follicle cycling)
- **MOA data retrieval**: Full mechanism of action from DrugBank (DB06791) to confirm receptor subtype selectivity and downstream signaling relevant to hair biology
- **Safety data retrieval**: Key warnings and contraindications from the TFDA/EMA package insert — currently unavailable and required before any clinical evaluation can proceed
- **Italy regulatory pathway assessment**: Whether an orphan designation or compassionate use framework would be applicable given the rarity of the condition and current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

