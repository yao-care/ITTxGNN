---
noindex: true
sitemap: false
layout: default
title: Colchicina
parent: Solo previsione del modello (L5)
nav_order: 126
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Colchicina
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **0** 
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

## Colchicina (Colchicina): Valutazione del Riposizionamento del Farmaco — Dati Insufficienti per l'Analisi Completa
{: .text-alpha }

## Sintesi in una frase

Colchicina (Colchicina) è un farmaco consolidato, ma i dati compilati attuali contengono **nessuna indicazione originale compilata**, **nessuna indicazione prevista da TxGNN** e lacune critiche di dati nel meccanismo d'azione e nelle informazioni di sicurezza. Un'analisi significativa del riposizionamento non può essere completata fino al rimedio di queste lacune; questo rapporto funge da registro dello stato e mappa stradale di rimedio.

---

## Panoramica Rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione Originale | Non compilata nei dati |
| Indicazione Nuova Prevista | Nessuna previsione TxGNN disponibile |
| Punteggio di Previsione TxGNN | Non disponibile |
| Livello di Evidenza | Non valutabile |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione Consigliata | **In Sospeso** |

---

## Informazioni sul Mercato Italiano

Licenze totali nel record: **0**.

<!-- review:begin it-lic-20261106-colchicina-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Nessuna autorizzazione di commercializzazione è stata restituita dalla query del registro. Licenze totali nel record: **0**.» Rimosso: l'affermazione contraddiceva i dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 2 autorizzazioni per questo farmaco, di cui 2 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-colchicina-1 -->

> **Nota:** Il log di query conferma che la ricerca nel registro è stata eseguita con successo (result_status: "success") ma ha restituito 0 record. Se Colchicina è nota per avere una presenza di mercato nel territorio target con un nome di prodotto o un titolare di licenza alternativo, è consigliata una ricerca mirata per nome di prodotto come fase successiva.

---

## Considerazioni di Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> La query del registro per il foglio illustrativo ha restituito 1 risultato (query_log id: 4), ma il contenuto non è stato trasferito ai dati compilati. Il recupero e l'analisi di questo documento sono classificati come lacuna **Blocking** (DG001) e devono essere completati prima di procedere con qualsiasi valutazione di sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: In Sospeso**

**Razionale:**
I dati compilati non contengono indicazioni previste da TxGNN, nessun dato di indicazione originale, e due lacune di dati irrisolte — una Blocking e una ad alta severità — che impediscono qualsiasi valutazione significativa del riposizionamento o della sicurezza da condursi in questo momento.

**Per procedere, è necessario quanto segue:**

- **\[Blocking — DG001\]** Analizzare il PDF del foglio illustrativo già recuperato dal registro (query_log id: 4) per estrarre avvertenze e controindicazioni; questo è la precondizione per entrare nella fase di screening di sicurezza S1
- **\[High — DG002\]** Interrogare il record DrugBank già identificato (query_log id: 3, result_count: 1) per compilare il campo del meccanismo d'azione (MOA) e le indicazioni originali
- **\[Required\]** Rieseguire la pipeline di previsione TxGNN con Colchicina come input per generare candidate di indicazioni di riposizionamento; senza previsioni, nessuna analisi di riposizionamento può essere avviata
- **\[Advisory\]** Verificare lo stato di autorizzazione di commercializzazione Italia/AIFA tramite una ricerca per nome di prodotto (ad es. "Colchicina Houde" o altri nomi di marchio conosciuti)
- **\[Advisory\]** Confermare l'ID di DrugBank e mappare all'INN standardizzato per garantire un'identificazione coerente tra fonti nei futuri cicli di pipeline

<!-- review:begin it-lic-20261106-colchicina-2 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «"Colchicina Houde" o altri nomi di marchio conosciuti), poiché il risultato di 0 licenze attuali può riflettere una limitazione dell'ambito della query piuttosto che una vera assenza di mercato» Rimosso: l'affermazione contraddiceva i dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 2 autorizzazioni per questo farmaco, di cui 2 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-colchicina-2 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «Nessuna autorizzazione di commercializzazione è stata restituita dalla query del registro» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-06 | Rimosso: «poiché il risultato di 0 licenze attuali può riflettere una limitazione dell'ambito della query piuttosto che una vera assenza di mercato» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

