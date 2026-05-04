---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# APIXABAN: Drug Repurposing Evaluation Report

## One-Sentence Summary

Apixaban (DrugBank: DB06605) is a well-known direct oral anticoagulant (Factor Xa inhibitor), marketed globally under the brand name Eliquis for stroke prevention in atrial fibrillation and treatment/prevention of venous thromboembolism. The TxGNN model has **not generated any predicted new indications** for this drug at this time. The evidence pack contains multiple critical data gaps that must be resolved before further evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug (INN) | Apixaban |
| DrugBank ID | DB06605 |
| Original Indication | Not recorded in evidence pack (known globally: anticoagulation — stroke prevention in non-valvular AF, DVT/PE treatment and prevention) |
| Predicted New Indication | **None** — TxGNN did not generate predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No prediction, no supporting studies in this pack) |
| Taiwan Market Status | ❌ Not marketed (未上市) |
| Number of TFDA Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is There No Prediction?

The TxGNN model returned an empty `predicted_indications` array for Apixaban. Several factors may explain this:

1. **Data gaps in the input pipeline**: The evidence pack flags two critical gaps — (DG001) TFDA package insert warnings/contraindications are missing, rated as "Blocking" severity; and (DG002) the mechanism of action (MOA) is not populated, rated as "High" severity. Without MOA data feeding into the knowledge graph, the model may lack sufficient connectivity to generate confident predictions.

2. **Taiwan regulatory absence**: Apixaban has zero TFDA licenses recorded (market status: 未上市). This may limit the drug's representation in the Taiwan-specific knowledge graph used by TxGNN, reducing the model's ability to identify repurposing opportunities.

3. **Known pharmacology context**: Apixaban is a selective, reversible direct Factor Xa inhibitor that blocks free and clot-bound Factor Xa, as well as prothrombinase activity. It is widely approved internationally (FDA, EMA) for: (a) reduction of stroke risk in non-valvular atrial fibrillation, (b) treatment of DVT and PE, (c) prophylaxis of DVT following hip or knee replacement surgery. This pharmacological profile is highly specific to the coagulation cascade, which may limit the model's ability to identify cross-indication signals.

---

## Clinical Trial Evidence

Currently no predicted indication exists, so no targeted clinical trial search was performed.

> To generate meaningful clinical trial evidence, TxGNN predictions or manual hypothesis generation is required first.

---

## Literature Evidence

Currently no predicted indication exists, so no targeted literature search was performed.

---

## Taiwan Market Information

Apixaban has **no TFDA-approved licenses** in Taiwan as of the data cutoff (2026-04-03).

> **Note:** Apixaban (Eliquis®, Bristol-Myers Squibb / Pfizer) is widely marketed in many other jurisdictions. The absence of Taiwan licensing may reflect a data collection gap rather than a true regulatory absence. This should be verified against the TFDA database directly.

---

## Safety Considerations

> No safety data is available in this evidence pack. Key warnings, contraindications, and drug-drug interactions all returned as data gaps or "not found."
>
> Please refer to the package insert for safety information.

**Known safety profile (general reference):** Apixaban carries class-wide anticoagulant risks including bleeding (major and minor), and has specific warnings regarding spinal/epidural anesthesia procedures, prosthetic heart valves, and premature discontinuation increasing thrombotic risk. These should be confirmed through the TFDA package insert once available.

---

## Data Gaps Summary

The following critical gaps were identified in this evidence pack:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA package insert warnings/contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Affects mechanism-association analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications were generated for Apixaban, and the evidence pack contains a Blocking-severity data gap (TFDA package insert) that prevents safety preliminary assessment. The drug's Taiwan market status shows zero authorizations, which may indicate an upstream data issue. Without a target indication to evaluate, no repurposing assessment can proceed.

**To proceed, the following is needed:**
- **Resolve DG001 (Blocking):** Obtain and parse TFDA package insert for Apixaban to enable safety preliminary assessment
- **Resolve DG002 (High):** Populate MOA data from DrugBank API (Factor Xa inhibitor) to enable mechanism-based prediction
- **Verify Taiwan market status:** Confirm whether Apixaban truly has no TFDA licenses, as it is widely marketed internationally under the brand Eliquis®
- **Re-run TxGNN prediction:** After resolving data gaps, re-execute the TxGNN model to generate predicted indications
- **If predictions are generated:** Collect clinical trial and literature evidence for the top predicted indication(s)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

