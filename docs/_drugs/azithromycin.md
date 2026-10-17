---
layout: default
title: Azithromycin
parent: Solo previsione del modello (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Azithromycin: nuova indicazione prevista, Sindrome da iperviscosità policlonale (livello di evidenza L5). Indicazione originale: Infezioni batteriche (streptococciche, stafilococciche, polmonite…"
monitor_inn: "Azithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

# Azitromicina: dalle infezioni batteriche alla sindrome da iperviscosità policlonale

## Sintesi

L'azitromicina è un antibiotico macrolide, originariamente usato per infezioni streptococciche e stafilococciche, polmonite batterica (anche da Mycoplasma pneumoniae), cervicite gonococcica acuta, congiuntivite, ulcera molle, leptospirosi, linfogranuloma venereo, framboesia e gengivite ulcerativa necrotizzante.
Il modello TxGNN predice come prima indicazione la **sindrome da iperviscosità policlonale**, ma **non esistono studi clinici né pubblicazioni** a supporto: si tratta di una previsione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (streptococciche, stafilococciche, polmonite, cervicite gonococcica, congiuntivite e altre) |
| Nuova indicazione predetta | Sindrome da iperviscosità policlonale |
| Punteggio di predizione TxGNN | 99,81% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, l'azitromicina è un macrolide con efficacia dimostrata nelle infezioni batteriche, ma per l'iperviscosità causata dall'aumento delle immunoglobuline policlonali non è stato stabilito alcun legame meccanicistico.

L'elevato punteggio (0,998) è un'indicazione computazionale e non è corroborato da alcuno studio. Gli effetti antinfiammatori e immunomodulatori dei macrolidi sono noti, ma non c'è alcun dato che li colleghi a questa condizione.

### Altre predizioni di rilievo (per contesto)

Il modello ha prodotto anche altre predizioni, con evidenza diversa:

| Malattia predetta | Punteggio | Livello | Note |
|------|------|------|------|
| Iperamilasemia | 99,81% | L5 | Reperto di laboratorio più che entità clinica; nessuna evidenza |
| Analbuminemia congenita | 99,79% | L5 | Nessun meccanismo plausibile |
| Cheratocongiuntivite epiteliale puntata | 99,78% | L4 | Solo un case report diagnostico (microsporidi), non dimostra efficacia |
| Incompatibilità di gruppo sanguigno | 99,70% | L5 | Nessuna evidenza |
| Malattia ematologica premaligna | 99,64% | L5 | Solo attività preclinica generica dei macrolidi |
| Gammopatia monoclonale | 99,61% | L4 | Studio preclinico (PMID 23546223): i macrolidi bloccano il flusso autofagico e sensibilizzano le cellule di mieloma al bortezomib; da considerare come domanda di ricerca |
| Malattia ematologica associata a neuropatia periferica acquisita | 99,56% | L5 | Nessuna evidenza |
| Peste setticemica | 99,52% | L4 | Studio in vitro su *Yersinia pestis* con scarsa attività dell'azitromicina; terapie di prima linea già consolidate |
| Disordine ematologico congenito (anemia falciforme) | 99,40% | L4 | Due studi di fase 1/2 ritirati con 0 pazienti; razionale antinfiammatorio plausibile per la sindrome toracica acuta; domanda di ricerca |

---

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati alla sindrome da iperviscosità policlonale.

---

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata alla sindrome da iperviscosità policlonale.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non vi sono autorizzazioni valide. Il testo delle indicazioni approvate non è disponibile. Principali autorizzazioni:

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Titolare | Stato |
|---------|------|------|------|-----------|
| 027860042 | ZITROMAX 3 cpr rivestite 500 mg | Compresse rivestite | Pfizer Italia Srl | Cancellata |
| 027860143 | ZITROMAX AVIUM 600, 8 cpr 600 mg | Compresse | Pfizer Italia Srl | Cancellata |
| 027897026 | Azitromicina sospensione orale 1.500 mg 200 mg/5 ml | Sospensione orale | Pfizer Italia Srl | Cancellata |
| 027948064 | TROZOCINA 3 cpr rivestite 500 mg | Compresse rivestite | Alfasigma SpA | Cancellata |
| 037555341 | Azitromicina 3 cpr rivestite 500 mg | Compresse rivestite | Teva Italia Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Condizioni associate a controindicazione o cautela (da relazioni farmaco-malattia nel grafo di conoscenza, non dal foglietto illustrativo)**: sindrome del QT lungo (anche familiare), torsione di punta, malattie epatiche, malattie della colecisti, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, miastenia gravis, malattie della giunzione neuromuscolare, disturbi dell'udito.
- **Interazioni**: le interrogazioni hanno evidenziato solo associazioni farmacologiche con il recettore della motilina (MLNR) e con TAS2R4; non sono state rilevate interazioni farmaco-farmaco classiche.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione principale non ha alcun supporto clinico, letterario o meccanicistico (L5). Le altre predizioni con qualche segnale (gammopatia monoclonale, anemia falciforme/sindrome toracica acuta) sono ancora a livello di domande di ricerca (L4), con studi clinici ritirati o solo dati preclinici. In Italia tutte le autorizzazioni risultano cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione dell'azitromicina e un'analisi del legame meccanicistico con l'iperviscosità policlonale
- Testo delle avvertenze e controindicazioni del foglietto illustrativo AIFA (dato attualmente mancante e bloccante per la valutazione di sicurezza)
- Verifica dello stato regolatorio attuale in Italia, dato che tutte le autorizzazioni elencate sono cancellate
- Valutazione di studi preclinici e clinici mirati per i segnali più promettenti (sindrome toracica acuta nell'anemia falciforme; sensibilizzazione al bortezomib nel mieloma/gammopatia monoclonale)
- Valutazione della compatibilità della via di somministrazione e della similarità con le indicazioni originali
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

