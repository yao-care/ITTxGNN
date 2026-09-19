---
layout: default
title: Lonafarnib
parent: Solo previsione del modello (L5)
nav_order: 139
evidence_level: L5
indication_count: 1
---

# Lonafarnib
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

# Lonafarnib: Da Sindrome di Hutchinson-Gilford al Lebbra

## Sintesi in una frase

Lonafarnib (Zokinvy) è un inibitore della farnesiltransferasi (FTase) e la prima terapia approvata dalla FDA per la Sindrome di Hutchinson-Gilford (HGPS) e le Laminopatie Progeroidi con difetto di processamento.
Il modello TxGNN predice che potrebbe avere potenziale terapeutico per il **Lebbra**, ma con **0 studi clinici** e **0 pubblicazioni** attualmente a supporto di questa direzione, la previsione poggia interamente sull'inferenza del modello derivata dal grafo della conoscenza biomedica — nessuna prova clinica o sperimentale è disponibile.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Sindrome di Hutchinson-Gilford (HGPS); non registrata a Taiwan |
| Nuova Indicazione Prevista | Lebbra |
| Punteggio di Previsione TxGNN | 99.14% |
| Livello di Prova | L5 |
| Stato del Mercato Taiwanese | ✗ Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Attendere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono inclusi in questo Evidence Pack. Sulla base di informazioni farmacologiche pubblicamente disponibili, Lonafarnib è un inibitore della farnesiltransferasi (FTase) — blocca competitivamente l'attacco di un gruppo farnesile (derivato da farnesilpirofofato) a proteine con motivo CaaX. Nella Sindrome di Hutchinson-Gilford, questo impedisce l'accumulo nucleare di progerina, una forma troncata permanentemente farnesilata di Lamin A che guida l'invecchiamento vascolare accelerato. Lo stesso meccanismo anti-farnesilazione era il razionale originale per investigare Lonafarnib come agente antitumorale, poiché le proteine Ras oncogeniche richiedono anche farnesilazione per l'ancoraggio alla membrana e l'attivazione.

Il collegamento biologico tra Lonafarnib e il lebbra non è ben supportato. *Mycobacterium leprae*, il batterio causativo del lebbra, non ha proteine di virulenza note che richiedono farnesilazione mediata dall'ospite. Inoltre, non ci sono prove pubblicate di una via meccanicistica diretta che colleghi l'inibizione della FTase dell'ospite all'attività anti-micobatterica o alla modulazione della risposta immunitaria granulomatosa caratteristica del lebbra.

Il punteggio di previsione elevato del modello TxGNN (0,9913) molto probabilmente riflette la vicinanza strutturale indiretta all'interno del grafo della conoscenza biomedica — ad esempio, nodi di comorbilità condivisi, intorni di interazione proteina-proteina, o annotazioni di percorsi sovrapposte — piuttosto che un razionale meccanicistico diretto. Tali punteggi derivati dalla topologia del grafo possono occasionalmente far emergere candidati genuini per il riposizionamento, ma senza un meccanismo biologicamente interpretabile questa previsione non può essere prioritizzata senza ulteriore validazione sperimentale.

---

## Prova da Studi Clinici

Attualmente non ci sono studi clinici correlati registrati.

---

## Prova da Letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni sulla Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: Attendere**

**Razionale:**
Questa previsione è supportata solo da prova L5 — inferenza del modello TxGNN senza studi clinici, nessuna letteratura pubblicata, e nessuna via meccanicistica stabilita che colleghi l'inibizione della farnesiltransferasi all'infezione da *Mycobacterium leprae* o alla patogenesi del lebbra.

**Per procedere, è necessario quanto segue:**
- Studi preclinici (in vitro o modello animale) esaminando se Lonafarnib o altri inibitori di FTase influenzano la viabilità, la crescita, o le risposte immunitarie dell'ospite a M. leprae
- Analisi meccanicistica chiarendo se l'inibizione della FTase dell'ospite potrebbe plausibilmente influenzare la sopravvivenza intracellulare micobatterica o la risposta granulomatosa nel lebbra
- Analisi di tracciamento dei percorsi del grafo della conoscenza TxGNN che hanno generato questo punteggio, per valutare se qualsiasi nodo biologico intermedio fornisce un razionale credibile
- Revisione del profilo di sicurezza completo includendo avvertenze, controindicazioni, e dati di interazione farmacologica dal foglio illustrativo approvato prima di qualsiasi ulteriore considerazione clinica

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

