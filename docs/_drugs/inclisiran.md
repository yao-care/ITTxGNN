---
layout: default
title: Inclisiran
parent: Solo previsione del modello (L5)
nav_order: 236
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Inclisiran: nuova indicazione prevista, Carenza di potassio (potassium deficiency disease) (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (il testo dell'indicazio…"
monitor_inn: "INCLISIRAN"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Inclisiran: Dall'ipercolesterolemia a una predizione di carenza di potassio (ipopotassiemia)
{: .text-alpha }

## Sintesi in una frase

Inclisiran è un siRNA che silenzia la sintesi epatica di PCSK9 per ridurre il colesterolo LDL. Il modello TxGNN lo associa con punteggio molto alto alla **carenza di potassio**, ma la predizione è puramente computazionale: per questa indicazione non risultano **studi clinici** né **pubblicazioni**.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (il testo dell'indicazione nell'autorizzazione AIFA è vuoto) |
| Nuova indicazione prevista | Carenza di potassio (potassium deficiency disease) |
| Punteggio di predizione TxGNN | 0,9993 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold |

## Perché questa predizione è plausibile?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Inclisiran (traduzione non ufficiale): «Inclisiran è un acido ribonucleico a doppio filamento a piccola interferenza (siRNA), coniugato sul filamento senso con N-acetilgalattosamina (GalNAc) triantennaria per facilitarne la captazione da parte degli epatociti. Negli epatociti, inclisiran utilizza il meccanismo di interferenza dell'RNA e dirige la degradazione catalitica dell'mRNA per PCSK9.» Testo originale in inglese: "Inclisiran is a double-stranded small interfering ribonucleic acid (siRNA), conjugated on the sense strand with triantennary N-Acetylgalactosamine (GalNAc) to facilitate uptake by hepatocytes. In hepatocytes, inclisiran utilizes the RNA interference mechanism and directs catalytic breakdown of mRNA for PCSK9." ([DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44), versione del 2026-08-19; consultato il 2026-11-19). In base alle conoscenze generali, inclisiran è un piccolo RNA interferente (siRNA) che riduce la sintesi epatica di PCSK9, con conseguente calo del colesterolo LDL.

Non emerge alcun legame meccanicistico plausibile tra il silenziamento di PCSK9 e l'omeostasi del potassio. L'elevato punteggio TxGNN (0,9993) è un risultato derivato dal modello e non è sostenuto da alcuno studio clinico o pubblicazione. Va quindi considerato solo un'ipotesi da verificare, non un'indicazione supportata.

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati alla carenza di potassio.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 049274020 | LEQVIO\*1 siringa preriempita SC 1,5 ml 284 mg 189 mg/ml con dispositivo di protezione del… | NOVARTIS EUROPHARM LTD | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. I dati compilati non contengono avvertenze, controindicazioni o interazioni farmacologiche documentate.

## Altre predizioni nella classifica (per contesto)

Tutte le prime 10 predizioni hanno livello di evidenza L5 e raccomandazione Hold. Le altre sono: malattia esofagea, coartazione atipica dell'aorta, emicrania (varie forme), malformazione esofagea non sindromica, ulcera esofagea, malattia di Raynaud e malformazione aortica.

Per la malformazione aortica risultano collegati due studi di fase 3 su inclisiran (NCT06597019 e NCT06597006, in reclutamento), ma riguardano bambini con ipercolesterolemia familiare eterozigote e omozigote. Il collegamento è con ogni probabilità un artefatto di mappatura dei termini di malattia, per cui l'evidenza non è stata elevata sopra L5.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (L5), senza studi né letteratura e senza alcun razionale meccanicistico plausibile. Mancano i dati di sicurezza del foglio illustrativo.

<!-- review:begin it-lic-20261106-inclisiran-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Inoltre l'unica autorizzazione italiana risulta cancellata e mancano i dati di sicurezza del foglio illustrativo.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-inclisiran-1 -->

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank, per valutare un eventuale legame con l'omeostasi del potassio
- Scarico e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), necessario per lo screening di sicurezza
- Una revisione della letteratura mirata sul rapporto tra inclisiran/PCSK9 ed elettroliti
- Verifica delle condizioni effettivamente studiate in NCT06597019 e NCT06597006 prima di qualsiasi riclassificazione

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «Inoltre l'unica autorizzazione italiana risulta cancellata e m» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

