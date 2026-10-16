---
layout: default
title: Ruxolitinib
parent: Solo previsione del modello (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ruxolitinib: nuova indicazione prevista, Tumore a cellule epitelioidi perivascolari del corpo uterino (livello di evidenza L5). Indicazione originale: Neoplasie mieloproliferative (policitemia vera, …"
---

# Ruxolitinib
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

# Ruxolitinib: Dalle neoplasie mieloproliferative alla sindrome emofagocitica associata a infezione

## Sintesi in una frase

Il ruxolitinib è un inibitore di JAK1/2 impiegato originariamente nelle neoplasie mieloproliferative (policitemia vera, mielofibrosi primaria e condizioni correlate). Il modello TxGNN lo propone per diverse nuove indicazioni; la più solida sul piano delle evidenze è la **sindrome emofagocitica associata a infezione** (emofagocitosi linfoistiocitica, HLH), sostenuta da **19 pubblicazioni** e nessuno studio clinico registrato. La prima indicazione per punteggio TxGNN è invece il **tumore a cellule epitelioidi perivascolari (PEComa) del corpo uterino**, privo di qualsiasi evidenza.

---

## Quadro generale

Nota metodologica: il modello ordina le predizioni in base al punteggio TxGNN. La prima in graduatoria (PEComa uterino) non ha alcuna evidenza a supporto, quindi la tabella riporta anche la predizione con le evidenze più ampie (HLH associata a infezione), che è quella analizzata in dettaglio nelle sezioni seguenti.

| Voce | Contenuto |
|------|------|
| Indicazione originale | Neoplasie mieloproliferative (policitemia vera, mielofibrosi primaria, mielofibrosi); il testo delle indicazioni autorizzate AIFA non è disponibile |
| Nuova indicazione prevista (prima in graduatoria) | Tumore a cellule epitelioidi perivascolari del corpo uterino |
| Punteggio TxGNN (prima in graduatoria) | 99,73% |
| Livello di evidenza (prima in graduatoria) | L5 |
| Nuova indicazione con più evidenze | Sindrome emofagocitica associata a infezione (punteggio TxGNN 99,32%) |
| Livello di evidenza (HLH associata a infezione) | L3 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (entrambe cancellate) |
| Decisione raccomandata | Hold per la prima in graduatoria; Proceed with Guardrails (come domanda di ricerca) per HLH associata a infezione |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. Sulla base delle conoscenze note, il ruxolitinib è un inibitore di JAK1/2, la sua efficacia nelle neoplasie mieloproliferative è dimostrata e, sul piano meccanicistico, potrebbe essere applicabile a condizioni guidate da segnali citochinici.

**HLH associata a infezione.** L'HLH è uno stato iperinfiammatorio guidato da citochine, in particolare l'interferone-gamma, che agisce attraverso la via JAK/STAT. Il blocco di JAK1/2 attenua questi segnali. Il razionale è supportato da due studi meccanicistici: uno in modelli murini di HLH (PMID 31015190) e uno che mostra come l'inibizione di JAK/STAT sensibilizzi i linfociti T CD8 all'apoptosi indotta dal desametasone (PMID 32530039).

**Liposarcoma.** Due studi preclinici indicano che la via JAK-STAT controlla le proprietà staminali tumorali e la chemioresistenza nel liposarcoma mixoide. Il razionale è plausibile ma indiretto, e non è confermato che il ruxolitinib sia stato testato.

**PEComa, linfangioleiomiomatosi e altre.** Queste patologie sono tipicamente guidate dall'attivazione della via mTOR (TSC1/TSC2). Nei dati forniti non è documentato un razionale per l'inibizione di JAK/STAT: la predizione è puramente computazionale.

---

## Evidenze da studi clinici

Al momento non risulta alcuno studio clinico registrato correlato.

---

## Evidenze dalla letteratura

Le evidenze si riferiscono a **HLH associata a infezione** (selezione delle pubblicazioni più rilevanti). Il tipo di studio è stato desunto dai titoli e va verificato sui testi completi.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Studio clinico (trattamento stratificato, pediatrico) | Blood | Ruxolitinib come farmaco di prima linea nell'HLH pediatrica, con trattamento stratificato in base alla risposta precoce |
| [33523540](https://pubmed.ncbi.nlm.nih.gov/33523540/) | 2021 | Serie di casi | Eur J Haematol | Ruxolitinib come terapia aggiuntiva nell'HLH secondaria |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Studio retrospettivo | Br J Haematol | Efficacia e sicurezza di un regime a base di ruxolitinib (n=53) vs HLH-94 modificato (n=42) nell'HLH pediatrica da EBV |
| [31879790](https://pubmed.ncbi.nlm.nih.gov/31879790/) | 2020 | Studio clinico | Ann Hematol | Ruxolitinib per GVHD acuta steroido-refrattaria in 12 pazienti con EBV-HLH sottoposti ad allo-HSCT |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Analisi di uso compassionevole | Ann Hematol | Sintilimab più ruxolitinib in 12 adulti con HLH associata a EBV |
| [41934358](https://pubmed.ncbi.nlm.nih.gov/41934358/) | 2026 | Indagine retrospettiva nazionale | Pediatr Hematol Oncol | Uso di ruxolitinib in 17 bambini giapponesi con HLH |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Caso clinico | J Pediatr Hematol Oncol | Emapalumab con ruxolitinib e desametasone in EBV-HLH con danno multiorgano |
| [36263041](https://pubmed.ncbi.nlm.nih.gov/36263041/) | 2022 | Caso clinico | Front Immunol | Ruxolitinib di prima linea per HLH secondaria in pazienti con AIDS |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Preclinico (modelli murini) | Blood | Meccanismi d'azione del ruxolitinib nei modelli murini di HLH |
| [32530039](https://pubmed.ncbi.nlm.nih.gov/32530039/) | 2020 | Preclinico/meccanicistico | Blood | L'inibizione di JAK/STAT sensibilizza i linfociti T CD8 all'apoptosi indotta dal desametasone |

Per il liposarcoma sono disponibili due studi preclinici (PMID [35186752](https://pubmed.ncbi.nlm.nih.gov/35186752/), 2022, e [30650179](https://pubmed.ncbi.nlm.nih.gov/30650179/), 2019) sul ruolo della via JAK-STAT nel liposarcoma mixoide.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 050666027 | OPZELURA crema derm 1 tubo 100 g 15 mg/g (Incyte Biosciences Distrib BV) | Crema (uso dermatologico) | Non disponibile; autorizzazione cancellata |
| 050666015 | OPZELURA crema derm 1 tubo 100 g 15 mg/g (Incyte Biosciences Distrib BV) | Crema (uso dermatologico) | Non disponibile; autorizzazione cancellata |

---

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Terapia mirata (inibitore di JAK1/2), non citotossico convenzionale |
| Rischio di mielosoppressione | Si rimanda alle avvertenze e precauzioni del foglietto illustrativo |
| Classificazione emetogena | Si rimanda alle avvertenze e precauzioni del foglietto illustrativo |
| Parametri da monitorare | Emocromo completo; funzionalità epatica e renale (si rimanda al foglietto illustrativo) |
| Protezione nella manipolazione | Si rimanda alle avvertenze e precauzioni del foglietto illustrativo |

---

## Considerazioni sulla sicurezza

**Interazioni farmacologiche** (100 interazioni totali rilevate; di seguito le principali):

- **Maggiori**: claritromicina, cobicistat, deferasirox, deferiprone, ibritumomab tiuxetan, tositumomab, tositumomab (I-131), samario (153Sm) lexidronam
- **Moderate**: desametasone, rosuvastatina, dexfenfluramina, fenfluramina, sibutramina, troglitazone, palifermina, cloruro di stronzio Sr-89
- **Minori**: aprepitant, cimetidina, miconazolo, clotrimazolo

Per avvertenze e controindicazioni si rimanda al foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold per la predizione con punteggio più alto (PEComa uterino); Proceed with Guardrails, come domanda di ricerca, per l'HLH associata a infezione**

**Motivazione:**
- La predizione di punteggio più alto (PEComa uterino, L5) è priva di studi e di razionale meccanicistico, e la patologia è guidata da mTOR. Per l'HLH associata a infezione esistono invece evidenze cliniche precoci (serie di casi, studi retrospettivi e uno studio pediatrico stratificato), accompagnate da un solido razionale meccanicistico (livello L3). Si tratta tuttavia di studi non randomizzati.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Verifica dei disegni di studio sui testi completi delle pubblicazioni
- Studi clinici prospettivi o randomizzati nell'HLH
- Valutazione dello stato regolatorio: le uniche autorizzazioni italiane sono per una crema topica, cancellate; occorre chiarire la compatibilità della via di somministrazione sistemica
- Per liposarcoma e altre predizioni: studi che testino direttamente il ruxolitinib
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

