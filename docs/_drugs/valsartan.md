---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

---

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker (ARB) established for the treatment of hypertension and heart failure by selectively blocking the AT1 receptor.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with a prediction score of **99.97%**.
Current evidence supporting this direction is limited to **1 preclinical mechanistic study** and **no registered clinical trials** specific to this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Heart Failure (ARB class; no Taiwan TFDA registration data captured in this dataset) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data source. Based on established pharmacological knowledge, Valsartan belongs to the angiotensin II receptor blocker (ARB) class. It selectively blocks the AT1 receptor subtype, preventing angiotensin II (Ang II) from exerting its vasoconstrictive, pro-fibrotic, and pro-inflammatory effects. In the kidney, this translates to reduced intraglomerular pressure, decreased proteinuria, and suppression of TGF-β–mediated renal fibrosis — the same pathways driving end-organ damage in hypertensive emergencies.

Malignant hypertensive renal disease (malignant nephrosclerosis) develops when severely elevated blood pressure causes acute nephrotoxic injury, characterised by fibrinoid necrosis of arterioles, thrombotic microangiopathy, and rapid deterioration of renal function. The central pathological driver is overactivation of Ang II via the renin-angiotensin-aldosterone system (RAAS), leading to sustained AT1R stimulation and a self-amplifying cycle of vasoconstriction and glomerular injury. Valsartan directly blocks this receptor, making the mechanistic rationale essentially first-principles: interrupt Ang II signalling at the primary effector point.

The TxGNN model's high prediction score (99.97%) is therefore mechanistically coherent. The principal uncertainty is not biological plausibility but the complete absence of dedicated clinical trial evidence specific to this severe disease subtype. Indirect preclinical support exists from animal models of RAAS-hyperactivated hypertensive nephropathy, though using a different drug mechanism (endothelin antagonism). Formal clinical investigation of ARBs — including valsartan — in malignant hypertensive nephropathy remains an open and clinically relevant research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Animal/Mechanistic | Pharmacological Research | Avosentan (endothelin-A antagonist) provided nephroprotection in double-transgenic rats overexpressing human renin and angiotensinogen — a model of severe RAAS-driven hypertensive nephropathy — at doses below those causing fluid retention; confirms pharmacological modulation of the renin-angiotensin axis can arrest hypertensive renal injury in vivo |

> **Important caveat:** The above study evaluates avosentan (an endothelin antagonist), not valsartan. Its relevance is mechanistic — it validates RAAS-hyperactivation as the primary pathological driver of malignant hypertensive nephropathy and demonstrates organ protection is achievable through targeted pathway blockade. No direct clinical or experimental evidence for valsartan in this specific indication was identified.

---

## Taiwan Market Information

No TFDA (Taiwan Food and Drug Administration) registration records for Valsartan were found in this dataset. Valsartan is broadly approved across major regulatory jurisdictions (U.S. FDA, EMA, PMDA) for hypertension, heart failure with reduced ejection fraction, and post-MI left ventricular dysfunction. The absence of Taiwan registration data in this evidence pack may reflect a data collection gap and should be verified directly against the TFDA drug database before regulatory decisions are made.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic case for Valsartan in malignant hypertensive renal disease is biologically compelling — AT1R blockade directly addresses the RAAS-driven glomerular injury cascade — the current evidence base is L4, consisting solely of one preclinical study using a mechanistically distinct drug. No clinical or human observational data exist to support advancement at this stage.

**To proceed, the following is needed:**

- **Clinical evidence:** Retrospective cohort study or registry analysis evaluating outcomes of ARB use (specifically valsartan or losartan as a comparator) in patients with confirmed malignant hypertensive nephropathy
- **Mechanistic data:** Formal MOA documentation from DrugBank (AT1R selectivity, binding kinetics, downstream RAAS suppression profile)
- **Safety data:** TFDA package insert or equivalent source to establish key warnings, contraindications, and renal-dose adjustment requirements (critical given the target population has severe renal impairment by definition)
- **Trial design:** Define diagnostic criteria distinguishing malignant hypertensive renal disease from other hypertensive nephropathy subtypes, and identify measurable endpoints (eGFR trajectory, proteinuria reduction, renal survival at 12 months)
- **Translational bridge:** Consider initiating a systematic literature review or meta-analysis on ARB use in hypertensive emergency with renal involvement as a lower-cost precursor to prospective trial planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

