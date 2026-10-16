---
layout: default
title: Oxacillin
parent: Solo previsione del modello (L5)
nav_order: 332
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Oxacillin: nuova indicazione prevista, Epiglottite (livello di evidenza L5). Indicazione originale: Infezioni da Staphylococcus aureus e infezioni stafilococciche (farin…"
monitor_inn: "oxacillin"
predicted_indications: ["epiglottitis", "laryngitis", "bacterial arthritis", "urinary tract infection (disease)"]
---

# Oxacillin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Oxacillina: da infezioni stafilococciche a epiglottite

## Sintesi in una frase

L'oxacillina è una penicillina resistente alle penicillinasi, utilizzata originariamente per le infezioni da *Staphylococcus aureus* e altre infezioni stafilococciche (faringite, polmonite stafilococcica, sinusite).
Il modello TxGNN prevede che possa essere efficace per l'**epiglottite**, con un punteggio molto alto (99,90%), ma finora **non sono disponibili studi clinici né pubblicazioni** a sostegno di questa indicazione specifica.
Si tratta quindi di una previsione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni da *Staphylococcus aureus* e infezioni stafilococciche (faringite, polmonite stafilococcica, sinusite); il testo dell'indicazione approvata AIFA non è disponibile |
| Nuova indicazione prevista | Epiglottite |
| Punteggio di previsione TxGNN | 99,90% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 (revocata) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

I dati dettagliati sul meccanismo d'azione non sono al momento disponibili. L'oxacillina è una beta-lattamina resistente alle penicillinasi: inibisce la sintesi della parete cellulare batterica legandosi alle proteine leganti le penicilline (PBP). La sua efficacia nelle infezioni da stafilococco sensibile alla meticillina è consolidata.

L'epiglottite è un'infezione batterica della regione sopraglottica. La causa classica è *Haemophilus influenzae* di tipo b, ma possono essere coinvolti anche *S. aureus* e gli streptococchi. Il punteggio elevato del modello riflette probabilmente la vicinanza, nel grafo di conoscenza, alle indicazioni già note di faringite e infezione stafilococcica.

Vi sono però limiti importanti: l'oxacillina ha scarsa attività su *H. influenzae* e il prodotto non è più in commercio in Italia (autorizzazione revocata). La rilevanza pratica di questa previsione è quindi limitata.

Per completezza, le altre previsioni del modello sono:

| Posizione | Indicazione prevista | Punteggio | Evidenza | Note |
|------|------|------|------|------|
| 2 | Laringite | 99,73% | L5 | Spesso virale e autolimitante; razionale debole |
| 3 | Artrite batterica | 99,50% | L4 | *S. aureus* è la prima causa; estensione dell'indicazione stafilococcica esistente |
| 4 | Infezione delle vie urinarie | 99,03% | L4 | Gli uropatogeni dominanti sono Gram-negativi, non coperti dall'oxacillina |

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata all'epiglottite.

A titolo informativo, per la seconda previsione per evidenza (artrite batterica) sono state reperite 20 pubblicazioni, in gran parte indirette: revisioni sul trattamento delle infezioni da *S. aureus* e sulla gestione delle infezioni osteoarticolari (che indicano nafcillina/oxacillina o cefazolina come scelta per i ceppi MSSA), studi epidemiologici e casistiche. Non vi sono studi specifici sull'oxacillina; è presente anche una segnalazione di sindrome DRESS indotta da oxacillina (PMID [29129411](https://pubmed.ncbi.nlm.nih.gov/29129411/)) e una di leucopenia e granulocitopenia dopo terapia ad alte dosi (PMID [860144](https://pubmed.ncbi.nlm.nih.gov/860144/)).

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 020711065 | PENSTAPHO*1 fiala IM EV 1 g + 1 fiala solv (LABORATOIRES DELBERT) | Non specificata (fiala per uso IM/EV con solvente) | Non disponibile; autorizzazione revocata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza, non da scheda tecnica):** malattia renale, piureter, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, mononucleosi infettiva, sindrome da infezione cronica da virus di Epstein-Barr.
- **Interazioni farmacologiche:** rilevate 41 interazioni; tra le principali di livello moderato figurano doxiciclina, tetraciclina, minociclina, picosolfato e iodio I-131. Claritromicina è di livello minore. Per altre (ad es. morfina, omeprazolo, vancomicina, metronidazolo, prednisone) il livello non è classificato.
- **Segnali di sicurezza dalla letteratura:** reazioni da ipersensibilità (DRESS) e leucopenia/granulocitopenia con terapia ad alte dosi.

Per le avvertenze complete fare riferimento al foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per l'epiglottite si basa solo sul modello (L5), senza studi né pubblicazioni, e l'oxacillina ha scarsa attività sull'agente classico (*H. influenzae*). Il prodotto è inoltre revocato in Italia, e per le infezioni stafilococciche esistono alternative consolidate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione dettagliati (ad es. da DrugBank)
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Evidenze cliniche o microbiologiche specifiche sull'oxacillina nell'epiglottite
- Valutazione di fattibilità regolatoria, dato lo stato di autorizzazione revocata
- Se si vuole un'opzione più solida, valutare l'artrite batterica da MSSA, che è un'estensione dell'indicazione stafilococcica esistente (livello L4), previa revisione sistematica di dati specifici sull'oxacillina
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

