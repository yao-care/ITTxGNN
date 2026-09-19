---
layout: default
title: Acamprosato
parent: Solo previsione del modello (L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# Acamprosato
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **0** 
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

# Acamprosato: Rapporto di Valutazione della Ripropositura del Farmaco

## Riassunto in una frase

L'acamprosato (Acamprosate) è un farmaco utilizzato storicamente per il mantenimento dell'astinenza nei pazienti dipendenti dall'alcol, anche se nel pacchetto di prove attuale non sono registrate indicazioni originali. Nessuna nuova indicazione è stata predetta dal modello TxGNN al momento, e nessuna prova da trial clinico o letteratura è disponibile per supportare la ripropositura. **Questo candidato non può procedere alla valutazione fino a quando i divari critici di dati non saranno risolti.**

---

## Panoramica rapida

| Elemento | Contenuto |
|------|------|
| Indicazione originale | Non disponibile (nessuna indicazione approvata registrata) |
| Nuova indicazione predetta | Nessuna — nessuna predizione TxGNN generata |
| Punteggio di predizione TxGNN | N/A |
| Livello di evidenza | L5 (Nessuna predizione del modello o studi di supporto disponibili) |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **In sospeso** |

---

## Perché questa predizione è ragionevole?

Attualmente, nessuna predizione TxGNN è stata generata per l'acamprosato, quindi una valutazione della plausibilità meccanicistica non può essere eseguita.

I dati dettagliati del meccanismo d'azione (MOA) non sono disponibili nel pacchetto di prove. Basandosi su informazioni pubblicamente note, si ritiene che l'acamprosato moduli la neurotrasmissione glutammatergica, agendo principalmente sui recettori NMDA e potenzialmente ripristinando l'equilibrio tra la neurotrasmissione eccitatoria e inibitoria alterato dall'esposizione cronica all'alcol. Il suo uso clinico stabilito è nel supporto dell'astinenza dall'alcol nei pazienti dipendenti dall'alcol che hanno già subito la disintossicazione.

Senza una nuova indicazione predetta da TxGNN, non è possibile valutare la relazione meccanicistica tra l'uso originale e qualsiasi potenziale indicazione riproposta. Questo rapporto dovrebbe essere riesaminato una volta che le predizioni TxGNN diventino disponibili e il divario di dati MOA (DG002) sia risolto tramite DrugBank.

---

## Evidenza da trial clinici

Attualmente nessun trial clinico correlato registrato per alcuna nuova indicazione predetta — nessuna predizione TxGNN è stata generata per questo farmaco.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile — nessuna predizione TxGNN è stata generata per questo farmaco.

---

## Informazioni sul mercato italiano

L'acamprosato è attualmente **non commercializzato** in Italia. Nessuna autorizzazione AIFA è stata trovata nel database normativo (0 licenze registrate).

---

## Considerazioni di sicurezza

> Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.
>
> **Nota:** Sono stati identificati i seguenti divari critici di dati:
> - **Avvisi/controindicazioni del foglio illustrativo TFDA** (Gravità: Bloccante) — non è possibile completare la valutazione della sicurezza della Fase 1 senza questi dati. Rimedio: scaricare e analizzare il PDF del foglio illustrativo dal sito web TFDA.
> - **Interazioni farmaco-farmaco**: Nessuna interazione trovata nella query del database (data della query: 2026-03-29).

---

## Conclusione e prossimi passi

**Decisione: In sospeso**

**Razionale:**
Nessuna indicazione predetta TxGNN è stata generata per l'acamprosato, e il farmaco non è commercializzato in Italia. Molteplici divari di dati bloccanti — inclusi il meccanismo d'azione e i dati di sicurezza del foglio illustrativo — impediscono qualsiasi valutazione di ripropositura significativa al momento.

**Per procedere, è necessario:**
- Eseguire la pipeline di predizione TxGNN per l'acamprosato per generare nuove indicazioni candidate
- Risolvere **DG002**: Ottenere dati dettagliati del meccanismo d'azione tramite la query dell'API DrugBank
- Risolvere **DG001**: Scaricare e analizzare il PDF ufficiale del foglio illustrativo dal sito web TFDA per estrarre avvisi, controindicazioni e informazioni sulla sicurezza
- Chiarire l'ID DrugBank (attualmente `null`) per abilitare il cross-referencing con i database farmaceutici
- Confermare le indicazioni originali approvate da fonti normative autorevoli (AIFA, EMA o equivalenti)
- Rivalutare una volta che i dati di cui sopra siano disponibili e le predizioni TxGNN siano generate

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

