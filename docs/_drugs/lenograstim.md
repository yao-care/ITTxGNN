---
layout: default
title: Lenograstim
parent: Solo previsione del modello (L5)
nav_order: 260
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Lenograstim: nuova indicazione prevista, Disturbo primario del rilascio piastrinico (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (testo dell'indicazione assente…"
monitor_inn: "LENOGRASTIM"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "severe nonproliferative diabetic retinopathy"]
---

# Lenograstim
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# Lenograstim: Dal trattamento della neutropenia al disturbo primario del rilascio piastrinico

## Sintesi in una frase

Lenograstim è un fattore di crescita ricombinante umano dei granulociti (G-CSF) che agisce sulla linea granulocitaria; i dati compilati per questo report non riportano un'indicazione approvata, perché il testo dell'indicazione è vuoto nell'unica autorizzazione AIFA, ormai cancellata.
Il modello TxGNN lo associa al **disturbo primario del rilascio piastrinico** con un punteggio molto alto, ma **non esistono studi clinici né pubblicazioni** a supporto di questa previsione.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (testo dell'indicazione assente nell'autorizzazione AIFA) |
| Nuova indicazione prevista | Disturbo primario del rilascio piastrinico |
| Punteggio di previsione TxGNN | 99,91% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni cancellate |
| Numero di autorizzazioni | 1 (cancellata) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

Dati dettagliati sul meccanismo d'azione non sono al momento disponibili nei dati compilati. Lenograstim è un G-CSF ricombinante umano che agisce sulla linea granulocitaria tramite il recettore del G-CSF.

I disturbi del rilascio piastrinico (difetti dei granuli di deposito o della secrezione) sono difetti qualitativi della funzione piastrinica. Non è stabilito alcun legame meccanicistico diretto con la via di segnalazione del G-CSF. L'alto punteggio TxGNN (0,999) deriva da una previsione basata sulla rete di conoscenza e non è supportato da dati biologici o clinici.

Altre previsioni del modello, tutte con livello di evidenza L5 e raccomandazione Hold:

| Indicazione prevista | Punteggio TxGNN | Considerazione meccanicistica |
|------|------|------|
| Trombastenia di Glanzmann | 99,89% | Il difetto riguarda il recettore integrinico αIIbβ3 (GPIIb/IIIa); il G-CSF non agisce su questa via. Un ruolo di supporto nel trapianto di cellule staminali è solo speculativo. |
| Pseudo-malattia di von Willebrand | 99,88% | Dovuta a una mutazione con guadagno di funzione di GPIbα; nessuna azione nota del G-CSF su GPIb-IX-V o sul VWF. |
| Retinopatia diabetica non proliferativa grave | 99,61% | Link teorico tramite la mobilizzazione di progenitori endoteliali dal midollo osseo, ma il G-CSF potrebbe favorire infiammazione e neovascolarizzazione retinica, con possibili problemi di sicurezza. |

## Evidenze dagli studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 029059096 | MYELOSTIM (polvere per uso EV/SC, 34 milioni UI/ml, con siringa di solvente preriempita e 2 aghi) | Non specificata | Non specificata |

Titolare: ITALFARMACO SpA. Lo stato dell'autorizzazione è **cancellato**: non risultano autorizzazioni valide in Italia.

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Non sono state trovate interazioni farmacologiche nei dati compilati.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello (L5), senza studi clinici né letteratura. Il meccanismo del G-CSF non è collegato in modo plausibile ai difetti qualitativi delle piastrine. L'unica autorizzazione italiana è cancellata e mancano i dati di sicurezza.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione (ad esempio da DrugBank)
- Indicazione originale approvata
- Ricerca sistematica di studi clinici e letteratura sulle indicazioni previste
- Valutazione di compatibilità delle vie di somministrazione
- Per la retinopatia diabetica, una valutazione specifica del rischio di neovascolarizzazione e infiammazione retinica
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

