---
layout: default
title: Tolcapone
parent: Solo previsione del modello (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: dalla malattia di Parkinson all'encefalite subacuta di Rasmussen

## Riassunto in una frase

Tolcapone è un inibitore selettivo della COMT (catecol-O-metiltransferasi), originariamente approvato come terapia adiuvante nella malattia di Parkinson dell'adulto per estendere l'effetto della levodopa.
Il modello TxGNN prevede che possa essere efficace per **l'encefalite subacuta di Rasmussen**, un'encefalopatia autoimmune cronica rara.
Attualmente, **nessuno studio clinico** e **nessuna letteratura pubblicata** supportano questa direzione — la previsione poggia interamente sull'inferenza a livello di grafo del modello.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originaria | Malattia di Parkinson (adiuvante a levodopa/carbidopa) |
| Nuova indicazione prevista | Encefalite subacuta di Rasmussen |
| Punteggio di previsione TxGNN | 99.93% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo Pacchetto di evidenze. In base alle informazioni contestuali in tutto il set di dati, tolcapone è un inibitore della COMT — blocca l'enzima che degrada la dopamina e la levodopa in periferia e nel cervello, aumentando così la disponibilità di dopamina alla sinapsi. La sua efficacia nella malattia di Parkinson è ben stabilita lungo questo asse dopaminergico.

L'encefalite subacuta di Rasmussen è un disturbo autoimmune raro e progressivo in cui le cellule T citotossiche attaccano i neuroni in un emisfero cerebrale, causando epilessia focale resistente ai farmaci e declino neurologico progressivo. La patologia centrale è mediata dal sistema immunitario — non è correlata alla dopamina. Non esiste un meccanismo noto per il quale l'inibizione della COMT sopprimrebbe l'attività delle cellule T autoreattive o ridurrebbe la distruzione neuronale in questa malattia.

L'alto punteggio TxGNN (99.93%) probabilmente riflette **la prossimità delle malattie a livello di grafo** — tolcapone e l'encefalite di Rasmussen occupano entrambi i nodi di "malattia neurologica" nel grafo di conoscenza, creando un collegamento apparente attraverso la propagazione della rete piuttosto che per una rilevanza farmacologica genuina. Questa è una limitazione riconosciuta dei modelli di reti neurali grafiche: i punteggi alti possono derivare da somiglianza strutturale del grafo senza supporto meccanicistico. A questo stadio, questa previsione dovrebbe essere trattata solo come un segnale di generazione di ipotesi.

---

## Evidenza dagli studi clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni sulla sicurezza

Si prega di consultare il foglio illustrativo per informazioni sulla sicurezza.

> **Nota:** Tolcapone comporta un rischio noto di **insufficienza epatica fulminante fatale**. Questo è una delle preoccupazioni più gravi di questa classe di farmaci e dovrebbe essere una considerazione centrale in qualsiasi valutazione di repurposing. Il profilo di sicurezza completo — comprese le controindicazioni, gli avvertimenti di scatola nera e le interazioni farmaco-farmaco — deve essere recuperato dal foglio illustrativo ufficiale prima che qualsiasi sviluppo clinico sia perseguito.

---

## Conclusioni e prossimi passi

**Decisione: Sospendere**

**Razionale:**
Nonostante un punteggio TxGNN molto elevato, questa previsione non ha base meccanicistica, nessuno studio clinico di supporto e nessuna letteratura pertinente. Il punteggio riflette quasi certamente un artefatto della topologia del grafo piuttosto che un segnale farmacologico, e il profilo di epatotossicità noto di tolcapone innalza una barriera di sicurezza significativa per qualsiasi nuova indicazione.

**Per procedere è necessario quanto segue:**
- Documentazione completa del meccanismo d'azione e profilo di sicurezza (compreso l'avvertimento di scatola nera sull'epatotossicità) recuperati dal foglio illustrativo ufficiale o dall'API di DrugBank
- Un'ipotesi biologicamente plausibile che colleghi l'inibizione della COMT alla fisiopatologia dell'encefalite di Rasmussen (ad es., qualsiasi ruolo della disregolazione delle catecolamine nella neuroinfammazione autoimmune)
- Almeno uno studio preclinico o una relazione di caso prima che questa indicazione possa essere elevata al di sopra di L5
- Verifica dello stato normativo italiano/AIFA se è da esplorare un percorso di autorizzazione al commercio
- Revisione comparativa delle previsioni di rango più elevato meccanicisticamente plausibili (ad es., Rank 10: parkinsonismo ad esordio giovanile; Rank 6: demenza a corpi di Lewy) che condividono l'asse della malattia dopaminergica e presentano una base meccanicistica più forte

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

