---
layout: default
title: Simvastatin
parent: Solo previsione del modello (L5)
nav_order: 405
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "simvastatin"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Simvastatin: nuova indicazione prevista, Brain stem infarction (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Simvastatin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

## Simvastatin: Brain stem infarction
{: .text-alpha }

## Riepilogo in una frase

La simvastatina è una statina utilizzata per ridurre il colesterolo e per la prevenzione cardiovascolare (ipertrigliceridemia, ipercolesterolemia familiare omozigote, aterosclerosi, ictus e infarto cerebrale).
Il modello TxGNN prevede che possa essere efficace per l'**ipercolesterolemia familiare**, con **8 studi clinici** e **20 pubblicazioni** nei dati compilati per questo report.
Si tratta però di un'indicazione già consolidata o quasi coincidente con quelle originali, quindi non di un vero riposizionamento.

## Quadro sintetico

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Brain stem infarction |
| Punteggio di predizione TxGNN | 0.9941 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

## Perché questa predizione è ragionevole?

Dati dettagliati sul meccanismo d'azione non sono al momento disponibili nei dati compilati. In base alle conoscenze generali, la simvastatina è un inibitore dell'HMG-CoA reduttasi: riduce la sintesi epatica di colesterolo e aumenta i recettori delle LDL, accelerando la clearance del colesterolo LDL.

Questo meccanismo è direttamente rilevante per l'ipercolesterolemia familiare. L'effetto completo richiede però una funzione residua del recettore delle LDL, ed è quindi limitato nella forma omozigote. Poiché l'ipercolesterolemia familiare omozigote figura già tra le indicazioni originali, questa predizione coincide di fatto con un uso già noto.

Altre predizioni nei dati rafforzano la stessa conclusione. L'«ipercolesterolemia autosomica dominante» (rango 4, L1) corrisponde alla forma eterozigote e condivide quasi tutte le evidenze. L'«infarto del tronco encefalico» (rango 2) è un sottotipo di indicazioni già presenti, ma senza evidenza diretta (L4).

## Evidenze dagli studi clinici

| Studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) (ENHANCE) | Fase 3 | Completato | 720 | Ezetimibe + simvastatina ad alte dosi vs simvastatina da sola nella FH eterozigote, con esito sulla progressione dell'aterosclerosi carotidea |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Fase 3 | Completato | 248 | Ezetimibe in associazione a simvastatina in adolescenti con FH eterozigote |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completato | 50 | Ezetimibe aggiunto ad atorvastatina o simvastatina nella FH omozigote (efficacia e sicurezza) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completato | 44 | Estensione open-label di sicurezza a lungo termine della stessa associazione nella FH omozigote |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Fase 3b | Completato | 442 | Effetti renali di rosuvastatina e simvastatina in dislipidemie di tipo IIa/IIb, inclusa FH eterozigote |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fase 3 | Completato | 249 | Alirocumab vs placebo nella FH eterozigote; simvastatina probabilmente solo terapia di fondo |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Fase 3 | Completato | 153 | Alirocumab in bambini e adolescenti con FH eterozigote; simvastatina solo terapia di fondo |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completato | 18 | Alirocumab in pazienti pediatrici con FH omozigote; simvastatina non è il farmaco in studio |

Solo due studi (ENHANCE e NCT00129402) hanno la simvastatina come parte centrale del regime. Negli altri è terapia di fondo o è coinvolta in modo indiretto.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Studio clinico (ENHANCE) | N Engl J Med | Simvastatina con o senza ezetimibe nella ipercolesterolemia familiare e progressione dell'aterosclerosi |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | Studio clinico | J Am Coll Cardiol | Efficacia e sicurezza di ezetimibe + simvastatina negli adolescenti con FH eterozigote |
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | Studio randomizzato | Circulation | Ezetimibe con atorvastatina o simvastatina nella FH omozigote (50 pazienti) |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisione sistematica Cochrane | Cochrane Database Syst Rev | Statine nei bambini con ipercolesterolemia familiare |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Revisione | Drug Saf | Benefici e rischi della simvastatina nella FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Revisione | Expert Opin Drug Saf | Valutazione di benefici e rischi della simvastatina nella FH |
| [2679083](https://pubmed.ncbi.nlm.nih.gov/2679083/) | 1989 | Studio clinico | Am J Med | Simvastatina 20-40 mg: riduzione del LDL-C del 38-42% nella FH |
| [33497862](https://pubmed.ncbi.nlm.nih.gov/33497862/) | 2021 | Analisi post hoc (studio 4S) | Atherosclerosis | Riduzione del LDL-C ed esiti clinici in soggetti con e senza fenotipo FH |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Linea guida | J Am Coll Cardiol | Linea guida ACC/AHA 2026 sulla gestione della dislipidemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Linea guida | Endocr Pract | Linee guida AACE/ACE sulla dislipidemia e la prevenzione cardiovascolare |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ne è attiva alcuna. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Sono elencate le prime 5.

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 037398118 | Simvastatina compresse rivestite 40 mg (Mylan) | Compresse rivestite | Non disponibile |
| 037134261 | Simvastatina compresse rivestite 20 mg (Sun Pharmaceutical) | Compresse rivestite | Non disponibile |
| 038559023 | Sinvalip compresse rivestite 20 mg (Genetic) | Compresse rivestite | Non disponibile |
| 037364054 | Omistat compresse rivestite 40 mg (Agips Farmaceutici) | Compresse rivestite | Non disponibile |
| 037593175 | Simvastatina compresse rivestite 20 mg (Zentiva Italia) | Compresse rivestite | Non disponibile |

## Considerazioni di sicurezza

- **Controindicazioni (da relazioni nel grafo di conoscenza, non dal foglio illustrativo)**: epatopatie, pancreatite, miopatia e malattie muscolari, rabdomiolisi, diabete e chetoacidosi diabetica, iperglicemia, gotta, malattie della colecisti, trombocitopenia, ulcera peptica, sindrome coronarica acuta, coronaropatia e infarto miocardico, tra le altre. Questi dati vanno verificati sul foglio illustrativo ufficiale.
- **Interazioni farmacologiche**: sono state identificate 696 interazioni. Quelle di livello **maggiore** includono amiodarone, amlodipina e fenofibrato. Tra le interazioni moderate: paclitaxel, nifedipina, omeprazolo, aprepitant, zidovudina ed etanolo.
- **Interazione con antiretrovirali (HIV)**: la simvastatina è un substrato sensibile del CYP3A4. Inibitori delle proteasi e cobicistat ne aumentano molto l'esposizione e il rischio di miopatia/rabdomiolisi, e sono documentati casi clinici. In questi pazienti si preferiscono statine più sicure (pitavastatina, pravastatina, rosuvastatina).
- **Uso pediatrico**: nei bambini con ipercolesterolemia familiare servono cautele specifiche (revisioni Cochrane).

Avvertenze e controindicazioni dal foglio illustrativo AIFA non sono disponibili nei dati compilati e vanno consultate separatamente.

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
L'evidenza per l'ipercolesterolemia familiare è di livello L1, con più studi di fase 3 completati e numerose revisioni e linee guida. Tuttavia si tratta di un uso già consolidato e non di un nuovo riposizionamento. Il profilo di interazioni e il rischio muscolare richiedono cautele, e tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione da DrugBank.
- Piano di gestione delle interazioni (CYP3A4, antiretrovirali, amiodarone, amlodipina, fibrati) e monitoraggio muscolare ed epatico.
- Valutazione dedicata per l'uso pediatrico.

**Altre predizioni (rango 2-8):**
- Infarto del tronco encefalico: nessuna evidenza diretta (L4), Hold.
- Deficit di proteina di trasferimento degli esteri del colesterolo, ipercolesterolemia da deficit di colesterolo 7α-idrossilasi, amiloidosi ABri e disturbo del neurosviluppo con andatura atassica: solo predizione del modello (L5), Hold.
- Infezione da HIV: solo studi farmacocinetici di interazione (L3), da trattare come questione di ricerca legata alla dislipidemia associata all'HIV e non come indicazione antivirale.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

