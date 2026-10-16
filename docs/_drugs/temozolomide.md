---
layout: default
title: Temozolomide
parent: Prove elevate (L1-L2)
nav_order: 425
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-15
description: "Temozolomide: nuova indicazione prevista, Tumore astrocitico dell'adulto (livello di evidenza L1). Indicazione originale: Astrocitoma anaplastico, astrocitoma (escluso il glioblastoma)…"
---

# Temozolomide
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **2** 
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

# Temozolomide: Dal glioma astrocitario all'astrocitoma adulto (conferma d'uso esistente)

## Sintesi in una frase

Temozolomide è un agente alchilante orale, originariamente impiegato per il trattamento dell'astrocitoma anaplastico, dell'astrocitoma (escluso il glioblastoma) e del glioblastoma cerebrale.
Il modello TxGNN predice un possibile beneficio per il **tumore astrocitico dell'adulto**, ma questa indicazione si sovrappone di fatto a quelle già esistenti, quindi non è un vero riposizionamento. Il supporto è di **2 studi clinici** e **20 pubblicazioni**.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Astrocitoma anaplastico, astrocitoma (escluso il glioblastoma), glioblastoma cerebrale (dalle indicazioni del knowledge graph; nelle autorizzazioni AIFA il testo dell'indicazione non è disponibile) |
| Nuova indicazione prevista | Tumore astrocitico dell'adulto |
| Punteggio di predizione TxGNN | 99,36% |
| Livello di evidenza | L1 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

---

## Perché la predizione è ragionevole?

Temozolomide è un agente alchilante orale che metila il DNA (O6-guanina, N7-guanina, N3-adenina). Ciò causa lesioni citotossiche e porta all'apoptosi delle cellule tumorali. I dati di meccanismo d'azione compilati per questo report non sono disponibili; la descrizione si basa quindi sulle conoscenze farmacologiche generali.

I tumori astrocitici dell'adulto, compresi l'astrocitoma anaplastico e il glioblastoma, coincidono con le indicazioni originali del farmaco. Il legame meccanicistico è quindi diretto. L'efficacia è modulata dallo stato di metilazione del promotore di MGMT, il principale biomarcatore predittivo.

**Nota importante:** poiché l'indicazione prevista coincide con quelle già note, il caso rappresenta la conferma di un uso esistente più che un nuovo riposizionamento.

### Seconda predizione (a titolo informativo)

TxGNN prevede anche il **neoplasma della cauda equina** (punteggio 99,30%), per lo più ependimomi mixopapillari. Il meccanismo alchilante potrebbe applicarsi ai tumori gliali, ma la biologia differisce dai gliomi astrocitici e il ruolo di MGMT negli ependimomi spinali non è stabilito. L'evidenza si limita a un caso clinico (PMID 29270703) di risposta a temozolomide in un ependimoma mixopapillare spinale recidivante, senza studi clinici registrati. Livello di evidenza L4: resta una domanda di ricerca.

---

## Evidenza dagli studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Fase 3 | Completato | 500 | Studio randomizzato: temozolomide vs PCV (procarbazina, lomustina, vincristina) nei gliomi maligni ricorrenti (astrocitomi WHO grado III e IV) |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Fase 1 | Completato | 26 | Dose-finding di sicurezza e farmacocinetica di XL184 (cabozantinib) con temozolomide e radioterapia in prima linea nel glioblastoma; non valuta l'efficacia di temozolomide da sola |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Radioterapia più temozolomide concomitante e adiuvante vs sola radioterapia nel glioblastoma |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (follow-up a 5 anni) | Lancet Oncol | Analisi a 5 anni dello studio EORTC-NCIC: beneficio di sopravvivenza di temozolomide con radioterapia |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08: temozolomide da sola vs sola radioterapia nell'astrocitoma maligno dell'anziano |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09: lomustina-temozolomide vs temozolomide standard nel glioblastoma con MGMT metilato |
| [29260225](https://pubmed.ncbi.nlm.nih.gov/29260225/) | 2017 | RCT | JAMA | Campi a bassa intensità (TTFields) più temozolomide di mantenimento vs temozolomide da sola |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT (analisi ad interim) | JAMA | TTFields più temozolomide vs temozolomide da sola nel glioblastoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Aggiunta di bevacizumab nel glioblastoma di nuova diagnosi trattato con temozolomide e radioterapia |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | RCT | JAMA Oncol | Aggiunta di veliparib a temozolomide nel glioblastoma con MGMT metilato |
| [34898238](https://pubmed.ncbi.nlm.nih.gov/34898238/) | 2022 | Linea guida | J Clin Oncol | Linea guida ASCO-SNO sulla terapia dei tumori astrocitici e oligodendrogliali diffusi dell'adulto |
| [17478095](https://pubmed.ncbi.nlm.nih.gov/17478095/) | 2007 | Revisione | Crit Rev Oncol Hematol | Astrocitoma anaplastico dell'adulto: la chemioterapia ha dato risultati incoerenti, con una meta-analisi che mostra un beneficio modesto |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ve ne sono di valide. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati compilati. Si elencano le principali:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 034527174 | TEMODAL 5 bust 5 cps 140 mg | Merck Sharp & Dohme BV | Cancellata |
| 034527198 | TEMODAL 5 bust 5 cps 180 mg | Merck Sharp & Dohme BV | Cancellata |
| 034527212 | TEMODAL 5 bust 5 cps 250 mg | Merck Sharp & Dohme BV | Cancellata |
| 039649052 | TEMOZOLOMIDE 5 cps 100 mg | Teva B.V. | Cancellata |
| 042082077 | TEMOMEDAC 5 cps 140 mg | Medac GmbH | Cancellata |

---

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Citotossico convenzionale (agente alchilante, imidazotetrazinone) |
| Rischio di mielosoppressione | Da valutare: il knowledge graph segnala controindicazioni correlate a trombocitopenia, neutropenia, pancitopenia, anemia aplastica e linfopenia, coerenti con un rischio ematologico rilevante |
| Classificazione emetogenica | Medio (secondo la categoria del farmaco; consultare il foglio illustrativo) |
| Parametri da monitorare | Emocromo completo con formula, funzionalità epatica e renale |
| Protezione nella manipolazione | Seguire le norme di manipolazione dei farmaci citotossici |

---

## Considerazioni sulla sicurezza

- **Condizioni associate a controindicazione nel knowledge graph** (non dal testo del foglio illustrativo): insufficienza epatica, trombocitopenia, neutropenia, agranulocitosi, anemia (compresa quella macrocitica e aplastica idiopatica), pancitopenia, linfopenia, sindrome mielodisplastica, anemia aplastica e pneumocistosi.
- **Interazioni farmacologiche** (100 totali rilevate; livello principale):
  - Moderata: naltrexone
  - Minore: levofloxacina
  - Livello non classificato: tra gli altri calcitriolo, pantoprazolo, omeprazolo, lansoprazolo, doxiciclina, morfina, metformina, prednisone, idrocortisone, amfotericina B.

Per avvertenze e controindicazioni ufficiali fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esistono evidenze solide (livello L1) con RCT di fase 3 che sostengono l'uso di temozolomide nei tumori astrocitici dell'adulto. Tuttavia, l'indicazione coincide con quelle originali, quindi non si tratta di un vero riposizionamento. In Italia tutte le autorizzazioni risultano cancellate, e mancano i dati di sicurezza dal foglio illustrativo AIFA.

**Per procedere sono necessari:**
- Verificare perché le autorizzazioni sono cancellate (ritiro commerciale o altri motivi) e se esistono alternative disponibili in Italia
- Acquisire dal sito AIFA il foglio illustrativo con avvertenze e controindicazioni ufficiali
- Integrare i dati sul meccanismo d'azione da DrugBank
- Definire un piano di monitoraggio ematologico e della funzionalità epatica
- Per il neoplasma della cauda equina: servono studi clinici prospettici prima di qualsiasi valutazione, essendo oggi disponibile solo un caso clinico
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

