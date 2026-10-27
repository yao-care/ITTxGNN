---
layout: default
title: Lincomycin
parent: Solo previsione del modello (L5)
nav_order: 271
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Lincomycin: nuova indicazione prevista, Iperamilasemia (livello di evidenza L5). Indicazione originale: Infezioni da pneumococco…"
monitor_inn: "lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
---

# Lincomycin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

## Lincomicina: dalle infezioni batteriche all'iperamilasemia
{: .text-alpha }

## Sintesi in una frase

La lincomicina è un antibiotico lincosamidico, originariamente usato per le infezioni da pneumococco, stafilococco e streptococco.
Il modello TxGNN predice una possibile efficacia per l'**iperamilasemia**, ma questa indicazione si basa solo sulla previsione del modello: ci sono **0 studi clinici** e **0 pubblicazioni** a supporto.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni da pneumococco, stafilococco e streptococco (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Iperamilasemia |
| Punteggio di previsione TxGNN | 99,14% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (0 valide, 2 cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe (o non potrebbe) essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle conoscenze generali, la lincomicina è un antibiotico lincosamidico che inibisce la sintesi proteica batterica legandosi alla subunità ribosomiale 50S. Questo meccanismo è coerente con l'uso nelle infezioni batteriche.

L'iperamilasemia, invece, è un reperto di laboratorio associato a danno pancreatico o delle ghiandole salivari e ad altre cause. Nessun meccanismo antibatterico spiega plausibilmente un suo trattamento. Non emerge quindi alcun legame meccanicistico tra l'indicazione originale e quella prevista.

Il punteggio elevato (99,14%) riflette probabilmente schemi di connettività nel grafo di conoscenza, non una relazione biologica validata. Va inoltre considerato che alcuni antibiotici sono stati associati a pancreatite come evento avverso, per cui l'associazione potrebbe addirittura avere direzione opposta.

Altre due previsioni di pari livello (stesso punteggio circa 99%) sono prive di supporto: la sindrome da iperviscosità policlonale (99,14%) e l'analbuminemia congenita (99,06%). Anche per queste non esiste un legame meccanicistico plausibile né alcuno studio.

---

## Evidenze da studi clinici

Attualmente nessuno studio clinico correlato risulta registrato.

---

## Evidenze dalla letteratura

Attualmente nessuna pubblicazione correlata risulta disponibile.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Titolare |
|---------|------|------|-----------|------|
| 020601098 | LINCOCIN*1 flaconcino iniett 600 mg 2 ml | Non indicata | Cancellata | Pfizer Italia Srl |
| 020601023 | LINCOCIN*12 cps 500 mg | Non indicata | Cancellata | Pfizer Italia Srl |

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza, non da scheda tecnica)**: insufficienza epatica, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, colite, malattie dell'apparato digerente e malattie intestinali.
- **Interazioni farmacologiche**: individuate 21 interazioni.
  - Livello moderato: balsalazide, acido picosolfurico, attapulgite, caolino, eritromicina, etinilestradiolo.
  - Livello non classificato: clotrimazolo, cimetidina, morfina, metformina, omeprazolo, lattulosio, triamcinolone, simvastatina, ranitidina, warfarin, lidocaina, cetirizina, montelukast, salmeterolo.

Per avvertenze e controindicazioni ufficiali, fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione è basata esclusivamente sul modello (livello L5), senza studi clinici né pubblicazioni, e non esiste un legame meccanicistico plausibile con l'iperamilasemia. Inoltre, tutte le autorizzazioni italiane sono cancellate e le controindicazioni a carico dell'apparato digerente suggeriscono cautela.

**Per procedere sarebbero necessari:**
- Scheda tecnica AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione da DrugBank
- Studi preclinici o clinici che supportino un legame con l'iperamilasemia
- Valutazione del rischio che la lincomicina causi o peggiori danno pancreatico
- Chiarimento sulla possibilità di rimettere in commercio il prodotto in Italia, data la cancellazione delle autorizzazioni
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

