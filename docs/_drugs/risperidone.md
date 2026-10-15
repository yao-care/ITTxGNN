---
layout: default
title: Risperidone
parent: Solo previsione del modello (L5)
nav_order: 383
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

# Risperidone: dalla schizofrenia e dal disturbo bipolare alla paralisi dello sguardo orizzontale familiare con scoliosi progressiva

## Sintesi in una frase

Il risperidone è un antipsicotico atipico utilizzato per schizofrenia, disturbo bipolare (mania) e disturbi dello spettro autistico. Il modello TxGNN lo indica come possibile candidato per la **paralisi dello sguardo orizzontale familiare con scoliosi progressiva**, una rara malattia genetica, con un punteggio molto alto. Per questa indicazione non risultano però **né sperimentazioni cliniche né pubblicazioni** nei dati compilati per questo report: si tratta di una pura previsione del modello.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Schizofrenia, disturbo bipolare (mania), disturbi dello spettro autistico (dal grafo di conoscenza TxGNN; i testi autorizzativi italiani non riportano l'indicazione) |
| Nuova indicazione prevista | Paralisi dello sguardo orizzontale familiare con scoliosi progressiva |
| Punteggio di predizione TxGNN | 99,76% |
| Livello di evidenza | L5 (solo previsione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni annullate (nessuna autorizzazione valida) |
| Numero di autorizzazioni | 20 (tutte annullate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è ragionevole?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. In generale, il risperidone agisce come antagonista dei recettori dopaminergici D2 e serotoninergici 5-HT2A, meccanismo alla base dei suoi usi psichiatrici consolidati.

Per questa nuova indicazione **non emerge alcun legame meccanicistico plausibile**. La condizione è un raro disturbo genetico legato al gene ROBO3, che riguarda la guida assonale nel romboencefalo. La farmacologia recettoriale del risperidone non ha una rilevanza evidente per questa patologia. L'alto punteggio del modello va quindi letto come un segnale statistico del grafo di conoscenza, non come una conferma biologica o clinica.

---

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

---

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni individuate sono **annullate**. Di seguito le prime 5 (prodotto originatore Risperdal, Janssen-Cilag SpA):

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica (dalla denominazione) | Stato |
|---------|------|------|-----------|
| 028752057 | Risperdal 60 cpr rivestite 1 mg bianche | Compresse rivestite | Annullata |
| 028752069 | Risperdal 60 cpr rivestite 2 mg arancioni | Compresse rivestite | Annullata |
| 028752071 | Risperdal 60 cpr rivestite 3 mg gialle | Compresse rivestite | Annullata |
| 028752083 | Risperdal 60 cpr rivestite 4 mg verdi | Compresse rivestite | Annullata |
| 028752095 | Risperdal soluzione orale 100 ml 1 mg/ml | Soluzione orale | Annullata |

Le altre autorizzazioni riguardano generici di diversi titolari (Sandoz, Mylan, Aurobindo, Ratiopharm), anch'essi annullati.

---

## Considerazioni sulla sicurezza

I dati compilati per questo report non includono avvertenze e controindicazioni tratte dal foglio illustrativo AIFA. Si riportano di seguito solo le informazioni disponibili da altre fonti.

- **Condizioni associate a controindicazione nel grafo di conoscenza** (non provengono dal testo del foglio illustrativo e vanno verificate):
  - Disturbi cardiovascolari: infarto miocardico, ictus e disturbi cerebrovascolari, malattie cardiache e della conduzione, arresto cardiaco improvviso, ipotensione e ipotensione ortostatica.
  - Disturbi metabolici: diabete mellito, iperglicemia, chetoacidosi diabetica, iperlipidemia, obesità.
  - Disturbi epatici ed ematologici: malattie del fegato e della colecisti, insufficienza epatica, neutropenia, agranulocitosi, emoglobinopatie.
  - Disturbi neurologici e altri: epilessia, atrofia multisistemica, sindrome da tachicardia posturale ortostatica, carcinoma mammario femminile.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni complessive (fonte DDInter). Tra quelle visibili, le più rilevanti sono di grado **maggiore** con **bupropione** e **morfina**. Numerose interazioni di grado moderato riguardano antidiabetici (metformina, acarbosio, alogliptin, albiglutide, canagliflozin), anticolinergici (atropina, glicopirronio, iosciamina, clidinio), epinefrina, idrocortisone, amfotericina B, loperamide, lorcaserina e bisacodile. Famotidina ha un'interazione moderata e ranitidina minore.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- La previsione ha un punteggio TxGNN elevato (99,76%), ma è priva di sperimentazioni cliniche, letteratura e di un legame meccanicistico plausibile (livello L5).
- Inoltre, tutte le autorizzazioni italiane del risperidone risultano annullate, il che complica ulteriormente qualsiasi percorso di riposizionamento.

**Per procedere sarebbe necessario:**
- Verificare se esista una base biologica credibile tra la farmacologia del risperidone e la patologia legata a ROBO3, o in alternativa deprioritizzare questa previsione.
- Acquisire il foglio illustrativo AIFA per completare le informazioni su avvertenze e controindicazioni.
- Ottenere i dati sul meccanismo d'azione da DrugBank.
- Chiarire la situazione regolatoria e la disponibilità del prodotto in Italia.
- Considerare le altre previsioni emerse per lo stesso farmaco, che hanno evidenze più solide. In particolare, per il **disturbo affettivo maggiore (depressione resistente al trattamento)** esistono due studi di fase 3 completati sul risperidone come terapia aggiuntiva (NCT00095134, 630 partecipanti; NCT00044681, 258 partecipanti) e diverse meta-analisi. Questa direzione appare molto più promettente e meriterebbe una valutazione a parte.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

