---
layout: default
title: Metformin
parent: Solo previsione del modello (L5)
nav_order: 288
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Metformin: nuova indicazione prevista, Sindrome della gamba rigida focale (focal stiff limb syndrome) (livello di evidenza L5). Indicazione originale: Diabete mellito di tipo 2"
---

# Metformin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Metformina: dal diabete mellito di tipo 2 alla sindrome della gamba rigida focale

## Sintesi in una frase

La metformina è un farmaco antidiabetico, originariamente utilizzato per il trattamento del diabete mellito di tipo 2. Il modello TxGNN ne prevede una possibile efficacia nella **sindrome della gamba rigida focale** (focal stiff limb syndrome), ma **non risultano sperimentazioni cliniche né pubblicazioni** a sostegno di questa ipotesi: si tratta di una predizione puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Diabete mellito di tipo 2 |
| Nuova indicazione prevista | Sindrome della gamba rigida focale (focal stiff limb syndrome) |
| Punteggio di predizione TxGNN | 99,45% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione potrebbe essere (o non essere) ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. Per quanto noto, la metformina agisce attraverso l'attivazione di AMPK, la riduzione della gluconeogenesi epatica e il miglioramento della sensibilità all'insulina. Questi meccanismi non provengono dai dati compilati e vanno confermati con una fonte primaria.

La sindrome della gamba rigida focale è una variante rara dello spettro della sindrome della persona rigida, generalmente considerata di natura autoimmune o neurologica (anticorpi anti-GAD65 o anti-recettore della glicina, ridotta inibizione GABAergica). **Non è supportato alcun collegamento meccanicistico** con l'azione della metformina. L'alto punteggio del modello è verosimilmente legato a una sovrapposizione di comorbilità (gli anticorpi anti-GAD65 sono associati anche al diabete autoimmune), non a una logica terapeutica.

Va inoltre notato che la sindrome della persona rigida classica ha lo stesso identico punteggio (0,99447): le due predizioni non rappresentano segnali indipendenti.

### Altre indicazioni previste (tutte di livello L5, decisione Hold)

| Posizione | Indicazione | Punteggio TxGNN | Osservazione |
|------|------|------|------|
| 2 | Sindrome della persona rigida classica | 99,45% | Stessa fisiopatologia autoimmune/GABAergica; nessun legame terapeutico dimostrato |
| 3 | Opsismodisplasia | 99,40% | Displasia scheletrica da mutazioni INPPL1 (SHIP2, regolatore della via PI3K/insulina); ipotesi solo generativa, non validata |
| 4 | Sindrome da disfunzione responsiva alla tiamina | 99,40% | Il legame deriva dal fenotipo diabetico condiviso; il trattamento è la tiamina; possibile interazione con i trasportatori di cationi organici da valutare come aspetto di sicurezza |
| 5 | Lipodistrofia localizzata indotta da farmaci | 99,06% | Maggiore vicinanza metabolica, ma processo tissutale locale improbabilmente sensibile a un insulino-sensibilizzante sistemico |

---

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

---

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati compilati. Di seguito le principali 5 autorizzazioni (tutte cancellate):

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 017758020 | GLUCOPHAGE 40 cpr rivestite 850 mg | Bruno Farmaceutici SpA | Cancellata |
| 039066509 | METFORMINA 30 cpr rivestite 500 mg | DOC Generici Srl | Cancellata |
| 035195205 | METFORMINA 30 cpr rivestite 500 mg | Teva Italia Srl | Cancellata |
| 050624093 | METFORMINA 60 cpr 750 mg a rilascio prolungato | Sandoz SpA | Cancellata |
| 049629013 | METFORMINA 30 cpr rivestite 500 mg | EG SpA | Cancellata |

---

## Considerazioni sulla sicurezza

Le informazioni su avvertenze e controindicazioni tratte dal foglio illustrativo AIFA non sono disponibili nei dati compilati. Si rimanda al foglio illustrativo per i dettagli.

- **Condizioni associate a controindicazione nel grafo di conoscenza (PrimeKG, non testo di scheda tecnica)**: insufficienza epatica, malattia renale, pancreatite, malattie epatiche e della colecisti, scompenso cardiaco congestizio, insufficienza surrenalica, ipopituitarismo e deficit ipofisari (inclusi deficit di ormone della crescita e ipogonadismo ipogonadotropo, sindrome di Kallmann, sindrome di Sheehan), malattie del timo e piouretere.
- **Interazioni farmacologiche**: individuate 100 interazioni complessive; tra quelle visibili, di gravità **maggiore**: **acetazolamide** ed **etanolo**. Interazioni di gravità moderata comprendono dolutegravir, abemaciclib, fenilefrina, ranitidina, formoterolo, pseudoefedrina, ketorolac, nifedipina, epinefrina, ibuprofene, etinilestradiolo, idrocortisone, salbutamolo, idroclorotiazide e acetoesamide. Minori: acarbosio e corticosteroidi topici (idrocortisone, alclometasone).

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul modello (livello L5), senza sperimentazioni né pubblicazioni, e non esiste un collegamento meccanicistico plausibile con la fisiopatologia autoimmune/neurologica della sindrome. Inoltre, tutte le autorizzazioni italiane del principio attivo risultano cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione verificati da una fonte primaria (es. DrugBank) e analisi di un eventuale legame meccanicistico
- Scheda tecnica/foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Chiarimento sulla situazione regolatoria in Italia (motivo delle cancellazioni e disponibilità di prodotti attualmente commercializzati)
- Revisione sistematica della letteratura ed eventuali studi preclinici sulle indicazioni previste
- Valutazione della compatibilità delle vie di somministrazione (ancora in sospeso)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

