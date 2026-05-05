---
layout: default
title: Nabumetone
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

Using the `txgnn-pipeline` skill as context. Now generating the evaluation report based on the Evidence Pack.

---

# Nabumetone: From Osteoarthritis / Rheumatoid Arthritis to Acromesomelic Dysplasia (Hunter-Thompson Type)

## One-Sentence Summary

Nabumetone is a non-selective COX inhibitor (NSAID) classically used to relieve pain and inflammation in osteoarthritis and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare hereditary skeletal disorder caused by GDF5/CDMP1 mutations.
However, this prediction is supported by **0 clinical trials** and **0 publications**, placing it at the lowest evidence level (L5), meaning it rests entirely on graph model inference with no human study data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis / Rheumatoid Arthritis (known NSAID class use; no Italy authorization on record) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Nabumetone from the data sources queried. Based on known pharmacological information, Nabumetone is a prodrug NSAID that is converted in vivo to its active metabolite 6-methoxy-2-naphthylacetic acid (6-MNA), which non-selectively inhibits both COX-1 and COX-2 enzymes. This reduces prostaglandin synthesis, thereby suppressing pain and inflammation in musculoskeletal conditions such as osteoarthritis and rheumatoid arthritis.

Acromesomelic dysplasia, Hunter-Thompson type (AMDH) is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in *GDF5* (also known as *CDMP1*), which encodes a bone morphogenetic protein (BMP) ligand critical for limb patterning and joint formation. The pathology involves disruption of the BMP/GDF5 developmental signalling pathway, resulting in disproportionate shortening of the middle and distal limb segments — a structural, non-inflammatory skeletal anomaly established prenatally.

There is no recognized mechanistic bridge between COX inhibition and the GDF5/BMP pathway disruption that underlies AMDH. Nabumetone can provide symptomatic pain relief in patients with secondary musculoskeletal complaints, but it has no capacity to modify the underlying genetic or developmental defect. The TxGNN model likely generated this prediction due to graph proximity between skeletal dysplasia nodes and inflammatory arthropathy nodes in the disease knowledge graph — a known source of false positives for NSAIDs in rare bone disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Nabumetone currently holds no marketing authorizations in Italy (AIFA). The drug is not marketed, and no license records were retrieved.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, mechanistic, or literature evidence supporting Nabumetone as a treatment for Acromesomelic Dysplasia, Hunter-Thompson Type. The disease is driven by a hereditary BMP/GDF5 pathway defect that is structurally and biologically incompatible with COX inhibition. The TxGNN score alone, without any corroborating evidence, is insufficient to justify further development.

**To revisit this prediction, the following would be needed:**
- A credible mechanistic hypothesis linking COX/prostaglandin pathways to GDF5 signalling (e.g., prostaglandin-modulated BMP receptor activity studies)
- At least one preclinical study (animal model or in vitro) demonstrating Nabumetone or a structurally related NSAID affecting GDF5-related phenotypes
- Review of whether the TxGNN graph edges connecting this drug-disease pair reflect genuine biological relationships or are artefacts of shared neighbourhood nodes (e.g., spondyloarthropathy or brachyolmia proximity)

> **Note on higher-ranked candidates:** Rank 8 — *Spondyloarthropathy* (susceptibility) — presents a more biologically plausible repurposing target. NSAIDs including Nabumetone are first-line agents for ankylosing spondylitis and SpA as a drug class (L1 class-effect evidence), though Nabumetone-specific RCT data is absent (L4). If a repurposing programme is pursued, that indication warrants prioritisation over the top-ranked rare skeletal dysplasias.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

