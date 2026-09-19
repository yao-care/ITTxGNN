---
layout: default
title: Perampanel
parent: Prove elevate (L1-L2)
nav_order: 162
evidence_level: L2
indication_count: 10
---

# Perampanel
{: .fs-9 }

Livello di evidenza: **L2** | Indicazioni previste: **10** 
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

# Perampanel: dalle crisi di esordio focale all'epilessia visiva

## Sintesi a una frase

Perampanel è un farmaco anticonvulsivante di terza generazione, il primo della sua classe — un antagonista selettivo non competitivo del recettore AMPA — approvato globalmente per le crisi di esordio focale e le crisi tonico-cloniche generalizzate primarie.
Il modello TxGNN prevede che potrebbe essere efficace per l'**epilessia visiva** (epilessia fotosensibile/riflessa scatenata da stimoli visivi), con **3 studi clinici** e **20 pubblicazioni** che attualmente supportano questa direzione.

---

## Panoramica rapida

| Voce | Contenuto |
|------|---------|
| Indicazione originale | Crisi di esordio focale; crisi tonico-cloniche generalizzate primarie (approvazione globale consolidata; nessuna registrazione italiana registrata) |
| Nuova indicazione prevista | Epilessia visiva |
| Punteggio di predizione TxGNN | 99.92% |
| Livello di evidenza | L2 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Procedere con Cautele |

---

## Perché questa predizione è ragionevole?

I dati formali del meccanismo d'azione non sono stati recuperati dall'API di DrugBank (lacuna nei dati DG002). Tuttavia, la letteratura clinica stabilisce coerentemente che il perampanel è un antagonista selettivo e non competitivo del recettore ionotropico AMPA (acido α-ammino-3-idrossi-5-metil-4-isossazolpropionico) del glutammato. Occupando un sito allosterico non competitivo sul recettore AMPA, blocca la trasmissione eccitatoria postsinaptica rapida — il fattore chiave di avvio e propagazione delle crisi — senza competere direttamente con il glutammato. Questo meccanismo lo distingue dai bloccanti dei canali del sodio e dagli agenti potenziatori del GABA e rappresenta l'approccio anti-glutammatergico più mirato attualmente approvato per l'epilessia.

L'epilessia visiva (epilessia fotosensibile) è una sindrome epilettica riflessa in cui le crisi sono scatenate specificamente da stimolazione fotoica intermittente, pattern visivi geometrici o altri stimoli visivi. La firma fisiopatologica è l'ipereccitabilità mediata da recettori AMPA all'interno della corteccia occipitale (visiva): lo stimolo scatenante guida onde eccitatori anormalmente amplificate attraverso la corteccia visiva primaria che possono quindi propagarsi alle aree secondarie e associative, generando crisi cliniche. Poiché il perampanel agisce direttamente sui recettori AMPA in tutta la corteccia — e la corteccia occipitale è il locus del circuito scatenante — l'allineamento meccanicistico tra il bersaglio del farmaco e il punto di ingresso della malattia è eccezionalmente alto.

Sia l'indicazione originale approvata (crisi di esordio focale e generalizzate sostenute dall'eccitazione glutammatergica) che l'epilessia visiva condividono lo stesso squilibrio fondamentale eccitazione-inibizione mediato dai recettori AMPA. La differenza chiave risiede nella modalità del trigger, non nel meccanismo delle crisi a valle. Questa logica farmacologica è precisamente ciò che rende la predizione del modello TxGNN così convincente: il riposizionamento non richiede un nuovo meccanismo, solo una nuova applicazione di uno già ben caratterizzato.

---

## Evidenza degli studi clinici

| Numero dello studio | Fase | Stato | Arruolamento | Risultati chiave |
|-------------|-------|--------|------------|--------------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Fase 2 | Completato | 18 | Studio randomizzato in doppio cieco controllato con placebo della tollerabilità, sicurezza e farmacocinetica di E2007 (codice di sviluppo del perampanel) in pazienti con crisi parziali o generalizzate refrattarie in trattamento con almeno un farmaco anticonvulsivante concomitante; il disegno RDBPC soddisfa i criteri L2 nonostante la piccola dimensione del campione |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Fase 4 | Completato | 12 | Ha valutato gli effetti del perampanel sull'EEG, potenziali evocati somatosensoriali, potenziali evocati uditivi troncoencefalici e — crucialmente — **potenziali evocati visivi (VEP)**; fornisce evidenza elettrofisiologica diretta dell'impatto del perampanel sulla via visiva |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Fase 4 | Completato | 30 | Ha valutato effetti cognitivi ed EEG del perampanel (come nuovo antagonista dei recettori AMPA) in pazienti con epilessia in Corea; contribuisce alla caratterizzazione neurofisiologica generale a supporto della modulazione diffusa dell'attività corticale |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|------|------|---------|--------------|
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Meta-analisi | The Medical Journal of Malaysia | Meta-analisi completa che conferma l'efficacia e la sicurezza del perampanel come terapia adiuvante per crisi sia generalizzate che focali; supporta l'applicabilità ad ampio spettro incluse le epilessie riflesse |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Revisione sistematica / Meta-analisi in rete | Journal of Neurology | Meta-analisi in rete che confronta i farmaci anticonvulsivanti per le epilessie generalizzate idiopatiche come terapia monofarmaco e adiuvante; il perampanel si posiziona come un'opzione efficace con un profilo di evidenza favorevole |
| [37059702](https://pubmed.ncbi.nlm.nih.gov/37059702/) | 2023 | Revisione Cochrane sistematica | Cochrane Database of Systematic Reviews | Revisione Cochrane di perampanel come terapia aggiuntiva per l'epilessia focale farmaco-resistente; sintesi sistematica di qualità gold-standard che conferma una riduzione clinicamente significativa delle crisi |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Revisione sistematica + Meta-analisi | Seizure | Meta-analisi basata su RCT del perampanel tra le indicazioni approvate; conferma l'efficacia per le crisi di esordio focale e PGTC via meccanismo di antagonismo AMPA |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Revisione sistematica / Meta-analisi in rete | Drugs | Confronto testa-a-testa in rete dei farmaci anticonvulsivanti di terza generazione (brivaracetam, cenobamate, eslicarbazepina, lacosamide, perampanel) per le crisi di esordio focale; contestualizza la posizione del perampanel nell'armamentario terapeutico |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Linea guida di pratica clinica | Neurology | Aggiornamento della linea guida di pratica dell'AAN/AES sui nuovi farmaci anticonvulsivanti per l'epilessia di nuova insorgenza e refrattaria; il perampanel è incluso come agente di terza generazione revisionato |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Revisione narrativa + Dati del mondo reale | Epilepsy & Behavior | Revisione completa della monoterapia con perampanel in contesti di studi clinici e del mondo reale; conferma il dosaggio una volta al giorno, la copertura ampia delle crisi inclusi i tipi generalizzati, e la tollerabilità |
| [37292124](https://pubmed.ncbi.nlm.nih.gov/37292124/) | 2023 | Coorte prospettica | Frontiers in Neurology | Studio prospettico della monoterapia con perampanel come trattamento iniziale nell'epilessia focale pediatrica di nuova diagnosi; tassi di risposta significativi con tollerabilità accettabile in un contesto del mondo reale |
| [41043235](https://pubmed.ncbi.nlm.nih.gov/41043235/) | 2025 | Coorte multicentrica prospettica | Epilepsy & Behavior | Studio multicentrico italiano sull'uso precoce del perampanel; ha dimostrato miglioramento nella frequenza delle crisi, qualità del sonno, ritmo circadiano e qualità della vita — fornendo dati italiani del mondo reale contemporanei |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Revisione | Expert Opinion on Drug Discovery | Revisione fondazionale sulla scoperta del perampanel e l'antagonismo del recettore AMPA; documenta il meccanismo unico del farmaco come il primo anticonvulsivante approvato che agisce sull'eccitazione postsinaptica — supportando direttamente la logica dell'epilessia visiva |

---

## Considerazioni sulla sicurezza

Si prega di consultare il foglio illustrativo per le informazioni sulla sicurezza.

> **Nota:** I dati formali sulla sicurezza (avvertenze e controindicazioni dal foglio illustrativo AIFA/TFDA) non hanno potuto essere recuperati (lacuna nei dati DG001, gravità: Blocco). I dati sulle interazioni tra farmaci non sono stati trovati nella ricerca nel database. Queste lacune dovrebbero essere risolte prima della valutazione dell'uso clinico.

---

## Conclusione e prossimi passi

**Decisione: Procedere con Cautele**

**Razionale:**
L'epilessia visiva è l'indicazione meccanicisticamente più direttamente allineata per il perampanel in questo intero set di predizioni — il circuito scatenante della malattia (ipereccitabilità occipitale mediata da recettori AMPA) è precisamente il bersaglio molecolare dell'antagonismo non competitivo del farmaco, e uno studio completato in Fase 2 RDBPC (NCT03780907, n=18) eleva l'evidenza a L2 con 20 pubblicazioni a supporto. Tuttavia, l'Italia non ha un'autorizzazione normativa esistente per il perampanel, e rimangono irrisolte due lacune critiche nei dati sulla sicurezza.

**Per procedere, è necessario quanto segue:**

- **Risolvere la lacuna nei dati di Blocco (DG001):** Recuperare il PDF del foglio illustrativo AIFA/TFDA per estrarre le controindicazioni e gli avvertimenti in scatola nera — questo è obbligatorio prima che qualsiasi valutazione della sicurezza possa essere completata
- **Risolvere la lacuna nei dati Alta (DG002):** Interrogare l'API di DrugBank per i dati formali del meccanismo d'azione per completare la sezione di analisi meccanicistica
- **Studio dedicato nell'epilessia fotosensibile:** Lo studio NCT03780907 era uno studio generale su crisi refrattarie (n=18); un RCT di Fase 2 appositamente progettato in pazienti con epilessia fotosensibile elevererebbe l'evidenza a un livello più conclusivo
- **Valutazione delle interazioni tra farmaci con farmaci antiepilettici che inducono gli enzimi:** I farmaci antiepilettici inducenti enzimi (carbamazepina, fenitoina, ossicarbamazepina) sono noti per ridurre significativamente i livelli plasmatici del perampanel; una valutazione formale è essenziale per scenari di prescrizione concomitante
- **Mappatura del percorso normativo italiano:** Poiché il perampanel non è attualmente autorizzato in Italia, una strategia normativa completa — incluso se perseguire un'estensione di una nuova indicazione o un programma di uso compassionevole off-label — deve essere definita prima di qualsiasi distribuzione clinica

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

