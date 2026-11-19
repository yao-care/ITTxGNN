# ITTxGNN - Claude CLI 使用指引

本 repo 的維運以母 repo（yao-care/txgnn）CLAUDE.md 為準；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用義大利文，依據是 AIFA 包裝清單（confezioni）；在地字樣集中在 `src/ittxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/ittxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/ittxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/it_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/ittxgnn/regulatory/licenses.py` | 本站沒有程式產生的許可證表；gate 依快照驗市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 正文裡跟許可證事實矛盾、直接刪掉的子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 507 筆紀錄（264 頁；
其中 1 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。

2026-11-12 表格列狀態對事實層（母目錄 `check_drug_page.py --row-status`）：levonorgestrel 036489019、norfloxacin 034401024／034941043／025000023 在表格寫「revocata」，AIFA 行政狀態（證據包原文）是 Autorizzata；以 `it-row-20261112-*`（每頁一筆）刪掉狀態註記。

## 新資料查不到的許可證（2026-11-17）

11-16 每週排程列出 137 張「新資料查不到」的 AIC（9 碼包裝碼）並開 issue。2026-11-17 用戶要求確認實際狀態：
AIFA 開放資料 confezioni.csv 是現行許可登錄（160,101 列，只有 Autorizzata／Sospesa；revoca、decadenza 後整筆移除），
137 張全是證據包從 2025-09-30 Classe A 給付清單收進來的包裝，現在 confezioni 與 Banca Dati Farmaci 線上查詢（依品名查 14,199 個現行 AIC）都不列。
其中 11 張的整個藥品見 AIFA sunset clause 失效公告（Determina 7/2025、456/2026、616/2026）；69 張還在 2026-06-30 Classe A 清單、43 張還在
2026-11-16 transparency 清單——給付清單不是許可登錄（撤銷後可售完庫存），不拿來判定有效。沒有找到「在別份現行許可清單上」的號。
- `scripts/license_adapter.py`：fetch() 把 confezioni 全部 AIC 記成 CURRENT（少於 100,000 不判定）；preprocess 對不在 CURRENT 的 9 碼 AIC 標
  `license_status: cancelled`＋`aifa_not_listed`（第一次發現日）、status 改「Non più autorizzata」（原值存 `aifa_status_before`），又出現就還原；
  `confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」，不算「查不到」、不開 issue。
- 64 頁狀態列／張數列、20 格許可證表狀態格照事實層同步；表格寫「valida」的 4 頁（atomoxetine、gemfibrozil、misoprostol、quinapril）以
  `it-row-20261117-*`、正文張數或狀態跟事實相反的 8 頁以 `it-lic-20261117-*` 更正（tobramycin 的 Nebicina 100／150 mg、meloxicam 的 MOBIC fiale／
  MELOXICAM Zentiva 原本就被寫成註銷，confezioni 為 Autorizzata，一併改正）。全部註銷的 2 頁依成分對 confezioni 確認：atomoxetine（STRATTERA 5 張，
  atomoxetina 現行 0 個包裝）、lenograstim（MYELOSTIM，現行 0 個；efbemalenograstim alfa 的 RYZNEUTA 是另一個藥）。

## 同一 DrugBank ID 的重複公開頁改轉址（2026-11-19）

用戶 2026-11-19 決定（照 ARTxGNN 同日做法）：公開藥物頁同一 DrugBank ID（front matter drugbank_id，沒有的用證據包與 dbXXXXX 轉址頁推斷）、預測相同的，留一頁、另一頁改轉址（layout: id_redirect、permalink 不變、sitemap: false、search_exclude、nav_exclude）。
11 組，各組預測、等級（全 L5）、許可證號完全相同；保留順序：查核紀錄數→字數（差 5% 內算平手）→義文 INN 名。
轉址：alfuzosina→alfuzosin、amlodipine→amlodipina（平手）、duloxetine→duloxetina、chlorpromazine→clorpromazina、clonidina→clonidine、doxazosin→doxazosina、epinephrine→adrenalina、apomorfina→apomorphine、desloratadine→desloratadina、colchicine→colchicina、ebastine→ebastina（平手）。
dbXXXXX 轉址頁原本指到被轉址頁的 8 頁（db00381、db00476、db00477、db00590、db00668、db00967、db01394、db11742）改成直接指保留頁，沒有轉址鏈。
被轉址頁 colchicine 的查核紀錄 it-lic-20261106-colchicine-1 留在 drug_reviews.json 當歷史（apply_drug_reviews 跳過轉址頁）；保留頁 colchicina 寫的是 2 張皆有效，沒有同樣的錯句。
公開藥物頁 448→437；FHIR 的 MK 以 DrugBank ID 對頁，不變（429）；衍生檔、hreflang 照重產。
