---
layout: default
title: Prasugrel
parent: Solo previsione del modello (L5)
nav_order: 358
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
description: "Prasugrel: nuova indicazione prevista, Pulmonary hypertension (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Prasugrel
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Prasugrel: Pulmonary hypertension
{: .text-alpha }

## Sintesi in una frase

Il prasugrel è un antiaggregante piastrinico (antagonista del recettore P2Y12), originariamente usato nella sindrome coronarica acuta. Il modello TxGNN lo indica come potenzialmente efficace per l'**emicrania** (rank 2 tra le predizioni, con punteggio del 0,9988), con **2 studi clinici** registrati (nessuno testa direttamente il prasugrel) e **2 pubblicazioni** pertinenti, entrambe di piccole dimensioni e non randomizzate. Le prove restano quindi preliminari.

Nota metodologica: la prima predizione in graduatoria è l'ipertensione polmonare (punteggio 0,9988), ma senza alcuno studio clinico e con una letteratura non pertinente (livello L5). Questo report si concentra sull'emicrania, l'unica indicazione con un segnale di evidenza concreto.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Pulmonary hypertension |
| Punteggio di predizione TxGNN | 0.9988 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 5 su 5) |
| Numero di autorizzazioni | 5 (valide: 5) |
| Decisione raccomandata | Hold (mantenere in attesa; tema di ricerca) |

---

## Perché questa predizione è ragionevole?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. In base alle conoscenze disponibili, il prasugrel è una tienopiridina che inibisce il recettore piastrinico P2Y12; la sua efficacia nella sindrome coronarica acuta è consolidata, e il meccanismo potrebbe essere applicabile all'emicrania.

Il razionale proposto riguarda soprattutto gli emicranici con forame ovale pervio (PFO). In questi pazienti, microemboli paradossi o mediatori vasoattivi derivati dalle piastrine potrebbero scatenare l'aura o gli attacchi. L'inibizione di P2Y12 (prasugrel, clopidogrel, ticagrelor) potrebbe ridurre l'attivazione piastrinica.

Il legame con l'indicazione originale è indiretto: in entrambi i casi entra in gioco l'attivazione piastrinica, ma il collegamento con l'emicrania resta ipotetico e limitato a un sottogruppo (emicrania con PFO).

---

## Evidenze dagli studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Fase 3 | In reclutamento | 32 | Studio COMFORT-PFO: terapia diretta al PFO nell'emicrania. Il riassunto cita il prasugrel come alternativa farmacologica alla chiusura del PFO, ma l'intervento testato non risulta essere il prasugrel. Supporta solo l'ipotesi PFO-emicrania. |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/D | Terminato | 7 | Studio su dispositivo (occlusore settale GORE CARDIOFORM) per l'emicrania, terminato con 7 partecipanti. Non è uno studio sul farmaco e non fornisce evidenze sul prasugrel. |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Coorte retrospettiva | Neurology | Revisione retrospettiva dell'uso off-label di tienopiridine (incluso il prasugrel) in pazienti emicranici con PFO. |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Studio pilota in aperto | Neurology | Studio TRACTOR: ticagrelor (inibitore P2Y12 non tienopiridinico) nell'emicrania refrattaria con PFO. Nasce dall'osservazione che clopidogrel e prasugrel riducevano i sintomi in alcuni pazienti. |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 039055090 | EFIENT 28 cpr rivestite 10 mg (Substipharm) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 045597402 | PRASUGREL 28x1 cpr rivestite 10 mg (Teva B.V.) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 045597186 | PRASUGREL 28x1 cpr rivestite 5 mg (Teva B.V.) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 039055025 | EFIENT 28 cpr rivestite 5 mg (Substipharm) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 046634022 | PRASUGREL 28 cpr rivestite 10 mg flacone (Viatris) | Compresse rivestite | Non disponibile (autorizzazione valida) |

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da relazioni nel grafo di conoscenza, non dal foglietto illustrativo)**: insufficienza epatica, disturbi della coagulazione, ictus e disturbi cerebrovascolari, infarto cerebrale, attacco ischemico transitorio, insufficienza vertebrobasilare, emorragia intracranica, porpora trombocitopenica, ipotensione, traumi.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni; tra quelle visibili le più rilevanti sono di livello **Maggiore** con deferasirox e ibritumomab tiuxetan, e di livello **Moderato** con acido acetilsalicilico, morfina, oppio, fenfluramina, destrofenfluramina e sibutramina. Le interazioni con inibitori di pompa protonica e antagonisti H2 (omeprazolo, pantoprazolo, famotidina, ranitidina ecc.) sono di livello Minore.

Per gli avvertimenti e le controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il segnale per l'emicrania si basa solo su una revisione retrospettiva e su un pilota in aperto con un farmaco affine, mentre gli studi registrati valutano la chiusura del PFO e non il prasugrel. Inoltre, tutte le autorizzazioni italiane sono cancellate e il profilo emorragico (controindicazioni cerebrovascolari ed emorragia intracranica) richiede cautela in una patologia non letale come l'emicrania.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione del prasugrel (DrugBank)
- Foglietto illustrativo AIFA con avvertenze e controindicazioni
- Uno studio randomizzato controllato sul prasugrel in emicranici con PFO
- Valutazione del rapporto rischio/beneficio emorragico in questa popolazione
- Chiarimento dello stato regolatorio (autorizzazioni cancellate) e della disponibilità del farmaco in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

