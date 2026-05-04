---
layout: default
title: Balsalazide
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Balsalazide
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

# Balsalazide: From Ulcerative Colitis to Gout

## One-Sentence Summary

Balsalazide is a prodrug of 5-aminosalicylic acid (5-ASA), designed to deliver the active anti-inflammatory agent directly to the colonic mucosa for the treatment of **ulcerative colitis**.
The TxGNN model predicts it may be effective for **Gout**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Evidence is limited exclusively to model prediction, representing the lowest confidence tier (Level 5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ulcerative Colitis |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 — Model prediction only; no supporting clinical or preclinical studies |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from our data sources. Based on established pharmacology, Balsalazide is a colon-targeted prodrug: after oral administration, intestinal bacteria cleave the azo bond to release 5-ASA at high local concentrations in the distal colon. 5-ASA exerts its anti-inflammatory effects primarily through inhibition of NF-κB, suppression of prostaglandin synthesis, and scavenging of reactive oxygen species — all acting locally within the colonic mucosa to control ulcerative colitis.

Gout, however, is driven by a fundamentally distinct mechanism. Monosodium urate crystal deposition in joint spaces triggers NLRP3 inflammasome activation, leading to caspase-1-mediated cleavage and release of IL-1β — a cytokine cascade that orchestrates acute gouty arthritis. While 5-ASA carries broad anti-inflammatory properties, there is no published evidence that it directly suppresses NLRP3 assembly or IL-1β maturation, which are the core drivers of gout pathology.

A critical pharmacokinetic barrier further undermines this prediction. Balsalazide is intentionally engineered for minimal systemic absorption: plasma 5-ASA concentrations are very low following oral dosing, which is clinically desirable for IBD but means that therapeutically meaningful drug levels are unlikely to be achieved in peripheral joint cavities. The combination of a mechanistic mismatch and inadequate systemic bioavailability makes this repurposing direction biologically implausible under the current formulation. This prediction most likely reflects structural noise in the knowledge graph underlying the TxGNN model.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Balsalazide is **not currently marketed in Italy**. No product authorizations have been identified in the regulatory database. Any future repurposing program targeting the Italian market would require a full marketing authorization application from the beginning.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert data (warnings, contraindications) for this drug could not be retrieved during the current evidence collection cycle and is flagged as a blocking data gap (DG001). This information is required before any clinical-stage evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.75%), but this numerical confidence is not supported by any clinical trials, published literature, or mechanistic evidence. The colon-targeted pharmacokinetics of Balsalazide and the NLRP3/IL-1β-centred pathology of gout represent a fundamental mismatch that cannot be bridged without significant formulation re-engineering. Additionally, the drug is not currently authorised in Italy, meaning the regulatory pathway would also need to start from scratch.

**To proceed, the following is needed:**

- **MOA verification:** Retrieve full DrugBank mechanistic data (DG002) to confirm or refute any 5-ASA activity on NLRP3, IL-1β, or uric acid transport pathways
- **Safety dossier:** Download and parse the official package insert (DG001 — currently blocking) to establish contraindications and key warnings
- **Bridging literature search:** Conduct a targeted PubMed search for mesalazine/5-ASA + gout or hyperuricemia to identify any indirect supporting evidence
- **PK modelling:** Assess whether modified-release or systemic 5-ASA formulations could achieve therapeutic joint concentrations, as a prerequisite for any further hypothesis generation
- **Consider alternative predictions:** Ranks 3 (Ankylosing Spondylitis), 4 (Rheumatoid Arthritis), 7 (Inflammatory Spondylopathy), and 10 (Anus Disease) offer stronger mechanistic rationales via the NF-κB/sulfasalazine analogy or colonic-distribution overlap, and may be more productive avenues for next-stage evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

