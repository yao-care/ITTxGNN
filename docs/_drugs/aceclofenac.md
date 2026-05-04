---
layout: default
title: Aceclofenac
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# ACECLOFENAC: Drug Repurposing Evaluation — Preliminary Assessment

## One-Sentence Summary

Aceclofenac is a non-steroidal anti-inflammatory drug (NSAID) of the phenylacetic acid class, widely used internationally for pain and inflammation management in musculoskeletal conditions.
The TxGNN model has **not yet generated predicted new indications** for this compound,
and **no clinical trial or literature evidence** has been collected at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Aceclofenac |
| DrugBank ID | [DB06736](https://go.drugbank.com/drugs/DB06736) |
| Original Indication | Not available in current evidence pack (known NSAID for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | **L5** — Model prediction pending; no supporting studies collected |
| Taiwan Market Status | ✗ Not marketed |
| Number of TFDA Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Drug Being Evaluated?

Aceclofenac (CAS 89796-99-6) is a second-generation NSAID and a prodrug of diclofenac. It preferentially inhibits cyclooxygenase-2 (COX-2), reducing prostaglandin synthesis and thereby exerting anti-inflammatory, analgesic, and antipyretic effects. It is marketed in numerous countries across Europe, Asia, and Latin America for the management of pain and inflammation associated with osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis.

Currently, detailed mechanism of action data was not returned from the evidence pack sources. Based on established pharmacological knowledge, aceclofenac's COX-2-preferential inhibition profile and its metabolic conversion to diclofenac provide a well-characterized mechanism. This NSAID mechanism could theoretically be relevant to inflammatory-driven conditions beyond musculoskeletal disease, but **no TxGNN predictions have been generated at this time** to guide exploration of specific new indications.

---

## Clinical Trial Evidence

Currently no predicted indication has been generated, and therefore no related clinical trials have been collected.

---

## Literature Evidence

Currently no predicted indication has been generated, and therefore no related literature has been collected.

---

## Taiwan (TFDA) Market Information

Aceclofenac currently holds **no valid TFDA marketing authorizations** in Taiwan. The drug is classified as **not marketed** in the Taiwanese market.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available from the queried sources for the Taiwan market.
>
> **General NSAID class warnings** (based on established pharmacology) include:
> - Cardiovascular thrombotic risk with prolonged use
> - Gastrointestinal bleeding, ulceration, and perforation risk
> - Renal function impairment, especially in patients with pre-existing renal disease
> - Contraindicated in patients with known hypersensitivity to aceclofenac, aspirin, or other NSAIDs
> - Caution in patients with asthma, hepatic impairment, or coagulation disorders
>
> *These are general class-level considerations and do not replace product-specific labelling.*

---

## Data Gaps Identified

The following critical data gaps were flagged during evidence collection:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API for full MOA data |

Additionally:
- **No TxGNN predictions** have been generated for this drug — the `predicted_indications` array is empty
- **No DDI data** was found in the queried sources
- **No TFDA licenses** exist, meaning Taiwan-specific prescribing information is unavailable

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Aceclofenac cannot proceed through the drug repurposing evaluation pipeline at this time. The TxGNN model has not generated any predicted new indications, and multiple blocking data gaps remain unresolved — most critically, the absence of TFDA safety labelling data (DG001) which prevents entry into the S1 safety screening stage.

**To proceed, the following is needed:**
1. **Run TxGNN prediction** for Aceclofenac (DB06736) to generate candidate new indications with confidence scores
2. **Resolve DG001** — Obtain TFDA package insert warnings and contraindications (or confirm no Taiwan-marketed product exists, and source equivalent data from EMA/MHRA/TGA)
3. **Resolve DG002** — Retrieve full MOA data from DrugBank API to enable mechanistic relevance analysis
4. **Collect clinical trial and literature evidence** once a predicted indication is available
5. **Reassess Taiwan regulatory pathway** — Since Aceclofenac is not marketed in Taiwan, any repurposing effort would require either a new drug application or a special import pathway

---

*This report was generated on 2026-04-03 based on Evidence Pack v4 (candidate ID: TW-DB06736-multi). Results are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

