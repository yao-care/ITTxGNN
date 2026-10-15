---
layout: default
title: Rifabutin
parent: Prove elevate (L1-L2)
nav_order: 378
evidence_level: L1
indication_count: 10
---

# Rifabutin
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **10** 
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

# Rifabutina: dalla profilassi delle infezioni micobatteriche all'infezione da HIV

## Sintesi in una frase

La rifabutina è un antibiotico della classe delle rifamicine, autorizzato in Italia con il nome commerciale Mycobutin. Nei dati compilati per questo report il testo dell'indicazione approvata non è disponibile. Il modello TxGNN la associa all'**infezione da HIV** con un punteggio molto alto. Il suo valore reale riguarda però le infezioni opportunistiche micobatteriche (complesso *Mycobacterium avium*, tubercolosi) nei pazienti con HIV, non un'attività antiretrovirale diretta. La direzione è supportata da **oltre 30 studi clinici registrati** e da **20 pubblicazioni**.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (il testo dell'indicazione della licenza AIFA è vuoto) |
| Nuova indicazione prevista | Infezione da HIV (infectious disease) |
| Punteggio di predizione TxGNN | 99,88% |
| Livello di evidenza | L1 |
| Stato di mercato in Italia | Solo autorizzazioni revocate (cancellate) |
| Numero di autorizzazioni | 1 (0 valide, 1 revocata) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

---

## Perché questa predizione è plausibile?

I dati sul meccanismo d'azione non sono presenti nel database. Secondo l'analisi di ragionevolezza disponibile, la rifabutina è una rifamicina che inibisce la RNA polimerasi DNA-dipendente batterica (gene *rpoB*). **Non ha attività antiretrovirale diretta.**

Il legame con l'HIV è indiretto, ma clinicamente concreto. Nei pazienti con HIV la rifabutina serve a trattare e prevenire le infezioni opportunistiche da micobatteri, in particolare il complesso *M. avium* (MAC) e la tubercolosi. Rispetto alla rifampicina è un induttore più debole del CYP3A4. Per questo è preferita nei pazienti in terapia antiretrovirale con inibitori della proteasi, perché altera meno le concentrazioni di questi farmaci.

Il punteggio TxGNN va quindi letto come segnale di un uso di supporto nei pazienti con HIV (trattamento e profilassi delle co-infezioni), non come evidenza di un effetto sul virus. Il rischio principale è rappresentato dalle interazioni farmacologiche con inibitori della proteasi, inibitori dell'integrasi e cabotegravir/rilpivirina a lunga durata d'azione, che richiedono aggiustamenti di dose e monitoraggio.

---

## Evidenza dagli studi clinici

Sono riportati i 10 studi più rilevanti, selezionati tra quelli con maggiore valore per l'efficacia, poi per sicurezza e farmacocinetica.

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Fase 3 | Completato | 450 | Claritromicina/etambutolo con rifabutina (due dosi) o placebo nella batteriemia da MAC in AIDS |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Fase 3 | Completato | 400 | Confronto randomizzato di quattro regimi per MAC disseminato in AIDS (claritromicina + etambutolo + rifabutina o clofazimina) |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Fase 3 | Completato | 1100 | Claritromicina vs rifabutina vs combinazione nella prevenzione della batteriemia da MAC (CD4 ≤ 100) |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Fase 3 | Completato | 720 | Azitromicina e rifabutina, da sole o in combinazione, per prevenire il MAC disseminato |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Non indicata | Completato | 200 | Studio randomizzato in doppio cieco di un regime con rifabutina per la batteriemia da MAC in AIDS |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Non indicata | Completato | 750 | Rifabutina vs placebo (doppio cieco) per la prevenzione della batteriemia da MAC (CD4 ≤ 200) |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Fase 2 | Completato | 246 | Tre regimi con claritromicina (con rifabutina, etambutolo o entrambi) nel MAC disseminato |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Non indicata | Completato | 215 | Regime intermittente a base di rifabutina nella tubercolosi correlata all'HIV |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Fase 2 | Completato | 47 | Farmacocinetica della rifabutina con terapia antiretrovirale nei pazienti con tubercolosi e HIV (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Fase 2 | Completato | 48 | Farmacocinetica della rifabutina con terapia antiretrovirale nei pazienti con tubercolosi e HIV (Sudafrica) |

Oltre a questi, sono registrati numerosi studi farmacocinetici sulle interazioni con antiretrovirali (indinavir, nelfinavir, nevirapina, efavirenz, maraviroc, dolutegravir, cabotegravir, lersivirina, vesatolimod).

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Coorte | J Antimicrob Chemother | Sicurezza ed efficacia della rifabutina in bambini con HIV/TB in terapia con lopinavir/ritonavir; precedente segnalazione di neutropenia limitante il trattamento |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Coorte | J Antimicrob Chemother | Farmacocinetica e sicurezza della rifabutina in bambini con HIV/TB; un precedente studio era stato interrotto per neutropenia grave |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Modello farmacocinetico | Br J Clin Pharmacol | Interazione rifabutina-dolutegravir: la rifabutina come alternativa alla rifampicina |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Studio di modellizzazione | Clin Infect Dis | Gestione delle interazioni di cabotegravir e rilpivirina a lunga durata d'azione con rifabutina e rifampicina |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | Revisione | Int J Tuberc Lung Dis | Co-somministrazione di rifabutina con terapia antiretrovirale a base di inibitori della proteasi |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Revisione | Drugs | Approccio terapeutico pratico alla co-infezione tubercolosi-HIV |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | Revisione | Drug Safety | Rapporto rischio-beneficio delle terapie per le infezioni da MAC |
| [8785257](https://pubmed.ncbi.nlm.nih.gov/8785257/) | 1996 | Revisione | Clin Infect Dis | Uso della rifabutina nella tubercolosi polmonare, anche nei pazienti con HIV |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Revisione | Arch Intern Med | Aggiornamento sulle interazioni di rifampicina e rifabutina |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Revisione | Microbiol Spectr | Tubercolosi associata all'infezione da HIV |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 028426017 | MYCOBUTIN*30 cps 150 mg (Pfizer Italia Srl) | Non indicata | Non indicata (autorizzazione revocata) |

---

## Considerazioni sulla sicurezza

I dati compilati non includono avvertenze né controindicazioni dal foglio illustrativo AIFA. Sono disponibili le seguenti informazioni.

- **Possibili controindicazioni dal grafo di conoscenza (non dal testo del foglio illustrativo):** trombocitopenia, neutropenia, agranulocitosi, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale. In linea con questo, due studi pediatrici hanno segnalato neutropenia in bambini con HIV/TB trattati con rifabutina.
- **Interazioni farmacologiche:** sono state individuate 163 interazioni. Tra quelle mostrate, una è di livello **maggiore** (eliglustat). Molte sono di livello moderato, ad esempio doxiciclina, idrocortisone, desametasone, betametasone, triamcinolone, morfina, metronidazolo, claritromicina, aprepitant, pioglitazone, saxagliptin, linagliptin, clorpropamide e calcitriolo. Una è di livello lieve (dolasetron). Nel contesto dell'HIV sono particolarmente rilevanti le interazioni con inibitori della proteasi, inibitori dell'integrasi e cabotegravir/rilpivirina a lunga durata d'azione.

Per le avvertenze complete fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails (procedere con cautele)**

**Motivazione:**
- Sono presenti più studi di fase 3 randomizzati e completati sul MAC e sulla sua prevenzione nei pazienti con HIV, quindi il livello di evidenza formale è L1. L'indicazione riguarda però le co-infezioni micobatteriche, non l'HIV in sé.
- L'unica autorizzazione italiana è revocata, e mancano il testo dell'indicazione e i dati di sicurezza del foglio illustrativo.
- Le interazioni farmacologiche numerose e il rischio di neutropenia richiedono precauzioni.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza).
- Ottenere i dati sul meccanismo d'azione da DrugBank.
- Chiarire lo stato regolatorio attuale in Italia, dato che l'autorizzazione è revocata, e l'eventuale disponibilità di altri prodotti.
- Definire un piano di gestione delle interazioni con gli antiretrovirali e di monitoraggio ematologico (emocromo con formula).

---

**Altre indicazioni predette (rango 2-10):** per leprosi e endocardite l'evidenza è limitata a studi preclinici e case report (livello L4). Per pneumocistosi è presente solo evidenza sperimentale indiretta e nessuna prova clinica. Per le restanti (neoplasia endocrina multipla, colangite sclerosante, disturbo del neurosviluppo, congiuntivite, AIDS felina, infezione da virus dell'immunodeficienza delle scimmie) non esistono studi né letteratura, e nessun legame meccanicistico plausibile: raccomandazione Hold.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

