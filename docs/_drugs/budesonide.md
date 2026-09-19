---
layout: default
title: Budesonide
parent: Prove moderate (L3-L4)
nav_order: 42
evidence_level: L4
indication_count: 10
---

# Budesonide
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **10** 
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

# Budesonide: dalle patologie infiammatorie all'eczema atopico

## Sommario in una frase

Il budesonide è un potente glucocorticoide sintetico utilizzato a livello mondiale per l'asma, la BPCO, la rinite allergica e le patologie infiammatorie intestinali; tuttavia, attualmente non è registrata alcuna indicazione approvata nel database italiano AIFA. Il modello TxGNN prevede che possa essere efficace per l'**eczema atopico**, in base al suo meccanismo di soppressione delle citochine Th2 che sono centrali in questa malattia della pelle. L'evidenza attuale consiste di **2 studi clinici recuperati** (nessuno dei quali valuta direttamente il budesonide per l'eczema) e **20 pubblicazioni** — con il supporto diretto più forte proveniente da uno studio di formulazione nanoparticellare preclinico del 2024 — collocando il livello di evidenza complessivo a **L4**.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|----------|
| Indicazione originaria | Nessuna indicazione approvata trovata nel database italiano AIFA |
| Indicazione predetta | Eczema atopico |
| Punteggio di predizione TxGNN | 99.96% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Hold |

---

## Perché questa predizione è ragionevole?

Il budesonide è un potente glucocorticoide sintetico che esercita i suoi effetti antinfiammatori legandosi ai recettori glucocorticoidi intracellulari (GR). Una volta legato, sopprime la trascrizione delle citochine Th2 chiave — incluse IL-4, IL-5 e IL-13 — inibendo contemporaneamente il reclutamento degli eosinofili e riducendo le cascate infiammatorie dipendenti da NF-κB. I dati dettagliati del MOA da DrugBank non erano disponibili per questa valutazione; il meccanismo descritto qui è basato sulla conoscenza farmacologica consolidata e sulla logica di riposizionamento fornita nel pacchetto di evidenze.

L'eczema atopico (ICD-10 L20) è principalmente guidato da una risposta infiammatoria dominante Th2, caratterizzata da segnalazione elevata IL-4/IL-13, funzione barriera cutanea compromessa e infiltrazione eosinofila tissutale. Il meccanismo del budesonide di sopprimere direttamente questi stessi percorsi citochino-mediati fornisce una logica meccanisticamente coerente per la sua potenziale utilità in questa indicazione. Infatti, i corticosteroidi topici in generale sono già un trattamento di prima linea per la dermatite atopica — la questione per questo candidato di riposizionamento risiede nel fatto se il budesonide specificamente, in particolare in formati di somministrazione innovativi, offra vantaggi significativi.

Una nota aggiuntiva di cautela: TxGNN ha classificato sia "eczema atopico" (rango #1, punteggio 99.96%) che "dermatite, atopica" (rango #3, punteggio 99.81%) come predizioni separate. Questi sono clinicamente la stessa entità (ICD-10 L20), suggerendo che il modello sta predicendo la stessa indicazione da due nodi del grafo di conoscenza diversi. L'evidenza umana più diretta in letteratura proviene da PMID 38275852 (2024), che ha sviluppato idrogel nanoparticellari di budesonide sensibili al pH esplicitamente progettati per la dermatite atopica pediatrica, confermando la logica farmacologica riconosciuta. Tuttavia, questo rimane uno studio di formulazione preclinico.

---

## Evidenza da studi clinici

Nessuno dei due studi recuperati valuta direttamente il budesonide come trattamento per l'eczema atopico. Entrambi sono Grado C — la malattia atopica appare come criterio di arruolamento di base o comorbilità, non come target di trattamento primario.

| Numero dello studio | Fase | Stato | Arruolamento | Principali risultati |
|-------------------|------|-------|-------------|-----------------|
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | NA | Sconosciuto | 150 | Caratterizza gli endotipi di asma grave pediatrico utilizzando analisi immunitarie, metabolomiche e microbiche; l'atopia (incluso l'eczema) è una variabile fenotipica di base, non un endpoint di trattamento — non applicabile come evidenza di budesonide per l'eczema |
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Fase 1/2 | Completato | 58 | Immunoterapia allergica (non budesonide) in bambini asmatici atopici ad alto rischio per l'asma; l'eczema è elencato come fattore di rischio di arruolamento — non applicabile come evidenza diretta di trattamento |

---

## Evidenza da letteratura

| PMID | Anno | Tipo | Rivista | Principali risultati |
|------|------|------|---------|-----------------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinico / Formulazione | Gels (Basel) | Nanoparticelle di Eudragit L100 caricate di budesonide formulate in idrogel sensibili al pH per la terapia locale della dermatite atopica pediatrica; sfrutta i cambiamenti di pH nelle lesioni atopiche per il rilascio mirato — l'evidenza diretta più forte disponibile, ma solo preclinico |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | RCT veterinaria | J Vet Pharmacol Ther | Studio randomizzato, in cieco, controllato con placebo, crossover (n=29 cani) di balsamo leave-on di budesonide 0,025% (Barazone) per la dermatite atopica canina; ha ridotto significativamente le lesioni cutanee e il prurito — unica evidenza di studio controllato, ma in un modello non umano |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Studio clinico | Pediatric Dermatology | Studio di knemometria in 14 bambini (5–12 anni) con dermatite atopica trattati con budesonide topico; ha rilevato un'attività glucocorticoide sistemica misurabile — conferma l'assorbimento dermico e la preoccupazione sulla sicurezza sistemica nei bambini |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Studio clinico | Dermatology (Basel) | Glucocorticosteroidi topici nei bambini con dermatite atopica valutati per gli effetti sull'asse IGF, ricambio di collagene osseo; assorbimento percutaneo confermato — baseline di sicurezza pertinente per l'uso topico pediatrico |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | Studio clinico prospettico | Allergologia et Immunopathologia | Risposta differenziale al budesonide in lattanti atopici vs. non-atopici con sibili ricorrenti; lo stato atopico ha modulato la risposta terapeutica — evidenza indiretta della sensibilità farmacologica nel fenotipo atopico |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Trasversale | Contact Dermatitis | Serie di patch-test di base italiana SIDAPA (2018–2019): la frequenza dell'allergia al budesonide è diminuita negli ultimi due decenni; conferma che il budesonide rimane il marcatore standard di ipersensibilità ai corticosteroidi in Italia |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Trasversale | Contact Dermatitis | Modelli di sensibilizzazione da contatto in pazienti di dermatologia asiatici con e senza dermatite atopica; positività al patch-test simile o superiore nei pazienti con DA — segnale di sicurezza pertinente per l'uso topico di budesonide |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Revisione | J Allergy Clin Immunol | Revisione delle terapie emergenti per l'EoE; i corticosteroidi topici ingeriti (incluso il budesonide) sono il trattamento off-label standard attuale — dimostra il ruolo antinfiammatorio mucosale consolidato con base meccanistica Th2 condivisa |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Revisione | Allergy | Ipersensibilità ai corticosteroidi nei pazienti asmatici; il budesonide identificato come causante allergia da contatto ritardata — segnale di sicurezza direttamente rilevante per l'applicazione topica nei pazienti atopici |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisione | Neuroimmunomodulation | Corticosteroidi intranasali e soppressione dell'asse HPA; discute la sicurezza sistemica nei pazienti con rinite allergica comorbida e dermatite atopica — supporta la necessità di monitoraggio sistemico nei contesti di politerapia |

---

## Informazioni sul mercato italiano

Il budesonide non è registrato nel database italiano AIFA. Nessun record di prodotto autorizzato è disponibile per questo mercato.

---

## Considerazioni di sicurezza

Si prega di consultare il foglio illustrativo per le informazioni di sicurezza.

> ⚠️ **Importante segnale di sicurezza identificato in letteratura**: Studi indipendenti multipli — inclusi PMID 30053491, 24603519, 35184304, 19183418, e 37550231 — riportano in modo coerente che il budesonide è un allergene da contatto riconosciuto nei pazienti con dermatite atopica, rientrante nel cluster di cross-reattività dei corticosteroidi del Gruppo B. Questo crea un paradosso terapeutico: l'agente antinfiammatorio previsto potrebbe agire lui stesso come aptene sensibilizzante nella popolazione di pazienti target. Questo risultato è specifico per le vie di somministrazione topica e deve essere affrontato come preoccupazione di sicurezza prioritaria prima che proceda qualsiasi indagine clinica nell'eczema atopico.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Logica:**
La base meccanistica per il budesonide nell'eczema atopico è farmacologicamente coerente (soppressione Th2 mediata da GR), ma l'evidenza attuale è limitata al lavoro di formulazione preclinico e ai segnali clinici indiretti. Criticamente, un rischio di sensibilizzazione da contatto ben documentato nella popolazione target esatta crea una preoccupazione di sicurezza che deve essere risolta prima di avanzare questo candidato.

**Per procedere, è necessario quanto segue:**

- **Risoluzione della lacuna di dati di sicurezza**: Ottenere il foglio illustrativo AIFA italiano (Data Gap DG001 — Bloccante) e i dati MOA di DrugBank (Data Gap DG002 — Alto) prima di qualsiasi ulteriore fase di valutazione
- **Valutazione del rischio di sensibilizzazione da contatto**: Condurre un protocollo formale di screening patch-test per l'ipersensibilità al budesonide nei pazienti con dermatite atopica prospettica; considerare la profilazione della cross-reattività dei corticosteroidi del Gruppo B
- **Evidenza di studi clinici umani**: Attualmente non esiste uno studio RCT o prospettico umano che valuti direttamente il budesonide per l'eczema atopico — uno studio di proof-of-concept di Fase 2 è richiesto per avanzare all'evidenza L2
- **Strategia di somministrazione innovativa**: Se si persegue questa indicazione, dare la priorità ai sistemi di somministrazione con nanoparticelle o incapsulati (come esplorato in PMID 38275852) per ridurre l'esposizione diretta al sensibilizzante e migliorare la concentrazione locale del farmaco
- **Deduplicazione del grafo di conoscenza**: "Eczema atopico" (rango #1) e "Dermatite, atopica" (rango #3) sono la stessa entità clinica (ICD-10 L20); queste due predizioni TxGNN dovrebbero essere unite nella pipeline per evitare il doppio conteggio dell'evidenza e delle raccomandazioni
- **Valutare il rango #2 (Bronchite) come candidato di priorità superiore**: L'indicazione di bronchite riporta evidenza L2 con una meta-analisi e revisione sistematica direttamente coinvolgente il budesonide, e una raccomandazione "Procedere con Guardrails" — questo potrebbe rappresentare un'opportunità di riposizionamento più immediata

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

