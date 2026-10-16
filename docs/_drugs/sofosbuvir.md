---
layout: default
title: Sofosbuvir
parent: Solo previsione del modello (L5)
nav_order: 408
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Sofosbuvir: nuova indicazione prevista, Infezione da virus dell'epatite B (99,77%) (livello di evidenza L5). Indicazione originale: Infezione cronica da virus dell'epatite C"
monitor_inn: "sofosbuvir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "chronic hepatitis B virus infection", "Kyasanur forest disease", "HIV infectious disease"]
---

# Sofosbuvir
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

# Sofosbuvir: dall'epatite C cronica all'epatite E (infezione da virus dell'epatite E)

## Sintesi in una frase

Sofosbuvir è un analogo nucleotidico originariamente usato per l'infezione cronica da virus dell'epatite C (HCV).
Il modello TxGNN lo prevede potenzialmente utile per diverse infezioni virali; tra le indicazioni predette, quella con il supporto più coerente sul piano meccanicistico e clinico diretto è l'**infezione da virus dell'epatite E (HEV)**, con **2 studi clinici** associati (di cui 1 specifico, di fase 2 su 10 pazienti) e **19 pubblicazioni** nei dati compilati. L'indicazione di rango 1 (epatite B) è invece considerata un probabile artefatto di prossimità nella rete di conoscenza.

> Nota metodologica: la predizione con il punteggio più alto è l'epatite B (99,77%), ma l'analisi dei dati mostra che non esiste un meccanismo antivirale plausibile contro l'HBV. Questo report approfondisce quindi l'epatite E, e riassume le altre predizioni nella sezione dedicata.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezione cronica da virus dell'epatite C |
| Nuova indicazione predetta (rango 1 TxGNN) | Infezione da virus dell'epatite B (99,77%) |
| Nuova indicazione approfondita | Infezione da virus dell'epatite E (99,49%) |
| Livello di evidenza | L2 (epatite E); L2 per epatite B ma solo come questione di sicurezza |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 5 (tutte cancellate) |
| Decisione raccomandata | Hold (con domanda di ricerca aperta sull'epatite E) |

## Perché questa predizione è ragionevole?

Non sono attualmente disponibili dati dettagliati sul meccanismo d'azione nei dati compilati. In base alle informazioni note, sofosbuvir è un analogo nucleotidico che inibisce la RNA polimerasi RNA-dipendente NS5B dell'HCV, e la sua efficacia nell'epatite C è consolidata.

Il virus dell'epatite E è un virus a RNA a filamento positivo dotato di una propria RNA polimerasi RNA-dipendente (ORF1): il meccanismo da analogo nucleotidico è quindi biologicamente plausibile. Studi in vitro riportano inibizione della replicazione di HEV, con effetto additivo in combinazione con ribavirina; un'alta dose di sofosbuvir, da solo o con ribavirina, ha mostrato attività anche in un modello animale (coniglio).

I risultati clinici sono però contrastanti: nel piccolo studio pilota HepNet si è osservata una riduzione iniziale della carica virale ma non una risposta virologica sostenuta, con comparsa di varianti associate a resistenza. Case report descrivono risposte con ledipasvir/sofosbuvir più ribavirina in pazienti refrattari alla ribavirina, mentre una serie in riceventi di trapianto non ha ottenuto l'eliminazione virale.

Per l'epatite B (rango 1), invece, l'HBV è un virus a DNA che replica tramite trascrizione inversa: un meccanismo antivirale diretto di sofosbuvir non è plausibile. Le variazioni di HBV DNA e HBsAg osservate nei pazienti co-infetti sono spiegate soprattutto dalla clearance dell'HCV e dalla riattivazione dell'HBV. Il punteggio molto alto è probabilmente un artefatto di prossimità tra virus epatotropi.

## Evidenza da studi clinici

Studi relativi all'epatite E:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT03282474](https://clinicaltrials.gov/study/NCT03282474) | Fase 2 | Completato | 10 | Studio pilota HepNet a braccio singolo con sofosbuvir nell'epatite E cronica; segnale preliminare di attività, senza clearance sostenuta |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Fase 4 | Stato sconosciuto | 25 | Studio di fattibilità in co-infezione HIV-HCV con SOF/VEL; non specifico per HEV |

Studi più rilevanti per l'epatite B (rango 1), da leggere come questione di sicurezza e non di efficacia:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completato | 21 | Ledipasvir/sofosbuvir per 12 settimane in soggetti con infezione da HBV; a braccio singolo, piccolo, in combinazione |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completato | 23 | DAA in co-infezione HCV/HBV; valuta la riattivazione dell'HBV |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Stato sconosciuto | 120 | SOF/VEL con TAF profilattico per prevenire la riattivazione dell'HBV in co-infetti |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Fase 2 | Stato sconosciuto | 21 | Ledipasvir/sofosbuvir in linfoma a cellule B indolente associato a HCV |

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [35814503](https://pubmed.ncbi.nlm.nih.gov/35814503/) | 2022 | Revisione | J Clin Exp Hepatol | Revisione delle evidenze in vitro e in vivo di sofosbuvir nell'epatite E |
| [37334496](https://pubmed.ncbi.nlm.nih.gov/37334496/) | 2023 | Analisi dello studio di fase 2 | Hepatology | Nello studio pilota NCT03282474 la carica virale è calata inizialmente ma senza risposta sostenuta; emergenza di varianti associate a resistenza |
| [31404927](https://pubmed.ncbi.nlm.nih.gov/31404927/) | 2019 | Serie di casi | Open Forum Infect Dis | Sofosbuvir aggiunto alla ribavirina in 3 trapiantati d'organo: nessuna risposta virologica sostenuta |
| [36942308](https://pubmed.ncbi.nlm.nih.gov/36942308/) | 2023 | Caso clinico | IDCases | Risposta a ledipasvir/sofosbuvir più ribavirina in epatite E persistente refrattaria alla ribavirina |
| [29946850](https://pubmed.ncbi.nlm.nih.gov/29946850/) | 2018 | Caso clinico | Infection | Epatite E acuta autoctona trattata con sofosbuvir e ribavirina |
| [26408347](https://pubmed.ncbi.nlm.nih.gov/26408347/) | 2016 | Studio in vitro | Gastroenterology | Sofosbuvir inibisce la replicazione di HEV genotipo 3, con effetto additivo con la ribavirina |
| [35247472](https://pubmed.ncbi.nlm.nih.gov/35247472/) | 2022 | Modello animale | Antiviral Res | Sofosbuvir ad alta dose, da solo o con ribavirina, inibisce la replicazione di HEV nel coniglio |
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Fase 2 in aperto (HBV) | J Med Virol | Ledipasvir/sofosbuvir in monoinfezione da HBV; endpoint: riduzione di HBsAg e HBV DNA |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Coorte | J Clin Med | Cinetiche diverse di HBV-DNA e HBsAg in co-infetti HCV durante terapia con DAA, con rischio di riattivazione |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 044928024 | EPCLUSA 28 cpr rivestite 200 mg + 50 mg flacone | Compresse rivestite | Non disponibile nei dati compilati (autorizzazione cancellata) |
| 044928048 | EPCLUSA 28 bust grat 200 mg + 50 mg | Granulato in bustine | Non disponibile (cancellata) |
| 044928036 | EPCLUSA 28 bust grat 150 mg + 37,5 mg | Granulato in bustine | Non disponibile (cancellata) |
| 044928012 | EPCLUSA 28 cpr rivestite 400 mg + 100 mg flacone | Compresse rivestite | Non disponibile (cancellata) |
| 045494010 | VOSEVI 28 cpr rivestite 400 mg + 100 mg + 100 mg flacone | Compresse rivestite | Non disponibile (cancellata) |

Tutte e 5 le autorizzazioni, intestate a Gilead Sciences Ireland UC, risultano cancellate; non vi sono autorizzazioni valide.

## Considerazioni di sicurezza

- **Rischio di riattivazione dell'HBV**: la letteratura documenta riattivazioni del virus dell'epatite B in pazienti co-infetti durante terapia con antivirali ad azione diretta contro l'HCV, compresi regimi con sofosbuvir. Nei co-infetti è quindi necessario uno screening dell'HBV e un monitoraggio (valutando una profilassi, ad esempio con TAF).
- **Interazioni farmacologiche** (8 segnalate):
  - Maggiori: apalutamide, enzalutamide, lorlatinib.
  - Moderate: fostamatinib, warfarin, dicumarolo, encorafenib.
  - Minori: ciclosporina.
- **Insufficienza renale grave**: la letteratura segnala che sofosbuvir non è approvato in caso di eGFR <30 ml/min, per preoccupazioni emerse da test preclinici.

Per avvertenze e controindicazioni complete si rimanda al foglio illustrativo.

## Altre indicazioni predette (sintesi)

| Indicazione | Punteggio TxGNN | Livello di evidenza | Valutazione |
|---|---|---|---|
| Infezione da HBV | 99,77% | L2 | Nessun meccanismo plausibile; dati solo di co-infezione, utili come questione di sicurezza |
| Epatite virale, animale | 99,48% | L4 | Categoria troppo vaga; nessuno studio clinico. Hold |
| Epatite A | 99,48% | L4 | Un solo studio in vitro; gli studi associati sono tutti su HCV. Hold |
| Febbre emorragica di Omsk | 99,47% | L5 | Solo predizione, nessuna evidenza specifica. Hold |
| Epatite B cronica | 99,46% | L2 | Come per l'HBV: questione di sicurezza, non di efficacia |
| Malattia della foresta di Kyasanur | 99,45% | L5 | Un solo studio biochimico/in vitro. Hold |
| Infezione da HIV | 99,23% | L3 | Nessun meccanismo antiretrovirale; i dati riguardano il trattamento dell'HCV in co-infetti, cioè l'indicazione originale |

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- L'unica direzione con razionale meccanicistico e prime prove cliniche dirette è l'epatite E, ma lo studio pilota (n=10) non ha ottenuto una risposta virologica sostenuta e ha mostrato varianti di resistenza. Le altre predizioni, compresa quella al primo posto (HBV), non hanno sostegno meccanicistico o evidenza specifica. Inoltre tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) provenienti da DrugBank.
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza).
- Studi controllati e di maggiori dimensioni sull'epatite E (ad esempio sofosbuvir in combinazione con ribavirina in pazienti refrattari), con endpoint di risposta virologica sostenuta.
- Un piano di monitoraggio della riattivazione dell'HBV per le popolazioni co-infette.
- Chiarimento della posizione regolatoria in Italia, dato che le autorizzazioni attuali sono tutte cancellate.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

