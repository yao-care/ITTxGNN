---
layout: default
title: Albutrepenonacog Alfa
parent: Solo previsione del modello (L5)
nav_order: 25
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "ALBUTREPENONACOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
description: "Albutrepenonacog Alfa: nuova indicazione prevista, Malattia di pseudo-von Willebrand (livello di evidenza L5). Indicazione originale: Emofilia (inclusa la forma sintomatica nelle portatrici femminili"
---

# Albutrepenonacog Alfa
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

## Albutrepenonacog alfa: dall'emofilia alla malattia di von Willebrand pseudo-tipo (pseudo-von Willebrand)
{: .text-alpha }

## Sintesi

Albutrepenonacog alfa è un fattore IX della coagulazione ricombinante fuso con albumina, utilizzato originariamente per il trattamento dell'emofilia. Il modello TxGNN ne prevede una possibile efficacia nella **malattia di pseudo-von Willebrand**, ma **non risulta alcuno studio clinico né alcuna pubblicazione** a supporto di questa direzione: la previsione resta puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Emofilia (inclusa la forma sintomatica nelle portatrici femminili) |
| Nuova indicazione prevista | Malattia di pseudo-von Willebrand |
| Punteggio di predizione TxGNN | 99,94% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 3 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle informazioni note, albutrepenonacog alfa è un fattore IX ricombinante legato all'albumina (rIX-FP), che sostituisce l'attività del fattore IX mancante nell'emofilia B.

La malattia di pseudo-von Willebrand, invece, è un disturbo di tipo piastrinico, causato da un difetto di guadagno di funzione della GPIbα piastrinica, che aumenta il legame con il fattore di von Willebrand. Non si tratta di un deficit di fattore IX, quindi **non esiste un razionale meccanicistico chiaro** per la terapia sostitutiva con fattore IX. Il punteggio elevato di TxGNN (0,9994) deriva solo dalla struttura del grafo di conoscenza e va interpretato con grande cautela.

Anche le altre indicazioni previste condividono questo limite. Si tratta di disturbi piastrinici o della superficie piastrinica, in cui il fattore IX non corregge il difetto di fondo:

| Rango | Malattia prevista | Punteggio TxGNN | Considerazione |
|------|------|------|------|
| 2 | Disturbo primario del rilascio piastrinico | 99,94% | Difetto di secrezione dei granuli; ogni legame passa solo da un effetto emostatico generico, speculativo |
| 3 | Trombastenia di Glanzmann | 99,92% | Difetto dell'integrina αIIbβ3; la gestione standard prevede trasfusioni di piastrine e fattore VIIa ricombinante |
| 4 | Sindrome di Scott | 99,63% | Difetto di esposizione della fosfatidilserina (TMEM16F/ANO6); legame concettuale vago con il complesso tenasi, senza evidenze |
| 5 | Diatesi emorragica da difetto del recettore del collagene | 99,28% | Difetto dei recettori piastrinici (es. GPVI); nessun supporto meccanicistico |
| 6 | Disordine emorragico da trombocitopenia costituzionale | 99,26% | Deficit numerico delle piastrine, non del fattore IX |

---

## Evidenze degli studi clinici

Attualmente non risulta alcuno studio clinico correlato registrato.

---

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 044891036 | IDELVION, 1 flacone EV 1.000 UI + solvente e dispositivi per la somministrazione | CSL Behring GmbH | Cancellata |
| 044891024 | IDELVION, 1 flacone EV 500 UI + solvente e dispositivi per la somministrazione | CSL Behring GmbH | Cancellata |
| 044891048 | IDELVION, 1 flacone EV 2.000 UI + solvente e dispositivi per la somministrazione | CSL Behring GmbH | Cancellata |

---

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Nei dati compilati per questo report non risultano interazioni farmacologiche note.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello computazionale (livello L5), senza studi clinici né letteratura. Inoltre il meccanismo del fattore IX non corrisponde al difetto piastrinico della malattia prevista, e tutte le autorizzazioni italiane risultano cancellate.

**Per procedere è necessario:**
- Reperire e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un ostacolo bloccante per lo screening di sicurezza
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Condurre una revisione sistematica della letteratura e uno studio preclinico per verificare un eventuale legame meccanicistico
- Chiarire la situazione regolatoria in Italia (motivo e implicazioni delle cancellazioni) e la compatibilità della via di somministrazione
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

