---
layout: default
title: Zonisamide
parent: Prove elevate (L1-L2)
nav_order: 216
evidence_level: L1
indication_count: 10
---

# Zonisamide
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **10** 
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

# Zonisamide: Dalle crisi parziali all'epilessia assenza

## Riassunto in una frase

La zonisamide è un farmaco antiepilettico a largo spettro (AED) approvato in molti paesi per il trattamento adiuvante delle crisi parziali (focali) in adulti. La predizione con il punteggio più alto del modello TxGNN è la **Sindrome di Tourette** (punteggio 99,85%), ma questa predizione attualmente non ha studi clinici o letteratura pubblicata che la supportino (L5). Questo rapporto si concentra sulla **predizione clinicamente più robusta: Epilessia assenza** (punteggio TxGNN 99,24%), supportata da **4 studi clinici** (inclusi due studi di Fase 3) e **20 pubblicazioni** — e rafforzata dall'approvazione normativa giapponese e dal consenso farmacologico consolidato sul meccanismo di blocco dei canali del calcio di tipo T della zonisamide.

---

## Panoramica rapida

| Item | Contenuto |
|------|---------|
| Indicazione originale | Epilessia — trattamento adiuvante delle crisi parziali (focali) in adulti (approvato in UE, Giappone, USA; attualmente non autorizzato in Italia) |
| Indicazione predetta | Epilessia assenza |
| Punteggio predizione TxGNN | 99,24% |
| Livello di evidenza | L1 |
| Stato del mercato italiano | ✗ Non commercializzato (0 autorizzazioni AIFA) |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Procedere con Guardrails |

---

## Perché questa predizione è ragionevole?

La zonisamide agisce attraverso molteplici meccanismi complementari: stabilizza le membrane neuronali bloccando i canali del sodio voltage-dipendenti, inibisce i canali del calcio di tipo T (Cav3.x), modula la trasmissione della dopamina e della serotonina, e debolmente inibisce l'anidrasi carbonica. Questo profilo multi-target la distingue dalla maggior parte degli AED e fornisce uno spettro anticonvulsivante ampio in molti tipi di crisi.

Il collegamento meccanicistico all'epilessia assenza è diretto e consolidato. Le crisi assenza (petit mal) originano da oscillazioni talamocorticali ritmiche guidate dai canali del calcio di tipo T nei neuroni di relè talamici e nelle cellule reticolari — lo stesso pathway bersaglio dell'etosuccimide, il trattamento di riferimento per l'epilessia assenza infantile e un puro bloccante dei canali del calcio di tipo T. Poiché la zonisamide condivide questo blocco dei canali di tipo T, la razionale farmacologica non è meramente inferenza da modello ma riflette il consenso neuroscientifico consolidato. Questo sovrapposizione con il meccanismo dell'etosuccimide è più convincente del collegamento più debole tra zonisamide e la maggior parte delle altre indicazioni predette da TxGNN.

A supporto di questo ragionamento dal punto di vista normativo e clinico: il Giappone ha approvato la zonisamide negli anni '80 in una vasta gamma di tipi di crisi incluse quelle generalizzate; una revisione di cartelle cliniche del 2005 (Wilfong & Schultz; n=45 pazienti pediatrici con crisi assenza) ha riportato che il 51,1% ha raggiunto la totale assenza di crisi sulla zonisamide; e una serie prospettica di casi del 2014 (Velizarova et al.) ha specificamente esaminato la zonisamide nell'epilessia assenza giovanile resistente ai farmaci. Due RCT multinazionali di Fase 3 (NCT00477295, NCT00848549) forniscono robusti dati di sicurezza ed efficacia nella popolazione epilettica più ampia, consentendo una valutazione della sicurezza fiduciosa per il riposizionamento nell'epilessia assenza.

---

## Evidenza da studi clinici

| Numero di studio | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT00477295](https://clinicaltrials.gov/study/NCT00477295) | Fase 3 | Completato | 583 | Studio randomizzato, multicentrico, in doppio cieco di non inferiorità confrontando zonisamide vs carbamazepina come monoterapia in epilessia parziale di nuova diagnosi; base di evidenza primaria per efficacia e sicurezza della zonisamide come monoterapia |
| [NCT00848549](https://clinicaltrials.gov/study/NCT00848549) | Fase 3 | Completato | 295 | Estensione in doppio cieco a lungo termine del programma di monoterapia di Fase 3; valuta la persistenza dell'efficacia e la sicurezza/tollerabilità a lungo termine della zonisamide, fornendo dati di follow-up di 2+ anni |
| [NCT07443241](https://clinicaltrials.gov/study/NCT07443241) | N/A | Completato | 779 | Analisi osservazionale retrospettiva di 779 pazienti trattati per status epilepticus (inclusa l'assenza) presso un ospedale universitario (2011–2023); valuta differenze specifiche per sesso in eziologia, trattamento e outcome — fornisce dati di trattamento dal mondo reale |
| [NCT04939675](https://clinicaltrials.gov/study/NCT04939675) | N/A | Sconosciuto | 40 | Studio di fattibilità che sviluppa un questionario di screening per l'epilessia revisionato incorporando nuove intuizioni sulla semiologia delle crisi; evidenza diretta limitata per l'efficacia della zonisamide nell'epilessia assenza |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|-----|------|------|---------|
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network Meta-analisi | Cochrane Database Syst Rev | Meta-analisi in rete aggiornata di dati di pazienti individuali sulla monoterapia con AED in tutti i tipi di epilessia; fornisce dati di efficacia comparativa e tollerabilità inclusa la zonisamide |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Linea guida di pratica clinica | Neurology | Linea guida aggiornata AAN/AES sull'efficacia dei nuovi AED come monoterapia iniziale per l'epilessia di nuova insorgenza; include livello di raccomandazione basato su evidenza per la zonisamide |
| [23350722](https://pubmed.ncbi.nlm.nih.gov/23350722/) | 2013 | Revisione sistematica ILAE | Epilepsia | Revisione sistematica complessiva ILAE dell'efficacia degli AED come monoterapia iniziale; assegna livelli di evidenza formali alla zonisamide in tutti i tipi di crisi |
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | Studio clinico | Epilepsy Res | Revisione di cartelle cliniche di 45 pazienti pediatrici (≤18 anni) con crisi assenza trattati con zonisamide; il 51,1% ha raggiunto la totale assenza di crisi — evidenza diretta chiave per l'epilessia assenza |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | Serie di casi prospettica | Epilepsy Res | Valutazione prospettica della zonisamide specificamente nell'epilessia assenza giovanile resistente ai farmaci (JAE); valuta l'efficacia in una popolazione con opzioni di trattamento limitate |
| [40351416](https://pubmed.ncbi.nlm.nih.gov/40351416/) | 2025 | Network Meta-analisi | Front Pharmacol | Network meta-analisi di singolo ASM come terapia adiuvante per l'epilessia focale farmaco-resistente; ranking di efficacia e sicurezza comparativa inclusa la zonisamide |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | Studio clinico | Epileptic Disord | Revisione retrospettiva di 15 pazienti con epilessia mioclonica giovanile trattati con zonisamide; riporta efficacia nei componenti di crisi assenza, mioclonica e generalizzate-tonico-cloniche, supportando l'attività a largo spettro |
| [16321507](https://pubmed.ncbi.nlm.nih.gov/16321507/) | 2006 | Revisione | Epilepsy Res | Sintesi dell'ampia esperienza clinica giapponese con zonisamide in adulti e bambini in tutti i tipi di crisi incluse le crisi assenza generalizzate; supporta il contesto normativo giapponese |
| [34941639](https://pubmed.ncbi.nlm.nih.gov/34941639/) | 2021 | Revisione narrativa | Pediatr Rep | Revisione terapeutica per l'epilessia assenza infantile inclusi i casi farmaco-resistenti; discute il ruolo dei nuovi AED e identifica la zonisamide come candidato per le presentazioni refrattarie |
| [16341290](https://pubmed.ncbi.nlm.nih.gov/16341290/) | 2005 | Revisione | Drugs Today | Revisione complessiva del profilo anticonvulsivante a largo spettro della zonisamide; documenta l'efficacia clinica nelle crisi assenza non responsive agli agenti di prima linea |

---

## Informazioni sul mercato italiano

La zonisamide **non è attualmente autorizzata in Italia** (0 registrazioni AIFA). Nessun prodotto in licenza è disponibile alla data di cutoff dei dati (2026-05-05).

Per riferimento, la zonisamide è commercializzata sotto il nome di brand **Zonegran®** (Eisai) in altri Stati Membri dell'UE (inclusi Germania, Francia e il Regno Unito precedentemente alla Brexit), ed è stata approvata negli Stati Uniti (Zonegran®, 2000) e in Giappone (Excegran®, 1989) — quest'ultimo coprendo uno spettro di crisi più ampio che include le crisi generalizzate. Un'autorizzazione all'immissione in commercio a livello europeo esiste, il che significa che la registrazione AIFA attraverso la procedura di mutuo riconoscimento o decentralizzata sarebbe una pathway normativa fattibile.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni complete sulla sicurezza. Nessun dato di interazione farmaco-farmaco o dati specifici su avvertenze/controindicazioni erano disponibili in questo Evidence Pack.

**Due importanti segnali di effetto avverso da notare, identificati durante la revisione delle evidenze:**

- **Rischio di metaemoglobinemia:** La zonisamide è un derivato solfonamidico. Le predizioni TxGNN #3, #4 e #6 (metaemoglobinemia di tipo alfa, metaemoglobinemia, deficienza di metaemoglobina reduttasi) sono state contrassegnate dalla pipeline come **avvertenze di sicurezza, non predizioni terapeutiche** — la zonisamide può *indurre* stress ossidativo e formazione di metaemoglobina. I pazienti con ipersensibilità ai solfonamidi o con deficienza pre-esistente di metaemoglobina reduttasi devono essere sottoposti a screening prima dell'uso.

- **Effetti avversi psichiatrici:** Un case report (PMID [2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/)) documenta mania indotta da zonisamide. Questo è rilevante quando si considera l'uso in popolazioni con comorbilità disturbi dell'umore.

---

## Conclusioni e passi successivi

**Decisione: Procedere con Guardrails**

**Razionale:**
Il blocco dei canali del calcio di tipo T della zonisamide fornisce una base meccanicistica convincente e farmacologicamente consolidata per l'efficacia nell'epilessia assenza. L'evidence package — inclusi due studi di Fase 3 completati, una meta-analisi in rete Cochrane, revisione sistematica ILAE, endorsement della linea guida AAN/AES, multiple serie di casi clinici direttamente in popolazioni con crisi assenza, e approvazione normativa giapponese per le crisi generalizzate — collettivamente soddisfa i criteri L1. Questo rappresenta il segnale di riposizionamento più robusto disponibile nell'intero Evidence Pack e giustifica il passaggio a una strategia di sviluppo clinico strutturata o regolamentare.

**Per procedere è necessario quanto segue:**

- **RCT dedicato di Fase 3 nell'epilessia assenza:** Gli studi di Fase 3 esistenti si concentravano sulle crisi parziali (focali); un trial double-blind prospettico specificamente nell'epilessia assenza infantile o giovanile è necessario per un'indicazione approvata da AIFA
- **Dati pediatrici di dosaggio e sicurezza:** La maggior parte dell'evidenza robusta deriva da studi su adulti con crisi parziali; i dati formali di dosaggio appropriato per l'età, PK e sicurezza nei bambini (la popolazione primaria di epilessia assenza) dovrebbero essere stabiliti formalmente
- **Pianificazione della pathway normativa AIFA:** Identificare la rotta più veloce verso l'autorizzazione del mercato italiano — mutuo riconoscimento da un titolare di autorizzazione di uno Stato Membro dell'UE esistente, o una nuova applicazione centralizzata EMA coprendo l'indicazione dell'epilessia assenza
- **Revisione completa del foglio illustrativo:** Ottenere e analizzare i dati completi di controindicazioni, avvertenze e DDI dai foggi illustrativi UE/USA/Giappone (non disponibili in questo Evidence Pack)
- **Protocollo di screening dell'ipersensibilità ai solfonamidi:** Data la rischiosità dell'effetto avverso metaemoglobinemia, sviluppare una checklist di pre-trattamento screening per lo stato di deficienza di G6PD e allergia ai solfonamidi

---

> **Riassunto di tutte le indicazioni predette da TxGNN (per riferimento):**
>
> | Rank | Indicazione | Punteggio TxGNN | Livello di evidenza | Decisione |
> |------|-----------|-------------|---------------|---------|
> | 1 | Sindrome di Tourette | 99,85% | L5 | Hold |
> | 2 | Tricotillomania | 99,78% | L5 | Hold |
> | 3 | Metaemoglobinemia (alfa) | 99,64% | L5 | ⚠️ Hold — preoccupazione di sicurezza (effetto avverso, non indicazione) |
> | 4 | Metaemoglobinemia | 99,63% | L5 | ⚠️ Hold — preoccupazione di sicurezza |
> | 5 | Angina di Prinzmetal | 99,55% | L5 | Hold |
> | 6 | Deficienza di metaemoglobina reduttasi | 99,53% | L5 | ⚠️ Hold — preoccupazione di sicurezza |
> | 7 | Disturbo bipolare affettivo maniacale | 99,35% | L3 | Domanda di ricerca (1 segnale RCT, campione insufficiente) |
> | **8** | **Epilessia assenza** | **99,24%** | **L1** | **✓ Procedere con Guardrails ← Focus primario di questo rapporto** |
> | 9 | Fibromialgia | 99,20% | L5 | Hold (1 trial ritirato prima dell'arruolamento) |
> | 10 | Congiuntivite | 99,16% | L5 | Hold |

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

