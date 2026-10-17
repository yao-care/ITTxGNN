---
layout: default
title: Metyrapone
parent: Solo previsione del modello (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metyrapone: nuova indicazione prevista, Ipertermia maligna da esercizio fisico (livello di evidenza L5). Indicazione originale: Non disponibile nei dati di autorizzazione AIFA (uso clinico noto da…"
monitor_inn: "metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
---

# Metyrapone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Metirapone: Dall'indicazione originale a "ipertermia maligna da esercizio fisico"

## Sintesi in una frase

Il metirapone è un inibitore della sintesi del cortisolo, usato in ambito endocrinologico (test diagnostico della funzione ipotalamo-ipofisaria e, occasionalmente, trattamento della sindrome di Cushing). Il modello TxGNN lo predice come potenzialmente efficace per l'**ipertermia maligna da esercizio fisico**, ma al momento **non risultano studi clinici né pubblicazioni** a sostegno di questa direzione: si tratta di una previsione basata solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati di autorizzazione AIFA (uso clinico noto da fonti farmacologiche: diagnostica della funzione ipotalamo-ipofisaria, sindrome di Cushing) |
| Nuova indicazione prevista | Ipertermia maligna da esercizio fisico |
| Punteggio di previsione TxGNN | 99,95% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 1 |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. Dai dati farmacologici compilati, il metirapone agisce sugli enzimi CYP11B1 (11-beta-idrossilasi) e CYP11B2, riducendo la sintesi del cortisolo surrenalico.

Tuttavia, **non esiste un legame meccanicistico noto** con la nuova indicazione. L'ipertermia maligna è legata soprattutto a varianti di RYR1/CACNA1S che alterano il rilascio di calcio nel muscolo scheletrico; l'inibizione della steroidogenesi surrenalica non è collegata a questa via. L'elevato punteggio TxGNN sembra un artefatto del grafo di conoscenza (vicinanza a malattie con vicini condivisi), non una motivazione farmacologica.

Lo stesso vale per le altre previsioni ad alto punteggio (suscettibilità all'ipertermia maligna, sindrome di King-Denborough, miopatia a nuclei centrali, miopatie multiminicore e centronucleari, ipertermia maligna da anestesia): tutte miopatie o condizioni correlate a RYR1, senza alcun supporto clinico o preclinico. Un'unica indicazione, la paralisi periodica familiare, presenta un segnale indiretto: uno studio fisiologico del 1971 ha usato il metirapone come sonda dell'attività surrenalica, senza valore terapeutico dimostrato. Anche per l'acidosi tubulare renale esiste solo un'ipotesi teorica legata ai precursori dei mineralcorticoidi.

## Evidenze da studi clinici

Attualmente non risulta alcuno studio clinico correlato registrato.

## Evidenze dalla letteratura

Per l'indicazione principale (ipertermia maligna da esercizio fisico) non risulta alcuna letteratura correlata.

A titolo informativo, per la previsione di rango 8 (paralisi periodica familiare) è disponibile un solo lavoro:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Studio meccanicistico/fisiologico | The Journal of Clinical Investigation | In un paziente di 19 anni con paralisi periodica iperkaliemica, la paralisi è stata indotta da cloruro di potassio, corticotropina e glucocorticoidi, ma non da mineralcorticoidi né da ACTH più metirapone. Evidenza solo indiretta, non terapeutica. |

## Informazioni sul mercato italiano

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 043094010 | CORMETO*50 cps molli 250 mg flacone (ESTEVE PHARMACEUTICALS SA) | Non indicata | Non indicata (autorizzazione cancellata) |

## Citotossicità

Il metirapone non è un farmaco antineoplastico citotossico; la sezione non si applica.

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza TxGNN, non da testo del foglio illustrativo)**: morbo di Addison, insufficienza surrenalica (primaria cronica e corticosurrenalica), ipoplasia surrenalica congenita (comprese le forme familiari e legate all'X), deficit familiare di glucocorticoidi, deficit parziale di CYP11A1, iperplasia surrenalica congenita.
- **Interazioni farmacologiche**: sono state identificate 12 voci; 10 interazioni di livello moderato (fonte DDInter) con estrogeni (etinilestradiolo, estradiolo, estrogeni coniugati, mestranolo, estrogeni esterificati, estrone solfato, comprese le formulazioni topiche) e con la ciproeptadina. Sono inoltre registrati i bersagli farmacologici CYP11B1 e CYP11B2.

Per avvertenze e precauzioni d'uso complete, consultare il foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione è supportata solo dal modello (L5), senza studi clinici né letteratura, e senza alcun razionale meccanicistico plausibile. Inoltre il prodotto autorizzato in Italia risulta cancellato.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione registrati e una valutazione meccanicistica che colleghi l'inibizione della CYP11B1 alla fisiopatologia dell'ipertermia maligna
- Dati preclinici (ad es. modelli RYR1) che giustifichino un'ipotesi terapeutica
- Foglio illustrativo AIFA con avvertenze e controindicazioni, per la valutazione di sicurezza
- Chiarimento dello stato regolatorio (autorizzazione cancellata) e delle vie di somministrazione disponibili
- Eventuale rivalutazione di indicazioni con segnale indiretto (ad es. paralisi periodica) solo dopo verifica del testo completo degli studi
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

