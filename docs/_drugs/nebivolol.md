---
layout: default
title: Nebivolol
parent: Solo previsione del modello (L5)
nav_order: 316
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Nebivolol: nuova indicazione prevista, Nefropatia ipertensiva maligna (livello di evidenza L5). Indicazione originale: Ipertensione arteriosa (disturbo ipertensivo)"
monitor_inn: "nebivolol"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Nebivolol
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

# Nebivololo: dall'ipertensione alla nefropatia ipertensiva maligna

## Sintesi in una frase

Il nebivololo è un beta-bloccante selettivo β1 con effetto vasodilatatore mediato dall'ossido nitrico, originariamente usato per l'ipertensione arteriosa.
Il modello TxGNN ne prevede una possibile efficacia nella **nefropatia ipertensiva maligna**, ma per questa indicazione **non risultano sperimentazioni cliniche né pubblicazioni** nei dati compilati per questo report: la previsione si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione arteriosa (disturbo ipertensivo); il testo dell'indicazione autorizzata non è presente nei dati AIFA compilati |
| Nuova indicazione prevista | Nefropatia ipertensiva maligna |
| Punteggio di predizione TxGNN | 99,42% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa previsione è plausibile?

I dati dettagliati sul meccanismo d'azione non sono al momento disponibili. In base alle conoscenze generali, il nebivololo è un beta-bloccante β1 selettivo che, attraverso l'attivazione della eNOS (legata all'agonismo β3), favorisce la vasodilatazione mediata dall'ossido nitrico. Questo profilo è biologicamente coerente con il danno renale da ipertensione.

L'ipertensione e la nefropatia ipertensiva maligna sono strettamente collegate: il controllo pressorio è il fondamento del trattamento. È probabile che l'elevato punteggio TxGNN rifletta soprattutto la vicinanza, nel grafo di conoscenza, all'indicazione ipertensiva già approvata, più che prove indipendenti di efficacia nella nefropatia. Va inoltre considerato che nell'ipertensione maligna l'uso dei beta-bloccanti richiede cautela clinica specifica.

Altre previsioni nello stesso elenco:
- **Ipertensione renovascolare maligna** (99,42%, L5): plausibile la riduzione del rilascio di renina da parte dei beta-bloccanti, ma non verificata.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (99,39%, L4): solo evidenze indirette precliniche (vedi sotto).
- **Ipertensione polmonare ad eziologia multifattoriale non chiara** (99,39%, L5): solo previsione.
- **Sindrome di Braddock** (99,14%, L5): nessun legame meccanicistico identificabile; probabile artefatto di prossimità nel grafo.

## Evidenze da sperimentazioni cliniche

Per la nefropatia ipertensiva maligna, l'indicazione principale, al momento non risultano sperimentazioni cliniche registrate. Nessuna sperimentazione risulta registrata nemmeno per le altre indicazioni previste.

## Evidenze dalla letteratura

Per l'indicazione principale (nefropatia ipertensiva maligna) al momento non sono disponibili pubblicazioni correlate.

Per completezza, per l'indicazione al 3° posto (ipertensione polmonare da malattia polmonare e/o ipossia) sono state recuperate le seguenti pubblicazioni, in gran parte indirette:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Studio clinico | Int J Cardiol | Studio CARNEBI: confronto multiparametrico tra carvedilolo, nebivololo e bisoprololo nello scompenso cardiaco moderato |
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | RCT | Cardiovasc Ther | Nebivololo vs carvedilolo sulla capacità di esercizio in quota (ipossia ipobarica) in soggetti sani |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | Studio di fisiologia clinica | J Hypertens | Effetti di beta-blocco selettivo e non selettivo sulla pressione ambulatoriale a 24 ore in ipossia ipobarica |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisione | Cardiovasc Drugs Ther | Effetti respiratori della terapia beta-bloccante nello scompenso cardiaco |
| [23400988](https://pubmed.ncbi.nlm.nih.gov/23400988/) | 2013 | Fisiologia clinica/animale | Anesth Analg | Il beta-blocco altamente β1-selettivo (nebivololo) compromette in modo dose-dipendente la perfusione cerebrale dopo emodiluizione nei ratti |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | Preclinico (animale) | Pharmacol Rep | Effetto nefroprotettivo del nebivololo in modelli di danno renale acuto nel ratto, con ruolo di SGLT2 |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | Preclinico (animale) | Can J Physiol Pharmacol | Effetto protettivo del nebivololo sulla nefrotossicità da metotrexato nel ratto via AKT1/Hif-1α/eNOS |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | Preclinico (animale) | Drug Chem Toxicol | Il nebivololo attenua il danno epatico da metotrexato via AKT1/Hif-1α/eNOS |
| [35202159](https://pubmed.ncbi.nlm.nih.gov/35202159/) | 2022 | Preclinico (in vitro) | Toxins | Effetto protettivo del nebivololo contro lo stress ossidativo da acidi aristolochici in cellule endoteliali |
| [42264321](https://pubmed.ncbi.nlm.nih.gov/42264321/) | 2026 | Preclinico (in vitro) | Life Sci | Effetti del nebivololo sulla risposta endoteliale in un modello in vitro di preeclampsia |

Nota: nessuno di questi lavori valuta il nebivololo come trattamento dell'ipertensione polmonare. Altri due articoli recuperati (nefrotossicità da mezzi di contrasto iodati e un nanobloccante antitumorale) non risultano pertinenti e sono stati omessi.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati compilati. Principali autorizzazioni (prime 5):

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 039418013 | Nebivololo 28 cpr 5 mg | Towa Pharmaceutical SpA | Cancellata |
| 045621024 | Nebivololo 28 cpr 5 mg | Aurobindo Pharma Italia Srl | Cancellata |
| 038132054 | Nebivololo 28 cpr 5 mg | Sandoz SpA | Cancellata |
| 032209013 | Nebilox 28 cpr div 5 mg | Menarini Internat. O.L.S.A | Cancellata |
| 032210015 | Lobivon 28 cpr 5 mg | A. Menarini Ind. Farm. Riun. Srl | Cancellata |

Altri nomi commerciali tra le autorizzazioni cancellate: Nebiscon, Nivolon, Nobistar.

## Considerazioni sulla sicurezza

- **Controindicazioni (da relazioni del grafo di conoscenza, non dal foglietto illustrativo)**: insufficienza epatica, malattie epatiche, malattie della colecisti, diabete mellito, chetoacidosi diabetica, vasculopatia periferica, claudicatio intermittens, arteriopatia periferica, ipoglicemia, blocco atrioventricolare, malattie bronchiali, malattia del nodo del seno (anche familiare).
- **Interazioni farmacologiche**: individuate 174 interazioni. Tra quelle di livello moderato: epinefrina, idrocortisone, ioscina (iosciamina), bupropione, triamcinolone, morfina, atropina, desametasone, lorcaserina, betametasone, budesonide, glicopirronio, canagliflozin, dapagliflozin, clorpropamide e dicicloverina. Di livello lieve: acido acetilsalicilico e ossido di magnesio.
- Per avvertenze e controindicazioni ufficiali consultare il foglietto illustrativo AIFA, non ancora acquisito.
- Nell'ipertensione polmonare il beta-blocco potrebbe teoricamente peggiorare la funzione ventricolare destra o le risposte all'ipossia: la sicurezza non è stata stabilita.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la nefropatia ipertensiva maligna è solo un risultato del modello (L5), senza sperimentazioni né letteratura, e probabilmente riflette la vicinanza all'indicazione ipertensiva già nota. In più, tutte le autorizzazioni italiane sono cancellate e mancano i dati di sicurezza ufficiali.

**Per procedere sono necessari:**
- Acquisizione e analisi del foglietto illustrativo AIFA (avvertenze e controindicazioni), prerequisito bloccante per lo screening di sicurezza
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Ricerca mirata di letteratura e studi clinici sul nebivololo nella nefropatia ipertensiva maligna e nell'ipertensione renovascolare
- Verifica dello stato regolatorio reale in Italia (motivi delle cancellazioni e disponibilità attuale del prodotto)
- Valutazione di sicurezza specifica per le popolazioni interessate, in particolare in presenza di ipertensione polmonare e compromissione renale
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

