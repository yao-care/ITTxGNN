---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 1
---

# Mometasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Mometasone: From Inflammatory Skin Conditions to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is a potent topical corticosteroid originally used for inflammatory skin conditions such as eczema and dermatitis.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma (CTCL)**,
with **0 clinical trials** and **2 publications** (both case reports) currently supporting this direction — one of which recorded mometasone as a failed prior treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory skin conditions (topical corticosteroid; no formal indication text available from regulatory records) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma (CTCL) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured data source. Based on known pharmacological information, mometasone is a potent topical glucocorticoid. It exerts its effects by activating the glucocorticoid receptor (GR), which in turn suppresses the NF-κB signaling pathway — resulting in pro-apoptotic and anti-proliferative effects on T lymphocytes. This cellular-level activity forms the mechanistic basis for the TxGNN prediction.

Primary cutaneous T-cell lymphoma, particularly Mycosis Fungoides (MF), is defined by clonal malignant T-cell proliferation within the skin. Since the primary disease target (the T lymphocyte) is the same cell type suppressed by corticosteroids, there is a plausible mechanistic bridge. NCCN guidelines for early-stage MF already list topical corticosteroids as a recognized class-effect treatment option, lending indirect clinical relevance to this prediction.

However, it is important to note that no clinical trials specifically evaluating mometasone for CTCL have been registered. The available published literature does not provide controlled efficacy evidence; one case report explicitly documented mometasone as a prior treatment that failed before the patient's condition responded to an alternative agent (tapinarof). The mechanistic link is present, but drug-specific evidence is absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University. Medical Center) | 62-year-old woman with cutaneous pseudolymphoma (atypical T-cell infiltrate); mometasone and tacrolimus both failed, patient subsequently responded to tapinarof — mometasone appears as a **prior failed treatment**, not a successful one |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | 11-year-old boy with CD8+CD56+ mycosis fungoides of cytotoxic immunophenotype; slow-progressive disease over 7 years affecting trunk and extremities — documents the clinical presentation of paediatric MF, no direct mometasone efficacy data |

---

## Taiwan Market Information

Mometasone currently has **no approved products** on the Taiwan market (TFDA records). No authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for mometasone specifically in primary CTCL is limited to L4 (mechanistic/indirect), with zero registered clinical trials and only two case reports — one of which records mometasone as a treatment failure. The TxGNN model score is high (99.36%), indicating strong graph-level signal, but this reflects class-effect plausibility rather than drug-specific validation.

**To proceed, the following is needed:**

- **Mechanism of action data (MOA)**: Retrieve full pharmacodynamic profile from DrugBank API to confirm GR-mediated pro-apoptotic activity in T cells
- **Safety data**: Download and parse the TFDA package insert PDF to assess contraindications and key warnings before any S1 safety evaluation can proceed
- **Class-effect benchmarking**: Identify clinical trial data for other potent topical corticosteroids (e.g., clobetasol) in early-stage MF to establish a class-level evidence anchor
- **Drug-specific literature search**: Broaden PubMed query (e.g., "mometasone AND mycosis fungoides") to determine whether any non-trial observational data exists
- **Route compatibility assessment**: Confirm whether topical mometasone formulations (cream/ointment) are appropriate for the target CTCL lesion distribution and stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

