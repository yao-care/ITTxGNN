---
layout: default
title: Zonisamide
parent: Solo previsione del modello (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide: Dall'epilessia alla sindrome di Tourette

## Sintesi in una frase

Lo zonisamide è un farmaco antiepilettico, autorizzato in Italia per l'epilessia (crisi parziali), ma tutte le autorizzazioni risultano oggi annullate. Il modello TxGNN lo indica come possibile candidato per la **sindrome di Tourette** (punteggio 99,85%), ma per questa indicazione non sono stati trovati **studi clinici né pubblicazioni** a supporto: la previsione resta puramente teorica.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Epilessia (crisi parziali); il testo dell'indicazione non è riportato nelle autorizzazioni compilate |
| Nuova indicazione prevista | Sindrome di Tourette |
| Punteggio di previsione TxGNN | 99,85% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni annullate |
| Numero di autorizzazioni | 9 (tutte annullate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. Sulla base delle conoscenze generali, lo zonisamide blocca i canali del sodio voltaggio-dipendenti e i canali del calcio di tipo T, con una debole modulazione dei sistemi dopaminergico e serotoninergico. Questo potrebbe, in teoria, avere un rapporto con i circuiti coinvolti nei tic.

Il legame, però, è debole e solo ipotetico. Una revisione pubblicata (PMID 36005856) indica che i farmaci antiepilettici possono addirittura **indurre** disturbi da tic e disturbo ossessivo-compulsivo: questo suggerisce cautela e non è un argomento a favore dell'uso.

Il punteggio elevato del modello riflette la vicinanza nel grafo di conoscenza, non prove cliniche.

---

## Evidenze da studi clinici

Al momento non risulta alcuno studio clinico registrato per lo zonisamide nella sindrome di Tourette.

---

## Evidenze dalla letteratura

Al momento non risulta alcuna letteratura specifica disponibile per lo zonisamide nella sindrome di Tourette.

---

## Altre indicazioni previste (contesto)

Il modello ha prodotto altre previsioni con punteggi simili. Nessuna ha evidenza clinica solida:

| Indicazione prevista | Punteggio | Livello | Osservazioni |
|------|------|------|------|
| Assenze epilettiche (absence epilepsy) | 99,24% | L3 | Razionale meccanicistico più solido (blocco dei canali T-type); studi piccoli o non controllati ([PMID 24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/), [PMID 15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/): 23 pazienti su 45 liberi da assenze in una revisione di cartelle cliniche). È un'estensione del tipo di crisi più che una nuova area terapeutica |
| Disturbo bipolare maniacale | 99,35% | L4 | Solo studio pilota open-label nella depressione bipolare ([PMID 17163811](https://pubmed.ncbi.nlm.nih.gov/17163811/)); segnalato un caso di mania indotta dal farmaco ([PMID 2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/)) |
| Fibromialgia | 99,20% | L5 | Unico studio ([NCT00259636](https://clinicaltrials.gov/study/NCT00259636), fase 4) ritirato con 0 partecipanti |
| Tricotillomania, angina di Prinzmetal, congiuntivite | 99,16–99,78% | L5 | Nessuna evidenza; link meccanicistico solo speculativo |
| Metemoglobinemia (e forme correlate) | 99,52–99,64% | L5 | Nessun legame meccanicistico plausibile; probabile artefatto del grafo di conoscenza |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Titolare |
|---------|------|------|-----------|-----------|
| 036959017 | ZONEGRAN 14 cps 25 mg | Capsule | Annullata | AMDIPHARM LTD |
| 036959094 | ZONEGRAN 28 cps 50 mg | Capsule | Annullata | AMDIPHARM LTD |
| 036959043 | ZONEGRAN 56 cps 100 mg | Capsule | Annullata | AMDIPHARM LTD |
| 044231013 | ZONISAMIDE 14 cps 25 mg | Capsule | Annullata | DOC GENERICI Srl |
| 044836070 | ZONISAMIDE 28 cps 50 mg | Capsule | Annullata | VIATRIS LIMITED |

Sono mostrate 5 delle 9 autorizzazioni totali (tutte monocomponente e annullate). Il testo delle indicazioni approvate non è disponibile nei dati compilati.

---

## Considerazioni sulla sicurezza

Le informazioni sulla sicurezza tratte dal foglietto illustrativo non sono disponibili nei dati compilati; si rimanda quindi al foglietto illustrativo AIFA/EMA.

**Controindicazioni derivate dal grafo di conoscenza** (relazioni farmaco-malattia di PrimeKG, non testo di etichetta; da considerare solo come segnali):
- Disturbi psichiatrici: ansia, disturbi nevrotici, distimia, disturbi psicotici, schizoaffettivi e schizofreniformi
- Malattie renali e litiasi renale (nefrolitiasi)
- Malattie epatiche e della colecisti
- Acidosi metabolica
- Malattie diarroiche
- Discrasie ematologiche: agranulocitosi e varie forme di neutropenia

**Interazioni farmacologiche** (100 interazioni complessive; le principali):
- **Maggiori**: anticolinergici (metscopolamina, iosciamina, atropina, scopolamina, glicopirronio, clidinio, dicicloverina, trospio, mepenzolato, propantelina) e metformina
- **Moderate**: aprepitant, morfina, desametasone, cimetidina, claritromicina, dronabinolo, nabilone, metoclopramide, miconazolo

Per la sindrome di Tourette in particolare, resta il segnale di cautela sui tic indotti da farmaci antiepilettici. Per la fase maniacale del disturbo bipolare, esiste un caso di mania indotta dallo zonisamide.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per la sindrome di Tourette esiste solo una previsione del modello (L5), senza studi clinici né letteratura, e la letteratura disponibile indica un possibile rischio di tic indotti da antiepilettici. Inoltre, tutte le autorizzazioni italiane sono annullate, e i dati di sicurezza ufficiali mancano.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per lo screening di sicurezza
- Reperire i dati sul meccanismo d'azione da DrugBank
- Verificare lo stato regolatorio attuale (motivo dell'annullamento delle autorizzazioni, eventuali alternative di mercato)
- Revisione sistematica della letteratura sullo zonisamide nei disturbi da tic e confronto con i trattamenti standard
- Se si desidera un'indicazione con razionale più forte, valutare in via prioritaria le **assenze epilettiche** (L3), che sono un'estensione all'interno della stessa area terapeutica, tramite studi controllati e confronto con etosuccimide/valproato
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

