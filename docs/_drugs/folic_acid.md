---
layout: default
title: Folic Acid
parent: Solo previsione del modello (L5)
nav_order: 211
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "folic acid"
predicted_indications: ["biotin metabolic disease"]
description: "Folic Acid: nuova indicazione prevista, Malattia del metabolismo della biotina (biotin metabolic disease) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Folic Acid
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

## Folic Acid: Malattia del metabolismo della biotina (biotin metabolic disease)
{: .text-alpha }

## Sintesi

L'acido folico (vitamina B9) è utilizzato per correggere le carenze vitaminiche e le anemie carenziali, in particolare l'anemia da carenza di folati. Il modello TxGNN ne predice una possibile efficacia per la **malattia del metabolismo della biotina**, ma la previsione si basa solo sul modello: **nessuno studio clinico** è registrato e la letteratura raccolta (20 pubblicazioni, per lo più revisioni generiche sulle vitamine) non dimostra un beneficio specifico.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Malattia del metabolismo della biotina (biotin metabolic disease) |
| Punteggio di previsione TxGNN | 0.9949 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | almeno 20 |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione dell'acido folico. In base alle conoscenze note, l'acido folico è una vitamina del gruppo B che agisce come cofattore nel metabolismo a un carbonio, con efficacia comprovata nelle carenze di folati.

La biotina (vitamina B7) è anch'essa una vitamina idrosolubile del gruppo B, coinvolta nelle reazioni di carbossilazione. La vicinanza funzionale nel metabolismo intermedio spiega probabilmente il punteggio elevato assegnato dal modello.

Tuttavia il legame è un'inferenza a livello di rete, non un meccanismo dimostrato. L'acido folico non sostituisce la biotina, non agisce sulla biotinidasi né sulla olocarbossilasi sintetasi e non ha un ruolo stabilito nel correggere i difetti enzimatici alla base di queste patologie (ad esempio deficit di biotinidasi o di olocarbossilasi sintetasi). Il trattamento standard resta la supplementazione farmacologica con biotina.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Le pubblicazioni raccolte sono quasi tutte revisioni narrative o studi indiretti sulle vitamine in generale. Nessuna dimostra l'efficacia dell'acido folico nei disturbi del metabolismo della biotina. Di seguito le più pertinenti.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Revisione | Handb Clin Neurol | Disturbi responsivi alle vitamine (cobalamina, folato, biotina, B1, E); errori congeniti del trasporto e metabolismo di cobalamina e folato |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Revisione | Acta Vitaminol Enzymol | Vitamine nelle malattie metaboliche: malassorbimento, errori del metabolismo vitaminico, sindromi vitamino-dipendenti |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Revisione | Int J Mol Sci | Carenza di vitamina B12 e sistema nervoso; cenni al ruolo di biotina e folato come cofattori |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Revisione | Arch Biochem Biophys | Ruolo degli integratori di micronutrienti (B12, folato, B6 e altri) nel danno al DNA e nel metabolismo |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Revisione | Clin Dermatol | Vitamine del gruppo B in dermatologia e nella sintesi eritrocitaria |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Revisione | Cureus | Vitamine e diabete di tipo 2; livelli ridotti di tiamina, piridossina e biotina |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Revisione | Endocr Metab Immune Disord Drug Targets | Relazione tra vitamine e diabete di tipo 2 |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Studio sperimentale su ratto | Biologica Latina | Carenza di vitamina H (biotina) e carenza combinata con acido folico indotte nel ratto |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non esistono autorizzazioni valide. Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati compilati. Le principali autorizzazioni:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 045545023 | ACIDO FOLICO*28 cpr 5 mg | EG SpA | Valida |
| 045532049 | NOVACID*120 cpr 5 mg | S.F. GROUP Srl | Valida |
| 045534043 | FOLATEX*120 cpr 5 mg | S.F. GROUP Srl | Valida |
| 045545050 | ACIDO FOLICO*28 cpr 400 mcg | EG SpA | Valida |
| 036345027 | FOLIDEX*120 cpr 400 mcg | ITALFARMACO SpA | Valida |

## Considerazioni di sicurezza

- **Controindicazioni derivate dalla knowledge graph** (non dal foglietto illustrativo): la knowledge graph associa all'acido folico numerose condizioni, tra cui malattia renale, diabete mellito, chetoacidosi diabetica, ulcera peptica, sarcoidosi, ipercalcemia, iperparatiroidismo, nefrolitiasi, emocromatosi ereditaria, emosiderosi, malattia di Wilson, anemia falciforme, anemia emolitica, malattia infiammatoria intestinale, colite ulcerosa, disturbo bipolare e iperossaluria primaria. Queste associazioni vanno verificate sul foglietto illustrativo prima di qualsiasi conclusione.
- **Interazioni farmacologiche**: sono state identificate 430 interazioni potenziali. Tra quelle con livello classificato: pancrelipasi (moderata) e sulfasalazina (minore). Molte altre hanno livello non specificato, ad esempio calcitriolo, pantoprazolo, omeprazolo, lansoprazolo, metformina, glimepiride, mesalazina, acarbosio, morfina, vancomicina, prednisone e simvastatina.

Per avvertenze e controindicazioni ufficiali consultare il foglietto illustrativo AIFA, non ancora acquisito.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda solo sul modello (L5): nessuno studio clinico, letteratura non specifica e nessun meccanismo plausibile, dato che il trattamento standard è la biotina. Inoltre in Italia non esistono autorizzazioni valide.

**Per procedere sono necessari:**
- Acquisizione e analisi del foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente un limite bloccante per la valutazione di sicurezza
- Dati sul meccanismo d'azione (ad esempio da DrugBank)
- Evidenze precliniche o cliniche che colleghino direttamente l'acido folico ai difetti del metabolismo della biotina
- Verifica del contesto regolatorio, poiché tutte le autorizzazioni risultano cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

