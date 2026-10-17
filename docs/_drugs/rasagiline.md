---
layout: default
title: Rasagiline
parent: Solo previsione del modello (L5)
nav_order: 374
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Rasagiline: nuova indicazione prevista, Neurodegenerazione associata a PLA2G6 (livello di evidenza L5). Indicazione originale: Morbo di Parkinson (e sindromi parkinsoniane correlate…"
monitor_inn: "Rasagiline"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
---

# Rasagiline
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

# Rasagilina: dal morbo di Parkinson alla neurodegenerazione associata a PLA2G6

## Sintesi in una frase

La rasagilina è un inibitore selettivo e irreversibile della monoamino ossidasi B (MAO-B), utilizzato originariamente per il trattamento del morbo di Parkinson e delle sindromi parkinsoniane correlate.
Il modello TxGNN prevede che possa essere efficace per la **neurodegenerazione associata a PLA2G6**.
Per questa direzione non risulta però alcuna evidenza: **0 studi clinici** e **0 pubblicazioni** nei dati compilati per questo report.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Morbo di Parkinson (e sindromi parkinsoniane correlate, secondo il grafo di conoscenza) |
| Nuova indicazione prevista | Neurodegenerazione associata a PLA2G6 |
| Punteggio di predizione TxGNN | 99,71% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle conoscenze farmacologiche generali, la rasagilina inibisce in modo selettivo e irreversibile la MAO-B, aumentando la disponibilità di dopamina; le sono inoltre attribuiti possibili effetti neuroprotettivi. La sua efficacia nel morbo di Parkinson è consolidata, e meccanicisticamente potrebbe essere applicabile ad alcuni aspetti della neurodegenerazione associata a PLA2G6.

La neurodegenerazione associata a PLA2G6 (che comprende la distrofia neuroassonale infantile e la distonia-parkinsonismo correlata a PLA2G6) condivide con il morbo di Parkinson manifestazioni parkinsoniane e patologia da alfa-sinucleina. Ciò spiega plausibilmente il punteggio molto elevato. In teoria, la rasagilina potrebbe attenuare il fenotipo distonico-parkinsoniano della forma ad esordio adulto.

Non ci si aspetta invece che modifichi il difetto di fondo, cioè il rimodellamento dei fosfolipidi e la disfunzione mitocondriale. Il legame meccanicistico si basa quindi solo su farmacologia generale, senza studi o letteratura a supporto.

**Altre predizioni del modello (tutte a bassa plausibilità o non nuove):**
- **Encefalite di Rasmussen** (99,56%): nessun legame meccanicistico evidente; il punteggio riflette probabilmente la vicinanza nella rete a nodi neurologici.
- **Mielite** (99,32%): nessun ruolo antinfiammatorio o immunomodulatore stabilito; esistono solo segnali neuroprotettivi preclinici.
- **Parkinsonismo giovanile di Hunt** (99,25%, livello L4): è sostanzialmente un sinonimo storico di indicazioni già coperte, quindi non rappresenta una vera opportunità di riposizionamento.
- **Deficit di transaldolasi** (99,19%) e **polimicrogiria perisilviana con ipoplasia cerebellare e artrogriposi** (99,01%): nessuna base meccanicistica plausibile; probabili artefatti del grafo.

---

## Evidenze da studi clinici

Attualmente non risulta alcuno studio clinico registrato correlato.

---

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Sono elencate le prime 5 autorizzazioni.

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|------|
| 044400012 | RASAGILINA*28 cpr 1 mg | DOC Generici Srl | Cancellata |
| 044372023 | AIDEX*28 cpr 1 mg | Ecupharma Srl | Cancellata |
| 043902016 | RASARAL*28 cpr 1 mg | Ralpharma Srl | Cancellata |
| 044945095 | RASABON*28 cpr 1 mg | Neuraxpharm Italy SpA | Cancellata |
| 036983029 | AZILECT*28 cpr 1 mg | Teva B.V. | Cancellata |

---

## Considerazioni di sicurezza

- **Controindicazioni derivate dal grafo di conoscenza** (relazioni farmaco-malattia, non testo del foglietto illustrativo): ipertensione e disturbi ipertensivi, atrofia multisistemica, sindrome da tachicardia posturale ortostatica, ipotensione ortostatica, discinesia indotta da farmaci, epilessia, disturbo bipolare, disturbo affettivo maggiore, epatopatie, malattie della colecisti, melanoma, feocromocitoma (surrenale), cancro del duodeno, dell'intestino tenue, del cuore e del surrene, paraganglioma simpatico.
- **Interazioni**: nei dati è presente solo il legame farmacologico con il bersaglio MAO-B (gene MAOB), senza interazioni farmaco-farmaco specifiche.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (livello L5): non ci sono studi clinici né letteratura, il legame meccanicistico è solo ipotetico e tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni ufficiali dal foglietto illustrativo AIFA
- Una revisione della letteratura mirata su rasagilina e neurodegenerazione associata a PLA2G6 (in particolare distonia-parkinsonismo ad esordio adulto)
- La verifica della possibilità pratica di ottenere il farmaco, dato lo stato di mercato "solo cancellate"
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

