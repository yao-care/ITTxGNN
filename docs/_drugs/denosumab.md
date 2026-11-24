---
layout: default
title: Denosumab
parent: Solo previsione del modello (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
last_modified_at: 2026-11-24
description: "Denosumab: nuova indicazione prevista, Retinopatia diabetica non proliferativa grave (severe nonproliferative diabetic retinopathy) (livello di evidenza L5). Indicazione originale: Non riportata nei …"
---

# Denosumab
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

## Denosumab: inibitore di RANKL (anticorpo monoclonale) → retinopatia diabetica non proliferativa grave (severe nonproliferative diabetic retinopathy)
{: .text-alpha }

## Sintesi in una frase

Denosumab è un anticorpo monoclonale che inibisce RANKL. Il modello TxGNN prevede una possibile efficacia nella **retinopatia diabetica non proliferativa grave (severe nonproliferative diabetic retinopathy)**, ma per questa indicazione non sono presenti **né studi clinici né pubblicazioni** a supporto: si tratta di una previsione puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Retinopatia diabetica non proliferativa grave (severe nonproliferative diabetic retinopathy) |
| Punteggio di predizione TxGNN | 0,9963 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Denosumab è un anticorpo monoclonale che inibisce RANKL. Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Denosumab (traduzione non ufficiale): «I prodotti a base di denosumab si legano al RANKL, una proteina transmembrana o solubile essenziale per la formazione, la funzione e la sopravvivenza degli osteoclasti, le cellule responsabili del riassorbimento osseo. I prodotti a base di denosumab impediscono al RANKL di attivare il suo recettore, RANK, sulla superficie degli osteoclasti e dei loro precursori.» Testo originale in inglese: "Denosumab products bind to RANKL, a transmembrane or soluble protein essential for the formation, function, and survival of osteoclasts, the cells responsible for bone resorption. Denosumab products prevent RANKL from activating its receptor, RANK, on the surface of osteoclasts and their precursors." ([DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd), versione del 2026-11-04; consultato il 2026-11-19).

Un possibile legame, ancora non validato, è che la via di segnalazione RANKL/OPG influenzi infiammazione, calcificazione vascolare e funzione endoteliale, processi che potrebbero riguardare la patologia microvascolare della retinopatia diabetica. Non sono disponibili meccanismi o dati specifici per la retina: la previsione resta quindi un'ipotesi da verificare.

Il punteggio è molto alto (0,9963), ma esso riflette solo l'output del modello e non sostituisce evidenze cliniche.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non è disponibile letteratura correlata per questa indicazione.

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 040108033 | PROLIA\*1 siringa SC 60 mg 1 ml | AMGEN EUROPE B.V. | Autorizzata |
| 041300017 | XGEVA\*1 flaconcino SC 120 mg 1,7 ml | AMGEN EUROPE B.V. | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

**Interazioni farmacologiche** (interrogazione completata, 100 interazioni totali; di seguito alcune di livello moderato):

- Corticosteroidi: idrocortisone, triamcinolone, desametasone, betametasone, budesonide, prednisolone, prednisone, metilprednisolone
- Immunosoppressori e farmaci correlati: tacrolimus, mercaptopurina, levamisolo, trimetrexato, dupilumab
- Radiofarmaci/anticorpi radiomarcati: ibritumomab tiuxetan, iobenguane (I-131), tositumomab, tositumomab (I-131)
- Ormoni: corticotropina, tetracosactide

Per le avvertenze e le controindicazioni si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio TxGNN elevato, ma non esistono studi clinici né pubblicazioni che studino direttamente la retinopatia diabetica non proliferativa grave; il livello di evidenza è quindi L5.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione di denosumab e sul suo possibile ruolo nella patologia microvascolare retinica
- Studi preclinici o clinici che valutino direttamente esiti retinici
- Avvertenze e controindicazioni dal foglio illustrativo AIFA per la valutazione della sicurezza
- Verifica della compatibilità di via di somministrazione e formulazione (ad es. sistemica vs. intravitreale)

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale); le predizioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

