---
layout: default
title: Dulaglutide
parent: Solo previsione del modello (L5)
nav_order: 80
evidence_level: L5
indication_count: 0
---

# Dulaglutide
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

# Dulaglutide: Dalla Diabete Mellito di Tipo 2 — Dati Insufficienti nella Pipeline di Riposizionamento

---

## Sintesi in una Frase

La dulaglutide è un agonista recettoriale di GLP-1 (peptide simile al glucagone-1) a lunga durata d'azione, meglio conosciuta con il nome commerciale Trulicity, originariamente sviluppata e approvata per il trattamento del diabete mellito di tipo 2.
L'esecuzione attuale della pipeline TxGNN ha restituito **nessuna nuova indicazione prevista** per questo farmaco — molto probabilmente a causa di input di dati incompleti a monte piuttosto che di un'assenza di potenziale di riposizionamento.
Questo rapporto documenta lo stato delle prove disponibili e raccomanda un risanamento mirato dei dati prima di procedere con qualsiasi valutazione di riposizionamento.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Diabete Mellito di Tipo 2 *(dedotto dalla classe di farmaci; non catturato nel pacchetto di prove)* |
| Nuova Indicazione Prevista | Non disponibile — la pipeline non ha restituito previsioni |
| Punteggio di Previsione TxGNN | N/A |
| Livello di Evidenza | N/A |
| Stato del Mercato Italiano | Non trovato nella query normativa (0 licenze restituite) |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | **Sospensione** |

---

## Perché Questa Previsione è Ragionevole?

Nessun candidato di riposizionamento TxGNN è stato generato in questa esecuzione della pipeline, quindi non esiste alcuna indicazione guidata dal modello da valutare. Tuttavia, vale la pena documentare perché la dulaglutide è un candidato per il riposizionamento farmacologicamente convincente in generale, e perché il risultato vuoto è molto probabilmente un artefatto della pipeline piuttosto che un risultato negativo significativo.

La dulaglutide è un agonista recettoriale di GLP-1 a lunga durata d'azione. Mima la segnalazione incretinica endogena stimolando la secrezione di insulina in modo dipendente dal glucosio, sopprimendo il rilascio di glucagone, rallentando lo svuotamento gastrico e agendo sui centri ipotalamici della sazietà. Poiché i recettori GLP-1 sono ampiamente espressi oltre il pancreas — nel sistema cardiovascolare, fegato, rene, cervello e tratto gastrointestinale — la base meccanicistica per gli effetti pleiotropici è ben consolidata. Lo studio REWIND sugli esiti cardiovascolari ha dimostrato una riduzione significativa degli eventi cardiovascolari avversi maggiori (MACE), e le prove emergenti supportano l'indagine nell'obesità, nella steatoepatite non alcolica (NASH/MASLD), nella malattia renale cronica e nelle malattie neurodegenerative come il Parkinson.

Il pacchetto di prove è privo di due input critici: il campo del meccanismo d'azione (MOA) è contrassegnato come un'assenza di dati, e non sono stati recuperati dati di licenza AIFA italiano. TxGNN si basa su incorporamenti di grafici di conoscenza che incorporano bersagli farmacologici e nodi delle indicazioni approvate. Senza questi punti di ancoraggio, il modello probabilmente non potrebbe generare previsioni sicure — producendo un set di risultati vuoto per impostazione predefinita piuttosto che indicare che la dulaglutide non ha valore di riposizionamento.

---

## Informazioni sul Mercato Italiano

La query normativa ha restituito **0 autorizzazioni** e uno stato "non commercializzato" per la dulaglutide in Italia. Questo risultato è quasi certamente un errore di recupero dei dati. La dulaglutide (Trulicity®) ha ricevuto l'autorizzazione all'immissione in commercio EMA nel 2014 ed è ampiamente elencata nel Formulario Farmaceutico Italiano (Lista di Trasparenza, AIFA). Le probabili cause del risultato nullo includono:

- La query ha utilizzato l'INN "DULAGLUTIDE" mentre il database AIFA potrebbe indicizzare con il nome commerciale "TRULICITY"
- Mancata corrispondenza di codifica o traslitterazione nella query automatizzata

**Azione consigliata:** Rieseguire la query AIFA utilizzando "TRULICITY" come termine di ricerca e fare riferimento incrociato all'EPAR (European Public Assessment Report) tramite il portale EMA.

---

## Considerazioni sulla Sicurezza

I dati sulla sicurezza non sono stati recuperati in questa esecuzione della pipeline. Si prega di fare riferimento al foglio illustrativo per informazioni complete sulla sicurezza.

Sulla base del profilo della classe degli agonisti del recettore GLP-1, le seguenti aree richiedono un'indagine al completamento del pacchetto di prove:

- **Rischio di tumore delle cellule C tiroidee**: Avvertenza a livello di classe basata su dati di carcinogenicità nei roditori; controindicato nei pazienti con anamnesi personale o familiare di carcinoma midollare della tiroide o MEN 2
- **Pancreatite**: Sono stati segnalati casi di pancreatite acuta; interrompere se sospettato
- **Ipoglicemia**: Il rischio aumenta se combinato con secretagoghi insulinici o insulina
- **Effetti gastrointestinali**: Nausea, vomito, diarrea — motivi più comuni per l'interruzione
- **Frequenza cardiaca**: Modesto aumento della frequenza cardiaca a riposo osservato in tutta la classe

---

## Conclusione e Prossimi Passi

**Decisione: Sospensione**

**Razionale:**
La pipeline TxGNN non ha restituito indicazioni previste perché il pacchetto di prove non contiene input critici a livello di farmaco (MOA, bersagli farmacologici, dati normativi AIFA, profilo di sicurezza). Le assenze di dati precludono sia l'inferenza del modello che la valutazione della sicurezza — questo è un problema di completezza della pipeline, non un riflesso del potenziale effettivo di riposizionamento della dulaglutide.

**Per procedere, è necessario:**

- **Rieseguire la query DrugBank (DB09045)** per recuperare il meccanismo d'azione, i bersagli proteici (GLP-1R, ecc.), e le interazioni farmaco-farmaco — l'assenza `DG002` deve essere risolta prima della riesecuzione della pipeline TxGNN
- **Rieseguire la query AIFA** utilizzando il nome commerciale "TRULICITY" per recuperare i dati di autorizzazione all'immissione in commercio italiana e le indicazioni approvate
- **Scaricare e analizzare il foglio illustrativo EMA/AIFA** (SmPC) per compilare i `key_warnings` e `contraindications` — necessario per risolvere l'assenza bloccante `DG001`
- **Rieseguire la pipeline TxGNN** con input di caratteristiche del farmaco completi; data l'ampia espressione del profilo del recettore di dulaglutide, ci si aspettano indicazioni previste significative
- **Definire gli ammassi di indicazioni cardiovascolari, metaboliche e neurologiche** come aree di revisione prioritaria in base alla biologia nota dei recettori GLP-1

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

