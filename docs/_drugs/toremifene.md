---
layout: default
title: Toremifene
parent: Solo previsione del modello (L5)
nav_order: 444
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Toremifene: nuova indicazione prevista, HIV infectious disease (infezione da HIV) (livello di evidenza L5). Indicazione originale: Non disponibile nei dati AIFA (testo dell'indicazione vuoto)"
monitor_inn: "TOREMIFENE"
predicted_indications: ["HIV infectious disease"]
---

# Toremifene
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Toremifene: dal carcinoma mammario all'infezione da HIV (predizione del modello)
{: .text-alpha }

## Sintesi

Il toremifene è un modulatore selettivo del recettore degli estrogeni (SERM), noto come farmaco per il carcinoma mammario. Il modello TxGNN lo predice come potenzialmente efficace per l'**infezione da HIV**, ma il supporto è molto debole: **nessuno studio clinico** registrato e **1 pubblicazione** preclinica, che riguarda l'attività antifungina contro *Cryptococcus* e non l'attività anti-HIV.

Nota: i dati compilati per questo report non riportano un'indicazione approvata in Italia. L'indicazione originale sopra citata deriva dalla conoscenza generale del farmaco e non da dati AIFA.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati AIFA (testo dell'indicazione vuoto) |
| Nuova indicazione predetta | HIV infectious disease (infezione da HIV) |
| Punteggio di predizione TxGNN | 0,9941 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione può essere ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Toremifene (traduzione non ufficiale): «Toremifene è un derivato trifeniletilenico non steroideo. Toremifene si lega ai recettori degli estrogeni e può esercitare attività estrogenica, antiestrogenica o entrambe, a seconda della durata del trattamento, della specie animale, del sesso, dell'organo bersaglio o dell'endpoint selezionato.» Testo originale in inglese: "Toremifene is a nonsteroidal triphenylethylene derivative. Toremifene binds to estrogen receptors and may exert estrogenic, antiestrogenic, or both activities, depending upon the duration of treatment, animal species, gender, target organ, or endpoint selected." ([DailyMed: Fareston (toremifene citrate) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5), versione del 2024-11-13; consultato il 2026-11-19). Si sa che il toremifene è un SERM, cioè un antagonista del recettore degli estrogeni, ma non è possibile costruire un ragionamento meccanicistico basato sulle annotazioni dei bersagli farmacologici.

Il punteggio TxGNN è molto elevato (0,9941), ma deriva solo da una predizione basata su rete di conoscenza. L'unica pubblicazione disponibile (2014) è uno studio preclinico che mostra come gli antagonisti del recettore degli estrogeni, tra cui il toremifene, legano proteine con dominio EF-hand (come la calmodulina) e hanno attività fungicida contro *Cryptococcus neoformans*, con sinergia con fluconazolo e amfotericina B in vitro.

Il legame con l'HIV è solo indiretto: la meningite criptococcica è un'importante infezione opportunistica nei pazienti con HIV/AIDS avanzato. Tuttavia lo studio non dimostra alcuna attività anti-HIV (effetto antivirale, soppressione virale o ricostituzione immunitaria). Il collegamento riguarda una coinfezione, non l'HIV in sé. Un'eventuale razionale di riposizionamento andrebbe definito separatamente, ad esempio come terapia antifungina adiuvante nella criptococcosi associata a HIV, e non come trattamento dell'HIV.

---

## Evidenza dagli studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Preclinico (in vitro / meccanicistico) | mBio | Gli antagonisti del recettore degli estrogeni (tamoxifene, toremifene) sono fungicidi contro *Cryptococcus*, si legano a proteine EF-hand e sono sinergici con fluconazolo e amfotericina B |

---

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 029914013 | FARESTON\*30 cpr 60 mg | ORION CORPORATION | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

---

## Cytotoxicity

| Voce | Contenuto |
|------|------|
| Classificazione citotossica | Terapia ormonale antineoplastica (SERM), non chemioterapico citotossico convenzionale |
| Rischio di mielosoppressione | Si rimanda alle avvertenze e precauzioni del foglio illustrativo; tra le malattie associate nella rete di conoscenza compaiono leucopenia e trombocitopenia |
| Classificazione emetogenica | Si rimanda alle avvertenze e precauzioni del foglio illustrativo |
| Parametri da monitorare | Emocromo, funzionalità epatica e renale, elettroliti (potassio, calcio), ECG per l'intervallo QT |
| Protezione nella manipolazione | Si rimanda alle avvertenze e precauzioni del foglio illustrativo |

---

## Considerazioni di sicurezza

Le informazioni su avvertenze e controindicazioni del foglio illustrativo AIFA non sono disponibili. Si rimanda al foglio illustrativo.

- **Controindicazioni/condizioni a rischio dalla rete di conoscenza (TxGNN/PrimeKG, non dal testo del foglio illustrativo)**: sindrome del QT lungo (anche familiare), torsione di punta, trombocitopenia, deficit di potassio, ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, leucopenia, iperplasia endometriale.
- **Interazioni farmacologiche** (100 interazioni totali, banca dati DDInter); tra le principali di livello **maggiore**: desametasone, claritromicina, levofloxacina, dolasetron, palonosetron, acido picosolfurico, polietilenglicole con elettroliti, solfato di sodio. Livello moderato, ad esempio: famotidina, pioglitazone, loperamide, aprepitant, cimetidina, miconazolo, nateglinide. Molte interazioni maggiori sono compatibili con un rischio additivo di prolungamento del QT o con alterazioni elettrolitiche.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (livello L5). L'unica pubblicazione è preclinica e riguarda l'attività antifungina, non anti-HIV. I dati di sicurezza del foglio illustrativo mancano.

<!-- review:begin it-lic-20261106-toremifene-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Inoltre l'unica autorizzazione italiana è cancellata e i dati di sicurezza del foglio illustrativo mancano.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-toremifene-1 -->

**Per procedere sono necessari:**
- Dati di sicurezza dal foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente bloccanti per lo screening di sicurezza
- Dati sul meccanismo d'azione (ad esempio da DrugBank)
- Evidenze dirette di attività anti-HIV, oppure ridefinizione dell'ipotesi (ad esempio terapia antifungina adiuvante nella criptococcosi associata a HIV) con studi in vivo e clinici
- Valutazione del rischio di prolungamento del QT e delle interazioni maggiori nella popolazione HIV in terapia combinata
- Chiarimento dello stato regolatorio e della disponibilità del prodotto in Italia

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «noltre l'unica autorizzazione italiana è cancellata e i» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Fareston (toremifene citrate) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2cab8dd1-3a10-48e6-86ce-0e5275ed49e5) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

