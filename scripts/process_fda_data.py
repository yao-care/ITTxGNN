#!/usr/bin/env python3
"""處理義大利 AIFA 藥品資料

從 AIFA 網站下載 A 類與 H 類藥品清單 CSV 並合併轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://www.aifa.gov.it/en/liste-farmaci-a-h
    CSV 直接下載:
      - Classe_A_per_principio_attivo_{date}.csv
      - Classe_H_per_principio_attivo_{date}.csv

產生檔案:
    data/raw/it_fda_drugs.json
"""

import json
import re
from pathlib import Path

import pandas as pd
import requests
import yaml


# AIFA CSV 下載 URL 模板（日期部分會更新，需嘗試最新日期）
AIFA_BASE = "https://www.aifa.gov.it"
AIFA_DOC_PATH = "/documents/20142/3442801"
AIFA_CSV_URLS = {
    "classe_a": f"{AIFA_BASE}{AIFA_DOC_PATH}/Classe_A_per_principio_attivo_30-09-2025.csv",
    "classe_h": f"{AIFA_BASE}{AIFA_DOC_PATH}/Classe_H_per_principio_attivo_30-09-2025.csv",
}

# 替代：等價藥品清單（有 AIC、活性成分、廠商等）
AIFA_EQUIV_URL = f"{AIFA_BASE}/documents/20142/825643/Lista_farmaci_equivalenti.csv"


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_aifa_csv(url: str, output_path: Path, description: str) -> bool:
    """下載單一 AIFA CSV 檔案

    Args:
        url: 下載 URL
        output_path: 輸出路徑
        description: 描述文字

    Returns:
        是否下載成功
    """
    print(f"  正在下載 {description}...")
    print(f"  URL: {url}")

    try:
        response = requests.get(url, timeout=120, headers={
            "User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)",
        })
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        # 檢查是否為 HTML（非 CSV）
        if "text/html" in content_type and "text/csv" not in content_type:
            # 進一步檢查內容開頭是否像 HTML
            head = response.content[:500].decode("utf-8", errors="replace")
            if "<html" in head.lower() or "<!doctype" in head.lower():
                print(f"  警告: 回傳 HTML 而非 CSV (Content-Type: {content_type})")
                return False

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(response.content)

        size_mb = output_path.stat().st_size / 1024 / 1024
        print(f"  下載完成: {output_path.name} ({size_mb:.1f} MB)")
        return True

    except requests.RequestException as e:
        print(f"  下載失敗: {e}")
        return False


def download_aifa_data(raw_dir: Path) -> list[Path]:
    """從 AIFA 下載藥品清單 CSV

    嘗試下載 A 類和 H 類藥品 CSV。若特定日期版本失敗，
    則嘗試等價藥品清單作為替代。

    Args:
        raw_dir: 輸出目錄

    Returns:
        成功下載的檔案路徑列表
    """
    print("正在從 AIFA 下載藥品清單 CSV...")
    print()

    downloaded = []

    # 嘗試下載 A 類和 H 類 CSV
    for key, url in AIFA_CSV_URLS.items():
        filename = url.rsplit("/", 1)[-1]
        output_path = raw_dir / filename
        if output_path.exists():
            print(f"  已存在: {output_path.name}")
            downloaded.append(output_path)
            continue
        if download_aifa_csv(url, output_path, f"{key} 藥品清單"):
            downloaded.append(output_path)

    # 若 A 類和 H 類都失敗，嘗試等價藥品清單
    if not downloaded:
        print("\n  A/H 類清單下載失敗，嘗試等價藥品清單...")
        equiv_path = raw_dir / "Lista_farmaci_equivalenti.csv"
        if equiv_path.exists():
            print(f"  已存在: {equiv_path.name}")
            downloaded.append(equiv_path)
        elif download_aifa_csv(AIFA_EQUIV_URL, equiv_path, "等價藥品清單"):
            downloaded.append(equiv_path)

    if not downloaded:
        print("\n自動下載失敗。請手動下載：")
        print(f"  前往: https://www.aifa.gov.it/en/liste-farmaci-a-h")
        print(f"  下載 CSV 檔案並放置於: {raw_dir}/")
        raise FileNotFoundError("無法下載 AIFA 藥品清單 CSV")

    return downloaded


def read_aifa_csv(csv_path: Path) -> pd.DataFrame:
    """讀取 AIFA CSV 檔案（自動偵測分隔符號和編碼）

    Args:
        csv_path: CSV 檔案路徑

    Returns:
        DataFrame
    """
    # AIFA CSV 使用分號分隔，通常 UTF-8 編碼
    for encoding in ("utf-8", "latin-1", "cp1252"):
        try:
            df = pd.read_csv(
                csv_path, encoding=encoding, sep=";",
                dtype=str, on_bad_lines="skip",
            )
            if len(df.columns) > 1:
                return df
        except (UnicodeDecodeError, Exception):
            continue

    # 嘗試逗號分隔
    for encoding in ("utf-8", "latin-1"):
        try:
            df = pd.read_csv(
                csv_path, encoding=encoding, sep=",",
                dtype=str, on_bad_lines="skip",
            )
            if len(df.columns) > 1:
                return df
        except (UnicodeDecodeError, Exception):
            continue

    raise ValueError(f"無法讀取 CSV: {csv_path}")


def normalize_columns(df: pd.DataFrame, source_file: str) -> pd.DataFrame:
    """正規化欄位名稱以符合 fields.yaml 的 field_mapping

    AIFA CSV 欄位名稱因版本不同：
    - A/H 類清單: "Principio Attivo", "Denominazione e Confezione", "Titolare AIC", "AIC" / "Codice AIC"
    - 等價藥品清單: "Principio attivo", "Farmaco", "Ditta", "AIC"

    統一映射至: Principio_Attivo, Denominazione, Titolare_AIC, Codice_AIC, Stato_AIC, Forma_Farmaceutica

    Args:
        df: 原始 DataFrame
        source_file: 來源檔案名稱

    Returns:
        正規化後的 DataFrame
    """
    # 清理欄位名稱中的空白
    df.columns = [c.strip() for c in df.columns]

    col_map = {}
    cols_lower = {c.lower(): c for c in df.columns}

    # Principio_Attivo（活性成分）
    for candidate in ["Principio Attivo", "Principio attivo", "principio_attivo", "Principio_Attivo"]:
        if candidate in df.columns:
            col_map[candidate] = "Principio_Attivo"
            break
    if "Principio_Attivo" not in col_map.values():
        for k, v in cols_lower.items():
            if "principio" in k and "attivo" in k:
                col_map[v] = "Principio_Attivo"
                break

    # Denominazione（藥品名稱）
    for candidate in ["Denominazione e Confezione", "Farmaco", "Denominazione", "Nome"]:
        if candidate in df.columns:
            col_map[candidate] = "Denominazione"
            break

    # Titolare_AIC（持有者）
    for candidate in ["Titolare AIC", "Ditta", "Titolare_AIC", "Titolare"]:
        if candidate in df.columns:
            col_map[candidate] = "Titolare_AIC"
            break

    # Codice_AIC
    for candidate in ["AIC", "Codice AIC", "Codice_AIC", "Codice Aic"]:
        if candidate in df.columns:
            col_map[candidate] = "Codice_AIC"
            break

    # Codice Gruppo Equivalenza（作為 Forma_Farmaceutica 的替代）
    for candidate in ["Codice Gruppo Equivalenza", "Codice_Gruppo"]:
        if candidate in df.columns:
            col_map[candidate] = "Codice_Gruppo"
            break

    # ATC
    for candidate in ["ATC", "ATC-kod", "Codice ATC"]:
        if candidate in df.columns:
            col_map[candidate] = "ATC"
            break

    df = df.rename(columns=col_map)

    # 從 A/H 類清單推斷 Stato_AIC（這些清單只包含有效的藥品）
    if "Stato_AIC" not in df.columns:
        if "classe_a" in source_file.lower():
            df["Stato_AIC"] = "Autorizzata (Classe A)"
        elif "classe_h" in source_file.lower():
            df["Stato_AIC"] = "Autorizzata (Classe H)"
        elif "equivalenti" in source_file.lower():
            df["Stato_AIC"] = "Autorizzata"
        else:
            df["Stato_AIC"] = ""

    # 補上缺少的欄位
    if "Forma_Farmaceutica" not in df.columns:
        df["Forma_Farmaceutica"] = ""

    return df


def process_aifa_csvs(csv_paths: list[Path], output_path: Path) -> Path:
    """處理多個 AIFA CSV 並合併轉換為 JSON

    Args:
        csv_paths: CSV 檔案路徑列表
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()

    dfs = []
    for csv_path in csv_paths:
        print(f"\n讀取: {csv_path.name}")
        df = read_aifa_csv(csv_path)
        print(f"  欄位: {', '.join(df.columns.tolist())}")
        print(f"  筆數: {len(df)}")
        df = normalize_columns(df, csv_path.name)
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    print(f"\n合併後總筆數: {len(combined)}")

    # 去重（以 Codice_AIC 為準）
    if "Codice_AIC" in combined.columns:
        before = len(combined)
        combined = combined.drop_duplicates(subset=["Codice_AIC"], keep="first")
        after = len(combined)
        if before != after:
            print(f"去重: {before} -> {after} ({before - after} 重複)")

    # 清理資料
    combined = combined.fillna("")

    # 轉換為 JSON
    data = combined.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(combined, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理義大利 AIFA 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "it_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找已下載的 CSV（AIFA A/H 類或等價藥品）
    aifa_csvs = sorted(raw_dir.glob("Classe_*_per_principio_attivo_*.csv"))
    equiv_csv = raw_dir / "Lista_farmaci_equivalenti.csv"

    if aifa_csvs:
        csv_paths = list(aifa_csvs)
        print(f"找到 {len(csv_paths)} 個 AIFA CSV 檔案")
    elif equiv_csv.exists():
        csv_paths = [equiv_csv]
        print(f"使用等價藥品清單: {equiv_csv.name}")
    else:
        # 下載
        csv_paths = download_aifa_data(raw_dir)

    # 處理 CSV
    process_aifa_csvs(csv_paths, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
