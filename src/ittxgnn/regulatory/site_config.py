"""本站查核機制的在地設定（2026-11-12 建；核心流程比照 TwTxGNN、UsTxGNN，程式在同目錄與 scripts/）。

頁面上的查核框、查核紀錄表、說明文字用本站語言（義大利文）；依據是 AIFA 包裝清單（confezioni）。
改這裡的字樣後跑 python3 scripts/apply_drug_reviews.py 重套，gate（scripts/check_seo_docs.py）會檢查。
COMMITS／REGEN_COMMITS：2026-10-31～11-06 正文的許可證刪改提交與期間內 AI 重產報告的提交（scripts/reviews_from_edits.py --git 用）。
"""
import json as _json

C = _json.loads(r"""{
 "SITE": "ITTxGNN",
 "ID_PREFIX": "it",
 "SNAPSHOT": "it_licenses.json.gz",
 "HEADER_LABEL": "Livello di evidenza",
 "OVERVIEW_LABELS": [
  "Livello di evidenza",
  "Livello di Evidenza"
 ],
 "WITHDRAWN_RE": "Ritirat[oa]",
 "DESC_LEVEL_RE": "livello di evidenza (L[1-5]|N/A)",
 "DESC_LEVEL_FMT": "livello di evidenza {lv}",
 "NA_DESC": "solo usi noti",
 "HEADER_RULE_NOTE": "2026-11-12 實測：有 Quick Overview 等級的 420 頁，頁首全部等於第一個等級（整格取最高會有 6 頁不同）",
 "MARKET_RE": "[Mm]ercato",
 "ID_RE": "\\b\\d{9}\\b",
 "PROSE_ID_RE": null,
 "ORIGINAL_LABELS": [
  "Indicazione originale",
  "Indicazione originaria"
 ],
 "ORIGINAL_NONE_RE": "^\\s*(non riportat|non disponibil|nessuna|n/a|–|-)",
 "ORIGINAL_SPLIT_RE": "[;,/()]+|\\be\\b|\\bo\\b",
 "ORIGINAL_NOTE": "2026-11-12：證據包的許可證紀錄來自 AIFA 包裝清單（confezioni）；可比對頁數以程式輸出為準",
 "COMMITS": [
  "59dcf297",
  "f2335681",
  "dfe5baa8"
 ],
 "REGEN_COMMITS": [
  "e168c43e",
  "adff3cfb",
  "23365207",
  "e81fadc0",
  "478c7121",
  "b892760c",
  "62dddc94"
 ],
 "SOURCES": [
  {
   "title": "AIFA – Elenco confezioni (open data)",
   "url": "https://drive.aifa.gov.it/farmaci/confezioni.csv"
  }
 ],
 "PROGRAM_LINE_RE": null,
 "CLASSIFY": [
  [
   "tw",
   "Taiwan|TFDA|台灣|臺灣"
  ],
  [
   "combo",
   "monocomponente|in associazione|combinazion|principio attivo singolo"
  ],
  [
   "cancel",
   "revoc|annullat|sospes|ritirat|non (?:è |sono )?(?:più )?(?:commercializzat|autorizzat|valid)|cessat|decadut|cancellat"
  ],
  [
   "count",
   "\\b\\d+\\b[^.;]{0,40}(?:autorizzazion|AIC|confezion|prodott)|(?:autorizzazion|AIC|confezion)[^.;]{0,30}\\b\\d+\\b|\\b(?:tutti|tutte|entrambi|entrambe)\\b[^.;]{0,30}(?:autorizzazion|valid)|\\bvalid[ei]\\b"
  ],
  [
   "product",
   "\\b(?:sotto forma|forma farmaceutica|compress|capsul|iniettabil|pomata|in commercio|commercializzat)"
  ]
 ],
 "T": {
  "label": {
   "correct": "Correzione di verifica",
   "annotate": "Nota di verifica",
   "rereview": "Revisione in sospeso",
   "rereview_result": "Esito della revisione"
  },
  "action": {
   "correct": "Corretto",
   "annotate": "Nota aggiunta",
   "rereview": "Segnato per la revisione",
   "section": "Sezione con fonti aggiunta",
   "rereview_result": "Revisione completata",
   "header_level": "Livello di evidenza dell'intestazione ricalcolato dalla panoramica rapida",
   "description_level": "Livello di evidenza della descrizione allineato all'intestazione"
  },
  "verdict": {
   "maintain": "Confermato",
   "downgrade": "Declassato",
   "upgrade": "Innalzato",
   "withdraw": "Ritirato"
  },
  "log_head": "## Registro delle verifiche",
  "disclaimer_re": "Avvertenza",
  "log_cols": [
   "Data di verifica",
   "Voce",
   "Intervento",
   "Fonte"
  ],
  "level_same": "livello di evidenza {o} invariato",
  "level_change": "livello di evidenza {o} → {n}",
  "orig": "Testo originale: «{x}»",
  "table_updated": "Le voci «{labels}» di questa pagina sono state aggiornate secondo l'esito della revisione; i valori originali sono riportati nel registro qui sotto.",
  "decision": "Raccomandazione sulla decisione: {x}",
  "source": "Fonte",
  "rereviewed": "Segnato per la revisione → rivisto (vedi l'esito della revisione)",
  "hdr": "Livello di evidenza dell'intestazione ricalcolato dalla panoramica rapida ({o} → {n})",
  "hdr_withdraw": "Previsione principale ritirata in revisione; livello di evidenza dell'intestazione ricalcolato ({o} → {n})",
  "now_listed": ", ora elencato in «{x}»",
  "rr": "Revisione: {v}, {c}",
  "tu": "; {l}: «{a}» → «{b}»",
  "desc": "Descrizione della pagina: «{a}» sostituito con «{b}» (segue l'intestazione; resto del testo invariato, originale conservato nel registro)",
  "revised": " (rivisto il {d}; versione precedente conservata nel registro)",
  "superseded": "Sostituito dalla tabella delle autorizzazioni generata dal programma (prima: {a})",
  "regen": "Non più presente dopo la rigenerazione del rapporto ({d}: {n}; prima: {a})",
  "program": "Non più presente dopo una correzione del programma ({d}: {n}; prima: {a})",
  "withdrawn": "Verifica ritirata ({d}: {n}; prima: {a})",
  "intro": "Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.",
  "intro_header": "Di seguito il registro delle verifiche di questa pagina; il livello di evidenza dell'intestazione segue la panoramica rapida. Le previsioni del modello, la tabella riepilogativa e le conclusioni non sono state riscritte.",
  "intro_rr": "Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base e il testo della previsione non è stato riscritto; livelli di evidenza e decisioni sono stati modificati solo da un esito di revisione (declassamento, innalzamento o ritiro), con i valori originali qui sotto.",
  "figures": "Nei dati (AIFA, elenco delle confezioni autorizzate) risultano {total} autorizzazioni per questo farmaco, di cui {valid} valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato.",
  "data_as_of": "AIFA, elenco delle confezioni autorizzate, al {date}",
  "notes": {
   "rewrite": "Corretto: l'affermazione non corrispondeva ai dati delle autorizzazioni ({d}) ed è stata sostituita dal testo attuale.",
   "tw": "Rimosso: testo residuo del modello taiwanese (TFDA), non pertinente a questa pagina.",
   "combo": "Rimosso: l'indicazione di prodotti monocomponente o in associazione non corrispondeva ai dati delle autorizzazioni ({d}).",
   "cancel": "Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni ({d}).",
   "count": "Rimosso: il numero o lo stato delle autorizzazioni indicato non corrispondeva ai dati delle autorizzazioni ({d}).",
   "product": "Rimosso: la descrizione dei prodotti non corrispondeva ai dati delle autorizzazioni ({d}).",
   "generic": "Rimosso: l'affermazione contraddiceva i dati delle autorizzazioni ({d})."
  },
  "notes_with_figures": [
   "cancel",
   "count",
   "product",
   "generic"
  ],
  "summary": "Rimosso: «{x}»",
  "regen_note": "il rapporto è stato rigenerato a novembre 2026 e non contiene più questa affermazione"
 }
}""")
