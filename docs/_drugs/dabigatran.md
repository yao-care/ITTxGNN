---
noindex: true
sitemap: false
layout: default
title: Dabigatran
parent: Solo previsione del modello (L5)
nav_order: 132
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-24
predicted_indications: []
---

# Dabigatran
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

## DABIGATRAN: valutazione candidata di riposizionamento dei farmaci — dati insufficienti, impossibile completare relazione completa
{: .text-alpha }

## Riepilogo in una frase

DABIGATRAN (DrugBank ID: DB14726) è un farmaco candidato identificato dalla scansione di riposizionamento dei farmaci in questa sessione. Tuttavia, i dati compilati attuali **non riescono ad acquisire l'indicazione originale**, **non hanno indicazioni predette da TxGNN** e **tutti i dati di sicurezza sono mancanti**, rendendo impossibile generare una valutazione completa nel formato standard; si consiglia di completare i dati prima di procedere alla valutazione.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|---------|
| Indicazione originale | Non acquisita (il campo dell'indicazione originale è vuoto) |
| Indicazione nuova predetta | Nessuna previsione disponibile (array `predicted_indications` vuoto) |
| Punteggio di previsione TxGNN | N/A |
| Livello di evidenza | N/A — nessun trial clinico o dati della letteratura |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | almeno 20 |
| Decisione consigliata | **Hold** |

---

## Perché questa previsione è ragionevole?

Impossibile eseguire un'analisi di correlazione del meccanismo.

I dati compilati attuali mostrano due lacune critiche nei dati:

1. **Indicazione originale non acquisita**: il campo `original_indications` è un array vuoto, e `original_moa` non contiene dati.
2. **Nessun risultato di previsione TxGNN**: `predicted_indications` è un array vuoto, indicando che la previsione del modello non è stata ancora eseguita o i risultati non sono stati inclusi nel Pack.

In assenza di "nuove indicazioni predette", non è possibile confrontare la sovrapposizione meccanicistica tra l'indicazione originale e le nuove indicazioni, né è possibile giudicare se questo farmaco candidato meriti un'ulteriore valutazione.

<!-- review:begin it-lic-20261106-dabigatran-2 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «DABIGATRAN non ha alcun record di autorizzazione di commercializzazione in Italia (`total_licenses: 0`, `licenses` vuoto).» Rimosso: l'affermazione contraddiceva i dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-dabigatran-2 -->

---

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 051110082 | DABIGATRAN ETEXILATO\*10 cps 110 mg | TEVA GmbH | Autorizzata |
| 051110029 | DABIGATRAN ETEXILATO\*10 cps 75 mg | TEVA GmbH | Autorizzata |
| 049846052 | DABIKASTE\*30 cps 110 mg | GLENMARK ARZNEIMITTEL GMBH | Autorizzata |
| 050696145 | DABIGATRAN ETEXILATO\*60 cps 110 mg | ACCORD HEALTHCARE SLU | Autorizzata |
| 049675085 | DABIGATRAN ETEXILATO\*6x10 cps 150 mg | DOC GENERICI Srl | Autorizzata |
| 050696057 | DABIGATRAN ETEXILATO\*30x1 cps 75 mg | ACCORD HEALTHCARE SLU | Autorizzata |
| 050854025 | DABIGATRAN ETEXILATO\*30 cps 75 mg | SANDOZ SpA | Autorizzata |
| 050854379 | DABIGATRAN ETEXILATO\*60 cps 150 mg | SANDOZ SpA | Autorizzata |
| 050696234 | DABIGATRAN ETEXILATO\*60x1 cps 150 mg | ACCORD HEALTHCARE SLU | Autorizzata |
| 049675061 | DABIGATRAN ETEXILATO\*6x10 cps 110 mg | DOC GENERICI Srl | Autorizzata |
| 049099132 | DABIGATRAN ETEXILATO\*60 cps 150 mg | EG SpA | Autorizzata |
| 049846114 | DABIKASTE\*60 cps 150 mg | GLENMARK ARZNEIMITTEL GMBH | Autorizzata |
| 051110106 | DABIGATRAN ETEXILATO\*30 cps 110 mg | TEVA GmbH | Autorizzata |
| 051110207 | DABIGATRAN ETEXILATO\*60 cps 150 mg | TEVA GmbH | Autorizzata |
| 038451011 | PRADAXA\*10x1 cps 75 mg | BOEHRINGER INGELHEIM INT.GMBH | Autorizzata |
| 049099068 | DABIGATRAN ETEXILATO\*30 cps 110 mg | EG SpA | Autorizzata |
| 049099070 | DABIGATRAN ETEXILATO\*60 cps 110 mg | EG SpA | Autorizzata |
| 051110120 | DABIGATRAN ETEXILATO\*60 cps 110 mg | TEVA GmbH | Autorizzata |
| 050696121 | DABIGATRAN ETEXILATO\*10 cps 110 mg | ACCORD HEALTHCARE SLU | Autorizzata |
| 038451112 | PRADAXA\*60x1 cps 150 mg | BOEHRINGER INGELHEIM INT.GMBH | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.
I dati contengono solo una parte delle autorizzazioni; l'elenco può essere incompleto.

<!-- licenses:end -->

---

## Considerazioni sulla sicurezza

Si prega di consultare il foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
I dati compilati di DABIGATRAN presentano molteplici lacune critiche nei dati (indicazione originale, MOA, previsione TxGNN, dati di sicurezza sono tutti mancanti), rendendo impossibile eseguire una valutazione di fattibilità di riposizionamento di qualsiasi entità; non è consigliabile procedere prima che i dati siano completati.

**Per procedere, è necessario quanto segue:**

- **\[Blocking\] Completa i risultati della previsione TxGNN**: riesegui il modello, includi DABIGATRAN (DB14726) nella pipeline di previsione, verifica che l'output di `predicted_indications` sia scritto correttamente nei dati compilati
- **\[Blocking\] Acquisisci l'indicazione originale**: ottieni il testo dell'indicazione approvata dall'API DrugBank o dal foglio illustrativo approvato, popola `original_indications`
- **\[High\] Completa i dati MOA**: interroga DrugBank per ottenere una descrizione completa del meccanismo d'azione, supportando l'analisi di correlazione del meccanismo successiva
- **\[High\] Analizza i dati di sicurezza del foglio illustrativo**: scarica e analizza il PDF del foglio illustrativo, estrai avvertenze e controindicazioni, popola il campo `safety`
- **\[Medium\] Conferma lo stato di commercializzazione in Italia (AIFA)**: DABIGATRAN (Pradaxa®) è un farmaco noto come commercializzato in Europa, si consiglia di interrogare direttamente il database AIFA per confermare l'autorizzazione
- **Dopo il completamento dei dati, genera nuovamente i dati compilati**, quindi procedi con il processo completo di valutazione del riposizionamento

<!-- review:begin it-lic-20261106-dabigatran-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «**\[Medium\] Conferma lo stato di commercializzazione in Italia (AIFA)**: DABIGATRAN (Pradaxa®) è un farmaco noto come commercializzato in Europa, si consiglia di interrogare direttamente il database AIFA per confermare l'autorizzazione, aggiorna il campo `taiwan_regulatory` (dovrebbe essere regolato a `italy_regulatory`)» Rimosso: testo residuo del modello taiwanese (TFDA), non pertinente a questa pagina. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-dabigatran-1 -->

<!-- review:begin it-lic-20261106-dabigatran-3 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «**\[High\] Analizza i dati di sicurezza del foglio illustrativo**: scarica e analizza il PDF del foglio illustrativo TFDA (il `query_log` mostra che la query è riuscita), estrai avvertenze e controindicazioni, popola il campo `safety`» Rimosso: testo residuo del modello taiwanese (TFDA), non pertinente a questa pagina. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-dabigatran-3 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «aggiorna il campo `taiwan_regulatory` (dovrebbe essere regolato a `italy_regulatory`)» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-06 | Rimosso: «DABIGATRAN non ha alcun record di autorizzazione di commercializzazione in Italia (`total_licenses: 0`, `licenses` vuoto)» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-06 | Rimosso: «TFDA (il `query_log` mostra che la query è riuscita)» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

