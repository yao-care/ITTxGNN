---
layout: default
title: Clobazam
parent: Prove moderate (L3-L4)
nav_order: 114
evidence_level: L4
indication_count: 10
---

# Clobazam
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **10** 
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

# Clobazam: dalla sindrome di Lennox-Gastaut alla sindrome epilettica correlata a infezione febbrile (FIRES)

## Sintesi

Il clobazam è una benzodiazepina utilizzata come antiepilettico, con indicazione originaria per la **sindrome di Lennox-Gastaut**. Il modello TxGNN predice una possibile efficacia per la **sindrome epilettica correlata a infezione febbrile (FIRES)**, ma i dati compilati per questo report non contengono studi clinici registrati e includono solo **2 pubblicazioni** (serie di casi), che non valutano direttamente il clobazam. L'evidenza si basa quindi essenzialmente sulla predizione del modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Sindrome di Lennox-Gastaut (dal grafo di conoscenza; il testo delle indicazioni AIFA non è disponibile) |
| Nuova indicazione predetta | Sindrome epilettica correlata a infezione febbrile (FIRES) |
| Punteggio di predizione TxGNN | 99,82% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 3 (tutte revocate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati nel database. In base alle conoscenze generali, il clobazam è un modulatore allosterico positivo del recettore GABA-A, e la sua efficacia nella sindrome di Lennox-Gastaut è nota. Meccanicisticamente, potrebbe essere applicabile anche ad altre epilessie refrattarie.

La FIRES è una sindrome epilettica refrattaria, una forma di stato epilettico refrattario di nuova insorgenza (NORSE) che colpisce bambini precedentemente sani. Viene spesso trattata con agenti GABAergici (benzodiazepine, barbiturici) e con anestetici ad alte dosi. Questo spiega perché una benzodiazepina come il clobazam risulti plausibile per il modello.

Va però sottolineato che le due pubblicazioni recuperate riguardano il lorazepam enterale e il perampanel, non il clobazam. Supportano la plausibilità dell'uso di benzodiazepine, ma non testano il farmaco in esame. Il punteggio molto elevato di TxGNN è una predizione, non un'evidenza clinica.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Serie di casi | Epileptic Disorders | Il lorazepam enterale come strategia di svezzamento efficace nei pazienti con FIRES dipendenti da midazolam |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Caso clinico | Cureus | Possibile ruolo del perampanel nel ridurre la dipendenza da barbiturici in un ragazzo di 13 anni con FIRES |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 045041035 | EPACLOB flacone orale sospensione 250 ml 1 mg/ml (revocata) | Sospensione orale | Non disponibile |
| 045041023 | EPACLOB flacone orale sospensione 150 ml 1 mg/ml (revocata) | Sospensione orale | Non disponibile |
| 045041062 | EPACLOB flacone orale sospensione 250 ml 2 mg/ml (revocata) | Sospensione orale | Non disponibile |

Tutte e tre le autorizzazioni (titolare: Ethypharm S.A.) risultano revocate; non sono presenti autorizzazioni valide.

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra le principali di livello **Maggiore**: morfina (anche liposomiale) ed eliglustat. Tra quelle di livello **Moderato**: bupropione, aprepitant, omeprazolo, esomeprazolo, lansoprazolo, cimetidina, claritromicina, metoclopramide, dronabinolo, fenfluramina e dexfenfluramina. Gli antiacidi (ossido, carbonato e idrossido di magnesio, idrossido di alluminio, carbonato di calcio, magaldrato) mostrano interazioni di livello **Minore**.
- **Aspetti da considerare**: sedazione, tolleranza ed eventi avversi comportamentali meritano attenzione, in particolare nei bambini.

Per le avvertenze e le controindicazioni complete, consultare il foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per la FIRES non esistono studi clinici né dati diretti sul clobazam; l'evidenza è limitata a predizione del modello e a letteratura su altri farmaci. Inoltre, in Italia tutte le autorizzazioni sono revocate e i dati di sicurezza da foglio illustrativo non sono disponibili.

**Per procedere sono necessari:**
- Dati diretti sul clobazam nella FIRES (serie di casi o studi clinici specifici)
- Acquisizione del foglio illustrativo AIFA con avvertenze e controindicazioni
- Dati sul meccanismo d'azione
- Verifica della disponibilità di una formulazione autorizzata in Italia, adatta alla popolazione pediatrica
- Piano di monitoraggio della sicurezza (sedazione, tolleranza, eventi comportamentali, interazioni con oppioidi)

## Altre indicazioni predette (per riferimento)

| Indicazione predetta | Punteggio TxGNN | Livello di evidenza | Raccomandazione |
|------|------|------|------|
| Epilessia con mioclonie periorali e assenze | 99,79% | L5 | Hold |
| Spasmi epilettici tardivi criptogenici | 99,77% | L5 | Hold |
| Epilessia infantile atipica con punte centrotemporali | 99,77% | L4 | Research Question |
| Epilessia fotosensibile del lobo occipitale | 99,77% | L5 | Hold |
| **Encefalopatia epilettica a esordio infantile** | 99,59% | L3 | **Proceed with Guardrails** |
| Epilessia occipitale benigna | 99,58% | L4 | Research Question |
| Encefalopatia epilettica precoce da mutazione GRIN2A | 99,40% | L5 | Hold |
| Sindrome delle gambe senza riposo | 99,30% | L5 | Hold |
| Polimicrogiria con ipoplasia del nervo ottico | 99,09% | L5 | Hold |

Tra queste, l'**encefalopatia epilettica a esordio infantile** è l'indicazione con il supporto più solido (linee guida e revisioni su LGS, sindrome di Dravet e altre encefalopatie dello sviluppo e epilettiche che discutono il clobazam). Si tratta però di un'estrapolazione dall'indicazione già nota, e richiede conferma specifica per sindrome.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

