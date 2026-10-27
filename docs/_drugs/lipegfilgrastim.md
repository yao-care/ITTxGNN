---
layout: default
title: Lipegfilgrastim
parent: Solo previsione del modello (L5)
nav_order: 273
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Lipegfilgrastim: nuova indicazione prevista, Disturbo primario di rilascio piastrinico (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (il testo dell'indicazione A…"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "diabetic retinopathy"]
---

# Lipegfilgrastim
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

## Lipegfilgrastim: dall'uso nella neutropenia al disturbo primario di rilascio piastrinico
{: .text-alpha }

## Sintesi in una frase

Lipegfilgrastim è un analogo pegilato del fattore stimolante le colonie di granulociti (G-CSF), che stimola la proliferazione e la differenziazione della linea neutrofila. Il modello TxGNN lo indica come possibile candidato per il **disturbo primario di rilascio piastrinico**, ma attualmente **non risultano studi clinici né pubblicazioni** a sostegno di questa ipotesi: si tratta di una previsione puramente computazionale.

Nota: i dati compilati per questo report non riportano il testo dell'indicazione approvata in Italia; la descrizione dell'uso originario deriva dalla classe farmacologica del prodotto.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (il testo dell'indicazione AIFA è vuoto) |
| Nuova indicazione prevista | Disturbo primario di rilascio piastrinico |
| Punteggio di previsione TxGNN | 99,93% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (nessuna attualmente valida) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere plausibile?

I dati sul meccanismo d'azione originale non sono al momento disponibili. Lipegfilgrastim appartiene alla classe dei G-CSF pegilati, che agiscono sul recettore del G-CSF delle cellule mieloidi stimolando la proliferazione e la differenziazione dei neutrofili.

Il disturbo primario di rilascio piastrinico è invece un difetto qualitativo della funzione piastrinica (alterata secrezione dei granuli e della segnalazione). **Non esiste un legame meccanicistico noto** tra la segnalazione del recettore del G-CSF e le vie di secrezione piastrinica. L'elevato punteggio TxGNN (0,999) è quindi una previsione basata sul grafo di conoscenza, senza conferma clinica.

### Altre previsioni del modello (tutte di livello L5, decisione Hold)

| Rango | Indicazione prevista | Punteggio TxGNN | Considerazione |
|------|------|------|------|
| 2 | Retinopatia diabetica non proliferante grave | 99,91% | Possibile ruolo teorico della mobilizzazione di cellule progenitrici nella riparazione vascolare, ma il G-CSF potrebbe favorire neovascolarizzazione o infiammazione retinica; ipotesi speculativa |
| 3 | Pseudo-malattia di von Willebrand | 99,91% | Difetto di gain-of-function della GPIbα piastrinica; il lipegfilgrastim non ha effetti noti sull'asse GPIb-VWF |
| 4 | Trombastenia di Glanzmann | 99,91% | Deficit dell'integrina αIIbβ3; l'agonismo sul recettore del G-CSF non corregge il difetto |
| 5 | Retinopatia diabetica | 99,75% | Come per la forma non proliferante grave, solo ipotesi speculativa |

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Indicazione approvata |
|---------|------|------|------|-----------|
| 042919011 | LONQUEX*1 siringa 6 mg 0,6 ml (TEVA B.V.) | Non indicata | Cancellata | Non indicata |
| 042919047 | LONQUEX*6 flaconcini SC 6 mg 0,6 ml (TEVA B.V.) | Non indicata | Cancellata | Non indicata |

---

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Nei dati compilati non sono presenti avvertenze, controindicazioni o interazioni farmacologiche documentate.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Tutte le previsioni poggiano esclusivamente sul punteggio del modello TxGNN, senza studi clinici, pubblicazioni né un razionale meccanicistico plausibile. Inoltre, in Italia le autorizzazioni disponibili sono entrambe cancellate.

**Per procedere sono necessari:**
- Recupero e analisi del foglio illustrativo AIFA (indicazioni, avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank per analizzare un eventuale legame meccanicistico
- Studi preclinici o revisioni della letteratura che colleghino la segnalazione del G-CSF alla funzione piastrinica
- Verifica della compatibilità delle vie di somministrazione e chiarimento dello stato regolatorio (autorizzazioni cancellate)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

