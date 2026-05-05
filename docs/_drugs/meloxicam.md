---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

The `txgnn-pipeline` skill covers model training and deployment pipelines — this task is a report-writing task governed by the system prompt's v5 reporting template. I'll now generate the report directly from the Evidence Pack.

---

# Meloxicam: From Arthritis & Pain Management to Acromesomelic Dysplasia (Hunter-Thompson Type)

## One-Sentence Summary

Meloxicam is a COX-2 preferential NSAID widely established for treating inflammatory musculoskeletal conditions such as osteoarthritis and rheumatoid arthritis.
The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal dysplasia caused by GDF5/BMPR1B pathway mutations.
Currently **0 clinical trials** and **0 publications** support this specific repurposing direction, placing evidence firmly at Level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no AIFA authorization on file in dataset) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed (per dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the dataset. Based on well-established pharmacological knowledge, Meloxicam is a preferential COX-2 inhibitor belonging to the oxicam class of NSAIDs. It reduces inflammation and pain primarily by blocking cyclooxygenase-2, thereby suppressing the synthesis of prostaglandin E2 (PGE2) at sites of inflammation and in the central nervous system. Its efficacy in chronic inflammatory arthropathies is supported by decades of clinical use globally.

Acromesomelic Dysplasia, Hunter-Thompson Type (AMDH) is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in GDF5 or BMPR1B, genes that govern bone and cartilage morphogenesis during embryonic limb development. The proposed mechanistic bridge is extremely tenuous: COX-2/PGE2 is known to modulate downstream BMP signaling in certain cartilage differentiation models, meaning that COX-2 inhibition could theoretically affect chondrogenic pathways. However, this connection is entirely indirect and has not been experimentally validated in any AMDH model, animal study, or human tissue study.

The most likely explanation for TxGNN's high score is **knowledge graph topology**: Meloxicam is densely connected to musculoskeletal and inflammatory disease nodes, and AMDH clusters near other skeletal diseases in the graph. GNN models are known to propagate high scores across topologically adjacent disease nodes regardless of biological plausibility. This prediction should be treated as a graph artifact rather than a pharmacological signal. Notably, among all ten predictions, the more clinically coherent targets — **Spondyloarthropathy (rank 6)**, **Rheumatoid Nodulosis (rank 7)**, and **RF-positive Polyarticular JIA (rank 8)** — score lower precisely because they appear further from the drug's graph neighborhood, even though they are far better mechanistic fits.

> ⚠️ **Critical Data Quality Alert — Rank 6 (Spondyloarthropathy):** NSAIDs including Meloxicam are **first-line therapy per EULAR and ACR clinical guidelines** for spondyloarthropathy, yet this dataset retrieved zero clinical trials and zero literature for this indication. This is a data collection gap, not a genuine absence of evidence. The strongest real-world repurposing signal for Meloxicam in this dataset is being systematically suppressed by incomplete evidence retrieval.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acromesomelic Dysplasia (Hunter-Thompson Type) and Meloxicam.

---

## Literature Evidence

Currently no related literature available for Acromesomelic Dysplasia (Hunter-Thompson Type) and Meloxicam.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN top prediction (Acromesomelic Dysplasia, Hunter-Thompson Type) is a rare, genetically determined skeletal dysplasia. There are no clinical trials, no publications, and the proposed mechanistic link through COX-2/BMP pathway cross-talk is highly speculative and entirely unvalidated. This does not constitute an actionable repurposing candidate.

**To proceed, the following is needed:**

- **Resolve evidence retrieval gap for Spondyloarthropathy (rank 6):** Re-run literature and clinical trial search with broader query terms (e.g., "ankylosing spondylitis", "axial SpA", "NSAID spondyloarthritis") — real-world evidence is substantial and should be captured before any final decision
- **Resolve AIFA data gap for Italy:** Meloxicam is a globally marketed reference NSAID; the absence of any Italy authorization record likely reflects a data collection issue and should be verified directly against the AIFA public registry
- **Obtain MOA data from DrugBank (DG002):** Formal MOA documentation is needed for the mechanistic link analysis section
- **Formally re-evaluate ranks 6–8** (Spondyloarthropathy, Rheumatoid Nodulosis, RF+ Polyarticular JIA) as the pharmacologically prioritized targets — these are mechanistically aligned with Meloxicam's COX-2 inhibition and deserve a dedicated evidence deep-dive before the Hold decision is considered final
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

