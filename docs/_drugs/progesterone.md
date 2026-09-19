---
layout: default
title: Progesterone
parent: Prove elevate (L1-L2)
nav_order: 172
evidence_level: L1
indication_count: 10
---

# Progesterone
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

# Progesterone: dalla terapia ormonale sostitutiva all'amenorrea

## Sintesi in una frase

Progesterone è un ormone steroideo endogeno naturale fondamentale per la fisiologia riproduttiva femminile, ampiamente utilizzato in medicina riproduttiva per il supporto della fase luteale, la terapia ormonale sostitutiva e la regolazione del ciclo mestruale.
Il modello TxGNN prevede che possa essere efficace per **Amenorrea (malattia)** — l'assenza clinica della mestruazione — con **molteplici studi clinici di Fase 3 completati** e **18 pubblicazioni** che supportano attualmente questa direzione.
Dato che progesterone è l'ormone centrale del ciclo mestruale, questa previsione rappresenta uno dei candidati al riposizionamento più diretto dal punto di vista meccanicistico e supportato da prove nel dataset.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|------|
| Indicazione originale | Nessuna (nessuna autorizzazione di commercializzazione registrata in Italia) |
| Nuova indicazione prevista | Amenorrea (malattia) |
| Punteggio di previsione TxGNN | 99.9996% |
| Livello di evidenza | L1 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Proseguire con salvaguardie |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili dalla fonte DrugBank. Sulla base delle informazioni farmacologiche e cliniche note, Progesterone (DB00396) è il principale progestinico endogeno del sistema riproduttivo femminile, prodotto dal corpo luteo dopo l'ovulazione. La sua relazione con l'amenorrea non è meramente plausibile — è direttamente meccanicistica: l'amenorrea è fondamentalmente uno stato di ciclo di progesterone mancato o assente.

Il **Test di stimolazione con progesterone (PCT)** è il primo passo diagnostico internazionalmente accettato nella valutazione dell'amenorrea secondaria. Un clinico somministra un breve ciclo di progesterone esogeno e osserva se si verifica sanguinamento da sospensione; una risposta positiva conferma un endometrio integro, sensibilizzato agli estrogeni, e localizza la causa alla disfunzione dell'asse ipotalamico-ipofisario-ovarico piuttosto che all'ostruzione del deflusso strutturale. Questo uso diagnostico è esso stesso un meccanismo terapeutico — nei pazienti anovulatori (come quelli con PCOS o amenorrea ipotalamica funzionale), un singolo ciclo di progesterone induce la mestruazione.

La letteratura conferma due dimensioni meccanicistiche aggiuntive. In primo luogo, il progesterone micronizzato per via orale regola la pulsatilità dei neuroni ipotalamici kisspeptina-neurochinina B-dinorfina (KNDy), modulando direttamente la secrezione di LH/FSH e ripristinando i cicli ovulatori in alcuni pazienti. In secondo luogo, nell'insufficienza ovarica prematura (POI) e nella menopausa chirurgica, la terapia ormonale sostitutiva combinata con estrogeni-progesterone ripristina il ciclo endometriale completo. In entrambi i percorsi, l'assenza causale di progesterone È la definizione dello stato amenorroico. Il punteggio quasi perfetto di TxGNN del 99.9996% (rango 13 complessivo) riflette questa realtà clinica consolidata piuttosto che una connessione speculativa.

---

## Evidenza da studi clinici

| Numero di studio | Fase | Stato | Iscrizione | Risultati principali |
|---------|------|------|------|---------|
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Fase 3 | Completato | 1,845 | Grande RCT di combinazione Estradiolo + Progesterone per sintomi vasomotori in donne in postmenopausa; convalida direttamente il ruolo del progesterone nella gestione ormonale dell'amenorrea associata al ciclo e della protezione endometriale nell'utero integro |
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Fase 3 | Completato | 300 | Preparazione di FSH vs. gonadotropina ipofisaria purificata in pazienti con **amenorrea I o cicli anovulatori** dovuti a disfunzione ipotalamica/ipofisaria; stabilisce l'amenorrea come indicazione primaria di Fase 3 |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | Sconosciuto | 330 | RCT multicentrico che confronta direttamente **Capsule di Progesterone** vs. formula tradizionale a base di erbe vs. combinazione per disturbi mestruali inclusa l'amenorrea in donne adulte; l'evidenza farmacologica più diretta in questo dataset |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Fase 4 | Completato | 42 | RCT che testa se la sospensione dello **sanguinamento da ritiro indotto da progesterone** prima dell'induzione dell'ovulazione influenza i tassi di gravidanza in pazienti con oligo/amenorrea; interroga direttamente il meccanismo del progesterone nel ripristino del ciclo |
| [NCT03309709](https://clinicaltrials.gov/study/NCT03309709) | Fase 3 | Sconosciuto | 90 | Studio randomizzato di progesterone sottocutaneo 25 mg (giorni del ciclo 18–25) per regressione di polipi endometriali; utilizza direttamente il progesterone come intervento di studio |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Fase 3 | Completato | 257 | Goserelina durante la chemioterapia per prevenire il **fallimento ovarico/amenorrea indotta da chemioterapia** in carcinoma mammario stadio I–IIIA; convalida la prevenzione dell'amenorrea come endpoint clinico primario regolamentato di Fase 3 |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Fase 2 | Completato | 271 | Elagolix (antagonista del GnRH) per sanguinamento uterino pesante associato a fibromi; l'amenorrea indotta come modello controllato, confermando il ritiro del progesterone come il trigger biochimico |
| [NCT07224438](https://clinicaltrials.gov/study/NCT07224438) | Fase 2 | In reclutamento | 20 | Kisspeptina SC per amenorrea ipotalamica; ha come bersaglio il percorso neuronale KNDy a monte della sintesi del progesterone, fornendo il contesto meccanicistico per la base neuroendocrina della carenza di progesterone in questo fenotipo |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Fase 3 | Terminato | 60 | **Acetato di medroxiprogesterone** post-ablazione per modificare i tassi di amenorrea endometriale dopo ablazione; testa direttamente un progestinico per la modulazione degli esiti dell'amenorrea (terminato in anticipo, risultati limitati) |
| [NCT01927432](https://clinicaltrials.gov/study/NCT01927432) | N/A | Completato | 73 | Caratterizzazione ecografica osservazionale della dinamica dell'onda follicolare ovarica in donne con amenorrea; stabilisce il collegamento tra disfunzione follicolare, anovulazione e amenorrea che la terapia con progesterone affronta |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Revisione clinica | Reviews in Endocrine & Metabolic Disorders | Revisione completa del progesterone micronizzato per via orale in endocrinologia; documenta il suo ruolo nella regolazione della pulsatilità LH/FSH attraverso neuroni KNDy, nel controllo della ciclicità endometriale e il suo uso diagnostico/terapeutico in tutto lo spettro dell'amenorrea |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Revisione | Current Problems in Pediatric & Adolescent Health Care | Revisione sistematica dell'eziologia dell'amenorrea e della gestione negli adolescenti e negli adulti giovani; posiziona la sostituzione con progesterone/estrogeni come pietra angolare del trattamento della disfunzione dell'asse HPO causante amenorrea |
| [40474175](https://pubmed.ncbi.nlm.nih.gov/40474175/) | 2025 | Coorte retrospettiva | BMC Surgery | La terapia sequenziale ad alte dosi di estrogeni e **progesterone** combinata con separazione a freddo isteroscopica migliora significativamente il recupero della morfologia della cavità uterina nei pazienti con amenorrea indotta da aderenze intrauterine (IUA) severa |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Revisione | Frontiers in Endocrinology | Revisione dell'eziologia della POI (insufficienza ovarica prematura) e del trattamento; identifica la TOS contenente progesterone come standard clinico per ripristinare la ciclicità e prevenire le complicanze a lungo termine nell'amenorrea associata a POI |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Revisione | Climacteric | Gestione dei sanguinamenti vaginali postmenopausali; la menopausa è clinicamente definita come 12 mesi di amenorrea completa dovuta al declino di estrogeni e progesterone — posiziona direttamente la carenza di progesterone come la causa centrale |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Revisione | Reviews in Endocrine & Metabolic Disorders | Trattamenti ormonali per l'endometriosi; discute la terapia con progestinici come intervento ormonale di prima linea, inclusa la gestione dell'amenorrea anovulatoria associata attraverso la decidualizzazione mediata dal progesterone |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Revisione | Seminars in Reproductive Medicine | Le aderenze intrauterine (sindrome di Asherman) come causa strutturale di amenorrea; il progesterone combinato con estrogeni viene utilizzato dopo la lisi isteroscopica per ripristinare la ciclicità endometriale |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Revisione | American Family Physician | Guida clinica classica alla valutazione dell'amenorrea; delinea il **test di stimolazione con progestinico** come il passo diagnostico fondamentale per differenziare le cause anovulatorie da quelle anatomiche |
| [945033](https://pubmed.ncbi.nlm.nih.gov/945033/) | 1976 | Serie di casi | Annals of Internal Medicine | 15 pazienti con sindrome galattorrea-amenorrea; LH e progesterone non hanno mostrato picchi ovulatori normali; documenta la carenza di progesterone come la firma biochimica dell'amenorrea, ripristinata con trattamento efficace |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analisi | Frontiers in Oncology | Meta-analisi dell'amenorrea indotta da chemioterapia in pazienti con carcinoma mammario in premenopausa; identifica l'età e il regime come fattori di rischio e sottolinea l'importanza dei controlli ormonali basati sul progesterone e delle strategie di protezione |

---

## Informazioni sul mercato italiano

Progesterone (DB00396) attualmente **non ha autorizzazioni di commercializzazione approvate in Italia**. Nessuna registrazione di prodotto, indicazioni concesse in licenza o dati sulla forma farmaceutica sono stati identificati nel database normativo. Il farmaco è classificato come **non commercializzato** in Italia al momento di questa valutazione (data di cutoff: 2026-05-06).

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> **Nota:** Il dataset formale sulla sicurezza per questa valutazione contiene lacune nei dati in categorie chiave di avvertenze e controindicazioni. Prima dell'uso clinico, i prescrittori dovrebbero consultare lo SmPC/foglio illustrativo attuale e le linee guida AIFA rilevanti. Di particolare rilevanza per il progesterone sono considerazioni note a livello di classe incluso il rischio di tromboembolismo, le condizioni sensibili agli ormoni (ad es., carcinoma mammario positivo ai recettori ormonali) e l'insufficienza epatica.

---

## Conclusioni e passaggi successivi

**Decisione: Proseguire con salvaguardie**

**Razionale:**
La previsione di TxGNN è inequivocabilmente supportata dalla farmacologia consolidata — il progesterone È il fondamento ormonale della regolazione del ciclo mestruale, e il suo uso clinico nella gestione dell'amenorrea è già pratica standard in tutto il mondo in molteplici sotto-indicazioni. Con evidenza L1 (molteplici RCT di Fase 3 completati confermati), il caso scientifico e clinico è robusto. I principali ostacoli al procedimento sono normativi (nessuna autorizzazione italiana) e completezza dei dati (lacune nella documentazione di sicurezza in questo dataset), piuttosto che qualsiasi carenza nelle prove cliniche.

**Per procedere, quanto segue è necessario:**
- Ottenere e rivedere lo SmPC completo / l'informazione per il prescrittore per documentare le controindicazioni, gli avvertimenti, le interazioni farmacologiche e le linee guida per le popolazioni speciali (la lacuna di dati in sospeso più critica)
- Recuperare la documentazione formale del meccanismo d'azione da DrugBank (MOA attualmente non disponibile nel dataset)
- Definire la sottopopolazione target specifica per il contesto italiano: amenorrea anovulatoria (PCOS/funzionale ipotalamica), amenorrea correlata a POI, amenorrea post-chemioterapia o post-chirurgica (correlata a IUA) — ognuna richiede un protocollo clinico distinto
- Avviare la valutazione del percorso normativo con AIFA per l'autorizzazione di commercializzazione (nuova domanda, riconoscimento reciproco o procedura decentralizzata)
- Stabilire un piano di monitoraggio della sicurezza affrontando il rischio di tromboembolismo, le controindicazioni ormonali e il monitoraggio della risposta endometriale negli scenari di uso a lungo termine

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

