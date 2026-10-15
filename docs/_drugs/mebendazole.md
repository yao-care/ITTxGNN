---
layout: default
title: Mebendazole
parent: Solo previsione del modello (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
---

# Mebendazole
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

# Mebendazolo: Dagli elmintiasi intestinali all'acne (predizione computazionale)

## Sintesi in una frase

Il mebendazolo è un antielmintico benzimidazolico, originariamente usato per enterobiasi, ascaridiasi e tricuriasi. Il modello TxGNN predice che possa essere efficace per l'**acne**, ma al momento non esistono **studi clinici** registrati e l'unica pubblicazione individuata è un caso clinico non pertinente (sparganosi), quindi il supporto è solo computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Enterobiasi, ascaridiasi, tricuriasi (dal grafo di conoscenza TxGNN; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione predetta | Acne |
| Punteggio di predizione TxGNN | 99,20% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cessate |
| Numero di autorizzazioni | 3 |
| Decisione raccomandata | Hold |

---

## Perché questa predizione potrebbe essere ragionevole?

Il mebendazolo è un antielmintico benzimidazolico che si lega alla beta-tubulina del parassita e inibisce la polimerizzazione dei microtubuli. I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione ufficiale, quindi quanto sopra deriva dalla conoscenza generale della classe.

In ambito oncologico sono stati descritti effetti antiproliferativi e antiangiogenici del mebendazolo. Tuttavia, nulla nei dati disponibili collega questi effetti alla fisiopatologia dell'acne (produzione di sebo, colonizzazione da *Cutibacterium acnes*, ipercheratinizzazione follicolare, infiammazione).

Non è stato quindi identificato un legame meccanicistico credibile tra le indicazioni originali (infezioni da elminti intestinali) e l'acne. Il punteggio TxGNN è molto elevato, ma resta una predizione computazionale da considerare come semplice ipotesi, priva di evidenze a supporto.

---

## Evidenze da studi clinici

Al momento non sono registrati studi clinici correlati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Caso clinico | Am J Trop Med Hyg | Caso di sparganosi proliferativa in Venezuela con lesioni cutanee simil-acneiche; non riguarda il trattamento dell'acne con mebendazolo e non è pertinente |

---

## Informazioni sul mercato italiano

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 023821022 | VERMOX sospensione orale 30 ml 20 mg/ml (Janssen Cilag) | Sospensione orale | Non riportata (autorizzazione cessata) |
| 023821010 | VERMOX 6 cpr 100 mg (Janssen Cilag) | Compresse | Non riportata (autorizzazione cessata) |
| 023821034 | VERMOX 30 cpr 500 mg (Janssen Cilag) | Compresse | Non riportata (autorizzazione cessata) |

Tutte e 3 le autorizzazioni risultano cessate: nessun prodotto a base di mebendazolo in forma singola o in associazione è attualmente valido.

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza TxGNN, non da testo di scheda tecnica)**: malattia epatica, malattia della colecisti.
- **Interazioni farmacologiche**: sono state identificate 10 interazioni.
  - Moderate: metronidazolo, iodio I-131, iodio I-123, fenobarbital, carbamazepina, ritonavir, fosfenitoina, fenitoina, primidone.
  - Minore: cimetidina.

Per le avvertenze e le controindicazioni formali si rimanda al foglio illustrativo, non disponibile tra i dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul modello (livello L5), senza studi clinici, senza letteratura pertinente e senza un legame meccanicistico plausibile con l'acne. Inoltre, in Italia tutte le autorizzazioni del mebendazolo risultano cessate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank e analisi di un'eventuale ipotesi biologica specifica per l'acne
- Foglio illustrativo AIFA con avvertenze e controindicazioni, indispensabile per lo screening di sicurezza
- Studi preclinici (es. modelli in vitro/animali di acne) o una ricerca bibliografica mirata su mebendazolo e dermatosi infiammatorie
- Valutazione della compatibilità della via di somministrazione (per l'acne sarebbe verosimilmente rilevante una formulazione topica, non presente nei dati)
- Chiarimento della situazione regolatoria, dato che non esistono autorizzazioni valide in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

