---
layout: default
title: Buprenorphine
parent: Prove moderate (L3-L4)
nav_order: 79
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-15
description: "Buprenorphine: nuova indicazione prevista, Porfiria acuta intermittente (livello di evidenza L4). Indicazione originale: Dipendenza da oppioidi"
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "extrapyramidal and movement disease", "benign shuddering attacks"]
---

# Buprenorphine
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **6** 
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

## Buprenorfina: dalla dipendenza da oppioidi alla porfiria acuta intermittente
{: .text-alpha }

## Sintesi in una frase

La buprenorfina è un oppioide agonista parziale del recettore μ, originariamente utilizzato per il trattamento della dipendenza da oppioidi (e per il dolore intenso).
Il modello TxGNN ne prevede una possibile efficacia nella **porfiria acuta intermittente**, ma **nessuno studio clinico** è registrato e la letteratura si limita a **1 case report del 1993** sulla gestione anestesiologica, che non dimostra alcun beneficio terapeutico.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Dipendenza da oppioidi (anche dipendenza da sostanze e da morfina, secondo il knowledge graph TxGNN) |
| Nuova indicazione prevista | Porfiria acuta intermittente |
| Punteggio di predizione TxGNN | 99,41% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 18 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione potrebbe essere ragionevole?

I dati compilati per questo report non includono una descrizione dettagliata del meccanismo d'azione. Dalle informazioni farmacologiche disponibili, la buprenorfina agisce sul recettore μ (OPRM1) e sul recettore κ (OPRK1). È un agonista parziale μ con effetto antagonista κ, utilizzato per la dipendenza da oppioidi e per il dolore intenso.

Non emerge alcun razionale meccanicistico diretto tra la dipendenza da oppioidi e la porfiria acuta intermittente. Il punteggio molto alto (0,994) è esclusivamente una predizione del modello. L'unico lavoro disponibile riguarda la gestione anestesiologica di una paziente con porfiria e riguarda la sicurezza perioperatoria dei farmaci, non un beneficio terapeutico. Inoltre, la sicurezza della buprenorfina nella porfiria (potenziale porfirinogenicità) non è stabilita dai dati disponibili e dovrebbe essere verificata prima di qualsiasi uso.

Altre predizioni di rilievo (tutte con punteggio ≈ 0,99): discinesia linguo-facio-buccale, disturbo da tic cronico, punte-onda continue durante il sonno, malattie extrapiramidali e del movimento, attacchi di brivido benigni. Per la discinesia esiste solo letteratura indiretta (oppioidi e agitazione nella demenza, studi preclinici); per le altre non è stata trovata alcuna evidenza.

## Evidenze da studi clinici

Al momento non risulta alcuno studio clinico registrato correlato.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case report | Masui (Jpn J Anesthesiol) | Gestione anestesiologica di una paziente con porfiria acuta intermittente sottoposta a isterectomia radicale per tumore ovarico; riguarda la sicurezza perioperatoria, non l'efficacia terapeutica |

## Informazioni sul mercato italiano

Tutte le 18 autorizzazioni di buprenorfina risultano cancellate; non ve ne sono di valide. Il testo delle indicazioni approvate non è disponibile. Principali autorizzazioni (prime 5):

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 025215043 | TEMGESIC 10 compresse sublinguali 0,2 mg | Eumedica Pharmaceuticals GmbH | Cancellata |
| 025215017 | TEMGESIC 5 fiale IM/EV 0,3 mg/1 ml | Eumedica Pharmaceuticals GmbH | Cancellata |
| 035568017 | TRANSTEC 3 cerotti transdermici 20 mg, 35 mcg/ora | Grünenthal Italia Srl | Cancellata |
| 044388155 | DURLEVATEC 3 cerotti transdermici 40 mg, 70 mcg/ora | Sandoz SpA | Cancellata |
| 043426093 | BUSETTE 4 cerotti transdermici 10 mg, 10 mcg/ora | Sandoz SpA | Cancellata |

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza TxGNN, non da scheda tecnica):** il grafo riporta relazioni di controindicazione con numerose condizioni, tra cui: sindrome del QT lungo e torsioni di punta, ipotensione ortostatica, BPCO e insufficienza respiratoria, epatopatie e infezioni croniche da HBV/HCV, ipotiroidismo, insufficienza surrenalica (morbo di Addison), ileo paralitico e occlusione intestinale, ipertrofia prostatica benigna, stenosi uretrale, malattie della colecisti, ipertensione intracranica/pseudotumor cerebri, e disturbi da uso di sostanze.
- **Interazioni/farmacologia:** i dati disponibili indicano soltanto i bersagli recettoriali (recettore μ, OPRM1, e recettore κ, OPRK1), non interazioni con altri farmaci.
- **Rischio specifico per le nuove indicazioni:** gli oppioidi possono abbassare la soglia convulsiva in alcuni contesti, aspetto rilevante per un'encefalopatia epilettica come le punte-onda continue durante il sonno. Per la porfiria, la sicurezza deve essere verificata.

Per le avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (nessuno studio clinico, un unico case report non terapeutico), non esiste un razionale meccanicistico diretto e il profilo di sicurezza nella porfiria non è noto. Tutte le autorizzazioni italiane sono inoltre cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e un razionale plausibile per la porfiria acuta intermittente
- Valutazione della sicurezza della buprenorfina nella porfiria (porfirinogenicità)
- Avvertenze e controindicazioni dal foglio illustrativo AIFA
- Studi preclinici o clinici specifici sulla nuova indicazione
- Verifica della fattibilità regolatoria, dato che non esistono autorizzazioni valide in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

