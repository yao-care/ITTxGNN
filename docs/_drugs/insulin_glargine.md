---
layout: default
title: Insulin Glargine
parent: Solo previsione del modello (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Insulin Glargine: nuova indicazione prevista, Ooforite autoimmune (livello di evidenza L5). Indicazione originale: Diabete mellito di tipo 1 e di tipo 2 (indicazioni derivate dal grafo…"
monitor_inn: "insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Insulina glargine: dal diabete mellito all'ooforite autoimmune

## Sintesi in una frase

L'insulina glargine è un'insulina basale ad azione prolungata, utilizzata originariamente per il trattamento del diabete mellito di tipo 1 e di tipo 2. Il modello TxGNN prevede una possibile efficacia per l'**ooforite autoimmune**, ma per questa indicazione **non risultano sperimentazioni cliniche né pubblicazioni** a supporto: la previsione poggia solo sul modello computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Diabete mellito di tipo 1 e di tipo 2 (indicazioni derivate dal grafo di conoscenza TxGNN; il testo dell'indicazione autorizzata non è disponibile nei dati compilati) |
| Nuova indicazione prevista | Ooforite autoimmune |
| Punteggio di previsione TxGNN | 99,88% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 8 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

I dati compilati non riportano un meccanismo d'azione dettagliato. L'insulina glargine è un analogo dell'insulina basale a lunga durata d'azione che agisce sul recettore dell'insulina per regolare il metabolismo del glucosio.

**Non è stato stabilito un legame meccanicistico diretto** con l'ooforite autoimmune, che è un disturbo ovarico immuno-mediato. Questa condizione si associa spesso a sindromi poliendocrine autoimmuni, che possono includere il diabete di tipo 1. Il punteggio elevato riflette quindi con ogni probabilità una vicinanza nella rete di conoscenza dovuta a comorbilità autoimmuni/endocrine condivise, non una reale motivazione terapeutica.

Anche le altre previsioni di alto rango seguono un andamento simile:
- **Sindrome da disfunzione tiamina-responsiva, sindrome della persona rigida (classica e focale)**: l'insulina tratterebbe solo il diabete concomitante, non la malattia primaria.
- **Lipodistrofie e lipoatrofie localizzate**: sono effetti avversi noti dell'iniezione di insulina, quindi un segnale di sicurezza e non un'indicazione terapeutica.
- **Opsismodisplasia**: collegamento solo speculativo tramite la via INPPL1/SHIP2 del segnale insulinico, senza alcuna prova di beneficio.
- **Agenesia pancreatica** (rango 6): la sostituzione insulinica è biologicamente plausibile come terapia sostitutiva, ma non rappresenta un meccanismo nuovo.

## Evidenze dalle sperimentazioni cliniche

Al momento non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Per l'ooforite autoimmune al momento non è disponibile letteratura correlata.

A titolo indicativo, per la seconda previsione per evidenza (agenzia pancreatica) sono state trovate solo pubblicazioni indirette (revisioni generali sulla terapia insulinica, uno studio veterinario sul gatto diabetico e un caso clinico di MODY5 trattato con un agonista GLP-1), nessuna delle quali studia l'insulina glargine in tale condizione.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 043658121 | ABASAGLAR 5 penne preriempite SC 100 U/ml 3 ml | n.d. | n.d. |
| 035724069 | LANTUS 5 cartucce SC 100 U/ml 3 ml | n.d. | n.d. |
| 035724246 | LANTUS SOLOSTAR 5 penne preriempite SC 100 U/ml 3 ml | n.d. | n.d. |
| 035724121 | LANTUS 1 flaconcino SC 1.000 U 10 ml | n.d. | n.d. |
| 043192347 | TOUJEO SOLOSTAR 3 penne preriempite SC 300 U/ml 1,5 ml | n.d. | n.d. |

Tutte le 8 autorizzazioni risultano cancellate; nessuna è attualmente valida. Sono mostrate le prime 5.

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state rilevate 352 interazioni. Tra quelle di livello moderato figurano:
  - altri antidiabetici (metformina, pioglitazone, alogliptin, albiglutide);
  - simpaticomimetici e beta-agonisti (epinefrina, fenilefrina, pseudoefedrina, salbutamolo, formoterolo);
  - corticosteroidi (idrocortisone);
  - estrogeni (estradiolo, etinilestradiolo);
  - altri (acebutololo, acetazolamide, idroclorotiazide, doxiciclina, etanolo, alpelisib).

  Le interazioni con corticosteroidi topici (idrocortisone topico, alclometasone topico) sono di livello minore.
- Per avvertenze e controindicazioni si rimanda al foglio illustrativo.
- Le lipodistrofie localizzate nel sito di iniezione sono un effetto avverso noto della terapia insulinica.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per l'ooforite autoimmune è esclusivamente computazionale (L5), senza sperimentazioni o letteratura, e verosimilmente riflette la comorbilità autoimmune con il diabete di tipo 1 e non un beneficio terapeutico. Inoltre, tutte le autorizzazioni italiane risultano cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank.
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza).
- Una valutazione del razionale biologico per l'ooforite autoimmune e ricerche mirate di letteratura e sperimentazioni.
- Chiarimento dello stato regolatorio in Italia, dato che non esistono autorizzazioni valide.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

