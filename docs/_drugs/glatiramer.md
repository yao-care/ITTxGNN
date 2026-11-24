---
layout: default
title: Glatiramer
parent: Solo previsione del modello (L5)
nav_order: 221
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Glatiramer: nuova indicazione prevista, Emoglobinopatia (livello di evidenza L5). Indicazione originale: Non riportata nei dati compilati per questo report (le autorizzazioni…"
monitor_inn: "GLATIRAMER"
predicted_indications: ["hemoglobinopathy"]
---

# Glatiramer
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

## Glatiramer: dalla sclerosi multipla all'emoglobinopatia
{: .text-alpha }

## Sintesi

Glatiramer (glatiramer acetato) è un immunomodulatore utilizzato nella sclerosi multipla. Il modello TxGNN lo associa all'**emoglobinopatia** con un punteggio molto alto, ma l'associazione non è supportata da evidenze reali: non risultano **sperimentazioni cliniche** e l'unica **pubblicazione** collegata non riguarda questa indicazione.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati compilati per questo report (le autorizzazioni AIFA non contengono il testo dell'indicazione) |
| Nuova indicazione prevista | Emoglobinopatia |
| Punteggio di previsione TxGNN | 0,9903 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 4 su 4) |
| Numero di autorizzazioni | 4 (valide: 4) |
| Decisione raccomandata | Hold |

## Perché questa previsione è (poco) plausibile?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Glatiramer (traduzione non ufficiale): «Il meccanismo o i meccanismi attraverso i quali glatiramer acetato esercita i suoi effetti nei pazienti con SM non sono completamente compresi. Tuttavia, si ritiene che glatiramer acetato agisca modificando i processi immunitari che si ritiene siano responsabili della patogenesi della SM.» Testo originale in inglese: "The mechanism(s) by which glatiramer acetate exerts its effects in patients with MS are not fully understood. However, glatiramer acetate is thought to act by modifying immune processes that are believed to be responsible for the pathogenesis of MS." ([DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716), versione del 2026-10-26; consultato il 2026-11-19). In base alle conoscenze generali, glatiramer acetato è un immunomodulatore che sposta la risposta dei linfociti T verso un fenotipo Th2 e agisce come "esca" per la proteina basica della mielina nella sclerosi multipla.

Le emoglobinopatie (ad esempio anemia falciforme e talassemie) sono causate da difetti nella struttura o nell'espressione dei geni della globina. Con i dati disponibili non emerge alcun ponte meccanicistico plausibile tra l'azione immunomodulatoria di glatiramer e la fisiopatologia di queste malattie.

Il punteggio elevato di TxGNN è un risultato del modello TxGNN (deep learning), non un'evidenza clinica. Il punteggio può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

<!-- review:begin it-lic-20261106-glatiramer-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Tutte e 4 le autorizzazioni risultano cancellate; non vi sono autorizzazioni valide.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-glatiramer-1 -->

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Caso clinico / commento | Revue neurologique | Disturbi immunitari multipli dopo l'interruzione di natalizumab in una paziente con sclerosi multipla e anamnesi di beta-talassemia. Non riguarda glatiramer né dimostra un'attività in questa condizione. |

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 035418060 | COPAXONE\*12 siringhe SC 40 mg/ml 1 ml + ago | TEVA GmbH | Autorizzata |
| 043860028 | COPEMYL\*28 siringhe SC 20 mg/ml | MYLAN SpA | Autorizzata |
| 045673023 | COPEMYLTRI\*12 siringhe preriempite 40 mg/ml 1 ml | MYLAN SpA | Autorizzata |
| 035418021 | COPAXONE\*28 siringhe SC 20 mg/ml 1 ml | TEVA GmbH | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: è stata rilevata 1 interazione di livello **Maggiore** con **natalizumab** (fonte: DDInter).

Per le altre informazioni di sicurezza (avvertenze e controindicazioni) si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul punteggio del modello (livello L5), senza sperimentazioni cliniche né letteratura pertinente e senza un meccanismo plausibile.

<!-- review:begin it-lic-20261106-glatiramer-2 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «La previsione si basa solo sul punteggio del modello (livello L5), senza sperimentazioni cliniche né letteratura pertinente e senza un meccanismo plausibile. Inoltre, in Italia non vi sono autorizzazioni attive.» Rimosso: l'affermazione contraddiceva i dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-glatiramer-2 -->

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (ad esempio da DrugBank) per valutare un eventuale collegamento biologico con le emoglobinopatie
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, indispensabili per lo screening di sicurezza
- Studi preclinici o mirati che mostrino un'attività di glatiramer in modelli di emoglobinopatia
- Verifica dello stato regolatorio attuale e della disponibilità del prodotto in Italia

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «Tutte e 4 le autorizzazioni risultano cancellate; non vi sono autorizzazioni valide» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-24 | Rimosso: «Inoltre, in Italia non vi sono autorizzazioni attive» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

