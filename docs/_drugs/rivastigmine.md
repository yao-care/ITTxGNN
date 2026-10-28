---
layout: default
title: Rivastigmine
parent: Solo previsione del modello (L5)
nav_order: 386
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
description: "Rivastigmine: nuova indicazione prevista, Glaucoma (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Rivastigmine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

## Rivastigmine: Glaucoma
{: .text-alpha }

## Sintesi

La rivastigmina è un inibitore delle colinesterasi, originariamente utilizzato per il trattamento della malattia di Alzheimer. Il modello TxGNN ne prevede una possibile efficacia nel **glaucoma**, ma al momento non sono registrati studi clinici e le evidenze si limitano a **3 pubblicazioni** (di cui 1 studio preclinico sul coniglio e 2 revisioni).

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Glaucoma |
| Punteggio di predizione TxGNN | 0.9927 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è plausibile?

I dati compilati non riportano una descrizione dettagliata del meccanismo d'azione. Dalle informazioni farmacologiche disponibili, la rivastigmina è un inibitore pseudo-irreversibile dell'acetilcolinesterasi (AChE) e della butirrilcolinesterasi (BChE).

Nell'occhio, l'inibizione delle colinesterasi aumenta i livelli di acetilcolina, che stimola i recettori muscarinici del muscolo ciliare e della trabecola. Ciò facilita il deflusso trabecolare e può ridurre la pressione intraoculare (PIO), principale fattore di rischio modificabile nel glaucoma. Si tratta di un meccanismo generale analogo a quello dei miotici colinergici come pilocarpina e fisostigmina.

Un'evidenza preclinica (PMID 10673128) mostra che la rivastigmina topica riduce la PIO nei conigli normotesi. Il punteggio TxGNN è molto alto, ma resta una predizione computazionale e non costituisce prova clinica. Il legame tra Alzheimer (deficit colinergico centrale) e glaucoma (modulazione colinergica del deflusso dell'umore acqueo) è quindi di tipo meccanicistico, non di patologia condivisa.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Studio preclinico (coniglio) | J Ocul Pharmacol Ther | La rivastigmina topica, inibitore selettivo dell'AChE, riduce la pressione intraoculare in conigli normotesi |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revisione | Front Mol Biosci | Analisi di genetica dei sistemi e modellistica molecolare sugli agenti colinergici per la riduzione della PIO; limiti degli agonisti M3 per effetti avversi sistemici |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revisione | Expert Opin Ther Pat | Aggiornamento sui brevetti di inibitori e riattivatori dell'AChE; l'inibizione lieve ha rilevanza terapeutica in Alzheimer, miastenia grave e glaucoma |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati. Principali autorizzazioni (prime 5):

| N. autorizzazione | Prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 034078055 | EXELON 56 cps 3 mg | Novartis Europharm Ltd | Valida |
| 034078081 | EXELON 56 cps 4,5 mg | Novartis Europharm Ltd | Valida |
| 041261064 | DEMELORA 30 cerotti transdermici 9,5 mg/die | Neuraxpharm Italy SpA | Valida |
| 041673106 | NIMVASTID 56 cps 3 mg | Krka d.d. Novo Mesto | Valida |
| 043087143 | Rivastigmina 30 cerotti transdermici 4,6 mg/die | Sandoz GmbH | Valida |

Le formulazioni autorizzate erano orali (capsule) e transdermiche (cerotti): un eventuale sviluppo oftalmico richiederebbe una nuova formulazione, ad esempio topica.

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal grafo di conoscenza TxGNN** (non dal foglio illustrativo): epilessia, malattie dei gangli della base, distonia focale della mano, blefarospasmo, BPCO (compresa la forma grave a esordio precoce), asma (intrinseco e allergico), malattie diarroiche, arresto cardiaco improvviso, malattie della conduzione cardiaca, blocco atrioventricolare, sindrome del nodo del seno (anche familiare), anoressia nervosa, ulcera peptica attiva, ostruzione delle vie urinarie, malattia di Parkinson e disturbi parkinsoniani.
- **Interazioni**: i dati farmacologici indicano come bersagli l'acetilcolinesterasi (ACHE) e la butirrilcolinesterasi (BCHE); non sono riportate interazioni con altri farmaci.
- **Aspetti da valutare in ambito oftalmico**: effetti avversi colinergici sistemici (nausea, bradicardia) ed effetti oculari (miosi, spasmo di accomodazione).

Le avvertenze e le controindicazioni del foglio illustrativo AIFA non sono disponibili: si rimanda al foglio illustrativo per le informazioni di sicurezza complete.

## Conclusioni e passi successivi

**Decisione: Hold**

**Motivazione:**
L'evidenza è limitata a un solo studio preclinico sul coniglio e a revisioni, senza alcuno studio clinico; il punteggio TxGNN è una predizione computazionale. Inoltre le autorizzazioni italiane sono tutte cancellate e le formulazioni esistenti non sono adatte all'uso oculare. Al momento è una domanda di ricerca, non un candidato pronto per lo sviluppo.

**Per procedere sono necessari:**
- Dati dettagliati sul meccanismo d'azione
- Acquisizione e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni)
- Studi preclinici aggiuntivi su modelli di glaucoma (non solo animali normotesi) e sviluppo di una formulazione oftalmica topica
- Valutazione della tollerabilità oculare e sistemica (miosi, spasmo di accomodazione, effetti colinergici)
- Verifica della fattibilità regolatoria, data l'assenza di autorizzazioni valide in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

