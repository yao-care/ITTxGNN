---
layout: default
title: Losartan
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 8
---

# Losartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

The txgnn-pipeline skill confirms this is a report generation task within the TxGNN pipeline. Now I'll generate the full evaluation report based on the Evidence Pack.

---

# Losartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Losartan is a well-established angiotensin II type 1 receptor (AT1R) blocker, widely used globally for the treatment of hypertension and renal protection in diabetic nephropathy — though no Italy approval is recorded in the current dataset.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
with **0 clinical trials** and **2 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (no Italy approval on record; based on established pharmacology) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on the repurposing rationale provided, Losartan is an angiotensin II type 1 receptor (AT1R) blocker — the founding member of the ARB (angiotensin receptor blocker) drug class. It directly antagonizes the vasoconstrictive, pro-inflammatory, and pro-fibrotic effects of angiotensin II (AngII) by competitively binding the AT1 receptor.

Malignant renovascular hypertension is a severe, life-threatening condition driven by extreme, sustained overactivation of the renin-angiotensin-aldosterone system (RAAS). The trigger — typically renal artery stenosis or vasculitis (e.g., Takayasu's arteritis) — causes the kidney to produce excess renin, generating high circulating AngII that drives intense afferent arteriolar constriction, dangerously elevated intraglomerular pressure, and end-organ damage. Because AT1R blockade directly cuts off this central effector, the mechanistic link between Losartan and this condition is physiologically coherent and strong.

The most relevant publication (PMID 10667645) describes a real patient: Takayasu's arteritis with unilateral nephrectomy, renal artery stenosis, and malignant hypertension refractory to conventional antihypertensive regimens and non-amendable to angioplasty. Combination enalapril + losartan successfully controlled blood pressure. While this is a single case report, it directly supports the model's prediction and is fully consistent with the RAAS blockade rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Losartan in malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10667645](https://pubmed.ncbi.nlm.nih.gov/10667645/) | 2000 | Case Report | Angiology | Enalapril + losartan successfully controlled refractory malignant hypertension in a patient with Takayasu's arteritis and renal artery stenosis; blood pressure improved without further renal deterioration |
| [22294399](https://pubmed.ncbi.nlm.nih.gov/22294399/) | 2009 | Animal Study | Current Protocols in Pharmacology | Describes validated rodent models (SHR, DOCA-salt, Goldblatt 2K1C) for antihypertensive evaluation; captopril and reference ARBs demonstrate activity in renovascular hypertension models, providing pharmacological context |

---

## Italy Market Information

Losartan currently has no recorded authorizations in Italy per this dataset (market status: Not Marketed, 0 licenses). This is notable given Losartan's widespread approval in other major markets (US, EU, Japan, Taiwan). Data completeness should be verified against the AIFA registry directly before drawing conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a highly compelling mechanistic link through RAAS/AT1R blockade, the evidence base for Losartan specifically in malignant renovascular hypertension is limited to a single case report and one animal model study (L4). No registered clinical trials exist for this indication, and all Italy regulatory and safety data are unavailable, making it premature to advance without resolving these gaps.

**To proceed, the following is needed:**
- Verify Italy (AIFA) approval status — Losartan is approved in most major markets; absence of records likely reflects a data gap rather than true non-approval
- Obtain full package insert (warnings, contraindications, DDI profile) from the official AIFA/TFDA source to complete the S1 safety screen
- Retrieve complete MOA documentation from DrugBank (DB00678)
- Commission a targeted systematic literature review for ARBs in malignant hypertension and renovascular hypertension subtypes to establish whether L3 evidence (observational studies, meta-analyses) already exists
- If literature review supports advancement, design a prospective pilot study or registry in patients with malignant renovascular hypertension receiving AT1R blocker therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

