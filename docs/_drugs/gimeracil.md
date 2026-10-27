---
layout: default
title: Gimeracil
parent: Prove elevate (L1-L2)
nav_order: 220
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Gimeracil: nuova indicazione prevista, Neoplasia del colon (livello di evidenza L1). Indicazione originale: Carcinoma gastrico (dal grafo di conoscenza"
monitor_inn: "gimeracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "lipoma of colon", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "colonic lymphangioma", "colon leiomyoma"]
---

# Gimeracil
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **10** 
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

## Gimeracil: dal carcinoma gastrico alla neoplasia del colon
{: .text-alpha }

## Sintesi in una frase

Il gimeracil è un componente dell'associazione S-1 (tegafur/gimeracil/oteracil), nata per il trattamento del carcinoma gastrico. Il modello TxGNN prevede che possa essere efficace per la **neoplasia del colon**, con **6 studi clinici** e **12 pubblicazioni** nei dati compilati per questo report. Le prove riguardano però l'associazione S-1 e non il gimeracil da solo, e le pubblicazioni sono quasi tutte case report.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Carcinoma gastrico (dal grafo di conoscenza; il testo delle indicazioni nelle autorizzazioni AIFA non è disponibile) |
| Nuova indicazione prevista | Neoplasia del colon |
| Punteggio di predizione TxGNN | 99,88% |
| Livello di evidenza | L1 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (0 valide, 2 cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

## Perché questa predizione è ragionevole?

Il gimeracil inibisce l'enzima diidropirimidina deidrogenasi (DPD), che degrada il 5-fluorouracile (5-FU). Nell'S-1 il tegafur è il profarmaco del 5-FU: inibendo la DPD, il gimeracil rallenta il catabolismo del 5-FU e ne mantiene più a lungo l'esposizione sistemica. I dati sul meccanismo d'azione originale non sono disponibili nei dati compilati; la descrizione precedente deriva dal razionale di riposizionamento.

Carcinoma gastrico e tumore del colon sono entrambi tumori gastrointestinali, e le fluoropirimidine sono una componente standard della terapia del carcinoma colorettale. Il meccanismo è quindi plausibilmente applicabile anche al colon.

Un limite importante: le prove cliniche riguardano il prodotto di associazione S-1, non il gimeracil singolo, quindi il contributo specifico del gimeracil non è separabile da quello degli altri componenti.

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Completato | 1535 | UFT+leucovorin vs TS-1 (S-1) come terapia adiuvante nel carcinoma del colon in stadio III; lo studio più solido del set |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Sconosciuto | 1191 | SOX (oxaliplatino + S-1) vs XELOX come adiuvante nel carcinoma colorettale in stadio III; nessun risultato disponibile |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Sconosciuto | 40 | S-1 + bevacizumab nel carcinoma colorettale non resecabile o ricorrente dopo fallimento di precedenti chemioterapie |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Sconosciuto | 82 | Raltitrexed + S-1 nel carcinoma colorettale metastatico dopo chemioterapia standard; endpoint primario: PFS mediana |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Non ancora in reclutamento | 52 | Fruquintinib + tegafur/gimeracil/oteracil in terza linea nel carcinoma colorettale metastatico, braccio singolo |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Terminato | 20 | Studio di sicurezza cardiaca (flusso coronarico) con S-1 o capecitabina + oxaliplatino; non è uno studio di efficacia |

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinico (xenotrapianto) | Oncology Reports | Irinotecano + S-1 orale ha potenziato l'attività antitumorale in xenotrapianti di cancro del colon, anche resistenti al 5-FU |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Studio farmacocinetico | Gan to Kagaku Ryoho | Utilità di S-1 nelle metastasi peritoneali da cancro del colon in un modello murino |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Studio retrospettivo | Gan to Kagaku Ryoho | Fattori di rischio di tossicità ematologica grave (16,1% di grado 3-4) in 87 pazienti trattati con S-1 + irinotecano |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report | J Oncol Pharm Pract | Ipertrigliceridemia indotta da S-1 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case report | Eur J Dermatol | Eritroderma con coinvolgimento mucoso e sindrome mano-piede da TS-1 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Research | Risposta completa con S-1 + irinotecano in metastasi epatiche da cancro del colon |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan to Kagaku Ryoho | Epatectomia in due tempi dopo SOX + panitumumab come downstaging nelle metastasi epatiche colorettali |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Case report | Gan to Kagaku Ryoho | Ritenzione urinaria da neuropatia acuta da oxaliplatino dopo trattamento con tegafur/gimeracil/oteracil |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 042291017 | TEYSUNO 42 cps 15 mg + 4,35 mg + 11,8 mg (Nordic Group BV) | Non indicata | Non indicata (autorizzazione cancellata) |
| 042291031 | TEYSUNO 42 cps 20 mg + 5,8 mg + 15,8 mg (Nordic Group BV) | Non indicata | Non indicata (autorizzazione cancellata) |

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Citotossico convenzionale (associazione a base di fluoropirimidina) |
| Rischio di mielosoppressione | Da consultare il foglio illustrativo; in letteratura si segnala tossicità ematologica grave di grado 3-4 nel 16,1% dei pazienti trattati con S-1 + irinotecano |
| Classificazione emetogenica | Consultare le avvertenze e precauzioni del foglio illustrativo |
| Parametri da monitorare | Emocromo con formula, funzione epatica e renale, elettroliti |
| Protezione nella manipolazione | Seguire le norme per la manipolazione dei farmaci citotossici |

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Dalla letteratura emergono reazioni avverse segnalate con S-1: sindrome mano-piede, eritroderma, ipertrigliceridemia e tossicità ematologica.

## Conclusioni e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esistono due studi di fase 3 sul carcinoma del colon/colorettale con S-1 (uno completato, con 1535 pazienti, e uno con stato sconosciuto e senza risultati), e questo giustifica il livello L1. Tuttavia l'evidenza riguarda l'associazione S-1 e non il gimeracil da solo, gli studi con stato sconosciuto non hanno risultati, la letteratura è prevalentemente costituita da case report e le autorizzazioni italiane sono tutte cancellate.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per lo screening di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Verifica dei risultati pubblicati dello studio NCT00660894 e aggiornamento dello stato di NCT03448549
- Valutazione del contributo specifico del gimeracil rispetto agli altri componenti dell'S-1
- Chiarimento della situazione regolatoria in Italia, dato che tutte le autorizzazioni risultano cancellate
- Piano di monitoraggio della sicurezza (tossicità ematologica, cutanea e cardiaca) e valutazione della DPD
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

