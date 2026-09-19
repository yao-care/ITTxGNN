---
layout: default
title: Modafinil
parent: Prove moderate (L3-L4)
nav_order: 149
evidence_level: L4
indication_count: 1
---

# Modafinil
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **1** 
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

# Modafinil: Da Narcolessia / Sonnolenza Diurna Eccessiva a Insonnia

## Riassunto in una frase

Il modafinil è un agente promotore della veglia approvato a livello globale per la narcolessia, l'eccessiva sonnolenza associata all'apnea ostruttiva del sonno e il disturbo del sonno legato al lavoro a turni — ma attualmente non dispone di autorizzazione all'immissione in commercio in Italia.
Il modello TxGNN predice che potrebbe avere rilevanza per l'**Insonnia**, con **29 studi clinici** e **19 pubblicazioni** identificate nella ricerca sulle prove.
Tuttavia, la stragrande maggioranza affronta la sonnolenza diurna piuttosto che l'insonnia direttamente, e un fondamentale paradosso meccanicistico mina significativamente la plausibilità di questa previsione.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originaria | Narcolessia, eccessiva sonnolenza associata a OSA, disturbo del sonno legato al lavoro a turni (approvato a livello globale; nessuna autorizzazione all'immissione in commercio in Italia) |
| Indicazione prevista | Insonnia (malattia) |
| Punteggio di previsione TxGNN | 99.85% |
| Livello di evidenza | L4 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | In sospeso |

---

## Perché questa previsione è ragionevole?

I dati dettagliati sul meccanismo d'azione non sono disponibili in questo Evidence Pack. Sulla base della letteratura pubblicata, il modafinil è un agente promotore della veglia che inibisce il trasportatore della dopamina (DAT), aumentando così la disponibilità di dopamina sinaptica nei circuiti promotori della veglia. Migliora anche la segnalazione di noradrenalina (NE) e orexina/ipocretina — effetti che collettivamente sostengono l'allerta e contrastano la sonnolenza patologica. Queste proprietà sono alla base dei suoi usi approvati nella narcolessia, nell'apnea ostruttiva del sonno (eccessiva sonnolenza residua) e nel disturbo del sonno legato al lavoro a turni.

Poiché il modafinil porta indicazioni approvate su molteplici sottotipi di disturbi del sonno, tutti i quali si raggruppano insieme nel grafo della conoscenza TxGNN, il modello probabilmente ha generato un punteggio di previsione elevato (99.85%) basato sulla prossimità topologica al nodo insonnia piuttosto che su un segnale terapeutico direzionale. Uno studio di Fase 4 (NCT00124384) ha specificamente arruolato pazienti con insonnia primaria, sebbene l'obiettivo dello studio fosse di migliorare il *funzionamento diurno* quando il modafinil è stato aggiunto alla terapia cognitivo-comportamentale — non per trattare direttamente le difficoltà di sonno notturno.

**Preoccupazione meccanicistica critica:** Esiste un paradosso fondamentale al centro di questa previsione. L'insonnia è caratterizzata da veglia indesiderata e difficoltà nel mantenere il sonno, e il trattamento efficace richiede agenti che facilitino l'inizio del sonno o il suo mantenimento. Il modafinil, tuttavia, *promuove* la veglia — ed è esso stesso classificato come un farmaco che può *causare* insonnia come effetto avverso. Questa previsione quasi certamente riflette un falso positivo del grafo della conoscenza: la prossimità del grafo ai nodi dei disturbi del sonno non cattura la direzionalità dell'azione farmacologica. Questa previsione deve essere interpretata con estrema cautela e non costituisce un candidato credibile al riposizionamento senza una ulteriore giustificazione meccanicistica.

---

## Prove da studi clinici

| Numero trial | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completato | 40 | **Modafinil** da solo o combinato con CBT-I nell'insonnia primaria; l'obiettivo principale era il miglioramento del funzionamento diurno, con valutazione secondaria della gravità dell'insonnia — non costituisce uno studio sul trattamento dell'insonnia |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Fase 2 | Completato | 138 | CBT-I ± armodafinil per insonnia e affaticamento in sopravvissuti al cancro al seno dopo chemioterapia; disegno a quattro bracci; l'armodafinil era inteso a contrastare l'affaticamento correlato al cancro, non come ausilio diretto del sonno |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Fase 2 | Completato | 226 | CBT-I ± armodafinil nei sopravvissuti al cancro con insonnia e affaticamento dopo chemioterapia; stessa logica di NCT01091974 — studio gemello più ampio |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Fase 2 | Completato | 70 | Studio pilota di BBT-I ± armodafinil 150 mg/giorno in pazienti con cancro al seno con insonnia; disegno preliminare, potenza limitata |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completato | 39 | Armodafinil e/o CBT-I per insonnia comorbida con apnea ostruttiva del sonno; valutati continuità del sonno e aderenza CPAP — campione piccolo, nessuna designazione di Fase |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Fase 2 | Completato | 830 | Piattaforma RECOVER-SLEEP: valutazione multi-intervento per disturbi del sonno nel Long COVID (PASC); il ruolo specifico del modafinil non è chiaro dal riassunto |
| [NCT06404099](https://clinicaltrials.gov/study/NCT06404099) | Fase 2 | Attivo, non in reclutamento | 361 | Piattaforma RECOVER-SLEEP: valutazione in corso di interventi per disturbi del sonno PASC; risultati in sospeso |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Fase 4 | Completato | 18 | **Modafinil** per disfunzione circadiana e cognitiva nel disturbo bipolare stabile; sonno misurato come endpoint secondario — campione molto piccolo (n=18) |
| [NCT00233090](https://clinicaltrials.gov/study/NCT00233090) | Fase 2 | Terminato | 21 | **Modafinil** vs. placebo per affaticamento post-TBI; terminato precocemente — prove insufficienti |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminato | 2 | **Modafinil** per disturbi del sonno/veglia in anziani; terminato dopo l'arruolamento di soli 2 partecipanti — nessuna conclusione possibile |

---

## Prove dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|---------|---------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisione basata su prove | *Drugs* | Revisione completa basata su RCT degli usi del modafinil approvati e investigazionali; conferma il profilo promotore della veglia nella narcolessia, OSA, SWSD e stati di affaticamento — nessun supporto per il trattamento dell'insonnia primaria |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisione sistematica / Meta-analisi | *PLoS One* | Il modafinil riduce significativamente l'affaticamento e l'eccessiva sonnolenza diurna in molteplici disturbi neurologici; conferma l'effetto promotore della veglia unidirezionale |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisione nello stile Cochrane | *Parkinsonism & Related Disorders* | Il modafinil migliora la sonnolenza diurna nella malattia di Parkinson; non affronta l'insonnia come obiettivo terapeutico |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisione linee guida EBM | *Movement Disorders* | Revisione basata su prove MDS dei trattamenti non motori del Parkinson; il modafinil è raccomandato per l'eccessiva sonnolenza diurna — non per l'insonnia |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Revisione narrativa | *Expert Opinion on Pharmacotherapy* | Gestione farmacologica e non farmacologica dei disturbi del sonno nella malattia di Parkinson; il modafinil discusso per la sonnolenza, non per l'insonnia |
| [15824337](https://pubmed.ncbi.nlm.nih.gov/15824337/) | 2005 | RCT | *Neurology* | Modafinil per affaticamento nella sclerosi multipla; conferma l'effetto promotore della veglia — nessun endpoint specifico per l'insonnia |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | RCT | *J Head Trauma Rehabilitation* | Modafinil per affaticamento e eccessiva sonnolenza diurna nel TBI cronico; nessun endpoint specifico per l'insonnia |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisione | *Drugs* | Disturbo del sonno legato al lavoro a turni: onere e gestione; il modafinil riduce l'EDS nel SWSD — direzionalità opposta alla terapia dell'insonnia |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Revisione | *Revue Neurologique* | Narcolessia con cataplessia; l'insonnia nel mantenimento del sonno annotata come sintomo della narcolessia, ma il ruolo del modafinil è rivolto alla sonnolenza diurna, non al sonno notturno |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Revisione | *Expert Opinion on Emerging Drugs* | Trattamenti emergenti per la narcolessia; il modafinil esaminato come la principale farmacoterapia per l'EDS diurno — non applicabile all'insonnia |

---

## Informazioni sul mercato italiano

Il modafinil attualmente **non ha autorizzazioni all'immissione in commercio** registrate in Italia. Non sono disponibili dati di licenza o indicazioni approvate per questo rapporto.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: In sospeso**

**Logica:**
Questa previsione TxGNN presenta un paradosso meccanicistico fondamentale — il modafinil è un agente promotore della veglia la cui farmacologia di base va direttamente contro l'obiettivo della terapia dell'insonnia, e nessun RCT completato ha dimostrato l'efficacia del modafinil come trattamento dell'insonnia primaria. Il punteggio di previsione elevato (99.85%) molto probabilmente riflette un falso positivo del grafo della conoscenza derivante dalla ampia presenza del modafinil nello spazio delle malattie dei disturbi del sonno, non un genuino segnale terapeutico.

**Per procedere, quanto segue è necessario:**
- Un'ipotesi meccanicistica credibile che spieghi come un agente promotore della veglia potrebbe beneficiare l'insonnia (ad es. consolidamento della veglia diurna migliorando l'architettura del sonno notturno attraverso la pressione omeostatica del sonno)
- Recupero dei dati completi del foglio illustrativo EMA/AIFA (avvertenze, controindicazioni, interazioni farmacologiche) prima di qualsiasi ulteriore pianificazione normativa o clinica
- Studio meccanicistico mirato o preclinico che esamini gli effetti bidirezzionali del sonno-veglia del modafinil, in particolare gli effetti sull'architettura del sonno notturno (polisonnografia)
- Se un'ipotesi plausibile emerge, uno studio di proof-of-concept di Fase 2 piccolo nell'insonnia primaria con endpoint basati su PSG obiettivi sarebbe necessario prima che qualsiasi percorso di riposizionamento possa essere considerato

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

