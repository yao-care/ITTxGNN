---
layout: default
title: Eliglustat
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Eliglustat
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

# Eliglustat: Gaucher Disease — TxGNN 預測資料不足，評估待補

---

## One-Sentence Summary

Eliglustat（品牌名：Cerdelga）是一種口服葡萄糖神經醯胺合酶抑制劑，核准用於第 1 型高雪氏症（Gaucher disease type 1）成人患者的長期基質減少療法。
本次 Evidence Pack（v4, 2026-04-20）中，**TxGNN 預測清單為空**，代表模型尚未對此藥產生可信的新適應症候選；同時，Taiwan 市場尚無核准許可，安全性資料亦存在缺口。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原核准適應症 | 第 1 型高雪氏症（Gaucher Disease Type 1） |
| 預測新適應症 | — 本次無 TxGNN 預測輸出 |
| TxGNN 預測分數 | 無 |
| 證據等級 | **L5**（模型尚無預測，無實際研究支撐） |
| Taiwan 市場狀態 | ✗ 未上市（0 張許可證） |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## Why is This Prediction Reasonable?

目前本 Evidence Pack 的 `predicted_indications` 為空陣列，代表 TxGNN 模型在此次批次中**未輸出任何新適應症預測**，可能原因包括：

1. 模型訓練時 Eliglustat 的知識圖譜（KG）節點連結度不足
2. 預測分數未超過篩選門檻
3. 資料管線在 mapping 階段發生遺失

就藥物本身而言，Eliglustat 透過抑制 UDP-葡萄糖神經醯胺合酶（GCS），減少 glucosylceramide 在巨噬細胞的異常堆積，屬高度靶向性的**酵素底物減少療法（SRT）**，機轉非常專一。

由於高雪氏症屬罕見溶小體貯積症，潛在的跨適應症轉用多集中在其他溶小體病變（如 Fabry disease、Niemann-Pick type C）或神經性高雪氏症（type 3）；然而這些方向目前均未出現在本次預測清單，無法進一步評估機轉關聯性。

---

## Clinical Trial Evidence

本次 Evidence Pack 無預測適應症，無對應臨床試驗資料。

> 目前無相關新適應症之已登錄臨床試驗可供呈現。

---

## Literature Evidence

本次 Evidence Pack 無預測適應症，無對應文獻資料。

> 目前無相關新適應症之文獻資料可供呈現。

---

## Taiwan Market Information

| 許可證字號 | 產品名稱 | 劑型 | 核准適應症 |
|-----------|---------|------|----------|
| — | — | — | — |

Eliglustat 目前在 Taiwan **尚未取得任何藥品許可證**，本次查詢（2026-03-29）TFDA 資料庫回傳 0 筆結果。

---

## Safety Considerations

本次資料包中所有安全性欄位均缺乏資料（key_warnings、contraindications 皆為空；DDI 查詢狀態為 not_found）。

> 請直接參閱 Cerdelga 原廠仿單（EMA/FDA SmPC/USPI）取得完整安全性資訊，特別注意 CYP2D6 表現型（EM/IM/PM）對劑量的影響及強效 CYP2D6/CYP3A 抑制劑交互作用。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本次 Evidence Pack 缺乏最關鍵的輸入——TxGNN 預測適應症清單為空，無法執行任何老藥新用評估；同時 MOA 資料缺失、Taiwan 尚未上市、安全性資料不完整，三項核心要素均不具備，不具備進入下一評估階段的條件。

**繼續推進需補齊以下資料：**

1. **重新執行 TxGNN 預測**：確認 Eliglustat（DB09039）在知識圖譜中的節點與邊是否正確載入，並降低或調整預測分數門檻
2. **補齊 MOA 資料**（DG002）：查詢 DrugBank API 取得 `mechanism_of_action`、`pharmacodynamics`、DrugBank categories
3. **補齊仿單安全性資料**（DG001）：從 EMA SmPC 或 FDA label 解析 key_warnings、contraindications、DDI
4. **評估 Taiwan 申請可行性**：確認 Eliglustat 是否有 IND 或孤兒藥申請計畫，或透過 EMA/FDA 互認機制加速取得 Taiwan 許可
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

