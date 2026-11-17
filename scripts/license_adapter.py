"""IT（AIFA）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：AIFA 開放資料 https://drive.aifa.gov.it/farmaci/confezioni.csv（全部包裝，; 分隔，免金鑰）。
欄位：CODICE_AIC（9 碼，＝證據包 license_id）、STATO_AMMINISTRATIVO（Autorizzata／Revocata／Sospesa…）。
站上原本的來源是 A／H 類給付清單（只有給付品項，不在清單不等於撤銷），這裡改用有正式行政狀態的全品項檔。
寫回：status＝行政狀態，原本的「(Classe A)」等給付類別後綴保留；reviewer 依文字判定（revoca、sospes 算註銷）。
新檔沒有的 AIC 保留原狀態。
2026-11-17（用戶要求確認查不到的許可證）：confezioni.csv 是 AIFA 的現行許可登錄（只列 Autorizzata／Sospesa 的包裝，
revoca、decadenza 之後整筆拿掉；2026-11-17 下載 160,101 列，Banca Dati Farmaci 線上查詢也只回這些包裝）。
11-16 排程「查不到」的 137 張 AIC 全是證據包從 2025-09-30 Classe A 清單收進來的包裝，現在 confezioni 與 Banca Dati Farmaci 都不列
（其中 11 張的整個藥品見 AIFA sunset clause 失效公告；69 張還在 2026-06-30 的 Classe A 清單、43 張還在 2026-11-16 的
transparency 清單——給付清單不是許可登錄，撤銷後可售完庫存的包裝會留一段時間，不拿來判定有效）。
preprocess 對 confezioni 沒有的 9 碼 AIC 標 license_status＝cancelled、aifa_not_listed（第一次發現日），status 改「Non più autorizzata」
（原狀態存 aifa_status_before）；之後又出現在 confezioni 就取消標記、還原原狀態（再由 update 依新狀態寫回）。下載失敗或筆數過少時不做這個判定。
"""
import csv
import io
import re
import time

import requests

RAW_FILE = "raw/aifa_confezioni_stato.json"
URL = "https://drive.aifa.gov.it/farmaci/confezioni.csv"
CURRENT: set = set()   # fetch() 填：confezioni 的全部 AIC（現行許可登錄）；空的就不做「不在清單」判定
MIN_CURRENT = 100000   # 現行 AIC 少於這個數＝下載或格式有問題，不判定
NOT_LISTED = "Non più autorizzata"


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
    out = [{"aic": (x["CODICE_AIC"] or "").strip(), "stato": (x["STATO_AMMINISTRATIVO"] or "").strip()} for x in rows if x.get("CODICE_AIC")]
    CURRENT.clear()
    aics = {r["aic"] for r in out if r["aic"]}
    if len(aics) >= MIN_CURRENT:
        CURRENT.update(aics)
    return out


def _aic(lid):
    s = str(lid or "").strip()
    return s if re.fullmatch(r"\d{9}", s) else None


def confirmed_absent(lid):
    """給 license_refresh：confezioni（現行許可登錄，有成功下載）沒有這個 9 碼 AIC＝確認已不是現行許可"""
    a = _aic(lid)
    return bool(CURRENT) and a is not None and a not in CURRENT


def preprocess(bundle):
    """confezioni 沒有的 AIC 標 cancelled（aifa_not_listed＝第一次發現日）；又出現的取消標記。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        a = _aic(r.get("license_id"))
        if a is None:
            continue
        if a in CURRENT:
            if r.get("aifa_not_listed"):
                r.pop("aifa_not_listed", None)
                r.pop("license_status", None)
                r["status"] = r.pop("aifa_status_before", None) or r.get("status")  # update() 再依新狀態寫回
                ch = True
        elif not r.get("aifa_not_listed"):
            r["aifa_not_listed"] = today
            r["license_status"] = "cancelled"
            r["aifa_status_before"] = r.get("status") or ""
            r["status"] = NOT_LISTED
            ch = True
    return ch


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
