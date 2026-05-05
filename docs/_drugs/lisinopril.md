---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

使用 `txgnn-pipeline` 確認此為 TW 系列 Evidence Pack 報告任務。現在根據 Evidence Pack JSON 產生報告。

**分析重點：**
- Drug: Lisinopril (DB00722)，ACE 抑制劑，原始 MOA 缺失
- 最高排名預測：Posterolateral MI（Rank 1，L4，無臨床試驗/文獻）
- 台灣未上市，授權數 0
- 非抗腫瘤藥物，省略 Cytotoxicity 章節
- 所有安全性資料均為 Data Gap，使用 fallback 文字

---

# Lisinopril: From Hypertension / Heart Failure to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is a well-established ACE inhibitor used globally for hypertension, heart failure, and post-myocardial infarction management, though no Taiwan regulatory approval is currently on record.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** — a specific anatomical subtype of MI — with **no dedicated clinical trials or publications** identified for this particular subtype at present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan regulatory record (globally: hypertension, heart failure, acute MI) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Lisinopril is an ACE (Angiotensin-Converting Enzyme) inhibitor that blocks the renin-angiotensin-aldosterone system (RAAS) by preventing the conversion of angiotensin I to angiotensin II. This leads to vasodilation, reduced aldosterone secretion, decreased cardiac afterload, and — critically — suppression of the angiotensin II–mediated myocardial fibrosis and ventricular remodeling that drives adverse outcomes after MI.

Posterolateral myocardial infarction is an anatomical subtype typically resulting from occlusion of the circumflex artery, affecting the posterior and lateral walls of the left ventricle. The pathophysiological cascade that follows — neurohormonal activation, RAAS upregulation, and progressive left ventricular remodeling — is fundamentally identical to that seen in any other MI territory. The landmark GISSI-3 randomized trial demonstrated that Lisinopril significantly improved six-week mortality and reduced left ventricular dysfunction across the broad acute MI population, providing strong mechanistic grounds for its applicability to this specific subtype.

The absence of dedicated evidence for posterolateral MI therefore reflects a gap in clinical trial subgroup reporting, not a genuine mechanistic limitation. Current cardiovascular guidelines (ESC, ACC/AHA) recommend ACE inhibitors for all MI patients with reduced ejection fraction or signs of heart failure, without restricting the recommendation by anatomical infarct location.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction specifically.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction specifically.

---

## Taiwan Market Information

No Taiwan regulatory approvals on record for Lisinopril.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan TFDA package insert data (warnings and contraindications) is currently unavailable — this is a blocking data gap that must be resolved before any clinical use evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for Lisinopril in posterolateral MI is well-grounded — directly supported by the GISSI-3 RCT covering general acute MI — no independent clinical trial or publication specifically addresses this anatomical subtype, and critical safety data (Taiwan TFDA package insert) is currently missing.

**To proceed, the following is needed:**

- **\[Blocking\]** Obtain Taiwan TFDA package insert — retrieve warnings and contraindications before any safety evaluation can begin
- **\[High Priority\]** Retrieve detailed MOA data from DrugBank (DB00722)
- Search for subgroup-level outcomes in existing large MI trials (GISSI-3, ISIS-4, CONSENSUS II) specifically reporting on posterolateral or circumflex-territory infarction cohorts
- Clarify whether existing general post-MI indications under current prescribing guidelines already encompass this anatomical subtype, which may make a dedicated repurposing pathway unnecessary
- Review whether Lisinopril is available or planned for Taiwan market entry, given current zero-license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

