---
layout: default
title: Acenocoumarol
parent: Solo previsione del modello (L5)
nav_order: 17
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Acenocoumarol: nuova indicazione prevista, Deficit di cofattore 2 dell'eparina (livello di evidenza L5). Indicazione originale: Embolia polmonare"
---

# Acenocoumarol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

# Acenocumarolo: Dalla trombofilia/embolia polmonare al deficit di cofattore 2 dell'eparina

## Sintesi

L'acenocumarolo è un anticoagulante antagonista della vitamina K, originariamente utilizzato per l'embolia polmonare e la trombofilia.
Il modello TxGNN prevede che possa essere efficace per il **deficit di cofattore 2 dell'eparina**,
ma al momento **non risultano studi clinici né pubblicazioni** a supporto: la previsione si basa unicamente sul modello computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Embolia polmonare; trombofilia (indicazioni derivate dal knowledge graph TxGNN, non dal testo autorizzativo AIFA) |
| Nuova indicazione prevista | Deficit di cofattore 2 dell'eparina |
| Punteggio di previsione TxGNN | 99,84% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (0 valide, 2 cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Attualmente non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle conoscenze generali, l'acenocumarolo è un antagonista della vitamina K che inibisce VKORC1, riducendo la sintesi dei fattori della coagulazione vitamina K-dipendenti (II, VII, IX, X) e delle proteine C e S.

Il deficit di cofattore 2 dell'eparina è una trombofilia ereditaria in cui l'inibizione della trombina, mediata da dermatan solfato ed eparina, è ridotta. Poiché gli antagonisti della vitamina K riducono la generazione di trombina e sono già impiegati nella prevenzione secondaria del tromboembolismo venoso in altre trombofilie ereditarie (compresa l'indicazione originale), il legame meccanicistico è plausibile.

Va tuttavia sottolineato che non sono disponibili dati specifici sul cofattore 2 dell'eparina. L'elevato punteggio TxGNN (0,998) è una previsione computazionale e probabilmente riflette la vicinanza del farmaco ai nodi di trombofilia e trombosi nel knowledge graph.

Altre previsioni del modello, con lo stesso livello di evidenza (L5) e la stessa raccomandazione (Hold):
- **Eccesso di fattore V con trombosi spontanea** (punteggio 99,78%): meccanismo coerente con la pratica anticoagulante standard, ma senza studi specifici.
- **Deficit di antitrombina di tipo 2** (punteggio 99,77%): gli antagonisti della vitamina K agiscono indipendentemente dall'antitrombina e sono usati per l'anticoagulazione a lungo termine, ma nei dati compilati non ci sono studi per questa indicazione.

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|------|
| 011782012 | SINTROM*20 cpr 4 mg | MERUS LABS LUXCO II SARL | Cancellata |
| 011782024 | SINTROM*20 cpr 1 mg | MERUS LABS LUXCO II SARL | Cancellata |

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state identificate 117 potenziali interazioni (fonte DDInter), ma per quelle elencate il livello di gravità non è classificato. Tra i farmaci coinvolti: calcitriolo, pantoprazolo, morfina, metformina, omeprazolo, lansoprazolo, vancomicina, prednisone, idrocortisone, cloruro di potassio, prednisolone, ranitidina, metronidazolo, acido acetilsalicilico, budesonide, desametasone, rosiglitazone, lattulosio, simvastatina e rosuvastatina.
- **Altre considerazioni**: il farmaco ha un indice terapeutico ristretto e richiede il monitoraggio dell'INR (valutazione generale basata su conoscenze farmacologiche).

Per avvertenze e controindicazioni si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello (livello L5), senza studi clinici né letteratura per le indicazioni previste. Inoltre il farmaco non ha autorizzazioni valide in Italia (entrambe cancellate) e mancano le informazioni di sicurezza tratte dal foglio illustrativo AIFA, un limite che impedisce di procedere alla valutazione di sicurezza.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA con avvertenze e controindicazioni (dato bloccante)
- Dati dettagliati sul meccanismo d'azione (MOA) da DrugBank
- Revisione sistematica della letteratura sull'uso degli antagonisti della vitamina K nel deficit di cofattore 2 dell'eparina
- Valutazione della disponibilità del prodotto in Italia, dato che le autorizzazioni risultano cancellate
- Classificazione della gravità delle interazioni farmacologiche e piano di monitoraggio dell'INR
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

