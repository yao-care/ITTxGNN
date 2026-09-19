---
layout: default
title: Duloxetina
parent: Solo previsione del modello (L5)
nav_order: 81
evidence_level: L5
indication_count: 0
---

# Duloxetina
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **0** 
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

# DULOXETINA: Valutazione Sospesa – Dossier di Prove Incompleto

## Riassunto in Una Frase

Duloxetina (duloxetine) è un inibitore della ricaptazione della serotonina e della norepinefrina (SNRI) riconosciuto a livello internazionale, approvato in diversi paesi per il disturbo depressivo maggiore, il disturbo d'ansia generalizzato e il dolore neuropatico.
Tuttavia, questo Dossier di Prove non contiene **alcuna nuova indicazione prevista da TxGNN**, **alcun registro normativo italiano** e **alcun dato di sicurezza**, rendendo una valutazione standard del riposizionamento del farmaco impossibile in questa fase.
È richiesta una ri-interrogazione corretta con l'identificatore DrugBank appropriato prima che qualsiasi valutazione possa procedere.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originaria | Non registrata nel database normativo italiano |
| Indicazione Nuova Prevista | Nessuna (previsioni TxGNN assenti) |
| Punteggio Previsione TxGNN | N/A |
| Livello di Evidenza | Non valutabile |
| Stato del Mercato Italia | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In Sospeso |

---

## Perché Non Sono Disponibili Previsioni?

Duloxetina ha restituito zero risultati dal database normativo italiano (AIFA), e il Dossier di Prove non contiene alcun ID DrugBank. Senza un nodo DrugBank valido, la pipeline del grafo della conoscenza TxGNN non può mappare il farmaco su alcun nodo di malattia e pertanto non produce alcuna indicazione prevista.

Questo è quasi certamente un **problema di collegamento dei dati**, non un'assenza genuina di potenziale di riposizionamento. Duloxetina è un composto ben caratterizzato con un meccanismo stabilito (inibizione duale del trasportatore della serotonina SERT e del trasportatore della norepinefrina NET) e un portafoglio di ricerca attivo che copre il dolore neuropatico correlato al cancro, l'incontinenza urinaria da sforzo, la fibromialgia e la neuropatia periferica indotta dalla chemioterapia, tra gli altri.

Le cause radice più probabili sono: (1) lo spelling dell'INN "DULOXETINA" che non corrisponde alla voce del database AIFA (che potrebbe essere indicizzato come "duloxetina" in minuscolo, o per i nomi commerciali **Cymbalta** / **Xeristar**), e (2) l'assenza di un ID DrugBank che impedisce l'esecuzione di TxGNN. La correzione di questi due punti dovrebbe sbloccare sia i dati del meccanismo d'azione che l'intero set di previsioni.

---

## Informazioni sul Mercato Italiano

Nessuna autorizzazione è stata trovata nel database normativo italiano per il termine di interrogazione **"DULOXETINA"**.

> **Nota:** Duloxetina è disponibile in commercio in Italia con i nomi commerciali **Cymbalta** e **Xeristar**. La query a zero risultati probabilmente riflette una mancata corrispondenza ortografica o una limitazione dell'ambito di ricerca nella pipeline automatizzata piuttosto che un'assenza effettiva dal mercato. Si consiglia una ricerca manuale AIFA utilizzando il nome commerciale o l'INN in minuscolo "duloxetina".

---

## Considerazioni sulla Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e Prossimi Passi

**Decisione: In Sospeso**

**Razionale:**
Il Dossier di Prove non contiene alcuna indicazione prevista da TxGNN, alcun record normativo AIFA e alcun avviso di sicurezza — nessuno dei dati minimi richiesti per una valutazione di livello di evidenza da L1 a L5 è presente. Procedere con la valutazione produrrebbe un rapporto strutturalmente vuoto senza contenuto azionabile.

**Per procedere, è necessario quanto segue:**

- **Risolvere l'ID DrugBank:** L'identificatore probabile di duloxetina è **DB00476**; confermare e ri-iniettare nella pipeline.
- **Ri-interrogare AIFA:** Utilizzare la minuscola "duloxetina" e/o i nomi commerciali "Cymbalta" / "Xeristar" per recuperare le autorizzazioni di mercato italiane esistenti e le indicazioni approvate.
- **Ri-eseguire TxGNN:** Con un ID DrugBank valido, ri-eseguire il passo di previsione del grafo della conoscenza per generare indicazioni previste classificate.
- **Recuperare il foglio illustrativo:** Scaricare il PDF del foglio illustrativo AIFA/TFDA per popolare gli avvisi chiave, le controindicazioni e i dati di interazioni farmacologiche.
- **Riconsegnare un Dossier di Prove completo:** Una volta colmate le lacune di cui sopra, rigenerare il Dossier di Prove e riconsegnare per una valutazione completa.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

