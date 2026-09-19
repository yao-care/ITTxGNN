---
layout: default
title: Dutasteride
parent: Solo previsione del modello (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: La valutazione del riposizionamento non può procedere — Dossier di evidenze incompleto

## Riassunto in una frase

Dutasteride è un inibitore duale della 5α-reduttasi (5-ARI), ampiamente approvato a livello internazionale per l'iperplasia prostatica benigna (IPB) e l'alopecia androgenetica, ma attualmente non commercializzato a Taiwan.
Questo Dossier di evidenze non contiene **alcuna nuova indicazione prevista da TxGNN**, e dati critici inclusi il meccanismo d'azione e le avvertenze di sicurezza sono mancanti.
Una valutazione completa del riposizionamento non può essere condotta finché le lacune identificate nei dati non vengono risolte.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originaria | Iperplasia prostatica benigna (IPB) *(da conoscenze farmaceutiche generali; non fornite nel Dossier di evidenze)* |
| Nuova indicazione prevista | Non disponibile |
| Punteggio di previsione TxGNN | Non disponibile |
| Livello di evidenza | L5 — nessuno studio di supporto fornito in questo dossier |
| Stato del mercato a Taiwan | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Attesa** |

---

## Perché questa previsione è ragionevole?

Nel Dossier di evidenze non è inclusa alcuna indicazione prevista da TxGNN, pertanto un ponte meccanicistico tra l'indicazione originaria e quella nuova non può essere tracciato al momento.

Anche i dati sul meccanismo d'azione sono assenti dal Dossier di evidenze. Sulla base della conoscenza farmacologica generale, dutasteride inibisce irreversibilmente entrambi gli isoenzimi Tipo 1 e Tipo 2 della 5α-reduttasi, bloccando la conversione periferica del testosterone in diidrotestosterone (DHT). Questa soppressione androgenica è alla base della sua efficacia nelle indicazioni di IPB e perdita di capelli e ha motivato l'uso investigazionale nella prevenzione del cancro della prostata (ad es., il trial REDUCE). Tuttavia, senza una specifica indicazione prevista da valutare, la rilevanza di questo meccanismo per qualsiasi nuovo target non può essere formalmente valutata qui.

Questa sezione sarà completata non appena l'output della previsione TxGNN (candidate_id: `TW-DB01126-multi`) sarà recuperato e aggiunto al Dossier di evidenze.

---

## Evidenza da trial clinici

Attualmente nessuna indicazione prevista è disponibile in questo Dossier di evidenze; l'evidenza da trial clinici non può essere delimitata o elencata.

---

## Evidenza dalla letteratura

Attualmente nessuna indicazione prevista è disponibile in questo Dossier di evidenze; l'evidenza dalla letteratura non può essere delimitata o elencata.

---

## Informazioni sul mercato di Taiwan

Dutasteride **non è attualmente commercializzato a Taiwan**. Nessuna licenza TFDA è registrata (la ricerca TFDA ha restituito 0 risultati il 2026-03-29).

---

## Considerazioni di sicurezza

Si rimanda al foglio illustrativo per le informazioni di sicurezza. Le avvertenze chiave, le controindicazioni e i dati sulle interazioni farmacologiche non sono stati recuperati in questo Dossier di evidenze.

> **Avviso di lacuna nei dati:** Le avvertenze/controindicazioni del foglio illustrativo TFDA (DG001, gravità: Bloccante) e i dati MOA/sicurezza di DrugBank (DG002, gravità: Alta) sono entrambi in sospeso. Finché DG001 non è risolto, il candidato non può avanzare oltre la porta di screening di sicurezza S1.

---

## Conclusione e prossimi passi

**Decisione: Attesa**

**Razionale:**
Il Dossier di evidenze per dutasteride è strutturalmente incompleto — non ci sono previsioni TxGNN da valutare e due lacune nei dati a livello bloccante rimangono irrisolte, impedendo qualsiasi analisi significativa di sicurezza o meccanicistica.

**Per procedere, è necessario quanto segue:**

1. **[Bloccante] Recuperare i risultati della previsione TxGNN** — il candidate_id `TW-DB01126-multi` dovrebbe includere almeno una indicazione prevista; confermare se la pipeline di previsione è stata eseguita e perché l'output è assente
2. **[Bloccante] Scaricare e analizzare il PDF del foglio illustrativo TFDA** (DG001) — estrarre le avvertenze chiave, le controindicazioni e le restrizioni di dosaggio per abilitare lo screening di sicurezza S1
3. **[Alta] Recuperare i dati MOA e strutturati di DrugBank** (DG002) — la query di DrugBank ha restituito 1 risultato il 2026-03-29 ma il MOA non è stato popolato; recuperare nuovamente e analizzare il campo farmacodinamica
4. **[Media] Confermare le indicazioni originarie approvate** — l'array `original_indications` è vuoto; incrociare le informazioni con l'etichettatura TFDA, EMA o FDA per popolare questo campo prima di procedere all'analisi di mappatura delle indicazioni

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

