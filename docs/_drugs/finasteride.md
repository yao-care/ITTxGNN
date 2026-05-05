---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

The txgnn-pipeline skill covers pipeline operations, not report writing — the detailed report format is already specified in the system prompt. Proceeding directly to generate the evaluation report.

---

# Finasteride: From Androgenetic Alopecia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5α-reductase type II inhibitor, globally approved for male androgenetic alopecia (1 mg) and benign prostatic hyperplasia (5 mg), both driven by excess dihydrotestosterone (DHT).
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital disorder of generalised hair overgrowth.
However, **no clinical trials and no supporting publications** have been identified for this specific indication, placing the evidence at the lowest level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication registered in Italy (licence data unavailable) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the Evidence Pack. Based on established pharmacological knowledge, Finasteride inhibits the 5α-reductase type II enzyme, blocking the peripheral conversion of testosterone to dihydrotestosterone (DHT). Reduction of DHT at the hair follicle level is the basis for its approved use in androgen-dependent hair disorders — most notably male-pattern androgenetic alopecia — where follicle miniaturisation is driven by DHT hypersensitivity.

Ambras syndrome (Ambras type hypertrichosis universalis congenita) is a rare congenital condition caused by chromosomal rearrangement at Xq24–q27.1, leading to widespread excessive body hair growth from birth or early infancy. Critically, this disorder is **not androgen-dependent**: its pathogenesis stems from a structural genomic abnormality, not from dysregulation of the androgen/DHT axis. Finasteride's mechanism of action therefore has no direct biological basis for addressing this condition.

The extremely high TxGNN score (99.99%) most likely reflects a **graph neural network neighbourhood spillover** from the broader "hair disease" node cluster rather than a genuine biological signal. Predictions of this type — high model score, zero clinical evidence, mechanistically implausible — are a known limitation of knowledge-graph-based repurposing and should be regarded as hypothesis-generating noise rather than actionable leads at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Finasteride has no registered authorisations in Italy based on available regulatory data. No licence records were retrieved from the AIFA database query.

> **Note:** Finasteride (Propecia® 1 mg, Proscar® 5 mg) is known to be marketed in several European markets. The absence of records may reflect a data retrieval gap rather than a true absence of authorisation. Verification against the current AIFA online registry is recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not retrievable from the queried sources for this evidence pack. The package insert of the Italy-approved product should be consulted directly. Clinically notable known risks for finasteride include sexual dysfunction (decreased libido, erectile dysfunction, ejaculatory disorder), post-finasteride syndrome (persistent adverse effects after discontinuation), and teratogenicity (Category X in pregnancy — exposure risk for women of childbearing potential handling crushed tablets).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ambras type hypertrichosis universalis congenita is a non-androgen-dependent genetic disorder; finasteride's DHT-reducing mechanism has no established or plausible biological pathway to address the underlying chromosomal aetiology, and zero clinical or preclinical evidence supports this repurposing direction.

**To proceed, the following is needed:**
- Preclinical mechanistic evidence demonstrating any effect of DHT suppression on the Xq24–q27.1 rearrangement phenotype or on non-androgen-mediated hair follicle overgrowth
- Verification of Italy (AIFA) regulatory status for finasteride via direct registry query
- Full safety data from the AIFA-approved package insert (warnings, contraindications, teratogenicity)
- Review of the rank 2 prediction — **hypertrichosis (disease)** (L4, Research Question) — which, while limited to older narrative reviews, has a partial mechanistic basis for androgen-driven subtypes and represents a more scientifically defensible starting point for any future hypothesis-generation work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

