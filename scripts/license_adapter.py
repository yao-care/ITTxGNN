"""IT（AIFA）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：AIFA 開放資料 https://drive.aifa.gov.it/farmaci/confezioni.csv（全部包裝，; 分隔，免金鑰）。
欄位：CODICE_AIC（9 碼，＝證據包 license_id）、STATO_AMMINISTRATIVO（Autorizzata／Revocata／Sospesa…）。
站上原本的來源是 A／H 類給付清單（只有給付品項，不在清單不等於撤銷），這裡改用有正式行政狀態的全品項檔。
寫回：status＝行政狀態，原本的「(Classe A)」等給付類別後綴保留；reviewer 依文字判定（revoca、sospes 算註銷）。
新檔沒有的 AIC 保留原狀態。
"""
import csv
import io
import re
import time

import requests

RAW_FILE = "raw/aifa_confezioni_stato.json"
URL = "https://drive.aifa.gov.it/farmaci/confezioni.csv"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    raw = r.content
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    rows = csv.DictReader(io.StringIO(text), delimiter=";")
    if "CODICE_AIC" not in (rows.fieldnames or []) or "STATO_AMMINISTRATIVO" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    return [{"aic": (x["CODICE_AIC"] or "").strip(), "stato": (x["STATO_AMMINISTRATIVO"] or "").strip()} for x in rows if x.get("CODICE_AIC")]


def validate(new, old):
    p = []
    if len(new) < 50000:
        p.append(f"只解析出 {len(new)} 筆（AIFA 通常 >100,000），疑似格式改變")
    if sum(1 for r in new if not r["stato"]) > 0.01 * max(1, len(new)):
        p.append("超過 1% 缺 STATO_AMMINISTRATIVO")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["aic"]: r["stato"] for r in new if r["stato"]}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    old = rec.get("status") or ""
    suffix = (re.search(r"\s*\((Classe [^)]*)\)\s*$", old) or [None, None])[1]
    want = f"{new} ({suffix})" if suffix else new
    if old == want:
        return False
    rec["status"] = want
    return True
