---
layout: default
title: Azathioprine
parent: Solo previsione del modello (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Azathioprine: nuova indicazione prevista, Sindrome da microftalmia colobomatosa con displasia rizomelica (livello di evidenza L5). Indicazione originale: Artrite reumatoide"
---

# Azathioprine
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

# Azatioprina: da artrite reumatoide a sindrome microftalmia-coloboma con displasia rizomelica

## Sintesi in una frase

L'azatioprina è un immunosoppressore (antimetabolita delle purine), originariamente indicato per l'**artrite reumatoide**. Il modello TxGNN ne prevede l'efficacia nella **sindrome da microftalmia colobomatosa con displasia rizomelica**, con un punteggio molto alto. A sostegno di questa previsione non c'è però **nessuno studio clinico e nessuna pubblicazione**: si tratta di una previsione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide |
| Nuova indicazione prevista | Sindrome da microftalmia colobomatosa con displasia rizomelica |
| Punteggio di previsione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è (poco) plausibile?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In base alle conoscenze disponibili, l'azatioprina è un antimetabolita purinico con azione immunosoppressiva, la cui efficacia nelle patologie immuno-mediate come l'artrite reumatoide è consolidata.

La nuova indicazione prevista è invece una rara sindrome dello sviluppo, a base genetica, che coinvolge occhio e scheletro. **Non si individua alcun legame meccanicistico plausibile**: l'immunosoppressione non ha un ruolo razionale in una condizione malformativa non immuno-mediata. Il punteggio elevato riflette soltanto la struttura del grafo di conoscenza su cui si basa il modello e non è corroborato da alcuna evidenza clinica o bibliografica.

---

## Evidenza clinica

Attualmente non risulta registrato alcuno studio clinico correlato.

---

## Evidenza bibliografica

Attualmente non è disponibile alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte e quattro le autorizzazioni censite sono cancellate; nessuna è attualmente valida. I prodotti sono compresse rivestite da 50 mg.

| N. autorizzazione | Prodotto | Titolare | Stato |
|---------|------|------|------|
| 050866019 | Azatioprina 50 mg cpr rivestite | DOC Generici Srl | Cancellata |
| 020957039 | Azatioprina 50 mg cpr rivestite | Aspen Pharma Trading Limited | Cancellata |
| 036292050 | Azatioprina 50 mg cpr rivestite | Sandoz SpA | Cancellata |
| 037534017 | Azafor 50 mg cpr rivestite | Dymalife Pharmaceutical Srl | Cancellata |

---

## Considerazioni sulla sicurezza

Le informazioni sulla scheda tecnica non sono disponibili nei dati compilati. Di seguito si riportano le informazioni ricavate da altre fonti.

- **Controindicazioni da grafo di conoscenza** (relazioni farmaco-malattia, non testo di scheda tecnica): pancreatite, trombocitopenia, anemia (inclusa anemia macrocitica), infezioni fungine e dermatofitosi, malattie infettive in generale, compromissione della funzione renale, linfomi (incluso il linfoma primitivo del sistema nervoso centrale, il linfosarcoma e il linfoma epatosplenico a cellule T), trombosi della vena epatica e sindrome di Budd-Chiari.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni. Quelle di livello **moderato** riguardano gli aminosalicilati: mesalazina, balsalazide, olsalazina e sulfasalazina. Quelle di livello **minore** riguardano i sali di zinco (acetato, gluconato, solfato). Per altre interazioni il livello di gravità non è determinato (ad esempio acido acetilsalicilico, amfotericina B, metformina, omeprazolo, pantoprazolo).

Per le avvertenze complete fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per questa sindrome rara si basa solo sul punteggio del modello (livello L5), senza studi né letteratura e senza alcun razionale meccanicistico. Inoltre, tutte le autorizzazioni italiane sono cancellate.

**Per procedere sarebbero necessari:**
- Un razionale biologico che colleghi l'azatioprina alla fisiopatologia della sindrome (oggi assente)
- Dati preclinici o casi clinici a supporto
- I dati sul meccanismo d'azione e sulle avvertenze/controindicazioni della scheda tecnica AIFA
- Una verifica dello stato regolatorio attuale del farmaco in Italia

**Nota:** nello stesso elenco di previsioni, due indicazioni hanno un livello di evidenza L1 e una raccomandazione "Proceed with Guardrails": la **malattia infiammatoria cronica intestinale** (rank 5) e la **colite ulcerosa** (rank 9). Entrambe sono però usi già consolidati nella pratica clinica più che veri riposizionamenti, e meritano una valutazione separata. Le misure di protezione indicate sono:
- genotipizzazione TPMT/NUDT15;
- monitoraggio di emocromo e funzionalità epatica;
- sorveglianza del rischio di linfomi, tumori cutanei e infezioni, soprattutto in associazione con farmaci anti-TNF.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

