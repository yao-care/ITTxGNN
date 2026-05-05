---
layout: default
title: Tolcapone
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

---

# Tolcapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Tolcapone is a selective COMT (catechol-O-methyltransferase) inhibitor, originally approved as adjunct therapy in adult Parkinson's disease to extend the effect of levodopa.
The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**, a rare chronic autoimmune encephalopathy.
Currently, **no clinical trials** and **no published literature** support this direction — the prediction rests entirely on the model's graph-level inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on contextual information throughout the dataset, Tolcapone is a COMT inhibitor — it blocks the enzyme that degrades dopamine and levodopa in the periphery and brain, thereby increasing dopamine availability at the synapse. Its efficacy in Parkinson's disease is well-established along this dopaminergic axis.

Rasmussen subacute encephalitis is a rare, progressive autoimmune disorder in which cytotoxic T-cells attack neurons in one cerebral hemisphere, causing drug-resistant focal epilepsy and progressive neurological decline. The core pathology is immune-mediated — not dopamine-related. There is no known mechanism by which COMT inhibition would suppress autoreactive T-cell activity or reduce neuronal destruction in this disease.

The high TxGNN score (99.93%) most likely reflects **graph-level disease proximity** — Tolcapone and Rasmussen encephalitis both occupy "neurological disease" nodes in the knowledge graph, creating an apparent link through network propagation rather than genuine pharmacological relevance. This is a recognized limitation of graph neural network models: high scores can arise from structural graph similarity without mechanistic support. At this stage, this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Tolcapone carries a known risk of **fatal fulminant hepatic failure**. This is one of the most serious concerns with this drug class and should be a central consideration in any repurposing evaluation. Full safety profiling — including contraindications, black box warnings, and drug-drug interactions — must be retrieved from the official package insert before any clinical development is pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score, this prediction has no mechanistic basis, no supporting clinical trials, and no relevant literature. The score almost certainly reflects graph topology artefact rather than pharmacological signal, and Tolcapone's known hepatotoxicity profile raises a significant safety bar for any new indication.

**To proceed, the following is needed:**
- Full MOA documentation and safety profile (including black box hepatotoxicity warning) retrieved from the official package insert or DrugBank API
- A biologically plausible hypothesis connecting COMT inhibition to Rasmussen encephalitis pathophysiology (e.g., any role of catecholamine dysregulation in autoimmune neuroinflammation)
- At minimum one preclinical study or case report before this indication can be elevated above L5
- Italy/AIFA regulatory status verification if a market authorization pathway is to be explored
- Comparative review of the higher-ranked mechanistically plausible predictions (e.g., Rank 10: juvenile-onset Parkinsonism; Rank 6: Lewy body dementia) which share the dopaminergic disease axis and carry stronger mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

