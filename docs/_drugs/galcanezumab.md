---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

The `txgnn-pipeline` skill covers pipeline management and deployment — it doesn't override the report format instructions in the system prompt. I'll proceed directly with generating the evaluation report from the Evidence Pack.

---

# Galcanezumab: From Migraine Prevention to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab (Emgality) is a humanized monoclonal antibody targeting CGRP, approved globally for the preventive treatment of migraine and episodic cluster headache. The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency** — a rare hereditary coagulation disorder — with **0 clinical trials** and **0 publications** currently supporting this direction. All three top predictions cluster around rare coagulation disorders with suspiciously uniform high scores, raising serious concerns that these results reflect a knowledge graph artifact rather than genuine biological repurposing signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention; episodic cluster headache (no Italian authorization on record) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, galcanezumab is an anti-CGRP monoclonal antibody whose proven efficacy in migraine prevention is grounded in blocking CGRP-mediated trigeminal sensitization and cranial vasodilation. It operates entirely within the nervous system's pain-signaling axis — specifically at the CGRP–RAMP1/CLR receptor interface — and has no established role in the coagulation cascade.

Heparin Cofactor II (HCFII) is a serpin-family thrombin inhibitor. HCFII deficiency leads to unopposed thrombin activity and a prothrombotic state. The HCFII–thrombin inhibition axis and the CGRP–receptor signaling system are functionally and biochemically distinct pathways, with no demonstrated crosstalk in the current scientific literature.

Critically, the same implausibility applies to all three top TxGNN predictions — HCFII deficiency, antithrombin deficiency type 2, and factor V excess with spontaneous thrombosis — which are all rare hereditary coagulation disorders with TxGNN scores exceeding 0.994. This tight clustering pattern is a hallmark of systematic supernode overprediction within the knowledge graph's "vascular regulation" cluster, not genuine individual biological signals. These predictions should be treated as graph topology artifacts until a dedicated KG audit confirms or refutes this hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Galcanezumab is not currently approved or marketed in Italy. No marketing authorizations are on record. Note that galcanezumab (Emgality) does hold EMA approval in Europe for migraine prevention — clinicians should refer to the EMA SmPC for the full authorized indication and safety profile.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications are rare hereditary coagulation disorders with zero supporting clinical trials or literature, and the mechanistic link between CGRP inhibition and coagulation factor pathways is biologically unestablished. The clustering of scores >0.994 across three thematically identical indications is a strong indicator of a knowledge graph overprediction artifact rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**

- **KG topology audit**: Investigate whether the TxGNN vascular/coagulation supernode is generating systematic false-positive signals; compare galcanezumab's KG neighborhood against confirmed negative controls
- **MOA data retrieval** (DG002): Pull galcanezumab's full biological interaction profile from DrugBank to formally characterize any cross-pathway activity
- **Mechanistic literature screen**: Conduct a targeted review to determine whether any peer-reviewed evidence supports CGRP–coagulation axis crosstalk before committing further evaluation resources
- **Safety data completion** (DG001): Retrieve the EMA SmPC / TFDA package insert to complete warnings, contraindications, and DDI assessment — currently all safety fields are data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

