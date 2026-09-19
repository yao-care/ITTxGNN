---
layout: default
title: Eliglustat
parent: Solo previsione del modello (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Eliglustat
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

# Eliglustat: Malattia di Gaucher — Dati di previsione TxGNN insufficienti, valutazione in sospeso

---

## Sintesi in una frase

Eliglustat (nome commerciale: Cerdelga) è un inibitore orale della glucosil-ceramide sintasi, approvato per la terapia a riduzione del substrato a lungo termine nei pazienti adulti affetti da malattia di Gaucher di tipo 1.
Nel presente Evidence Pack (v4, 2026-04-20), **l'elenco delle previsioni TxGNN è vuoto**, indicando che il modello non ha ancora generato candidati di nuove indicazioni credibili per questo farmaco; inoltre, il mercato taiwanese non ha ancora approvazioni autorizzate e vi sono lacune nei dati di sicurezza.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione approvata originaria | Malattia di Gaucher di tipo 1 (Gaucher Disease Type 1) |
| Nuove indicazioni previste | — Nessun output di previsione TxGNN in questa sessione |
| Punteggio di previsione TxGNN | Assente |
| Livello di evidenza | **L5** (nessuna previsione del modello, nessun supporto di ricerca effettiva) |
| Stato del mercato taiwanese | ✗ Non commercializzato (0 certificati di autorizzazione) |
| Numero di certificati di autorizzazione | 0 |
| Raccomandazione decisionale | **Hold** |

---

## Perché questa previsione è ragionevole?

L'attuale Evidence Pack presenta un array `predicted_indications` vuoto, indicando che il modello TxGNN **non ha generato alcuna previsione di nuove indicazioni** in questa sessione, con possibili cause includenti:

1. Insufficiente connettività dei nodi del grafo di conoscenza (KG) di Eliglustat durante l'allenamento del modello
2. I punteggi di previsione non hanno superato la soglia di filtraggio
3. Perdita di dati nella fase di mappatura della pipeline

Dal punto di vista farmacologico, Eliglustat agisce inibendo l'UDP-glucosil-ceramide sintasi (GCS), riducendo l'anormale accumulo di glucosilceramide nei macrofagi, rappresentando una **terapia altamente mirata di riduzione del substrato (SRT)** con un meccanismo d'azione molto specifico.

Poiché la malattia di Gaucher è una malattia da accumulo lisosomiale rara, i potenziali riutilizzi cross-indication si concentrano principalmente su altre malattie da accumulo lisosomiale (come la malattia di Fabry, la malattia di Niemann-Pick di tipo C) o la malattia di Gaucher di tipo neuronale (tipo 3); tuttavia, nessuno di questi orientamenti attualmente compare nell'elenco delle previsioni di questa sessione, pertanto non è possibile procedere a ulteriori valutazioni di correlazione meccanicistica.

---

## Evidenze da studi clinici

L'Evidence Pack attuale non contiene indicazioni previste e non dispone di dati di studi clinici corrispondenti.

> Attualmente non sono disponibili dati di studi clinici registrati relativi a nuove indicazioni potenziali.

---

## Evidenze da letteratura

L'Evidence Pack attuale non contiene indicazioni previste e non dispone di dati bibliografici corrispondenti.

> Attualmente non sono disponibili dati bibliografici relativi a nuove indicazioni potenziali.

---

## Informazioni sul mercato taiwanese

| Numero di certificato di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|----------------------------------------|------------------|-------------------|----------------------|
| — | — | — | — |

Eliglustat attualmente **non ha ottenuto alcun certificato di autorizzazione di farmaco** nel mercato taiwanese. La presente ricerca (2026-03-29) ha restituito 0 risultati dal database TFDA.

---

## Considerazioni di sicurezza

Nel presente Evidence Pack tutti i campi di sicurezza presentano lacune di dati (key_warnings e contraindications sono vuoti; lo stato della ricerca DDI è not_found).

> Si prega di consultare direttamente il foglio illustrativo della ditta produttrice di Cerdelga (EMA/FDA SmPC/USPI) per ottenere informazioni di sicurezza complete, prestando particolare attenzione all'influenza del fenotipo CYP2D6 (EM/IM/PM) sulla posologia e alle interazioni con forti inibitori di CYP2D6/CYP3A.

---

## Conclusione e fasi successive

**Decisione: Hold**

**Razionale:**
L'Evidence Pack attuale manca dell'input più critico — l'elenco delle indicazioni previste da TxGNN è vuoto, rendendo impossibile eseguire qualsiasi valutazione di riutilizzo del farmaco; inoltre, i dati meccanicistici sono incompleti, il mercato taiwanese non è ancora penetrato, e i dati di sicurezza sono frammentari, tre elementi fondamentali risultano tutti assenti, non sussistono le condizioni per procedere alla fase di valutazione successiva.

**I dati seguenti devono essere completati per proseguire:**

1. **Rieseguire la previsione TxGNN**: Verificare che Eliglustat (DB09039) abbia nodi e bordi corretti caricati nel grafo di conoscenza, e abbassare o ricalibrare la soglia del punteggio di previsione
2. **Completare i dati meccanicistici** (DG002): Interrogare l'API DrugBank per ottenere `mechanism_of_action`, `pharmacodynamics`, e categorie DrugBank
3. **Completare i dati di sicurezza del foglio illustrativo** (DG001): Estrarre da EMA SmPC o etichetta FDA i campi key_warnings, contraindications, DDI
4. **Valutare la fattibilità della domanda taiwanese**: Confermare se Eliglustat dispone di un IND o di un piano di domanda per farmaci orfani, oppure accelerare l'ottenimento dell'autorizzazione taiwanese attraverso meccanismi di riconoscimento reciproco EMA/FDA

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

