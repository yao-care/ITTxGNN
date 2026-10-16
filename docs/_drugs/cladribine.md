---
layout: default
title: Cladribine
parent: Solo previsione del modello (L5)
nav_order: 110
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Cladribine: nuova indicazione prevista, Rabdomiosarcoma embrionale parameningeo (livello di evidenza L5). Indicazione originale: Leucemia a cellule capellute"
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
---

# Cladribine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **7** 
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

# Cladribina: dalla leucemia a cellule capellute al rabdomiosarcoma embrionale parameningeo

## Sintesi

La cladribina è un analogo nucleosidico purinico, originariamente impiegato nel trattamento della leucemia a cellule capellute (hairy cell leukemia, anche nella variante) e della sclerosi multipla recidivante-remittente.
Il modello TxGNN ne predice una possibile efficacia nel **rabdomiosarcoma embrionale parameningeo**, con un punteggio molto alto (99,77%), ma **senza alcuno studio clinico né pubblicazione** a supporto: si tratta di una previsione puramente computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Leucemia a cellule capellute; sclerosi multipla recidivante-remittente (dalle indicazioni della base di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Rabdomiosarcoma embrionale parameningeo |
| Punteggio di previsione TxGNN | 99,77% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 3 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione registrato. In base alle conoscenze generali, la cladribina è un analogo nucleosidico purinico resistente all'adenosina deaminasi, fosforilato dalla deossicitidina chinasi. Si accumula come trifosfato, causando rotture del DNA e apoptosi, soprattutto nei linfociti.

Un effetto antiproliferativo sui tumori solidi è teoricamente plausibile, ma non è supportato da alcuna evidenza clinica o bibliografica. L'attività della cladribina dipende da un'elevata attività della deossicitidina chinasi rispetto alla 5'-nucleotidasi, caratteristica delle cellule linfoidi e non dimostrata nel rabdomiosarcoma. L'alto punteggio TxGNN è verosimilmente influenzato dalla vicinanza tra le diverse voci di rabdomiosarcoma nel grafo di conoscenza, più che da segnali indipendenti.

Le altre indicazioni previste hanno lo stesso profilo di evidenza (tutte L5, Hold): rabdomiosarcoma embrionale botrioide della vagina (99,77%), rabdomiosarcoma embrionale extraepatico delle vie biliari (99,76%), rabdomiosarcoma embrionale della prostata (99,75%), rabdomiosarcoma extraepatico delle vie biliari (99,75%) e rabdomiosarcoma in generale (99,74%). Per il sarcoma epatico (99,70%) l'unico elemento è un caso clinico su un'altra malattia (vedi sotto).

## Evidenze da studi clinici

Attualmente non risulta alcuno studio clinico correlato registrato.

## Evidenze dalla letteratura

Per l'indicazione principale non è disponibile letteratura correlata.

Per l'indicazione di rango 7 (sarcoma epatico) è presente un solo elemento, non pertinente:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) | 2004 | Caso clinico | Der Hautarzt | Terapia con cladribina in un caso di mastocitosi sistemica indolente (smoldering): malattia ematologica diversa, senza rilevanza diretta per il sarcoma epatico |

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Stato |
|---------|------|------|-----------|
| 045615010 | MAVENCLAD 1 cpr 10 mg (Merck Europe BV) | Non indicata | Cancellata |
| 045615046 | MAVENCLAD 6 cpr 10 mg (Merck Europe BV) | Non indicata | Cancellata |
| 045615022 | MAVENCLAD 4 cpr 10 mg (Merck Europe BV) | Non indicata | Cancellata |

## Citotossicità

La cladribina è un antineoplastico citotossico (analogo nucleosidico purinico, antimetabolita).

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Citotossico convenzionale (analogo purinico) |
| Rischio di mielosoppressione | Alto: le associazioni nella base di conoscenza con neutropenia, trombocitopenia, anemia e agranulocitosi indicano un rischio ematologico rilevante |
| Classificazione emetogena | Si rimanda alle avvertenze e precauzioni del foglietto illustrativo |
| Parametri da monitorare | Emocromo con formula, funzionalità renale ed epatica, funzione neurologica (neuropatia periferica) |
| Protezione nella manipolazione | Si raccomanda di seguire le norme per la manipolazione dei farmaci citotossici |

## Considerazioni di sicurezza

- **Controindicazioni/condizioni a rischio (dal grafo di conoscenza TxGNN, non dal testo del foglietto illustrativo)**: malattia renale, piouretere, trombocitopenia, iperuricemia, neutropenia, agranulocitosi, malattie del sistema nervoso periferico, neuropatia periferica, anemia, anemia macrocitica.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni; tra quelle riportate:
  - **Gravità maggiore**: corticosteroidi (idrocortisone, triamcinolone, desametasone, betametasone, budesonide, prednisolone, prednisone), deferiprone, ibritumomab tiuxetan, iobenguano (I-131), tositumomab (anche I-131), samario (153Sm) lexidronam, cloruro di stronzio Sr-89.
  - **Gravità moderata**: palifermin, dipiridamolo, cilostazolo, eltrombopag.
  - **Gravità non nota**: acido acetilsalicilico.

Per avvertenze e controindicazioni ufficiali si rimanda al foglietto illustrativo, attualmente non disponibile nei dati compilati.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Non esistono studi clinici né letteratura a supporto di alcuna delle indicazioni previste (livello L5, o L4 non pertinente per il sarcoma epatico). Il punteggio TxGNN elevato è solo computazionale, e il profilo di tossicità ematologica è rilevante. In Italia, inoltre, tutte le autorizzazioni risultano cancellate.

**Per procedere sono necessari:**
- Verifica preclinica: citotossicità in vitro su linee cellulari di rabdomiosarcoma ed espressione della deossicitidina chinasi.
- Dati ufficiali di sicurezza (avvertenze e controindicazioni) dal foglietto illustrativo AIFA.
- Dati dettagliati sul meccanismo d'azione (DrugBank).
- Chiarimento dello stato regolatorio in Italia (autorizzazioni cancellate) e delle indicazioni approvate.
- Una ricerca bibliografica mirata su cladribina e rabdomiosarcoma/sarcomi, prima di formulare una domanda di ricerca clinica.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

