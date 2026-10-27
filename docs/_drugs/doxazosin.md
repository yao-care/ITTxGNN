---
layout: default
title: Doxazosin
parent: Prove moderate (L3-L4)
nav_order: 152
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-15
description: "Doxazosin: nuova indicazione prevista, Disturbo emicranico (migraine disorder) (livello di evidenza L4). Indicazione originale: Ipertensione e iperplasia prostatica benigna"
monitor_inn: "Doxazosin"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Doxazosin
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **2** 
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

## Doxazosin: Dall'ipertensione e dall'iperplasia prostatica benigna all'emicrania
{: .text-alpha }

## Sintesi in una frase

Doxazosin è un antagonista selettivo dei recettori alfa-1 adrenergici, originariamente impiegato per il trattamento dell'ipertensione e dell'iperplasia prostatica benigna.
Il modello TxGNN prevede che possa essere efficace per il **disturbo emicranico (migraine disorder)**,
ma al momento l'evidenza si limita a **1 pubblicazione** di tipo narrativo e a **nessuno studio clinico registrato**.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione e iperplasia prostatica benigna (dal knowledge graph; i testi delle autorizzazioni AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Disturbo emicranico (migraine disorder) |
| Punteggio di predizione TxGNN | 99,20% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report. In base alle conoscenze generali sulla classe, doxazosin è un antagonista alfa-1 adrenergico; i dati di farmacologia compilati confermano l'interazione con i recettori α1A, α1B e α1D (geni ADRA1A, ADRA1B, ADRA1D). La sua efficacia nell'ipertensione e nei sintomi urinari da iperplasia prostatica benigna è nota.

Il possibile legame con l'emicrania passerebbe dalla modulazione del tono noradrenergico e della reattività vascolare cerebrale e simpatica, meccanismi coinvolti nella fisiopatologia dell'emicrania. Si tratta però di un'inferenza basata sulla classe farmacologica, non di un dato fornito direttamente.

È importante sottolineare che il punteggio TxGNN molto alto (0,992) è una predizione computazionale e non costituisce evidenza clinica. Anche il sottotipo **emicrania con aura del tronco encefalico** ha ottenuto un punteggio quasi identico (99,19%), ma senza alcuno studio o pubblicazione a supporto: il valore sembra ereditato dal nodo generale "emicrania" e non da un segnale specifico del sottotipo. Resta in livello L5 e con raccomandazione Hold.

---

## Evidenza dagli studi clinici

Attualmente non risulta alcuno studio clinico registrato correlato.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revisione narrativa | Headache | Discussione sul ruolo dei bloccanti alfa-1 nella profilassi dell'emicrania. In 10 pazienti trattati con terazosina o doxazosin, 9 hanno mostrato riduzione di frequenza e/o gravità degli attacchi, ma 5 hanno sospeso il farmaco per effetti collaterali. Non sono forniti dati controllati di efficacia. |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Di seguito le prime 5.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 034434187 | DOXAZOSINA 20 cpr 4 mg | EG SpA | Cancellata |
| 040243065 | DOXAZOSIN 30 cpr 2 mg | Aurobindo Pharma Italia Srl | Cancellata |
| 037248059 | KIMURA 30 cpr div 2 mg | S.F. Group Srl | Cancellata |
| 039353026 | CARDURA 30 cpr div 2 mg | BB Farma Srl | Cancellata |
| 037397015 | DOXAZOSIN 3x10 cpr 2 mg | DOC Generici Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni associate nel knowledge graph** (non derivate dal foglietto illustrativo): atrofia multisistemica, sindrome da tachicardia posturale ortostatica, ipotensione ortostatica, insufficienza epatica, malattie del fegato, malattie della colecisti, disturbi ipotensivi, stenosi del piloro, priapismo, sindrome dell'iride a bandiera intraoperatoria, ostruzione intestinale.
- **Interazioni**: la ricerca è stata completata e ha individuato 3 interazioni di tipo farmacologico, tutte con i recettori α1A, α1B e α1D (bersagli terapeutici del farmaco). Non sono state identificate interazioni con altri farmaci.
- **Nota sulla tollerabilità**: il blocco alfa-1 può causare ipotensione e capogiri, rilevanti in una popolazione con emicrania; nello studio del 1997, 5 pazienti su 10 hanno interrotto il trattamento per effetti collaterali. Per il sottotipo con aura del tronco encefalico gli effetti ipotensivi potrebbero essere particolarmente preoccupanti.

Per le avvertenze e le controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa su un punteggio computazionale elevato, ma l'unica evidenza è una revisione narrativa del 1997 con pochi pazienti e un alto tasso di interruzione per effetti collaterali. Non esistono studi clinici registrati. Inoltre, tutte le autorizzazioni italiane risultano cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Studi clinici controllati (idealmente RCT di fase 2) di doxazosin nella profilassi dell'emicrania
- Valutazione del profilo di tollerabilità (ipotensione, capogiri) in pazienti con emicrania
- Chiarimento dello stato regolatorio in Italia, visto che nessuna autorizzazione è valida
- Evidenza specifica per sottotipo prima di considerare l'emicrania con aura del tronco encefalico
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

