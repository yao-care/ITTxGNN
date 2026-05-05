---
layout: default
title: Lonafarnib
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 1
---

# Lonafarnib
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

Using **txgnn-pipeline** skill to guide report generation for this TxGNN evidence pack.

---

# Lonafarnib: From Hutchinson-Gilford Progeria Syndrome to Leprosy

## One-Sentence Summary

Lonafarnib (Zokinvy) is a farnesyltransferase (FTase) inhibitor and the first FDA-approved therapy for Hutchinson-Gilford Progeria Syndrome (HGPS) and processing-deficient Progeroid Laminopathies.
The TxGNN model predicts it may have therapeutic potential for **Leprosy**, yet with **0 clinical trials** and **0 publications** currently supporting this direction, the prediction rests entirely on model inference derived from the biomedical knowledge graph — no clinical or experimental evidence is available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hutchinson-Gilford Progeria Syndrome (HGPS); not registered in Taiwan |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not included in this Evidence Pack. Based on publicly available pharmacological information, Lonafarnib is a farnesyltransferase (FTase) inhibitor — it competitively blocks the attachment of a farnesyl group (derived from farnesylpyrophosphate) to proteins bearing a CaaX motif. In Hutchinson-Gilford Progeria Syndrome, this prevents the nuclear accumulation of progerin, a permanently farnesylated truncated form of Lamin A that drives accelerated vascular aging. The same anti-farnesylation mechanism was the original rationale for investigating Lonafarnib as an anticancer agent, since oncogenic Ras proteins also require farnesylation for membrane anchoring and activation.

The biological link between Lonafarnib and leprosy is not well supported. *Mycobacterium leprae*, the causative bacterium of leprosy, has no known virulence proteins that require host-mediated farnesylation. Neither is there published evidence of a direct mechanistic pathway connecting host FTase inhibition to anti-mycobacterial activity or modulation of the granulomatous immune response characteristic of leprosy.

The TxGNN model's high prediction score (0.9913) most likely reflects indirect structural proximity within the biomedical knowledge graph — for example, shared comorbidity nodes, protein-protein interaction neighbourhoods, or overlapping pathway annotations — rather than a direct mechanistic rationale. Such graph-topology-derived scores can occasionally surface genuine repurposing candidates, but without a biologically interpretable mechanism this prediction cannot be prioritised without further experimental validation.

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
This prediction is supported by L5 evidence only — TxGNN model inference with no clinical trials, no published literature, and no established mechanistic pathway connecting farnesyltransferase inhibition to *Mycobacterium leprae* infection or leprosy pathogenesis.

**To proceed, the following is needed:**
- Preclinical studies (in vitro or animal model) examining whether Lonafarnib or other FTase inhibitors affect M. leprae viability, growth, or host immune responses
- Mechanistic analysis clarifying whether host FTase inhibition could plausibly influence mycobacterial intracellular survival or the granulomatous response in leprosy
- Trace-back analysis of the TxGNN knowledge-graph pathways that generated this score, to assess whether any intermediate biological node provides a credible rationale
- Full safety profile review including warnings, contraindications, and drug interaction data from the approved package insert before any further clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

