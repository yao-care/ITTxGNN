---
layout: default
title: Desloratadina
parent: Solo previsione del modello (L5)
nav_order: 71
evidence_level: L5
indication_count: 0
---

# Desloratadina
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

# Desloratadina: pacchetto di prove incompleto — nessuna previsione di riposizionamento disponibile

## Sommario

Desloratadina è un antistaminico di seconda generazione ampiamente utilizzato per la rinite allergica e l'orticaria cronica.
Questo pacchetto di prove contiene **nessuna indicazione prevista da TxGNN**, il che significa che una valutazione del riposizionamento farmacologico non può essere completata in questa fase.
Inoltre, il farmaco è **attualmente non commercializzato in Italia** con questo INN, e i dati chiave di sicurezza e meccanismo d'azione sono assenti dal pacchetto.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Rinite allergica, orticaria cronica (conoscenza generale; non compilata nel pacchetto di prove) |
| Nuova indicazione prevista | Non disponibile — TxGNN non ha restituito previsioni |
| Punteggio di previsione TxGNN | N/A |
| Livello di evidenza | N/A |
| Stato del mercato in Italia | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Sospendere** |

---

## Perché questo rapporto non può essere completato

Il pacchetto di prove per Desloratadina manca di tre componenti critici:

**1. Nessuna previsione TxGNN è stata restituita.**
L'array `predicted_indications` è vuoto. Senza almeno una indicazione prevista, non c'è nessun candidato di riposizionamento da valutare. Questo potrebbe indicare che il farmaco non è stato trovato nel grafo della conoscenza TxGNN, oppure la pipeline di previsione non ha completato l'esecuzione.

**2. I dati sul meccanismo d'azione sono assenti.**
Il campo `original_moa` è contrassegnato come lacuna nei dati (gravità: alta). È noto che desloratadina sia un antagonista selettivo periferico del recettore H₁ dell'istamina — ma questo dato non è stato recuperato nel pacchetto di prove. La query di DrugBank ha restituito un risultato (`result_count: 1`), ma i dati non sono stati compilati, suggerendo un errore nell'estrazione della pipeline.

**3. I dati di sicurezza non sono disponibili.**
Sia i principali avvertimenti che le controindicazioni hanno restituito `[Data Gap]`. La query sul foglio illustrativo TFDA ha restituito un risultato (`result_count: 1`) ma non è stata analizzata nel pacchetto.

---

## Informazioni sul mercato italiano

Nessuna autorizzazione italiana è stata trovata per **DESLORATADINA** con questo INN esatto.

> **Nota:** i prodotti contenenti desloratadina possono essere commercializzati con nomi commerciali (p. es. Aerius, Neoclarityn) con ortografie INN diverse o formulazioni combinate. Si consiglia una ricerca con "desloratadine" (ortografia inglese).

---

## Considerazioni di sicurezza

I dati di sicurezza non sono stati estratti con successo in questo pacchetto di prove. Si prega di fare riferimento alle informazioni sul prodotto dell'EMA e al foglio illustrativo per Desloratadina per gli avvertimenti attuali, controindicazioni e interazioni farmacologiche.

La query sulla DDI non ha restituito alcuna interazione (`query_status: not_found`), il che potrebbe riflettere una mancata corrispondenza del termine di ricerca piuttosto che una vera assenza di interazioni note.

---

## Conclusione e fasi successive

**Decisione: Sospendere**

**Razionale:**
Il pacchetto di prove è strutturalmente incompleto — nessuna indicazione prevista esiste e i dati critici a livello di farmaco (meccanismo d'azione, sicurezza) non sono stati estratti nonostante le query a monte abbiano avuto successo. Una valutazione del riposizionamento non può essere responsabilmente scritta senza almeno una previsione TxGNN per ancorare l'analisi.

**Per procedere, è necessario quanto segue:**

- **Rieseguire la pipeline di previsione TxGNN** utilizzando l'identificatore corretto di DrugBank per Desloratadina (DB00967) per generare indicazioni previste
- **Estrarre i dati di DrugBank** — la query di DrugBank ha restituito 1 risultato; confermare che il passaggio di estrazione non ha fallito silenziosamente e compilare `original_moa`, `drugbank_id` e `categories`
- **Analizzare il foglio illustrativo TFDA / EMA** — la query del foglio illustrativo ha restituito 1 risultato; estrarre avvertimenti, controindicazioni e indicazioni approvate nel pacchetto di prove
- **Verificare l'ortografia dell'INN** — le query hanno utilizzato `DESLORATADINA` (INN italiano/spagnolo); confermare che il grafo della conoscenza TxGNN utilizza lo stesso identificatore, oppure rimappare su `desloratadine` (INN in inglese / standard di DrugBank)
- **Rieseguire le query per le autorizzazioni italiane** utilizzando ortografie alternative o nomi commerciali per confermare la vera assenza di mercato

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

