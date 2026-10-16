---
layout: default
title: Tolcapone
parent: Solo previsione del modello (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tolcapone: nuova indicazione prevista, Encefalite subacuta di Rasmussen (livello di evidenza L5). Indicazione originale: Morbo di Parkinson e sindromi parkinsoniane correlate (il testo dell'…"
---

# Tolcapone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Tolcapone: Dal morbo di Parkinson alla encefalite subacuta di Rasmussen

## Sintesi in una frase

Tolcapone è un inibitore della COMT, originariamente impiegato nel trattamento del morbo di Parkinson e delle sindromi parkinsoniane correlate. Il modello TxGNN ne prevede una possibile efficacia nell'**encefalite subacuta di Rasmussen**, ma per questa direzione non risultano **né studi clinici né pubblicazioni** a supporto: la previsione si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Morbo di Parkinson e sindromi parkinsoniane correlate (il testo dell'indicazione autorizzata in Italia non è disponibile) |
| Nuova indicazione prevista | Encefalite subacuta di Rasmussen |
| Punteggio di previsione TxGNN | 99,93% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 (revocata) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle informazioni note, tolcapone è un inibitore della catecol-O-metiltransferasi (COMT), enzima che degrada le catecolamine, ed è utilizzato nel morbo di Parkinson per prolungare l'effetto della levodopa.

Tra l'indicazione originale e quella prevista **non emerge un legame meccanicistico plausibile**. L'encefalite di Rasmussen è una encefalite cronica immuno-mediata, con neuroinfiammazione sostenuta dai linfociti T, mentre l'inibizione della COMT agisce sul metabolismo delle catecolamine. L'elevato punteggio (0,999) riflette probabilmente la vicinanza nel grafo di conoscenza ad altre patologie neurologiche, più che una base biologica specifica.

Altre previsioni nella stessa lista sono più coerenti dal punto di vista biologico:
- **Demenza a corpi di Lewy** (punteggio 99,64%): condivide con il Parkinson la patologia da alfa-sinucleina e la disfunzione dopaminergica. L'unica pubblicazione trovata è però un modello preclinico, non uno studio su tolcapone.
- **Neurodegenerazione associata a PLA2G6**: i fenotipi di distonia-parkinsonismo si sovrappongono a quelli dell'indicazione originale, ma non esistono evidenze dirette.
- **Paralisi agitante giovanile di Hunt**: è un termine storico per il parkinsonismo a esordio giovanile, quindi molto vicino alle indicazioni originali. Si tratta più di un'indicazione affine che di un vero riposizionamento.

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Per l'encefalite subacuta di Rasmussen al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 033280049 | TASMAR 100 mg compresse rivestite (flacone) | Non indicata | Non indicata (autorizzazione revocata; titolare: Viatris Healthcare Limited) |

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal grafo di conoscenza** (non dal foglio illustrativo): malattia epatica, malattia della colecisti, melanoma, disturbi ipotensivi, rabdomiolisi, fascite nodulare, discinesia tardiva, discinesia linguo-facciale-buccale.
- **Interazioni farmacologiche**: sono state identificate 65 interazioni. Quelle di gravità **maggiore** includono il **blu di metilene**. Tra quelle di gravità moderata figurano epinefrina, morfina, codeina, dronabinolo, nabilone, naltrexone, metoclopramide, prometazina, clorfenamina, cetirizina, destrometorfano ed etanolo. Per warfarin e dicumarolo la gravità è minore. L'interazione con omeprazolo ha livello non classificato.
- **Epatotossicità**: segnalata nell'analisi delle singole previsioni come rischio rilevante, in particolare in malattie epatiche o metaboliche e in pazienti pediatrici.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per l'encefalite di Rasmussen è priva di studi clinici, di letteratura e di un legame meccanicistico plausibile (livello L5). Il prodotto è inoltre senza autorizzazioni valide in Italia e presenta un noto rischio di epatotossicità.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e un'analisi della plausibilità biologica rispetto alla patogenesi immuno-mediata.
- Avvertenze e controindicazioni del foglio illustrativo AIFA.
- Evidenze precliniche o cliniche specifiche per tolcapone.
- Una valutazione del rapporto rischio-beneficio epatico e della fattibilità regolatoria, dato lo stato di autorizzazione revocata.
- Come alternativa, dare priorità alle previsioni più coerenti con l'indicazione originale (demenza a corpi di Lewy, parkinsonismo giovanile) come quesiti di ricerca.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

