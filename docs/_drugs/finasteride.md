---
layout: default
title: Finasteride
parent: Solo previsione del modello (L5)
nav_order: 198
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Finasteride: nuova indicazione prevista, Ipertricosi universale congenita di tipo Ambras (livello di evidenza L5). Indicazione originale: Iperplasia prostatica benigna (dato dal grafo di conoscenza"
---

# Finasteride
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

# Finasteride: Dall'iperplasia prostatica benigna all'ipertricosi

## Sintesi in una frase

Finasteride è un inibitore della 5-alfa-reduttasi di tipo II, originariamente utilizzato per il trattamento dell'iperplasia prostatica benigna.
Il modello TxGNN ne prevede una possibile efficacia per l'**ipertricosi** (e, con punteggio leggermente più alto, per la sindrome di Ambras), ma al momento non risultano **studi clinici** registrati e sono disponibili solo **4 pubblicazioni** di tipo generale, senza evidenza diretta di efficacia.

---

## Panoramica rapida

Nota: la predizione con rango 1 (sindrome di Ambras) è priva di qualsiasi evidenza e di un razionale meccanicistico plausibile. Per questo la tabella riporta la predizione di rango 1 come indicato nel modello di report, mentre l'analisi delle evidenze si concentra sull'ipertricosi (rango 2), l'unica con letteratura associata.

| Voce | Contenuto |
|------|------|
| Indicazione originale | Iperplasia prostatica benigna (dato dal grafo di conoscenza; il testo delle indicazioni autorizzate non è disponibile) |
| Nuova indicazione prevista (rango 1) | Ipertricosi universale congenita di tipo Ambras |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L5 (L4 per l'ipertricosi, rango 2) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo report. In base alle conoscenze generali, finasteride inibisce la 5-alfa-reduttasi di tipo II e riduce i livelli di diidrotestosterone (DHT). Questo meccanismo è alla base della sua efficacia nell'iperplasia prostatica benigna e nell'alopecia androgenetica.

Per la **sindrome di Ambras** (rango 1) il legame meccanicistico è debole: si tratta di una condizione congenita legata a riarrangiamenti cromosomici che alterano la regolazione di TRPS1, non primariamente guidata dagli androgeni. L'alto punteggio (0,99994) deriva solo dal grafo di conoscenza.

Per l'**ipertricosi** (rango 2) il collegamento è anch'esso limitato. L'ipertricosi riguarda aree non androgeno-dipendenti, mentre finasteride agisce su condizioni androgeno-dipendenti come l'alopecia androgenetica e, in parte, l'irsutismo. L'unico punto di contatto è la sovrapposizione con l'irsutismo. Le altre predizioni (malformazioni odontali/parodontali, sindrome di Dandy-Walker, anomalie genetiche isolate del fusto del capello, tricomegalia familiare isolata) non mostrano un meccanismo plausibile e sembrano artefatti del grafo. Per la sindrome di Dandy-Walker si aggiungono possibili preoccupazioni di sicurezza, poiché gli antiandrogeni influenzano lo sviluppo.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Pubblicazioni associate all'ipertricosi (rango 2):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Revisione | Ann Dermatol Venereol | Distingue ipertricosi (aree non androgeno-dipendenti, spesso iatrogena o metabolica) da irsutismo; non richiede monitoraggio ormonale |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Revisione | Ther Umsch | Panoramica dei trattamenti per alopecia androgenetica e irsutismo |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Revisione | Hautarzt | Finasteride per la calvizie maschile; laser per ipertricosi e irsutismo |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Altro (strumento diagnostico) | Hautarzt | Descrizione di TrichoScan per l'analisi digitale dei capelli |

Si tratta di articoli narrativi di contesto: nessuno fornisce evidenza diretta dell'efficacia di finasteride nell'ipertricosi.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ve ne sono di valide. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili. Principali autorizzazioni (compresse rivestite da 5 mg):

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 028308017 | Proscar, 15 cpr rivestite 5 mg | Organon Italia Srl | Cancellata |
| 038791024 | Finasteride, 15 cpr rivestite 5 mg | Teva Italia Srl | Cancellata |
| 038413011 | Finestar, 15 cpr rivestite 5 mg | Eberlife Farmaceutici SpA | Cancellata |
| 038443014 | Stecur, 15 cpr rivestite 5 mg | Genetic SpA | Cancellata |
| 039681010 | Terip, 15 cpr rivestite 5 mg | Pharmacare Srl | Cancellata |

---

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo)**: malattia epatica, malattia della colecisti.
- **Interazioni farmacologiche**: sono state identificate 100 possibili interazioni, ma per quelle esaminate il livello di gravità è sconosciuto. Tra i farmaci coinvolti: calcitriolo, doxiciclina, clotrimazolo, dolasetron, dicicloverina, clorexidina, famotidina, acido acetilsalicilico, amoxicillina, bupropione, pantoprazolo, glimepiride, mesalazina, acarbosio, morfina, metformina, omeprazolo, sucralfato, palonosetrone, rosiglitazone.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Le predizioni hanno punteggi TxGNN molto alti ma si basano solo sul grafo di conoscenza: nessuno studio clinico, letteratura solo di contesto, meccanismo poco plausibile (ipertricosi non androgeno-dipendente). Inoltre non esistono autorizzazioni italiane valide. Per l'ipertricosi (rango 2) può essere considerata al più una domanda di ricerca (L4).

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione da DrugBank
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Evidenza preclinica o clinica diretta sull'efficacia di finasteride nell'ipertricosi, o nella sottopopolazione con componente androgeno-dipendente (irsutismo)
- Valutazione del livello di gravità delle interazioni farmacologiche
- Verifica della situazione regolatoria in Italia, dato che tutte le autorizzazioni sono cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

