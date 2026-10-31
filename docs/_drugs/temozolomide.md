---
layout: default
title: Temozolomide
parent: Solo previsione del modello (L5)
nav_order: 425
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-31
description: "Temozolomide: nuova indicazione prevista, neoplasia della cauda equina (livello di evidenza L5). Indicazione originale: Astrocitoma anaplastico, astrocitoma (escluso il glioblastoma)…"
---

# Temozolomide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

## Temozolomide: neoplasia della cauda equina
{: .text-alpha }

## Sintesi in una frase

Temozolomide è un agente alchilante orale, noto per l'uso in tumori cerebrali di origine gliale (astrocitoma anaplastico, astrocitoma, glioblastoma). Il modello TxGNN (deep learning) ne prevede una possibile efficacia nella **neoplasia della cauda equina**, ma al momento sono disponibili **0 studi clinici** e solo **3 pubblicazioni** (tutti case report, di cui uno solo realmente pertinente a questa patologia).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Astrocitoma anaplastico, astrocitoma (escluso il glioblastoma), glioblastoma cerebrale (relazioni registrate nel knowledge graph; il testo delle indicazioni nelle autorizzazioni italiane non è disponibile) |
| Nuova indicazione prevista | Neoplasia della cauda equina |
| Punteggio di previsione TxGNN | 0,9930 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | almeno 20 |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

I dati di meccanismo d'azione compilati per questo report non sono disponibili. In base alle conoscenze farmacologiche generali, temozolomide è un agente alchilante orale che metila il DNA (O6-guanina, N7-guanina, N3-adenina), causando lesioni citotossiche e apoptosi nelle cellule tumorali in divisione. La sua attività dipende in larga misura dalla metilazione del promotore di MGMT: una bassa espressione di MGMT aumenta la sensibilità al farmaco.

Il farmaco penetra nel sistema nervoso centrale ed è utilizzato nei gliomi primari del SNC. I tumori della cauda equina sono più spesso ependimomi mixopapillari, di derivazione gliale, e ciò rende biologicamente plausibile un'estensione dell'uso. Il punteggio TxGNN (modello di deep learning) è molto alto (0,9930) e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenza biologica; resta una previsione computazionale.

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report con revisione | European Spine Journal | Efficacia notevole di temozolomide in un ependimoma mixopapillare spinale recidivante, con recidive multiple e disseminazione liquorale |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Carcinoma NUT nasale con risposte ripetute durante trattamento multimodale con radioterapia; non riguarda direttamente la cauda equina |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report con revisione | Neuro-Chirurgie | Criptococcosi neuromeningea atipica in un bambino trattato per glioma del ponte; non riguarda direttamente la cauda equina |

Il primo case report riguarda un ependimoma mixopapillare spinale (tumore tipico della regione terminale del midollo e della cauda equina), che è affine alla patologia prevista ma non coincide esattamente con la "neoplasia della cauda equina". Nessuna pubblicazione citata studia direttamente la patologia prevista come entità definita con un disegno di studio solido; per questo il livello di evidenza è fissato a L5.

## Informazioni sul mercato italiano

Sono presenti almeno 20 autorizzazioni valide per il principio attivo singolo; l'elenco può essere parziale. Il testo delle indicazioni approvate non è riportato nei dati compilati.

| Numero di autorizzazione | Nome del prodotto | Titolare | Indicazione approvata |
|---------|------|------|-----------|
| 039649052 | Temozolomide 5 cps 100 mg | TEVA B.V. | Non disponibile |
| 039649090 | Temozolomide 5 cps 180 mg | TEVA B.V. | Non disponibile |
| 039761337 | Temozolomide 5 cps 180 mg | Accord Healthcare SLU | Non disponibile |
| 041333131 | Temozolomide 5x1 cps 5 mg | Sun Pharmaceutical Ind. EU B.V. | Non disponibile |
| 034527174 | Temodal 5 cps 140 mg | Merck Sharp & Dohme BV | Non disponibile |

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Citotossico convenzionale (agente alchilante) |
| Rischio di mielosoppressione | Si vedano le avvertenze e precauzioni del foglio illustrativo; il knowledge graph registra controindicazioni legate a neutropenia, trombocitopenia, pancitopenia, anemia aplastica e linfopenia |
| Classificazione emetogenica | Si vedano le avvertenze e precauzioni del foglio illustrativo |
| Parametri da monitorare | Emocromo completo con formula, funzionalità epatica e renale |
| Protezione nella manipolazione | Seguire le norme per la manipolazione dei farmaci citotossici |

## Considerazioni di sicurezza

- **Controindicazioni registrate nel knowledge graph** (non derivate dal testo del foglio illustrativo): insufficienza epatica, trombocitopenia, neutropenia, agranulocitosi, anemia (anche macrocitica), pneumocistosi, pancitopenia, linfopenia, sindrome mielodisplastica, anemia aplastica idiopatica e anemia aplastica.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle elencate, naltrexone è di livello moderato e levofloxacina di livello minore. Le altre (ad es. calcitriolo, pantoprazolo, doxiciclina, clotrimazolo, morfina, metformina, omeprazolo, lansoprazolo, prednisone, idrocortisone) hanno gravità non classificata.

Per le avvertenze e le controindicazioni ufficiali, fare riferimento al foglio illustrativo AIFA, non ancora analizzato.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa su un punteggio computazionale elevato e su un solo case report pertinente (ependimoma mixopapillare spinale), senza studi clinici registrati. Mancano inoltre il testo delle indicazioni e le avvertenze del foglio illustrativo, necessari per la valutazione di sicurezza.

**Per procedere sono necessari:**
- Studi clinici o serie di casi più ampie su ependimomi mixopapillari/tumori della cauda equina trattati con temozolomide
- Acquisizione e analisi del foglio illustrativo AIFA (avvertenze, controindicazioni, indicazioni approvate)
- Dati sul meccanismo d'azione da DrugBank
- Dati sulla via di somministrazione e sullo stato di metilazione di MGMT in questi tumori
- Piano di monitoraggio ematologico, data la mielosoppressione segnalata
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

