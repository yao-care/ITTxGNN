---
layout: default
title: Turoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa (NovoEight®) is a B-domain truncated recombinant Factor VIII (rFVIII), originally developed for the prevention and treatment of bleeding episodes in Hemophilia A.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with a prediction score of **99.99%**.
However, this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on knowledge-graph topology and carries no empirical clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hemophilia A (congenital Factor VIII deficiency) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, turoctocog alfa is a B-domain truncated recombinant human coagulation Factor VIII. It functions as a cofactor in the intrinsic tenase complex (FVIIIa + FIXa), dramatically amplifying thrombin generation via the intrinsic coagulation cascade. Its established efficacy is in Hemophilia A — a disease defined by FVIII deficiency leading to impaired secondary haemostasis.

Primary release disorder of platelets (Storage Pool Disease) involves defective release of α- and/or δ-granule contents from platelets, impairing primary haemostasis. This is a fundamentally different pathophysiological domain from FVIII's mechanism: FVIII acts on secondary haemostasis (coagulation cascade), whereas platelet granule release disorders affect primary haemostasis (platelet plug formation). The TxGNN model's connection here appears to arise from downstream convergence nodes between the coagulation cascade and platelet activation pathways in the knowledge graph — an indirect topological link rather than a direct mechanistic relationship.

In summary, the high prediction score reflects network proximity in the disease–drug knowledge graph, not a direct therapeutic mechanism. FVIII supplementation does not address the underlying defect in platelet granule secretion, and no biological rationale currently supports a clinical benefit in this condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is classified as L5 (model-only, no empirical support), the mechanistic link between FVIII supplementation and platelet release disorders is indirect and biologically implausible as a primary therapeutic strategy, and no clinical trials or publications exist to validate this repurposing hypothesis. The drug is also not currently authorised in Italy, adding a regulatory barrier to any development pathway.

**To proceed, the following would be needed:**

- **Data gaps resolution**: Obtain full package insert / SmPC to characterise known warnings, contraindications, and approved indications
- **MOA clarification**: Confirm detailed mechanism of action from DrugBank or EMA product literature
- **Mechanistic plausibility re-evaluation**: Commission a focused literature review assessing whether any secondary FVIII-related effects (e.g., thrombin burst amplification) could theoretically compensate for platelet granule release defects in ex vivo or animal models
- **Alternative higher-priority indications**: Among the 10 predicted indications, **Acquired Coagulation Factor Deficiency** (rank 5, includes Acquired Hemophilia A) represents a far more mechanistically grounded repurposing candidate and should be evaluated first
- **Italy regulatory strategy**: Given zero current authorisations in Italy, a regulatory gap analysis (EMA orphan designation potential, off-label use framework) would be required before any clinical development is initiated

---

> **⚠️ Data Quality Note — Rank 8 ("flood factor deficiency"):** This disease term is likely an OCR/encoding artefact of "blood factor deficiency." This entity should be cleaned and re-evaluated before being included in any scoring or regulatory submission.
>
> **📌 Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Any drug repurposing candidate must undergo clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

