---
layout: default
title: Octreotide
parent: Solo previsione del modello (L5)
nav_order: 156
evidence_level: L5
indication_count: 2
---

# Octreotide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Octreotide: Da Acromegalia/Tumori Neuroendocrini a Cheratosi Follicolata Invertita Vulvare

## Riassunto in una frase

Octreotide è un analogo sintetico della somatostatina con indicazioni cliniche consolidate nell'acromegalia, nella sindrome carcinoide e nei tumori neuroendocrini.
Il modello TxGNN ne predice l'efficacia per la **Cheratosi Follicolata Invertita Vulvare**,
ma con **0 studi clinici** e **0 pubblicazioni** a supporto di questa direzione, la predizione riposa interamente su inferenza del modello.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originaria | Acromegalia, sindrome carcinoide, tumori neuroendocrini (nessuna autorizzazione italiana in archivio) |
| Indicazione nuova predetta | Cheratosi Follicolata Invertita Vulvare |
| Punteggio predizione TxGNN | 99.58% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili nel Pacchetto di evidenze. In base alla farmacologia consolidata, Octreotide è un analogo sintetico dell'ottapeptide della somatostatina che agonizza principalmente i recettori SSTR2 e SSTR5, sopprimendo l'ormone della crescita (GH), l'IGF-1 e vari ormoni gastrointestinali. La sua efficacia provata nell'acromegalia e nei tumori neuroendocrini è mediata interamente da questo asse dei recettori della somatostatina.

Il collegamento meccanicistico proposto con la **Cheratosi Follicolata Invertita Vulvare (IFK)** è altamente indiretto e richiede almeno quattro passaggi inferenziali: (1) i recettori SSTR2/5 sono espressi a bassi livelli nei cheratinociti epidermici; (2) Octreotide sopprime il rilascio di IGF-1, che potrebbe teoricamente attenuare la proliferazione dei cheratinociti guidata da IGF-1R; (3) l'IFK è un raro tumore benigno di origine del follicolo pilifero associato all'infezione da HPV e a differenziamento acantomatoso — condizioni senza alcun collegamento consolidato all'asse SSTR; (4) nessuno studio ha direttamente esplorato l'agonismo SSTR nell'IFK o nelle cheratosi follicolari correlate.

Il modello di rete grafica TxGNN assegna un punteggio numerico elevato (99.58%), ma ciò riflette la prossimità strutturale nel grafo della conoscenza, non la plausibilità clinica. L'inferenza meccanicistica qui è tra i segnali di riproposizionamento della categoria più debole, e l'estrema rarità dell'IFK vulvare rende la validazione clinica prospettica altamente impraticabile senza almeno una conferma preclinica in vitro come minimo.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Octreotide attualmente non detiene **alcun'autorizzazione commerciale in Italia**. Il farmaco non è commercializzato e nessuna licenza approvata da AIFA è in archivio.

---

## Considerazioni di sicurezza

Si rimanda al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e fasi successive

**Decisione: Sospendere**

**Razionale:**
Questo è un segnale di predizione pura del modello (Livello di evidenza L5) senza studi clinici di supporto o letteratura pubblicata. Il collegamento meccanicistico tra l'agonismo dei recettori della somatostatina di Octreotide e la cheratosi follicolata invertita vulvare copre ≥4 salti grafici indiretti senza validazione sperimentale a nessun livello — cellulare, animale o umano.

**Per procedere, è necessario quanto segue:**

- **Validazione meccanicistica preclinica:** Confermare l'espressione funzionale di SSTR2/5 nelle cellule tumorali IFK e testare l'attività anti-proliferativa di Octreotide in vitro prima di qualsiasi ulteriore investimento
- **Revisione letteraria ampliata:** Ampliare la ricerca ad analoghi della somatostatina + cheratosi della pelle, tumori follicolari e proliferazione epiteliale guidata da HPV per identificare eventuali evidenze di supporto indirette
- **Documentazione MOA:** Recuperare i dati completi di farmacologia DrugBank per caratterizzare formalmente il percorso grafico farmaco-malattia
- **Profilo di sicurezza:** Ottenere informazioni complete sulla prescrizione (avvertenze, controindicazioni, DDI) — attualmente tutti i campi di sicurezza sono lacune nei dati
- **Percorso normativo italiano:** Octreotide non è commercializzato in Italia; stabilire lo stato normativo e la disponibilità di formulazioni è un prerequisito per qualsiasi programma di sviluppo clinico in questa giurisdizione
- **Verifica della fattibilità della malattia:** L'IFK vulvare è una condizione benigna estremamente rara — condurre uno scoping epidemiologico per valutare se una popolazione di studio clinico è realizzabile

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

