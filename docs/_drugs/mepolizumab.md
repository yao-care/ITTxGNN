---
layout: default
title: Mepolizumab
parent: Prove moderate (L3-L4)
nav_order: 285
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-15
description: "Mepolizumab: nuova indicazione prevista, Trombocitopenia da distruzione immunitaria (livello di evidenza L4). Indicazione originale: Polmonite eosinofila / eosinofilia polmonare (dal grafo di conosce…"
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
---

# Mepolizumab
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **5** 
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

# Mepolizumab: Dalla polmonite eosinofila alla trombocitopenia da distruzione immunitaria

## Sintesi

Mepolizumab è un anticorpo monoclonale anti-IL-5, originariamente associato al trattamento della polmonite eosinofila e dell'eosinofilia polmonare. Il modello TxGNN ne predice una possibile efficacia nella **trombocitopenia da distruzione immunitaria**, ma l'evidenza è molto limitata: **nessuno studio clinico** e **1 pubblicazione** (un caso clinico) tra i dati compilati per questo report.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Polmonite eosinofila / eosinofilia polmonare (dal grafo di conoscenza; il testo dell'indicazione autorizzata non è disponibile) |
| Nuova indicazione predetta | Trombocitopenia da distruzione immunitaria |
| Punteggio di predizione TxGNN | 99,66% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 6 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione può essere plausibile?

I dati sul meccanismo d'azione non sono al momento disponibili nei dati compilati. Mepolizumab è tuttavia noto come anticorpo anti-IL-5 che deprime gli eosinofili.

Un legame plausibile esiste solo in un contesto ristretto: la sindrome ipereosinofila (HES) con citopenia immuno-mediata secondaria. In questo caso, controllare la disregolazione immunitaria guidata dagli eosinofili potrebbe ridurre indirettamente la distruzione piastrinica immuno-mediata.

Per la trombocitopenia immune primaria non esiste un meccanismo stabilito: la patogenesi è dominata da autoanticorpi contro le glicoproteine piastriniche e da disregolazione dei linfociti T, non dall'asse IL-5/eosinofili. L'elevatissimo punteggio TxGNN (0,997) è una predizione computazionale e non è supportato da dati clinici.

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Caso clinico | Blood Cells Mol Dis | Risoluzione di una diatesi immunitaria ipereosinofila resistente agli steroidi con mepolizumab e miglioramento concomitante di una microangiopatia trombotica mista (contesto di sindrome emolitico-uremica atipica) |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 044648057 | NUCALA siringa preriempita SC 100 mg 1 ml (1 pz) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 044648095 | NUCALA siringa preriempita SC 40 mg 0,4 ml (1 pz) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 044648069 | NUCALA siringhe preriempite SC 100 mg 1 ml (3 pz) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 044648032 | NUCALA penna preriempita SC 100 mg 1 ml (1 pz) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 044648044 | NUCALA penne preriempite SC 100 mg 1 ml (3 pz) | Non indicata | Non disponibile (autorizzazione cancellata) |

Titolare: GlaxoSmithKline Trading Services Ltd. Una sesta autorizzazione (044648018, flaconcino SC 100 mg) è anch'essa cancellata.

## Altre predizioni TxGNN (a titolo informativo)

Le altre indicazioni predette hanno punteggi altrettanto elevati ma evidenza ancora più debole, e per tutte la raccomandazione è Hold:

- **Disturbo primario del rilascio piastrinico** (99,61%, L4): solo una revisione generale sulla gestione della HES; nessun legame meccanicistico diretto.
- **Pseudo-malattia di von Willebrand** (99,44%, L5): nessuna evidenza; via patogenetica non correlata all'IL-5.
- **Trombocitopenia autoimmune** (99,33%, L5): probabile variante della ITP; nessuna evidenza.
- **Trombastenia di Glanzmann** (99,28%, L5): difetto ereditario dell'integrina αIIbβ3; nessun ruolo plausibile per l'inibizione di IL-5.

La vicinanza nel grafo di conoscenza tra disturbi piastrinici sembra spiegare questi punteggi più di una reale base biologica.

## Considerazioni sulla sicurezza

Non sono disponibili dati su avvertenze, controindicazioni o interazioni farmacologiche nei dati compilati. Si rimanda al foglio illustrativo per le informazioni di sicurezza.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa quasi esclusivamente sul modello computazionale: nessuno studio clinico e un solo caso clinico in un contesto di HES/microangiopatia trombotica, non di trombocitopenia immune primaria. Inoltre, tutte le autorizzazioni italiane risultano cancellate e mancano i dati di sicurezza.

**Per procedere sono necessari:**
- Recupero e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un limite bloccante per lo screening di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Verifica dello stato regolatorio attuale in Italia (le autorizzazioni elencate sono cancellate) e del testo delle indicazioni
- Evidenze cliniche aggiuntive, almeno in sottopopolazioni con HES e citopenia immuno-mediata concomitante
- Valutazione di compatibilità della via di somministrazione e della similarità con l'indicazione originale
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

