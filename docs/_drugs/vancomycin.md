---
layout: default
title: Vancomycin
parent: Solo previsione del modello (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomicina: dall'infezione da Clostridium difficile alla sclerodermia diffusa

## Sintesi in una frase

La vancomicina è un antibiotico glicopeptidico, usato in origine per la colite da *Clostridium difficile*, le infezioni stafilococciche e l'endocardite.
Il modello TxGNN la associa alla **sclerodermia diffusa** con un punteggio molto alto, ma **non risultano studi clinici** e l'unica pubblicazione trovata è un caso clinico non pertinente.
Il punteggio è quindi molto probabilmente un artefatto del grafo di conoscenza e non una reale indicazione di efficacia.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Colite da *Clostridium difficile*, infezioni stafilococciche, endocardite (testo autorizzato AIFA non disponibile) |
| Nuova indicazione prevista | Sclerodermia diffusa |
| Punteggio di previsione TxGNN | 99,92% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 2 (entrambe revocate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è (o non è) ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. È noto che la vancomicina è un antibiotico glicopeptidico che inibisce la sintesi della parete cellulare batterica, agendo sulla sintesi del peptidoglicano nei batteri Gram-positivi.

La sclerodermia diffusa è una malattia autoimmune e fibrotica, senza relazione con un'infezione batterica. **Non esiste un collegamento meccanicistico plausibile** tra l'azione antibatterica della vancomicina e la fisiopatologia della sclerodermia. L'elevato punteggio TxGNN è verosimilmente un artefatto del grafo di conoscenza.

L'unica pubblicazione recuperata riguarda un caso di eritrodermia con sepsi ed eosinofilia, che non sostiene alcuna efficacia nella sclerodermia.

**Altre previsioni del modello.** Tra le prime dieci, solo la **polmonite streptococcica** (punteggio 99,60%, livello L4) è biologicamente plausibile: *Streptococcus pneumoniae* è Gram-positivo e sensibile alla vancomicina, che si usa come terapia empirica o di salvataggio per i ceppi resistenti alla penicillina. Tuttavia si tratta di un uso già compreso nello spettro antibatterico, non di un vero riposizionamento, e si sovrappone all'indicazione esistente per la polmonite stafilococcica. Se i ceppi sono sensibili, si preferiscono alternative meglio tollerate (beta-lattamici, fluorochinoloni respiratori). Le altre previsioni (febbre paratifoide, salmonellosi, febbre tifoide) riguardano batteri Gram-negativi, verso i quali la vancomicina è poco attiva; le restanti non hanno alcun razionale meccanicistico.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Caso clinico | The American Journal of Case Reports | Eritrodermia con sepsi ed eosinofilia in un uomo di 56 anni; non pertinente alla sclerodermia e priva di evidenze di efficacia |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 034984031 | MAXIVANIL*4 cps 250 mg (revocata) | Capsule | Non disponibile |
| 035003033 | LEVOVANOX*4 cps 250 mg (revocata) | Capsule | Non disponibile |

Entrambe le autorizzazioni, intestate a GENETIC SpA, risultano revocate: non vi sono prodotti attualmente validi in Italia con questo principio attivo nei dati compilati.

## Considerazioni di sicurezza

- **Controindicazioni (da relazioni del grafo di conoscenza, non dal foglietto illustrativo)**: malattia renale, piouretere, neutropenia, agranulocitosi, disturbi dell'udito e malattie del sistema uditivo.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle mostrate:
  - **Maggiori**: immunoglobulina umana G (endovenosa), immunoglobulina umana anti-neurotossina botulinica A/B, antigene vivo di *Vibrio cholerae* CVD 103-HgR (vaccino vivo).
  - **Moderate** (esempi): ketorolac, ibuprofene, diclofenac, celecoxib, amfotericina B, amikacina, bacitracina, capreomicina, carboplatino, colestiramina, metformina, mesalazina, estradiolo, etinilestradiolo, ibandronato, balsalazide.

Per avvertenze e controindicazioni ufficiali si rimanda al foglietto illustrativo, non disponibile nei dati compilati.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per la sclerodermia diffusa non esistono studi clinici né letteratura di supporto, e il meccanismo antibatterico della vancomicina non offre alcun razionale; il punteggio TxGNN, pur elevato, va interpretato come artefatto del grafo. Inoltre in Italia non vi sono autorizzazioni valide.

**Per procedere sarebbe necessario:**
- Un razionale biologico credibile per un effetto antifibrotico o immunomodulante, assente allo stato attuale.
- I dati del foglietto illustrativo AIFA su avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza).
- I dati sul meccanismo d'azione da DrugBank.
- Se si volesse approfondire la polmonite streptococcica, un confronto con le alternative standard e la verifica del reale valore aggiunto rispetto all'indicazione stafilococcica già esistente.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

