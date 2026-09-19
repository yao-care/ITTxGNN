---
layout: default
title: Disulfiram
parent: Solo previsione del modello (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
---

# Disulfiram
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

# Disulfiram: Disturbo da Uso di Alcol — Valutazione di Repurposing (Dati Incompleti)

## Riassunto in Una Frase

Il disulfiram è un inibitore della aldeide deidrogenasi (ALDH) utilizzato storicamente come deterrente alcolico per il disturbo da uso di alcol (AUD). Questo Fascicolo di Evidenze contiene **nessuna previsione di repurposing di TxGNN** — l'array `predicted_indications` è vuoto — e i dati critici di sicurezza e i dati meccanicistici sono assenti a causa di lacune nei dati non risolte. **Una valutazione completa di repurposing non può essere completata fino a quando non saranno ottenuti i dati dell'output della pipeline TxGNN e i dati del foglio illustrativo.**

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Disturbo da Uso di Alcol (conoscenza generale; non compilato nel Fascicolo di Evidenze) |
| Nuova Indicazione Prevista | Non disponibile — `predicted_indications` è vuoto |
| Punteggio di Previsione TxGNN | Non disponibile |
| Livello di Evidenza | Indeterminato (nessun output di previsione) |
| Stato di Commercializzazione in Italia | ✗ Non Commercializzato (0 autorizzazioni) |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | **Rinvio** |

---

## Perché Questa Previsione è Ragionevole?

Nessuna previsione di TxGNN è presente in questo Fascicolo di Evidenze, quindi nessuna rationale meccanicistica basata su evidenze per una nuova indicazione può essere fornita in questa fase.

Il disulfiram è ampiamente noto come inibitore di ALDH (aldeide deidrogenasi) che causa un accumulo avversario di acetaldeide all'ingestione di alcol. Al di là del DUA, la ricerca esplorativa ha esaminato le sue proprietà chelanti il rame e inibenti il proteasoma in contesti oncologici — ma questi indirizzi **non sono oggetto di questo rapporto**, poiché nessuna previsione formale di TxGNN è stata generata per guidare la valutazione.

I dati dettagliati del meccanismo d'azione sono inoltre segnalati come una lacuna nei dati di alta gravità (DG002) e devono essere recuperati da DrugBank prima che qualsiasi analisi meccanicistica del repurposing possa essere condotta.

---

## Evidenza da Trial Clinici

Attualmente nessun trial clinico correlato registrato — i dati di `predicted_indications` sono vuoti e nessuna indicazione target è stata identificata.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata disponibile — i dati di `predicted_indications` sono vuoti e nessuna indicazione target è stata identificata.

---

## Informazioni sul Mercato Italiano

Il disulfiram non ha autorizzazioni di prodotti approvati in Italia. La query normativa ha restituito 0 risultati — questo farmaco non è attualmente commercializzato in Italia.

---

## Considerazioni di Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> Nota: Sebbene la query del foglio illustrativo TFDA (`tfda_package_insert`) abbia restituito uno stato di successo con 1 risultato, i campi di sicurezza strutturati (avvertenze, controindicazioni) non sono stati analizzati nel Fascicolo di Evidenze. La query DDI ha inoltre restituito nessun risultato. Tutte e tre le categorie di dati di sicurezza richiedono un follow-up prima che sia possibile qualsiasi valutazione della sicurezza clinica.

---

## Conclusione e Prossimi Passi

**Decisione: Rinvio**

**Rationale:**
Questo Fascicolo di Evidenze manca dei tre input minimi richiesti per una valutazione di repurposing: output di previsione TxGNN, dati del meccanismo d'azione e informazioni sulla sicurezza strutturate. Procedere senza questi produrrebbe una raccomandazione non supportata.

**Per procedere, quanto segue è necessario:**

1. **Eseguire la pipeline TxGNN per Disulfiram** — generare `predicted_indications` con punteggi, link ai trial e riferimenti bibliografici; senza questo il rapporto non ha nessuna indicazione target da valutare
2. **Analizzare il contenuto del foglio illustrativo TFDA** (DG001, Blocco) — la query ha restituito un risultato ma i dati di sicurezza strutturati non sono stati estratti; avvertenze e controindicazioni devono essere compilate prima che qualsiasi screening di sicurezza sia possibile
3. **Recuperare MOA da DrugBank API** (DG002, Alta) — la query di DrugBank ha restituito un risultato ma MOA rimane non compilato; questo è necessario per l'analisi di plausibilità meccanicistica
4. **Integrare i dati DDI da una fonte alternativa** — la query DDI corrente ha restituito `not_found`; consultare il database DrugBank DDI o MICROMEDEX per escludere i rischi di interazione
5. **Controllare i database EMA / FDA per le indicazioni approvate** — poiché l'Italia ha 0 autorizzazioni, le etichette normative internazionali possono fornire il contesto di indicazione approvata necessario per l'intestazione del rapporto

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

