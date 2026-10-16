---
layout: default
title: Moxonidine
parent: Solo previsione del modello (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Moxonidine: nuova indicazione prevista, Ipotricosi semplice del cuoio capelluto (livello di evidenza L5). Indicazione originale: Ipertensione (ipertensione essenziale, disturbo ipertensivo)"
---

# Moxonidine
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

# Moxonidina: dall'ipertensione all'ipotricosi semplice del cuoio capelluto

## Sintesi in una frase

La moxonidina è un antipertensivo ad azione centrale, originariamente usato per il trattamento dell'ipertensione.
Il modello TxGNN la prevede come potenzialmente efficace per l'**ipotricosi semplice del cuoio capelluto**,
ma al momento **non esistono studi clinici né pubblicazioni** a supporto di questa indicazione: si tratta di una previsione basata solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione (ipertensione essenziale, disturbo ipertensivo) |
| Nuova indicazione prevista | Ipotricosi semplice del cuoio capelluto |
| Punteggio di predizione TxGNN | 99,95% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 6 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Allo stato attuale, i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report. In base alle informazioni di farmacologia disponibili, la moxonidina è un agonista dei recettori α2-adrenergici (con legame ai sottotipi α2A, α2B e α2C) e, secondo la letteratura generale, agisce anche sui recettori imidazolinici I1: riduce il tono simpatico centrale e quindi la pressione arteriosa.

Per quanto riguarda l'ipotricosi semplice del cuoio capelluto, non è stato individuato alcun legame meccanicistico plausibile con la biologia del follicolo pilifero o con i geni delle ipotricosi ereditarie. L'elevato punteggio TxGNN (99,95%) riflette verosimilmente similarità di rete nel grafo di conoscenza e non una motivazione farmacologica. Il rapporto di similarità con l'indicazione originale non è stato valutato.

Anche le altre previsioni di rango elevato appartengono in gran parte a due gruppi:
- **Disturbi dei capelli** (ipotricosi congenita con milia, alopecia areata diffusa, alopecia): nessuna evidenza e nessun nesso meccanicistico noto.
- **Forme di ipertensione** (ipertensione renovascolare maligna, nefropatia ipertensiva maligna): plausibilità solo indiretta, per estrapolazione dall'indicazione originale. Le forme di ipertensione polmonare, invece, sono patologie distinte e il meccanismo antipertensivo sistemico non è trasferibile.

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenza dalla letteratura

Per l'indicazione principale (ipotricosi semplice del cuoio capelluto) non è disponibile alcuna letteratura correlata.

Per completezza, per la previsione "alopecia" (rango 4) è stata recuperata una sola pubblicazione, che però non riguarda la moxonidina:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/) | 2024 | Caso clinico | Georgian Medical News | Caso di sindrome di Graham-Little-Piccardi-Lasseur (variante del lichen planopilare) in una paziente bulgara; non valuta l'efficacia della moxonidina |

## Informazioni sul mercato italiano

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 036677033 | Moxonidina 28 cpr rivestite 0,2 mg (EG SpA) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |
| 034063014 | Fisiotens 28 cpr rivestite 0,2 mg (Viatris Italia Srl) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |
| 034063053 | Fisiotens 28 cpr rivestite 0,4 mg (Viatris Italia Srl) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |
| 039676085 | Moxonidina 28 cpr rivestite 0,4 mg (Mylan SpA) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |
| 039676022 | Moxonidina 28 cpr rivestite 0,2 mg (Mylan SpA) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |

Sono presenti in totale 6 autorizzazioni, tutte cancellate; nessuna è attualmente valida.

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche / bersagli**: la moxonidina si lega ai recettori α2A (ADRA2A), α2B (ADRA2B) e α2C (ADRA2C)-adrenergici. Non sono stati registrati livelli di gravità per interazioni con altri farmaci.

Per le altre informazioni di sicurezza (avvertenze e controindicazioni) si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per l'ipotricosi semplice del cuoio capelluto è basata esclusivamente sul punteggio del modello (livello di evidenza L5), senza studi clinici, senza letteratura pertinente e senza un nesso meccanicistico plausibile. Inoltre, il farmaco non ha attualmente alcuna autorizzazione valida in Italia.

**Per procedere, sono necessari:**
- Dati sul meccanismo d'azione della moxonidina e analisi di un possibile legame con la biologia del follicolo pilifero
- Dati preclinici (ad es. modelli di follicolo pilifero) che giustifichino l'ipotesi
- Acquisizione e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza
- Verifica dello stato regolatorio, poiché tutte le autorizzazioni italiane risultano cancellate
- Eventuale rivalutazione delle previsioni di ambito ipertensivo (ipertensione renovascolare maligna e nefropatia ipertensiva maligna, livello L4), più coerenti con il meccanismo noto del farmaco, come "domande di ricerca" da approfondire con una revisione della letteratura
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

