---
layout: default
title: Amisulpride
parent: Solo previsione del modello (L5)
nav_order: 27
evidence_level: L5
indication_count: 0
---

# Amisulpride
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

# AMISULPRIDE: Valutazione del Riposizionamento del Farmaco — In Attesa dei Dati di Previsione

## Sintesi in una Frase

L'amisulpride (DrugBank: DB06288) è un derivato benzamidico noto a livello internazionale come antipsicotico atipico.
L'attuale Dossier di Evidenza contiene **nessuna indicazione prevista da TxGNN**, e rimangono lacune critiche nei dati nel meccanismo d'azione e nelle informazioni di sicurezza normative.
Questo rapporto documenta lo status attuale e delinea i passaggi necessari prima che una valutazione del riposizionamento possa procedere.

---

## Panoramica Rapida

| Voce | Contenuto |
|------|-----------|
| Nome del Farmaco (INN) | Amisulpride |
| ID DrugBank | DB06288 |
| Indicazione Originale | Non disponibile nei dati attuali |
| Indicazione Nuova Prevista | **Nessuna** — previsioni TxGNN non ancora generate |
| Punteggio di Previsione TxGNN | N/A |
| Livello di Evidenza | **L5** (Nessuna previsione o studi di supporto disponibili) |
| Status di Commercializzazione a Taiwan | ✗ Non commercializzato (Non commercializzato) |
| Numero di Autorizzazioni (TFDA) | 0 |
| Decisione Consigliata | **Rinvio** |

---

## Perché Questa Previsione è Ragionevole?

> **Attualmente nessuna indicazione prevista da TxGNN è disponibile per la valutazione.**

Attualmente, i dati dettagliati sul meccanismo d'azione (MOA) non sono stati recuperati per l'amisulpride in questo Dossier di Evidenza. Sulla base di informazioni pubblicamente note, l'amisulpride è un antagonista selettivo del recettore dopaminergico D₂/D₃ appartenente alla classe benzamidica degli antipsicotici atipici. È ampiamente utilizzato a livello internazionale per il trattamento della schizofrenia (sintomi positivi e negativi) ed è stato anche oggetto di investigazione per altre condizioni psichiatriche.

Tuttavia, poiché l'array `predicted_indications` è vuoto, nessuna analisi di collegamento meccanicistico tra un'indicazione originale e una nuova indicazione prevista può essere eseguita. La lacuna nei dati MOA (DG002) limita ulteriormente la capacità di valutare eventuali previsioni future nel contesto delle relazioni bersaglio-malattia.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato è disponibile — TxGNN non ha ancora generato indicazioni previste per questo farmaco.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata è disponibile — senza un'indicazione prevista, nessuna ricerca mirata di letteratura è stata condotta.

---

## Informazioni sul Mercato Taiwanese

L'amisulpride attualmente non detiene **nessuna autorizzazione di commercializzazione TFDA** a Taiwan (status di mercato: Non commercializzato). Nessun record di licenza è disponibile.

---

## Considerazioni di Sicurezza

> Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

Tutti i campi di sicurezza (avvertimenti chiave, controindicazioni e interazioni farmacologiche) sono stati restituiti come lacune nei dati o non trovati nell'attuale Dossier di Evidenza. Le seguenti lacune critiche nei dati sono state identificate:

- **DG001 (Bloccante):** Gli avvertimenti del foglio illustrativo TFDA e le controindicazioni non sono stati recuperati. Questo deve essere risolto prima che qualsiasi valutazione di sicurezza della Fase 1 possa procedere.
- **DG002 (Alta):** I dati sul meccanismo d'azione mancano da DrugBank, impattando l'analisi della rilevanza meccanicistica.

---

## Conclusione e Azioni Successive

**Decisione: Rinvio**

**Motivazione:**
Nessuna indicazione prevista da TxGNN esiste per l'amisulpride in questo Dossier di Evidenza, e lacune critiche nei dati (MOA, etichettatura di sicurezza TFDA) impediscono una valutazione significativa. Il farmaco inoltre non è attualmente commercializzato a Taiwan, aggiungendo complessità normativa a qualsiasi percorso di riposizionamento.

**Per procedere, è necessario quanto segue:**

1. **Generare previsioni TxGNN** — Eseguire il modello TxGNN per l'amisulpride (DB06288) per ottenere indicazioni candidate per il riposizionamento con punteggi di confidenza
2. **Risolvere DG001 (Bloccante)** — Recuperare gli avvertimenti del foglio illustrativo TFDA e le controindicazioni (fonte: sito web TFDA, metodo: scaricare e analizzare il PDF del foglio illustrativo)
3. **Risolvere DG002 (Alta)** — Recuperare i dati dettagliati su MOA dall'API DrugBank per abilitare l'analisi di collegamento meccanicistico
4. **Condurre ricerca di evidenza** — Una volta disponibile un'indicazione prevista, eseguire ricerche su studi clinici (ClinicalTrials.gov) e letteratura (PubMed) per la coppia farmaco-indicazione
5. **Rivalutare il percorso di commercializzazione** — Poiché l'amisulpride non è commercializzato a Taiwan, valutare se una via di importazione/accesso speciale o una nuova richiesta di farmaco sarebbe necessaria per qualsiasi indicazione riposizionata

---

*Questo rapporto è stato generato il 2026-04-03. Cutoff dei dati: 2026-04-03. I risultati sono solo per scopi di ricerca e non costituiscono consulenza medica. I candidati per il riposizionamento di farmaci richiedono validazione clinica prima dell'applicazione.*

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

