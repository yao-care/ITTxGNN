---
layout: default
title: Ceftazidime
parent: Solo previsione del modello (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ceftazidime: nuova indicazione prevista, Infezione delle vie urinarie (valutata) (livello di evidenza L5). Indicazione originale: Infezioni batteriche (streptococciche, polmonite batterica…"
monitor_inn: "Ceftazidime"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "urinary tract infection (disease)", "epiglottitis", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
---

# Ceftazidime
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

# Ceftazidima: dalle infezioni batteriche all'infezione delle vie urinarie

## Sintesi

La ceftazidima è una cefalosporina di terza generazione, utilizzata originariamente per infezioni batteriche come polmonite, meningite, peritonite e infezioni da stafilococchi e streptococchi.
Il modello TxGNN la indica come potenzialmente efficace per l'**infezione delle vie urinarie** (punteggio 99,41%). Le evidenze sono **4 studi clinici** e **20 pubblicazioni**, ma in gran parte riguardano l'associazione ceftazidima-avibactam e non la ceftazidima da sola.

Nota: la prima previsione in graduatoria (iperamilasemia) e le successive 2 e 3 non hanno alcun supporto clinico né meccanicistico. Questo report si concentra sulla previsione con il maggior supporto di evidenze (infezione delle vie urinarie, rank 4) e, in sintesi, sulle altre previsioni in cui sono presenti dati.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (streptococciche, polmonite batterica, meningite batterica, peritonite, infezioni da *S. aureus*, ecc.), secondo il grafo di conoscenza; il testo delle indicazioni approvate AIFA non è disponibile |
| Nuova indicazione prevista | Infezione delle vie urinarie (valutata); la prima della graduatoria TxGNN è l'iperamilasemia (99,51%, senza evidenze, L5, Hold) |
| Punteggio di previsione TxGNN | 99,41% (infezione delle vie urinarie) |
| Livello di evidenza | L2 (per le vie urinarie, con riserva: dati prevalentemente su combinazione) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 17 (tutte revocate, 0 valide) |
| Decisione raccomandata | Proceed with Guardrails (per le vie urinarie); Hold per le previsioni senza evidenze |

---

## Perché questa previsione è ragionevole?

I dati dettagliati sul meccanismo d'azione non sono al momento disponibili nei dati compilati per questo report. In base alle conoscenze generali, la ceftazidima è una cefalosporina di terza generazione che si lega alle proteine leganti la penicillina (PBP) e inibisce la sintesi della parete cellulare batterica, con attività contro i batteri Gram-negativi, *Pseudomonas aeruginosa* incluso.

Le infezioni delle vie urinarie complicate sono frequentemente sostenute da patogeni Gram-negativi sensibili a questa classe. La previsione è quindi biologicamente plausibile e molto vicina alle indicazioni antibatteriche originali: non si tratta di un vero riposizionamento in senso meccanicistico, ma di un'estensione all'interno della stessa classe terapeutica.

Un limite importante: la maggior parte dei dati clinici riguarda ceftazidima-avibactam (associazione con inibitore delle beta-lattamasi) e non la ceftazidima in monoterapia, il che limita l'attribuzione diretta dei risultati. Inoltre, tutte le autorizzazioni italiane risultano revocate, quindi la disponibilità del prodotto andrebbe verificata.

---

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Fase 2 | Completato | 129 | Studio randomizzato in doppio cieco su sicurezza ed efficacia di CXA-101 endovena vs ceftazidima in infezioni urinarie complicate, inclusa pielonefrite |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Fase 4 | Completato | 60 | Ceftazidima-avibactam vs miglior terapia disponibile in infezioni da Gram-negativi resistenti ai carbapenemi (polmonite, infezioni urinarie e intra-addominali complicate, batteriemia) in adulti cinesi; in aperto |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Fase 1 | Completato | 43 | Studio farmacocinetico e di interazione farmacologica di avibactam + ceftazidima in volontari sani; nessun dato di efficacia |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/D | In reclutamento | 5000 | Farmacocinetica, farmacodinamica e sicurezza di farmaci poco studiati in bambini e giovani adulti; non specifico per le infezioni urinarie |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Revisione sistematica / network meta-analisi | J Comp Eff Res | Efficacia delle opzioni terapeutiche per infezioni urinarie complicate e pielonefrite acuta |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Revisione | Int J Antimicrob Agents | Approccio pratico SIMIT-SPILF al trattamento delle infezioni da Gram-negativi multiresistenti |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Revisione | Int J Antimicrob Agents | Dati clinici sui nuovi antibiotici per Gram-negativi multiresistenti, inclusa ceftazidima-avibactam |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Coorte retrospettiva multicentrica | Clin Infect Dis | Ceftazidima-avibactam nelle infezioni da *K. pneumoniae* produttrice di KPC |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Coorte retrospettiva (classificata RCT nei dati) | Antimicrob Agents Chemother | Meropenem-vaborbactam vs ceftazidima-avibactam nelle infezioni da Enterobacteriaceae resistenti ai carbapenemi |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Revisione | Clin Infect Dis | Aggiustamento della dose antibiotica in insufficienza renale, incluso ceftazidima/avibactam |
| [26289307](https://pubmed.ncbi.nlm.nih.gov/26289307/) | 2015 | Revisione | Pharmacotherapy | Ceftazidima-avibactam contro batteri Gram-negativi multiresistenti |

---

## Altre previsioni con dati disponibili

**Otite media infettiva (99,19%, L3, Proceed with Guardrails).** Sono presenti studi pediatrici su otite media suppurativa cronica da *Pseudomonas*:
- [10826908](https://pubmed.ncbi.nlm.nih.gov/10826908/) (2000): studio randomizzato in aperto, ceftazidima vs aztreonam in 30 bambini; successo dell'84,6% nel gruppo ceftazidima.
- [10768520](https://pubmed.ncbi.nlm.nih.gov/10768520/) (2000): terapia parenterale ambulatoriale con ceftazidima in 52 bambini.
- [8451104](https://pubmed.ncbi.nlm.nih.gov/8451104/) (1993): ceftazidima in bambini con otite media suppurativa cronica senza colesteatoma.

Sono studi piccoli e datati; l'uso andrebbe riservato a forme pseudomonali o resistenti, guidato da coltura, nel rispetto dell'antimicrobial stewardship.

**Epiglottite (99,39%, L4, Research Question).** Solo due case report, nessuno con evidenza di efficacia della ceftazidima.

**Infezione da Peptostreptococcus (99,17%, L4, Research Question).** Solo uno studio in vitro del 1981 ([19802974](https://pubmed.ncbi.nlm.nih.gov/19802974/)) che mostra attività limitata sugli anaerobi.

**Uretrite gonococcica (99,27%, L5, Hold).** La classe è attiva in linea di principio, ma la ceftazidima non è un agente raccomandato e l'unico articolo recuperato non è pertinente.

**Uretrite da Ureaplasma (99,27%, L5, Hold).** Ureaplasma è privo di parete cellulare: i beta-lattamici sono attesi inefficaci. La previsione è contraddetta dalla biologia.

**Iperamilasemia, sindrome da iperviscosità policlonale, analbuminemia congenita, incompatibilità di gruppo sanguigno (L5, Hold).** Nessun legame meccanicistico né evidenza; probabili artefatti del grafo.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 036579035 | Ceftazidima, flacone IM 1 g + fiala solvente 3 ml (ALMUS) | Polvere e solvente per uso intramuscolare | Non disponibile (autorizzazione revocata) |
| 036568032 | Fribat, fiala IM 1 g + solvente 3 ml (EPIFARMA) | Polvere e solvente per uso intramuscolare | Non disponibile (revocata) |
| 025212022 | Glazidim, flaconcino IM 500 mg + solvente 1,5 ml (SANDOZ) | Polvere e solvente per uso intramuscolare | Non disponibile (revocata) |
| 025859024 | Starcef, flacone 500 mg + solvente 1,5 ml (F.I.R.M.A.) | Polvere e solvente per uso intramuscolare | Non disponibile (revocata) |
| 036604027 | Ceftazidima, flacone IM 1 g + solvente 3 ml (MYLAN) | Polvere e solvente per uso intramuscolare | Non disponibile (revocata) |

Le 17 autorizzazioni registrate sono tutte revocate; qui sono elencate le 5 principali.

---

## Considerazioni sulla sicurezza

- **Controindicazioni segnalate nel grafo di conoscenza** (non dal testo del foglio illustrativo): malattia renale, piureterite, malattia epatica, malattia della colecisti, disturbi della coagulazione, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, deficit congenito di protrombina.
- **Interazioni farmacologiche** (100 interazioni totali; principali di livello moderato):
  - Amfotericina B (incluse le formulazioni colesterilsolfato, complesso lipidico e liposomiale)
  - Aminoglicosidi: kanamicina, neomicina, streptomicina
  - Acido picosolfurico
  - Altre di livello non classificato: calcitriolo, pantoprazolo, doxiciclina, morfina, metformina, omeprazolo, sucralfato, lansoprazolo, vancomicina, atropina, lattulosio, triamcinolone.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails** (infezione delle vie urinarie e otite media pseudomonale); **Hold** per le previsioni prive di evidenze.

**Motivazione:**
- Per le vie urinarie la plausibilità biologica è alta e esistono studi clinici completati, ma riguardano per lo più ceftazidima-avibactam, quindi l'evidenza diretta per la ceftazidima da sola è limitata. Si tratta di un'estensione intra-classe più che di un vero riposizionamento. Lo stato di mercato (solo autorizzazioni revocate) richiede verifica.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (attualmente mancanti, bloccanti per lo screening di sicurezza)
- Verifica della disponibilità commerciale in Italia (prodotti attualmente non autorizzati)
- Studi comparativi sulla ceftazidima in monoterapia nelle infezioni urinarie complicate, distinti dai dati sulle associazioni
- Per l'otite media: conferma con evidenze più recenti e linee guida di stewardship antimicrobica
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

