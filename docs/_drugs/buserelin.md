---
layout: default
title: Buserelin
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 5
---

# Buserelin
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

以下為依據 Evidence Pack 產生的藥師評估報告：

---

# Buserelin: From Hormone-Dependent Conditions to Hypertrichosis

## One-Sentence Summary

Buserelin is a synthetic GnRH (gonadotropin-releasing hormone) agonist used clinically to suppress sex hormone production in hormone-sensitive conditions, though no approved indication is formally recorded in the current dataset.
The TxGNN model predicts it may be relevant for **Hypertrichosis**, with **0 clinical trials** and **1 publication** currently touching on this area — making the evidence base extremely limited.
Given the weak mechanistic rationale and absence of direct clinical evidence, this candidate currently does not meet the threshold for active development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Buserelin is a GnRH agonist: when administered continuously, it downregulates pituitary GnRH receptors, thereby suppressing LH and FSH secretion and dramatically reducing downstream sex hormone production (testosterone and estrogen). This mechanism is the basis of its use in hormone-sensitive conditions such as prostate cancer and endometriosis.

The core problem with this prediction is a conceptual mismatch between the drug's mechanism and the target disease. **Hypertrichosis** — excessive hair growth occurring in a generalized, non-patterned distribution — is largely **not androgen-dependent**. This distinguishes it fundamentally from hirsutism (androgen-driven, patterned excess hair growth in women), where GnRH agonists do have a theoretical and practical rationale. Hypertrichosis can arise from genetic mutations, medications, paraneoplastic phenomena, or systemic conditions — none of which are addressed by GnRH axis suppression.

The single supporting publication (a 2019 case report on Cantu syndrome) describes hypertrichosis as one feature of a rare genetic disorder with pituitary involvement. It neither evaluates Buserelin as a treatment nor proposes any hormonal intervention for the hair phenotype. The TxGNN model likely detected a surface-level co-occurrence between GnRH axis signals and hair growth phenotypes, but the biological rationale for using Buserelin to actively treat hypertrichosis remains unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Case Report | *Endocrinology, Diabetes & Metabolism Case Reports* | Describes a patient with Cantu syndrome (hypertrichotic osteochondrodysplasia) found to have multiple pituitary hormone deficiencies; supports routine endocrine monitoring in this rare genetic condition — does not evaluate Buserelin as a treatment for hypertrichosis |

---

## Italy Market Information

Buserelin currently has **no approved authorizations in Italy**. It is not marketed, and no license records are on file in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.75%), the biological rationale is critically weak — hypertrichosis is predominantly non-androgen-dependent, meaning Buserelin's core mechanism of GnRH suppression has no plausible therapeutic pathway to this indication. No clinical trials exist, and the only associated publication is an indirect case report unrelated to Buserelin's use.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) retrieved from DrugBank or primary pharmacology sources
- Confirmed original approved indications via EMA or TFDA package insert
- Complete safety profile including key warnings, contraindications, and drug interactions
- Preclinical or mechanistic evidence specifically linking GnRH suppression to hypertrichosis pathophysiology (currently absent)
- If further pursuit is considered, a literature review focusing on androgen-dependent subtypes of hypertrichosis where a hormonal intervention could be justified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

