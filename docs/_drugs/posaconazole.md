---
layout: default
title: Posaconazole
parent: Solo previsione del modello (L5)
nav_order: 356
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: nuova indicazione prevista, Pneumocistosi (pneumocystosis) (livello di evidenza L5). In Italia, confezioni AIFA: 11 (autorizzate: 11)"
---

# Posaconazole
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

## Posaconazole: Pneumocistosi (pneumocystosis)
{: .text-alpha }

## Sintesi in una frase

Il posaconazolo è un antifungino triazolico, originariamente utilizzato per infezioni fungine come aspergillosi, candidosi e altre micosi.
Il modello TxGNN ne prevede una possibile efficacia nella **pneumocistosi**, ma l'evidenza a supporto è molto limitata: **1 studio clinico** (che riguarda un altro farmaco) e **5 pubblicazioni** generali (linee guida, revisioni e una coorte), nessuna delle quali dimostra direttamente l'efficacia del posaconazolo in questa patologia.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Pneumocistosi (pneumocystosis) |
| Punteggio di predizione TxGNN | 0.9977 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 11 su 11) |
| Numero di autorizzazioni | 11 (valide: 11) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è ragionevole?

Secondo le sezioni «Mechanism of Action» e «Microbiology» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Posaconazole (traduzione non ufficiale): «Posaconazolo è un agente antimicotico azolico. […] Posaconazolo blocca la sintesi dell'ergosterolo, un componente chiave della membrana cellulare fungina, attraverso l'inibizione dell'enzima lanosterolo 14α-demetilasi dipendente dal citocromo P-450, responsabile della conversione del lanosterolo in ergosterolo nella membrana cellulare fungina. Ciò determina un accumulo di precursori sterolici metilati e una deplezione di ergosterolo all'interno della membrana cellulare, indebolendo così la struttura e la funzione della membrana cellulare fungina.» Testo originale in inglese: "Posaconazole is an azole antifungal agent. […] Posaconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84), versione del 2026-02-13; consultato il 2026-11-19). In generale, il posaconazolo è un azolico antifungino che inibisce la lanosterolo 14-alfa-demetilasi (CYP51), bloccando la sintesi dell'ergosterolo nella membrana fungina. La sua efficacia nelle micosi invasive come aspergillosi e candidosi è ben nota.

Tuttavia, il collegamento meccanicistico con la pneumocistosi è debole. *Pneumocystis jirovecii* non possiede ergosterolo nella membrana cellulare e utilizza colesterolo e altri steroli, per cui il bersaglio degli azoli non è chiaramente presente. Il punteggio TxGNN molto alto riflette con ogni probabilità la prossimità nella rete di conoscenza con altre indicazioni antifungine (aspergillosi, candidosi) più che un'effettiva corrispondenza meccanicistica. Questo collegamento non ha potuto essere verificato su dati curati dei bersagli farmacologici.

---

## Evidenza dagli studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fase 3 | Completato | 602 | Rezafungin (un'echinocandina, non posaconazolo) vs regime antimicrobico standard per prevenire le infezioni fungine invasive in adulti sottoposti a trapianto allogenico di sangue e midollo; nessuna evidenza diretta sul posaconazolo nella pneumocistosi |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revisione | Swiss Medical Weekly | Panoramica di candidosi, aspergillosi, criptococcosi e polmonite da Pneumocystis; cita la profilassi con posaconazolo attivo sulle muffe nei pazienti emato-oncologici |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisione | Clinical Pharmacokinetics | Penetrazione degli antinfettivi, inclusi gli antifungini, nel liquido di rivestimento epiteliale polmonare |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Coorte | Transplant Infectious Disease | Complicanze infettive nella malattia del trapianto contro l'ospite acuta dopo trapianto di fegato |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Linee guida | The Lancet Infectious Diseases | Raccomandazioni della British Society for Medical Mycology sulla diagnosi delle malattie fungine gravi (aggiornamento 2025) |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Linee guida | Zhonghua Jie He He Hu Xi Za Zhi | Linee guida cinesi 2025 per la diagnosi e il trattamento delle malattie fungine polmonari invasive |

---

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 048149025 | POSACONAZOLO\*24x1 cpr gastrores 100 mg | ACCORD HEALTHCARE SLU | Autorizzata |
| 037059021 | NOXAFIL\*24 cpr gastrores 100 mg | MERCK SHARP & DOHME BV | Autorizzata |
| 046570014 | POSACONAZOLO\*orale sosp 105 ml 40 mg/ml con cucchiaio dosatore | EG SpA | Autorizzata |
| 047254053 | POSACONAZOLO\*24 cpr gastrores 100 mg | EG SpA | Autorizzata |
| 037059019 | NOXAFIL\*orale sosp 105 ml 40 mg/ml | MERCK SHARP & DOHME BV | Autorizzata |
| 048411019 | POSACONAZOLO\*24 cpr gastrores 100 mg | FRESENIUS KABI ITALIA Srl | Autorizzata |
| 050634017 | POSACONAZOLO\*24 cpr gastrores 100 mg | ABDI FARMA GMBH | Autorizzata |
| 047335056 | POSACONAZOLO\*24 cpr gastrores 100 mg | MYLAN SpA | Autorizzata |
| 049469099 | POSACONAZOLO\*24 cpr gastrores 100 mg | ZENTIVA ITALIA Srl | Autorizzata |
| 047914092 | POSACONAZOLO\*24 cpr gastrores 100 mg | TEVA B.V. | Autorizzata |
| 047603016 | POSACONAZOLO\*orale sosp 105 ml 40 mg/ml | MYLAN SpA | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

---

## Considerazioni sulla sicurezza

**Interazioni farmacologiche**: sono state identificate 269 interazioni. Tra quelle principali di livello **maggiore**:
- Loperamide
- Triamcinolone
- Budesonide

Tra quelle di livello **moderato**: famotidina, ranitidina, rabeprazolo, omeprazolo, cimetidina, idrocortisone, desametasone, betametasone, aprepitant, claritromicina, saxagliptin, bisacodile, acido picosolfurico e polietilenglicole con elettroliti.

Per avvertenze e controindicazioni si rimanda al foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'evidenza è solo di livello L4: manca qualsiasi studio che valuti direttamente il posaconazolo nella pneumocistosi, e il meccanismo plausibile è contraddetto dal fatto che *Pneumocystis* non possiede ergosterolo.

<!-- review:begin it-lic-20261106-posaconazole-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «L'evidenza è solo di livello L4: manca qualsiasi studio che valuti direttamente il posaconazolo nella pneumocistosi, e il meccanismo plausibile è contraddetto dal fatto che *Pneumocystis* non possiede ergosterolo. Inoltre, tutte le autorizzazioni italiane risultano cancellate.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-posaconazole-1 -->

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione verificati da fonti curate (es. DrugBank)
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, necessarie per lo screening di sicurezza
- Studi preclinici o clinici che valutino direttamente il posaconazolo nella pneumocistosi
- Chiarimento dello stato regolatorio attuale del prodotto in Italia

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «Inoltre, tutte le autorizzazioni italiane risultano cancellate» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

