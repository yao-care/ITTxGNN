---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 5
---

# Benralizumab
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

The txgnn-pipeline skill confirms this is standard TxGNN report work. Proceeding with the Evidence Pack analysis and report generation.

---

# Benralizumab: From Severe Eosinophilic Asthma to Thrombocytopenia due to Immune Destruction

## One-Sentence Summary

Benralizumab is a humanized anti-IL-5Rα monoclonal antibody approved globally (brand name: Fasenra) for add-on maintenance treatment of severe eosinophilic asthma, though not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Thrombocytopenia due to Immune Destruction (ITP)**, ranking this as the top candidate with a score of 99.34%.
However, **no clinical trials** and **no published literature** currently support this direction — this is a model-only prediction with no empirical corroboration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (global approval; not registered in Taiwan) |
| Predicted New Indication | Thrombocytopenia due to Immune Destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (DrugBank API query pending). Based on known pharmacological information, benralizumab is a humanized anti-IL-5Rα monoclonal antibody that directly targets the IL-5 receptor alpha subunit on eosinophils and basophils. Through enhanced antibody-dependent cell-mediated cytotoxicity (ADCC), it achieves near-complete and rapid depletion of circulating eosinophils. Its clinical efficacy for severe eosinophilic asthma has been established in multiple global Phase 3 trials.

The mechanistic link between the IL-5Rα/eosinophil axis and immune-mediated thrombocytopenia (ITP), however, is extremely weak. ITP is primarily driven by anti-platelet IgG autoantibodies targeting glycoproteins GPIIb/IIIa and GPIb/IX on the platelet surface, leading to accelerated platelet clearance by splenic macrophages. Eosinophils do not play an established role in this process; the disease is fundamentally antibody- and T-cell-mediated, not eosinophil-driven.

The high TxGNN score most likely reflects a **computational bystander effect** in the knowledge graph: eosinophils participate in broader systemic inflammatory networks that share nodes with autoimmune cytopenias, leading the model to assign high similarity scores. This is a statistical inference, not a mechanism-driven hypothesis. Without any preclinical or clinical corroborating evidence, this prediction should be treated as an exploratory signal only — it is not a clinically actionable repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for thrombocytopenia due to immune destruction.

---

## Literature Evidence

Currently no related literature available for thrombocytopenia due to immune destruction.

---

## Taiwan Market Information

Benralizumab has no authorized products registered in Taiwan (0 licenses on record with TFDA). The drug is globally marketed as **Fasenra** (AstraZeneca) for severe eosinophilic asthma but has not obtained Taiwan regulatory approval.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert data was queried but full safety content (warnings, contraindications) could not be parsed in this Evidence Pack version. DrugBank API query is also pending. These are flagged as high-priority data gaps requiring remediation before any clinical evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a high confidence score (99.34%), but this is entirely unsupported by clinical trials or published literature, and the mechanistic rationale linking IL-5Rα blockade to immune-mediated platelet destruction is not biologically established. Proceeding without empirical grounding would carry unacceptable scientific risk.

**To proceed, the following is needed:**
- **Preclinical data**: Animal model studies investigating whether eosinophil depletion affects platelet count or anti-platelet antibody titres in ITP models
- **Literature sweep**: Systematic search for any reported cases of benralizumab use in ITP, hypereosinophilic syndrome with thrombocytopenia, or related autoimmune cytopenias
- **Mechanistic clarification**: Peer-reviewed evidence establishing a role (if any) for IL-5 or eosinophils in platelet immune destruction pathways
- **MOA documentation**: DrugBank API query to complete mechanism of action profiling (currently flagged as high-severity data gap DG002)
- **Safety profiling**: TFDA package insert full-text extraction to enable S1 safety screening (flagged as blocking data gap DG001)
- **Regulatory pathway assessment**: Since benralizumab is not registered in Taiwan, a full regulatory feasibility review would be required before any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

