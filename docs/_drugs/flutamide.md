---
layout: default
title: Flutamide
parent: Solo previsione del modello (L5)
nav_order: 207
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "FLUTAMIDE"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
description: "Flutamide: nuova indicazione prevista, Fibroma of prostate (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Flutamide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

## Flutamide: Fibroma of prostate
{: .text-alpha }

## Sintesi in una frase

Flutamide è un antiandrogeno non steroideo, originariamente impiegato nel trattamento del carcinoma della prostata.
Il modello TxGNN prevede una possibile efficacia per **suscettibilità al carcinoma prostatico/cerebrale**, ma per questa previsione **non sono stati trovati studi clinici né pubblicazioni** a supporto: si tratta di una previsione basata solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Fibroma of prostate |
| Punteggio di previsione TxGNN | 0.9998 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo report. In base alle conoscenze note, flutamide è un antagonista del recettore degli androgeni (tramite il metabolita idrossiflutamide), la cui efficacia nel carcinoma prostatico è consolidata.

La "suscettibilità genetica" non è uno stato patologico trattabile, ma una predisposizione: non esiste quindi una vera indicazione terapeutica distinta da valutare.

Pertanto la previsione non rappresenta un riposizionamento genuino e non è supportata da evidenze cliniche.

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati a questa previsione.

*Nota di contesto:* per altre previsioni di flutamide (in particolare "tumore dell'apparato riproduttivo maschile", che include il carcinoma prostatico) esistono molti studi, ma riguardano l'uso già approvato e non la nuova indicazione di questo report. Esempi: lo studio di fase 2 sulla chemioprevenzione con flutamide nella neoplasia intraepiteliale prostatica ([NCT00006214](https://clinicaltrials.gov/study/NCT00006214)) e lo studio di fase 4 che confronta enzalutamide e flutamide nel carcinoma prostatico resistente alla castrazione ([NCT02918968](https://clinicaltrials.gov/study/NCT02918968)).

## Evidenza dalla letteratura

Attualmente non risulta alcuna letteratura correlata a questa previsione.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 034707012 | FLUTAMIDE*21 cpr 250 mg (EG SpA) | Compresse | Non disponibile (autorizzazione valida) |

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Terapia ormonale (antiandrogeno non steroideo), non chemioterapico citotossico convenzionale |
| Rischio di mielosoppressione | Fare riferimento alle avvertenze e precauzioni del foglio illustrativo |
| Classificazione emetogenica | Fare riferimento alle avvertenze e precauzioni del foglio illustrativo |
| Parametri da monitorare | Funzionalità epatica (in particolare, per il noto rischio di epatotossicità), emocromo |
| Protezione nella manipolazione | Fare riferimento alle avvertenze e precauzioni del foglio illustrativo |

## Considerazioni sulla sicurezza

- **Avvertenze principali:** i dati compilati segnalano un'epatotossicità (avvertenza riquadrata), che pesa contro nuove indicazioni.
- **Controindicazioni (dal grafo di conoscenza, non dal foglio illustrativo):** insufficienza epatica, malattie epatiche, malattie della colecisti, metemoglobinemia, solfemoglobinemia, iperbilirubinemia (anche ereditaria), sindrome di Gilbert, deficit di G6PD, glicogenosi, cistinuria, galattosemia, deficit di piruvato deidrogenasi E3, metemoglobinemia da deficit di metemoglobina reduttasi.
- **Interazioni farmacologiche:** rilevate 100 interazioni in totale. Tra le principali di gravità **maggiore**: dolasetron e cisapride. Tra quelle di gravità moderata: claritromicina, levofloxacina, ondansetron, palonosetron, famotidina, loperamide, naltrexone, acido obeticolico e vari lassativi (bisacodile, lattulosio, lattitolo, polietilenglicole, olio di ricino, glicerina, sodio solfato, acido picosolfurico). Metronidazolo è di gravità minore.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio TxGNN elevato ma nessuno studio clinico né pubblicazione a supporto (livello L5). La "suscettibilità genetica" non è una condizione trattabile. Inoltre l'autorizzazione italiana è cancellata e il profilo di epatotossicità sfavorisce nuovi sviluppi.

**Per procedere sarebbe necessario:**
- Chiarire se esista una popolazione o un'indicazione clinicamente definibile (ad es. prevenzione in soggetti ad alto rischio) distinta dal carcinoma prostatico già trattato
- Dati dettagliati sul meccanismo d'azione
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, attualmente non disponibili e necessarie per lo screening di sicurezza
- Un piano di monitoraggio della funzionalità epatica e una valutazione del profilo rischio-beneficio rispetto agli antiandrogeni più recenti

---

*Nota sulle altre previsioni:* tra le altre indicazioni previste, "tumore benigno dell'apparato riproduttivo" ha livello L3 (studi osservazionali e istopatologici, in parte su flutamide in iperplasia prostatica benigna), mentre "tumore dell'apparato riproduttivo maschile" ha livello L1 solo perché include il carcinoma prostatico, già indicazione originale. Le altre (fibroma prostatico, tumore di Brenner, leiomioma prostatico, tumore filloide prostatico, HIV e infezioni correlate in modelli animali) hanno livello L5, senza evidenze di supporto.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

