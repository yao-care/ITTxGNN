---
layout: default
title: Metoclopramide
parent: Solo previsione del modello (L5)
nav_order: 294
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "METOCLOPRAMIDE"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
description: "Metoclopramide: nuova indicazione prevista, Gastroduodenitis (livello di evidenza L5). In Italia, confezioni AIFA: 2 (autorizzate: 2)"
---

# Metoclopramide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

## Metoclopramide: Gastroduodenitis
{: .text-alpha }

## Sintesi

Il modello TxGNN ne prevede un possibile impiego nell'**ulcera gastrica**, ma i dati compilati mostrano soltanto **1 studio clinico** (uso procedurale, non terapeutico) e una letteratura composta soprattutto da rassegne datate. Il supporto è quindi molto debole.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Gastroduodenitis |
| Punteggio di predizione TxGNN | 0.9990 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è plausibile?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Metoclopramide (traduzione non ufficiale): «La metoclopramide stimola la motilità del tratto gastrointestinale superiore senza stimolare le secrezioni gastriche, biliari o pancreatiche. L'esatto meccanismo d'azione della metoclopramide nel trattamento del reflusso gastroesofageo e della gastroparesi diabetica acuta e ricorrente non è stato completamente stabilito.» Testo originale in inglese: "Metoclopramide stimulates motility of the upper gastrointestinal tract without stimulating gastric, biliary, or pancreatic secretions. The exact mechanism of action of metoclopramide in the treatment of gastroesophageal reflux and acute and recurrent diabetic gastroparesis has not been fully established." ([DailyMed: Reglan (metoclopramide hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de55c133-eb08-4a35-91a2-5dc093027397), versione del 2026-02-09; consultato il 2026-11-19). Dalla letteratura raccolta, la metoclopramide è un antagonista del recettore D2 e agonista 5-HT4 che accelera lo svuotamento gastrico e stimola la motilità del tratto gastrointestinale superiore.

Il legame con l'ulcera gastrica è però **sintomatico e indiretto**: il farmaco può alleviare nausea, ritardato svuotamento e reflusso associati alla malattia ulcerosa, ma non favorisce la guarigione della mucosa né riduce la secrezione acida. Uno studio sperimentale sul ratto (PMID 2730234) ha mostrato un effetto protettivo in modelli di ulcera indotta, ma non è un dato clinico.

Altre predizioni nella stessa area (gastroduodenite, ulcera peptica, ulcera gastrodigiunale) poggiano sullo stesso razionale procinetico. Per la **perforazione ulcerosa**, invece, non esiste alcun razionale terapeutico: è un'emergenza chirurgica in cui un procinetico non è indicato e potrebbe essere dannoso.

---

## Evidenza dagli studi clinici

| Studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Fase 4 | Sconosciuto | 60 | Premedicazione con metoclopramide in sanguinamento gastrointestinale superiore: valuta la necessità di ripetere l'endoscopia e la visibilità delle pareti gastriche. Studio randomizzato in doppio cieco; uso procedurale, non prova di efficacia sull'ulcera |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | RCT | Rev Gastroenterol Mex | Metoclopramide ad alte dosi vs placebo per la visualizzazione endoscopica nel sanguinamento digestivo alto: utilità controversa |
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT | Am J Gastroenterol | Efficacia della metoclopramide per la visualizzazione gastrica nel sanguinamento digestivo alto attivo |
| [42127996](https://pubmed.ncbi.nlm.nih.gov/42127996/) | 2026 | Linea guida | Endoscopy | Linea guida ESGE sulla gestione endoscopica del sanguinamento da ulcera peptica; non dimostra l'efficacia della metoclopramide |
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Rassegna | Drugs | Proprietà farmacologiche e uso clinico della metoclopramide, incluso il supporto all'endoscopia d'urgenza |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Rassegna | Ann Intern Med | Farmacologia e applicazioni cliniche: antiemetico e stimolante della muscolatura liscia gastrointestinale |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Rassegna | Postgrad Med | Strategie per ulcere ed esofagite da reflusso refrattarie ai regimi standard |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Studio preclinico | Arch Int Pharmacodyn Ther | Effetto antiulcera e antisecretorio della metoclopramide nel ratto |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Studio crossover | MMW Munch Med Wochenschr | Nessuna variazione significativa di gastrina e secrezione acida in volontari sani |
| [1441547](https://pubmed.ncbi.nlm.nih.gov/1441547/) | 1992 | Rassegna | Wiad Lek | Dispepsia non ulcerosa: tra i procinetici preferiti figura la metoclopramide |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Rassegna | Annu Rev Med | Gastrite ed esofagite da reflusso alcalino |

---

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 042091013 | METOCLOPRAMIDE\*5 fiale IM EV 10 mg 2 ml | SALF SpA | Autorizzata |
| 020766010 | PLASIL\*10 mg/2 ml soluzione iniettabile 5 fiale 2 ml | SANOFI Srl | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

---

## Considerazioni di sicurezza

- **Controindicazioni dal grafo di conoscenza** (non provenienti dal foglio illustrativo): ipertensione, epilessia, disturbi d'ansia e nevrotici, distimia, porfiria, cirrosi epatica, insufficienza renale, feocromocitoma e paraganglioma, tumori di duodeno, intestino tenue, cuore e surrene, ulcera peptica attiva, sindrome neurolettica maligna, discinesia tardiva, disturbi parkinsoniani e malattia di Parkinson, distonia di torsione, deficit di piruvato deidrogenasi E3 e metaemoglobinemia da deficit di metaemoglobina reduttasi.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle visibili, le principali di livello **maggiore** riguardano **tramadolo** e **amisulpride**. Numerose interazioni di livello moderato coinvolgono oppioidi (fentanil, codeina, diidrocodeina, alfentanil), sedativi e ansiolitici (alprazolam, amobarbital, etanolo), antistaminici (clorfenamina, cetirizina) e altri (amitriptilina, amantadina, abiraterone). Il paracetamolo è di livello minore.
- Particolarmente rilevante: l'ulcera peptica attiva e la perforazione compaiono tra le situazioni a rischio, il che si scontra con l'indicazione prevista.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo, non disponibile nei dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- L'evidenza è a livello L4: l'unico studio clinico riguarda un uso procedurale (visualizzazione endoscopica) e non la guarigione dell'ulcera; la letteratura è costituita in gran parte da rassegne datate. Il meccanismo è solo sintomatico e le controindicazioni nel grafo includono l'ulcera peptica attiva.

<!-- review:begin it-lic-20261106-metoclopramide-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Il meccanismo è solo sintomatico e le controindicazioni nel grafo includono l'ulcera peptica attiva. / Inoltre, tutte le autorizzazioni italiane risultano cancellate.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-metoclopramide-1 -->

**Per procedere è necessario:**
- Reperire e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza.
- Ottenere i dati sul meccanismo d'azione da DrugBank.
- Definire con precisione il bersaglio clinico (sollievo sintomatico vs. guarigione dell'ulcera vs. uso procedurale in endoscopia): quest'ultimo appare il filone più concreto, grazie ai recenti RCT del 2024 e 2026.
- Valutare lo stato regolatorio attuale e le formulazioni disponibili.
- Eseguire studi clinici controllati con endpoint di guarigione ulcerosa o di sintomi, se si vuole sostenere l'indicazione terapeutica.

<!-- review:begin it-lic-20261106-metoclopramide-2 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Valutare lo stato regolatorio attuale e le formulazioni disponibili, dato che le autorizzazioni note sono cancellate.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-metoclopramide-2 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «Inoltre, tutte le autorizzazioni italiane risultano cancellate» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-24 | Rimosso: «dato che le autorizzazioni note sono cancellate» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Reglan (metoclopramide hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de55c133-eb08-4a35-91a2-5dc093027397) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

