---
layout: default
title: Almotriptan
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 3
---

# Almotriptan
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

# ALMOTRIPTAN: Drug Repurposing Evaluation Report

## One-Sentence Summary

Almotriptan is a selective 5-HT₁B/₁D receptor agonist, widely known for the acute treatment of migraine headaches. The TxGNN model currently has **no predicted new indications** for this drug, and the evidence pack contains significant data gaps in mechanism of action, safety, and regulatory information. Further data collection is required before any repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Almotriptan |
| DrugBank ID | [DB00918](https://go.drugbank.com/drugs/DB00918) |
| Original Indication | Acute migraine treatment (per general pharmacological knowledge; not populated in evidence pack) |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — Model prediction only; no predicted indications or supporting studies |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of TFDA Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not generated any predicted new indications for Almotriptan, so there is no repurposing hypothesis to evaluate at this time.

From general pharmacological knowledge, Almotriptan is a second-generation triptan — a selective serotonin 5-HT₁B/₁D receptor agonist. It works by constricting dilated intracranial blood vessels and inhibiting the release of pro-inflammatory neuropeptides, thereby aborting acute migraine attacks. Its high selectivity for 5-HT₁B/₁D receptors (with minimal activity at other serotonin receptor subtypes) gives it a favorable tolerability profile among the triptans.

> ⚠️ **Data Gap:** The evidence pack's `original_moa` field is not populated. The mechanism described above is based on established pharmacological literature. A formal DrugBank API query is recommended to fill this gap (see remediation plan DG002).

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indications exist for Almotriptan, so no targeted clinical trial search was performed for repurposing candidates.

---

## Literature Evidence

Currently no TxGNN-predicted indications exist for Almotriptan, so no targeted literature search was performed for repurposing candidates.

---

## Taiwan Market Information

Almotriptan is **not marketed in Taiwan**. No TFDA drug licenses were found (query date: 2026-03-29). There are no authorized products, dosage forms, or approved indications registered with the TFDA.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> ⚠️ **Data Gap (Blocking):** TFDA package insert warnings and contraindications could not be retrieved (DG001). This is classified as a **Blocking** gap — the candidate cannot enter Stage 1 safety screening until this is resolved.
>
> No drug-drug interaction (DDI) data was found in the queried databases.

---

## Data Gaps Summary

The following critical data gaps were identified and must be addressed before any repurposing evaluation can proceed:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | **High** | Affects mechanism-indication relationship analysis | Query DrugBank API |
| — | TxGNN Predicted Indications | **High** | No repurposing candidates to evaluate | Run/re-run TxGNN prediction pipeline for DB00918 |
| — | Original Indications (structured) | Medium | Quick Overview table incomplete | Populate from DrugBank or TFDA data |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Almotriptan currently has no TxGNN-predicted new indications, is not marketed in Taiwan, and has multiple blocking data gaps. There is insufficient information to evaluate any repurposing hypothesis at this time.

**To proceed, the following is needed:**
1. **Run/re-run the TxGNN prediction pipeline** for Almotriptan (DB00918) to generate candidate indications
2. **Resolve DG001 (Blocking):** Obtain TFDA package insert warnings and contraindications — required before Stage 1 safety screening
3. **Resolve DG002 (High):** Query DrugBank API for detailed mechanism of action data to enable mechanism–indication relationship analysis
4. **Populate original indication data** from DrugBank or authoritative pharmacological references
5. **Reassess Taiwan regulatory pathway** — since Almotriptan is not marketed in Taiwan, any repurposing effort would need to account for initial market authorization requirements

---

*Report generated: 2026-04-03 | Evidence Pack version: v4 | Candidate ID: TW-DB00918-multi*

*⚠️ This report is for research reference only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

