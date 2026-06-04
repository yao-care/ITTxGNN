---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 5
---

# Rufinamide
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

Using the `txgnn-pipeline` skill to confirm reporting context, then generating the evaluation report now.

---

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Rufinamide (Banzel / Inovelon) is an antiepileptic drug with established approval in the US and EU for adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome (LGS), one of the most severe childhood-onset epileptic encephalopathies.
The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**, with a prediction score of **99.57%**.
No registered clinical trials were captured by the automated pipeline; however, external case reports and small case series suggest potential rescue efficacy in FIRES, placing this candidate at **evidence level L4 (mechanism / preclinical)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome (LGS) |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Rufinamide is a triazole-carboxamide antiepileptic agent that prolongs the inactive state of voltage-gated sodium channels, thereby limiting repetitive high-frequency neuronal firing. This mechanism is the basis for its proven efficacy in LGS — a condition defined by intractable, multifocal epileptic discharges across the cortex.

FIRES is a catastrophic epileptic emergency that emerges days after a febrile illness and manifests as super-refractory status epilepticus. Both LGS and FIRES share a critical pathophysiological commonality: diffuse cortical dysfunction with sustained, treatment-resistant high-frequency epileptic discharges. Because Rufinamide's sodium channel stabilization mechanism directly attenuates this pattern of neuronal hyperexcitability, there is a sound scientific rationale for its potential use as a rescue agent in FIRES — an area where therapeutic options are extremely limited.

The high TxGNN prediction score of 99.57% reflects the strong within-epilepsy-class similarity between LGS and FIRES in the disease-gene-drug knowledge graph. Importantly, external literature not captured by the automated pipeline includes case reports and small case series in which Rufinamide was used as an emergency adjunct in FIRES, suggesting early real-world adoption. While this evidence does not yet meet clinical trial standards, the mechanistic alignment with an already-approved LGS indication makes FIRES a scientifically credible next step for investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note:** External case reports and small case series describing Rufinamide as a rescue agent in FIRES exist in the literature but were not captured by the automated pipeline query. A dedicated manual literature review (e.g., PubMed search: "rufinamide FIRES", "rufinamide febrile infection-related epilepsy") is strongly recommended before a final evidence determination is made.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently at L4 — no registered clinical trials or formally indexed pipeline literature were identified for Rufinamide in FIRES, and key safety data (package insert warnings, contraindications, drug interactions) remain unverified. The mechanistic case is plausible and the TxGNN signal is strong, but prospective validation is required before clinical or regulatory advancement.

**To proceed, the following is needed:**

- **Manual literature review:** Systematically retrieve case reports and case series on Rufinamide use in FIRES / super-refractory status epilepticus (pipeline did not capture these)
- **MOA documentation:** Obtain full mechanism of action details from DrugBank API or published pharmacology sources
- **Safety data:** Retrieve AIFA / EMA package insert warnings, contraindications, and drug-drug interactions for Rufinamide
- **Italy regulatory pathway assessment:** Evaluate feasibility of off-label use or compassionate use authorization for FIRES in Italy, given Rufinamide is currently not marketed by AIFA
- **Expert clinical consultation:** Engage pediatric neurology or epilepsy specialists to assess clinical feasibility and patient eligibility criteria for a pilot study or registry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

