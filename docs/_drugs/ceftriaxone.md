---
layout: default
title: Ceftriaxone
parent: Solo previsione del modello (L5)
nav_order: 98
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Ceftriaxone: nuova indicazione prevista, Sindrome da iperviscosità policlonale (livello di evidenza L5). Indicazione originale: Infezioni batteriche (infezione streptococcica, polmonite batterica…"
monitor_inn: "CEFTRIAXONE"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
---

# Ceftriaxone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **7** 
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

# Ceftriaxone: dalle infezioni batteriche alla sindrome da iperviscosità policlonale

## Riepilogo in breve

Il ceftriaxone è una cefalosporina di terza generazione, utilizzata per infezioni batteriche come polmonite, meningite, gonorrea e salmonellosi. Il modello TxGNN lo associa con punteggio molto alto alla **sindrome da iperviscosità policlonale**, ma **non esistono studi clinici né pubblicazioni** a sostegno di questa direzione. La previsione appare quindi priva di plausibilità biologica e più probabilmente frutto di un artefatto del grafo di conoscenza.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (infezione streptococcica, polmonite batterica, meningite batterica, gonorrea, salmonellosi, artrite batterica e altre). Fonte: grafo di conoscenza, non il foglio illustrativo, perché i testi delle indicazioni autorizzate non sono disponibili |
| Nuova indicazione prevista | Sindrome da iperviscosità policlonale |
| Punteggio di previsione TxGNN | 99,39% |
| Livello di evidenza | L5 (solo previsione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è (poco) ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Il ceftriaxone è una cefalosporina di terza generazione che inibisce la sintesi della parete cellulare batterica. La sua efficacia nelle infezioni batteriche è consolidata.

La sindrome da iperviscosità policlonale, invece, è causata da un eccesso di immunoglobuline e non ha alcun bersaglio antibatterico. Non è identificabile un legame meccanicistico con l'indicazione originale. L'alto punteggio del modello riflette probabilmente associazioni statistiche nel grafo di conoscenza, non una logica biologica.

## Evidenze da studi clinici

Attualmente nessuno studio clinico correlato risulta registrato.

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate e nessuna è attualmente valida. I testi delle indicazioni autorizzate e le forme farmaceutiche non sono riportati nei dati compilati. Le principali autorizzazioni:

| N. autorizzazione | Prodotto | Titolare | Stato |
|---------|------|------|------|
| 035869039 | Ceftriaxone 1 g IM + solvente 3,5 ml | EG SpA | Cancellata |
| 025202058 | Rocefin 1 g IM + solvente 3,5 ml | Roche SpA | Cancellata |
| 025202019 | Rocefin 250 mg IM + solvente 2 ml | Roche SpA | Cancellata |
| 036138028 | Ceftriaxone 1 g IM + solvente 3,5 ml | Eugia Pharma (Malta) Limited | Cancellata |
| 035952023 | Pantoxon 1 g IM + solvente 3,5 ml | Aesculapius Farmaceutici Srl | Cancellata |

## Considerazioni sulla sicurezza

I dati sulle avvertenze e sulle controindicazioni del foglio illustrativo non sono disponibili.

- **Controindicazioni segnalate dal grafo di conoscenza** (non da testo di etichetta): malattie epatiche, malattie della colecisti, ittero neonatale, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, anemia emolitica.
- **Interazioni farmacologiche** (100 interazioni totali; riportate le principali):
  - **Maggiori**: cloruro di calcio, glucoeptonato di calcio, gluconato di calcio.
  - **Moderate**: kanamicina, neomicina, streptomicina, acido picosolfurico.
  - Per molte altre interazioni il livello di gravità non è determinato.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per la sindrome da iperviscosità policlonale non esistono studi clinici né letteratura, e manca un legame meccanicistico plausibile. Il livello di evidenza è L5. Inoltre, tutte le autorizzazioni italiane risultano cancellate.

**Per procedere sarebbero necessari:**
- Una revisione critica della previsione, per verificare se sia un artefatto del grafo.
- I dati sul meccanismo d'azione e sulle avvertenze e controindicazioni del foglio illustrativo AIFA.
- Una rivalutazione delle previsioni alternative con maggiore plausibilità, in particolare l'otite media infettiva e l'otite media suppurativa (evidenza L3). Il loro uso è però già clinicamente consolidato e quindi poco innovativo come riposizionamento.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

