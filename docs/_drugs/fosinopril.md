---
layout: default
title: Fosinopril
parent: Solo previsione del modello (L5)
nav_order: 214
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "FOSINOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Fosinopril: nuova indicazione prevista, Malignant hypertensive renal disease (livello di evidenza L5). In Italia, confezioni AIFA: 7 (autorizzate: 7)"
---

# Fosinopril
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

## Fosinopril: Malignant hypertensive renal disease
{: .text-alpha }

## Sintesi in una frase

Il fosinopril è un ACE-inibitore, originariamente utilizzato per il trattamento dell'ipertensione.
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione renovascolare maligna**,
ma per questa direzione non risultano **né sperimentazioni cliniche né pubblicazioni** a supporto: la previsione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Malignant hypertensive renal disease |
| Punteggio di previsione TxGNN | 0.9987 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 7 su 7) |
| Numero di autorizzazioni | 7 (valide: 7) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Fosinopril (traduzione non ufficiale): «Negli animali e nell'uomo, fosinopril sodico viene idrolizzato dalle esterasi nella forma farmacologicamente attiva, fosinoprilat, un inibitore competitivo specifico dell'enzima di conversione dell'angiotensina (ACE). L'ACE è una peptidil dipeptidasi che catalizza la conversione dell'angiotensina I nella sostanza vasocostrittrice angiotensina II.» Testo originale in inglese: "In animals and humans, fosinopril sodium is hydrolyzed by esterases to the pharmacologically active form, fosinoprilat, a specific competitive inhibitor of angiotensin-converting enzyme (ACE). ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: Fosinopril Sodium (fosinopril) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fc38f1bb-f175-4a81-8ed9-c8701efdea35), versione del 2023-11-27; consultato il 2026-11-19). In base alle conoscenze generali, il fosinopril è un profarmaco che viene convertito nel metabolita attivo fosinoprilato, un inibitore dell'enzima di conversione dell'angiotensina (ACE). Riduce quindi i livelli di angiotensina II, uno dei principali motori dell'ipertensione dipendente dalla renina.

L'ipertensione renovascolare dipende fortemente dal sistema renina-angiotensina-aldosterone (RAAS), perciò il legame biologico è plausibile. Va però sottolineato che si tratta essenzialmente di un'estensione dell'indicazione ipertensiva già esistente, più che di un vero segnale di riposizionamento. Gli ACE-inibitori comportano inoltre il rischio di un peggioramento acuto della funzione renale in caso di stenosi bilaterale delle arterie renali.

Le altre previsioni del modello seguono una logica simile o più debole:
- **Malattia renale ipertensiva maligna** (0.9987): il RAAS contribuisce al danno vascolare e alla nefrosclerosi; l'indicazione si sovrappone in gran parte all'uso ipertensivo già approvato.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (0.9987) e **ipertensione polmonare a meccanismo multifattoriale non chiaro** (0.9987): gli ACE-inibitori non sono un trattamento consolidato; le terapie attuali agiscono sulle vie di endotelina, ossido nitrico e prostaciclina.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Per l'indicazione principale (ipertensione renovascolare maligna) non è disponibile letteratura correlata. Per la terza previsione (ipertensione polmonare da malattia polmonare/ipossia) sono state recuperate due pubblicazioni, **nessuna delle quali sostiene l'efficacia**:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclinico/bioinformatica | Experimental and Therapeutic Medicine | Analisi bioinformatica di geni in cellule mesangiali di topo nella nefropatia diabetica; non pertinente |
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Case report (evento avverso) | Revue des Maladies Respiratoires | Polmonite eosinofila ipossica in due pazienti trattati con enalapril e fosinopril; segnale di sicurezza, non di efficacia |

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 027824022 | TENSOGARD\*14 cpr 20 mg | BAUSCH HEALTH IRELAND LIMITED | Autorizzata |
| 038074175 | FOSINOPRIL\*14 cpr 20 mg | DOC GENERICI Srl | Autorizzata |
| 027747029 | FOSIPRES\*14 cpr 20 mg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 027747017 | FOSIPRES\*28 cpr 10 mg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 041340175 | FOSINOPRIL\*14 cpr 20 mg | AUROBINDO PHARMA ITALIA Srl | Autorizzata |
| 037462280 | FOSINOPRIL\*14 cpr 20 mg | ZENTIVA ITALIA Srl | Autorizzata |
| 027735024 | ELITEN\*14 cpr 20 mg | BAUSCH HEALTH IRELAND LIMITED | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

- **Controindicazioni (da relazioni tra farmaco e malattia nel grafo di conoscenza, non dal foglio illustrativo)**: malattia renale, malattia epatica, pancreatite, malattia della colecisti, angioedema (anche ereditario, acquisito e indotto da bloccanti del RAAS), lupus eritematoso sistemico, carenza di potassio, diabete e chetoacidosi diabetica, neutropenia e agranulocitosi, stenosi aortica e valvulopatia aortica, ipotensione, iperparatiroidismo, encefalopatia/coma epatico, malattie del tessuto connettivo e malattie ossee.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle elencate, le più rilevanti sono di livello **maggiore** con **bicarbonato di potassio** e **citrato di potassio** (rischio di iperkaliemia). Numerose interazioni di livello moderato riguardano corticosteroidi (idrocortisone, betametasone, budesonide, triamcinolone, desametasone), antidiabetici (alogliptin, canagliflozin, dapagliflozin, empagliflozin, clorpropamide, metformina, saxagliptin), acido acetilsalicilico, bupropione, morfina, dronabinolo, acido picosolfurico e polietilenglicole con elettroliti.
- **Segnale polmonare**: un case report ha associato gli ACE-inibitori (incluso il fosinopril) a polmonite eosinofila ipossica.
- **Sicurezza renale**: in caso di stenosi bilaterale delle arterie renali o di malattia renale ipertensiva maligna vanno valutati funzione renale, creatinina e potassiemia.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo, che non è disponibile nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio alto (0,9987) ma si basa solo sul modello (livello L5), senza sperimentazioni né letteratura di supporto. L'indicazione si sovrappone in gran parte all'ipertensione già approvata, quindi non rappresenta un reale segnale di riposizionamento.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da fonti come DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, indispensabili per lo screening di sicurezza
- Ricerca di studi clinici o letteratura specifica sull'ipertensione renovascolare e sulla malattia renale ipertensiva maligna
- Valutazione del profilo di sicurezza renale (iperkaliemia, aumento della creatinina, stenosi bilaterale delle arterie renali)
- Chiarimento della strategia regolatoria

<!-- review:begin it-lic-20261106-fosinopril-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Chiarimento della strategia regolatoria, dato che attualmente non esistono autorizzazioni valide in Italia» Rimosso: il numero o lo stato delle autorizzazioni indicato non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-fosinopril-1 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «dato che attualmente non esistono autorizzazioni valide in Italia» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Fosinopril Sodium (fosinopril) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fc38f1bb-f175-4a81-8ed9-c8701efdea35) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

