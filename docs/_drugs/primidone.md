---
layout: default
title: Primidone
parent: Solo previsione del modello (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: Dall'Epilessia al Neoplasma del Nervo Trigemino

## Riassunto in una frase

Primidone è un farmaco anticonvulsivante della classe dei barbiturici con una lunga storia di utilizzo nei disturbi convulsivi e nella gestione del tremore essenziale.
Il modello TxGNN prevede che potrebbe essere efficace per il **Neoplasma del Nervo Trigemino** con un punteggio di **99.99%**, tuttavia **0 studi clinici** e **0 pubblicazioni** supportano direttamente questa indicazione.
L'analisi del dossier probatorio suggerisce fortemente che questa previsione riflette una perdita semantica nel grafo della conoscenza piuttosto che un vero segnale terapeutico.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Non registrata in Italia; uso farmacologico consolidato per epilessia e tremore essenziale |
| Indicazione Prevista | Neoplasma del Nervo Trigemino |
| Punteggio Previsione TxGNN | 99.99% |
| Livello di Evidenza | L5 |
| Stato Mercato Italia | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Sospensione |

---

## Perché questa previsione è ragionevole?

Attualmente i dati dettagliati sul meccanismo d'azione non sono disponibili nel dossier probatorio. Basandosi sulla conoscenza farmacologica consolidata, Primidone è un farmaco anticonvulsivante della classe dei barbiturici che viene metabolizzato in vivo in fenobarbital e feniletilmalonamide (PEMA). Questi metaboliti attivi aumentano primariamente la neurotrasmissione inibitoria mediata dai recettori GABA-A e stabilizzano i canali del sodio voltaggio-dipendenti neuronali, sopprimendo così l'ipereccitabilità patologica. Questo doppio meccanismo sostiene l'efficacia consolidata di Primidone nelle crisi tonico-cloniche generalizzate, nelle crisi parziali e nel tremore essenziale.

Il neoplasma del nervo trigemino è una lesione strutturale e proliferativa del nervo trigemino — una fisiopatologia fondamentalmente diversa dalla disregolazione elettrofisiologica affrontata da Primidone. La crescita tumorale è guidata da segnali di proliferazione e sopravvivenza cellulare incontrollati (ad es. recettori dei fattori di crescita, evasione dell'apoptosi), processi completamente al di fuori dell'ambito del potenziamento GABA-A o del blocco dei canali del sodio. Né Primidone né i suoi metaboliti posseggono proprietà citotossiche, antiproliferative o antiangiogeniche note.

Il punteggio di previsione TxGNN del 99.99% quasi certamente nasce da **perdita semantica**: nel grafo della conoscenza biomedica, il nodo "neoplasma del nervo trigemino" si trova adiacente a "nevralgia trigemino" — un'indicazione in cui gli anticonvulsivanti (in particolare carbamazepina) hanno un'efficacia ben documentata. Il modello confonde la prossimità strutturale nello spazio del grafo con la rilevanza terapeutica, producendo un punteggio elevato che non corrisponde a un vero segnale di trattamento. Questa previsione dovrebbe quindi essere trattata come un noto artefatto della modellazione basata su grafo piuttosto che come un'opportunità di riproposta del farmaco.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul Mercato Italiano

Primidone non è attualmente autorizzato o commercializzato in Italia. Nessun record di licenza AIFA è disponibile.

---

## Considerazioni sulla Sicurezza

Si rimanda al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: Sospensione**

**Razionale:**
Il neoplasma del nervo trigemino è una malattia proliferativa senza connessione meccanicistica con la farmacologia anticonvulsivante di Primidone; il punteggio TxGNN estremamente alto è quasi certamente un falso positivo causato dalla perdita semantica nel grafo della conoscenza tra "neoplasma del nervo trigemino" e il nodo adiacente "nevralgia trigemino", e non vi è alcuna evidenza da studi clinici o dalla letteratura a supporto di questa indicazione.

**Per procedere è necessario quanto segue:**
- Non perseguire il neoplasma del nervo trigemino come bersaglio di riproposta a meno che dati preclinici indipendenti non dimostrino direttamente un effetto di Primidone o dei suoi metaboliti sulla biologia del tumore del nervo trigemino
- Reindirizzare l'analisi verso indicazioni meccanicisticamente difendibili all'interno dello stesso insieme di previsioni — **nevralgia trigemino** (posizione 9, L3 evidenza, S2 Procedere con Cautele), **crisi audiogeniche** (posizione 3, L4), **epilessia da spavento** (posizione 7, L4), e **crisi da lettura** (posizione 8, L4) sono candidati più promettenti
- Recuperare i dati completi del meccanismo d'azione di Primidone dall'API DrugBank per colmare il gap di dati attuale (DG002) e consentire un corretto scoring del collegamento meccanicistico su tutte le indicazioni previste
- Ottenere e analizzare il foglio illustrativo TFDA/AIFA (DG001) per completare il profilo di sicurezza prima di qualsiasi valutazione della fattibilità clinica

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

