---
layout: default
title: Clonidine
parent: Solo previsione del modello (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clonidine: nuova indicazione prevista, Sindrome faciodigitogenitale (livello di evidenza L5). Indicazione originale: Ipertensione, glaucoma ad angolo aperto, ADHD (dal grafo di conoscenza"
monitor_inn: "Clonidine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "migraine disorder", "manic bipolar affective disorder"]
---

# Clonidine
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

## Clonidina: dall'ipertensione alla faciodigitogenital syndrome (sindrome di Aarskog-Scott)
{: .text-alpha }

## Sintesi

La clonidina è un agonista dei recettori alfa-2 adrenergici, originariamente impiegato per ipertensione, glaucoma ad angolo aperto e disturbo da deficit di attenzione e iperattività (ADHD).
Il modello TxGNN prevede come prima indicazione la **sindrome faciodigitogenitale**, ma per questa previsione **non esistono studi clinici né pubblicazioni**.
Tra le indicazioni predette, quella con le evidenze più solide è la **sindrome di Tourette** (2 studi clinici e 18 pubblicazioni, incluse linee guida europee e una network meta-analisi), che è anche la candidata più sensata per un'ulteriore valutazione.

> **Nota importante:** la previsione di rango 1 è, secondo l'analisi, probabilmente un artefatto del grafo di conoscenza. Per questo, oltre alla tabella sulla prima indicazione, il report approfondisce anche le indicazioni successive con evidenze reali.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, glaucoma ad angolo aperto, ADHD (dal grafo di conoscenza; i testi di indicazione AIFA non sono disponibili) |
| Nuova indicazione predetta (rango 1) | Sindrome faciodigitogenitale |
| Punteggio di predizione TxGNN | 99,999% |
| Livello di evidenza | L5 (solo predizione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 2 (entrambe revocate) |
| Decisione raccomandata | Hold (per la sindrome faciodigitogenitale) |

**Indicazioni predette alternative con evidenze:**

| Rango | Indicazione | Punteggio TxGNN | Livello di evidenza | Raccomandazione |
|---|---|---|---|---|
| 5 | Sindrome di Tourette | 99,98% | L3 | Proceed with Guardrails |
| 6 | Obesità | 99,91% | L3 | Domanda di ricerca |
| 9 | Emicrania | 99,81% | L3 | Domanda di ricerca |
| 10 | Disturbo bipolare maniacale | 99,76% | L3 | Domanda di ricerca |
| 2 | Disturbo specifico dello sviluppo | 99,99% | L4 | Hold |
| 4 | Tricotillomania | 99,99% | L5 | Hold |
| 3, 7, 8 | Fibroma condromixoide, ipervitaminosi, sindrome da microdelezione 16p11.2 prossimale | 99,7–99,9% | L5 | Hold |

---

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle informazioni note, la clonidina è un agonista alfa-2 adrenergico che riduce il tono noradrenergico centrale; la sua efficacia nell'ipertensione è consolidata e, dal punto di vista meccanicistico, può essere applicabile a condizioni con iperattività noradrenergica.

Per la **sindrome faciodigitogenitale** (sindrome di Aarskog-Scott), un raro disturbo legato all'X causato da mutazioni di FGD1, non è stato identificato alcun legame meccanicistico plausibile con la modulazione alfa-2 adrenergica. La previsione sembra guidata da associazioni a livello di grafo (ad esempio fenotipi comportamentali simili all'ADHD) e non da evidenze biologiche.

Per la **sindrome di Tourette**, il razionale è invece solido: l'agonismo alfa-2 riduce il tono noradrenergico e modula i circuiti cortico-striato-talamo-corticali implicati nella genesi dei tic. La clonidina è utile anche per ADHD, impulsività e aggressività in comorbidità.

---

## Evidenze da studi clinici

Per la sindrome faciodigitogenitale: **al momento non risultano studi clinici registrati correlati.**

Per completezza, gli studi relativi alla sindrome di Tourette (rango 5):

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Fase 4 | Sconosciuto | 32 | Verifica se il trattamento notturno con clonidina riduce l'aggressività diurna in bambini con Tourette e ADHD |
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Fase 4 | Completato | 12 | Confronto tra levetiracetam e clonidina nei tic in bambini con Tourette; risultati non disponibili |

---

## Evidenze dalla letteratura

Per la sindrome faciodigitogenitale: **al momento non risulta letteratura correlata.**

Pubblicazioni più rilevanti per la sindrome di Tourette (rango 5):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network meta-analisi | Lancet Child & Adolescent Health | Confronto di efficacia, tollerabilità e accettabilità dei farmaci per la sindrome di Tourette in età pediatrica e giovanile |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Linee guida | European Child & Adolescent Psychiatry | Linee guida europee v2.0 sul trattamento farmacologico di Tourette e disturbi da tic |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Studio clinico | Psychiatry Investigation | Efficacia e sicurezza del cerotto di clonidina in Tourette con ADHD |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Revisione sistematica | Neurology | Trattamento dei tic nella sindrome di Tourette e nei disturbi cronici da tic |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Revisione sistematica | Journal of Psychopharmacology | Qualità delle evidenze sui trattamenti farmacologici per la sindrome di Tourette |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Revisione sistematica | J Child Psychol Psychiatry | Trattamenti per Tourette in bambini e giovani |
| [40392363](https://pubmed.ncbi.nlm.nih.gov/40392363/) | 2025 | Preclinico (ratto) | J Neuroimmune Pharmacology | La clonidina riduce la neuroinfiammazione in un modello di Tourette nel ratto |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Report clinico | Lancet | Piccole dosi di clonidina migliorano alcuni bambini non responsivi all'aloperidolo |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 027393026 | CATAPRESAN TTS2 – 2 cerotti transdermici 5 mg (revocata) | Cerotto transdermico | Non disponibile |
| 027393014 | CATAPRESAN TTS1 – 2 cerotti transdermici 2,5 mg (revocata) | Cerotto transdermico | Non disponibile |

Entrambe le autorizzazioni, intestate a Lavipharm Pharm. Products S.A., risultano revocate: non vi sono attualmente prodotti validi a base di clonidina nei dati compilati.

---

## Considerazioni sulla sicurezza

**Controindicazioni derivate dal grafo di conoscenza** (non provengono dal foglietto illustrativo): il grafo associa alla clonidina controindicazioni con numerose condizioni, tra cui:
- Cardiovascolari: infarto miocardico, ischemia miocardica, trombosi coronarica, arresto cardiaco improvviso, disturbi della conduzione cardiaca, ipotensione
- Metaboliche: diabete di tipo 1 e 2, chetoacidosi diabetica, gotta, ipercalcemia, carenza di potassio, disturbi del metabolismo del fosforo
- Altre: insufficienza epatica, insufficienza respiratoria, anuria, pancreatite, lupus eritematoso sistemico, disturbi della coagulazione, emoglobinopatie, dermatite, disturbi d'ansia e nevrotici, distimia

**Interazioni farmacologiche / profilo farmacologico:** la clonidina si lega ai recettori alfa-1D e ai recettori alfa-2A, 2B e 2C; sono segnalate interazioni anche con i canali HCN1, HCN2 e HCN4 (dati murini) e con il trasportatore di cationi organici 1 (OCT1/SLC22A1). Non sono disponibili interazioni con altri farmaci classificate per livello di gravità.

**Precauzioni emerse dalla valutazione (Tourette):** monitorare ipotensione, bradicardia e sedazione; evitare la sospensione brusca (rischio di ipertensione di rimbalzo).

Per le avvertenze e le controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold** (per la sindrome faciodigitogenitale, previsione di rango 1)

**Motivazione:**
- Nonostante il punteggio molto alto, la previsione non è supportata da studi, letteratura né razionale meccanicistico, ed è con ogni probabilità un artefatto del grafo.
- Tra le alternative, la **sindrome di Tourette** (Proceed with Guardrails, L3) è la più promettente: la clonidina è già inclusa in linee guida europee e in una network meta-analisi, anche se gli studi clinici identificati sono piccoli e di fase 4, senza dati di fase 3. Obesità, emicrania e mania restano a livello di domande di ricerca, con evidenze indirette o limitate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (dato mancante che impedisce lo screening di sicurezza)
- Conferma delle dimensioni dell'effetto dalla meta-analisi e dalle linee guida per la sindrome di Tourette
- Chiarimento della situazione regolatoria: oggi in Italia sono presenti solo autorizzazioni revocate
- Piano di monitoraggio di sicurezza (pressione arteriosa, frequenza cardiaca, sedazione, sospensione graduale), considerando le numerose controindicazioni cardiovascolari e metaboliche segnalate dal grafo
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

