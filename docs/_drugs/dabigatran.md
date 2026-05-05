---
layout: default
title: Dabigatran
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 0
---

# Dabigatran
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# DABIGATRAN: 藥物再利用候選評估 — 資料不足，無法完成完整報告

## One-Sentence Summary

DABIGATRAN（DrugBank ID: DB14726）為本次藥物再利用掃描所識別之候選藥物。
然而，目前的 Evidence Pack **未能擷取原始適應症**、**無 TxGNN 預測適應症**、且**全部安全性資料缺失**，
無法依標準格式產生完整評估報告，建議先補齊資料後再進行評估。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 未擷取（原始適應症欄位為空） |
| Predicted New Indication | 無可用預測（`predicted_indications` 陣列為空） |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — 無臨床試驗或文獻資料 |
| Italy Market Status | Not marketed（查詢結果：未上市，授權數量 0） |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

無法進行機轉關聯性分析。

本次 Evidence Pack 顯示兩項關鍵資料缺口：

1. **原始適應症未擷取**：`original_indications` 欄位為空陣列，`original_moa` 亦無資料。
2. **無 TxGNN 預測結果**：`predicted_indications` 為空陣列，代表模型預測尚未執行或結果未納入 Pack。

在缺乏「新預測適應症」的情況下，無從比較原適應症與新適應症之間的機轉重疊性，
亦無從判斷此候選藥物是否值得進一步評估。

---

## Italy Market Information

DABIGATRAN 在 Italy 查無任何上市授權紀錄（`total_licenses: 0`，`licenses` 為空）。

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
DABIGATRAN 的 Evidence Pack 存在多項關鍵資料缺口（原始適應症、MOA、TxGNN 預測、安全性資料均缺失），
無法執行任何程度的再利用可行性評估，不建議在資料補齊前推進。

**To proceed, the following is needed:**

- **\[Blocking\] 補齊 TxGNN 預測結果**：重新執行模型，將 DABIGATRAN（DB14726）納入預測管線，確認 `predicted_indications` 輸出正確寫入 Evidence Pack
- **\[Blocking\] 擷取原始適應症**：從 DrugBank API 或核准仿單取得已核准適應症文字，填入 `original_indications`
- **\[High\] 補齊 MOA 資料**：查詢 DrugBank 取得完整作用機轉描述，支援後續機轉關聯分析
- **\[High\] 解析仿單安全性資料**：下載並解析 TFDA 仿單 PDF（query\_log 顯示已成功查詢），提取警語、禁忌症，填入 `safety` 欄位
- **\[Medium\] 確認 Italy（AIFA）上市狀態**：DABIGATRAN（Pradaxa®）在歐洲為已知上市藥物，建議直接查詢 AIFA 資料庫確認授權情況，更新 `taiwan_regulatory`（應調整為 `italy_regulatory`）欄位
- **資料補齊後重新產生 Evidence Pack v5**，再進行完整的再利用評估流程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

