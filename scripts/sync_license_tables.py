#!/usr/bin/env python3
"""市場段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定「程式產生許可證表」；範本 FRTxGNN／UkTxGNN／SgTxGNN 同名檔）。

為什麼：藥物頁「## Informazioni sul mercato italiano」段落原本是 AI 寫的自由格式許可證表（欄位五花八門：Forma farmaceutica
多半是 AI 從品名猜的或「Non indicata」、Indicazione approvata 全是「Non registrata」，狀態寫在號碼格或適應症格的括號裡），
AIFA confezioni 每週變動後表上的狀態就過期，checker 擋整頁、要人處理。改成程式依證據包
（data/bundles/<藥>/drug_bundle.json 的 tfda.records：AIFA 9 碼 AIC 包裝）產生：

  | Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
  - 列＝證據包存的全部紀錄（收集器最多存 20 筆），有效（Autorizzata）在前，其餘照證據包順序。
  - 欄位照 AIFA 原文、不翻譯：AIC、品名（AIFA 寫法「NOME*confezione」，星號跳脫成 \\* 免得 markdown 當成斜體）、titolare AIC。
  - 狀態欄＝AIFA STATO_AMMINISTRATIVO 原文（Autorizzata／Sospesa；證據包附的「(Classe A)」給付類別不寫）；
    license_adapter 標 aifa_not_listed 的號碼寫本站既有寫法「Non più autorizzata」（confezioni 已不列，分不出撤銷或失效）。
  - 表後一句來源（SOURCE）；有「Non più autorizzata」的列時另加 NL_NOTE；證據包只收到部分包裝（total_matches 大於紀錄數）
    時另加 PART_NOTE（本站原有的程式句）。證據包沒有任何紀錄時不放表，改一句 NONE_LINE。
程式區塊前後有「<!-- licenses:begin -->」「<!-- licenses:end -->」；gate（src/ittxgnn/regulatory/licenses.py）依
snapshots/it_licenses.json.gz 的 rows 檢查程式區塊＝重算結果。每週許可證排程經 scripts/license_adapter.py 的 sync_tables 重排，
scripts/build_license_snapshot.py 結尾也全站重排一次。

第一次換表（--migrate）時另做兩件事（之後頁面上已是程式區塊，不會再發生）：
  - AI 表緊鄰的上一行／下一行裡，只講「表上列了幾筆／前 N 筆／清單可能不完整」的句子（CAPTION）與子句（CAP_CLAUSE）一併拿掉
    （程式表列出證據包全部紀錄並有自己的說明句，舊說明的筆數會跟新表對不上）；同一行其他句子留著；查核紀錄的更正文字所在的句子不動。
  - 錨在被取代的表或說明上的查核紀錄標 status: superseded＋superseded_by（紀錄保留、頁面不顯示框，同 Tw 慣例）。
用法（repo 根目錄，先還原 data/）：
  python3 scripts/sync_license_tables.py [--dry-run] [--migrate] [頁 ...]
  python3 scripts/sync_license_tables.py --captions [--dry-run]   # 市場段落其他位置的舊表說明句（一次性）
  carry_block(old, new)：sync_notes_to_docs.py 整頁重寫時把舊頁的程式區塊移植到新頁。
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_RE = re.compile(r"^## Informazioni sul [Mm]ercato [Ii]taliano\s*$")
HEAD = ["| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |", "|------|------|------|------|"]
SOURCE = "Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime."
NL_NOTE = "«Non più autorizzata»: la confezione non figura più nell'elenco AIFA delle confezioni autorizzate."
PART_NOTE = "I dati contengono solo una parte delle autorizzazioni; l'elenco può essere incompleto."
NONE_LINE = "Nei dati AIFA utilizzati per questo rapporto non risulta alcuna confezione di questo farmaco."
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
NOT_LISTED = "Non più autorizzata"
VALID = "Autorizzata"
SUPERSEDED_BY = "Tabella delle autorizzazioni generata dal programma (scripts/sync_license_tables.py, 2026-11-24, dai dati AIFA)"
NUMW = r"(?:\d+|una|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|undici|dodici|quindici|venti)"
_LST = r"(?:elencat[ei]|mostrat[ei]|riportat[ei]|indicat[ei]|present[ia]t[ei])"
_AUT = r"(?:autorizzazioni|confezioni|prodotti|AIC)"
# 只講表上列了幾筆的整句說明（--migrate 時跟著舊表拿掉；--captions 掃整個市場段落）
CAPTION = re.compile(
    r"^\*?(?:"
    # Di seguito le prime 5. / Si elencano le principali 5: / Sono elencate le prime 5 autorizzazioni. / Nella tabella sono elencate le prime 5 autorizzazioni.
    rf"(?:Di seguito|Si elencano|Si riportano|Sono (?:qui )?{_LST}|(?:Nella tabella|Qui) sono {_LST}|Elencat[ei]|L'elenco (?:mostra|riporta)|La tabella (?:mostra|riporta))"
    rf"(?: sono {_LST})? (?:solo )?(?:le |alcune (?:delle )?)?(?:prime|principali|fino a)(?: {NUMW})?(?: {_AUT}(?: principali)?)?"
    rf"(?: delle {NUMW} {_AUT}(?: \w+)?)?(?: \([^)]*\))?\s*[.:]"
    # Sono mostrate 5 delle 8 autorizzazioni registrate. / L'elenco mostra le prime 5 delle 8 autorizzazioni. / Elencate le prime 5 delle 11 autorizzazioni.
    rf"|(?:Sono (?:qui )?{_LST}|Elencat[ei]|L'elenco (?:mostra|riporta)) (?:le prime )?{NUMW} delle {NUMW} {_AUT}(?: (?:registrate|presenti|disponibili))?\."
    # Principali autorizzazioni: / Le principali sono: / Esempi tra le principali: / Le prime 5: / Elenco delle principali autorizzazioni:
    rf"|(?:Principali (?:autorizzazioni|prodotti)|(?:Le|I) principali(?: autorizzazioni| prodotti)?(?: sono)?|Le autorizzazioni principali(?: sono)?|"
    rf"Alcune delle principali(?: autorizzazioni)?|Elenco delle principali(?: autorizzazioni| {NUMW})?|Esempi(?: di autorizzazioni| tra le principali)?|"
    rf"Le prime {NUMW}(?: sono)?|Di seguito (?:alcune )?(?:delle )?(?:autorizzazioni )?principali(?: autorizzazioni)?|"
    rf"Le principali sono elencate di seguito)(?: \([^)]*\))?\s*[:.]"
    # 只講清單不完整的句子（程式表有自己的 PART_NOTE）
    rf"|L'elenco(?: delle autorizzazioni)?(?: seguente)? (?:può|potrebbe) essere parziale\."
    rf"|L'elenco(?: delle autorizzazioni)? è parziale: (?:i dati (?:compilati|locali) (?:comprendono|contengono) altre autorizzazioni non (?:mostrate|riportate)(?: qui)?|"
    rf"i dati locali sulle autorizzazioni potrebbero non essere completi|sono riportate solo le prime {NUMW})\."
    rf"|L'elenco mostra solo {NUMW} delle autorizzazioni disponibili\."
    r"|I dati contengono solo una parte delle autorizzazioni; l'elenco può essere incompleto\."
    rf"|Di seguito sono elencate fino a {NUMW} autorizzazioni\."
    # 2026-11-24 寬偵測補抓的寫法
    rf"|Si elencano {NUMW} delle autorizzazioni principali\."
    rf"|Le prime {NUMW} autorizzazioni\s*:"
    rf"|L'elenco seguente riporta alcune delle autorizzazioni principali; l'elenco può essere parziale\."
    rf"|Sono elencate {NUMW} delle {NUMW} autorizzazioni valide \(tutte per prodotti a singolo principio attivo\)\."
    rf"|Elenco parziale: sono mostrate {NUMW} delle {NUMW} autorizzazioni, tutte valide\."
    rf"|L'elenco può essere parziale \(almeno {NUMW} autorizzazioni; sono riportate le prime {NUMW}\)\."
    rf"|Le autorizzazioni principali, tutte come medicinale a singolo principio attivo, sono:"
    r")\*?$", re.I)
# 句首只講表上列了幾筆的子句（「L'elenco mostra le prime 5 delle 6 autorizzazioni presenti; il testo …」）：拿掉子句，後半句首字母大寫
CAP_PREFIX = re.compile(
    rf"^(?:L'elenco (?:mostra|riporta) le prime {NUMW}(?: delle {NUMW})? autorizzazioni(?: presenti)?|L'elenco è limitato alle prime {NUMW} autorizzazioni|"
    rf"L'elenco seguente riporta le principali autorizzazioni|L'elenco mostra le principali autorizzazioni tra quelle compilate|"
    rf"Sono elencate le {NUMW} autorizzazioni principali);\s+(?=\w)", re.I)
# 同一句後半只講表上列了幾筆的子句（「…; qui sono elencate le prime 5.」）：只拿掉這個子句
CAP_CLAUSE = re.compile(
    rf"\s*;\s*(?:qui (?:ne )?sono {_LST}(?: le prime)? {NUMW}|la tabella ne (?:mostra|riporta) le prime {NUMW}|ne sono {_LST} le prime {NUMW}|"
    rf"l'elenco mostra le prime {NUMW}|l'elenco seguente ne riporta le principali|l'elenco comprende le principali|"
    rf"di seguito sono riportate {NUMW} autorizzazioni a titolo di esempio)(?=[.:]$)", re.I)
SPLIT = re.compile(r"(?<=[.!?:])\s+(?=[A-ZÀ-Ý*\[(«\"])")


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    t = t if len(t) <= n else t[:n - 1].rstrip() + "…"
    return t.replace("*", "\\*")


def status_label(r):
    if r.get("aifa_not_listed"):
        return NOT_LISTED
    s = re.sub(r"\s*\((?:Classe [^)]*)\)\s*$", "", str(r.get("status") or "")).strip()
    return s or "–"


def table_rows(recs):
    seen, act, rest = set(), [], []
    for r in recs:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        lab = status_label(r)
        row = f"| {k} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'))} | {cell(r.get('license_holder') or r.get('manufacturer'), 60) or '–'} | {lab} |"
        (act if lab == VALID else rest).append(row)
    return act + rest


def rows_of(tf, fc=None):
    """快照用：(表格列, 證據包總數)，跟 process 同一套"""
    rows = table_rows(tf.get("records") or [])
    return rows, max(len(rows), int(tf.get("total_matches") or 0))


def program_block(rows, partial=False):
    if not rows:
        return [NONE_LINE]
    return HEAD + rows + ["", SOURCE] + ([NL_NOTE] if any(r.endswith(f"| {NOT_LISTED} |") for r in rows) else []) \
        + ([PART_NOTE] if partial else [])


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _section(lines):
    a = next((i + 1 for i, l in enumerate(lines) if SEC_RE.match(l)), None)
    if a is None:
        return None, None
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _caption_trim(line, protect=()):
    """拿掉行裡只講表上列了幾筆的整句（CAPTION）與子句（CAP_CLAUSE）：回 (新行, 拿掉的文字)"""
    if not line.strip() or line.startswith(("|", "#", "<!--", "---", ">", "{:")):
        return line, []
    sents = SPLIT.split(line.strip())
    out, gone = [], []
    for x in sents:
        if any(x.strip() in p or p in x for p in protect):  # 查核紀錄的更正文字／錨點所在的句子不動（拿掉會讓更正框消失）
            out.append(x)
            continue
        if CAPTION.match(x.strip()):
            gone.append(x.strip())
            continue
        m = CAP_PREFIX.match(x.strip())
        if m:
            gone.append(m.group(0).strip())
            x = x.strip()[m.end():]
            x = x[:1].upper() + x[1:]
        m = CAP_CLAUSE.search(x)
        if m:
            gone.append(m.group(0).strip())
            x = x[:m.start()] + x[m.end():]
            if x.endswith(":"):  # 「…, tutte valide; l'elenco comprende le principali:」拿掉子句後句尾改句號
                x = x[:-1] + "."
        out.append(x)
    if gone:
        return " ".join(out), gone
    return line, []


def process(text, recs, partial=False, migrate=False, protect=()):
    """回傳 (新內容或 None, 拿掉的文字)。只動市場段落的第一張表（或程式區塊）與 --migrate 時緊鄰的表說明。"""
    lines = text.split("\n")
    a, b = _section(lines)
    if a is None:
        return add_section(text, table_rows(recs), partial), ""
    rows = table_rows(recs)
    blk = wrap(program_block(rows, partial))
    removed = []
    if BEGIN in lines[a:b] and END in lines[a:b]:
        x = lines.index(BEGIN, a)
        y = lines.index(END, x)
        out = lines[:x] + blk + lines[y + 1:]
    else:
        tb = [k for k in range(a, b) if lines[k].startswith("|")]
        if not tb:
            if not rows:
                return None, ""
            out = lines[:a] + [""] + blk + [""] + lines[a:]
        else:
            x = y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            removed += lines[x:y + 1]
            pre, post = lines[:x], lines[y + 1:]
            if migrate:
                k = len(pre) - 1
                while k >= a and not pre[k].strip():
                    k -= 1
                if k >= a:
                    nl, cap = _caption_trim(pre[k], protect)
                    if cap:
                        pre[k] = nl
                        removed += cap
                k = 0
                while k < len(post) and k < b - y - 1 and not post[k].strip():
                    k += 1
                if k < b - y - 1:
                    nl, cap = _caption_trim(post[k], protect)
                    if cap:
                        post[k] = nl
                        removed += cap
            out = pre + [""] + blk + [""] + post
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return (t2 if t2 != text else None), "\n".join(removed)


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁整頁沒有「## Informazioni sul mercato italiano」段落、但證據包有紀錄的，
# 補段落放程式表。位置：標題（小寫比對）為 considerazioni sulla sicurezza／conclusioni e prossimi passi／registro delle verifiche／avvertenza 的段落中最前面一個之前（安全性→結論→查核紀錄→免責聲明）。
# noindex 頁與證據包沒有紀錄的頁不補。
ADD_SEC = "## Informazioni sul mercato italiano"
ADD_BEFORE = ('considerazioni sulla sicurezza', 'conclusioni e prossimi passi', 'registro delle verifiche', 'avvertenza')


def is_public(text):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    return not re.search(r"^noindex:\s*true", fm, re.M)


def add_section(text, rows, partial=False):
    if not rows or not is_public(text):
        return None
    lines = text.split("\n")
    heads = {m.group(1).lower(): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    k = at - 1
    while k > 0 and not lines[k].strip():
        k -= 1
    if lines[k].strip() == "<!-- review:begin log -->":  # 查核紀錄段的標題在 log 區塊裡：段落放在區塊之前（否則套用查核紀錄時會被當成 log 區塊的內容）
        at = k
    sec = [ADD_SEC, ""] + wrap(program_block(rows, partial)) + [""]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))
    return t2 if t2 != text else None


def trim_section_captions(text, protect=()):
    """市場段落裡（不限緊鄰表）只講舊表列了幾筆的句子拿掉（--captions）。回傳 (新內容或 None, 拿掉的文字)"""
    lines = text.split("\n")
    a, b = _section(lines)
    if a is None or BEGIN not in lines[a:b]:
        return None, ""
    gone = []
    i0, i1 = lines.index(BEGIN, a), lines.index(END, a)
    inbox = False
    for k in range(a, b):
        if lines[k].startswith("<!-- review:begin"):
            inbox = True
        if lines[k].startswith("<!-- review:end"):
            inbox = False
            continue
        if inbox or i0 <= k <= i1:
            continue
        nl, cap = _caption_trim(lines[k], protect)
        if cap:
            lines[k] = nl
            gone += cap
    if not gone:
        return None, ""
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)), "\n".join(gone)


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁市場段落（取代新頁段落的第一張表）；舊頁沒有就原樣"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = new_text.split("\n")
    a, b = _section(lines)
    if a is None:
        return new_text
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if BEGIN in lines[a:b]:
        x = lines.index(BEGIN, a)
        out = lines[:x] + blk + lines[lines.index(END, x) + 1:]
    elif not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        out = lines[:x] + [""] + blk + [""] + lines[y + 1:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def bundle_for(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def _skip(raw):
    h = raw[:3000]
    return "layout: id_redirect" in h or 'http-equiv="refresh"' in h


def supersede(removed_by_page, today=None):
    """--migrate 時：錨在拿掉的文字上、新頁面上也找不到的查核紀錄標 superseded（紀錄保留）。回傳標記的 id"""
    data = ROOT / "docs/_data/drug_reviews.json"
    doc = json.loads(data.read_text(encoding="utf-8"))
    today = today or dt.date.today().isoformat()
    marked = []
    for r in doc["records"]:
        stem = r["file"][:-3]
        gone = removed_by_page.get(stem)
        if not gone or r.get("status") or r.get("action") not in ("correct", "annotate", "rereview"):
            continue
        page = (ROOT / "docs/_drugs" / r["file"]).read_text(encoding="utf-8")
        page = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", page, flags=re.S)
        page = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", page, flags=re.S)  # 程式表裡的號碼不算錨點
        keys = [x for x in (r.get("anchor"), r.get("replacement"), r.get("claim")) if x and x.strip()]
        if not keys:
            continue
        loc = r.get("anchor") or (r.get("replacement") if r["action"] == "correct" else r.get("claim")) or r.get("claim")
        if loc and loc.strip() and loc in page:
            continue  # 錨點還在頁面上：照舊套用
        gl = [g.strip() for g in gone.split("\n") if g.strip()]
        if any(k in gone or any(k.strip() in g for g in gl) or any(g in k for g in gl) for k in keys):
            r["status"] = "superseded"
            r["superseded_by"] = SUPERSEDED_BY
            r["superseded_on"] = today
            marked.append(r["id"])
    if marked:
        data.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return marked


def _protect():
    out = {}
    f = ROOT / "docs/_data/drug_reviews.json"
    if f.exists():
        for r in json.loads(f.read_text(encoding="utf-8")).get("records", []):
            if r.get("status"):
                continue
            out.setdefault(r["file"][:-3], []).extend(x for x in (r.get("replacement"), r.get("anchor")) if x and x.strip())
    return out


def resync(stems=None, dry=False, migrate=False):
    """回傳 ([(頁, 欄位, 前值, 後值)], {頁: 拿掉的文字})"""
    changed, removed = [], {}
    prot = _protect() if migrate else {}
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if stems is not None and page.stem not in stems:
            continue
        b = bundle_for(page.stem)
        if b is None:
            continue
        raw = page.read_bytes().decode("utf-8")
        if _skip(raw):
            continue
        crlf = "\r\n" in raw[:500]
        tf = b.get("tfda") or {}
        recs = tf.get("records") or []
        rows, total = rows_of(tf)
        new, gone = process(raw.replace("\r\n", "\n"), recs, total > len(rows), migrate, prot.get(page.stem, ()))
        if new is None:
            continue
        changed.append((page.stem, "Tabella delle autorizzazioni (programma)", "", f"{len(rows)} righe"))
        if gone:
            removed[page.stem] = gone
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed, removed


def main(argv):
    dry, migrate = "--dry-run" in argv, "--migrate" in argv
    only = {a for a in argv if not a.startswith("--")} or None
    if "--captions" in argv:
        prot, n, rm = _protect(), 0, {}
        for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
            if only and page.stem not in only:
                continue
            raw = page.read_text(encoding="utf-8")
            if _skip(raw):
                continue
            new, gone = trim_section_captions(raw, prot.get(page.stem, ()))
            if new:
                n += 1
                rm[page.stem] = gone
                print(f"  {page.stem}：{gone}")
                if not dry:
                    page.write_text(new, encoding="utf-8")
        print(f"市場段落舊表說明句拿掉 {n} 頁")
        if not dry and rm:
            print(f"錨在拿掉的說明句上的查核紀錄標 superseded：{len(supersede(rm))} 筆")
        return
    changed, removed = resync(only, dry, migrate)
    print(f"許可證表（程式）改 {len(changed)} 頁" + (f"；拿掉舊表／表說明的頁 {len(removed)}" if migrate else ""))
    if migrate:
        caps = {k: [g for g in v.split("\n") if g and not g.startswith("|")] for k, v in removed.items()}
        for k, v in caps.items():
            if v:
                print(f"  說明句 {k}：{v}")
    if migrate and not dry:
        ids = supersede(removed)
        print(f"錨在被取代的表或表說明上的查核紀錄標 superseded：{len(ids)} 筆")
        for i in ids:
            print("  ", i)


if __name__ == "__main__":
    main(sys.argv[1:])
