"""正文許可證張數的程式改寫（2026-11-24，用戶決定；概念比照 KrTxGNN／MyTxGNN 同名檔與 TwTxGNN page_postprocess.rewrite_count_prose，
規則是本站義大利文句型，移植自 FRTxGNN 同名檔）。

正文裡「N autorizzazioni valide (su M)」「delle M autorizzazioni N risultano valide」「Sono presenti N autorizzazioni」「Tutte le N autorizzazioni
risultano valide」這類 AIFA 張數敘述（本站的「autorizzazione」＝9 碼 AIC 包裝），由程式依許可證快照（snapshots/it_licenses.json.gz 的 facts）改寫，
每週資料更新後跟著改，不逐筆寫查核紀錄（程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥許可張數」的地方，其餘一律不動：
  - 句子要有 autorizzazione／AIC／confezione 字樣，且沒有試驗、文獻、劑量、年份等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter、引言框；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）；事實層 partial 的頁整頁不動。
  - 整句不動（skipped 記 hedged/subset，不列待查）：有保留（almeno、parziale、una parte、circa、oltre、più di、fino a）、
    講表上幾筆（elencate、mostrate、riportate、tabella、prime、principali、seguenti、esempi）、相對數（altre、restanti、di cui、ulteriori）、
    劑型、劑量、廠商、單方／複方子集（monocomponente、singolo principio attivo、associazione、generici、titolare…）、證據包或查詢。
  - 數字只認阿拉伯數字；文字數詞（due～dodici、entrambe、tutte e tre）與 una／un'unica／una sola 不改，事實不符時列 wordnum／singular。
角色（看數字前後）：valide／attive／in corso di validità→有效；revocate／cancellate／sospese／non (risultano) più autorizzate→非有效；
「N … su M」「delle M autorizzazioni」「Delle M」的 M→總數；「N autorizzazioni valide su M」「delle M … N risultano valide」的 N→有效；
「Tutte (e) (le) N autorizzazioni … valide」「Le N autorizzazioni sono tutte valide」「N autorizzazioni, tutte valide」→全部有效（總數＝有效數才成立，否則列 premise）。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同列 ambiguous。
原數字或新數字是 0 或 1 的不改（0 是前提不同、1 會牽動單複數配合），列 zero-premise／singular。
同一行只要有一句含張數而被略過，整行都不動（免得前後句數字對不上）。
"""
from __future__ import annotations

import re

NUMW = {"due": 2, "tre": 3, "quattro": 4, "cinque": 5, "sei": 6, "sette": 7, "otto": 8, "nove": 9, "dieci": 10, "undici": 11, "dodici": 12,
        "entrambe": 2, "entrambi": 2, "ambedue": 2}
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý*\[(«-])")
NUM = re.compile(r"(?<![\w.,/°-])(\d{1,4})(?![\w/%°-]|[.,]\d)")
WORDNUM = re.compile(r"\b(" + "|".join(NUMW) + r")\b", re.I)
NOUN = r"(?:autorizzazion[ei](?: all'immissione in commercio| italiane| locali| registrate| a commercio)?|AIC|confezion[ei](?: autorizzate)?)"
LICENSE = re.compile(r"\bautorizzazion[ei]\b|\bAIC\b|\bconfezion[ei]\b", re.I)
NOT_LICENSE = re.compile(r"\bstud[io]\b|\bsperimentazion|\btrial\b|pubblicazion|articol|PMID|NCT|pazient|\bcasi\b|\bmg\b|\bml\b|µg|microgramm|%|"
                         r"\b(19|20)\d\d\b|\banni\b|\bmesi\b|settiman|\bgiorni\b|punteggio|predizion|interazion|eventi avversi|\bdose", re.I)
HEDGED = re.compile(r"almeno|\bparziale\b|parzialmente|(?:elenco|dati|lista)[^.;]{0,30}parzial|una parte|circa|\boltre\b|più di|meno di|fino a|quasi|"
                    r"elencat|mostrat|riportat[ei] (?:qui|sopra|sotto|di seguito|nella|in tabella)|sono riportat[ei] (?:le|solo|\d)|indicat[ei] (?:qui|sopra|sotto|nella)|tabella|\bprim[ei]\b|principal|seguent|esempi|sopra|sotto|"
                    r"\baltr[ei]\b|restant|\bdi cui\b|ulterior|\banche\b|anch'ess|"
                    r"monocomponente|singolo principio|principio attivo singolo|solo principio|\b(?:del|di) sol[oa]\b|a base di|associazion|combinazion|"
                    r"generic|equivalent|biosimilar|titolar|intestat|\bdi \w+ (?:SpA|Srl)\b|"
                    r"compress|capsul|fial|cerott|iniett|soluzion|sciropp|crema|pomata|\bgel\b|collirio|polvere|supposte|spray|\bin forma\b|dosaggi|"
                    r"Evidence Pack|interrog|ricerca|veterinar", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
CANC = r"(?:revocat[ae]|cancellat[ae]|annullat[ae]|sospes[ae]|decadut[ae]|ritirat[ae]|non (?:risultano |sono )?più autorizzat[ae])"
VALID = r"(?:valide|attive|in corso di validità|in vigore)"


def _role(s, a, b):
    left, right = s[max(0, a - 40):a].lower(), s[b:b + 80].lower()
    if re.search(r"(?:\bsu|\bdelle|\bdegli|\bdei|\bsu un totale di|\bdelle sue)\s+$", left):
        if re.search(r"\bdelle\s+$", left) and re.match(rf"\s+{NOUN}\s+{VALID}\b", right, re.I):
            return "valid"  # 「delle 11 autorizzazioni valide」
        return "total"
    if re.search(rf"\b{NOUN}\s+(?:\w+\s+)?sono\s+$", left, re.I) and not re.match(rf"\s+(?:{VALID}|{CANC})", right):
        return "total"  # 「Complessivamente le autorizzazioni sono 7」
    if re.match(rf"\s+(?:(?:risultano|sono|restano)\s+)?{CANC}\b", right) or \
            re.match(rf"\s+{NOUN}\s+(?:\w+\s+)?(?:(?:risultano|sono)\s+)?{CANC}\b", right, re.I):
        return "cancelled"
    # 「N autorizzazioni valide su M」「N su M」：N 是有效數
    if re.match(rf"\s+(?:{NOUN}\s+)?(?:{VALID}\s+)?su\s+\d+\b", right, re.I):
        return "valid"
    if re.match(rf"\s+(?:(?:risultano|sono|restano)\s+)?{VALID}\b", right) or \
            re.match(rf"\s+{NOUN}\s+{VALID}\b", right, re.I):
        return "valid"
    if re.search(rf"\b(?:risultano|sono)\s+{VALID}\s+$", left) and re.match(rf"\s+{NOUN}\b", right, re.I):
        return "valid"
    # 「Tutte e N le autorizzazioni (registrate) risultano valide」
    if re.search(r"\btutt[ei] e\s+$", left) and re.match(rf"\s+(?:le|i)\s+{NOUN}\b", right, re.I):
        return "allvalid" if re.match(rf"\s+(?:le|i)\s+{NOUN}\s*(?:\([^)]*\)\s*)?(?:\w+\s+){{0,2}}?(?:(?:risultano|sono)\s+)?{VALID}", right, re.I) else "total"
    if re.match(rf"\s+{NOUN}\b", right, re.I):
        if re.search(r"\b(?:tutte(?: e)?(?: le)?|le)\s+$", left) and \
                re.match(rf"\s+{NOUN}\s*(?:\w+\s+){{0,3}}?,?\s*(?:(?:risultano|sono)\s+)?(?:tutte\s+)?{VALID}", right, re.I):
            return "allvalid"
        if re.match(rf"\s+{NOUN}(?:\s+\w+){{0,3}}?\s*,\s*tutte\s+(?:\w+\s+)?{VALID}", right, re.I):
            return "allvalid"
        return "total"
    return None


def _readings(role, f, explicit=False):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    nonvalid = None if t is None or v is None else t - v
    if role == "cancelled":
        return {c, nonvalid}, (c if c == nonvalid else None)
    if role == "valid":
        return {v}, v
    if role == "allvalid":
        return {t}, t
    if explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f, roles):
    lo = sent.lower()
    allv = "allvalid" in roles or re.search(r"\btutte\s+(?:\w+\s+){0,2}valide\b|\bnessuna\s+(?:\w+\s+){0,2}(?:revocat|cancellat|annullat)", lo)
    if allv and (f.get("valid") != f.get("total") or f.get("cancelled")):
        return False
    return True


ONE = re.compile(r"\b(?:una sola|un'unica|l'unica|una singola)\s+(?:autorizzazione|AIC|confezione)\b"
                 r"|\b(?:una|un')\s*(?:autorizzazione|confezione)\s+(?:\w+\s+)?(?:valida|attiva|autorizzata)\b", re.I)


def _wordnum_mismatch(sent, f):
    """文字數詞（due～dodici、entrambe、tutte e tre）講張數：跟事實不符就列 wordnum（不改，單複數與數詞要一起改）"""
    lo = sent.lower()
    for m in WORDNUM.finditer(lo):
        w = NUMW[m.group(1)]
        right = lo[m.end():m.end() + 60]
        if not re.match(rf"\s+(?:le\s+)?{NOUN}\b", right, re.I) and not re.match(rf"\s+le\s+{NOUN}\b", right, re.I):
            if not (m.group(1) in ("entrambe", "entrambi", "ambedue") and re.match(rf"\s+(?:le\s+)?{NOUN}", right, re.I)):
                continue
        allv = re.search(rf"{VALID}", lo[m.end():]) and not re.search(CANC, lo)
        canc = re.search(CANC, lo[m.end():])
        t, v = f.get("total"), f.get("valid")
        if canc:
            if w != (t - v if t is not None and v is not None else None):
                return True
        elif allv:
            if not (w == t == v):
                return True
        elif w not in (t, v):
            return True
    return False


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not LICENSE.search(sent) or NOT_LICENSE.search(sent):
        return sent, None
    if ONE.search(sent) and not HEDGED.search(sent) and f.get("total") != 1 \
            and not re.search(r"\b(?:non|nessun\w*|senza)\b", sent, re.I):
        return sent, "singular"  # 「una sola autorizzazione」而事實不是 1 張：要改單複數配合，列待查
    if WORDNUM.search(sent) and not HEDGED.search(sent) and _wordnum_mismatch(sent, f):
        return sent, "wordnum"
    if not NUM.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    if not any(r for _, r in found):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    subs, roles = [], {r for _, r in found if r}
    for m, role in found:
        if role is None:
            continue
        old = int(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0 or v == 0:
            return sent, "zero-premise"
        if old == 1 or v == 1:
            return sent, "singular"
        subs.append((m, v))
    if not _premise_ok(sent, f, roles):
        return sent, "premise"  # 說「全部有效」而事實有註銷：數字對也不改，列待查
    if not subs:
        return sent, None
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", ">")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
