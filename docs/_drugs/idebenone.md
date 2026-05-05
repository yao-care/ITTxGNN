---
layout: default
title: Idebenone
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Idebenone
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

Using the `txgnn-pipeline` skill confirmed this is a standard TxGNN report generation task. Now I'll generate the evaluation report based on the Evidence Pack.

---

# Idebenone: From Leber's Hereditary Optic Neuropathy to Hepatic Porphyria

## One-Sentence Summary

Idebenone is a synthetic coenzyme Q10 analogue with potent antioxidant and mitochondrial-support properties, known in certain markets for its approved use in Leber's Hereditary Optic Neuropathy (LHON). The TxGNN model predicts it may be effective for **Hepatic Porphyria** with a score of **99.92%**. However, this prediction is currently supported by **no clinical trials and no published literature**, placing it at the earliest stage of evidence (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; known approved use for LHON in other markets |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Idebenone is a synthetic analogue of coenzyme Q10 (ubiquinone) that functions as a potent free radical scavenger and supports mitochondrial electron transport chain function. Its established use in LHON — a mitochondrial disease causing retinal ganglion cell death from oxidative damage — demonstrates a proven protective effect in oxidative-stress-driven tissue injury.

Hepatic porphyria is a group of disorders arising from enzyme defects in the heme biosynthesis pathway, causing toxic porphyrin intermediates to accumulate in the liver. Oxidative stress is a recognized secondary pathogenic mechanism in this condition: accumulated porphyrins act as photosensitizers that generate reactive oxygen species (ROS), directly injuring hepatocytes. Idebenone's free radical scavenging capability could theoretically reduce this oxidative burden and limit secondary hepatocellular toxicity — a hypothesis that is biologically plausible but mechanistically indirect, since Idebenone does not address the root enzyme deficiency.

It is important to note that this mechanistic link is weak. Idebenone's potential role in porphyria, if any, would be as an adjunctive antioxidant rather than a disease-modifying agent. The TxGNN high prediction score likely reflects knowledge graph proximity between oxidative-stress-related rare liver diseases, rather than Idebenone-specific pharmacology against porphyria. This prediction is best treated as a research hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Idebenone has no registered product authorizations. No license data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications for Idebenone sit at Evidence Level L5, supported exclusively by TxGNN model scores with zero clinical trials and zero published literature across every queried disease. The top prediction (hepatic porphyria) carries a biologically plausible but mechanistically indirect hypothesis that has not been tested in any preclinical or clinical setting. The drug is not registered in Taiwan, and complete safety profile data (warnings, contraindications, DDI) is currently unavailable — making it impossible to advance even to an initial safety screen.

**To proceed, the following is needed:**

- Retrieve full MOA documentation from DrugBank or peer-reviewed sources
- Obtain package insert data (warnings, contraindications) from a market where Idebenone is approved (e.g., EU/Raxone label for LHON)
- Conduct a targeted preclinical literature search for Idebenone in oxidative-stress-driven liver injury models (e.g., heme/porphyrin-induced hepatotoxicity)
- Consult a rare disease specialist or clinical pharmacologist to assess whether the antioxidant hypothesis merits a formal in vitro study in porphyria cell models
- Re-evaluate the remaining 9 predicted indications to identify whether any disease sub-group (particularly the myopathy cluster: IMNM, antisynthetase syndrome, focal myositis) offers a stronger mechanistic and evidence basis for parallel development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

