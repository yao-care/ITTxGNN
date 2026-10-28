---
layout: default
title: Silodosin
parent: Solo previsione del modello (L5)
nav_order: 403
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Silodosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
description: "Silodosin: nuova indicazione prevista, Ipertricosi universale congenita di tipo Ambras (Ambras type hypertrichosis universalis congenita) (livello di evidenza L5). Indicazione originale: Non riportat…"
---

# Silodosin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

## Silodosin: Ipertricosi universale congenita di tipo Ambras (Ambras type hypertrichosis universalis congenita)
{: .text-alpha }

## Riepilogo in una frase

La silodosina è un antagonista selettivo del recettore alfa-1A adrenergico, originariamente utilizzato per il trattamento dell'ipertrofia prostatica benigna (IPB).
Il modello TxGNN ne prevede una possibile efficacia per l'**ipertricosi universale congenita di tipo Ambras**, con un punteggio molto alto (0,9999).
Al momento però **non risultano sperimentazioni cliniche né pubblicazioni** a sostegno di questa direzione: la previsione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Ipertricosi universale congenita di tipo Ambras (Ambras type hypertrichosis universalis congenita) |
| Punteggio di previsione TxGNN | 0.9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

Non sono attualmente disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. Dai dati farmacologici compilati, la silodosina si lega ai recettori alfa-1A, alfa-1B e alfa-1D, con azione principale sul sottotipo alfa-1A, e viene usata per migliorare il flusso urinario nei pazienti con IPB.

Il legame con la nuova indicazione risulta debole. L'ipertricosi di tipo Ambras è una condizione genetica legata a riarrangiamenti del cromosoma 8q22 che influenzano la regolazione di TRPS1. Non esiste alcun collegamento meccanicistico documentato tra il blocco alfa-1 e questa eziologia. Il punteggio elevato deriva dal modello TxGNN (deep learning) e può riflettere similarità che il modello ha appreso tra malattie correlate, non prove biologiche o cliniche.

Lo stesso vale per le altre previsioni del modello, tutte in L5 e senza studi a supporto:

| Indicazione prevista | Punteggio TxGNN | Considerazioni |
|------|------|------|
| Ipertricosi (generica) | 0,9999 | L'ipertricosi è di solito un effetto avverso da evitare (ad es. con minoxidil), non un bersaglio terapeutico; l'ipotesi vascolare è speculativa |
| Sindrome malformativa con componente dentale/parodontale | 0,9999 | Nessun legame plausibile; il punteggio del modello TxGNN (deep learning) può riflettere similarità apprese tra malattie correlate, non prove biologiche |
| Sindrome con malformazione di Dandy-Walker come caratteristica principale | 0,9998 | Un farmaco postnatale non può correggere difetti strutturali dello sviluppo |
| Anomalia genetica isolata del fusto del pelo | 0,9998 | Difetto strutturale genetico, nessun legame con la segnalazione alfa-adrenergica |
| Tricomegalia isolata familiare | 0,9923 | Nessun meccanismo documentato; punteggio più basso del gruppo |

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Attualmente non risulta disponibile letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati compilati. Le principali (5 di 20):

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 039775046 | SILODYX 30 cps 4 mg | Recordati Ireland Ltd | Valida |
| 039775111 | SILODYX 30 cps 8 mg | Recordati Ireland Ltd | Valida |
| 039789045 | UROREC 30 cps 4 mg | Recordati Ireland Ltd | Valida |
| 039789110 | UROREC 30 cps 8 mg | Recordati Ireland Ltd | Valida |
| 047058019 | VIRSIL 30 cps 4 mg | S.F. Group Srl | Valida |

Le restanti autorizzazioni riguardano equivalenti di silodosina (4 mg e 8 mg, capsule) di vari titolari, anch'esse cancellate.

## Considerazioni di sicurezza

- **Controindicazioni (da relazioni del grafo di conoscenza, non dal foglio illustrativo)**: atrofia multisistemica, sindrome da tachicardia posturale ortostatica, ipotensione ortostatica, insufficienza epatica, malattia renale, piouretere, sindrome intraoperatoria dell'iride a bandiera (IFIS).
- **Interazioni**: l'analisi ha riportato solo le interazioni farmacologiche con i bersagli recettoriali alfa-1A, alfa-1B e alfa-1D; non sono stati identificati con questa fonte altri farmaci interagenti.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo, non ancora acquisito.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione è basata solo sul modello (L5): nessuna sperimentazione, nessuna pubblicazione e nessun meccanismo biologico plausibile che colleghi il blocco alfa-1A all'ipertricosi di tipo Ambras. Inoltre, in Italia tutte le autorizzazioni sono attualmente cancellate.

**Per procedere sarebbe necessario:**
- Acquisire il meccanismo d'azione dettagliato (dati DrugBank).
- Acquisire avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per la valutazione di sicurezza).
- Formulare un'ipotesi biologica credibile che colleghi la segnalazione alfa-1 alla regolazione di TRPS1 o alla biologia del follicolo pilifero, con eventuali studi preclinici.
- Valutare se un'indicazione per una condizione in cui l'ipertricosi è un tratto genetico abbia una reale utilità clinica.
- Verificare la compatibilità delle vie di somministrazione e la situazione autorizzativa in Italia.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

