---
layout: default
title: Prasugrel
parent: Solo previsione del modello (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: dalla sindrome coronarica acuta all'ipertensione polmonare

## Sintesi in una frase

Prasugrel è un inibitore del P2Y12 tienopiridinico utilizzato per la prevenzione degli eventi cardiovascolari trombotici nei pazienti con sindrome coronarica acuta (ACS) sottoposti a intervento coronarico percutaneo (ICP).
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione polmonare**, con un punteggio di previsione del 99.88%.
Tuttavia, **nessuno studio clinico o pubblicazione direttamente rilevante** a supporto di questa specifica indicazione è stato identificato — tutti gli studi recuperati sono stati valutati come non contributivi a causa di una mancata corrispondenza delle parole chiave, posizionando questo a un **livello di evidenza L5 (sola previsione del modello)**.

---

## Panoramica rapida

| Elemento | Contenuto |
|---------|----------|
| Indicazione Originale | Sindrome coronarica acuta (ACS) / Intervento coronarico percutaneo (ICP) — prevenzione degli eventi trombotici |
| Indicazione Nuova Prevista | Ipertensione polmonare |
| Punteggio di Previsione TxGNN | 99.88% |
| Livello di Evidenza | L5 |
| Stato del Mercato in Italia | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In sospeso |

---

## Perché questa previsione è ragionevole?

Prasugrel è un tienopiridinico di terza generazione che inibisce irreversibilmente il recettore P2Y12 dell'ADP piastrinico, bloccando l'attivazione e l'aggregazione piastrinica. È un profarmaco che raggiunge effetti antiaggreganti più rapidi e coerenti rispetto al clopidogrel, grazie a una conversione epatica più efficiente al suo metabolita attivo. Il suo ruolo consolidato è nella prevenzione della trombosi arteriosa dopo l'impianto di stent coronarico.

Il ponte meccanicistico verso l'ipertensione arteriosa polmonare (PAH) si basa sull'osservazione che le piastrine attivate sono importanti contributori della fisiopatologia della PAH. Nella PAH, le piastrine rilasciano trombossano A2 (TXA2), serotonina e fattore di crescita derivato dalle piastrine (PDGF) nella circolazione polmonare — tutti fattori che determinano vasocostrizione e rimodellamento vascolare polmonare. L'inibizione del P2Y12 potrebbe teoricamente ridurre questi segnali derivati dalle piastrine e attenuare il danno vascolare progressivo.

Tuttavia, questo rimane **una mera inferenza meccanicistica indiretta**. La farmacologia nota di prasugrel riguarda la trombosi arteriosa, non il rimodellamento vascolare polmonare, e nessuno studio preclinico o clinico è stato identificato che testi direttamente questa ipotesi. L'elevato punteggio TxGNN probabilmente riflette vicinanze condivise nella rete del grafo di conoscenza (ad esempio, trombosi, biologia piastrinica) piuttosto che un'efficacia validata empiricamente nella PAH. Questa previsione è meglio considerata come un segnale generatore di ipotesi, non come evidenza clinica attuabile.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato registrato.

> **Nota sulla qualità dei dati:** Due studi sono stati recuperati durante la ricerca di evidenze ma sono stati valutati come non contributivi (Grado di Rilevanza C):
> - **[NCT03993119](https://clinicaltrials.gov/study/NCT03993119)**: Uno studio osservazionale spagnolo sull'uso di NOAC in pazienti anziani con fibrillazione atriale non valvolare — valuta rivaroxaban/apixaban, non prasugrel, in una malattia completamente diversa.
> - **[NCT04846556](https://clinicaltrials.gov/study/NCT04846556)**: Uno studio retrospettivo su apixaban nel tromboembolismo venoso associato al cancro — nessuna intersezione con prasugrel o ipertensione polmonare.
>
> Entrambi i risultati sono il risultato di artefatti di corrispondenza incrociata delle parole chiave del database e non contribuiscono a questa valutazione di riutilizzo.

---

## Evidenza da Letteratura

Attualmente nessuna letteratura correlata che supporti direttamente l'uso di prasugrel nell'ipertensione polmonare.

> **Nota sulla qualità dei dati:** Due pubblicazioni sono state recuperate ma non sono rilevanti per questa indicazione:
> - **[PMID 34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/)** (Kardiologiia, 2021): Registro di comorbilità COVID-19 che esamina l'impatto della terapia cardiovascolare di base sui risultati di COVID-19 — prasugrel non è specificamente studiato, e lo scopo è completamente non correlato alla PAH.
> - **[PMID 21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/)** (Curr Med Res Opin, 2011): Coorte retrospettiva sull'aderenza al clopidogrel post-ICP nell'ACS — prasugrel è menzionato solo come comparatore di trattamento nel contesto dell'ACS, senza alcun riferimento all'ipertensione polmonare.

---

## Informazioni sul Mercato Italiano

Prasugrel attualmente non ha autorizzazioni di commercializzazione approvate in Italia. Il farmaco non è commercializzato e nessuna licenza di prodotto è registrata.

> **Contesto:** Prasugrel (marchio commerciale Efient®) è approvato dall'EMA e commercializzato in molteplici paesi dell'UE per le indicazioni ACS/ICP. L'assenza di dati di registrazione specifici per l'Italia in questo Evidence Pack potrebbe riflettere una lacuna nei dati piuttosto che una vera indisponibilità. È consigliata una verifica indipendente tramite il database ufficiale dell'AIFA.

---

## Considerazioni di Sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

> **Nota:** I dati formali di sicurezza (avvertimenti chiave, controindicazioni e interazioni farmaco-farmaco) non erano disponibili dalle fonti di dati attuali. In base alla classe farmacologica di prasugrel (inibitore irreversibile del P2Y12), le seguenti avvertenze generali sono ben consolidate nella letteratura e dovrebbero essere verificate rispetto al foglio illustrativo completo:
> - **Il rischio di sanguinamento** è la preoccupazione principale — prasugrel ha un avvertimento in scatola nera per sanguinamento serio e fatale nella sua etichettatura FDA/EMA.
> - **Controindicato** nei pazienti con precedente ictus o TIA (danno netto stabilito nello studio TRITON-TIMI 38).
> - **Non consigliato** nei pazienti ≥75 anni o <60 kg senza una valutazione attenta del beneficio-rischio.

---

## Conclusioni e Prossimi Passi

**Decisione: In sospeso**

**Razionale:**
Nonostante un elevato punteggio di previsione TxGNN (99.88%), il collegamento meccanicistico tra l'inibizione del P2Y12 e l'ipertensione polmonare è speculativo e indiretto. Nessuno studio clinico o letteratura a supporto è stato identificato, risultando in un livello di evidenza L5 che non giustifica l'avanzamento senza dati preclinici fondamentali.

**Per procedere, è necessario quanto segue:**
- **Studi preclinici**: Esperimenti in vitro o su modelli animali per testare se l'inibizione del P2Y12 riduce il rimodellamento vascolare polmonare o la pressione ventricolare destra nei modelli PAH (ad esempio, monocrotalina o PAH indotta da ipossia nei roditori)
- **Validazione meccanicistica**: Evidenza che TXA2 derivato dalle piastrine, serotonina, o PDGF siano significativamente soppressi dall'inibizione del P2Y12 nel contesto della circolazione polmonare
- **Revisione di sicurezza**: Analisi completa del foglio illustrativo per il rischio di sanguinamento e il profilo di controindicazione — essenziale prima di qualsiasi progettazione dello studio sulla popolazione PAH
- **Esplorazione dei biomarcatori**: Investigazione dei marcatori di attivazione piastrinica nelle coorti PAH per identificare una popolazione di pazienti che molto probabilmente trarrà beneficio
- **Confronto con le terapie PAH esistenti**: Posizionare il meccanismo potenziale di prasugrel rispetto agli agenti PAH approvati (inibitori PDE5, ERA, analoghi delle prostacicline) per valutare se la terapia antiaggregante offre un valore additivo

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

