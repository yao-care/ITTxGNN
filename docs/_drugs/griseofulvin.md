---
layout: default
title: Griseofulvin
parent: Solo previsione del modello (L5)
nav_order: 229
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "wound myiasis", "creeping myiasis", "furuncular myiasis", "echinococcus granulosus infectious disease"]
description: "Griseofulvin: nuova indicazione prevista, Myiasis (livello di evidenza L5). In Italia, confezioni AIFA: 2 (autorizzate: 2)"
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

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Griseofulvin: Myiasis
{: .text-alpha }

## Riepilogo in una frase

La griseofulvina è un antifungino orale utilizzato per le dermatofitosi (tinea del piede, del corpo, dell'unghia, della barba, del cuoio capelluto e dell'inguine). Il modello TxGNN la predice come potenzialmente efficace per la **miasi**, con un punteggio molto alto (0.9941). Per questa direzione non risultano **né sperimentazioni cliniche né pubblicazioni** tra i dati compilati per questo report: la predizione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione predetta | Myiasis |
| Punteggio di predizione TxGNN | 0.9941 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole (o no)?

Secondo le sezioni «Mechanism of Action» e «Microbiology» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Griseofulvin (traduzione non ufficiale): «Il meccanismo di griseofulvina consiste nel legame alle proteine microtubulari, necessarie per la mitosi. […] Il meccanismo di griseofulvina consiste nel legame alle proteine microtubulari, necessarie per la mitosi. Attività in vivo Griseofulvina può essere attiva contro la maggior parte dei ceppi dei seguenti dermatofiti, come descritto nella sezione INDICAZIONI E USO: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans e Trichophyton verrucosum.» Testo originale in inglese: "The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. […] The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. Activity In Vivo Griseofulvin may be active against most strains of the following dermatophytes as described in the INDICATIONS AND USAGE section: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans and Trichophyton verrucosum." ([DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d), versione del 2025-05-14; consultato il 2026-11-19). In generale, la griseofulvina è un antifungino che interferisce con la funzione dei microtubuli e con la mitosi nei funghi. La sua efficacia nelle dermatofitosi è consolidata.

Per la miasi, però, **non emerge un legame meccanicistico plausibile**. La miasi è un'infestazione da larve di ditteri e non esiste un'attività antifungina nota contro le larve di insetti. Il punteggio elevato proviene dal modello TxGNN (deep learning) e può riflettere similarità che il modello ha appreso tra malattie correlate (ad esempio tra infezioni cutanee e dei tessuti molli), non evidenza biologica. La gestione standard prevede la rimozione delle larve, la cura della ferita e, quando indicato, l'ivermectina.

Lo stesso vale per le forme correlate predette: miasi da ferita, miasi strisciante (trattata con ivermectina o albendazolo, oppure con estrazione della larva) e miasi furuncolare (occlusione/estrazione della larva, talvolta ivermectina). In nessun caso è documentata un'attività larvicida della griseofulvina.

Tra le altre predizioni, l'unica con un'ipotesi meccanicistica è l'**infezione da Echinococcus granulosus** (punteggio 0.9932). La griseofulvina agisce sul fuso mitotico, concettualmente affine ai benzimidazoli (albendazolo), che colpiscono la tubulina. Si tratta tuttavia di una pura ipotesi: non è dimostrata un'attività di legame alla tubulina negli elminti e non sono disponibili dati preclinici o clinici. Albendazolo, chirurgia e PAIR restano lo standard; sarebbero necessari test in vitro di attività protoscolicida prima di qualsiasi ulteriore valutazione.

## Evidenze da sperimentazioni cliniche

Al momento non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Indicazione approvata |
|---------|------|------|------|-----------|
| 016762041 | FULCIN 500 mg, 10 compresse (SIT Laboratorio Farmaceutico Srl) | Compresse | Valida | Non riportata |
| 016762015 | FULCIN 125 mg, 20 compresse (SIT Laboratorio Farmaceutico Srl) | Compresse | Valida | Non riportata |

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
Tutte le predizioni (miasi, miasi da ferita, strisciante, furuncolare ed echinococcosi) sono al livello L5, senza sperimentazioni né letteratura, e senza un legame meccanicistico plausibile, salvo un'ipotesi speculativa per l'echinococcosi.

<!-- review:begin it-lic-20261106-griseofulvin-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Tutte le predizioni (miasi, miasi da ferita, strisciante, furuncolare ed echinococcosi) sono al livello L5, senza sperimentazioni né letteratura, e senza un legame meccanicistico plausibile, salvo un'ipotesi speculativa per l'echinococcosi. Inoltre, in Italia le autorizzazioni della griseofulvina risultano tutte cancellate, e le alternative standard per queste condizioni sono ben consolidate.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 2 autorizzazioni per questo farmaco, di cui 2 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-griseofulvin-1 -->

**Per procedere sarebbe necessario:**
- Reperire il foglio illustrativo AIFA (avvertenze e controindicazioni) per completare la valutazione di sicurezza.
- Acquisire i dati sul meccanismo d'azione (ad esempio da DrugBank).
- Ottenere dati preclinici in vitro (ad esempio attività protoscolicida su *Echinococcus*) prima di ogni ulteriore considerazione.
- Valutare la fattibilità regolatoria.

<!-- review:begin it-lic-20261106-griseofulvin-2 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Valutare la fattibilità regolatoria, dato che il farmaco non ha attualmente autorizzazioni valide in Italia.» Rimosso: il numero o lo stato delle autorizzazioni indicato non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 2 autorizzazioni per questo farmaco, di cui 2 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-griseofulvin-2 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «Inoltre, in Italia le autorizzazioni della griseofulvina risultano tutte cancellate, e le alternative standard per queste condizioni sono be» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-06 | Rimosso: «dato che il farmaco non ha attualmente autorizzazioni valide in Italia» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

