---
layout: default
title: Calcifediol
parent: Solo previsione del modello (L5)
nav_order: 83
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Calcifediol: nuova indicazione prevista, Carenza di vitamina D (termine obsoleto) (livello di evidenza L5). Indicazione originale: Ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo…"
monitor_inn: "calcifediol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "hereditary hypophosphatemic rickets", "vitamin D-dependent rickets"]
---

# Calcifediol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Calcifediol: Dalle indicazioni attuali alla carenza di vitamina D (predizione TxGNN)

## Riepilogo in una frase

Il calcifediolo (25-idrossivitamina D3) è un metabolita della vitamina D, usato per disturbi del metabolismo calcio-fosforo e delle ossa, come rachitismo, osteomalacia e ipofosfatemia.
Il modello TxGNN prevede che possa essere utile per la **carenza di vitamina D** (termine classificato come obsoleto nell'ontologia), ma per questa indicazione **non sono stati trovati studi clinici né pubblicazioni**.
L'evidenza è quindi limitata alla sola predizione del modello (livello L5).

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, ipofosfatemia, rachitismo, osteomalacia, osteodistrofia renale (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Carenza di vitamina D (termine obsoleto) |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione è ragionevole?

I dati disponibili non riportano un meccanismo d'azione dettagliato. In base alle informazioni note, il calcifediolo è il precursore circolante diretto del calcitriolo (forma attiva della vitamina D) e il principale marcatore dello stato vitaminico D. Dal punto di vista meccanicistico, la sua somministrazione nella carenza di vitamina D è quindi plausibile.

Va tuttavia considerato che il termine di malattia è contrassegnato come obsoleto: un eventuale uso reale richiederebbe la corrispondenza con il termine attuale di carenza di vitamina D, non supportata dai dati disponibili. Il punteggio molto alto potrebbe riflettere soprattutto la vicinanza nel grafo alle indicazioni già esistenti (rachitismo, osteomalacia, ipofosfatemia).

### Altre predizioni considerate

| Indicazione prevista | Punteggio TxGNN | Evidenza | Commento |
|------|------|------|------|
| Acidosi tubulare renale | 99,86% | L5 | Legame indiretto: il calcifediolo non corregge il difetto tubulare. Rischio di peggiorare ipercalciuria e ipercalcemia. Nessuno studio. |
| Rachitismo ipofosfatemico ereditario | 99,76% | L4 | Il calcifediolo dipende dalla 1α-idrossilazione renale, soppressa da FGF23, quindi è improbabile che funzioni in monoterapia; al massimo come supporto. Coerente con le indicazioni già esistenti. |
| Rachitismo vitamina D-dipendente | 99,18% | L4 | Razionale forte solo per il tipo 1B (carenza di 25-idrossilasi, CYP2R1), che il calcifediolo aggira. Non efficace nei tipi 1A e 2. |

## Evidenza da studi clinici

Attualmente non risultano studi clinici registrati correlati alla predizione principale (né alle altre predizioni).

## Evidenza dalla letteratura

Per la predizione principale (carenza di vitamina D) non è disponibile letteratura. Le pubblicazioni seguenti riguardano due predizioni secondarie.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Revisione | Nutrients | Tipi di rachitismo e trattamento con vitamina D e analoghi (rachitismo ipofosfatemico); evidenza indiretta |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Caso clinico/Revisione | Journal of Bone and Mineral Research | Rachitismo vitamina D-dipendente tipo 1B (deficit di 25-idrossilasi): condizione rara o sottodiagnosticata; sette pazienti di due famiglie |

## Informazioni sul mercato italiano

Tutte e 4 le autorizzazioni risultano cancellate; il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati.

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 024139014 | DIDROGYL gocce orali soluz. 1,5 mg 10 ml | Non riportata | Non riportata |
| 048177012 | VIDENKA gocce orali soluz. 0,15 mg/ml 10 ml | Non riportata | Non riportata |
| 045241041 | NEODIDRO 10 capsule molli 0,266 mg | Non riportata | Non riportata |
| 045241039 | NEODIDRO 5 capsule molli 0,266 mg | Non riportata | Non riportata |

## Considerazioni sulla sicurezza

- **Controindicazioni suggerite dal grafo di conoscenza** (relazioni farmaco-malattia del grafo TxGNN, non testo di scheda tecnica): malattia renale, piouretere, sarcoidosi, ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, nefrolitiasi (inclusa la suscettibilità legata a SLC26A1), nefropatia acuta da urati, iperfosfatemia, ipervitaminosi, arteriosclerosi obliterante.
- **Interazioni farmacologiche**: sono state rilevate 57 interazioni; tra le principali:
  - **Maggiori**: colecalciferolo, calcitriolo, burosumab.
  - **Moderate**: fosfenitoina, carbamazepina, barbiturici (amobarbital, butalbital, butabarbital), diuretici tiazidici (idroclorotiazide, bendroflumetiazide, benztiazide, clorotiazide, clortalidone), idrossido di alluminio, resine sequestranti degli acidi biliari (colestiramina, colesevelam, colestipolo), digitossina, calcipotriolo e calcitriolo topici.

Per avvertenze e controindicazioni della scheda tecnica, fare riferimento al foglio illustrativo, non disponibile nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold (sospendere)**

**Motivazione:**
La predizione principale si basa solo sul modello (L5), senza studi né letteratura, e riguarda un termine di malattia obsoleto. Inoltre, tutte le autorizzazioni italiane sono cancellate e mancano i dati di sicurezza da scheda tecnica. Tra le predizioni secondarie, il rachitismo vitamina D-dipendente tipo 1B ha il razionale meccanicistico più solido, ma è sostenuto solo da evidenza a livello di casi clinici (L4).

**Per procedere è necessario:**
- Scaricare e analizzare la scheda tecnica AIFA per avvertenze e controindicazioni (lacuna bloccante).
- Ottenere i dati sul meccanismo d'azione (ad esempio da DrugBank).
- Mappare il termine obsoleto di carenza di vitamina D al termine attuale dell'ontologia.
- Raccogliere evidenze cliniche (studi e letteratura) per la carenza di vitamina D e per il rachitismo vitamina D-dipendente tipo 1B.
- Valutare il rischio di ipercalcemia/ipercalciuria nelle popolazioni con acidosi tubulare renale o malattia renale.
- Chiarire la situazione regolatoria, dato che non esiste alcuna autorizzazione valida in Italia.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

