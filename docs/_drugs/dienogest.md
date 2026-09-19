---
layout: default
title: Dienogest
parent: Solo previsione del modello (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Dienogest
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# DIENOGEST: Candidato di riposizionamento — Dati insufficienti per valutazione completa

## Riassunto sintetico

Dienogest (DrugBank DB09123) è un progestinico sintetico; tuttavia, l'Evidence Pack attuale non contiene alcun record di indicazione originaria dal database normativo e **nessuna nuova indicazione predetta da TxGNN**, rendendo una valutazione standard di riposizionamento impossibile a questo stadio. I gap critici nei dati relativi al meccanismo d'azione, agli avvertimenti di sicurezza e alla storia normativa devono essere risolti prima di poter trarre alcuna conclusione basata sull'evidenza.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originaria | Non disponibile (nessun record normativo di Taiwan trovato) |
| Nuova indicazione predetta | Non disponibile (predizioni TxGNN non ancora generate) |
| Punteggio di predizione TxGNN | — |
| Livello di evidenza | L5 — Predizione del modello non ancora eseguita; nessuno studio di supporto recuperabile |
| Stato mercato Taiwan | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Sospensione** |

---

## Perché questa predizione è ragionevole?

Nessuna indicazione predetta da TxGNN è disponibile in questo Evidence Pack (`predicted_indications: []`). Senza una malattia target, una logica meccanicistica non può essere costruita.

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili. Basandosi sul record DrugBank DB09123, Dienogest è classificato come un progestinico (progestina sintetica di quarta generazione). La sua attività farmacologica è mediata dall'agonismo del recettore del progesterone, ed è ampiamente utilizzato nei mercati europei e asiatici per l'endometriosi e la contraccezione ormonale — sebbene nessuna di queste indicazioni compaia nel database normativo di Taiwan interrogato.

**Per procedere con questa sezione**, la pipeline di predizione TxGNN deve prima essere eseguita e una malattia target deve essere confermata prima che qualsiasi ponte meccanicistico possa essere valutato.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato in questo Evidence Pack. Ciò è dovuto al fatto che nessuna indicazione predetta è stata identificata; una volta confermata una malattia target, una query su ClinicalTrials.gov può essere eseguita.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata disponibile. L'indicazione target deve essere specificata prima che una query su PubMed possa produrre risultati significativi.

---

## Informazioni di mercato di Taiwan

Nessuna autorizzazione trovata. La query TFDA (2026-03-29) ha restituito 0 record per DIENOGEST.

---

## Considerazioni di sicurezza

Fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

Nessun dato di interazione farmacologica è stato trovato nella query del database DDI (2026-03-29). L'analisi del foglio illustrativo TFDA è stata registrata come riuscita (ID query 4), ma i campi di avvertimento e controindicazione estratti non sono disponibili in questa versione dell'Evidence Pack.

---

## Conclusione e prossimi passi

**Decisione: Sospensione**

**Razionale:**
L'Evidence Pack per Dienogest manca di tutti e tre gli elementi richiesti per una valutazione di riposizionamento: un'indicazione target predetta da TxGNN, dati del meccanismo d'azione e contenuto di sicurezza/normativo. Non esiste alcuna base su cui valutare la plausibilità di efficacia, la forza dell'evidenza o il profilo di rischio in questo momento.

**Per procedere, è necessario quanto segue:**

1. **Eseguire la pipeline di predizione TxGNN** — Generare indicazioni candidate classificate per DB09123 in modo che una malattia target possa essere selezionata
2. **Recuperare il MOA dall'API DrugBank** — Popolare `original_moa` per abilitare la logica meccanicistica (Data Gap DG002, gravità: Alta)
3. **Scaricare e analizzare il PDF del foglio illustrativo TFDA** — Estrarre avvertimenti e controindicazioni per sbloccare la valutazione di sicurezza (Data Gap DG001, gravità: Bloccante)
4. **Confermare l'indicazione originaria** — Interrogare i record DrugBank o WHO INN per popolare `original_indications` (attualmente vuoto)
5. **Ri-eseguire la generazione dell'Evidence Pack** (versione target: v5) — Una volta risolti i gap di cui sopra, inviare nuovamente per una classificazione completa L1–L5 dell'evidenza e una raccomandazione Go/Hold/Proceed

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

