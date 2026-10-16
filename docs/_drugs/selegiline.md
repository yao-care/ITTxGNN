---
layout: default
title: Selegiline
parent: Prove moderate (L3-L4)
nav_order: 401
evidence_level: L3
indication_count: 4
last_modified_at: 2026-10-15
description: "Selegiline: nuova indicazione prevista, Schizofrenia (livello di evidenza L3). Indicazione originale: Malattia di Parkinson (e depressione, disturbi d'ansia…"
monitor_inn: "Selegiline"
predicted_indications: ["polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "schizophrenia", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies"]
---

# Selegiline
{: .fs-9 }

Livello di evidenza: **L3** | Indicazioni previste: **4** 
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

# Selegilina: dalla malattia di Parkinson alla schizofrenia

## Sintesi in una frase

La selegilina è un inibitore della monoamino ossidasi B (MAO-B), originariamente impiegato nel trattamento della malattia di Parkinson e della depressione.
Il modello TxGNN la indica come potenzialmente efficace per la **schizofrenia** (in particolare per i sintomi negativi), con **1 studio clinico registrato** e **20 pubblicazioni** recuperate, quasi tutte di livello preliminare o di revisione.

Nota: la prima previsione in graduatoria (polimicrogiria perisilviana con ipoplasia cerebellare e artrogriposi) non ha alcuna evidenza a supporto. Il report si concentra sulla seconda, la schizofrenia, perché è l'unica con evidenza clinica diretta.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Malattia di Parkinson (e depressione, disturbi d'ansia, secondo il grafo di conoscenza); il testo delle indicazioni approvate in Italia non è disponibile |
| Nuova indicazione prevista | Schizofrenia |
| Punteggio di predizione TxGNN | 99,14% |
| Livello di evidenza | L3 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 3 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (come ipotesi di ricerca) |

Altre previsioni del modello, tutte con evidenza debole o assente:

| Indicazione prevista | Punteggio TxGNN | Livello di evidenza | Decisione |
|------|------|------|------|
| Polimicrogiria perisilviana con ipoplasia cerebellare e artrogriposi | 99,15% | L5 | Hold |
| Disturbo congenito della glicosilazione con fucosilazione difettosa | 99,02% | L5 | Hold |
| Distrofia retinica con o senza anomalie extraoculari | 99,01% | L5 | Hold |

---

## Perché questa previsione è ragionevole?

Dai dati compilati per questo report non sono disponibili informazioni dettagliate sul meccanismo d'azione. Sulla base delle conoscenze note, la selegilina è un inibitore irreversibile e selettivo della MAO-B (a dosi orali ≥20 mg/die l'inibizione diventa non selettiva e coinvolge anche la MAO-A). Aumentando la disponibilità di dopamina, ha dimostrato efficacia nel Parkinson e ha proprietà antiossidanti.

I sintomi negativi e cognitivi della schizofrenia sono associati a una ridotta attività dopaminergica prefrontale, e lo stress ossidativo è coinvolto nella progressione della malattia. Per questo la selegilina è stata studiata come terapia aggiuntiva agli antipsicotici per i sintomi negativi. Il legame meccanicistico è quindi plausibile, ma resta ipotetico: la letteratura recuperata offre un segnale che genera ipotesi, non un beneficio confermato.

Per le altre tre previsioni non si individua un legame meccanicistico credibile: si tratta di malformazioni o difetti metabolici/strutturali su cui l'inibizione della MAO-B non ha un effetto noto.

---

## Evidenza dagli studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completato | 70 | Selegilina in aggiunta agli antipsicotici vs placebo per i sintomi negativi in pazienti ricoverati con schizofrenia cronica (randomizzato). I risultati non sono disponibili nei dati compilati |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Revisione sistematica/meta-analisi | Eur Neuropsychopharmacol | Efficacia e sicurezza della selegilina (orale e transdermica) in diversi disturbi psichiatrici |
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT | Am J Psychiatry | Studio multicentrico in doppio cieco controllato con placebo: selegilina aggiuntiva agli antipsicotici per i sintomi negativi in pazienti ambulatoriali |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Hum Psychopharmacol | Selegilina aggiunta a risperidone per i sintomi negativi, 8 settimane, doppio cieco |
| [10587287](https://pubmed.ncbi.nlm.nih.gov/10587287/) | 1999 | RCT | J Clin Psychopharmacol | Deprenyl aggiuntivo per i sintomi negativi in 16 pazienti clinicamente stabili, doppio cieco |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biol Psychiatry | Selegilina 10 mg/die vs placebo per la discinesia tardiva (33 pazienti, 6 settimane) |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | Studio pilota in aperto | J Nerv Ment Dis | Selegilina a basso dose (5 mg due volte al giorno) aggiuntiva per sintomi negativi in schizofrenia/disturbo schizoaffettivo |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Revisione | Ann Pharmacother | Ruolo della selegilina nei sintomi negativi della schizofrenia |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Revisione sistematica | Schizophr Res | Trattamento farmacologico dei sintomi negativi primari della schizofrenia |
| [26848926](https://pubmed.ncbi.nlm.nih.gov/26848926/) | 2016 | Revisione sistematica (Cochrane) | Cochrane Database Syst Rev | Trattamenti antiossidanti per la schizofrenia |
| [7901857](https://pubmed.ncbi.nlm.nih.gov/7901857/) | 1993 | Studio clinico | Pharmacopsychiatry | Selegilina per il parkinsonismo indotto da neurolettici |

Gli altri documenti recuperati riguardano temi adiacenti (disfunzione sessuale da antipsicotici, storia degli inibitori delle MAO, dipendenza da nicotina) e sono solo indirettamente rilevanti. Per la distrofia retinica esiste un'unica revisione del 2005 (PMID 16392036) sull'aggregazione proteica nelle cellule retiniche, che non testa la selegilina.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 025462021 | JUMEX*25 cpr 10 mg (Chiesi Italia) | Compresse | Non disponibile (autorizzazione cancellata) |
| 032010011 | SELECOM*50 cpr 5 mg (Fulton Medicinali) | Compresse | Non disponibile (autorizzazione cancellata) |
| 025462019 | JUMEX*50 cpr 5 mg (Chiesi Italia) | Compresse | Non disponibile (autorizzazione cancellata) |

Nessuna delle tre autorizzazioni è attualmente valida.

---

## Considerazioni sulla sicurezza

Il testo del foglio illustrativo AIFA con avvertenze e controindicazioni non è disponibile: si rimanda al foglio illustrativo per le informazioni di sicurezza complete.

- **Controindicazioni suggerite dal grafo di conoscenza** (non derivate dal testo del foglio illustrativo): atrofia multisistemica, ipotensione ortostatica, sindrome da tachicardia posturale ortostatica, malattia renale, malattia epatica, malattia della colecisti, disturbo bipolare e disturbi affettivi maggiori, disturbi psicotici (inclusi disturbi schizofreniformi e schizoaffettivi), feocromocitoma e paraganglioma simpatico, arresto cardiaco improvviso, malattie della conduzione cardiaca, melanoma, tumori (duodeno, intestino tenue, cuore, surrene), discinesia tardiva e discinesia linguo-facio-buccale. È rilevante che l'elenco comprenda i disturbi psicotici, cioè proprio l'area della nuova indicazione prevista: questo punto richiede una valutazione attenta.
- **Interazioni**: la selegilina agisce su MAO-A e MAO-B. Per le possibili interazioni da inibizione delle MAO si raccomandano cautele con farmaci serotoninergici e simpaticomimetici, oltre che con gli antipsicotici in associazione.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails** (solo come domanda di ricerca; per le altre tre previsioni: Hold)

**Motivazione:**
- Per la schizofrenia esistono un piccolo studio randomizzato completato (early Phase 1, n=70) e diversi RCT più datati sui sintomi negativi, oltre a una meta-analisi recente, ma i risultati non sono forniti nei dati compilati e non c'è conferma da studi di fase 2/3. L'evidenza è di livello L3: un segnale che genera ipotesi, non un beneficio dimostrato.
- Il punteggio TxGNN elevato (99%) è una predizione basata sul grafo e, da solo, non è sufficiente a giustificare un avanzamento.

**Per procedere sono necessari:**
- Recupero e analisi dei risultati di NCT00456976 e degli RCT già pubblicati (PMID 15677608, 17972359, 10587287), con una sintesi quantitativa dell'effetto sui sintomi negativi
- Testo del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e che blocca la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Piano di monitoraggio della sicurezza per le interazioni da inibizione delle MAO e per l'uso con antipsicotici, tenendo conto della controindicazione segnalata nel grafo per i disturbi psicotici
- Chiarimento dello stato regolatorio, dato che tutte le autorizzazioni italiane risultano cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

