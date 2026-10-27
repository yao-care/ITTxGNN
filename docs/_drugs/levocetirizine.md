---
layout: default
title: Levocetirizine
parent: Solo previsione del modello (L5)
nav_order: 265
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Levocetirizine: nuova indicazione prevista, Artrite reumatoide (livello di evidenza L5). Indicazione originale: Rinite allergica, rinite vasomotoria…"
monitor_inn: "Levocetirizine"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Levocetirizine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Levocetirizina: dalla rinite allergica all'artrite reumatoide
{: .text-alpha }

## Sintesi in una frase

La levocetirizina è un antistaminico H1 utilizzato per la rinite allergica, la rinite vasomotoria e l'orticaria idiopatica.
Il modello TxGNN ne prevede una possibile efficacia nell'**artrite reumatoide**, ma si tratta di una previsione puramente computazionale: attualmente **non risultano studi clinici né pubblicazioni** a supporto.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Rinite allergica, rinite vasomotoria, orticaria idiopatica (dal grafo di conoscenza TxGNN; i testi delle autorizzazioni AIFA non riportano indicazioni) |
| Nuova indicazione prevista | Artrite reumatoide |
| Punteggio di predizione TxGNN | 99,73% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 16 |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle conoscenze generali, la levocetirizina è un antagonista del recettore H1 dell'istamina, con efficacia nota nelle patologie allergiche.

Un legame plausibile ma **non verificato** è che il blocco dei recettori H1 possa modulare l'infiammazione mediata dall'istamina a livello sinoviale. Sono inoltre riportati effetti antinfiammatori della levocetirizina, come l'inibizione della migrazione degli eosinofili e la riduzione dell'espressione delle molecole di adesione.

Questi effetti, tuttavia, non sono riconosciuti come modificanti la malattia nell'artrite reumatoide, che dipende soprattutto dalle vie di TNF, IL-6 e dai linfociti T e B. Il punteggio elevato di TxGNN va quindi interpretato con cautela.

Le altre due previsioni di punteggio elevato (sindrome da microftalmia colobomatosa-displasia rizomelica, punteggio 99,59%; sindrome brachidattilia-sindattilia, punteggio 99,52%) non mostrano alcun legame meccanicistico plausibile: sono malformazioni congenite genetiche su cui un antistaminico sintomatico non può agire. Probabilmente riflettono artefatti della topologia del grafo di conoscenza. Anche per queste non vi sono studi né pubblicazioni.

---

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 16 autorizzazioni risultano cancellate; nessuna è attualmente valida. Si elencano le prime 5.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 051063016 | XYZAL 20 cpr rivestite 5 mg | FARMED Srl | Cancellata |
| 039439056 | Levocetirizina 20 cpr rivestite 5 mg | Aurobindo Pharma Italia Srl | Cancellata |
| 035666205 | XYZAL gocce orali 20 ml 5 mg/ml | UCB Pharma SpA | Cancellata |
| 040809042 | Levocetirizina 20 cpr rivestite 5 mg | KRKA d.d. Novo Mesto | Cancellata |
| 049594029 | XYZAL 20 cpr rivestite 5 mg | Farma 1000 Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni dal grafo di conoscenza** (non derivate dal foglio illustrativo): malattia renale, piouretere, malattia renale cronica, sindrome da insufficienza renale cronica, insufficienza renale terminale.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni. Quelle elencate sono per lo più di livello moderato; tra le principali:
  - Oppioidi e affini: morfina (anche liposomiale), fentanil, diidrocodeina, oppio, loperamide, difenossina, difenossilato
  - Altri depressori del SNC o sostanze con effetto sedativo: etanolo, prometazina, clorfenamina, dronabinolo, nabilone
  - Altri: bupropione, metoclopramide, sibutramina, istamina, iodio I-131 e I-123
  - Interazione minore: ialuronidasi

Per avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per l'artrite reumatoide si basa solo sul modello (livello L5), senza studi clinici né letteratura, e il meccanismo ipotizzato non è coerente con la fisiopatologia principale della malattia. Inoltre, tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Fogli illustrativi AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Studi preclinici o rassegne della letteratura sul ruolo dell'antagonismo H1 nell'artrite reumatoide
- Verifica della fattibilità regolatoria, dato che non esistono autorizzazioni valide in Italia
- Valutazione della sicurezza nei pazienti con insufficienza renale
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

