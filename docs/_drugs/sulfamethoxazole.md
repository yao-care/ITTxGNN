---
layout: default
title: Sulfamethoxazole
parent: Solo previsione del modello (L5)
nav_order: 414
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Sulfamethoxazole: nuova indicazione prevista, Congiuntivite contagiosa acuta (livello di evidenza L5). Indicazione originale: Non disponibile nel testo autorizzativo AIFA"
monitor_inn: "sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
---

# Sulfamethoxazole
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

# Sulfametossazolo: dalle infezioni batteriche alla congiuntivite contagiosa acuta

## Riepilogo in breve

Il sulfametossazolo è un antibatterico sulfamidico, usato in associazione fissa con il trimetoprim (cotrimossazolo, ad esempio Bactrim). Nei dati compilati compare tra le indicazioni originali per otite media infettiva, nocardiosi, toxoplasmosi, pneumocistosi, shigellosi e altre.
Il modello TxGNN lo prevede come potenzialmente efficace per la **congiuntivite contagiosa acuta**, con un punteggio molto alto. Le prove a sostegno sono però limitate: **nessuno studio clinico registrato** e **1 pubblicazione** di tipo osservazionale. Inoltre la "congiuntivite" è già tra le indicazioni originali, quindi non si tratta di un vero riposizionamento.

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nel testo autorizzativo AIFA; nel grafo di conoscenza compaiono otite media infettiva, nocardiosi, toxoplasmosi, pneumocistosi, shigellosi, congiuntivite, ecc. |
| Nuova indicazione prevista | Congiuntivite contagiosa acuta |
| Punteggio di predizione TxGNN | 99,63% |
| Livello di evidenza | L4 (come assegnato nei dati compilati; nessuno studio clinico registrato, solo 1 studio di coorte retrospettivo) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (entrambe cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

I dati sul meccanismo d'azione non sono disponibili nelle informazioni compilate. In base alle conoscenze generali, il sulfametossazolo inibisce la diidropteroato sintasi batterica, bloccando la sintesi dei folati. È un meccanismo antibatterico compatibile con le congiuntiviti di origine batterica.

Va però chiarito un punto importante: la congiuntivite è già tra le indicazioni originali del farmaco nel grafo di conoscenza. Il punteggio elevato (0,996) riflette con ogni probabilità questa sovrapposizione con un uso già noto, più che un segnale realmente nuovo. Inoltre il farmaco si usa in associazione fissa con il trimetoprim, quindi un'eventuale attività non può essere attribuita al solo sulfametossazolo.

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Studio di coorte (retrospettivo) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Analisi retrospettiva della batteriologia e della sensibilità agli antibiotici nella congiuntivite batterica acuta pediatrica in Grecia occidentale; descrive i profili di sensibilità, non l'efficacia del sulfametossazolo |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 028313029 | BACTRIM PERFUSIONE*5 fiale EV 80 mg/5 ml + 400 mg/5 ml (EUMEDICA PHARMACEUTICALS GmbH) | Non indicata | Non indicata (autorizzazione cancellata) |
| 021978046 | BACTRIM*16 cpr 160 mg + 800 mg (EUMEDICA PHARMACEUTICALS GmbH) | Non indicata | Non indicata (autorizzazione cancellata) |

## Considerazioni sulla sicurezza

Le informazioni del foglio illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili: per la sicurezza si rimanda al foglio illustrativo.

- **Controindicazioni/condizioni a rischio (dal grafo di conoscenza, non dal testo del foglio illustrativo)**: porfiria (inclusa porfiria ereditaria e disturbi del metabolismo delle porfirine), malattie renali (insufficienza renale, uremia, glomerulonefrite, piureterere), malattie epatiche e della colecisti, discrasie ematiche (trombocitopenia, neutropenia, agranulocitosi, anemia da carenza di acido folico), deficit di G6PD, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, malattia da accumulo di glicogeno, cistinuria e galattosemia.
- **Interazioni farmacologiche**: sono state rilevate 151 interazioni; tra quelle elencate, di livello moderato, figurano:
  - antidiabetici sulfonilureici (clorpropamide, glimepiride, acetoesamide, glipizide, gliburide) e diverse insuline (umana, aspart, degludec, detemir, glargine, glulisina), con possibile effetto ipoglicemizzante;
  - balsalazide e acido picosolfurico.

  Sono di livello lieve famotidina, claritromicina, dolasetron, palonosetron, cisapride e granisetron.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La congiuntivite è già tra le indicazioni originali, quindi la previsione non rappresenta un vero riposizionamento. Le prove sono scarse (nessuno studio clinico, una sola coorte retrospettiva) e tutte le autorizzazioni italiane sono cancellate, il che limita la rilevanza pratica.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione (da DrugBank)
- Chiarimento se la congiuntivite contagiosa acuta si distingue effettivamente dall'indicazione già nota
- Dati di efficacia specifici per la congiuntivite, con valutazione del contributo del trimetoprim nell'associazione
- Verifica della fattibilità della via di somministrazione (es. formulazione oftalmica), attualmente non valutata
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

