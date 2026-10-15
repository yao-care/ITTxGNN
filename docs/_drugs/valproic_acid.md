---
layout: default
title: Valproic Acid
parent: Solo previsione del modello (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Valproic Acid
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Acido valproico: dall'epilessia al neoplasma del nervo trigemino

## Sintesi in una frase

L'acido valproico è un farmaco antiepilettico e stabilizzatore dell'umore, usato in origine per epilessia, epilessia di assenza e disturbo bipolare in fase maniacale. Il modello TxGNN lo indica come possibile candidato per il **neoplasma del nervo trigemino** (punteggio molto alto), ma per questa indicazione i dati compilati mostrano **0 studi clinici** e **1 pubblicazione**, non pertinente al tumore. Il livello di evidenza è quindi molto debole.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Epilessia, disturbo bipolare maniacale, epilessia di assenza (da archi di indicazione del grafo di conoscenza TxGNN; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Neoplasma del nervo trigemino |
| Punteggio di predizione TxGNN | 99,97% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 20 (tutte revocate, 0 valide) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nel materiale compilato. In generale, l'acido valproico è noto per il blocco dei canali del sodio, il potenziamento della trasmissione GABAergica e l'inibizione dei canali del calcio di tipo T, oltre a una generica attività di inibizione delle istone deacetilasi (HDAC).

Il legame con il neoplasma del nervo trigemino appare debole. L'unico lavoro collegato è una serie di casi del 1997 sulla sindrome di Sturge-Weber, che non è un tumore del trigemino; lì il valproato serve al controllo delle crisi, non ha un effetto antitumorale. Il razionale basato sull'inibizione delle HDAC è generico e non supportato da dati per questa indicazione. Il punteggio elevato è verosimilmente dovuto alla prossimità nel grafo con epilessia e termini neurologici, più che a un'evidenza biologica specifica.

Per completezza, il modello propone anche altre indicazioni, in gran parte epilessie riflesse (visiva, startle, da alimentazione, da lettura, ecc.) e la nevralgia del trigemino. Per queste il valproato è meccanicisticamente plausibile, ma l'evidenza specifica è scarsa o indiretta; la più sostenuta è l'epilessia visiva (L3, "domanda di ricerca"), che è di fatto un'estensione di un uso già consolidato.

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie di casi | Anales espanoles de pediatria | Esperienza su 14 casi di sindrome di Sturge-Weber in 25 anni (caratteristiche cliniche, evoluzione, risposta terapeutica); non riguarda un neoplasma del trigemino |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano revocate; il testo dell'indicazione approvata non è disponibile. Si elencano le principali 5:

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 038485037 | DEPAKIN CHRONO 30 cpr 300 mg rilascio prolungato (BB Farma) | Compresse a rilascio prolungato | Non disponibile |
| 043953013 | DEPAKIN CHRONO 30 cpr 500 mg rilascio prolungato, flacone (General Pharma Solutions) | Compresse a rilascio prolungato | Non disponibile |
| 022483109 | DEPAKIN CHRONO 30 cpr 300 mg rilascio prolungato (Sanofi) | Compresse a rilascio prolungato | Non disponibile |
| 022483147 | DEPAKIN orale granulato 30 bustine 100 mg rilascio modificato (Sanofi) | Granulato a rilascio modificato | Non disponibile |
| 036334023 | ACIDO VALPROICO 30 cpr 500 mg rilascio prolungato (Sandoz) | Compresse a rilascio prolungato | Non disponibile |

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da archi del grafo di conoscenza, non da testo di scheda tecnica)**: disturbo d'ansia, disturbo nevrotico, disturbo distimico, deficit di carbamoil fosfato sintetasi I, porfiria (inclusa porfiria ereditaria e malattie del metabolismo delle porfirine), malattia renale, piouretere, iperargininemia, malattie ematologiche, pancreatite, citrullinemia, disturbo cognitivo, malattia epatica, malattia della colecisti, trombocitopenia.
- **Interazioni farmacologiche**: sono state identificate 248 interazioni. Tra quelle elencate:
  - **Maggiore**: glicerolo fenilbutirrato.
  - **Moderata**: bupropione, morfina (anche liposomiale), acido acetilsalicilico, claritromicina, difenossina, difenossilato, carbone attivo, dronabinolo, metoclopramide, nabilone.
  - **Minore**: cimetidina, esomeprazolo, ossido di magnesio, idrossido di alluminio, carbonato di calcio, magaldrato, carbonato e idrossido di magnesio.

Per avvertenze e precauzioni d'uso fare riferimento al foglio illustrativo, non disponibile nei dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per il neoplasma del nervo trigemino non esistono studi clinici e l'unica pubblicazione collegata non è pertinente; il punteggio TxGNN molto alto riflette probabilmente la vicinanza nel grafo a termini neurologici, non un'evidenza reale (livello L5).
- Il prodotto non ha autorizzazioni valide in Italia, e il profilo di sicurezza è rilevante (epatotossicità, controindicazioni in disturbi ematologici, pancreatite, ecc.).

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) e prove precliniche dell'effetto antitumorale del valproato su tumori del trigemino/nervi cranici.
- Recupero e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza.
- Verifica dello stato regolatorio attuale in Italia, dato che tutte le autorizzazioni risultano revocate.
- Se l'obiettivo è clinicamente più realistico, dare priorità a indicazioni con razionale più solido (ad esempio l'epilessia visiva o la nevralgia del trigemino), con revisione sistematica dedicata al valproato.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

