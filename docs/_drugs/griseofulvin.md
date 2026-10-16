---
layout: default
title: Griseofulvin
parent: Solo previsione del modello (L5)
nav_order: 229
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Griseofulvin: nuova indicazione prevista, Miasi (livello di evidenza L5). Indicazione originale: Tinea (tinea pedis, tinea corporis, tinea unguium…"
---

# Griseofulvin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Griseofulvina: Dalla tinea alla miasi (predizione TxGNN)

## Riepilogo in una frase

La griseofulvina è un antifungino orale utilizzato per le dermatofitosi (tinea del piede, del corpo, dell'unghia, della barba, del cuoio capelluto e dell'inguine). Il modello TxGNN la predice come potenzialmente efficace per la **miasi**, con un punteggio molto alto (99,4%). Per questa direzione non risultano **né sperimentazioni cliniche né pubblicazioni** tra i dati compilati per questo report: la predizione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Tinea (tinea pedis, tinea corporis, tinea unguium, tinea barbae e altre dermatofitosi). Il testo dell'indicazione approvata AIFA non è riportato nelle autorizzazioni; l'elenco deriva dal knowledge graph TxGNN |
| Nuova indicazione predetta | Miasi |
| Punteggio di predizione TxGNN | 99,41% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (0 valide, 2 cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole (o no)?

I dati dettagliati sul meccanismo d'azione non sono al momento disponibili. In generale, la griseofulvina è un antifungino che interferisce con la funzione dei microtubuli e con la mitosi nei funghi. La sua efficacia nelle dermatofitosi è consolidata.

Per la miasi, però, **non emerge un legame meccanicistico plausibile**. La miasi è un'infestazione da larve di ditteri e non esiste un'attività antifungina nota contro le larve di insetti. Il punteggio elevato riflette probabilmente la vicinanza nel grafo di conoscenza (ad esempio associazioni comuni con infezioni cutanee e dei tessuti molli) più che una plausibilità biologica. La gestione standard prevede la rimozione delle larve, la cura della ferita e, quando indicato, l'ivermectina.

Lo stesso vale per le forme correlate predette: miasi da ferita, miasi strisciante (trattata con ivermectina o albendazolo, oppure con estrazione della larva) e miasi furuncolare (occlusione/estrazione della larva, talvolta ivermectina). In nessun caso è documentata un'attività larvicida della griseofulvina.

Tra le altre predizioni, l'unica con un'ipotesi meccanicistica è l'**infezione da Echinococcus granulosus** (punteggio 99,3%). La griseofulvina agisce sul fuso mitotico, concettualmente affine ai benzimidazoli (albendazolo), che colpiscono la tubulina. Si tratta tuttavia di una pura ipotesi: non è dimostrata un'attività di legame alla tubulina negli elminti e non sono disponibili dati preclinici o clinici. Albendazolo, chirurgia e PAIR restano lo standard; sarebbero necessari test in vitro di attività protoscolicida prima di qualsiasi ulteriore valutazione.

## Evidenze da sperimentazioni cliniche

Al momento non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Indicazione approvata |
|---------|------|------|------|-----------|
| 016762041 | FULCIN 500 mg, 10 compresse (SIT Laboratorio Farmaceutico Srl) | Compresse | Cancellata | Non riportata |
| 016762015 | FULCIN 125 mg, 20 compresse (SIT Laboratorio Farmaceutico Srl) | Compresse | Cancellata | Non riportata |

## Considerazioni sulla sicurezza

- **Controindicazioni (dal knowledge graph, non dal foglio illustrativo)**: gli archi farmaco-malattia di TxGNN segnalano controindicazioni in presenza di:
  - insufficienza epatica;
  - porfiria (inclusa la porfiria ereditaria e i disturbi del metabolismo delle porfirine);
  - lupus eritematoso sistemico (anche pediatrico);
  - abuso/dipendenza da sostanze;
  - agranulocitosi e varie forme di neutropenia (ciclica, congenita grave, idiopatica dell'adulto, sindrome di Kostmann, sindrome di Rowell e altre forme congenite).
- **Interazioni farmacologiche**: la ricerca ha riportato 100 interazioni; tra quelle visualizzate prevalgono quelle di livello moderato. Le principali riguardano:
  - anticoagulanti/antiaggreganti: warfarin, dicumarolo, apixaban, rivaroxaban, ticagrelor, fostamatinib (moderate); acido acetilsalicilico (minore);
  - antidiabetici: saxagliptin, linagliptin, repaglinide (moderate); liraglutide (minore);
  - altri: aprepitant, rolapitant, eliglustat, naloxegol, nitisinone, macimorelin, artemetere, meflochina, praziquantel (moderate).
- Il foglio illustrativo AIFA con avvertenze e controindicazioni ufficiali non è stato reperito; per le informazioni di sicurezza si rimanda quindi al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Tutte le predizioni (miasi, miasi da ferita, strisciante, furuncolare ed echinococcosi) sono al livello L5, senza sperimentazioni né letteratura, e senza un legame meccanicistico plausibile, salvo un'ipotesi speculativa per l'echinococcosi. Inoltre, in Italia le autorizzazioni della griseofulvina risultano tutte cancellate, e le alternative standard per queste condizioni sono ben consolidate.

**Per procedere sarebbe necessario:**
- Reperire il foglio illustrativo AIFA (avvertenze e controindicazioni) per completare la valutazione di sicurezza.
- Acquisire i dati sul meccanismo d'azione (ad esempio da DrugBank).
- Ottenere dati preclinici in vitro (ad esempio attività protoscolicida su *Echinococcus*) prima di ogni ulteriore considerazione.
- Valutare la fattibilità regolatoria, dato che il farmaco non ha attualmente autorizzazioni valide in Italia.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

