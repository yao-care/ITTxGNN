---
layout: default
title: Levothyroxine
parent: Solo previsione del modello (L5)
nav_order: 269
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-28
description: "Levothyroxine: nuova indicazione prevista, ipoplasia/aplasia renale (livello di evidenza L5). Indicazione originale: Ipotiroidismo"
---

# Levothyroxine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

## Levotiroxina: dall'ipotiroidismo all'ipoplasia/aplasia renale
{: .text-alpha }

## Riepilogo in una frase

La levotiroxina è un ormone tiroideo sintetico (T4), utilizzato originariamente nel trattamento dell'ipotiroidismo e delle patologie tiroidee correlate.
Il modello TxGNN ne prevede una possibile efficacia per l'**ipoplasia/aplasia renale**, ma **non sono presenti sperimentazioni cliniche né pubblicazioni** a sostegno di questa direzione: si tratta di una previsione basata solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipotiroidismo (relazione registrata nel grafo di conoscenza; il testo delle indicazioni nelle autorizzazioni AIFA non è disponibile) |
| Nuova indicazione prevista | Ipoplasia/aplasia renale |
| Punteggio di predizione TxGNN | 0,9967 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | Almeno 20 (l'elenco potrebbe essere parziale) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In base alle conoscenze disponibili, la levotiroxina agisce come ligando dei recettori degli ormoni tiroidei alfa (THRA) e beta (THRB), ed è usata nella sostituzione ormonale tiroidea.

Esiste solo un legame biologico generico: gli ormoni tiroidei partecipano allo sviluppo fetale e alla maturazione renale (nefrogenesi, maturazione tubulare). Tuttavia l'ipoplasia/aplasia renale è una malformazione strutturale congenita, generalmente legata a varianti genetiche (ad es. PAX2, HNF1B, RET) che agiscono nelle prime fasi dell'embriogenesi. La levotiroxina somministrata dopo la nascita non dovrebbe invertire un'agenesia strutturale.

L'elevato punteggio TxGNN (0.9967) deriva dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate (fenotipi o geni correlati alla tiroide e allo sviluppo), non evidenza biologica, più che un reale segnale terapeutico.

Altre previsioni nella stessa lista (agenesia renale bilaterale, sequenza di Potter, complesso di Carney) sono anch'esse prive di evidenze cliniche. Il complesso di Carney è la più plausibile dal punto di vista biologico, per il coinvolgimento tiroideo e la via cAMP/PKA, ma resta solo un'ipotesi.

## Evidenze da sperimentazioni cliniche

Al momento non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

Sono presenti almeno 20 autorizzazioni valide per prodotti monocomponente; l'elenco potrebbe essere parziale. Di seguito le principali 5 (il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati compilati).

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 024402125 | EUTIROX 50 cpr 50 mcg | Merck Serono SpA | Valida |
| 049815095 | LEVOTIROXINA 50 cpr 125 mcg | Abdi Farma GmbH | Valida |
| 046860058 | LEVOTIRSOL soluzione orale 30 flaconcini 1 ml 88 mcg | IBSA Farmaceutici Italia Srl | Valida |
| 046021414 | LEVOTIROXINA 50 cpr 125 mcg | DOC Generici Srl | Valida |
| 034368086 | TIROSINT soluzione orale 30 flaconcini 1 ml 50 mcg/ml | IBSA Farmaceutici Italia Srl | Valida |

## Considerazioni sulla sicurezza

Le seguenti controindicazioni derivano da relazioni farmaco-malattia registrate nel grafo di conoscenza (non dal testo del foglio illustrativo):

- **Malattie cardiovascolari e metaboliche:** ipertensione, coronaropatia, infarto del miocardio, diabete mellito, chetoacidosi diabetica.
- **Malattie ossee:** osteoporosi, osteoporosi post-menopausale.
- **Insufficienze ipofisarie e ipogonadismi:** ipopituitarismo, deficit di ormone della crescita, ipogonadismo ipogonadotropo, sindrome di Kallmann, sindrome di Sheehan e forme correlate.
- **Altro:** malattie del timo.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo AIFA.

## Conclusione e passi successivi

**Decisione: Hold**

**Motivazione:**
Non esistono studi clinici né pubblicazioni sull'uso della levotiroxina nell'ipoplasia/aplasia renale. Il punteggio deriva dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate, non evidenza biologica; non è plausibile che l'ormone inverta una malformazione strutturale congenita.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e un'analisi del legame meccanicistico con lo sviluppo renale.
- Avvertenze e controindicazioni dal foglio illustrativo AIFA.
- Evidenze precliniche o cliniche che studino direttamente la malattia prevista.
- Una valutazione dei rischi di sovradosaggio (effetti cardiaci e ossei) nella popolazione interessata.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

