---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# AMIODARONE: Drug Repurposing Evaluation Report

## One-Sentence Summary

Amiodarone is a well-known Class III antiarrhythmic agent widely used internationally for the management of ventricular and supraventricular arrhythmias. The TxGNN model has **not generated any predicted new indications** for this drug at this time. The evidence pack contains significant data gaps that must be resolved before further evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Amiodarone |
| DrugBank ID | [DB01118](https://go.drugbank.com/drugs/DB01118) |
| Original Indication | Not available in evidence pack (known internationally: cardiac arrhythmias) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction, no supporting studies) |
| Taiwan (TFDA) Market Status | ❌ Not marketed (未上市) |
| Number of TFDA Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is There No Prediction?

Amiodarone (DrugBank: DB01118) was queried through the TxGNN pipeline, but the model returned **no predicted new indications**. This may be due to one or more of the following reasons:

1. **Insufficient input features** — The evidence pack is missing critical data including the mechanism of action (MOA), TFDA package insert warnings, and contraindication profiles. Without these, the model's knowledge graph linkage may be incomplete.
2. **No TFDA market presence** — Amiodarone has zero TFDA authorizations in Taiwan, meaning there is no local regulatory anchor from which to derive indication text or safety metadata for the repurposing pipeline.

Internationally, Amiodarone is recognized as a potent Class III antiarrhythmic agent that works primarily by blocking potassium channels, prolonging the cardiac action potential and refractory period. It also exhibits Class I (sodium channel blocking), Class II (beta-adrenergic blocking), and Class IV (calcium channel blocking) properties, making it one of the most pharmacologically complex antiarrhythmics available. Its known indications include life-threatening ventricular arrhythmias (ventricular fibrillation, hemodynamically unstable ventricular tachycardia) and atrial fibrillation/flutter refractory to other treatments.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted clinical trial search was performed for a repurposed indication.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature search was performed for a repurposed indication.

---

## Taiwan (TFDA) Market Information

Amiodarone currently has **no TFDA authorizations** in Taiwan. The TFDA query (2026-03-29) returned zero results. This drug is classified as **未上市 (not marketed)** in the Taiwan regulatory system.

---

## Safety Considerations

> Safety data (warnings, contraindications, and drug-drug interactions) could not be retrieved from the evidence pack sources. Please refer to the international package insert (e.g., FDA-approved labelling for Cordarone®/Pacerone®) for comprehensive safety information.
>
> **Known critical safety concerns (from international labelling):**
> - **Black Box Warning (FDA):** Pulmonary toxicity (potentially fatal), hepatotoxicity, and proarrhythmic effects. Should only be used for life-threatening arrhythmias due to substantial toxicity.
> - **Thyroid dysfunction:** Amiodarone contains ~37% iodine by weight; both hypo- and hyperthyroidism are common.
> - **QT prolongation and Torsades de Pointes risk.**
> - **Corneal microdeposits** occur in nearly all patients.
> - **Extensive drug-drug interactions** due to CYP3A4 and CYP2C8 inhibition (e.g., with warfarin, digoxin, simvastatin, and other QT-prolonging agents).
>
> ⚠️ *These safety notes are based on general pharmacological knowledge and are not sourced from the evidence pack. They are provided for reference only.*

---

## Data Gaps Requiring Resolution

The evidence pack flagged the following critical gaps:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanism-association analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has not produced any predicted new indications for Amiodarone. Additionally, there are **blocking-level data gaps** (missing TFDA safety data and MOA) that prevent the candidate from entering even the preliminary safety evaluation stage (S1). Without a predicted indication to evaluate, there is no actionable repurposing hypothesis at this time.

**To proceed, the following is needed:**
- **[Blocking]** Obtain TFDA package insert data (warnings, contraindications) — or, if no TFDA approval exists, source equivalent data from FDA/EMA labelling
- **[High]** Populate mechanism of action (MOA) from DrugBank API to enable knowledge graph linkage
- **[High]** Investigate why TxGNN produced no predictions — verify that the drug node is properly connected in the knowledge graph and that input features are complete
- **[Medium]** If Amiodarone is not marketed in Taiwan, consider whether the repurposing pipeline should evaluate it under an alternative regulatory framework (e.g., cross-referencing with FDA/EMA indications)
- **[Optional]** Re-run TxGNN prediction after resolving data gaps to determine if new indications emerge

---

*This report was generated on 2026-04-03 based on Evidence Pack v4 (data cutoff: 2026-04-03). Results are for research reference only and do not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

