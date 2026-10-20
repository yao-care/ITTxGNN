---
layout: default
title: Ribavirin
parent: Solo previsione del modello (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ribavirin: nuova indicazione prevista, Infezione cronica da virus dell'epatite B (livello di evidenza L5). Indicazione originale: Infezione cronica da HCV"
monitor_inn: "Ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related mesenteritis", "IgG4-related mediastinitis"]
---

# Ribavirin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Ribavirina: dall'epatite C cronica all'epatite B cronica

## Sintesi in una frase

La ribavirina è un antivirale analogo nucleosidico, originariamente usato per l'infezione cronica da virus dell'epatite C (HCV) e per le infezioni da virus respiratorio sinciziale (RSV).
Il modello TxGNN prevede che possa essere utile per l'**epatite B cronica**, con **15 studi clinici** e **20 pubblicazioni** identificati. Le prove dirette sono però limitate: un solo studio di fase 3 mirato all'HBV (NCT00114361), in cui la ribavirina è associata a peginterferone.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezione cronica da HCV; infezione da HCV; malattia infettiva da RSV (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Infezione cronica da virus dell'epatite B |
| Punteggio di predizione TxGNN | 99,86% |
| Livello di evidenza | L1 (secondo la classificazione automatica; vedi nota sotto) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 1 (cancellata) |
| Decisione raccomandata | Hold |

**Nota sul livello di evidenza:** la classificazione L1 richiede almeno due studi di fase 3 completati. Qui solo NCT00114361 è di fase 3, completato e direttamente pertinente all'HBV. Gli altri studi di fase 3 riguardano l'HCV o sono di stato sconosciuto. Un livello più prudente sarebbe quindi L2.

## Perché questa predizione è plausibile?

Il meccanismo d'azione dettagliato non è presente nei dati compilati per questo report. La ribavirina è un analogo della guanosina ad ampio spettro antivirale: inibisce le inosina monofosfato deidrogenasi (IMPDH1 e IMPDH2), riduce il pool intracellulare di GTP e ha effetti immunomodulatori. Le due IMPDH sono i bersagli farmacologici riportati nei dati.

HCV e HBV sono entrambi virus epatotropi che causano epatite cronica, cirrosi e carcinoma epatocellulare. Spesso i pazienti vengono trattati con regimi a base di interferone, e questo spiega la prossimità nel grafo di conoscenza. Tuttavia l'attività anti-HBV diretta della ribavirina è debole: un eventuale beneficio sarebbe come terapia aggiuntiva al peginterferone, non come farmaco singolo. Molti studi recuperati riguardano la coinfezione HCV/HBV, dove la ribavirina agisce sulla componente HCV.

Non ci sono prove di un beneficio solido rispetto alla terapia standard per l'HBV (analoghi nucleos(t)idici, peginterferone).

## Evidenze dagli studi clinici

Sono riportati gli studi più pertinenti all'HBV, seguiti da alcuni studi HCV a pertinenza indiretta.

| Studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Fase 3 | Completato | 138 | Peginterferone alfa-2a + ribavirina vs peginterferone da solo in HBV cronica HBeAg-negativa; l'associazione non isola il contributo della ribavirina |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Fase 2/3 | Completato | 120 | Studio pilota interferone alfa-2b + ribavirina in epatite B cronica |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Fase 3 | Sconosciuto | 24 | Ribavirina come immunomodulatore in aggiunta agli analoghi nucleotidici anti-HBV (pilota) |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Fase 3 | Sconosciuto | 320 | Peginterferone alfa-2a + ribavirina in coinfezione HCV/HBV ed epatite C |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Fase 4 | Sconosciuto | 20 | Peginterferone alfa-2b + ribavirina in coinfezione HBV/HDV (delta) |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Fase 2 | Terminato | 210 | INX-08189 con peginterferone e ribavirina in HCV genotipo 2 e 3; pertinenza HBV incerta |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Fase 4 | Completato | 129 | Risposta virologica sostenuta e profilo IL-28B in HCV genotipo 1; indiretto per HBV |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Fase 3 | Completato | 36 | Regime DAA con ribavirina in HCV con cirrosi scompensata; ribavirina agisce su HCV |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Fase 4 | Completato | 506 | Programma di sorveglianza e controllo dell'epatopatia da HCV; non testa la ribavirina nell'HBV |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Fase 3 | Completato | 72 | Sofosbuvir + daclatasvir + ribavirina in HCV genotipo 4 (Egitto); HCV |

Gli altri studi recuperati riguardano esclusivamente l'HCV.

## Evidenze dalla letteratura

Non sono presenti studi randomizzati: si tratta quasi esclusivamente di revisioni.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Revisione | Viruses | Coinfezione HCV/HBV: la terapia peginterferone + ribavirina è stata raccomandata per i coinfetti con HCV RNA positivo |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Revisione | World J Gastroenterol | Aggiornamento su trattamento ed esiti della doppia infezione cronica HCV/HBV |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Revisione | Hepatology | Aspetti immunologici della terapia antivirale di HBV e HCV |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Revisione | Curr Opin Virol | Effetto del genotipo IL28B sulla risposta in HBV e HCV |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Revisione | World J Gastroenterol | Polimorfismo IL28B e infezione da HBV |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Revisione | Nihon Rinsho | Infezione HCV-HBV; efficacia di peginterferone alfa-2b + ribavirina contro HCV |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Revisione | Expert Rev Anti Infect Ther | Opzioni terapeutiche per epatite B e C cronica nei bambini |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Revisione | World J Gastroenterol | Prevenzione del carcinoma epatocellulare nelle epatiti virali B e C |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 041806035 | RIBAVIRINA 140 cps 200 mg (Aurobindo Pharma Italia Srl) | Capsule | Non disponibile |

L'unica autorizzazione è cancellata: attualmente non risulta alcun prodotto a base di ribavirina in commercio in Italia secondo i dati compilati. Questo incide sulla fattibilità.

## Citotossicità

La ribavirina è un antimetabolita nucleosidico antivirale, non un antineoplastico: la sezione non si applica.

## Considerazioni sulla sicurezza

I dati di sicurezza derivati dal foglietto illustrativo AIFA non sono disponibili. Dal grafo di conoscenza TxGNN (non dal testo dell'etichetta) risultano associazioni di controindicazione con:

- **Malattie ematologiche:** anemia (inclusa emolitica e macrocitica), anemia falciforme, emoglobinopatie, pancitopenia, anemia aplastica ereditaria
- **Malattie cardiovascolari:** infarto miocardico, coronaropatia, aterosclerosi, ischemia miocardica
- **Malattie epatiche e pancreatiche:** cirrosi epatica, epatite autoimmune, pancreatite
- **Malattie respiratorie:** BPCO, asma, malattia polmonare interstiziale, sarcoidosi
- **Altre:** insufficienza renale, parodontite

**Interazioni:** i dati indicano come bersagli farmacologici le inosina monofosfato deidrogenasi 1 e 2 (IMPDH1, IMPDH2); non sono elencate interazioni con altri farmaci.

Per le informazioni complete sulla sicurezza, consultare il foglietto illustrativo.

## Altre indicazioni previste

Le altre nove predizioni (rank 2-10) hanno evidenza molto debole e raccomandazione Hold:

- **Sindrome epatopolmonare:** un solo caso clinico, che descrive un evento avverso da interferone; nessun legame meccanicistico.
- **Porfiria epatica:** solo revisioni e casi in cui la porfiria cutanea tarda compare durante la terapia con peginterferone/ribavirina, quindi un'associazione avversa e non terapeutica.
- **Trombosi portale primitiva, sclerosi epatoportale, ipertensione portale non cirrotica familiare a esordio precoce, cirrosi idiopatica associata al rame, patologie correlate a IgG4 (pachimeningite, mesenterite, mediastinite):** nessuno studio né pubblicazione, solo predizione del modello.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'unico studio di fase 3 mirato all'HBV usa la ribavirina in associazione a peginterferone, senza isolarne il contributo. L'attività anti-HBV diretta è debole e non vi sono prove di superiorità rispetto agli standard attuali. Inoltre non esiste alcun prodotto autorizzato in commercio in Italia e mancano i dati di sicurezza AIFA.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per la valutazione di sicurezza
- Acquisire dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Analizzare i risultati di NCT00114361 e NCT03759782 per capire il contributo specifico della ribavirina nell'HBV
- Confrontare con gli analoghi nucleos(t)idici e il peginterferone da soli
- Valutare la fattibilità regolatoria e commerciale, dato che l'autorizzazione italiana è cancellata
- Definire un piano di monitoraggio della sicurezza (in particolare anemia emolitica e rischio cardiovascolare) e considerare la teratogenicità
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

