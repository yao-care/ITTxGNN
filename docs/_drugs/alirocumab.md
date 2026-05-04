---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# ALIROCUMAB: Drug Repurposing Evaluation — Awaiting Predicted Indications

## One-Sentence Summary

Alirocumab (Praluent®) is a fully human monoclonal antibody targeting PCSK9, originally developed for the treatment of hypercholesterolemia and reduction of cardiovascular risk. The TxGNN model has **not yet generated predicted new indications** for this drug, and the evidence pack currently contains **no clinical trials** and **no literature** to evaluate. Further data collection is required before a repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in current evidence pack (known: hypercholesterolemia, cardiovascular risk reduction) |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions or supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not generated any predicted new indications for Alirocumab, so a mechanistic plausibility assessment cannot be performed at this time.

For reference, Alirocumab is a PCSK9 (proprotein convertase subtilisin/kexin type 9) inhibitor. PCSK9 normally binds to LDL receptors on the surface of hepatocytes, promoting their degradation and thereby reducing the liver's ability to clear LDL cholesterol from the blood. By blocking PCSK9, Alirocumab increases the number of available LDL receptors, significantly lowering LDL-C levels. This mechanism has been validated in the landmark ODYSSEY OUTCOMES trial demonstrating cardiovascular event reduction.

The PCSK9 pathway has been implicated in areas beyond lipid metabolism — including inflammation, sepsis, hepatic regeneration, and viral infection — suggesting potential repurposing avenues. However, until TxGNN predictions are generated, no formal mechanistic bridging analysis can be conducted.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no indication-specific clinical trial search has been performed.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no indication-specific literature search has been performed.

---

## Taiwan Market Information

Alirocumab is **not currently marketed in Taiwan**. No TFDA marketing authorizations were found (query date: 2026-03-29).

> Note: Alirocumab is approved in the US (FDA), EU (EMA), and many other markets under the brand name **Praluent®** (Sanofi / Regeneron) for primary hypercholesterolemia, mixed dyslipidemia, and established atherosclerotic cardiovascular disease to reduce cardiovascular risk.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug-drug interactions) is available in the current evidence pack.

> Please refer to the package insert for safety information. Key known safety considerations for Alirocumab from the approved label include:
> - **Hypersensitivity reactions** (including pruritus, rash, urticaria; rare cases of hypersensitivity vasculitis)
> - **Injection site reactions** (most common adverse event)
> - **Neurocognitive events** (monitored in clinical trials; no confirmed causal relationship)
> - **Hepatic impairment** (no dose adjustment needed for mild-to-moderate; limited data in severe)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for Alirocumab is critically incomplete — no TxGNN predicted indications have been generated, no Taiwan marketing authorizations exist, and safety/MOA data remain unfilled. Without a predicted new indication, no repurposing evaluation pathway can be initiated.

**To proceed, the following is needed:**

1. **TxGNN Prediction Run** — Execute the TxGNN model for Alirocumab (DB09302) to generate candidate repurposing indications with prediction scores
2. **Mechanism of Action (MOA) Data** — Query DrugBank API to retrieve full MOA, target, and pathway data (Data Gap DG002)
3. **TFDA Package Insert** — Obtain and parse the official package insert for warnings and contraindications (Data Gap DG001), or if not marketed in Taiwan, source from FDA/EMA approved labels
4. **Drug-Drug Interaction Data** — Re-query DDI databases; Alirocumab as a monoclonal antibody has limited CYP-mediated interactions, but statin co-administration patterns should be documented
5. **Taiwan Market Access Assessment** — If repurposing candidates are identified, evaluate pathway for TFDA registration or compassionate use

---

*This report was generated on 2026-04-03 based on Evidence Pack v4 (candidate ID: TW-DB09302-multi). Results are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

