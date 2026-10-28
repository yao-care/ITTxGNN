---
layout: default
title: Miconazole
parent: Prove moderate (L3-L4)
nav_order: 300
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-15
monitor_inn: "miconazole"
predicted_indications: ["acne (disease)"]
description: "Miconazole: nuova indicazione prevista, Acne (acne (disease)) (livello di evidenza L4). Indicazione originale: Non riportata nei dati locali"
---

# Miconazole
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **1** 
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

## Miconazole: Acne (acne (disease))
{: .text-alpha }

## Sintesi in una frase

Il miconazolo è un antifungino imidazolico, originariamente utilizzato per micosi cutanee e mucose (tinea, candidosi cutanea e vulvovaginale, pitiriasi versicolor).
Il modello TxGNN prevede che possa essere efficace per l'**acne**, con un punteggio molto alto ma con **nessuno studio clinico registrato** e **4 pubblicazioni** di supporto, di cui nessuna è una sperimentazione clinica robusta sull'acne.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Acne (acne (disease)) |
| Punteggio di predizione TxGNN | 0.9954 |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa predizione è plausibile?

I dati compilati per questo report non riportano il meccanismo d'azione. In base alla farmacologia generale degli azoli, il miconazolo inibisce l'enzima fungino CYP51 (lanosterolo 14-alfa-demetilasi), bloccando la sintesi dell'ergosterolo e quindi la crescita del fungo.

Il collegamento con l'acne è plausibile attraverso due vie:
1. **Attività antibatterica**: dati *in vitro* mostrano che gli azoli sono attivi contro *Propionibacterium (Cutibacterium) acnes*, batterio coinvolto nell'acne (PMID 20045949).
2. **Attività anti-Malassezia**: la follicolite da *Malassezia* (Pityrosporum) mima clinicamente l'acne ed è spesso scambiata per acne volgare (PMID 8593718). In questo caso l'effetto sarebbe su una condizione diversa, non sull'acne in sé.

Il miconazolo è inoltre descritto con effetti antinfiammatori e antibatterici sulla cute (PMID 18627330), che potrebbero contribuire all'azione sulle lesioni infiammatorie. Il punteggio TxGNN elevato è una predizione computazionale e non costituisce evidenza clinica.

## Evidenza dagli studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisione | Expert Opin Pharmacother | Rassegna sui molteplici effetti del miconazolo nelle patologie cutanee; antifungino imidazolico consolidato |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Studio clinico (split-face, piccolo) | Skin Res Technol | Valutazione clinica e bioinstrumentale dell'acne infiammatoria lieve catameniale; disegno esatto non confermato |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Studio *in vitro* | Biol Pharm Bull | Attività *in vitro* degli azoli antifungini contro *P. acnes* isolato da pazienti con acne volgare |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Studio clinico | Clin Exp Dermatol | Diagnosi e prove terapeutiche nella follicolite da *Malassezia* (condizione diversa dall'acne volgare) |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 025999121 | NIZACOL*10 cpr 500 mg (NEW RESEARCH Srl) | Non disponibile | Non disponibile (autorizzazione valida) |
| 038371011 | LORAMYC*14 cpr buccali 50 mg flacone (IST.GENTILI Srl) | Non disponibile | Non disponibile (autorizzazione valida) |

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo)**: malattia epatica, malattia della colecisti.
- **Interazioni farmacologiche**: sono state identificate 376 interazioni. Esempi tra quelle di livello moderato: paclitaxel, fentanil, alfentanil, acalabrutinib, nifedipina, amlodipina, amiodarone, amitriptilina, alprazolam, etinilestradiolo, estradiolo, alfuzosina, aliskiren, alosetron, idrocodone. Esempi di livello minore: dolutegravir, loratadina, amfotericina B, ambrisentan.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'evidenza è limitata a predizione del modello, dati *in vitro* e piccoli studi indiretti (livello L4). Non ci sono studi clinici registrati sull'acne, tutte le autorizzazioni italiane sono cancellate e mancano i dati di sicurezza ufficiali, che costituiscono una lacuna bloccante.

**Per procedere è necessario:**
- Recuperare e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni).
- Ottenere i dati sul meccanismo d'azione (es. da DrugBank).
- Valutare la compatibilità della via di somministrazione (probabile uso topico per l'acne) e la somiglianza con l'indicazione originale.
- Condurre studi clinici controllati sull'acne volgare, distinguendola dalla follicolite da *Malassezia*.
- Valutare il profilo di interazioni e l'impatto della malattia epatica in caso di uso sistemico.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

