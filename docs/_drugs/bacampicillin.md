---
layout: default
title: Bacampicillin
parent: Prove moderate (L3-L4)
nav_order: 60
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-15
description: "Bacampicillin: nuova indicazione prevista, Malattia dell'uretra (nello specifico, uretrite non gonococcica) (livello di evidenza L3). Indicazione originale: Infezioni delle vie urinarie, gonorrea, fa…"
monitor_inn: "bacampicillin"
predicted_indications: ["epiglottitis", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "celiac trunk compression syndrome", "lymph node palisaded myofibroblastoma", "sacrum chordoma", "disease of retroperitoneum", "disease of uterine broad ligament", "urethral disease", "disease of peritoneum"]
---

# Bacampicillin
{: .fs-9 }

Livello di evidenza: **L3** | Indicazioni previste: **10** 
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

# Bacampicillina: Da infezioni delle vie urinarie a malattia dell'uretra

## Sintesi in una frase

La bacampicillina è un profarmaco dell'ampicillina, originariamente utilizzato per le infezioni delle vie urinarie, la gonorrea, la faringite e la sinusite.
Il modello TxGNN prevede che possa essere efficace per la **malattia dell'uretra**, ma le evidenze sono molto limitate: **nessuno studio clinico registrato** e **una sola pubblicazione** (uno studio pilota del 1989).

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni delle vie urinarie, gonorrea, faringite, sinusite (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia dell'uretra (nello specifico, uretrite non gonococcica) |
| Punteggio di predizione TxGNN | 99,85% |
| Livello di evidenza | L3 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 (revocata) |
| Decisione raccomandata | Hold |

Nota: l'indicazione con il punteggio più alto è l'epiglottite (99,92%, livello L4, senza alcuna evidenza diretta). Questo report si concentra sulla malattia dell'uretra, perché è l'unica previsione per cui sono disponibili dati di letteratura. Il punteggio è ottenuto da un modello di grafo e non rappresenta una probabilità di efficacia clinica.

---

## Perché questa predizione è ragionevole?

Attualmente non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, la bacampicillina è un profarmaco dell'ampicillina, un beta-lattamico: dopo la somministrazione orale viene convertita in ampicillina, che inibisce la sintesi della parete batterica. La sua efficacia nelle infezioni urinarie e nella gonorrea è già riconosciuta, e sul piano meccanicistico potrebbe essere applicabile alle patologie uretrali di origine batterica.

Il limite principale è però rilevante. L'uretrite non gonococcica è causata spesso da *Chlamydia trachomatis* e *Ureaplasma*, patogeni poco coperti dai beta-lattamici. Le linee guida attuali privilegiano doxiciclina o azitromicina, quindi l'efficacia della bacampicillina è dubbia.

Per le altre indicazioni previste (ad esempio l'epiglottite), il legame è plausibile solo in modo indiretto, tramite lo spettro antibatterico dell'ampicillina. Nella pratica attuale si usano cefalosporine di terza generazione a causa della resistenza all'ampicillina. Per le previsioni di ambito oncologico, chirurgico o vascolare (gravidanza ectopica addominale, linfangioma cistico addominale, sindrome da compressione del tronco celiaco, cordoma sacrale e altre) non esiste alcun razionale meccanicistico, e i punteggi elevati sembrano artefatti della predizione su grafo.

---

## Evidenze dagli studi clinici

Al momento non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [2921050](https://pubmed.ncbi.nlm.nih.gov/2921050/) | 1989 | Studio pilota clinico | Genitourinary Medicine | 84 uomini con uretrite non gonococcica trattati con bacampicillina 800 mg due volte al giorno per 7 giorni; 24 positivi per *C. trachomatis*. Tra i 23 positivi presenti al follow-up, 22 sono risultati negativi, ma solo 14 sono diventati asintomatici con strisci uretrali normali. |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 034473013 | BACAMPICILLINA*12 cpr rivestite 1.200 mg (K24 Pharmaceuticals Srl) | Compresse rivestite | Non disponibile (autorizzazione revocata) |

---

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza TxGNN, non dal foglio illustrativo)**: malattia renale, piureter, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, mononucleosi infettiva, sindrome da infezione cronica da virus di Epstein-Barr.
- **Interazioni farmacologiche**: sono state identificate 34 interazioni in totale. Le principali, di livello moderato, riguardano:
  - antiacidi e antiulcera: famotidina, ranitidina, cimetidina, nizatidina, omeprazolo, esomeprazolo, lansoprazolo, dexlansoprazolo, pantoprazolo, rabeprazolo, carbonato di calcio, idrossido di alluminio, carbonato di magnesio, idrossido di magnesio;
  - tetracicline: doxiciclina, minociclina, tetraciclina;
  - altri: balsalazide, acido picosolfurico.
  
  L'interazione con la claritromicina è di livello minore.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo, attualmente non disponibile nei dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'unica evidenza è un piccolo studio pilota del 1989 senza gruppo di confronto chiaro, in una condizione in cui i beta-lattamici sono poco efficaci e le linee guida indicano alternative migliori. Il prodotto è inoltre revocato in Italia.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione da DrugBank
- Studi controllati rispetto a doxiciclina o azitromicina nell'uretrite non gonococcica
- Verifica della disponibilità del prodotto o di formulazioni alternative di ampicillina, dato lo stato di revoca
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

