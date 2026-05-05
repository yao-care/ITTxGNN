---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

The `txgnn-pipeline` skill is noted. This is a report generation task using the Drug Repurposing Evaluation Report Prompt v5. Proceeding to generate the report from the Evidence Pack.

---

# Etoricoxib: From Musculoskeletal Pain to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a highly selective COX-2 inhibitor (NSAID), approved in many markets for inflammatory conditions including osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, and acute gout. The TxGNN model predicts it may be effective for **Migraine Disorder** with a near-perfect prediction score; however, there are currently **0 clinical trials** and **0 publications** directly supporting this specific indication, placing evidence at the lowest level (L5). Closely related indications — headache disorder and trigeminal autonomic cephalalgia — do have preliminary case-series evidence that provides indirect biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Italy authorization records available; etoricoxib is a selective COX-2 inhibitor used for inflammatory joint pain |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this dataset. Based on known pharmacological information, etoricoxib is a highly selective inhibitor of cyclooxygenase-2 (COX-2), the inducible isoform responsible for prostaglandin synthesis during inflammation and pain. Its efficacy in musculoskeletal inflammatory conditions is well established, and mechanistically it may be applicable to migraine disorder through a shared inflammatory pathway.

The biological link to migraine rests on the trigeminovascular hypothesis: COX-2 inhibition reduces the synthesis of prostaglandin E₂ (PGE₂), a key mediator of neurogenic inflammation in the trigeminovascular system. By dampening PGE₂-driven sensitisation of trigeminal nerve endings in the dura mater, a selective COX-2 inhibitor such as etoricoxib theoretically could abort or prevent migraine attacks. This is consistent with the established mechanism of indomethacin — a non-selective COX inhibitor that is a recognised treatment for several indomethacin-responsive headache subtypes — and case reports show etoricoxib can substitute for indomethacin in those syndromes (see evidence for the related rank-9 indication, headache disorder).

However, a critical distinction must be noted: migraine involves not only prostaglandin-mediated inflammation but also CGRP signalling, cortical spreading depression, and central sensitisation — pathways not directly targeted by COX-2 inhibition. The TxGNN model likely predicts this link via graph-network proximity between etoricoxib's target profile and migraine's disease node, informed in part by the broader epilepsy–migraine shared genetic susceptibility literature captured under rank-3 (susceptibility to migraine with or without aura). This genetic network proximity is mechanistically distant from a direct therapeutic effect, which explains why no direct clinical evidence exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for etoricoxib in migraine disorder.

---

## Literature Evidence

Currently no related literature available for etoricoxib in migraine disorder.

---

## Italy Market Information

Etoricoxib currently has no marketing authorizations registered in Italy in this dataset (0 authorizations, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Note from Evidence Pack:** One adverse event case report (PMID [21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/)) documented life-threatening hyperkalemia and acute kidney dysfunction with etoricoxib in a patient on telmisartan and a low-sodium diet. A separate case report (PMID [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/)) described reversible cerebral vasoconstriction syndrome (RCVS) possibly induced by etoricoxib — particularly relevant given that migraine patients may have overlapping RCVS risk. These signals, while arising from the headache disorder evidence query rather than the migraine query directly, are clinically important for any neurological use of etoricoxib.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect score to migraine disorder, but the evidence base is entirely absent — no clinical trials and no publications directly address etoricoxib for this indication. The prediction is biologically plausible at a theoretical level (COX-2/PGE₂/trigeminovascular pathway), but biological plausibility alone is insufficient to advance a repurposing candidate. The closely related indication of **headache disorder (rank 9)** carries a stronger research case, supported by multiple published case series showing etoricoxib as an effective alternative to indomethacin in indomethacin-responsive headache syndromes, and should be considered as the more actionable near-term research target.

**To proceed, the following is needed:**

- **MOA data from DrugBank:** Retrieve full pharmacology, drug targets, and toxicity profile for etoricoxib (DB01628) to complete mechanism-of-action analysis and refine the migraine pathway rationale.
- **TFDA/EMA package insert:** Obtain full text of contraindications and key warnings (currently blocking safety pre-screen at stage S0) to assess whether neurological/vascular use is formally contraindicated.
- **Focused literature search:** Conduct a dedicated PubMed search specifically combining "etoricoxib" AND "migraine" (rather than the broader susceptibility disease term used in this dataset) to confirm whether any direct evidence exists that was missed by the current query strategy.
- **Reclassify primary candidate:** Consider elevating **headache disorder** (rank 9, Evidence Level L4, stage S1) as the primary repurposing candidate for near-term investigation, given it has direct published case evidence of etoricoxib efficacy and a clear mechanistic link via the indomethacin-COX-2 pathway.
- **RCVS risk assessment:** Before any neurological indication is pursued, a formal benefit-risk assessment for RCVS (etoricoxib-induced vasoconstriction) in migraine patients — who already have elevated cerebrovascular sensitivity — is required.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

