---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

Using the TxGNN pipeline skill context, I'll now produce the full evaluation report for Nitisinone.

---

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone (NTBC) is an HPPD enzyme inhibitor originally approved for Hereditary Tyrosinemia Type 1 (HT-1), a rare inborn error of tyrosine metabolism causing progressive liver and kidney damage.
The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**, with **0 clinical trials** and **2 publications** currently supporting this direction — both of which describe renal tubular recovery specifically in HT-1 patients on NTBC, rather than evidence in primary renal tubular acidosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hereditary Tyrosinemia Type 1 (HT-1) — derived from clinical context; no Italy registration on file |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, nitisinone inhibits **4-hydroxyphenylpyruvate dioxygenase (HPPD)**, an enzyme in the tyrosine degradation pathway. In HT-1, a defective downstream enzyme (fumarylacetoacetate hydrolase, FAH) causes toxic metabolites — chiefly **succinylacetone** — to accumulate. By blocking HPPD upstream, nitisinone prevents succinylacetone production and halts the cascade of hepatic and renal injury.

The predicted link to renal tubular acidosis arises from HT-1's renal phenotype: succinylacetone directly damages proximal renal tubules, producing secondary Fanconi syndrome with features of tubular acidosis. Clinical observations confirm that NTBC therapy improves this tubular dysfunction in HT-1 patients — explaining why the TxGNN knowledge graph connected nitisinone to the renal tubular acidosis node.

However, this mechanistic bridge is **strictly HT-1-specific**. Primary renal tubular acidosis (driven by mutations in SLC4A1, ATP6V1B1, CA2, or other tubular transporters) has no shared upstream metabolic pathway with HT-1. Nitisinone offers no pharmacological rationale against primary RTA. The TxGNN prediction most likely reflects a shared graph neighbourhood ("toxic metabolite accumulation → tubular injury") rather than a genuine new indication pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Observational Study | Molecular Genetics and Metabolism | Prospective follow-up in HT-1 patients showing that NTBC therapy produces early, measurable improvement of proximal renal tubular dysfunction (Fanconi syndrome markers) within weeks of treatment initiation |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case Series | Indian Journal of Gastroenterology | Four paediatric HT-1 cases treated with NTBC: three maintained normal liver function, undetectable urinary succinylacetone, and no portal hypertension or residual renal tubular signs after ~3 years of therapy |

> **Note:** Both publications report renal outcomes as secondary findings within HT-1 management, not as standalone studies of nitisinone in renal tubular acidosis.

---

## Italy Market Information

Nitisinone is not registered in Italy. No marketing authorizations are on file. Orfadin® (the branded formulation) holds EMA orphan designation and is approved in the EU for HT-1, but Italy-specific authorization data was not returned in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for renal tubular acidosis is biologically explainable, but only within the HT-1 disease context — both supporting publications describe secondary renal improvement in HT-1 patients, not therapeutic activity against primary or idiopathic renal tubular acidosis. Without a plausible mechanism outside of HT-1 and with zero registered clinical trials, this indication does not warrant active development as a new target.

**To proceed, the following is needed:**

- A mechanistic hypothesis for NTBC activity in primary (non-HT-1) renal tubular acidosis (e.g., inherited transportopathies or toxic secondary RTA from other metabolic causes)
- Identification of RTA subtypes where toxic tyrosine metabolites, or an analogous upstream enzyme block, could be operative
- Preclinical data (cell or animal models of primary RTA) testing nitisinone
- Retrieval of the full package insert (TFDA / EMA SmPC) to assess contraindications, key warnings, and drug interactions before any safety evaluation can proceed
- Expert review by a metabolic disease specialist to evaluate graph-predicted plausibility vs. clinical reality
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

