---
layout: default
title: Levetiracetam
parent: Solo previsione del modello (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Levetiracetam: nuova indicazione prevista, Stato epilettico (livello di evidenza L5). Indicazione originale: Epilessia parziale"
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["visual epilepsy", "startle epilepsy", "audiogenic seizures", "eating seizures", "thinking seizures", "micturation-induced seizures", "orgasm-induced seizures", "reading seizures", "status epilepticus", "beta-ketothiolase deficiency"]
---

# Levetiracetam
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

# Levetiracetam: Dall'epilessia parziale allo stato epilettico

## Sintesi in una frase

Il levetiracetam è un farmaco antiepilettico, originariamente impiegato per l'epilessia parziale. Il modello TxGNN lo indica come potenzialmente efficace per lo **stato epilettico** (indicazione con il supporto più solido tra le 10 previste), con **16 studi clinici** e **20 pubblicazioni** nei dati compilati per questa indicazione; tra gli studi, due di fase 3 completati e due RCT pubblicati su NEJM e Lancet.

> Nota: il rank 1 per punteggio TxGNN è "epilessia visiva" (visual epilepsy), ma l'evidenza è solo indiretta (L4, Hold). Questo report si concentra sull'indicazione con l'evidenza più robusta (stato epilettico, rank 9) e riassume le altre in una tabella comparativa.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Epilessia parziale (dal grafo di conoscenza; nelle licenze AIFA il testo dell'indicazione non è disponibile) |
| Nuova indicazione prevista | Stato epilettico (indicazione con l'evidenza più solida; rank 9 per punteggio TxGNN) |
| Punteggio di predizione TxGNN | 99,91% (per lo stato epilettico); 99,98% per l'epilessia visiva, rank 1 |
| Livello di evidenza | L1 (≥2 RCT di fase 3 completati) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; 0 valide) |
| Decisione raccomandata | Proceed with Guardrails (per lo stato epilettico) |

---

## Perché questa predizione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati. In base alla letteratura recuperata, il levetiracetam si lega alla proteina delle vescicole sinaptiche SV2A e modula il rilascio di neurotrasmettitori, riducendo l'iperecitabilità neuronale.

L'epilessia parziale e lo stato epilettico condividono la stessa base fisiopatologica: un'attività neuronale eccessiva e sincronizzata. Uno stato epilettico è una crisi prolungata o ripetuta senza recupero della coscienza; ridurre l'iperecitabilità tramite SV2A è quindi un razionale coerente per interromperlo, in particolare come farmaco di seconda linea dopo le benzodiazepine.

Va precisato che lo studio ESETT ha mostrato un'efficacia **comparabile** tra levetiracetam, fosfenitoina e valproato, non una superiorità. Inoltre l'uso in fase acuta rappresenta un'espansione rispetto all'indicazione originale.

---

## Evidenze dagli studi clinici (stato epilettico)

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Fase 3 | Completato | 478 | ESETT: fosfenitoina vs valproato vs levetiracetam nello stato epilettico refrattario alle benzodiazepine |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Fase 3 | Completato | 203 | Levetiracetam EV + clonazepam vs clonazepam da solo in ambito preospedaliero |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Fase 2 | Completato | 80 | Levetiracetam vs valproato nei bambini con stato epilettico refrattario |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Fase 2 | Completato | 144 | Levetiracetam + midazolam nello stato epilettico convulsivo generalizzato pediatrico |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Fase 2/3 | In reclutamento | 124 | Ketamina + levetiracetam vs levetiracetam in bambini con stato refrattario alle benzodiazepine |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Fase 4 | Completato | 62 | Levetiracetam vs fosfenitoina nello stato epilettico convulsivo (in aperto) |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | Non specificata | Completato | 138 | Levetiracetam vs acido valproico nello stato epilettico pediatrico |
| [NCT06067412](https://clinicaltrials.gov/study/NCT06067412) | Non specificata | Completato | 70 | Fenitoina vs levetiracetam nello stato epilettico pediatrico |
| [NCT07098728](https://clinicaltrials.gov/study/NCT07098728) | Non specificata | In reclutamento | 180 | Levetiracetam EV vs fenobarbital in crisi prolungate nei bambini |
| [NCT00362141](https://clinicaltrials.gov/study/NCT00362141) | Fase 2 | Sconosciuto | 12 | Sicurezza e tollerabilità del levetiracetam aggiuntivo nello stato epilettico |

---

## Evidenze dalla letteratura (stato epilettico)

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | N Engl J Med | Studio randomizzato di tre anticonvulsivanti nello stato epilettico refrattario alle benzodiazepine |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | RCT (analisi per età) | Lancet | ESETT: levetiracetam, fosfenitoina e valproato nello stato epilettico stabilizzato, per fascia d'età |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | RCT | Health Technol Assess | EcLiPSE: levetiracetam come alternativa alla fenitoina nei bambini con stato epilettico convulsivo |
| [35333156](https://pubmed.ncbi.nlm.nih.gov/35333156/) | 2022 | Revisione sistematica | Health Technol Assess | Sintesi delle evidenze sul trattamento preospedaliero e in pronto soccorso dello stato epilettico convulsivo negli adulti |
| [38580318](https://pubmed.ncbi.nlm.nih.gov/38580318/) | 2024 | Revisione | Semin Neurol | Aggiornamento sulla gestione farmacologica; fenitoina, valproato e levetiracetam hanno profili simili di efficacia e sicurezza |
| [38830068](https://pubmed.ncbi.nlm.nih.gov/38830068/) | 2024 | Revisione | Continuum | Panoramica della gestione emergente dello stato epilettico |
| [39626562](https://pubmed.ncbi.nlm.nih.gov/39626562/) | 2025 | Linee guida | Brain Dev | Linee guida giapponesi 2023 per lo stato epilettico pediatrico |
| [34659919](https://pubmed.ncbi.nlm.nih.gov/34659919/) | 2021 | Revisione | Cureus | Confronto fenitoina vs levetiracetam nel trattamento dello stato epilettico |

---

## Altre indicazioni previste

| Rank | Indicazione | Punteggio TxGNN | Evidenza | Raccomandazione | Nota |
|------|------|------|------|------|------|
| 1 | Epilessia visiva | 99,98% | L4 | Hold | Letteratura su crisi generali, non specifica |
| 2 | Epilessia da sussulto (startle) | 99,96% | L3 | Research Question | Piccole serie e casi clinici a favore, nessun RCT |
| 3 | Crisi audiogene | 99,96% | L3 | Research Question | Evidenza prevalentemente animale (incluso RCT veterinario nei gatti) |
| 4 | Crisi da alimentazione | 99,96% | L4 | Hold | Solo evidenza indiretta |
| 5 | Crisi da pensiero | 99,96% | L4 | Hold | Solo razionale antiepilettico generico |
| 6 | Crisi da minzione | 99,96% | L4 | Hold | Solo evidenza indiretta |
| 7 | Crisi da orgasmo | 99,96% | L5 | Hold | Nessuno studio |
| 8 | Crisi da lettura | 99,94% | L4 | Hold | Casi clinici; un caso con seletracetam, altro farmaco |
| 10 | Deficit di beta-chetotiolasi | 99,90% | L5 | Hold | Nessun legame meccanicistico; probabile artefatto di rete |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni AIFA risultano cancellate; il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati compilati. Elenco delle principali (5 su 20):

| Numero di autorizzazione | Nome del prodotto | Titolare | Indicazione approvata |
|---------|------|------|-----------|
| 035039229 | KEPPRA 30 cpr rivestite 1.000 mg | UCB PHARMA S.A. | Non disponibile |
| 051131011 | KEPPRA 30 cpr rivestite 1.000 mg | DIFARMED S.L.U. | Non disponibile |
| 041466119 | MATEVER 60 cpr rivestite 500 mg | PHARMATHEN S.A. | Non disponibile |
| 040273017 | ITALEPT 60 cpr rivestite 500 mg | SO.SE.PHARM Srl | Non disponibile |
| 045107024 | Levetiracetam soluzione orale 100 mg/ml | AUROBINDO PHARMA ITALIA Srl | Non disponibile |

---

## Considerazioni sulla sicurezza

**Controindicazioni e condizioni da valutare** (dal grafo di conoscenza, non dal foglietto illustrativo): disturbi d'ansia, disturbi nevrotici, disturbo distimico, malattie renali, malattie epatiche, malattie della colecisti, disturbi psicotici e schizoaffettivi, disturbi mentali, neutropenia, agranulocitosi, leucopenia, pancitopenia.

**Interazioni farmacologiche**: sono state identificate 100 interazioni. Quelle di livello **moderato** includono morfina (anche liposomiale), dronabinolo, nabilone, metoclopramide, oppio e sibutramina. Altre interazioni sono di livello non classificato (ad es. pantoprazolo, omeprazolo, metformina, glimepiride).

**Segnalazioni dalla letteratura**: iponatriemia, iperplasia gengivale, aggravamento delle crisi in alcuni pazienti ed effetti comportamentali/irritabilità.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo AIFA, non ancora acquisito.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails** (per lo stato epilettico)

**Motivazione:**
Due studi di fase 3 completati (ESETT, n=478; n=203) e RCT pubblicati su NEJM e Lancet sostengono il levetiracetam come opzione di seconda linea; lo studio mostra però efficacia comparabile e non superiorità. Le altre indicazioni previste restano in Hold o come questione di ricerca per carenza di evidenza diretta.

**Per procedere è necessario:**
- Verificare lo stato regolatorio in Italia: tutte le 20 autorizzazioni sono cancellate, incluso l'uso endovenoso
- Acquisire avvertenze e controindicazioni dal foglietto illustrativo AIFA (dato mancante e bloccante per lo screening di sicurezza)
- Acquisire i dati sul meccanismo d'azione da DrugBank
- Monitorare effetti avversi comportamentali e psichiatrici e adattare la dose in base alla funzione renale
- Per epilessia da sussulto e crisi audiogene: valutare studi clinici prospettici dedicati
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

