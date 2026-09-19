---
layout: default
title: Buserelin
parent: Solo previsione del modello (L5)
nav_order: 43
evidence_level: L5
indication_count: 5
---

# Buserelin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Buserelin: da Condizioni Ormonodipendenti a Ipertricosi

## Riassunto in una frase

Buserelin è un agonista sintetico del GnRH (ormone di rilascio della gonadotropina) utilizzato clinicamente per sopprimere la produzione di ormoni sessuali in condizioni ormono-sensibili, sebbene nessuna indicazione approvata sia formalmente registrata nel dataset attuale.
Il modello TxGNN prevede che potrebbe essere rilevante per l'**Ipertricosi**, con **0 trial clinici** e **1 pubblicazione** che attualmente toccano quest'area — rendendo la base di prove estremamente limitata.
Data la débole razionale meccanicistica e l'assenza di prove cliniche dirette, questo candidato attualmente non soddisfa la soglia per lo sviluppo attivo.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originaria | Nessuna indicazione approvata registrata |
| Indicazione nuova prevista | Ipertricosi |
| Punteggio di predizione TxGNN | 99.75% |
| Livello di prove | L5 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | In sospeso |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili in questo dataset. Basandosi su informazioni farmacologiche note, Buserelin è un agonista del GnRH: quando somministrato continuamente, riduce i recettori del GnRH ipofisari, sopprimendo così la secrezione di LH e FSH e riducendo drasticamente la produzione di ormoni sessuali a valle (testosterone ed estrogeno). Questo meccanismo è la base del suo utilizzo in condizioni ormono-sensibili come il cancro alla prostata e l'endometriosi.

Il problema principale di questa predizione è una mancanza concettuale tra il meccanismo del farmaco e la malattia target. L'**Ipertricosi** — crescita eccessiva di peli che si verifica in una distribuzione generalizzata e non strutturata — è largamente non androgeno-dipendente. Questo la distingue fondamentalmente dall'irsutismo (crescita eccessiva di peli strutturata e androgeno-dipendente nelle donne), dove gli agonisti del GnRH hanno effettivamente una razionale teorica e pratica. L'ipertricosi può sorgere da mutazioni genetiche, farmaci, fenomeni paraneoplastici o condizioni sistemiche — nessuna delle quali è affrontata dalla soppressione dell'asse GnRH.

L'unica pubblicazione a supporto (un rapporto di caso del 2019 sulla sindrome di Cantu) descrive l'ipertricosi come una caratteristica di un raro disturbo genetico con coinvolgimento ipofisario. Non valuta Buserelin come trattamento né propone alcun intervento ormonale per il fenotipo dei peli. È probabile che il modello TxGNN abbia rilevato una co-occorrenza superficiale tra i segnali dell'asse GnRH e i fenotipi di crescita dei peli, ma la razionale biologica per l'utilizzo attivo di Buserelin nel trattamento dell'ipertricosi rimane non supportata.

---

## Evidenza da trial clinici

Attualmente nessun trial clinico correlato è registrato.

---

## Evidenza da letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|---------|----------------------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Rapporto di caso | *Endocrinology, Diabetes & Metabolism Case Reports* | Descrive un paziente con sindrome di Cantu (osteocondrodisplasia ipertricotica) con deficit multipli di ormoni ipofisari; supporta il monitoraggio endocrino routinario in questa rara condizione genetica — non valuta Buserelin come trattamento per l'ipertricosi |

---

## Informazioni sul mercato italiano

Buserelin attualmente non dispone di autorizzazioni approvate in Italia. Non è commercializzato e nessun record di licenza è archiviato in questo dataset.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusione e passi successivi

**Decisione: In sospeso**

**Razionale:**
Nonostante un alto punteggio di predizione TxGNN (99.75%), la razionale biologica è criticamente débole — l'ipertricosi è predominantemente non androgeno-dipendente, il che significa che il meccanismo principale di Buserelin di soppressione del GnRH non ha una via terapeutica plausibile per questa indicazione. Non esistono trial clinici e l'unica pubblicazione associata è un rapporto di caso indiretto non correlato all'uso di Buserelin.

**Per procedere è necessario quanto segue:**
- Dati dettagliati del meccanismo d'azione (MOA) recuperati da DrugBank o da fonti di farmacologia primaria
- Indicazioni originali approvate confermate via EMA o foglio illustrativo TFDA
- Profilo di sicurezza completo incluso avvertenze chiave, controindicazioni e interazioni farmacologiche
- Prove precliniche o meccanicistiche che collegano specificamente la soppressione del GnRH alla fisiopatologia dell'ipertricosi (attualmente assenti)
- Se si considera il proseguimento, una revisione della letteratura focalizzata su sottotipi di ipertricosi androgeno-dipendenti dove un intervento ormonale potrebbe essere giustificato

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

