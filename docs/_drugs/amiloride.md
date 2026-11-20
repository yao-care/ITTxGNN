---
layout: default
title: Amiloride
parent: Solo previsione del modello (L5)
nav_order: 38
evidence_level: L5
indication_count: 5
monitor_inn: "amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-20
description: "Amiloride: nuova indicazione prevista, Nefropatia ipertensiva maligna (malignant hypertensive renal disease) (livello di evidenza L5). In Italia, confezioni AIFA: 1 (autorizzate: 1)"
---

# Amiloride
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

## Amiloride: diuretico risparmiatore di potassio (blocco di ENaC) → Nefropatia ipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Sintesi in una frase

Amiloride è un diuretico risparmiatore di potassio. Il modello TxGNN prevede un possibile beneficio per la **nefropatia ipertensiva maligna (malignant hypertensive renal disease)**, ma nei dati compilati per questo report non risultano **né sperimentazioni cliniche né pubblicazioni** che studino direttamente questa malattia. La previsione si basa quindi solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Nefropatia ipertensiva maligna (malignant hypertensive renal disease) |
| Punteggio di previsione TxGNN | 0,9982 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa previsione è plausibile?

Secondo la sezione «Clinical Pharmacology» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Amiloride (traduzione non ufficiale): «Amiloride HCl è un farmaco risparmiatore di potassio (antikaliuretico) che possiede un'attività natriuretica, diuretica e antipertensiva debole (rispetto ai diuretici tiazidici). In alcuni studi clinici questi effetti si sono sommati parzialmente agli effetti dei diuretici tiazidici.» Testo originale in inglese: "Amiloride HCl is a potassium-conserving (antikaliuretic) drug that possesses weak (compared with thiazide diuretics) natriuretic, diuretic, and antihypertensive activity. These effects have been partially additive to the effects of thiazide diuretics in some clinical studies." ([DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68), versione del 2026-11-11; consultato il 2026-11-19). Sulla base delle informazioni note, amiloride agisce sul canale epiteliale del sodio (ENaC). Questo favorisce l'eliminazione di sodio (natriuresi) e il risparmio di potassio.

In linea teorica, l'azione sul sodio e sul volume potrebbe interessare il danno renale legato all'ipertensione. Si tratta però di un'ipotesi puramente predittiva: non esistono studi che la verifichino. Il punteggio elevato riflette l'associazione costruita dal modello, non una prova clinica.

C'è inoltre un'importante riserva di sicurezza. Il rischio di iperkaliemia è rilevante nei pazienti con compromissione della funzione renale, cioè proprio nella popolazione di interesse.

## Evidenze dagli studi clinici

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare |
|---------|------|------|
| 023070016 | MODURETIC*20 cpr 5 mg + 50 mg | NEOPHARMED GENTILI SpA |

Il nome del prodotto indica un'associazione a dose fissa (5 mg + 50 mg). Questa autorizzazione non descrive quindi la situazione regolatoria del singolo principio attivo.

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state rilevate 136 interazioni. Tra quelle di livello moderato figurano:
  - metformina;
  - corticosteroidi (idrocortisone, betametasone, budesonide, desametasone);
  - inibitori di SGLT2 (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin);
  - exenatide;
  - bupropione;
  - alcuni lassativi e agenti osmotici (bisacodile, olio di ricino, glicerina, lattitolo, lattulosio);
  - dronabinolo.

  Le interazioni con doxiciclina, amoxicillina e cimetidina sono di livello minore.
- **Iperkaliemia**: è il rischio principale da considerare, soprattutto con insufficienza renale e in presenza di farmaci interagenti.

Per avvertenze e controindicazioni complete si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Non esistono studi clinici né pubblicazioni che riguardino direttamente la nefropatia ipertensiva maligna, quindi il livello di evidenza è L5.
- Il rischio di iperkaliemia in caso di compromissione renale rende necessaria cautela.

**Per procedere sono necessari:**
- una revisione sistematica della letteratura mirata sulla nefropatia ipertensiva e su amiloride;
- dati precliniche e di meccanismo specifici per questa malattia;
- dati dettagliati sul meccanismo d'azione;
- il foglio illustrativo AIFA con avvertenze e controindicazioni;
- un piano di monitoraggio del potassio sierico e della funzione renale prima di qualsiasi studio clinico.

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale); le predizioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

