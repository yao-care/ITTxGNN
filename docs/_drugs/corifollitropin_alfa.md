---
layout: default
title: Corifollitropin Alfa
parent: Solo previsione del modello (L5)
nav_order: 128
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Corifollitropin Alfa: nuova indicazione prevista, Gastroduodenite (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (il testo dell'indicazione nelle a…"
monitor_inn: "corifollitropin alfa"
predicted_indications: ["gastroduodenitis", "migraine disorder", "peptic ulcer disease", "migraine with brainstem aura", "Raynaud disease", "pulmonary hypertension", "kyphoscoliotic heart disease", "migraine with or without aura, susceptibility to"]
---

# Corifollitropin Alfa
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

# Corifollitropina alfa: dall'indicazione originale a gastroduodenite (predizione computazionale)

## Sintesi in una frase

La corifollitropina alfa è un analogo ricombinante dell'FSH a lunga durata d'azione. Nei dati compilati per questo report non risulta alcuna indicazione approvata registrata. Il modello TxGNN ne predice l'efficacia per la **gastroduodenite** con un punteggio molto alto, ma **non sono presenti studi clinici né pubblicazioni** a supporto: la predizione resta puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (il testo dell'indicazione nelle autorizzazioni AIFA è vuoto) |
| Nuova indicazione predetta | Gastroduodenite |
| Punteggio di predizione TxGNN | 99,65% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (entrambe cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione può (o non può) essere ragionevole?

Il meccanismo d'azione dettagliato non è disponibile nei dati compilati. In base alle conoscenze generali, la corifollitropina alfa è un analogo a lunga durata dell'FSH (subunità beta dell'FSH fusa con il peptide carbossi-terminale della beta-hCG) che agisce sui recettori dell'FSH nel tessuto gonadico.

Per la gastroduodenite non è stato identificato alcun legame meccanicistico plausibile: il coinvolgimento del recettore dell'FSH nell'infiammazione della mucosa gastroduodenale non è accertato. Il punteggio elevato (0,997) deriva da un modello basato su grafi di conoscenza e riflette probabilmente artefatti di prossimità nella rete, più che una reale biologia.

Anche le altre predizioni del modello non sono supportate da evidenze:

| Rango | Malattia predetta | Punteggio TxGNN | Osservazione |
|------|------|------|------|
| 2 | Emicrania | 99,63% | Link ormonale indiretto; la stimolazione gonadotropinica aumenta l'estradiolo e potrebbe peggiorare l'emicrania |
| 3 | Ulcera peptica | 99,61% | Nessun meccanismo noto che colleghi l'agonismo FSH a secrezione acida o difesa mucosa |
| 4 | Emicrania con aura del tronco encefalico | 99,59% | Sottotipo raro a base genetica; possibile rischio di scatenare l'aura con picchi estrogenici |
| 5 | Malattia di Raynaud | 99,59% | Influenza ormonale sul tono vascolare, ma nessun meccanismo FSH dimostrato |
| 6 | Ipertensione polmonare | 99,44% | La sindrome da iperstimolazione ovarica potrebbe essere dannosa in malattie cardiopolmonari |
| 7 | Cardiopatia cifoscoliotica | 99,36% | Condizione secondaria a deformità spinale; probabile artefatto di rete |
| 8 | Suscettibilità a emicrania con o senza aura | 99,11% | Fenotipo di suscettibilità genetica, non un'indicazione trattabile |

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Titolare |
|---------|------|------|-----------|------|
| 039943028 | ELONVA siringa preriempita SC 150 mcg 0,5 ml + 1 ago | n.d. | Cancellata | ORGANON N.V. |
| 039943016 | ELONVA siringa preriempita SC 100 mcg 0,5 ml + 1 ago | n.d. | Cancellata | ORGANON N.V. |

---

## Considerazioni di sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Dalle informazioni sul farmaco si possono comunque segnalare, in via generale, i rischi noti delle gonadotropine, in particolare la sindrome da iperstimolazione ovarica, potenzialmente sfavorevole in presenza di patologie cardiopolmonari. Non sono state rilevate interazioni farmacologiche nei dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione è solo computazionale (livello L5), senza studi clinici né letteratura, e priva di un meccanismo biologico plausibile. Inoltre le autorizzazioni italiane sono tutte cancellate e mancano i dati di sicurezza del foglio illustrativo.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Una revisione della letteratura per verificare un'eventuale base biologica dell'FSH nelle patologie gastroduodenali
- Una valutazione di priorità: dato il profilo ormonale del farmaco, le indicazioni predette (in particolare emicrania e ipertensione polmonare) richiederebbero un'attenta valutazione del rischio
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

