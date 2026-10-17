---
layout: default
title: Fosinopril
parent: Solo previsione del modello (L5)
nav_order: 214
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Fosinopril: nuova indicazione prevista, Ipertensione renovascolare maligna (livello di evidenza L5). Indicazione originale: Ipertensione (disturbo ipertensivo)"
monitor_inn: "FOSINOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Fosinopril
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Fosinopril: Dall'ipertensione alla Ipertensione renovascolare maligna

## Sintesi in una frase

Il fosinopril è un ACE-inibitore, originariamente utilizzato per il trattamento dell'ipertensione.
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione renovascolare maligna**,
ma per questa direzione non risultano **né sperimentazioni cliniche né pubblicazioni** a supporto: la previsione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione (disturbo ipertensivo) |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di previsione TxGNN | 99,87% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni annullate (nessuna attualmente valida) |
| Numero di autorizzazioni | 7 (tutte annullate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Al momento i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report. In base alle conoscenze generali, il fosinopril è un profarmaco che viene convertito nel metabolita attivo fosinoprilato, un inibitore dell'enzima di conversione dell'angiotensina (ACE). Riduce quindi i livelli di angiotensina II, uno dei principali motori dell'ipertensione dipendente dalla renina.

L'ipertensione renovascolare dipende fortemente dal sistema renina-angiotensina-aldosterone (RAAS), perciò il legame biologico è plausibile. Va però sottolineato che si tratta essenzialmente di un'estensione dell'indicazione ipertensiva già esistente, più che di un vero segnale di riposizionamento. Gli ACE-inibitori comportano inoltre il rischio di un peggioramento acuto della funzione renale in caso di stenosi bilaterale delle arterie renali.

Le altre previsioni del modello seguono una logica simile o più debole:
- **Malattia renale ipertensiva maligna** (99,87%): il RAAS contribuisce al danno vascolare e alla nefrosclerosi; l'indicazione si sovrappone in gran parte all'uso ipertensivo già approvato.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (99,87%) e **ipertensione polmonare a meccanismo multifattoriale non chiaro** (99,87%): gli ACE-inibitori non sono un trattamento consolidato; le terapie attuali agiscono sulle vie di endotelina, ossido nitrico e prostaciclina.
- **Sindrome di Braddock** (99,81%): malattia molto rara che comprende l'ipertensione polmonare; il legame deriva probabilmente dalle associazioni del grafo di conoscenza, senza un razionale meccanicistico specifico.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Per l'indicazione principale (ipertensione renovascolare maligna) non è disponibile letteratura correlata. Per la terza previsione (ipertensione polmonare da malattia polmonare/ipossia) sono state recuperate due pubblicazioni, **nessuna delle quali sostiene l'efficacia**:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclinico/bioinformatica | Experimental and Therapeutic Medicine | Analisi bioinformatica di geni in cellule mesangiali di topo nella nefropatia diabetica; non pertinente |
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Case report (evento avverso) | Revue des Maladies Respiratoires | Polmonite eosinofila ipossica in due pazienti trattati con enalapril e fosinopril; segnale di sicurezza, non di efficacia |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 027824022 | TENSOGARD 14 cpr 20 mg | Bausch Health Ireland Limited | Annullata |
| 038074175 | FOSINOPRIL 14 cpr 20 mg | DOC Generici Srl | Annullata |
| 027747029 | FOSIPRES 14 cpr 20 mg | A. Menarini Ind. Farm. Riun. Srl | Annullata |
| 027747017 | FOSIPRES 28 cpr 10 mg | A. Menarini Ind. Farm. Riun. Srl | Annullata |
| 041340175 | FOSINOPRIL 14 cpr 20 mg | Aurobindo Pharma Italia Srl | Annullata |

Sono presenti in tutto 7 autorizzazioni, tutte annullate; nessuna è attualmente valida.

## Considerazioni sulla sicurezza

- **Controindicazioni (da relazioni tra farmaco e malattia nel grafo di conoscenza, non dal foglio illustrativo)**: malattia renale, malattia epatica, pancreatite, malattia della colecisti, angioedema (anche ereditario, acquisito e indotto da bloccanti del RAAS), lupus eritematoso sistemico, carenza di potassio, diabete e chetoacidosi diabetica, neutropenia e agranulocitosi, stenosi aortica e valvulopatia aortica, ipotensione, iperparatiroidismo, encefalopatia/coma epatico, malattie del tessuto connettivo e malattie ossee.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle elencate, le più rilevanti sono di livello **maggiore** con **bicarbonato di potassio** e **citrato di potassio** (rischio di iperkaliemia). Numerose interazioni di livello moderato riguardano corticosteroidi (idrocortisone, betametasone, budesonide, triamcinolone, desametasone), antidiabetici (alogliptin, canagliflozin, dapagliflozin, empagliflozin, clorpropamide, metformina, saxagliptin), acido acetilsalicilico, bupropione, morfina, dronabinolo, acido picosolfurico e polietilenglicole con elettroliti.
- **Segnale polmonare**: un case report ha associato gli ACE-inibitori (incluso il fosinopril) a polmonite eosinofila ipossica.
- **Sicurezza renale**: in caso di stenosi bilaterale delle arterie renali o di malattia renale ipertensiva maligna vanno valutati funzione renale, creatinina e potassiemia.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo, che non è disponibile nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio alto (99,87%) ma si basa solo sul modello (livello L5), senza sperimentazioni né letteratura di supporto. L'indicazione si sovrappone in gran parte all'ipertensione già approvata, quindi non rappresenta un reale segnale di riposizionamento. In Italia, inoltre, tutte le autorizzazioni sono annullate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da fonti come DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, indispensabili per lo screening di sicurezza
- Ricerca di studi clinici o letteratura specifica sull'ipertensione renovascolare e sulla malattia renale ipertensiva maligna
- Valutazione del profilo di sicurezza renale (iperkaliemia, aumento della creatinina, stenosi bilaterale delle arterie renali)
- Chiarimento della strategia regolatoria, dato che attualmente non esistono autorizzazioni valide in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

