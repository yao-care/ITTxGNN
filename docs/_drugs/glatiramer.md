---
layout: default
title: Glatiramer
parent: Solo previsione del modello (L5)
nav_order: 221
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
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

Il meccanismo d'azione originale non è disponibile nei dati compilati. In base alle conoscenze generali, glatiramer acetato è un immunomodulatore che sposta la risposta dei linfociti T verso un fenotipo Th2 e agisce come "esca" per la proteina basica della mielina nella sclerosi multipla.

Le emoglobinopatie (ad esempio anemia falciforme e talassemie) sono causate da difetti nella struttura o nell'espressione dei geni della globina. Con i dati disponibili non emerge alcun ponte meccanicistico plausibile tra l'azione immunomodulatoria di glatiramer e la fisiopatologia di queste malattie.

Il punteggio elevato di TxGNN è un risultato del modello TxGNN (deep learning), non un'evidenza clinica. Il punteggio può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Caso clinico / commento | Revue neurologique | Disturbi immunitari multipli dopo l'interruzione di natalizumab in una paziente con sclerosi multipla e anamnesi di beta-talassemia. Non riguarda glatiramer né dimostra un'attività in questa condizione. |

## Informazioni sul mercato italiano

Tutte e 4 le autorizzazioni risultano cancellate; non vi sono autorizzazioni valide.

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Titolare | Indicazione approvata |
|---------|------|------|------|-----------|
| 035418060 | COPAXONE 12 siringhe SC 40 mg/ml 1 ml + ago | Non disponibile | TEVA GmbH | Non disponibile |
| 043860028 | COPEMYL 28 siringhe SC 20 mg/ml | Non disponibile | MYLAN SpA | Non disponibile |
| 045673023 | COPEMYLTRI 12 siringhe preriempite 40 mg/ml 1 ml | Non disponibile | MYLAN SpA | Non disponibile |
| 035418021 | COPAXONE 28 siringhe SC 20 mg/ml 1 ml | Non disponibile | TEVA GmbH | Non disponibile |

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: è stata rilevata 1 interazione di livello **Maggiore** con **natalizumab** (fonte: DDInter).

Per le altre informazioni di sicurezza (avvertenze e controindicazioni) si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul punteggio del modello (livello L5), senza sperimentazioni cliniche né letteratura pertinente e senza un meccanismo plausibile. Inoltre, in Italia non vi sono autorizzazioni attive.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (ad esempio da DrugBank) per valutare un eventuale collegamento biologico con le emoglobinopatie
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, indispensabili per lo screening di sicurezza
- Studi preclinici o mirati che mostrino un'attività di glatiramer in modelli di emoglobinopatia
- Verifica dello stato regolatorio attuale e della disponibilità del prodotto in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

