---
layout: default
title: Paromomycin
parent: Solo previsione del modello (L5)
nav_order: 341
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Paromomycin: nuova indicazione prevista, Cirrosi associata al rame idiopatica (livello di evidenza L5). Indicazione originale: Coma epatico / encefalopatia epatica (dal grafo di conoscenza TxGNN"
monitor_inn: "paromomycin"
predicted_indications: ["idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatic porphyria", "acute urate nephropathy", "peritonitis"]
---

# Paromomycin
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

## Paromomicina: dall'encefalopatia epatica alla cirrosi associata al rame idiopatica
{: .text-alpha }

## Sintesi

La paromomicina è un antibiotico aminoglicosidico poco assorbito per via orale, originariamente usato nel coma epatico e nell'encefalopatia epatica. Il modello TxGNN la indica come potenzialmente efficace per la **cirrosi associata al rame idiopatica**, ma il supporto è solo computazionale: per questa indicazione non risultano **né studi clinici né pubblicazioni**.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Coma epatico / encefalopatia epatica (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Cirrosi associata al rame idiopatica |
| Punteggio di predizione TxGNN | 99,90% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (0 valide, 2 cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione potrebbe essere ragionevole (o no)

I dati compilati per questo report non includono una descrizione dettagliata del meccanismo d'azione. In generale, la paromomicina è un aminoglicoside con attività antibatterica e antiprotozoaria, scarsamente assorbito per via orale: nell'encefalopatia epatica riduce la carica batterica intestinale.

Non emerge alcun legame meccanicistico diretto con la cirrosi associata al rame, che dipende dal metabolismo del rame e non da un processo antibiotico-sensibile. Il punteggio elevato (0,999) riflette probabilmente la vicinanza, nel grafo, a nodi di malattie epatiche condivise con l'indicazione originale, e non una plausibilità biologica dimostrata.

Lo stesso punteggio è attribuito ad altre quattro predizioni (trombosi portale primitiva, sindrome epatopolmonare, sclerosi epatoportale, ipertensione portale non cirrotica familiare a esordio precoce), tutte prive di studi e con razionale solo ipotetico o speculativo. Il punteggio, quindi, discrimina poco.

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata alla cirrosi associata al rame idiopatica.

Per la predizione di rango 8, la **peritonite** (punteggio 99,03%), sono state recuperate 16 pubblicazioni, ma riguardano soprattutto la leishmaniosi (suscettibilità in vitro, resistenza, formulazioni, combinazioni) e l'amebiasi, non la peritonite. Si citano per trasparenza le più rilevanti:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [11096579](https://pubmed.ncbi.nlm.nih.gov/11096579/) | 1999 | Revisione | Curr Treat Options Gastroenterol | Gestione dell'amebiasi e dell'ascesso epatico amebico, principalmente con metronidazolo |
| [23833177](https://pubmed.ncbi.nlm.nih.gov/23833177/) | 2013 | Revisione | J Antimicrob Chemother | Effetti immunomodulatori dei farmaci antileishmania, tra cui la paromomicina |
| [21393188](https://pubmed.ncbi.nlm.nih.gov/21393188/) | 2011 | Studio in vitro | J Antimicrob Chemother | Interazioni in vitro tra sitamachina e altri farmaci, inclusa la paromomicina, contro Leishmania donovani |
| [26469696](https://pubmed.ncbi.nlm.nih.gov/26469696/) | 2015 | Studio in vitro | PLoS One | Fitness comparativa di un isolato di L. donovani e del ceppo resistente alla paromomicina |
| [23970484](https://pubmed.ncbi.nlm.nih.gov/23970484/) | 2014 | Studio in vitro | J Antimicrob Chemother | Interazione in vitro tra paromomicina solfato e quattro farmaci leishmanicidi |
| [22514145](https://pubmed.ncbi.nlm.nih.gov/22514145/) | 2013 | Studio preclinico (formulazione) | Drug Test Anal | Microsfere di albumina caricate con paromomicina per la leishmaniosi viscerale |
| [34840954](https://pubmed.ncbi.nlm.nih.gov/34840954/) | 2021 | Caso clinico | IDCases | Colite amebica fulminante trattata con metronidazolo e paromomicina durante chemioterapia |

Nessuna di queste pubblicazioni supporta un uso della paromomicina nella peritonite.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 020177010 | KAMAN*16 cps 250 mg (I.B.N. Savio Srl) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 016531016 | HUMATIN*16 cps 250 mg (Pfizer Italia Srl) | Non indicata | Non disponibile (autorizzazione cancellata) |

## Considerazioni di sicurezza

- **Controindicazioni derivate dal grafo di conoscenza** (non dal foglietto illustrativo): malattia renale, piouretere, disturbi dell'udito e sordità mista X-linked con gusher perilinfatico. Ciò è coerente con la nota tossicità renale e uditiva degli aminoglicosidi in caso di esposizione sistemica.
- **Interazioni farmacologiche**: sono state identificate 36 interazioni. Tra le principali:
  - **Maggiori**: miorilassanti non depolarizzanti (cisatracurio, atracurio, doxacurio, metocurina, mivacurio) e vaccino vivo contro il colera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderate**: inibitori di pompa protonica (omeprazolo, esomeprazolo, lansoprazolo, dexlansoprazolo, rabeprazolo), estrogeni (etinilestradiolo, estradiolo, mestranolo), metotrexato, micofenolato mofetile, enflurano, picosolfato e indio In-111 ossichinolina.
  - **Minori**: digossina.
- Per avvertenze e controindicazioni da etichetta, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (L5), senza studi clinici né letteratura per la cirrosi associata al rame idiopatica e senza un meccanismo plausibile. Inoltre in Italia le due autorizzazioni sono entrambe cancellate e i dati di sicurezza da etichetta mancano.

**Per procedere sarebbe necessario:**
- Recuperare il foglietto illustrativo AIFA (avvertenze e controindicazioni), necessario per qualsiasi valutazione di sicurezza.
- Ottenere dati sul meccanismo d'azione (ad es. da DrugBank) e valutare un'eventuale ipotesi biologica con il metabolismo del rame.
- Condurre una revisione sistematica della letteratura mirata e, se emergesse un razionale, studi preclinici.
- Valutare il profilo di sicurezza in caso di insufficienza epatica o renale, data la possibile esposizione sistemica e la tossicità degli aminoglicosidi.
- Considerare che, tra le predizioni elencate, nessuna ha evidenza clinica; la peritonite ha solo letteratura indiretta (L4) e non pertinente.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

