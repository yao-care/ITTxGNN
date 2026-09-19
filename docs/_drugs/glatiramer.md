---
layout: default
title: Glatiramer
parent: Solo previsione del modello (L5)
nav_order: 117
evidence_level: L5
indication_count: 1
---

# Glatiramer
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

# Glatiramer: Dalla Sclerosi Multipla all'Emoglobinopatie

## Riassunto in Una Frase

L'acetato di glatiramer (Copaxone) è un farmaco immunomodulante ben consolidato per la sclerosi multipla ricorrente-remittente (RRMS), che modula le risposte delle cellule T per sopprimere l'infiammazione neurologica.
Il modello TxGNN predice che potrebbe essere efficace per **Emoglobinopatie**,
tuttavia, con **nessuna sperimentazione clinica** e solo **1 case report tangenzialmente correlato**, la base di evidenze è estremamente limitata, collocando questa previsione al confine tra L4–L5.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Sclerosi multipla ricorrente-remittente (RRMS) |
| Nuova Indicazione Predetta | Emoglobinopatie |
| Punteggio di Previsione TxGNN | 99.03% |
| Livello di Evidenza | L4–L5 (borderline) |
| Stato di Commercializzazione in Italia | ✗ Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In sospeso |

---

## Perché Questa Previsione è Ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili in questo pacchetto di prove. Sulla base della conoscenza farmacologica consolidata, l'acetato di glatiramer è un polipeptide sintetico casuale di quattro aminoacidi (alanina, lisina, acido glutammico, tirosina) che imita la proteina basica della mielina (MBP). La sua azione primaria è spostare le risposte delle cellule T-helper da fenotipi pro-infiammatori Th1 verso fenotipi anti-infiammatori Th2, e indurre popolazioni di cellule T regolatorie che attenuano l'autoimmunità del sistema nervoso centrale.

Le emoglobinopatie — incluse la malattia falciforme (SCD) e la talassemia beta — sono fondamentalmente disturbi genetici causati da mutazioni nei geni della globina, che portano a emoglobina strutturalmente anomala o insufficiente e conseguenti globuli rossi disfunzionali. Mentre componenti infiammatorie secondarie sono sempre più riconosciute nella SCD (attivazione dell'endotelio vascolare, infiammazione sterile), il meccanismo della malattia principale è di natura ematopoietica e molecolare, non autoimmune.

Il ponte meccanicistico tra l'asse immunomodulante mirato al SNC del glatiramer e la patobiologia primaria dell'emoglobinopia è indiretto nel migliore dei casi. Lo stesso pacchetto di prove fornito in questa valutazione riconosce che l'asse immunitario del glatiramer e la principale patologia dell'emoglobinopia mancano di una connessione meccanicistica diretta plausibile ("缺乏合理直接機轉橋接"). Questa previsione molto probabilmente riflette una correlazione computazionale rilevata attraverso nodi di rete immunitaria condivisi nel grafo di conoscenza TxGNN, piuttosto che un percorso terapeutico clinicamente azionabile.

---

## Evidenze da Studi Clinici

Attualmente nessuna sperimentazione clinica correlata registrata.

---

## Evidenze dalla Letteratura

| PMID | Anno | Tipo | Journal | Risultati Chiave |
|------|------|------|---------|------------------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case Report | Revue Neurologique | Un paziente con SM di 35 anni con una **storia clinica di talassemia beta** ha sviluppato complicanze immunitarie dopo l'interruzione del natalizumab. Il glatiramer **non è il farmaco in studio**; la talassemia beta è una comorbidità incidentale, non il bersaglio del trattamento. |

> ⚠️ **Importante avvertenza:** Questo case report studia il **natalizumab**, non il glatiramer. La menzione della talassemia beta è un dettaglio della storia medica del paziente, non un risultato terapeutico. Questa pubblicazione **non fornisce alcuna evidenza diretta** per il glatiramer nell'emoglobinopia.

---

## Considerazioni sulla Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: In sospeso**

**Razionale:**
Non ci sono studi clinici registrati e l'unica pubblicazione recuperata è un case report su un farmaco diverso (natalizumab) nel quale l'emoglobinopia appare solo come comorbidità di background del paziente — questo non costituisce evidenza per l'efficacia del glatiramer nell'emoglobinopia. Combinato con l'assenza di una razionale meccanicistica chiara, questa previsione è improbabile che rappresenti un'opportunità di drug repurposing vitale in questo momento.

**Per procedere, è necessario quanto segue:**
- Studio di fattibilità meccanicistica: investigare se qualsiasi percorso infiammatorio secondario nella SCD o talassemia beta (ad es. attivazione di NF-κB, disregolazione delle cellule T) effettivamente si sovrappone con i bersagli noti del glatiramer
- Dati preclinici (in vitro o in modello animale) che dimostrino specificamente un effetto del glatiramer in modelli di malattia dell'emoglobinopia
- Revisione mirata della letteratura sulla disregolazione immunitaria nella malattia falciforme e talassemia per valutare la plausibilità biologica più rigorosamente
- Consultazione con esperti con un ematologo e immunologo clinico per valutare se uno spostamento Th1→Th2 potrebbe avere una rilevanza terapeutica significativa nelle emoglobinopatie
- Recupero di dati MOA completi da DrugBank (identificato come lacuna nei dati) prima di qualsiasi ulteriore valutazione

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

