---
layout: default
title: Moroctocog Alfa
parent: Solo previsione del modello (L5)
nav_order: 310
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
description: "Moroctocog Alfa: nuova indicazione prevista, Primary release disorder of platelets (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Moroctocog Alfa
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

## Moroctocog Alfa: Primary release disorder of platelets
{: .text-alpha }

## Sintesi in una frase

Moroctocog alfa è un fattore VIII della coagulazione ricombinante (privo del dominio B), originariamente usato per il trattamento dell'emofilia.
Il modello TxGNN prevede una possibile efficacia nel **disturbo da rilascio piastrinico primario**, ma questa previsione non è sostenuta da **alcuno studio clinico** né da **alcuna pubblicazione**: si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Primary release disorder of platelets |
| Punteggio di previsione TxGNN | 0.9997 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 7 su 7) |
| Numero di autorizzazioni | 7 (valide: 7) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. Moroctocog alfa è un fattore VIII ricombinante privo del dominio B, che sostituisce il FVIII endogeno nel complesso tenasi intrinseco. La sua efficacia nell'emofilia si fonda proprio su questa funzione sostitutiva.

Il disturbo da rilascio piastrinico primario dipende invece da difetti della secrezione dei granuli piastrinici e della trasduzione del segnale, non da una carenza di FVIII. Non emerge quindi un legame meccanicistico plausibile. L'elevato punteggio TxGNN è probabilmente un artefatto di prossimità nella rete di conoscenza, dovuto al vicinato condiviso dei disturbi emorragici e dell'emostasi.

### Altre indicazioni previste (tutte senza evidenze cliniche)

| Posizione | Malattia prevista | Punteggio TxGNN | Valutazione del legame meccanicistico |
|------|------|------|------|
| 2 | Pseudo-malattia di von Willebrand | 0,9997 | Associazione biologica debole: il FVIII si lega al VWF, ma il difetto primario è a carico del GPIbα piastrinico; la terapia standard è la trasfusione di piastrine |
| 3 | Trombastenia di Glanzmann | 0,9996 | Difetto dell'integrina αIIbβ3; la sostituzione del FVIII non lo corregge; standard: piastrine e FVIIa ricombinante |
| 4 | Carenza acquisita di fattori della coagulazione | 0,9988 | Candidata più plausibile sul piano meccanicistico, ma nell'emofilia acquisita gli autoanticorpi inibitori neutralizzano il FVIII; la categoria è inoltre eterogenea |
| 5 | Sindrome di Scott | 0,9986 | Difetto di esposizione della fosfatidilserina (TMEM16F/ANO6); legame indiretto e speculativo |
| 6 | Diatesi emorragica da difetto del recettore del collagene | 0,9973 | Patologia dell'adesione piastrina-parete vasale, non della cascata dipendente dal FVIII |
| 7 | Disordine emorragico da trombocitopenia costituzionale | 0,9972 | Il problema è il numero o la funzione piastrinica, non il FVIII |
| 8 | "Flood factor deficiency" | 0,9911 | Termine non riconducibile a un'entità clinica nota, probabilmente un'etichetta errata o ambigua dell'ontologia; da verificare prima di ogni valutazione |

## Evidenze dagli studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano


| Numero di autorizzazione | Nome del prodotto | Indicazione approvata |
|---------|------|-----------|
| 034421053 | REFACTO AF siringa preriempita EV 3.000 UI + solvente 4 ml + kit per infusione | Non disponibile nei dati |
| 034421040 | REFACTO AF flaconcino EV 2.000 UI + siringa 4 ml | Non disponibile nei dati |
| 034421077 | REFACTO AF siringa preriempita EV 1.000 UI + solvente 4 ml + kit per infusione | Non disponibile nei dati |
| 034421065 | REFACTO AF siringa preriempita EV 500 UI + solvente 4 ml + kit per infusione | Non disponibile nei dati |
| 034421038 | REFACTO AF flaconcino EV 1.000 UI + siringa 4 ml | Non disponibile nei dati |

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Nei dati compilati per questo report non risultano interazioni farmacologiche registrate.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per il disturbo da rilascio piastrinico primario si basa solo sul modello (L5), senza studi clinici né letteratura. Il difetto piastrinico non è mediato dal FVIII, e il prodotto non ha più autorizzazioni valide in Italia.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione del farmaco
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Una revisione sistematica della letteratura e delle registrazioni di studi per le indicazioni previste
- La verifica dell'identità della malattia "flood factor deficiency"
- Una valutazione preliminare della carenza acquisita di fattori della coagulazione, la candidata meccanicisticamente più plausibile, tenendo conto degli inibitori anti-FVIII
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

